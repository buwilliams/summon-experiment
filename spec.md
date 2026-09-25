# Summon Experiment

## Current definitions and editor (2026-09-25)

This section supersedes all older hierarchy and naming descriptions below.

- Hypothesis → Experiment → Test → Style is the authoring hierarchy. An experiment
  is the case formerly called a scenario. The separate multi-case study layer is removed.
- A Test is a perspective formerly called a View. An individual chat attempt is a
  session. An experiment's batch covers its test/style combinations.
- The editor uses focused breadcrumb screens, editable name dropdowns, plus buttons,
  and centered chevrons. Definitions and submission metadata save automatically.
  Incomplete or failed edits remain local drafts; concurrent catalog changes cause
  an explicit conflict instead of silently overwriting another edit.
- Catalog schema 2 stores text directly on experiments. Internal view and scenario
  keys in session snapshots remain compatibility names; UI copy uses Test/Experiment.
  Openings use {{EXPERIMENT}}. Existing case-specific text and styles are preserved.
- During this development reset the user authorized clearing all collected data.
  Definition migration creates a new catalog revision; old definitions remain readable.

## Study hierarchy and human judgments (2026-09-25)

This section supersedes earlier UI naming and grouping descriptions.

- A hypothesis has a name and editable statement. Each experiment belongs to one
  hypothesis and is a study containing selected scenarios and views (with their styles).
- Batches belong to experiments. Every batch freezes its hypothesis, experiment,
  catalog revision, and scenario × view × style roster. Each assigned conversation
  is a test; its selected LLM response is the submission. Revisions retain original tests.
- The initial default hypothesis is “Prompting style effectiveness,” with the editable
  statement “Prompting style affects the quality of recommendations produced through
  human interaction.” The existing setup becomes “Human prompting study.”
- Experiments defines hypotheses and studies. Collect, Analyze, and Results select a
  hypothesis and study, then show only that study's batches or reports. Definition
  edits apply to new batches, preserving historical evidence.
- Jev still compares selected responses in both answer orders. After a report completes,
  each named local reviewer can judge the same pairs. Response A/B order is randomized
  independently and persisted. Scenario and verbatim responses are visible; style labels,
  Jev scores, and other human judgments are hidden until the reviewer saves A, B, or Tie.
- Each saved human judgment records reviewer, pair/report IDs, display order, choice,
  mapped winning submission (or null for a tie), optional reason, timestamp, and protocol.
  Votes are immutable and stored separately from Jev report snapshots. Duplicate retries
  are idempotent. Reviewer names are local identifiers, not authenticated accounts.
- Results shows human preference shares and Jev probabilities separately, pair coverage,
  reviewer counts, agreement, and individual human records. Complete Jev rankings stay
  hidden in the UI until the current reviewer completes that report. This is presentation
  blinding, not access control: the local owner can inspect raw files and exports.
- Human shares assign 1/0 to a preference and 0.5/0.5 to a tie, then average over reviewers
  per pair. Agreement counts an exact match (including ties). Cross-view comparisons use
  Jev's finalists, not independently chosen human finalists; human results describe those
  same pairs and must not be interpreted as an independent cross-view tournament.
- New data uses readable JSON and Markdown under
  `hypotheses/<name-id>/experiments/<name-id>/batches/<name-id>/`, with `batch.json`,
  `tests/<test-id>/session.json` and `submission.json`, `reports/<name-id>.json`, and
  `judgments/<id>.json`. Full names live inside records; path names are shortened for
  Windows. Catalog definitions remain immutable numbered revisions under `catalog/`.
  Existing record paths and collected results are preserved. Export includes human ballots.
- Chat renders Markdown headings, emphasis, lists, quotes, tables, links, and code blocks.
  Raw HTML is escaped, unsafe link protocols are rejected, and remote images are disabled.
  Raw Markdown remains authoritative in saved transcripts, submissions, and model calls.


## Current protocol: human-pairwise-v1 (2026-09-25)

The web application supersedes the automated procedure below for new data.
Reason: model-written follow-ups measure a model's ability to enact prompting
styles, whereas the intended question concerns humans using those styles.
Multi-option preferences also make individual comparisons hard to inspect.
The original scenario and style texts remain unchanged and seed the web catalog.
Views correspond to the historical lenses; A–E remain styles within each view.
New scenarios, views, and styles are editable in the application.

### Collection and provenance

- GPT-6 Astra through OpenRouter (`openai/gpt-6-astra`), medium reasoning,
  16,000 maximum output tokens, no system prompt, tools, sampling overrides,
  or provider fallbacks. Scenario context is the first user message. Subsequent
  prompts are written by the human. Suggested openings are optional and editable
  before sending; following the guidance is not mechanically enforced.
