"""Local human-led experiment workspace. Historical CLI results are never imported."""
import itertools
import hashlib
import json
import math
import os
import re
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from starlette.middleware.trustedhost import TrustedHostMiddleware

ROOT = Path(__file__).resolve().parents[2]
STATIC = Path(__file__).parent / "static"
MODEL = "openai/gpt-6-astra"
JUDGE = "typesafe/jev-1.13"
STYLES = dict(zip("ABCDE", ["Plain", "Persona", "Method named", "Method enacted", "Child lens"]))


def now():
    return datetime.now(timezone.utc).isoformat()


def uid():
    return uuid.uuid4().hex


from .storage import FileStore
from .studies import with_studies, study_scope, validate_studies
from .markdown import render_markdown
from .human_judging import register_human_judging, human_summary
from .cleanup import register_cleanup


class Store(FileStore):
    def seed(self, root):
        if self.all("catalog"):
            return
        scenarios, views = [], {}
        for folder in sorted((root / "experiments").glob("[0-9][0-9][0-9]-*")):
            scenarios.append(dict(id=uid(), name=folder.name.split("-", 1)[1].replace("-", " ").title(),
                                  text=(folder / "scenario.md").read_text(encoding="utf-8").strip()))
            for lens in sorted(p for p in folder.iterdir() if p.is_dir()):
                if lens.name not in views:
                    views[lens.name] = dict(id=uid(), name=lens.name.replace("-", " ").title(), styles=[])
                styles = views[lens.name]["styles"]
                for file in sorted(lens.glob("test*.md")):
                    opening = file.read_text(encoding="utf-8").strip()
                    code = file.stem.removeprefix("test")
                    name = f"{code} · {STYLES.get(code, code)}"
                    style = next((s for s in styles if s["name"] == name), None)
                    if style is None:
                        style = dict(id=uid(), name=name, opening=opening.strip(), openings={})
                        styles.append(style)
                    style["openings"][scenarios[-1]["id"]] = opening.strip()
        self.put("catalog", with_studies(dict(id="catalog", revision=1, scenarios=scenarios, views=list(views.values()))))


def scenario_style(style, scenario):
    return {**{k: v for k, v in style.items() if k != "guidance"}, "opening": style.get("openings", {}).get(scenario["id"], style["opening"])}


class Gateway:
    def post(self, endpoint, body):
        key = os.getenv("OPENROUTER_API_KEY")
        if not key:
            raise ValueError("Add OPENROUTER_API_KEY to the local .env file and restart.")
        with httpx.Client(timeout=300) as client:
            response = client.post("https://openrouter.ai/api/" + endpoint, json=body,
                                   headers={"Authorization": f"Bearer {key}"})
        if response.status_code >= 400:
            raise ValueError(f"Provider returned HTTP {response.status_code}. Check account access, credit, and input size; retry when resolved.")
        return response.json()

    def chat(self, messages):
        raw = self.post("v1/chat/completions", dict(model=MODEL, messages=messages, max_tokens=16000,
                        reasoning={"effort": "medium"}, provider={"allow_fallbacks": False}))
        choice = raw["choices"][0]
        if choice.get("finish_reason") != "stop" or not choice["message"].get("content") or choice["message"].get("refusal"):
            raise ValueError("The model did not return a complete response. Your prompt is saved; retry it.")
        return choice["message"], raw

    def judge(self, scenario, answers):
        raw = self.post("alpha/decisions", dict(model=JUDGE, state=dict(scenario=scenario, answers=answers),
            questions={"better": dict(type="choice", instructions="Which answer do you think is better?",
                                     criteria={k: f"{k} is better." for k in answers})}))
        probs = raw.get("answers", {}).get("better", {}).get("probabilities", {})
        if set(probs) != set(answers) or any(isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not 0 <= p <= 1 for p in probs.values()) or abs(sum(probs.values()) - 1) > .01:
            raise ValueError("Jev returned invalid probabilities. Retry the report.")
        return probs, raw


class SessionInput(BaseModel):
    scenario: str
    view: str
    style: str
    participant: str = Field(min_length=1, max_length=100)
    batch: str = Field(min_length=1, max_length=100)
    experiment_id: str | None = None


class PromptInput(BaseModel):
    text: str = Field(min_length=1, max_length=100000)


class SubmissionInput(BaseModel):
    message: int = Field(ge=0)
    notes: str = Field(default="", max_length=10000)


