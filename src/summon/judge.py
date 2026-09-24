"""Jev preference scores (spec §6): A–E within each lens, and D across lenses."""

import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import httpx

from . import (
    CROSS_LENS_TEST, LENSES, RESULTS, SCENARIOS, TESTS, Fatal, log, read_json,
    require_env, result_path, scenario_text, with_retries, write_json,
)

ENDPOINT = "https://openrouter.ai/api/alpha/decisions"
QUESTION = "Which answer do you think is better?"
CROSS_LENS = "cross-lens"


def judgment_path(scenario, group):
    """group is a lens name, or CROSS_LENS for the D-vs-D comparison."""
    return RESULTS / scenario / group / "judgment.json"


def call_jev(http, body, label):
    def call():
        r = http.post(ENDPOINT, json=body)
        if r.status_code in (400, 401, 402, 403, 404):
            raise Fatal(f"HTTP {r.status_code}: {r.text[:500]}")
        r.raise_for_status()
        data = r.json()
        probs = (data.get("answers") or {}).get("better", {}).get("probabilities")
        expected = set(body["questions"]["better"]["criteria"])
        if not isinstance(probs, dict) or set(probs) != expected:
            raise ValueError(f"probabilities missing or incomplete: {probs!r}")
        if abs(sum(float(p) for p in probs.values()) - 1) > 0.01:
            raise ValueError(f"probabilities don't sum to 1: {probs!r}")
        return data

    return with_retries(call, label=label)


def judge(http, cfg, scenario, options, seed_key, label):
    """Ask Jev which of `options` ({key: summary}) is better, shown in a seeded random order
    under anonymous IDs. Returns the judgment record with a score per key."""
    order = sorted(options)
    random.Random(f"{cfg['seed']}:{seed_key}").shuffle(order)
    ids = {f"answer_{i}": key for i, key in enumerate(order, 1)}
    body = {
        "model": cfg["judge_model"],
        "state": {
            "scenario": scenario_text(scenario),
            "answers": {aid: options[key] for aid, key in ids.items()},
        },
        "questions": {
            "better": {
                "type": "choice",
                "instructions": QUESTION,
                "criteria": {aid: f"{aid} is better." for aid in ids},
            }
        },
    }
    data = call_jev(http, body, label)
    answer = data["answers"]["better"]
    scores = {ids[aid]: float(p) for aid, p in answer["probabilities"].items()}
    return {
        "scenario": scenario,
        "judge_model": cfg["judge_model"],
        "question": QUESTION,
        "display_order": order,
        "id_to_option": ids,
        "scores": {k: scores[k] for k in sorted(scores)},
        "top_choice": ids.get(answer.get("choice")),
        "confidence": answer.get("confidence"),
        "judged_at": datetime.now(timezone.utc).isoformat(),
        "raw_response": data,
    }


def jobs(lenses):
    """Yield (label, output path, scenario, options-or-missing, seed_key) for every judgment."""
    for s in SCENARIOS:
        for lens in lenses:
            paths = {t: result_path(s, lens, t) for t in TESTS}
            yield (f"{s}/{lens}", judgment_path(s, lens), s, paths, f"{lens}:{s}")
        if len(lenses) > 1:
            paths = {l: result_path(s, l, CROSS_LENS_TEST) for l in lenses}
            yield (f"{s}/{CROSS_LENS}", judgment_path(s, CROSS_LENS), s, paths, f"{CROSS_LENS}:{s}")


def score_one(http, cfg, label, out, scenario, paths, seed_key):
    options = {k: read_json(p)["summary"] for k, p in paths.items()}
    j = judge(http, cfg, scenario, options, seed_key, label)
    write_json(out, j)
    return j


def main(cfg, lenses=None):
    key = require_env("OPENROUTER_API_KEY")
    http = httpx.Client(headers={"Authorization": f"Bearer {key}"}, timeout=120)
    todo = []
    for label, out, scenario, paths, seed_key in jobs(lenses or LENSES):
        if out.exists():
            log(f"{label}: done, skipping")
            continue
        missing = [k for k, p in paths.items() if not p.exists()]
        if missing:
            log(f"{label}: waiting on {', '.join(missing)}; skipping")
            continue
        todo.append((label, out, scenario, paths, seed_key))

    failed = []
    with ThreadPoolExecutor(max_workers=cfg.get("concurrency", 8)) as pool:
        futures = {pool.submit(score_one, http, cfg, *job): job[0] for job in todo}
        for f in as_completed(futures):
            label = futures[f]
            try:
                j = f.result()
            except Exception as e:
                failed.append(label)
                log(f"{label}: FAILED: {type(e).__name__}: {e}")
                continue
            ranked = sorted(j["scores"].items(), key=lambda kv: -kv[1])
            log(f"{label}: " + "  ".join(f"{k} {p:.2f}" for k, p in ranked))
    if failed:
        log(f"\n{len(failed)} judgment(s) failed; run `summon score` again to retry them.")