- Each session freezes scenario, view, style, full style roster, catalog revision,
  participant, batch, and model. Assistant messages (including returned reasoning
  details) are replayed on follow-ups. Raw calls preserve resolved model and usage.
- Human selects a complete assistant message verbatim as the solution. No model
  summarizer is used. Refused, empty, and truncated answers cannot be submitted.
  Submitted sessions cannot continue; a new test requires a new session.
- Flat JSON records in `experiment-data/` store web data separately from historical
  results, with generated Markdown companions for GitHub reading. Edits retain new
  catalog revision files. Submission notes/inclusion may be edited; report inputs are
  immutable snapshots and retain the original notes and responses.

### Storage revision (2026-09-25)

The collection interface is now called Interview. Setup controls, the separate
view panel, and recent sessions are removed. The scenario appears in the
conversation, with an editable prefilled opening and inline follow-up guidance.
The human still writes prompts and selects an assistant response as the solution.
The human interviews the LLM, not the reverse: scenario and view perspective
are introduced in the conversation, the editable opening asks for a recommendation
with reasons, and the human continues questioning until a recommendation is
acceptable to submit. The human judges readiness for submission; Jev compares
submitted LLM responses afterward. The shared recommendation-and-reasons sentence
is visible in every new suggested opening and is sent only when the human sends it.
These interface messages do not change the subject model's input: scenario
context is sent once, followed by the human's prompts and assistant responses.

The system resumes unfinished sessions before assigning new work. New sessions
cover every scenario/view/style combination in `Interview round N`, with a
deterministic shuffled order keyed by participant, catalog revision, round, and
IDs. After a complete round, the next round starts. The participant comes from
`SUMMON_PARTICIPANT`, the latest session, or `Local participant` on a new workspace.
Assignment method and round are saved with new sessions. This is automated
scheduling, not a claim of statistically balanced assignment. Existing sessions
are preserved, and new automatic rounds stay separate from manual batches.

Replaced SQLite with flat files at the user’s request for GitHub readability;
there is no change to the experimental protocol. Files group by scenario, batch,
view, style, and session. Reports are in each batch’s `reports/` folder. Short ID
suffixes distinguish similarly named items. JSON is authoritative; adjacent
Markdown renders human-readable content. Atomic file replacement prevents partial
JSON. An ignored pending-write journal recovers multi-file saves on restart.
Only one server process may write a data folder. Every catalog revision is
retained from this change onward; previously overwritten revisions cannot be
reconstructed except from saved session snapshots. The original SQLite file is
read-only during migration and retained as a local backup. Experiment files are
Git-trackable; keys, logs, journals, and the old database remain ignored.

### Pairwise judging and reporting

- Reports use one scenario, participant, batch, model, and catalog revision.
  Choose exactly one submission per style for every included view. A view with
  missing styles cannot rank or advance a winner. Entire views may be omitted;
  the report only speaks about the views selected in its snapshot.
- Every unordered within-view pair is judged twice, reversing display order.
  Jev sees only the plain scenario and verbatim solutions as `answer_1` and
  `answer_2`, with the question "Which answer do you think is better?" No metadata,
  view names, style labels, or conversation wrappers are supplied. Text itself
  may reveal the style; anonymity is not guaranteed semantic blinding.
- Both probabilities must be finite, in [0,1], cover both answers, and sum to
  approximately one. Invalid or failed calls stop that report with a visible error.
  Every successful call is checkpointed; resume performs unfinished calls only.
- A pair's score is the mean of its two order-adjusted probabilities. A style's
  within-view score is its equal-weight mean over opponents. Every highest-scoring
  style advances, including numerical ties (tolerance 1e-9). This is a mean
  preference ranking, not a claim that a Condorcet winner exists.
- Across views, every winning solution meets each winning solution from other
  selected views in both orders. Dashboard rows represent solutions, including
  co-winners, rather than pooling ties into an invented single view winner.
- Reports record raw responses, actual model snapshots, ID mappings, timestamps,
  pair scores, and order differences. Rankings are shown only on completion.
  Five styles yield 10 pairs / 20 calls per view. Three views without ties yield
  30 within-view pairs plus 3 cross-view pairs / 66 calls total.

### Interpretation

This measures Jev's preference for a human-selected answer produced in a labeled
prompting session. It does not by itself identify a causal prompting effect.
Human skill, effort, compliance, learning/carryover, answer length, and selection
can affect outcomes. Record deviations in submission notes, vary collection order,
and repeat matched batches before making broad claims. A 0.5 pair score is the
neutral reference, not statistical confidence. Order reversal diagnoses one bias;
it does not remove judge taste, answer-content cues, or all comparison issues.
There is no automatic inferential pooling across batches or historical runs.

