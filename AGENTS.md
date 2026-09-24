# Agent instructions: running the Summon experiment

You are operating this experiment for a person. They care about the results, not the mechanics: run it, keep them informed, fix problems, and report findings in plain language. The design is in `spec.md`; read it before changing anything experimental.

## Setup

- Requires Python ≥ 3.11 and [uv](https://docs.astral.sh/uv/). Run `uv sync`.
- Keys go in `.env` (copy `.env.example`): `ANTHROPIC_API_KEY` and `OPENROUTER_API_KEY`. If they're missing, walk the person through getting them (see `README.md`) and have them paste the keys into `.env` themselves. Never ask for keys in chat, print them, or commit `.env` (it's gitignored).
- Check a key is set without revealing it: `awk -F= '/=/{print $1": "(length($2)?"set":"EMPTY")}' .env`

## Running

```bash
uv run summon run      # 45 conversations, `concurrency` (8) in parallel → results/<lens>/<scenario>/<test>.json and .md
uv run summon score    # 9 within-lens + 3 cross-lens Jev calls → results/**/judgment.json
uv run summon report   # results/scores.csv and results/report.md
```

- Run the whole pipeline in the background and log it so the person can follow along with `tail -f results/summon.log`:
  `mkdir -p results && (PYTHONUNBUFFERED=1 uv run summon run && PYTHONUNBUFFERED=1 uv run summon score && uv run summon report) >> results/summon.log 2>&1`
- `--lens <name>` (repeatable) limits any command to certain lenses.
- Log lines are prefixed with `<lens>/<scenario>/<test>`. Watch for `FAILED`; successes print `ok [n/45]`.

## Reruns, redos, and failures

- Every command skips work that's already saved, so after failures just rerun the same command; it fills only the gaps. A failed test saves nothing.
- To redo one test: delete its `.json`, plus the judgments that used it: `results/<lens>/<scenario>/judgment.json`, and for a `testD` also `results/cross-lens/<scenario>/judgment.json`. Then rerun `run`, `score`, `report`.
- Before starting a fresh run, move the previous `results/` to a descriptive `results-<name>/` folder rather than deleting it. Past runs are the record.
- Retries: API calls retry with backoff (4 attempts). Auth errors stop the run immediately; fix the key and rerun.

## Rules that keep the experiment valid

- Each test file exists once per lens and is shared by every scenario. Never create per-scenario copies of tests.
- Jev must never see the lens, condition, or prompt wrapper, only the scenario and anonymous outcome summaries.
- Don't send a system prompt, tools, or sampling parameters to the subject model (Opus 5.5 rejects `temperature`), and don't enable model fallbacks.
- In each lens, D's and E's openings stay within ±10% of each other in word count.
- Changing experiment files (scenarios, tests, prompts in `run.py`) changes the experiment. Record why in `spec.md`, and don't mix results from before and after a change in one results folder.

## Reporting

Read `results/report.md` and summarize for the person: the cross-lens winner, each lens's A–E ranking, and how confident to be (one conversation per test, so single runs are noisy; compare against earlier `results-*/` runs). Quote the actual numbers, and say plainly when a result didn't replicate.
