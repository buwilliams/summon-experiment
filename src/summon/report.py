"""Write scores.csv and report.md (spec §7), organized scenario > lens > test."""

import csv
import statistics

from . import CROSS_LENS_TEST, LENSES, RESULTS, SCENARIOS, TESTS, read_json
from .judge import CROSS_LENS, judgment_path

NAMES = {"testA": "A Plain", "testB": "B Persona", "testC": "C Method named",
         "testD": "D Method enacted", "testE": "E Child lens"}


def ranks(scores):
    """Competition ranking, higher first; equal scores share a rank."""
    return {k: 1 + sum(1 for other in scores.values() if other > s) for k, s in scores.items()}


def table(scores, header, note=""):
    r = ranks(scores)
    lines = [f"| Rank | {header} | Preference score |", "|---|---|---|"]
    for k in sorted(scores, key=lambda k: (r[k], k)):
        lines.append(f"| {r[k]} | {NAMES.get(k, k)} | {scores[k]:.3f} |")
    if note:
        lines += ["", note]
    return "\n".join(lines)


def top_note(j):
    top, conf = j.get("top_choice"), j.get("confidence")
    return f"Jev's top choice: {NAMES.get(top, top) if top else 'n/a'}" + (
        f" (confidence {conf:.2f})" if isinstance(conf, (int, float)) else "")


def main(cfg, lenses=None):
    lenses = lenses or LENSES
    groups = [*lenses, CROSS_LENS] if len(lenses) > 1 else list(lenses)
    judged, missing = {}, []   # judged[(scenario, group)] = judgment
    for s in SCENARIOS:
        for g in groups:
            path = judgment_path(s, g)
            if path.exists():
                judged[(s, g)] = read_json(path)
            else:
                missing.append(f"{s}/{g}")
    if not judged:
        raise SystemExit("No judgments yet; run `summon score` first.")

    RESULTS.mkdir(exist_ok=True)
    with open(RESULTS / "scores.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["scenario", "comparison", "option", "preference_score", "rank", "display_position"])
        for (s, g), j in judged.items():
            r = ranks(j["scores"])
            for k, p in j["scores"].items():
                w.writerow([s, g, k, p, r[k], j["display_order"].index(k) + 1])

    within = [j for (s, g), j in judged.items() if g != CROSS_LENS]
    cross = [j for (s, g), j in judged.items() if g == CROSS_LENS]
    out = [
        "# Summon experiment report",
        "",
        "Preference score = Jev's probability that an outcome is the best of those compared. "
        "Within a lens 5 outcomes are compared (no-preference baseline 0.20); "
        "across lenses the 3 lenses' D outcomes are compared (baseline 0.33).",
        "",
        "## Overall",
        "",
    ]
    if within:
        avg = {t: statistics.mean(j["scores"][t] for j in within) for t in TESTS}
        wins = {t: sum(j.get("top_choice") == t for j in within) for t in TESTS}
        by_lens = {l: [j for (s, g), j in judged.items() if g == l] for l in lenses}
        out += [f"All {len(within)} within-lens comparisons, each weighted equally:", "",
                "| Rank | Condition | Average | Won | " + " | ".join(lenses) + " |",
                "|---|---|---|---|" + "---|" * len(lenses)]
        r = ranks(avg)
        for t in sorted(TESTS, key=lambda t: (r[t], t)):
            cells = [f"{statistics.mean(j['scores'][t] for j in js):.2f}" if js else "–"
                     for js in by_lens.values()]
            out.append(f"| {r[t]} | {NAMES[t]} | {avg[t]:.3f} | {wins[t]} of {len(within)} | "
                       + " | ".join(cells) + " |")
        out.append("")
    if cross:
        avg = {l: statistics.mean(j["scores"][l] for j in cross) for l in lenses}
        out += [f"Across lenses ({NAMES[CROSS_LENS_TEST]} from each lens), {len(cross)} scenarios:", "",
                table(avg, "Lens"), ""]

    for s in SCENARIOS:
        out += [f"## Scenario: {s}", ""]
        for g in groups:
            title = f"Across lenses ({NAMES[CROSS_LENS_TEST]})" if g == CROSS_LENS else f"Lens: {g}"
            j = judged.get((s, g))
            out += [f"### {title}", "",
                    table(j["scores"], "Lens" if g == CROSS_LENS else "Condition", top_note(j))
                    if j else "_Not scored yet._", ""]

    positions = {}
    for j in judged.values():
        n = len(j["display_order"])
        for p, k in enumerate(j["display_order"], 1):
            positions.setdefault(p, []).append(j["scores"][k] * n)  # 1.0 = baseline
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
