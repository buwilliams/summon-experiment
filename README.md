# Summon experiment

Tests whether prompting in a reasoning method's own vocabulary produces answers a judge prefers. 3 lenses (critical-rationalism, social, economic) × 3 scenarios × 5 prompting conditions = 45 short conversations with Claude Opus 5.5 (opening, three generated follow-up questions, then "What should we do?"), scored by Jev (via OpenRouter) within each lens, plus a cross-lens comparison of each lens's method-enacted (D) outcome. See `spec.md` for the design.

## Setup

Requires Python ≥ 3.11 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env    # then fill in both keys
```

- `ANTHROPIC_API_KEY`: from https://console.anthropic.com → Settings → API Keys. API usage is billed to the Console account's credits.
- `OPENROUTER_API_KEY`: from https://openrouter.ai/settings/keys.

## Run

```bash
uv run summon run      # 45 conversations (8 in parallel) → results/<lens>/<scenario>/<test>.json/.md
uv run summon score    # Jev: 9 within-lens + 3 cross-lens calls → results/.../judgment.json
uv run summon report   # results/scores.csv and results/report.md
```

Each command skips work that's already saved, so rerunning after a failure only fills the gaps. To redo one test, delete its `.json` (and that scenario's `judgment.json`, so it's rescored). To start over, delete `results/`.

Scenarios live in `experiments/###-<name>.md` (run in numeric order; add `004-…` to add one). Each lens folder `experiments/<lens>/` holds five tests, `testA.md` … `testE.md`, shared by every scenario. Add `--lens <name>` to any command to limit it to one lens. Each has an opening (with `{{SCENARIO}}` replaced by the scenario text) and, below `---- follow-up guidance ----`, the guidance the questioner uses to write follow-up questions. Earlier one-shot runs are kept in `results-oneshot-run1/` and `results-oneshot-run2/`.
