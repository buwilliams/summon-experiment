# Summon experiment

**Which prompting style performs best?**

We compare four styles: asking plainly, assigning a persona, naming a method, and enacting the method in its own vocabulary. "Best" means the outcome a judge prefers. The hypothesis is that enacting a method (asking the questions a practitioner would ask, in their language) summons that way of reasoning and beats the other styles. A fifth condition, the same kind of structured questions asked by a curious child, checks that any gain comes from the method and not just from asking more questions. Claude Opus 5.5 is the subject model and [Jev](https://openrouter.ai/docs/guides/community/jev-tutorial) (via OpenRouter) is the judge. The full design is in [`spec.md`](spec.md).

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

## Results

From one full run (`results-three-lens-run1/`). Each number is Jev's preference score: its probability that an outcome is the best of those compared. **Bold** marks the top score in each column.

### Individual experiments

Five outcomes compared per scenario, so 0.20 means no preference.

**critical-rationalism**

| Condition | independent-lab | legacy-rewrite | churn-cause | Average |
|---|---|---|---|---|
| A Plain | 0.18 | **0.44** | 0.26 | **0.29** |
| B Persona | 0.25 | 0.02 | **0.55** | 0.27 |
| C Method named | 0.01 | 0.09 | 0.06 | 0.05 |
| D Method enacted | 0.10 | 0.18 | 0.04 | 0.11 |
| E Child lens | **0.46** | 0.27 | 0.08 | 0.27 |

**social**

| Condition | independent-lab | legacy-rewrite | churn-cause | Average |
|---|---|---|---|---|
| A Plain | 0.10 | 0.29 | **0.37** | **0.25** |
| B Persona | **0.41** | 0.14 | 0.18 | 0.24 |
| C Method named | 0.10 | 0.03 | 0.22 | 0.12 |
| D Method enacted | 0.15 | 0.04 | 0.22 | 0.14 |
| E Child lens | 0.24 | **0.50** | 0.01 | 0.25 |

**economic**

| Condition | independent-lab | legacy-rewrite | churn-cause | Average |
|---|---|---|---|---|
| A Plain | 0.06 | 0.08 | 0.34 | 0.16 |
| B Persona | **0.31** | **0.36** | **0.48** | **0.38** |
| C Method named | 0.25 | 0.04 | 0.06 | 0.12 |
| D Method enacted | 0.11 | 0.20 | 0.10 | 0.14 |
| E Child lens | 0.27 | 0.32 | 0.02 | 0.20 |

### Cumulative

**All nine comparisons** (3 lenses × 3 scenarios), each weighted equally:

| Rank | Condition | Average score | Comparisons won | critical-rationalism | social | economic |
|---|---|---|---|---|---|---|
| 1 | B Persona | **0.30** | 5 of 9 | 0.27 | 0.24 | 0.38 |
| 2 | E Child lens | 0.24 | 2 of 9 | 0.27 | 0.25 | 0.20 |
| 3 | A Plain | 0.24 | 2 of 9 | 0.29 | 0.25 | 0.16 |
| 4 | D Method enacted | 0.13 | 0 of 9 | 0.11 | 0.14 | 0.14 |
| 5 | C Method named | 0.10 | 0 of 9 | 0.05 | 0.12 | 0.12 |

**Across lenses:** the method-enacted (D) outcome from each lens, compared head to head (3 outcomes per scenario, so 0.33 means no preference):

| Lens | independent-lab | legacy-rewrite | churn-cause | Average |
|---|---|---|---|---|
| social | **0.63** | 0.06 | **0.47** | 0.39 |
| economic | 0.13 | **0.71** | 0.32 | 0.39 |
| critical-rationalism | 0.24 | 0.23 | 0.21 | 0.23 |

**Reading these:** each cell comes from one conversation and one Jev call, and earlier runs showed single runs can reorder. The full conversations are in `results-three-lens-run1/<lens>/<scenario>/<test>.md` and Jev's raw judgments in the `judgment.json` files.

## Running it

Ask your coding agent (Claude Code, Codex, or similar) to run the experiment: operational instructions for agents are in [`AGENTS.md`](AGENTS.md). The one thing only you can provide is two API keys, which the agent will ask you to put in a local `.env` file:

- **Anthropic:** from https://console.anthropic.com → Settings → API Keys. API usage is billed to Console credits, separately from a Claude subscription.
- **OpenRouter** (for Jev): from https://openrouter.ai/settings/keys.

A full run takes about 30 minutes and costs roughly $25 in Opus usage; Jev's cost is negligible.

## What's where

- `spec.md`: the full design.
- `experiments/`: the scenarios (`###-<name>.md`) and, per lens, the five test files. Each test file holds the opening prompt and the guidance for its follow-up questions.
- `results-three-lens-run1/`: the run reported above, with every conversation in readable Markdown and a `report.md`.
- `results-oneshot-run1/`, `results-oneshot-run2/`, `results-conversation-run1/`, `results-archive/`: earlier runs from previous versions of the design (one-shot prompts, a single lens, the original D). Useful for historical comparison, but not directly comparable with the current results.
- `src/summon/`: the code.
