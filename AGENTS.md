# Agent instructions: running the Summon experiment

## Current web application

New work uses the human-led web app (`summon-web` / `python -m summon.web`).
Read the current protocol at the top of `spec.md`. The instructions below refer
to historical CLI reproduction. Do not run the old automated pipeline to collect
new human-led data. Use the Windows checkout; WSL is not needed.

The web app uses GPT-6 Astra and Jev via server-side `OPENROUTER_API_KEY` in `.env`.
Never print or commit keys. Data is in Git-trackable `experiment-data/` JSON and Markdown files; preserve
it and archived results. JSON is authoritative; Markdown companions are generated.
Catalog revisions are retained. Run one server process per data folder. The old
SQLite file is a local migration backup only. Test with temporary
data folders and fake gateways (`python -m unittest discover -s tests -v`); keep
connection smoke checks out of experiment data. No system prompts, tools,
sampling overrides, or model fallbacks. Submitted responses and report snapshots
are immutable. Catalog edits affect new sessions only.

## Historical data cleanup

On 2026-09-25 the user requested clearing all collected automated results and
interview batches while retaining scenarios, lenses, and styles. Collected data
was moved to a verified local backup outside this repository. Do not reimport
it or old SQLite data without an explicit request. Historical CLI code remains
for reference; use the web app for new collection.