class ReportInput(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    submissions: list[str] = Field(min_length=2)


def ranking(ids, pairs):
    rows = []
    for id in ids:
        scores = [p["scores"][id] for p in pairs if id in p.get("scores", {})]
        rows.append(dict(id=id, score=sum(scores) / len(scores) if scores else None, comparisons=len(scores)))
    return sorted(rows, key=lambda x: -(x["score"] if x["score"] is not None else -1))


def create_app(data_path=None, gateway=None):
    load_dotenv(ROOT / ".env")
    store = Store(data_path or ROOT / "experiment-data")
    if data_path is None:
        store.migrate_sqlite(ROOT / "data" / "summon.sqlite3")
    store.seed(ROOT)
    current_catalog = store.get("catalog", "catalog")
    if current_catalog.get("schema_version") != 2 or any("guidance" in s for v in current_catalog["views"] for s in v["styles"]):
        upgraded = with_studies(current_catalog)
        upgraded["revision"] += 1
        store.put("catalog", upgraded)
    gateway = gateway or Gateway()
    app = FastAPI(title="Summon")
    app.state.store = store
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "testserver"])
    lock = threading.RLock()
    busy = set()
    register_human_judging(app, store, lock)
    # A stopped process leaves durable work that can be explicitly resumed.
    for report in store.all("report"):
        if report["status"] == "running":
            report.update(status="interrupted", error="Server stopped. Resume to continue saved comparisons.")
            store.put("report", report)

    @app.middleware("http")
    async def same_origin(request: Request, call_next):
        origin = request.headers.get("origin")
        if request.method != "GET" and origin and origin != str(request.base_url).rstrip("/"):
            return JSONResponse({"detail": "Cross-origin writes are disabled."}, status_code=403)
        return await call_next(request)

    @app.exception_handler(ValueError)
    async def invalid(request, exc):
        return JSONResponse({"detail": str(exc)}, status_code=400)

    @app.get("/api/state")
    def state():
        batch_list = batches()
        sessions = store.all("session")
        for session in sessions:
            for message in session["messages"]:
                message["html"] = render_markdown(message.get("content", ""))
        reports = store.all("report")
        ballots = store.all("ballot")
        for report in reports:
            report["human"] = human_summary(report, ballots)
        return dict(catalog=store.get("catalog", "catalog"), sessions=sessions,
                    submissions=store.all("submission"), reports=reports, batches=batch_list,
                    model=MODEL, connected=bool(os.getenv("OPENROUTER_API_KEY")))

    @app.put("/api/catalog")
    def catalog(data: dict):
        with lock:
            old = store.get("catalog", "catalog")
            if data.get("revision") != old["revision"]:
                raise HTTPException(409, "Catalog changed. Reload before editing.")
            ids = set()
            def validate(record, fields):
                for field in ["id", *fields]:
                    if not isinstance(record.get(field), str) or not record[field].strip():
                        raise ValueError(f"{field} is required.")
                if record["id"] in ids:
                    raise ValueError("Duplicate catalog ID")
                ids.add(record["id"])
            if data.get("schema_version") != 2:
                raise ValueError("Definitions have changed. Reload to edit experiments.")
            if not data.get("views"):
                raise ValueError("Keep at least one test.")
            for v in data["views"]:
                validate(v, ["name"])
                if not v.get("styles"):
                    raise ValueError("Each test needs a style.")
                for s in v["styles"]:
                    validate(s, ["name", "opening"])
                    openings = s.get("openings", {})
                    if not isinstance(openings, dict) or any(
                        not isinstance(key, str) or not key or not isinstance(text, str) or not text.strip()
                        for key, text in openings.items()
                    ):
                        raise ValueError("Style openings must use experiment IDs and contain text.")
                    s.pop("guidance", None)
            data = with_studies(data)
            validate_studies(data, validate)
            return store.put("catalog", dict(id="catalog", revision=old["revision"] + 1,
                schema_version=2, views=data["views"], hypotheses=data["hypotheses"], experiments=data["experiments"]))

    @app.post("/api/sessions")
    def new_session(data: SessionInput):
        c, experiment, hypothesis = study_scope(store.get("catalog", "catalog"), data.experiment_id)
        def find(items, id):
            match = next((x for x in items if x["id"] == id), None)
            if not match:
                raise ValueError("Choose an existing experiment, test, and style.")
            return match
        scenario = find(c["scenarios"], data.scenario)
        view = find(c["views"], data.view)
        style = scenario_style(find(view["styles"], data.style), scenario)
        return store.put("session", dict(id=uid(), created=now(), revision=c["revision"], scenario=scenario,
            view=dict(id=view["id"], name=view["name"]), style=style, participant=data.participant.strip(),
            batch=data.batch.strip(), experiment=experiment, hypothesis=hypothesis, model=MODEL, style_roster=view["styles"], messages=[], calls=[], status="open", pending=None))

    def batch_key(participant, revision, name):
        return hashlib.sha256(json.dumps([participant, revision, name]).encode()).hexdigest()[:24]

    def session_batch(s):
        return s.get("batch_id") or batch_key(s["participant"], s["revision"], s["batch"])

    def dated_batch_name(created, names):
        date = datetime.fromisoformat(created).astimezone().strftime("%Y%m%d")
        prefix = f"Batch {date}-"
        revisions = [int(name[len(prefix):]) for name in names
                     if name.startswith(prefix) and name[len(prefix):].isdigit()]
        return prefix + str(max(revisions, default=0) + 1)

    def ensure_batches():
        existing = {b["id"] for b in store.all("batch")}
        for s in store.all("session"):
            id = session_batch(s)
            if id in existing:
                continue
            path = store.path / "catalog" / f"revision-{s['revision']:06d}.json"
            if not path.exists():
                raise ValueError("The catalog revision for this older batch is missing; restore it before continuing.")
            c = json.loads(path.read_text(encoding="utf-8"))
            experiment = s.get("experiment")
            c, default_experiment, hypothesis = study_scope(c, experiment["id"] if experiment else None)
            experiment = experiment or default_experiment
            store.put("batch", dict(id=id, name=s["batch"], participant=s["participant"],
                revision=s["revision"], created=s["created"], catalog=c, experiment=experiment, hypothesis=s.get("hypothesis", hypothesis)))
            existing.add(id)
        # Stable IDs keep links intact when legacy labels are standardized.
        saved = store.all("batch")
        names = {b["name"] for b in saved}
        for batch in saved:
            updates = []
            if "experiment" not in batch:
                _, experiment, hypothesis = study_scope(batch["catalog"])
                batch.update(experiment=experiment, hypothesis=hypothesis)
                updates.append(("batch", batch))
            if not re.fullmatch(r"Batch \d{8}-[1-9]\d*", batch["name"]):
                batch["previous_name"] = batch["name"]
                batch["name"] = dated_batch_name(batch["created"], names)
                names.add(batch["name"])
                updates.append(("batch", batch))
            for kind in ["session", "submission"]:
                for record in store.all(kind):
                    if session_batch(record) == batch["id"] and (record["batch"] != batch["name"] or not record.get("batch_id") or not record.get("experiment")):
                        record.update(batch=batch["name"], batch_id=batch["id"], experiment=batch["experiment"], hypothesis=batch["hypothesis"])
                        updates.append((kind, record))
            if updates:
                store.put_many(updates)

    def batch_progress(batch):
        sessions = [s for s in store.all("session") if session_batch(s) == batch["id"]]
        latest = {}
        for s in sessions:
            latest[(s["scenario"]["id"], s["view"]["id"], s["style"]["id"])] = s
        c = batch["catalog"]
        total = len(c["scenarios"]) * sum(len(v["styles"]) for v in c["views"])
        return dict(**batch, total=total, completed=sum(s["status"] == "submitted" for s in latest.values()),
                    in_progress=sum(s["status"] == "open" for s in latest.values()),
                    interviews=[dict(id=s["id"], scenario=s["scenario"]["name"], view=s["view"]["name"],
                                     style=s["style"]["name"], status=s["status"], revises=s.get("revises")) for s in latest.values()],
                    session_ids=[s["id"] for s in sessions])

    @app.get("/api/batches")
    def batches():
        with lock:
            ensure_batches()
            return [batch_progress(b) for b in store.all("batch")]

    @app.post("/api/batches")
    def new_batch(experiment_id: str | None = None):
        with lock:
            ensure_batches()
            sessions = store.all("session")
            participant = os.getenv("SUMMON_PARTICIPANT") or (sessions[-1]["participant"] if sessions else "Local participant")
            c, experiment, hypothesis = study_scope(store.get("catalog", "catalog"), experiment_id)
            names = {b["name"] for b in store.all("batch")}
            names.update(r["value"]["name"] for a in store.cleanup.archives() for r in a["records"] if r["kind"] == "batch")
            name = dated_batch_name(now(), names)
            return store.put("batch", dict(id=batch_key(participant, c["revision"], name), name=name,
                participant=participant, revision=c["revision"], created=now(), catalog=c, experiment=experiment, hypothesis=hypothesis))

    def choose_interview(batch_id: str | None = None):
        """Resume only within the selected batch; its frozen roster defines progress."""
        with lock:
            ensure_batches()
            available = store.all("batch")
            batch = store.get("batch", batch_id) if batch_id else (available[-1] if available else new_batch())
            progress = batch_progress(batch)
            sessions = [store.get("session", i["id"]) for i in progress["interviews"]]
            opened = [s for s in sessions if s["status"] == "open"]
            if opened:
                return opened[-1]
            c = batch["catalog"]
            collected = {(s["scenario"]["id"], s["view"]["id"], s["style"]["id"]) for s in sessions}
            candidates = [(scenario, view, style) for scenario in c["scenarios"]
                          for view in c["views"] for style in view["styles"]
                          if (scenario["id"], view["id"], style["id"]) not in collected]
            if not candidates:
                return dict(complete=True, batch_id=batch["id"])
            def order(cell):
                return hashlib.sha256((batch["id"] + ":".join(x["id"] for x in cell)).encode()).hexdigest()
            scenario, view, style = min(candidates, key=order)
            style = scenario_style(style, scenario)
            return store.put("session", dict(id=uid(), created=now(), revision=batch["revision"], scenario=scenario,
                view=dict(id=view["id"], name=view["name"]), style=style, participant=batch["participant"],
                batch=batch["name"], batch_id=batch["id"], experiment=batch["experiment"], hypothesis=batch["hypothesis"], model=MODEL, style_roster=view["styles"], messages=[], calls=[], status="open", pending=None,
                assignment=dict(method="batch-shuffled-v2", batch_id=batch["id"])))

    @app.post("/api/interview/next")
    def next_interview(batch_id: str | None = None):
        session = choose_interview(batch_id)
        if session.get("complete") or session["messages"]:
            return session
        return opening(session["id"])

    @app.post("/api/sessions/{id}/opening")
    def opening(id: str):
        with lock:
            session = store.get("session", id)
            if id in busy:
                raise HTTPException(409, "The initial recommendation is already being generated.")
            if session["messages"]:
                return session
            if session["status"] != "open":
                raise HTTPException(409, "This interview is already submitted.")
            style_text = session["style"]["opening"].replace("{{SCENARIO}}", "").replace("{{EXPERIMENT}}", "").strip()
            prompt = (f"Experiment:\n{session['scenario']['text']}\n\n"
                      f"Test:\n{session['view']['name']}\n\n"
                      f"Style:\n{session['style']['name']}\n{style_text}\n\n"
                      "Provide a recommendation for this experiment and explain the reasons behind it.")
            session["initial_prompt"] = prompt
            session["collection_protocol"] = "automatic-opening-v1"
            store.put("session", session)
        return chat(id, PromptInput(text=prompt))

    @app.post("/api/sessions/{id}/revise")
    def revise(id: str):
        with lock:
            source = store.get("session", id)
            if id in busy:
                raise HTTPException(409, "Wait for the current response before revising.")
            if source["status"] == "open":
                return source
            # Return an existing revision rather than creating parallel edit branches.
            family = [s for s in store.all("session") if session_batch(s) == session_batch(source)
                      and all(s[k]["id"] == source[k]["id"] for k in ["scenario", "view", "style"])]
            latest = family[-1]
            if latest["status"] == "open":
                return latest
            draft = dict(latest, id=uid(), created=now(), status="open", pending=None, revises=latest["id"])
            draft.pop("submission", None)
            draft.pop("error", None)
            return store.put("session", draft)

    @app.post("/api/sessions/{id}/messages")
    def chat(id: str, data: PromptInput):
        if not data.text.strip():
            raise ValueError("Enter a prompt.")
        with lock:
            session = store.get("session", id)
            if id in busy or session["status"] != "open":
                raise HTTPException(409, "Session is busy or already submitted.")
            busy.add(id)
            session["pending"] = data.text
            session.pop("error", None)
            store.put("session", session)
        try:
            message = dict(role="user", content=data.text)
            # Scenario is included once, as user context, with no hidden style or system prompt.
            messages = session["messages"] + [message]
            context = dict(role="user", content="Experiment:\n" + session["scenario"]["text"])
            # Automatic openings already contain the scenario, view, and style.
            answer, raw = gateway.chat(messages if session.get("initial_prompt") else [context, *messages])
            session["messages"] = messages + [answer]
            session["calls"].append(dict(at=now(), raw=raw))
            session["pending"] = None
            return store.put("session", session)
        except Exception as exc:
            session["error"] = str(exc) if isinstance(exc, ValueError) else "Request failed. Prompt saved; retry when ready."
            store.put("session", session)
            raise ValueError(session["error"])
        finally:
            with lock:
                busy.discard(id)

    @app.post("/api/sessions/{id}/submit")
    def submit(id: str, data: SubmissionInput):
        with lock:
            s = store.get("session", id)
            if id in busy or s["status"] != "open":
                raise HTTPException(409, "Session is busy or submitted.")
            if data.message >= len(s["messages"]) or s["messages"][data.message]["role"] != "assistant":
                raise ValueError("Select an assistant response.")
            sub = dict(id=uid(), session=id, created=now(), revision=s["revision"], scenario=s["scenario"],
                       view=s["view"], style=s["style"], participant=s["participant"], batch=s["batch"],
                       model=s["model"], message=data.message, text=s["messages"][data.message]["content"],
                       notes=data.notes, included=True, turns=(data.message + 1) // 2, batch_id=session_batch(s))
            for field in ["experiment", "hypothesis"]:
                if field in s:
                    sub[field] = s[field]
            # Journal both writes so restart completes an interrupted submission.
            s.update(status="submitted", submission=sub["id"])
            updates = [("submission", sub), ("session", s)]
            if s.get("revises"):
                previous = store.get("session", s["revises"])
                if previous.get("submission"):
                    old = store.get("submission", previous["submission"])
                    old.update(included=False, superseded_by=sub["id"])
                    sub["replaces"] = old["id"]
                    updates.append(("submission", old))
            store.put_many(updates)
            return sub

    @app.patch("/api/submissions/{id}")
    def edit_submission(id: str, data: dict):
        with lock:
            s = store.get("submission", id)
            if not isinstance(data.get("notes", ""), str) or not isinstance(data.get("included", True), bool):
                raise ValueError("Invalid submission metadata.")
            s.update(notes=data.get("notes", s["notes"]), included=data.get("included", s["included"]))
            return store.put("submission", s)

    def run_report(id):
        report = store.get("report", id)
        try:
            def compare(a, b, stage):
                key = ":".join([stage, *sorted([a["id"], b["id"]])])
                pair = next((p for p in report["pairs"] if p["key"] == key), None)
                if pair is None:
                    pair = dict(key=key, stage=stage, ids=[a["id"], b["id"]], orders=[])
                    report["pairs"].append(pair)
                for order in [[a, b], [b, a]][len(pair["orders"]):]:
                    probs, raw = gateway.judge(a["scenario"]["text"], {f"answer_{i+1}": s["text"] for i, s in enumerate(order)})
                    pair["orders"].append(dict(mapping={f"answer_{i+1}": s["id"] for i, s in enumerate(order)},
                                               probabilities=probs, raw=raw, at=now()))
                    store.put("report", report)
                scores = {a["id"]: 0., b["id"]: 0.}
                for result in pair["orders"]:
                    for aid, sid in result["mapping"].items():
                        scores[sid] += result["probabilities"][aid] / 2
                pair["scores"] = scores
                pair["order_gap"] = abs(pair["orders"][0]["probabilities"]["answer_1"] - pair["orders"][1]["probabilities"]["answer_2"])
                store.put("report", report)
            groups = {}
            for s in report["submissions"]:
                groups.setdefault(s["view"]["id"], []).append(s)
            winners = []
            report["rankings"] = {}
            for view, subs in groups.items():
                for a, b in itertools.combinations(subs, 2):
                    compare(a, b, "within")
                rows = ranking([s["id"] for s in subs], [p for p in report["pairs"] if p["stage"] == "within"])
                report["rankings"][view] = rows
                best = rows[0]["score"]
                # Exact ties advance together; no arbitrary winner.
                winners.extend(s for s in subs if any(r["id"] == s["id"] and abs(r["score"] - best) < 1e-9 for r in rows))
            for a, b in itertools.combinations(winners, 2):
                if a["view"]["id"] != b["view"]["id"]:
                    compare(a, b, "cross")
            report["cross_ranking"] = ranking([s["id"] for s in winners], [p for p in report["pairs"] if p["stage"] == "cross"])
            report.update(status="complete", finished=now(), error=None)
        except Exception as exc:
            report.update(status="failed", error=str(exc) if isinstance(exc, ValueError) else "Comparison failed. Resume to retry unfinished work.")
        finally:
            store.put("report", report)
            with lock:
                busy.discard(id)

    def launch(report):
        with lock:
            if report["id"] in busy:
                raise HTTPException(409, "Report is already running.")
            busy.add(report["id"])
            report.update(status="running", error=None)
            store.put("report", report)
            threading.Thread(target=run_report, args=(report["id"],), daemon=True).start()
        return report

    def prepare_report(data: ReportInput):
        if len(set(data.submissions)) != len(data.submissions):
            raise ValueError("Duplicate submissions selected.")
        subs = [store.get("submission", id) for id in data.submissions]
        if any(not s["included"] for s in subs):
            raise ValueError("An excluded submission was selected.")
        for field in ["revision", "batch", "model", "participant"]:
            if len({s[field] for s in subs}) != 1:
                raise ValueError(f"Use the same {field} for a matched report.")
        for field in ["experiment", "hypothesis"]:
            if len({json.dumps(s.get(field), sort_keys=True) for s in subs}) != 1:
                raise ValueError(f"Use the same {field} for a matched report.")
        if len({json.dumps(s["scenario"], sort_keys=True) for s in subs}) != 1:
            raise ValueError("Compare submissions from the same experiment revision.")
        cells = [(s["view"]["id"], s["style"]["id"]) for s in subs]
        if len(set(cells)) != len(cells):
            raise ValueError("Select one submission per test/style. Use separate batches for repeats.")
        c = store.get("catalog", "catalog")
        # Require the complete style roster frozen at session creation (stored below).
        groups = {}
        for s in subs:
            groups.setdefault(s["view"]["id"], []).append(s)
        for view, group in groups.items():
            session = store.get("session", group[0]["session"])
            roster = session.get("style_roster")
            if roster is None:
                roster = next((v["styles"] for v in c["views"] if v["id"] == view), [])
            if len(group) < 2 or {s["style"]["id"] for s in group} != {s["id"] for s in roster}:
                raise ValueError("Each selected test needs one submission for every style before ranking.")
        return dict(id=uid(), name=data.name, created=now(), status="queued", submissions=subs,
                    pairs=[], rankings={}, cross_ranking=[], judge_model=JUDGE, protocol="human-pairwise-v1",
                    experiment=subs[0].get("experiment"), hypothesis=subs[0].get("hypothesis"))

    @app.post("/api/reports")
    def report(data: ReportInput):
        return launch(prepare_report(data))

    @app.post("/api/batches/{id}/reports")
    def report_batch(id: str):
        with lock:
            ensure_batches()
            batch = store.get("batch", id)
            progress = batch_progress(batch)
            if not progress["total"] or progress["completed"] != progress["total"]:
                raise ValueError(f"Complete this batch before running: {progress['completed']} of {progress['total']} interviews submitted.")
            grouped = {}
            for interview in progress["interviews"]:
                session = store.get("session", interview["id"])
                sub = store.get("submission", session["submission"])
                if not sub["included"]:
                    raise ValueError("This batch contains an excluded submission. Include or revise it before running.")
                grouped.setdefault(sub["scenario"]["id"], []).append(sub)
            # Validate every scenario before starting any paid work.
            prepared = []
            for subs in grouped.values():
                data = ReportInput(name=f"{batch['name']} · {subs[0]['scenario']['name']}", submissions=[s["id"] for s in subs])
                result = prepare_report(data)
                result["batch_id"] = id
                prepared.append(result)
            if any(r.get("batch_id") == id and r["status"] == "running" for r in store.all("report")):
                raise HTTPException(409, "Reports for this batch are already running.")
            return [launch(result) for result in prepared]

    @app.post("/api/reports/{id}/resume")
    def resume(id: str):
        report = store.get("report", id)
        if report["status"] == "complete":
            raise HTTPException(409, "Report is already complete.")
        return launch(report)

    @app.get("/api/export")
    def export():
        return JSONResponse({**state(), "human_judgments": store.all("ballot")}, headers={"Content-Disposition": 'attachment; filename="summon-export.json"'})

    @app.get("/")
    def index():
        return FileResponse(STATIC / "index.html")

    register_cleanup(app, store, lock, busy, ensure_batches)
    app.mount("/static", StaticFiles(directory=STATIC), name="static")
    return app


def main():
    import uvicorn
    uvicorn.run(create_app(), host="127.0.0.1", port=int(os.getenv("SUMMON_PORT", "8765")))


if __name__ == "__main__":
    main()
