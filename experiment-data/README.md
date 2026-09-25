# Experiment data

This folder is the web application's live storage and is readable on GitHub.
JSON files are authoritative. Matching Markdown files are generated for reading;
edit through the web application so both stay in sync.

```text
catalog/
  revision-000006.json           Hypotheses, experiments, tests, styles
  revision-000006.md             Readable definitions; earlier revisions retained
hypotheses/
  <name-id>/
    experiments/
      <name-id>/
        batches/
          <batch-name-id>/
            batch.json          Participant, experiment snapshot, frozen session roster
            batch.md            Readable batch overview
            tests/
              test-<id>/
                session.json    Transcript, settings, provenance, raw model calls
                session.md      Readable conversation
                submission.json Selected response and research notes
                submission.md   Readable submitted solution
            reports/
              <name-id>.json    Frozen inputs, Jev calls, probabilities, rankings
              <name-id>.md      Readable Jev results
            judgments/
              <id>.json         Human reviewer, display order, choice, reason, time
              <id>.md           Readable human judgment
```

The definition hierarchy is Hypothesis → Experiment → Test → Style. An experiment
is one case. A test is a perspective such as Economic or Social. Its batches repeat
the test × style combinations. Each conversation is a session, and only its selected
response is judged. Batch snapshots freeze the definitions used for collection.

Catalog schema 2 stores the case text directly in `experiments`; there is no separate
scenario list. Internal `views` and `view_ids` keys mean tests; session `scenario` and
`view` keys hold the frozen experiment and test. The `tests/` directory is a legacy
storage name for sessions. These compatibility names do not add UI hierarchy levels.

This hierarchy applies to new records. Existing `batches/` and `scenarios/` paths
are retained so earlier evidence and links remain intact. Full names and IDs are
stored in JSON; compact folder names keep paths within Windows limits.

Human judgments are separate from Jev reports. A named reviewer gets a persistent,
randomized A/B order for each pair and can choose A, B, or a tie. Saved preferences
are immutable; retries cannot overwrite them. The UI reveals Jev scores and style
labels only after the choice is saved. Reviewer names are local identifiers, not
accounts; raw files and exports remain available to the workspace owner.

Cross-test comparisons use Jev's finalists. Human votes describe the same pairs,
not an independently selected human tournament. Human preference shares and Jev
probabilities are kept separate in Results.


Session records identify the participant and catalog revision. Separate sessions
can share the same experiment, batch, test, and style. Short ID suffixes distinguish
names that would otherwise collide; full IDs remain inside the JSON files.
Existing paths stay stable when a record is saved again.

Batch progress is calculated from the latest session for each experiment/test/style
combination. Revised sessions link to their predecessor with `revises`; replacement
submissions use `replaces` and `superseded_by`. Previous content is retained.

Submitted solutions and report input snapshots are preserved. Submission notes
and inclusion can change without rewriting earlier reports. Reports checkpoint
each Jev call; unfinished reports can resume from those files.

All JSON/Markdown here can be committed normally. Saving in the app does **not**
automatically commit or push. Review transcripts and raw model responses before
publishing, just as you would any experiment data. API credentials stay in the
ignored `.env`, outside this folder.

The server writes files atomically and uses an ignored `.pending.json` journal
to finish interrupted saves after restart. Run one server per data folder. Stop
the server before restoring backups, manually editing records, or switching data
branches. Back up this whole folder or use the app's combined JSON export.

Previous SQLite data, automated results, and interview data were cleared from
this working tree on 2026-09-25. A verified local backup is outside the repository.
The catalog and source experiment definitions were retained.

## Recoverable cleanup

The Data screen previews removal of collected records and their dependencies. It
keeps every catalog revision. Before removing files, it saves and verifies an exact
JSON/Markdown snapshot in the sibling `.experiment-data-trash/` folder. That folder
is ignored by Git and does not appear in active workspace scans or exports.

Restore checks parent dependencies and conflicts before restoring original files.
Archives are durable operation journals as well as backups, so interrupted removals
or restores finish on restart. There is no automatic permanent deletion. Back up
`.experiment-data-trash/` separately if you want to keep these archives off-device.
