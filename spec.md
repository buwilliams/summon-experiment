# Summon Experiment — Conversation Specification (3 lenses × 3 scenarios × 5 conditions)

**Question: which prompting style gets the best outcome from an AI model: asking plainly, assigning a persona, naming a method, or enacting the method in its own vocabulary?** A child-lens control checks that any gain comes from the method, not just from asking more questions.

The experiment is kept deliberately simple: generate outcomes under each prompting style, have a judge pick its favorites, and look at the data. Improvements come after we have results.

---

## 1. Purpose

### 1.1 The conjecture

LLMs are trained on human text, and humans reason from many different epistemic positions: methods, schools of thought, and traditions for forming, evaluating, and criticizing ideas. The conjecture is that framing an inquiry naturally in an epistemic position's own vocabulary summons its characteristic way of reasoning and produces better outcomes, with an outsized payoff for the prompting involved.

The experiment compares asking a plain question, invoking an identity, naming a method, and enacting the method in the language of the inquiry itself. Each test is a short conversation: an opening, three follow-up questions written by a separate model in the condition's style, and a final "What should we do?" We measure only which outcomes a judge prefers.

An earlier one-shot version (a single prompt, no follow-ups) gave rankings that changed between identical runs. Real use involves back-and-forth in which the model can be questioned and clarify, which is what this version adds.

The project runs **three experiments**, one per lens. Each holds its lens fixed, so within an experiment the prompting style is the only thing that varies between conditions. A **cross-lens comparison** then asks which lens's enacted method (D) produces the outcome Jev prefers: what reasoner each lens summons, and which one wins.

### 1.2 Conditions

| Test | Condition | What the prompt does |
|---|---|---|
| testA | **A — Plain** | The scenario only. |
| testB | **B — Persona** | Adds an identity ("You are a world-class expert: a scientist / sociologist / economist by training…") without stating a method. |
| testC | **C — Method named** | Names the lens's method ("Use the method of conjectures and refutations…", "Use impression management…", "Use profit maximization…") without its reasoning questions. |
| testD | **D — Method enacted** | Asks the questions a practitioner would naturally ask, in that position's vocabulary. **This is the conjecture's treatment.** |
| testE | **E — Child lens, same form** | Same length and question structure as D, but asked by a child with little or no background knowledge: naive, concrete questions that still refer to the situation. Controls for "any rich, structured prompt helps". |

### 1.3 Lenses

| Lens (folder) | Governing value | Named framework |
|---|---|---|
| `critical-rationalism` | Clear thinking | Critical rationalism: conjecture and refutation |
| `social` | Popularity: approval, reputation, standing | Impression management (Goffman) |
| `economic` | Profits | Profit maximization |

Each lens has its own five tests. Condition A (plain) is the same text in every lens; B–E are written in the lens's vocabulary.

### 1.4 Design

Each test file exists once per lens, and every scenario runs through the same tests: the tests are the control and the scenario is the variable. 3 lenses × 3 scenarios × 5 conditions = **45 tests**. The judge never sees which lens or condition produced an answer; it only says which answer it thinks is better.

---

## 2. Directory layout

```
summon-experiment/
├── spec.md
├── README.md                        # how to run
├── pyproject.toml
├── .env.example                     # ANTHROPIC_API_KEY=, OPENROUTER_API_KEY=
├── config.yaml                      # §8
├── experiments/
│   ├── 001-independent-lab.md       # scenarios: ###-<name>.md, run in numeric order
│   ├── 002-legacy-rewrite.md
│   ├── 003-churn-cause.md
│   └── <lens>/                      # critical-rationalism, social, economic
│       └── testA.md … testE.md      # the five conditions: opening + follow-up guidance
├── results/
│   ├── scores.csv
│   ├── report.md
│   ├── <lens>/<scenario>/
│   │   ├── testA.json               # conversation turns, outcome summary, usage
│   │   ├── testA.md                 # readable copy of the conversation
│   │   ├── …
│   │   └── judgment.json            # Jev's scores for this lens/scenario's five tests
│   └── cross-lens/<scenario>/
│       └── judgment.json            # Jev's scores for the three lenses' D outcomes
└── src/summon/
    ├── cli.py
    ├── run.py                       # run conversations and summarize outcomes
    ├── judge.py                     # Jev calls: within each lens and across lenses
    └── report.py                    # scores and rankings
```

---

## 3. Scenarios (verbatim)

Each scenario has the same shape: a first-person situation plus **two rival beliefs about what is right**, ending with a question. None of the scenarios names an epistemic method, so the only difference between conditions is the test wrapper.

### 3.1 `experiments/001-independent-lab.md`

```markdown
I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?
```

*(Minimal edit to the original: "He hired me innovation" → "He hired me to lead innovation", to fix a dropped word. Revert it if you want the original wording.)*