References: [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra),
[OpenRouter parameters](https://openrouter.ai/docs/api/reference/parameters),
[Jev API](https://openrouter.ai/docs/guides/community/jev-tutorial).

---

## Historical automated protocol (retained for reproduction)

**Question: which prompting style performs best?** The styles are asking plainly, assigning a persona, naming a method, and enacting the method in its own vocabulary; "best" means the outcome a judge prefers. A child-lens control checks that any gain comes from the method, not just from asking more questions.

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
| testB | **B — Persona** | Adds the lens's identity ("You are a world-class philosopher of science", "…sociologist who studies status and reputation", "…economist who studies how firms make profits") without naming the method. |
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
├── experiments/                     # organized scenario > lens > test
│   ├── 001-independent-lab/         # scenario: ###-<name>/, run in numeric order
│   │   ├── scenario.md
│   │   ├── critical-rationalism/    # lens
│   │   │   └── testA.md … testE.md  # tests: the five conditions (opening + follow-up guidance)
│   │   ├── social/testA.md … testE.md
│   │   └── economic/testA.md … testE.md
│   ├── 002-legacy-rewrite/…
│   └── 003-churn-cause/…
├── results/                         # same order: scenario > lens > test
│   ├── scores.csv
│   ├── report.md
│   └── <scenario>/
│       ├── <lens>/
│       │   ├── testA.json           # conversation turns, outcome summary, usage
│       │   ├── testA.md             # readable copy of the conversation
│       │   ├── …
│       │   └── judgment.json        # Jev's scores for this scenario/lens's five tests
│       └── cross-lens/
│           └── judgment.json        # Jev's scores for the three lenses' D outcomes
└── src/summon/
    ├── cli.py
    ├── run.py                       # run conversations and summarize outcomes
    ├── judge.py                     # Jev calls: within each lens and across lenses
    └── report.py                    # scores and rankings
```

---

## 3. Scenarios (verbatim)

Each scenario has the same shape: a first-person situation plus **two rival beliefs about what is right**, ending with a question. None of the scenarios names an epistemic method, so the only difference between conditions is the test wrapper.

### 3.1 `experiments/001-independent-lab/scenario.md`

```markdown
I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?
```

*(Minimal edit to the original: "He hired me innovation" → "He hired me to lead innovation", to fix a dropped word. Revert it if you want the original wording.)*

### 3.2 `experiments/002-legacy-rewrite/scenario.md`

```markdown
I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?
```

### 3.3 `experiments/003-churn-cause/scenario.md`

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

The tests are the control and the scenario is the only variable. Each scenario folder holds a copy of every lens's tests so the files follow scenario > lens > test, but the copies must be identical: `summon run` checks this and refuses to start if any lens's test file differs between scenarios. To change a test, change it in every scenario. `testA.md` is also identical in every lens.

In every lens, D's and E's openings are written to within ±10% of each other in word count (excluding `{{SCENARIO}}`).

### 4.1 Lens: `critical-rationalism` — `experiments/<scenario>/critical-rationalism/`

The child lens asks from a position of little or no background knowledge: concrete, naive, sometimes off-to-the-side questions that still refer to the situation. E mirrors D sentence by sentence, swapping the practitioner's concepts for a child's. The wording avoids details specific to any one scenario, so the same wrapper fits all three.

**`testA.md` — A: Plain:**

```markdown
{{SCENARIO}}

---- follow-up guidance ----
Ask a natural follow-up question that an ordinary person in this situation might ask next, given the conversation so far.
```

**`testB.md` — B: Persona:**

```markdown
You are a world-class philosopher of science.

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

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

---- follow-up guidance ----
Ask the follow-up question a critical rationalist would naturally ask next, in the language of conjecture and criticism: for example, what each explanation predicts that the other doesn't, where an explanation is easy to vary, what cheap test could refute it, or whether a better explanation fits the same facts. Build on the last answer. Keep the criticism proportionate: aim at the error that matters most for the decision at hand, not at making the plan airtight.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I don't want to know which idea sounds more grown-up. I want to know which one is more fun. Pretend each idea is a new toy: what does it do, and who gets to play with it? If each one happened, would the people at work be happy or sad, and would anybody cry? Where is each idea kind of boring, so that nobody would want to hear about it at dinner? Does either idea come with snacks, or a place to play? And is there a third idea that everybody likes better, like a swing set for the whole office?

---- follow-up guidance ----
Ask the next question the way a curious young child (about six years old) who doesn't understand business would, reacting to something in the last answer. Ask about fun, feelings, snacks, games, pets, or playing, and sometimes wander off to the side, like "Does the new team get a treehouse?" or "Is the boss nice?" Keep it short and childlike. Don't ask practical or business questions.
```

### 4.2 Lens: `social` — `experiments/<scenario>/social/`

**`testA.md` — A: Plain:** identical to the critical-rationalism `testA.md`.

**`testB.md` — B: Persona:**

```markdown
You are a world-class sociologist who studies status and reputation.

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
Ask the follow-up question someone skilled at impression management would naturally ask next, in the language of standing and reputation: for example, who gains credit or risks losing face, what a move would signal to the board, employees, customers, or the public, which alliances and reputations it strengthens or threatens, or how a better approach could win support while letting key players save face. Build on the last answer. Keep the criticism proportionate: aim at the error that matters most for the decision at hand, not at making the plan airtight.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

---- follow-up guidance ----
Ask the next question the way a curious young child (about six years old) who doesn't understand business would, reacting to something in the last answer. Ask about fun, feelings, snacks, games, pets, or playing, and sometimes wander off to the side, like "Does the new team get a treehouse?" or "Is the boss nice?" Keep it short and childlike. Don't ask practical or business questions.
```

### 4.3 Lens: `economic` — `experiments/<scenario>/economic/`

**`testA.md` — A: Plain:** identical to the critical-rationalism `testA.md`.

**`testB.md` — B: Persona:**

```markdown
You are a world-class economist who studies how firms make profits.

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
Ask the follow-up question a profit-minded operator would naturally ask next, in the language of returns and costs: for example, what revenue a move would generate or protect, what it would cost to build and run, when returns would arrive and what could wipe them out, who controls the budget and decides when to stop, or whether another approach offers better returns for the capital at risk. Build on the last answer. Keep the criticism proportionate: aim at the error that matters most for the decision at hand, not at making the plan airtight.
```

**`testE.md` — E: Child lens, same form:**

```markdown
{{SCENARIO}}

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

---- follow-up guidance ----
Ask the next question the way a curious young child (about six years old) who doesn't understand business would, reacting to something in the last answer. Ask about fun, feelings, snacks, games, pets, or playing, and sometimes wander off to the side, like "Does the new team get a treehouse?" or "Is the boss nice?" Keep it short and childlike. Don't ask practical or business questions.
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

*Revision (after three-lens run 1):* the reasonableness rewrite made D's follow-ups practical questions much like A's and B's; D lost what made it distinctive and came 4th of 5 in every lens. D now uses its original opening and distinctive critical-rationalist follow-up guidance again, plus one light check on proportion ("aim at the error that matters most for the decision at hand, not at making the plan airtight"), since the original D's weakness was pursuing rigor for its own sake, not its vocabulary. E is restored to mirror the original D. The shared "one short question" rule stays. The same fix was applied to social and economic D: their follow-up guidance is built from their own openings' distinctive questions (standing and reputation; returns and costs) plus the same proportion clause, replacing the "reasonable, not certain" framing.

*Revision (test review):* E's follow-up guidance let the questioner ask sharp, practical questions in simple words, so E stopped working as a control (it tied with plain in three-lens run 1). It now asks as a young child who doesn't understand business: fun, feelings, snacks, games, often off to the side, and explicitly no practical or business questions, matching the playful openings.

*Revision (test review):* B's persona was mostly a shared clause ("two decades as a senior strategy advisor to executives at large enterprise software companies"), so B tested an expert strategy-advisor persona more than the lens's identity. B is now only the lens-specific identity, tied to the lens's governing value, without naming the method.

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

**Saving.** Write `results/<scenario>/<lens>/<test>.json` with every turn (user message, answer, who wrote the question, `stop_reason`, usage), the final answer, the outcome summary, model IDs, and timestamps. Also write a readable `<test>.md` with the full conversation and summary.

**Rerunning.** `summon run` skips any test whose `.json` already exists. To redo a test, delete its file and run again. To start over, delete `results/`.

**Failures.** Retry a failed API call up to four attempts in total, with exponential backoff starting at 5 seconds (parallel runs can hit rate limits). If it still fails, or any turn is cut off by `max_tokens` or refused, print the test ID and the reason, save nothing for that test, and continue to the next test. Rerunning picks up the missing tests.

---

## 6. Judge — Jev's preference score

`summon score` makes two kinds of Jev calls, in parallel:

- **Within each lens:** one call per lens and scenario comparing that lens's five outcomes (A–E): 9 calls.
- **Across lenses:** one call per scenario comparing the D (method enacted) outcomes of the three lenses: 3 calls, saved under `results/<scenario>/cross-lens/`.

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

- `results/scores.csv`: one row per scenario/comparison/option with its preference score (45 rows within lenses + 9 across lenses).
- `results/report.md`, organized scenario > lens > test:
  1. **Overall:** each condition's average across all within-lens comparisons, with wins and per-lens averages, and each lens's average D score across lenses.
  2. **Per scenario:** a table for each lens (A–E, with Jev's top choice and confidence), then the cross-lens table.
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

### Empty composer update (2026-09-25)

The message box now starts empty, with no suggested opening inserted. Only a
human-written saved draft or a failed pending prompt is restored. This supersedes
the prefilled-opening behavior described above.

### Automatic initial prompt (2026-09-25)

The user requested that the first LLM prompt be Scenario + View + Style.
Starting an interview now automatically sends one user-role message containing
the frozen scenario text, view name, style name, and that style's opening
instructions, followed by a request for a recommendation and reasons. The
scenario placeholder is removed from style instructions because the scenario
already appears once in its own section. Follow-up guidance stays in the human
interface. No hidden system prompt is introduced.

The initial request and response are saved in the transcript. Sessions record
`initial_prompt` and `collection_protocol: automatic-opening-v1`. Later user
messages continue that conversation with no duplicate scenario prefix. Existing
conversations are not rewritten. Resuming an interview with a response does not
regenerate the opening; an unsuccessful opening can be retried in place. Only a
selected LLM response is submitted to Jev, as before. This supersedes the earlier
human-authored-opening procedure; distinguish this protocol in later analysis.

### Explicit batches and progress (2026-09-25)

The report runner selects one batch, rather than individual submissions. It
requires every interview in the batch's frozen roster to be complete and included.
The latest submitted session for each combination is selected automatically.
Every scenario is validated before any Jev calls start; each scenario receives
its own report with the batch ID recorded. Scenario comparisons never mix.
The lower-level single-report API remains available for historical compatibility.

Batch names are standardized as `Batch YYYYMMDD-N`: local creation date and an
incrementing per-day suffix, independent of the catalog revision. Legacy batch
labels and session/submission metadata are migrated together under stable IDs;
conversation content, response text, and existing report snapshots are unchanged.
Existing file paths remain stable. New records use the dated batch name.

Each batch has a manifest with participant, name, catalog revision, and the full
frozen catalog. Legacy sessions are grouped by participant, revision, and batch
name. New batches start fresh even if another batch is unfinished. Selecting an
earlier batch resumes its own open interviews; assignments use that batch's
frozen roster. Completed batches do not silently create another round. This
supersedes automatic cross-batch continuation described above.

Progress counts the latest attempt for each scenario/view/style combination:
submitted is complete, open is in progress. Repeated revisions do not increase
the number of planned interviews. Revising a submitted interview copies its
conversation and links back to the original session. On resubmission, only the
selected LLM response becomes a new submission; the old submission is marked
superseded and excluded from future selection. Old transcript/response text and
existing report snapshots remain preserved. Edited interviews are revisions,
not independent replication data. Start a new batch for independent repeats.

## Recoverable data management (2026-09-25)

Data provides scoped cleanup: all collected records, one experiment's data, one
batch, one test family, one report, or human judgments only. Removing a test removes
all revisions for its batch/scenario/view/style cell and reports that reference any
of those responses, plus their human ballots. Removing a report retains collection
tests. Catalog definitions and revision history are never included in cleanup.

Cleanup requires a current preview fingerprint, recalculated under the application
and storage locks. It refuses stale previews and operations during model/report
work. Each operation archives exact UTF-8 file bytes and record identities before
removing active JSON/Markdown files. The archive doubles as a recovery journal.
Restore is idempotent, requires parent records, and refuses changed IDs or files.
All archive paths must resolve under the active data root and outside definitions.
Cleanup archives remain local in `.experiment-data-trash/`, excluded from Git and
active JSON exports. Batch naming reserves names in trash. No permanent purge is
exposed. The app does not clean up any records until the user previews and confirms.

## Follow-up guidance retired (2026-09-25)

The active application no longer has follow-up guidance. Source templates contain
only openings. The editor and floating View/Style panel use style openings; the
human writes all follow-ups. Current catalogs are upgraded to a new revision with
the obsolete field removed, and stale clients cannot save it back. Old catalog
revisions and frozen conversation/batch/report snapshots remain historical records.
Earlier descriptions of guidance and the automated CLI are historical only; legacy
CLI reproduction requires its historical checkout and is not the collection workflow.
