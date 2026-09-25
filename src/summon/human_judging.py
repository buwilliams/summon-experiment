"""Durable anonymous pair assignments, independent of Jev's saved scores."""
import hashlib
import secrets
from datetime import datetime, timezone
from typing import Literal

from fastapi import HTTPException
from pydantic import BaseModel, Field

from .markdown import render_markdown


class ReviewerInput(BaseModel):
    reviewer: str = Field(min_length=1, max_length=100)


class VoteInput(ReviewerInput):
    choice: Literal["A", "B", "tie"]
    reason: str = Field(default="", max_length=10000)


def reviewer_key(name):
    value = name.strip().casefold()
    if not value:
        raise ValueError("Enter a reviewer name.")
    return value


def ballot_view(ballot, report):
    subs = {s["id"]: s for s in report["submissions"]}
    result = dict(id=ballot["id"], report_id=report["id"], stage=ballot["stage"],
        reviewer=ballot["reviewer"], status=ballot["status"],
        scenario=report["submissions"][0]["scenario"],
        responses=[dict(label=label, text=subs[sid]["text"], html=render_markdown(subs[sid]["text"]))
                   for label, sid in zip(["A", "B"], ballot["display_order"])])
    if ballot["status"] == "complete":
        pair = next(p for p in report["pairs"] if p["key"] == ballot["pair_key"])
        result.update(choice=ballot["choice"], reason=ballot["reason"], judged_at=ballot["judged_at"],
            jev={label: pair["scores"][sid] for label, sid in zip(["A", "B"], ballot["display_order"])},
            identities={label: f"{subs[sid]['view']['name']} / {subs[sid]['style']['name']}"
                        for label, sid in zip(["A", "B"], ballot["display_order"])})
    return result


def human_summary(report, ballots):
    records = [b for b in ballots if b["report_id"] == report["id"] and b["status"] == "complete"]
    pairs = []
    agreement = 0
    for pair in report["pairs"]:
        votes = [b for b in records if b["pair_key"] == pair["key"]]
        if not votes:
            continue
        scores = {sid: sum(b["scores"][sid] for b in votes) / len(votes) for sid in pair["ids"]}
        pairs.append(dict(key=pair["key"], stage=pair["stage"], ids=pair["ids"], scores=scores, votes=len(votes)))
        jev_winner = max(pair["scores"], key=pair["scores"].get)
        if abs(pair["scores"][pair["ids"][0]] - pair["scores"][pair["ids"][1]]) < 1e-9:
            jev_winner = None
        agreement += sum(b["winner_id"] == jev_winner for b in votes)
    return dict(votes=len(records), judged_pairs=len(pairs), total_pairs=len(report["pairs"]),
        reviewers=len({b["reviewer_key"] for b in records}), agreement=agreement,
        pairs=pairs, records=[dict(id=b["id"], reviewer=b["reviewer"], pair_key=b["pair_key"],
            choice=b["choice"], display_order=b["display_order"], winner_id=b["winner_id"],
            reason=b["reason"], judged_at=b["judged_at"]) for b in records])


def register_human_judging(app, store, lock):
    @app.post("/api/reports/{id}/ballots")
    def assignments(id: str, data: ReviewerInput):
        with lock:
            key = reviewer_key(data.reviewer)
            report = store.get("report", id)
            if report["status"] != "complete":
                raise HTTPException(409, "Wait for Jev comparisons to finish before judging this report.")
            existing = {b["pair_key"]: b for b in store.all("ballot")
                        if b["report_id"] == id and b["reviewer_key"] == key}
            updates = []
            for pair in report["pairs"]:
                if pair["key"] in existing:
                    continue
                order = list(pair["ids"])
                secrets.SystemRandom().shuffle(order)
                bid = hashlib.sha256(f"{id}:{pair['key']}:{key}".encode()).hexdigest()[:32]
                ballot = dict(id=bid, created=datetime.now(timezone.utc).isoformat(),
                    report_id=id, report_name=report["name"], pair_key=pair["key"], stage=pair["stage"],
                    reviewer=data.reviewer.strip(), reviewer_key=key, display_order=order,
                    status="pending", protocol="anonymous-human-pairwise-v1",
                    source={k: v for k, v in report["submissions"][0].items()
                            if k in {"scenario", "batch", "batch_id", "hypothesis", "experiment"}})
                updates.append(("ballot", ballot))
                existing[pair["key"]] = ballot
            if updates:
                store.put_many(updates)
            # Persisted random order also prevents restarting to reshuffle a difficult pair.
            ordered = sorted(existing.values(), key=lambda b: (b["stage"] != "within", b["id"]))
            return dict(report_id=id, reviewer=data.reviewer.strip(), total=len(ordered),
                completed=sum(b["status"] == "complete" for b in ordered),
                ballots=[ballot_view(b, report) for b in ordered])

    @app.post("/api/ballots/{id}/vote")
    def vote(id: str, data: VoteInput):
        with lock:
            ballot = store.get("ballot", id)
            if ballot["reviewer_key"] != reviewer_key(data.reviewer):
                raise ValueError("This comparison belongs to a different reviewer.")
            report = store.get("report", ballot["report_id"])
            if ballot["status"] == "complete":
                if ballot["choice"] != data.choice or ballot["reason"] != data.reason:
                    raise HTTPException(409, "This judgment is already saved. Its original preference is preserved.")
                return ballot_view(ballot, report)
            winner = None if data.choice == "tie" else ballot["display_order"][0 if data.choice == "A" else 1]
            ballot.update(status="complete", choice=data.choice, reason=data.reason, winner_id=winner,
                scores={sid: .5 if winner is None else float(sid == winner) for sid in ballot["display_order"]},
                judged_at=datetime.now(timezone.utc).isoformat())
            store.put("ballot", ballot)
            return ballot_view(ballot, report)