### 3.2 `experiments/002-legacy-rewrite.md`

```markdown
I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?
```

### 3.3 `experiments/003-churn-cause.md`

```markdown
I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?
```

Design notes (not part of the scenario files):
- **independent-lab**: a strategy choice where the user's own belief is one of the options, so the responses may reveal whether the assistant favors the user's position.
- **legacy-rewrite**: a classic engineering strategy dilemma with a known literature and known failure modes.
- **churn-cause**: a *causal-diagnosis* question. This is where conjecture and refutation should show its largest advantage, because the two beliefs make different, testable predictions.

---

## 4. Test templates (verbatim)

Each test file has two parts, separated by the line `---- follow-up guidance ----`. Above it is the opening template: `{{SCENARIO}}` is replaced with the scenario file's contents (trimmed), and the result is the **first user message**. Below it is the guidance given to the questioner for the follow-up turns (§5); it is never shown to the subject model. There is **no system prompt** in any condition.

Each test exists exactly once per lens, so the tests are the control and the scenario is the only variable: every scenario is run through the same files. `testA.md` is identical in every lens.

In every lens, D's and E's openings are written to within ±10% of each other in word count (excluding `{{SCENARIO}}`).

### 4.1 Lens: `critical-rationalism` — `experiments/critical-rationalism/`

The child lens asks from a position of little or no background knowledge: concrete, naive, sometimes off-to-the-side questions that still refer to the situation. E mirrors D sentence by sentence, swapping the practitioner's concepts for a child's. The wording avoids details specific to any one scenario, so the same wrapper fits all three.

**`testA.md` — A: Plain:**

```markdown
{{SCENARIO}}

---- follow-up guidance ----
Ask a natural follow-up question that an ordinary person in this situation might ask next, given the conversation so far.
```

**`testB.md` — B: Persona:**

```markdown
You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

{{SCENARIO}}

---- follow-up guidance ----
Ask a natural follow-up question that an ordinary person in this situation might ask next, given the conversation so far.
```

**`testC.md` — C: Method named:**

```markdown
Use the method of conjectures and refutations (critical rationalism) to answer the following.

{{SCENARIO}}

---- follow-up guidance ----
Ask a follow-up question that asks the assistant to keep using the method of conjectures and refutations (critical rationalism), without spelling out what the method involves.
```

**`testD.md` — D: Method enacted:**

```markdown
{{SCENARIO}}

I don't need certainty; I want the most reasonable explanation we can act on now and correct as we learn. Treat each belief as a conjecture: what does each one claim is going on, and why? Whose values and goals is each one built around, and are they the ones that matter most here? What might both be leaving out that could change the outcome? Which assumption is most worth checking first, and what is a quick way to check it? And is there a better explanation that fits the same facts than either one?

---- follow-up guidance ----
Ask one short follow-up question that a reasonable critical rationalist would ask next. Aim for reasonableness, not certainty: we will act on the best current explanation and correct it as we learn. Look for what the last answer leaves out that matters: whose values it is serving and whether they are the right ones, what could change the outcome that it hasn't considered, or the one assumption most worth checking first. Keep it brief and practical; don't ask for more rigor, proof, or procedure.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I don't need to be super sure; I just want a good idea we can try now and fix if it turns out wrong. Pretend each idea is a new toy: what does it do, and who gets to play with it? Which idea would make the people at work happy, and would anybody cry? Did everybody forget about something, like snacks or a place to play? Which part should we try first, and could we try it really fast, like before lunch? And is there a third idea everybody likes better, like a swing set for the whole office?

---- follow-up guidance ----
Ask the follow-up question a curious child with little or no background knowledge would ask next: naive, concrete, sometimes off to the side, but still about the situation. Build on the last answer.
```

### 4.2 Lens: `social` — `experiments/social/`

**`testA.md` — A: Plain:** identical to the critical-rationalism `testA.md`.

**`testB.md` — B: Persona:**

```markdown
You are a world-class expert: a sociologist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

{{SCENARIO}}

---- follow-up guidance ----
Ask a natural follow-up question that an ordinary person in this situation might ask next, given the conversation so far.
```

**`testC.md` — C: Method named:**

```markdown
Use impression management to answer the following.

{{SCENARIO}}

---- follow-up guidance ----
Ask a follow-up question that asks the assistant to keep using impression management, without spelling out what it involves.
```

**`testD.md` — D: Method enacted:**

