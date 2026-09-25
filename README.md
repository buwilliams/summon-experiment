# Summon experiment

## Human-led web workspace (current)

Summon has five browser screens: **Collect**, **Hypotheses**, **Analyze**,
**Results**, and **Data**. The subject is **GPT-6 Astra**
(`openai/gpt-6-astra` through OpenRouter); Jev remains the judge.

### Start locally on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\summon-web.exe
```

Or use `uv sync` and `uv run summon-web`. Open http://127.0.0.1:8765.
Set `OPENROUTER_API_KEY` in the gitignored `.env` file. Both providers use this
key; it stays on the server. `SUMMON_PORT` overrides port 8765. No WSL is required.
The server binds to loopback and supports people sharing a local computer, not public hosting.

On opening the app, enter your name. It is remembered for the browser tab session,
including refreshes. Use **Switch user** in the header to enter another name or
select a previous participant. Collect shows only your batches; new batches,
sessions, submissions, and human judgments carry your name. Definitions, reports,
and data management remain shared. Names are identifiers, not authentication.
Existing records keep their original participant names.

### Collect and compare

Collect opens with hypothesis cards, then experiment cards. The experiment screen
shows the case and a single start action; existing batches appear below it. Starting
creates a batch and opens Astra's first recommendation. A batch screen holds progress,
resume, review/revision, and the Analyze handoff. Breadcrumbs return to these choices
without adding setup controls to the conversation. Tests and styles are assigned by
the system, and the floating assignment remains beneath the composer.

Batch names use **Batch YYYYMMDD-N**. Each session submits one selected assistant
response. Revising preserves the original and replaces its submission for future
reports; existing reports retain their frozen inputs.

1. Open **Collect**. The system resumes unfinished work or assigns the next
   experiment, test, and style automatically. The experiment appears in the conversation.
   The app sends the experiment, test, and style to Astra automatically and requests
   a recommendation with reasons. Then the empty message box lets you question
   that response. The exact initial prompt is available in the conversation.
   Participant and batch are managed locally.
2. Select any complete assistant response as the solution. This freezes the
   session and submission. Full messages, model output, usage, and timestamps are retained.
3. The editor can add/edit experiments, tests, and styles. Each save starts a new
   catalog revision; existing sessions keep their original content. Submission
   notes and inclusion can change, but submitted text cannot be silently rewritten.
4. Select a completed batch in Analyze. It uses the latest submitted
   response for each session and creates a report for the experiment.
   Every planned session must be submitted and included; readiness is shown
   before running. Use a new batch for independent repeats.
5. Jev compares every pair within each test, in both answer orders. Mean
   preference determines the test winner; tied winners all advance. Winners from
   different tests are then compared pairwise. Results retains raw calls,
   order effects, coverage, and rankings. Failed/interrupted reports can resume.

Web data lives in **`experiment-data/`**, as Git-trackable JSON plus readable
Markdown companions. See [the data layout](experiment-data/README.md). JSON is
the source of truth; Markdown is generated on each save. Every catalog revision
is retained. Use **Export workspace** for a combined JSON export, or back up the
folder with the server stopped. Run only one server process per data folder.
Existing `data/summon.sqlite3` is automatically migrated and verified on first
startup, then retained locally as a backup. Old `data/` logs stay gitignored.
Saving data does not automatically commit or push it to GitHub.
Large answers are sent verbatim; a provider context-limit error leaves the report
failed and resumable, never silently truncated or summarized. API calls incur
normal provider charges. A five-style test requires 20 Jev calls; three tests
usually require 66 calls including the winner round (ties increase that count).

Validation: `.\.venv\Scripts\python.exe -m unittest discover -s tests -v`.
Tests use a fake gateway and temporary data folders, without paid calls.

Protocol details and limitations are at the top of [spec.md](spec.md).

## Experiment definitions

The three experiments and three tests (critical rationalism, social, economic),
with prompting styles A–E, remain in `experiments/` and the saved catalog in
`experiment-data/catalog/`. These are the definitions for fresh batches.

Collected automated results and previous interview data were cleared from the
working tree on 2026-09-25. No old scores are presented as current evidence.
The original CLI code remains available for historical reproduction; new data
collection uses the web app.

### Hypotheses, experiments, tests, and human judging

The definition hierarchy is **Hypothesis → Experiment → Test → Style**.
An experiment is one case (formerly called a scenario), not a container of cases.
A test supplies a perspective, such as Critical Rationalism, Economic, or Social.
Styles A–E specify how to prompt within that test. **Collect** creates batches
for one experiment and assigns a chat session for each test/style combination.

In **Analyze**, select a completed batch and run Jev reports. Then choose **Compare responses**; your active name identifies your judgments. Compare anonymous A/B responses, choose
A, B, or a tie, and optionally record why. Jev's judgment appears after saving your
preference. Resume with the same reviewer name; recorded preferences are preserved.

**Results** shows human preferences separately from Jev probabilities, including pair
coverage and agreement. Full Jev results appear after that reviewer completes the report.
Cross-test comparisons continue to use Jev's finalists. Reviewer names identify local
records, not accounts. The exported workspace includes human judgment records.

New JSON and Markdown records follow `hypotheses/…/experiments/…/batches/…/`, with
`tests/`, `reports/`, and `judgments/` beneath each batch. Catalog revisions retain
hypothesis statements and experiment scopes. Chat displays Markdown while preserving
the original text for submission and judging.

### Development cleanup

Open **Data** to see record counts, export the active workspace, and preview cleanup.
You can remove one report, a session and its complete revision history, a whole batch,
all collected data for an experiment, human judgments only, or all collected data.
The preview includes dependent reports and human judgments. Confirm with **Move these
records to trash**; **Restore** returns the saved files without overwriting changes.

Hypotheses, experiment definitions, tests, styles, and catalog
revision history are retained. Trash is stored locally in `.experiment-data-trash/`
and ignored by Git. The workspace export contains active data; back up the trash
folder separately if you want to retain cleanup archives when moving the project.
Model requests and running reports must finish before cleanup or restore. Interrupted
cleanup/restores resume at startup. Batch date suffixes are not reused after cleanup.

### Focused hypothesis editor

The **Hypotheses** screen drills down through hypothesis → experiment → test →
style. Each level shows its own editable content and the next choices. Breadcrumbs
return to parent levels. Type in an editable dropdown to rename its selected record;
use the centered chevron to select a sibling or the adjacent + to add one.

Definitions, submission notes, and inclusion changes save automatically after a
short pause. A status shows Saving, Saved, or a save error. Incomplete new records
are kept as local drafts until required fields are filled. Drafts also survive a
reload or failed request. A conflicting server revision is never silently overwritten.

Active catalog schema 2 stores experiment text directly on each experiment;
there is no separate scenario list or study container. Internal `views`, `view_ids`,
and session `scenario`/`view` keys remain compatibility names for tests and frozen
experiment context. Opening templates now use `{{EXPERIMENT}}`; the old token is
still recognized when reading historical files. Original source templates under
`experiments/` are seed material, not the live catalog.

The trash icon beside each definition selector deletes that definition and returns
to its parent. Undo restores the most recent deletion until another edit is made.
Hypothesis deletion includes its experiments; test deletion removes the selected
experiment's membership. Styles are shared within a test, so deleting a style applies
to every experiment using that test. Existing collected batch snapshots are unchanged.
The final required hypothesis/experiment, test in an experiment, or style in a test
cannot be removed; its disabled trash icon explains the requirement.

### Focused analysis, results, and data

Analyze and Results use hypothesis → experiment → batch → report breadcrumbs.
Analyze exposes the next useful action: collect missing responses, run or resume
Jev, then compare anonymous responses. A completed report opens the human-judging
step; rerunning Jev is a secondary disclosure. Collect hands off directly to its
batch in Analyze.

Results first offers a choice of human judgments, rankings within a test, rankings
across test winners, or comparison records. Tables and raw pair records appear only
after choosing them. Jev rankings remain hidden until the current reviewer finishes
judging. Reports remain discoverable through their saved hypothesis and experiment
snapshots even if the live definitions have been deleted.

Data opens with Clean up, Trash, and Export. Cleanup proceeds from scope to a record
to a separate dependency-count preview, then moves the confirmed selection to trash.
Trash opens a selected archive before offering restoration. Existing fingerprint,
busy-request, and restore-conflict checks remain in force.

Frontend checks: `node --test tests/*.test.cjs`.
