# Summon experiment

**Which prompting style performs best?**

We compare four styles: asking plainly, assigning a persona, naming a method, and enacting the method in its own vocabulary. "Best" means the outcome a judge prefers. The hypothesis is that enacting a method (asking the questions a practitioner would ask, in their language) summons that way of reasoning and beats the other styles. A fifth condition, the same kind of structured questions asked by a curious child, checks that any gain comes from the method and not just from asking more questions. Claude Opus 5.5 is the subject model and [Jev](https://openrouter.ai/docs/guides/community/jev-tutorial) (via OpenRouter) is the judge. The full design is in [`spec.md`](spec.md).

## Design

Five prompting **conditions**, compared on the same scenarios:

| | Condition | What the opening does |
|---|---|---|
| A | Plain | The scenario only. |
| B | Persona | Adds the lens's identity ("a world-class philosopher of science"), without naming the method. |
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

From one full run (`results-three-lens-run2/`) of the current tests. Each number is Jev's preference score: its probability that an outcome is the best of those compared.

### Individual experiments

One table per scenario. Each column is one lens's comparison of its five outcomes (0.20 means no preference); **bold** marks the lens's top condition. The line below each table compares the three lenses' D outcomes head to head (0.33 means no preference).

**independent-lab**

| Condition | critical-rationalism | social | economic |
|---|---|---|---|
| A Plain | 0.10 | 0.18 | 0.15 |
| B Persona | 0.24 | 0.17 | 0.14 |
| C Method named | **0.37** | 0.03 | 0.22 |
| D Method enacted | 0.16 | 0.20 | 0.24 |
| E Child lens | 0.13 | **0.42** | **0.25** |

Across lenses (D): **critical-rationalism 0.42**, social 0.39, economic 0.19

**legacy-rewrite**

| Condition | critical-rationalism | social | economic |
|---|---|---|---|
| A Plain | 0.02 | 0.14 | 0.16 |
| B Persona | 0.24 | 0.07 | 0.21 |
| C Method named | 0.23 | **0.40** | 0.27 |
| D Method enacted | 0.22 | 0.01 | 0.06 |
| E Child lens | **0.29** | 0.38 | **0.30** |

Across lenses (D): critical-rationalism 0.40, social 0.08, **economic 0.52**

**churn-cause**

| Condition | critical-rationalism | social | economic |
|---|---|---|---|
| A Plain | 0.16 | 0.12 | **0.36** |
| B Persona | 0.06 | 0.13 | 0.29 |
| C Method named | 0.03 | **0.61** | 0.06 |
| D Method enacted | **0.73** | 0.02 | 0.16 |
| E Child lens | 0.02 | 0.12 | 0.13 |

Across lenses (D): **critical-rationalism 0.73**, social 0.16, economic 0.11

### Cumulative

**All nine comparisons** (3 scenarios × 3 lenses), each weighted equally. The lens columns average each lens's three scenarios.

| Rank | Condition | Average score | Comparisons won | critical-rationalism | social | economic |
|---|---|---|---|---|---|---|
| 1 | C Method named | 0.25 | 3 of 9 | 0.21 | **0.35** | 0.18 |
| 2 | E Child lens | 0.23 | 3 of 9 | 0.15 | 0.31 | **0.23** |
| 3 | D Method enacted | 0.20 | 2 of 9 | **0.37** | 0.08 | 0.15 |
| 4 | B Persona | 0.17 | 0 of 9 | 0.18 | 0.12 | 0.21 |
| 5 | A Plain | 0.15 | 1 of 9 | 0.09 | 0.15 | 0.22 |

**Across lenses:** each lens's D outcome, averaged over the three scenarios:

| Rank | Lens | Average score | Scenarios won |
|---|---|---|---|
| 1 | critical-rationalism | 0.52 | 2 of 3 |
| 2 | economic | 0.27 | 1 of 3 |
| 3 | social | 0.21 | 0 of 3 |

**Reading these:** each cell comes from one conversation and one Jev call, and earlier runs showed that single runs can reorder, so treat small differences as noise. The full conversations are in `results-three-lens-run2/<scenario>/<lens>/<test>.md`, and Jev's raw judgments are in the `judgment.json` files.

## Running it

Ask your coding agent (Claude Code, Codex, or similar) to run the experiment: operational instructions for agents are in [`AGENTS.md`](AGENTS.md). The one thing only you can provide is two API keys, which the agent will ask you to put in a local `.env` file:

- **Anthropic:** from https://console.anthropic.com → Settings → API Keys. API usage is billed to Console credits, separately from a Claude subscription.
- **OpenRouter** (for Jev): from https://openrouter.ai/settings/keys.

A full run takes about 30 minutes and costs roughly $25 in Opus usage; Jev's cost is negligible.

## What's where

- `spec.md`: the full design.
- `experiments/`: organized scenario > lens > test. Each scenario folder (`###-<name>/`) holds `scenario.md` and a folder per lens with the five test files. Each test file holds the opening prompt and the guidance for its follow-up questions; a lens's tests are identical in every scenario.
- `results-three-lens-run2/`: the run reported above, with every conversation in readable Markdown and a `report.md`.
- `results-three-lens-run1/`, `results-oneshot-run1/`, `results-oneshot-run2/`, `results-conversation-run1/`, `results-archive/`: earlier runs from previous versions of the design (older B, D, and E; one-shot prompts; a single lens). Useful for historical comparison, but not directly comparable with the current results.
- `src/summon/`: the code.