```markdown
{{SCENARIO}}

I want to know which approach wins approval and improves standing. Consider how each proposal would play inside and outside the company. Who gains status or credit, and who risks losing face or taking the blame? If each proposal went ahead, what would it signal to the board, employees, customers, and the public? Where might looking decisive or reassuring an audience matter more than operational results? What alliances and reputations would each proposal strengthen or threaten? And is there a third approach that wins greater support while letting the important players save face?

---- follow-up guidance ----
Ask one short follow-up question that someone skilled at impression management would ask next. Aim for what is reasonable, not certain: we will act on the best current read of how this will land and adjust as we learn. Look for what the last answer leaves out that matters for approval and standing: whose opinion it overlooks, how it would look to an audience it hasn't considered, or the one reputational risk most worth checking first. Keep it brief and practical; don't ask for more rigor, proof, or procedure.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

---- follow-up guidance ----
Ask the follow-up question a curious child with little or no background knowledge would ask next: naive, concrete, sometimes off to the side, but still about the situation. Build on the last answer.
```

### 4.3 Lens: `economic` — `experiments/economic/`

**`testA.md` — A: Plain:** identical to the critical-rationalism `testA.md`.

**`testB.md` — B: Persona:**

```markdown
You are a world-class expert: an economist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

{{SCENARIO}}

---- follow-up guidance ----
Ask a natural follow-up question that an ordinary person in this situation might ask next, given the conversation so far.
```

**`testC.md` — C: Method named:**

```markdown
Use profit maximization to answer the following.

{{SCENARIO}}

---- follow-up guidance ----
Ask a follow-up question that asks the assistant to keep using profit maximization, without spelling out what it involves.
```

**`testD.md` — D: Method enacted:**

```markdown
{{SCENARIO}}

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

---- follow-up guidance ----
Ask one short follow-up question that a profit-minded operator would ask next. Aim for what is reasonable, not certain: we will act on the best current estimate and correct it as we learn. Look for what the last answer leaves out that matters for profits: a cost, risk, or source of revenue it hasn't considered, whether the expected return justifies the money and time, or the one financial assumption most worth checking first. Keep it brief and practical; don't ask for more rigor, proof, or procedure.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

---- follow-up guidance ----
Ask the follow-up question a curious child with little or no background knowledge would ask next: naive, concrete, sometimes off to the side, but still about the situation. Build on the last answer.
```

---

## 5. Run — conversations and outcome summaries

`summon run` runs all 45 tests (all lenses, or those given with `--lens`), `concurrency` of them in parallel (default 8); the turns within one conversation are sequential. Each test is a short conversation, not a single prompt, so that the model can be questioned and clarify its thinking the way it would with a real user.

**Conversation.** Each test has 5 user turns (with `followups: 3`):

1. **Opening:** the test's template above the guidance marker, with `{{SCENARIO}}` filled in.
2. **Follow-ups 1–3:** written by a separate questioner call (below), which reads the conversation so far and follows the test's guidance.
3. **Final:** always the fixed question `What should we do?`

Every turn goes to the subject model through the Anthropic Messages API (Python `anthropic` SDK):

- Model `claude-opus-5-5`, `max_tokens: 32000`, streamed.
- `thinking: {"type": "adaptive"}`, `output_config: {"effort": "medium"}`.
- No system prompt, no tools, no temperature or other sampling parameters, and no fallbacks. Each test starts a fresh conversation; nothing carries over between tests.
- Each assistant reply is sent back in later turns exactly as returned, thinking blocks included, so the model builds on its own reasoning. Only the `text` blocks count as its answer.

**Questioner.** Before each follow-up, a separate call to the same model and settings (`max_tokens: 8000`) receives only this prompt, with the test's guidance and a plain-text transcript of the conversation so far:

```
You are playing the user in the conversation below, which is still in
progress. Write the user's next message: one short follow-up question.

{guidance}

Don't ask for a final recommendation yet; that comes later. Reply with only
the question, nothing else.

<conversation>
{transcript}
</conversation>
```

The guidance is deliberately short and generic, and the questioner is free to drift: we are testing model capability, not a fixed script. Follow-ups are minimal, quick questions for every condition.

*Revision (conversation run 2):* D's opening and guidance were rewritten around reasonableness rather than certainty, following the view that epistemic positions are value-based and model-based: good criticism looks for what the current model leaves out and whose values set the frame, rather than demanding more rigor. In run 1 the questioner had pushed D toward ever-heavier validation procedures. E was rewritten to keep mirroring D, and the shared questioner prompt now asks for one short question.

**Outcome summary.** Jev's context is small and each call holds all five of a scenario's outcomes, so Jev judges summaries. After the final turn, a separate call (same model and settings, `max_tokens: 8000`) summarizes the outcome of the conversation:

```
Below is a scenario and a conversation about it. Summarize the outcome in
about 250 words of plain prose: what the assistant ultimately recommends
doing, its main reasons, the actions or tests it proposes, and its key
caveats, in the assistant's own terms. Do not describe the conversation, the
questions asked, or how the recommendation developed. Do not evaluate the
recommendation or add ideas it does not contain.

<scenario>
{scenario}
</scenario>

<conversation>
{transcript}
</conversation>
```

