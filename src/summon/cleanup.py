"""Previewed, recoverable cleanup of collected data, never catalog definitions."""
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from fastapi import HTTPException
from pydantic import BaseModel

KINDS = ("batch", "session", "submission", "report", "ballot")


class CleanupInput(BaseModel):
    scope: Literal["all", "experiment", "batch", "test", "report", "judgments"]
    id: str | None = None
    fingerprint: str | None = None


class Cleanup:
    def __init__(self, store):
        self.store = store
        self.root = store.path.resolve()
        self.trash = self.root.parent / ("." + self.root.name + "-trash")
        # Each archive is also a durable operation journal. Complete interrupted work.
        for archive in self.archives():
            if archive["status"] in {"removing", "restoring"}:
                self.finish(archive)

    def archives(self):
        return sorted((json.loads(p.read_text(encoding="utf-8")) for p in self.trash.glob("*.json")), key=lambda a: (a["created"], a["id"]))

    def save(self, archive):
        if not isinstance(archive.get("id"), str) or not all(c in "0123456789abcdef" for c in archive["id"]) or len(archive["id"]) != 32:
            raise ValueError("Invalid cleanup archive ID.")
        self.store._atomic(self.trash / (archive["id"] + ".json"), json.dumps(archive, ensure_ascii=False, indent=2) + "\n")

    def checked_path(self, relative):
        path = (self.root / relative).resolve()
        if not path.is_relative_to(self.root) or path == self.root or path.suffix not in {".json", ".md"}:
            raise ValueError("Cleanup archive contains an invalid path.")
        if path.relative_to(self.root).parts[0] not in {"batches", "scenarios", "hypotheses"}:
            raise ValueError("Cleanup cannot modify definitions or configuration.")
        return path

    def finish(self, archive):
        restoring = archive["status"] == "restoring"
        files = [(self.checked_path(f["path"]), f["text"]) for f in archive["files"]]
        # Never overwrite a changed file, even during restart recovery.
        for path, text in files:
            if path.exists() and path.read_bytes() != text.encode("utf-8"):
                raise ValueError("A file changed since cleanup. Restore requires resolving the conflicting record first.")
        try:
            for path, text in files:
                if restoring:
                    self.store._atomic(path, text)
                else:
                    path.unlink(missing_ok=True)
            archive["status"] = "restored" if restoring else "trashed"
            archive["updated"] = datetime.now(timezone.utc).isoformat()
            self.save(archive)
        except Exception:
            self.store.failed = True
            raise

    def selection(self, data):
        records = {kind: self.store.all(kind) for kind in KINDS}
        chosen = {kind: [] for kind in KINDS}
        if data.scope == "all":
            return records, "All collected data"
        if data.scope == "judgments":
            chosen["ballot"] = records["ballot"]
            return chosen, "All human judgments"
        if not data.id:
            raise ValueError("Choose a record to clean up.")
        if data.scope == "experiment":
            c = self.store.get("catalog", "catalog")
            e = next((e for e in c["experiments"] if e["id"] == data.id), None)
            if not e:
                raise ValueError("Experiment not found.")
            chosen["batch"] = [b for b in records["batch"] if b.get("experiment", {}).get("id") == data.id]
            title = "Collected data for " + e["name"]
        elif data.scope == "batch":
            chosen["batch"] = [self.store.get("batch", data.id)]
            title = chosen["batch"][0]["name"]
        elif data.scope == "test":
            test = self.store.get("session", data.id)
            # Remove the complete revision family so an older answer cannot reappear.
            chosen["session"] = [s for s in records["session"] if s.get("batch_id") == test.get("batch_id")
                and all(s[k]["id"] == test[k]["id"] for k in ["scenario", "view", "style"])]
            title = f"Session: {test['scenario']['name']} / {test['view']['name']} / {test['style']['name']}"
        else:
            chosen["report"] = [self.store.get("report", data.id)]
            title = chosen["report"][0]["name"]
        batch_ids = {b["id"] for b in chosen["batch"]}
        if batch_ids:
            chosen["session"] = [s for s in records["session"] if s.get("batch_id") in batch_ids]
        session_ids = {s["id"] for s in chosen["session"]}
        chosen["submission"] = [s for s in records["submission"] if s["session"] in session_ids]
        if data.scope != "report":
            chosen["report"] = [r for r in records["report"] if r.get("batch_id") in batch_ids
                or any(s["session"] in session_ids for s in r["submissions"])]
        report_ids = {r["id"] for r in chosen["report"]}
        chosen["ballot"] = [b for b in records["ballot"] if b["report_id"] in report_ids]
        return chosen, title

    def plan(self, data):
        chosen, title = self.selection(data)
        files, identities = [], []
        for kind, records in chosen.items():
            for record in records:
                identities.append(dict(kind=kind, id=record["id"], value=record))
                path = self.store._path(kind, record)
                for file in [path, path.with_suffix(".md")]:
                    if file.exists():
                        relative = file.resolve().relative_to(self.root).as_posix()
                        self.checked_path(relative)
                        files.append(dict(path=relative, text=file.read_bytes().decode("utf-8")))
        fingerprint = hashlib.sha256(json.dumps(files, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        return dict(title=title, counts={k: len(v) for k, v in chosen.items()},
                    fingerprint=fingerprint, files=files, records=identities)

    def remove(self, data):
        plan = self.plan(data)
        if data.fingerprint != plan["fingerprint"]:
            raise HTTPException(409, "The data changed. Review a fresh cleanup preview before continuing.")
        if not plan["files"]:
            raise ValueError("There is no collected data in this selection.")
        archive = dict(**plan, id=uuid.uuid4().hex, created=datetime.now(timezone.utc).isoformat(), status="removing")
        # The complete verified snapshot is durable before any live file is removed.
        try:
            self.save(archive)
            saved = json.loads((self.trash / (archive["id"] + ".json")).read_text(encoding="utf-8"))
            if saved != archive:
                raise ValueError("Cleanup backup verification failed; live records were not removed.")
            self.finish(archive)
        except Exception:
            self.store.failed = True
            raise
        return self.summary(archive)

    def restore(self, id):
        archive = next((a for a in self.archives() if a["id"] == id), None)
        if not archive:
            raise HTTPException(404, "Cleanup archive not found.")
        if archive["status"] == "restored":
            return self.summary(archive)
        active = {k: {r["id"]: r for r in self.store.all(k)} for k in KINDS}
        saved = {k: {r["id"]: r["value"] for r in archive["records"] if r["kind"] == k} for k in KINDS}
        for record in archive["records"]:
            current = active[record["kind"]].get(record["id"])
            if current is not None and current != record["value"]:
                raise HTTPException(409, "A newer record uses this ID. Move the conflicting data to trash before restoring.")
        # Restoring a report alone requires its original tests and responses to exist.
        available = {k: set(active[k]) | set(saved[k]) for k in KINDS}
        for kind, values in saved.items():
            for r in values.values():
                refs = []
                if kind == "session":
                    refs = [("batch", r.get("batch_id"))]
                elif kind == "submission":
                    refs = [("session", r["session"])]
                elif kind == "report":
                    refs = [("submission", s["id"]) for s in r["submissions"]]
                elif kind == "ballot":
                    refs = [("report", r["report_id"])]
                if any(id and id not in available[parent] for parent, id in refs):
                    raise HTTPException(409, "Restore the parent batch, sessions, or report first.")
        for f in archive["files"]:
            path = self.checked_path(f["path"])
            if path.exists() and path.read_bytes() != f["text"].encode("utf-8"):
                raise HTTPException(409, "A file at the original location has changed. Restore will not overwrite it.")
        archive["status"] = "restoring"
        self.save(archive)
        self.finish(archive)
        return self.summary(archive)

    @staticmethod
    def summary(archive):
        return {k: archive[k] for k in ["id", "title", "counts", "created", "status"]}


def register_cleanup(app, store, lock, busy, ensure_batches):
    manager = store.cleanup

    def idle():
        if busy:
            raise HTTPException(409, "Wait for current model requests and reports to finish before managing data.")
        if store.failed:
            raise HTTPException(409, "Restart to recover an interrupted file operation first.")

    @app.get("/api/data")
    def inventory():
        with lock, store.lock:
            ensure_batches()
            return dict(counts={k: len(store.all(k)) for k in KINDS},
                trash=[manager.summary(a) for a in reversed(manager.archives()) if a["status"] != "restored"], busy=bool(busy))

    @app.post("/api/data/preview")
    def preview(data: CleanupInput):
        with lock, store.lock:
            idle()
            ensure_batches()
            plan = manager.plan(data)
            return {k: plan[k] for k in ["title", "counts", "fingerprint"]}

    @app.post("/api/data/cleanup")
    def cleanup(data: CleanupInput):
        with lock, store.lock:
            idle()
            ensure_batches()
            return manager.remove(data)

    @app.post("/api/data/trash/{id}/restore")
    def restore(id: str):
        with lock, store.lock:
            idle()
            return manager.restore(id)
