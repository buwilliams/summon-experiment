"""Write scores.csv and report.md (spec §7)."""

import csv

from . import CROSS_LENS_TEST, LENSES, RESULTS, SCENARIOS, TESTS, read_json
from .judge import CROSS_LENS, judgment_path


def ranks(scores):
    """Competition ranking, higher first; equal scores share a rank."""
    return {k: 1 + sum(1 for other in scores.values() if other > s) for k, s in scores.items()}


def mean_scores(judgments, keys):
    return {k: sum(j["scores"][k] for j in judgments) / len(judgments) for k in keys}


def name(key):
    """testD -> D; lens names stay as they are."""
    return key[-1] if key in TESTS else key


def table(scores, header, note=""):
    r = ranks(scores)
    lines = [f"| Rank | {header} | Preference score |", "|---|---|---|"]
    for k in sorted(scores, key=lambda k: (r[k], k)):
        lines.append(f"| {r[k]} | {name(k)} | {scores[k]:.3f} |")
    if note:
        lines += ["", note]
    return "\n".join(lines)


def top_note(j):
    top, conf = j.get("top_choice"), j.get("confidence")
    return f"Jev's top choice: {name(top) if top else 'n/a'}" + (
        f" (confidence {conf:.2f})" if isinstance(conf, (int, float)) else "")


def load(group):
    found, missing = {}, []
    for s in SCENARIOS:
        path = judgment_path(group, s)
        if path.exists():
            found[s] = read_json(path)
        else:
            missing.append(f"{group}/{s}")
    return found, missing


def section(title, judged, keys, header):
    out = [f"## {title}", ""]
    if not judged:
        return out + ["_No scenarios scored yet._", ""]
    baseline = 1 / len(keys)
    out += [f"No-preference baseline: {baseline:.2f}. Overall across {len(judged)} of {len(SCENARIOS)} scenarios:", "",
            table(mean_scores(list(judged.values()), keys), header), ""]
    for s, j in judged.items():
        out += [f"### {s}", "", table(j["scores"], header, top_note(j)), ""]
    return out


def main(cfg, lenses=None):
    lenses = lenses or LENSES
    per_lens = {}
    missing = []
    for lens in lenses:
        per_lens[lens], m = load(lens)
        missing += m
    cross, m = load(CROSS_LENS) if len(lenses) > 1 else ({}, [])
    missing += m
    if not any(per_lens.values()) and not cross:
        raise SystemExit("No judgments yet; run `summon score` first.")

    RESULTS.mkdir(exist_ok=True)
    with open(RESULTS / "scores.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["comparison", "scenario", "option", "preference_score", "rank", "display_position"])
        for group, judged in [*per_lens.items(), (CROSS_LENS, cross)]:
            for s, j in judged.items():
                r = ranks(j["scores"])
                for k, p in j["scores"].items():
                    w.writerow([group, s, k, p, r[k], j["display_order"].index(k) + 1])

    out = [
        "# Summon experiment report",
        "",
        "Preference score = Jev's probability that an answer is the better one. "
        "Scores in one comparison sum to 1, so the no-preference baseline is 1 / (number of answers).",
        "",
    ]
    if len(lenses) > 1:
        out += section(f"Across lenses: {CROSS_LENS_TEST[-1]} (method enacted) from each lens",
                       cross, lenses, "Lens")
    for lens in lenses:
        out += section(f"Lens: {lens} (conditions A–E)", per_lens[lens], TESTS, "Condition")

    positions = {}
    for judged in [*per_lens.values(), cross]:
        for j in judged.values():
            n = len(j["display_order"])
            for p, k in enumerate(j["display_order"], 1):
                positions.setdefault(p, []).append(j["scores"][k] * n)  # normalize: 1.0 = baseline
    out += [
        "## Notes", "",
        "**Missing:** " + (", ".join(missing) if missing else "none") + ".",
        "",
        "**Mean score by display position**, relative to baseline (1.00 = no position effect):",
        "",
        "| Position | Relative score |", "|---|---|",
    ]
    out += [f"| {p} | {sum(v) / len(v):.2f} |" for p, v in sorted(positions.items())]
    out += [
        "",
        "**Reading the results:** there is one conversation per test and one Jev call per comparison, "
        "so small score differences may be chance.",
        "",
    ]
    (RESULTS / "report.md").write_text("\n".join(out))
    print(f"Wrote {RESULTS / 'scores.csv'} and {RESULTS / 'report.md'}.")