**Saving.** Write `results/<lens>/<scenario>/<test>.json` with every turn (user message, answer, who wrote the question, `stop_reason`, usage), the final answer, the outcome summary, model IDs, and timestamps. Also write a readable `<test>.md` with the full conversation and summary.

**Rerunning.** `summon run` skips any test whose `.json` already exists. To redo a test, delete its file and run again. To start over, delete `results/`.

**Failures.** Retry a failed API call up to four attempts in total, with exponential backoff starting at 5 seconds (parallel runs can hit rate limits). If it still fails, or any turn is cut off by `max_tokens` or refused, print the test ID and the reason, save nothing for that test, and continue to the next test. Rerunning picks up the missing tests.

---

## 6. Judge — Jev's preference score

`summon score` makes two kinds of Jev calls, in parallel:

- **Within each lens:** one call per lens and scenario comparing that lens's five outcomes (A–E): 9 calls.
- **Across lenses:** one call per scenario comparing the D (method enacted) outcomes of the three lenses: 3 calls, saved under `results/cross-lens/<scenario>/`.

A comparison runs only when all of its outcomes exist. Both use the same request below, with as many answers as there are options (5 within a lens, 3 across lenses).

**Request.** Put the plain scenario and all five summaries in the state under anonymous IDs `answer_1` … `answer_5`, in a random (seeded) order for each comparison, so that no condition is always shown in the same position. Ask a single [`choice`](https://docs.typesafe.ai/primitives/choice) question whose options are the five answers. POST to `https://openrouter.ai/api/alpha/decisions` with `Authorization: Bearer $OPENROUTER_API_KEY`:

```json
{
  "model": "typesafe/jev-1.13",
  "state": {
    "scenario": "...plain scenario text...",
    "answers": {
      "answer_1": "...summary...",
      "answer_2": "...summary...",
      "answer_3": "...summary...",
      "answer_4": "...summary...",
      "answer_5": "...summary..."
    }
  },
  "questions": {
    "better": {
      "type": "choice",
      "instructions": "Which answer do you think is better?",
      "criteria": {
        "answer_1": "answer_1 is better.",
        "answer_2": "answer_2 is better.",
        "answer_3": "answer_3 is better.",
        "answer_4": "answer_4 is better.",
        "answer_5": "answer_5 is better."
      }
    }
  }
}
```

Jev receives only the plain scenario and the summaries: never the lens, condition, or prompt wrapper.

**Preference score.** Jev's response has `answers.better.probabilities`: one value from 0 to 1 for each answer, summing to 1. Mapped back to its condition, that probability is the condition's **preference score** for the scenario, used as-is. Higher is better; the no-preference baseline is 0.2 within a lens and 0.33 across lenses.

If the probabilities are missing, don't cover every option, or don't sum to about 1, retry the call up to three times; never fill in a missing score. Save the display order, the ID-to-condition mapping, and the raw response (including `choice` and `confidence`) to that comparison's `judgment.json`. Like `run`, `score` skips comparisons that already have a `judgment.json`. Reference: [OpenRouter Jev tutorial](https://openrouter.ai/docs/guides/community/jev-tutorial).

---

## 7. Report

`summon report` writes:

- `results/scores.csv`: one row per comparison/scenario/option with its preference score (45 rows within lenses + 9 across lenses).
- `results/report.md` with:
  1. **Across lenses:** each lens's mean D score across the three scenarios, ranked, then one table per scenario.
  2. **Per lens:** each condition's mean score across the three scenarios, ranked, then one table per scenario, with Jev's top choice and confidence.
  3. **Notes:** any comparisons missing because tests failed, and the mean score at each display position relative to baseline, to show whether position in the list influenced Jev.

Equal scores share a rank. Every scenario counts equally in the averages.

**Reading the results:** there is one conversation per test and one Jev call per comparison, so small score differences may be chance. The natural next step is a second full run to see whether the ranking holds.

---

## 8. CLI and config

```
summon run       # run missing conversations and summarize outcomes
summon score     # run missing Jev comparisons (within and across lenses)
summon report    # write scores.csv and report.md

# any command can be limited to lenses: --lens social --lens economic
```

`config.yaml`:

```yaml
seed: 20260924
subject_model: claude-opus-5-5
max_tokens: 32000
effort: medium
followups: 3
judge_model: typesafe/jev-1.13
concurrency: 8              # conversations / Jev calls in parallel
```

API keys come from the environment or `.env`. Requirements: Python ≥ 3.11 with `uv`; dependencies `anthropic`, `httpx`, `pyyaml`, and `python-dotenv`.
