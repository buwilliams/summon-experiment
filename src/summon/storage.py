"""Readable, Git-friendly records with atomic writes and recoverable multi-file saves."""
import hashlib
import json
import re
import sqlite3
import threading
from pathlib import Path

from fastapi import HTTPException


def segment(name, identity, limit=20):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:limit] or "untitled"
    suffix = hashlib.sha256(identity.encode()).hexdigest()[:8]
    return f"{slug}-{suffix}"


class FileStore:
    def __init__(self, path):
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)
        self.lock = threading.RLock()
        self.failed = False
        pending = self.path / ".pending.json"
        if pending.exists():
            self.put_many(json.loads(pending.read_text(encoding="utf-8")))
        from .cleanup import Cleanup
        self.cleanup = Cleanup(self)

    def _files(self, kind):
        if kind == "batch":
            return sorted([*self.path.glob("batches/*/batch.json"), *self.path.glob("hypotheses/**/batch.json")])
        if kind == "catalog":
            files = sorted((self.path / "catalog").glob("revision-*.json"))
            return files[-1:]
        if kind not in {"session", "submission", "report", "ballot"}:
            raise ValueError("Unknown record kind")
        extra = []
        if kind == "ballot":
            extra = list(self.path.glob("hypotheses/**/judgments/*.json"))
        elif kind == "report":
            extra = list(self.path.glob("hypotheses/**/reports/*.json"))
        return sorted(set([*self.path.glob(f"scenarios/**/{kind}.json"), *self.path.glob(f"hypotheses/**/{kind}.json"), *extra]))

    def all(self, kind):
        with self.lock:
            records = [json.loads(p.read_text(encoding="utf-8")) for p in self._files(kind)]
            return sorted(records, key=lambda r: (r.get("created", ""), r["id"]))

    def get(self, kind, id):
        with self.lock:
            for value in self.all(kind):
                if value["id"] == id:
                    return value
        raise HTTPException(404, "Record not found")

    def _path(self, kind, value):
        if kind == "catalog":
            return self.path / "catalog" / f"revision-{value['revision']:06d}.json"
        # Existing records retain their paths when labels or definitions change.
        for path in self._files(kind):
            if json.loads(path.read_text(encoding="utf-8"))["id"] == value["id"]:
                return path
        source = value["source"] if kind == "ballot" else value["submissions"][0] if kind == "report" else value
        if source.get("experiment") and source.get("hypothesis"):
            h, e = source["hypothesis"], source["experiment"]
            base = self.path / "hypotheses" / segment(h["name"], h["id"], 10) / "experiments" / segment(e["name"], e["id"], 10) / "batches"
            batch_id = source["id"] if kind == "batch" else source.get("batch_id", source["batch"])
            batch_name = source["name"] if kind == "batch" else source["batch"]
            base /= segment(batch_name, batch_id)
            if kind == "batch":
                return base / "batch.json"
            if kind == "report":
                return base / "reports" / (segment(value["name"], value["id"], 10) + ".json")
            if kind == "ballot":
                return base / "judgments" / (value["id"] + ".json")
            session_id = value["session"] if kind == "submission" else value["id"]
            return base / "tests" / segment("test", session_id) / f"{kind}.json"
        if kind == "batch":
            return self.path / "batches" / segment(value["name"], value["id"]) / "batch.json"
        if kind == "ballot":
            report = self.get("report", value["report_id"])
            return self._path("report", report).parent / "human-judgments" / value["id"] / "ballot.json"
        source = value["submissions"][0] if kind == "report" else value
        scenario = source["scenario"]
        base = self.path / "scenarios" / segment(scenario["name"], scenario["id"])
        base /= "batches"
        base /= segment(source["batch"], source["batch"])
        if kind == "report":
            return base / "reports" / segment(value["name"], value["id"]) / "report.json"
        for field in ["view", "style"]:
            base /= segment(source[field]["name"], source[field]["id"])
        session_id = value["session"] if kind == "submission" else value["id"]
        base /= segment("session", session_id)
        return base / f"{kind}.json"

    def _atomic(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        temp = path.with_suffix(path.suffix + ".tmp")
        with temp.open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
            stream.flush()
            import os
            os.fsync(stream.fileno())
        temp.replace(path)

    def put(self, kind, value):
        self.put_many([(kind, value)])
        return value

    def put_many(self, records):
        with self.lock:
            if self.failed:
                raise RuntimeError("A file save failed. Restart to recover the pending write before saving more data.")
            pending = self.path / ".pending.json"
            self._atomic(pending, json.dumps(records, ensure_ascii=False, indent=2) + "\n")
            try:
                for kind, value in records:
                    path = self._path(kind, value)
                    self._atomic(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")
                    self._atomic(path.with_suffix(".md"), self._markdown(kind, value))
                pending.unlink()
            except Exception:
                self.failed = True
                raise

    def migrate_sqlite(self, legacy):
        marker = self.path / ".sqlite-migrated"
        if not legacy.exists() or marker.exists():
            return
        connection = sqlite3.connect(legacy.resolve().as_uri() + "?mode=ro", uri=True)
        try:
            records = [(kind, json.loads(body)) for kind, body in connection.execute("SELECT kind, body FROM records ORDER BY rowid")]
        finally:
            connection.close()
        missing = []
        for kind, value in records:
            try:
                existing = self.get(kind, value["id"])
            except HTTPException:
                missing.append((kind, value))
            else:
                if existing != value:
                    raise ValueError("SQLite migration conflicts with existing flat files; original database is unchanged.")
        if missing:
            self.put_many(missing)
        for kind, value in records:
            if self.get(kind, value["id"]) != value:
                raise ValueError("Migration verification failed; original database is unchanged.")
        self._atomic(marker, "Migrated and verified. Original SQLite database retained locally.\n")

    def _markdown(self, kind, value):
        if kind == "batch":
            c = value["catalog"]
            total = len(c["scenarios"]) * sum(len(v["styles"]) for v in c["views"])
            lines = [f"# {value['name']}", "", f"Participant: {value['participant']}", "",
                     f"Created: {value['created']} · Catalog revision: {value['revision']}", "",
                     f"Planned sessions: {total}", "",
                     "The JSON file freezes the experiment, test, and style roster for this batch.",
                     "Each session stores its conversation and selected submission together.", ""]
            if value.get("experiment"):
                lines += [f"Hypothesis: {value['hypothesis']['name']}", "", f"Experiment: {value['experiment']['name']}", ""]
        elif kind == "catalog":
            lines = [f"# Experiment catalog · revision {value['revision']}", ""]
            for h in value.get("hypotheses", []):
                lines += [f"## Hypothesis: {h['name']}", "", h["statement"], ""]
                for e in value.get("experiments", []):
                    if e["hypothesis_id"] == h["id"]:
                        lines += [f"### Experiment: {e['name']}", "", e.get("text", e.get("description", "")), "",
                                  "Tests: " + ", ".join(v["name"] for v in value["views"] if v["id"] in e["view_ids"]), ""]
            for s in value.get("scenarios", []):
                lines += [f"### {s['name']}", "", s["text"], ""]
            for view in value["views"]:
                lines += [f"## {view['name']}", ""]
                for style in view["styles"]:
                    lines += [f"### {style['name']}", "", style["opening"], ""]
                    for scenario_id, opening in style.get("openings", {}).items():
                        scenario_name = next((s["name"] for s in value.get("scenarios", value.get("experiments", [])) if s["id"] == scenario_id), scenario_id)
                        lines += [f"**Opening for {scenario_name}**", "", opening, ""]
        elif kind == "ballot":
            lines = [f"# Human judgment · {value['reviewer']}", "", f"Report: {value['report_name']}", "",
                     f"Status: {value['status']} · Stage: {value['stage']}", "", f"Pair: {value['pair_key']}", "",
                     f"Response A: {value['display_order'][0]}", "", f"Response B: {value['display_order'][1]}", "",
                     "Jev scores and style labels were hidden until the preference was saved.", ""]
            if value["status"] == "complete":
                lines += [f"Preference: {value['choice']}", "", f"Judged at: {value['judged_at']}", "", value["reason"], ""]
        elif kind == "report":
            lines = [f"# {value['name']}", "", f"Status: {value['status']}", "", f"Protocol: {value['protocol']}", ""]
            labels = {s["id"]: f"{s['view']['name']} / {s['style']['name']}" for s in value["submissions"]}
            if value.get("error"):
                lines += [value["error"], ""]
            if value["status"] == "complete":
                for group, rows in [*value["rankings"].items(), ("Across tests", value["cross_ranking"])]:
                    name = next((s["view"]["name"] for s in value["submissions"] if s["view"]["id"] == group), group)
                    lines += [f"## {name}", ""]
                    for row in rows:
                        score = "Not compared" if row["score"] is None else f"{row['score']:.1%}"
                        lines += [f"- {labels[row['id']]}: {score} ({row['comparisons']} pairs)"]
                    lines += [""]
            lines += ["## Pairwise comparisons", ""]
            for pair in value["pairs"]:
                lines += [f"### {labels[pair['ids'][0]]} vs {labels[pair['ids'][1]]}", "", f"Stage: {pair['stage']} · {len(pair['orders'])}/2 orders saved", ""]
                for id, score in pair.get("scores", {}).items():
                    lines += [f"- {labels[id]}: {score:.1%}"]
                lines += [""]
        else:
            lines = [f"# {value['scenario']['name']} · {value['view']['name']} · {value['style']['name']}", "",
                     f"Participant: {value['participant']} · Batch: {value['batch']} · Revision: {value['revision']}", "",
                     f"Created: {value['created']} · Model: {value['model']}", ""]
            if kind == "session":
                lines += [f"Status: {value['status']}", "", "## Experiment", "", value["scenario"]["text"], ""]
                for i, message in enumerate(value["messages"]):
                    lines += [f"## Message {i + 1} · {message['role']}", "", message.get("content", ""), ""]
                if value.get("pending"):
                    lines += ["## Pending prompt", "", value["pending"], ""]
            else:
                lines += [f"Session: {value['session']} · Selected message index: {value['message']}", "",
                          "## Submitted solution", "", value["text"], "", "## Notes", "", value["notes"], "",
                          f"Included in future reports: {value['included']}", ""]
        return "\n".join(lines) + "\n"
