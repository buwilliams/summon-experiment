# Summon experiment

**Which prompting style gets the best outcome from an AI model: asking plainly, assigning a persona, naming a method, or enacting the method in its own vocabulary?**

The hypothesis is that enacting a method (asking the questions a practitioner would ask, in their language) summons that way of reasoning and beats the other styles. A fifth condition, the same kind of structured questions asked by a curious child, checks that any gain comes from the method and not just from asking more questions. Claude Opus 5.5 is the subject model and [Jev](https://openrouter.ai/docs/guides/community/jev-tutorial) (via OpenRouter) is the judge. The full design is in [`spec.md`](spec.md).

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

## Running it

Ask your coding agent (Claude Code, Codex, or similar) to run the experiment: operational instructions for agents are in [`AGENTS.md`](AGENTS.md). The one thing only you can provide is two API keys, which the agent will ask you to put in a local `.env` file:

- **Anthropic:** from https://console.anthropic.com → Settings → API Keys. API usage is billed to Console credits, separately from a Claude subscription.
- **OpenRouter** (for Jev): from https://openrouter.ai/settings/keys.

A full run takes about 30 minutes and costs roughly $25 in Opus usage; Jev's cost is negligible.

## What's where

- `spec.md`: the full design.
- `experiments/`: the scenarios (`###-<name>.md`) and, per lens, the five test files. Each test file holds the opening prompt and the guidance for its follow-up questions.
- `results-*/`: past runs, with every conversation in readable Markdown and a `report.md`.
- `src/summon/`: the code.

## Results so far

| Folder | What it is | Headline |
|---|---|---|
| `results-oneshot-run1/`, `results-oneshot-run2/` | Critical-rationalism, single prompt, no follow-ups | Rankings didn't replicate between identical runs; only E (last) was stable. |
| `results-conversation-run1/` | Critical-rationalism, conversations (original D) | D won 2 of 3 scenarios decisively (churn-cause, legacy-rewrite) but lost independent-lab, where its questioner over-pursued rigor. |
| `results-archive/` | An early 3-lens one-shot run whose lens setup was later reorganized | Kept for reference. |

After conversation run 1, D was revised toward reasonableness rather than certainty (see `spec.md` §5). The current three-lens run uses that revision.

Each result folder holds the full conversations (`<test>.md`), Jev's judgments, and a `report.md`.
