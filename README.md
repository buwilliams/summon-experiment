# Summon experiment

Does prompting in a reasoning method's own vocabulary summon that way of reasoning, and produce outcomes a judge prefers? This project tests that with Claude Opus 5.5 as the subject and [Jev](https://openrouter.ai/docs/guides/community/jev-tutorial) (via OpenRouter) as the judge. The full design is in [`spec.md`](spec.md).

## Design

Five prompting **conditions**, compared on the same scenarios:

| | Condition | What the opening does |
|---|---|---|
| A | Plain | The scenario only. |
| B | Persona | Adds an expert identity ("a scientist by training…"). |
| C | Method named | Names the method ("Use the method of conjectures and refutations…"). |
| D | Method enacted | Asks the questions a practitioner would ask, in the method's vocabulary. **The treatment.** |
| E | Child lens | Same form as D, asked by a curious child. Control for "any structured prompt helps". |

Each condition is run through three **lenses**, one experiment each:

| Lens | Governing value | Method |
|---|---|---|
| `critical-rationalism` | Clear thinking | Conjecture and refutation |
| `social` | Popularity | Impression management |
| `economic` | Profits | Profit maximization |

…on three business **scenarios** (`independent-lab`, `legacy-rewrite`, `churn-cause`): 3 lenses × 3 scenarios × 5 conditions = **45 tests**.

**How a test runs.** Each test is a short conversation: the condition's opening, then three follow-up questions written by a separate model call following the condition's guidance, then a fixed "What should we do?" A summarizer condenses the outcome (the final recommendation, its reasons and caveats) to about 250 words.

**How it's judged.** Jev never sees the lens, condition, or prompt. It gets the scenario and anonymous outcome summaries and answers "Which answer do you think is better?"; its probability for each answer is that answer's **preference score**. There are two comparisons:

- **Within a lens:** A–E for each scenario (baseline 0.20).
- **Across lenses:** the D outcomes of the three lenses for each scenario (baseline 0.33).

## Setup

Requires Python ≥ 3.11 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env    # then fill in both keys
```

- `ANTHROPIC_API_KEY`: from https://console.anthropic.com → Settings → API Keys (billed to Console credits, separate from a Claude subscription).
- `OPENROUTER_API_KEY`: from https://openrouter.ai/settings/keys.

## Run

```bash
uv run summon run      # 45 conversations, 8 in parallel → results/<lens>/<scenario>/<test>.json and .md
uv run summon score    # 9 within-lens + 3 cross-lens Jev calls → results/**/judgment.json
uv run summon report   # results/scores.csv and results/report.md
```

Add `--lens <name>` (repeatable) to limit any command to certain lenses; parallelism is `concurrency` in `config.yaml`. A full run takes about 30 minutes and costs roughly $25 in Opus usage (Jev's cost is negligible).

Every command skips work that's already saved, so rerunning after a failure only fills the gaps. To redo a test, delete its `.json`, plus the `judgment.json` files that used it: `results/<lens>/<scenario>/judgment.json`, and for a D test also `results/cross-lens/<scenario>/judgment.json`. To start over, move or delete `results/`.

## Files

```
experiments/
├── 001-independent-lab.md …       # scenarios; add 004-<name>.md to add one
└── <lens>/testA.md … testE.md     # one file per condition
src/summon/                        # run.py, judge.py, report.py, cli.py
```

Each test file has the opening (with `{{SCENARIO}}` replaced by the scenario text) above the line `---- follow-up guidance ----`, and the questioner's guidance below it. The subject model never sees the guidance.

## Results so far

| Folder | What it is | Headline |
|---|---|---|
| `results-oneshot-run1/`, `results-oneshot-run2/` | Critical-rationalism, single prompt, no follow-ups | Rankings didn't replicate between identical runs; only E (last) was stable. |
| `results-conversation-run1/` | Critical-rationalism, conversations (original D) | D won 2 of 3 scenarios decisively (churn-cause, legacy-rewrite) but lost independent-lab, where its questioner over-pursued rigor. |
| `results-archive/` | An early 3-lens one-shot run whose lens setup was later reorganized | Kept for reference. |

After conversation run 1, D was revised toward reasonableness rather than certainty (see `spec.md` §5). The current three-lens run uses that revision.

Each result folder holds the full conversations (`<test>.md`), Jev's judgments, and a `report.md`.
