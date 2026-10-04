# Publishing Frontier Wire

The publication route is unchanged: `ADanMan/frontier-wire`, branch `main`,
GitHub Pages from `/docs`, at https://adanman.github.io/frontier-wire/.
The edition covers AI, tech, science, world, culture and economy in RU + EN.
Follow [FORMAT.md](../FORMAT.md); omit rubrics without worthwhile verified news.

The requested editor schedule is 07:00 and 19:00 in `Europe/Moscow`. Configure exactly one
editor automation in the assistant that owns the schedule. This repository does
not install a scheduler or invoke Claude. The existing digest bridge only
collects source material; it is not a second editor. Leave its schedule alone.

## Before writing

1. Fetch the latest `main` into a clean checkout. Do not reset someone else's
   changes. Read this file, `FORMAT.md` and today's edition if it already exists.
2. Compute today's date in `Europe/Moscow`, regardless of the runner's timezone.
   Choose `morning` for the 07:00 slot and `evening` for 19:00. For the initial
   one-off restoration use `recovery`. If the corresponding file under
   `publication_runs/<year>/<date>-<slot>.json` is already on remote `main`,
   the slot is complete: verify it and stop without adding more articles.
3. Require a current-day digest under `digests/<year>/<date>.md`. Reuse the
   bridge's fresh digest when available; otherwise run
   `TZ=Europe/Moscow python3 scripts/digest.py` on an available networked runner.
   Never relabel an old digest or fill missed publication days in bulk.
4. Read the full source pages before selecting stories. Check the original
   publication date separately from the digest date. A short feed summary,
   inaccessible article or paywall is insufficient evidence for an expanded
   story. Use accessible primary material where possible, distinguish reported
   claims from findings, and do not present planned events as completed.
5. Compare candidates with existing articles. Treat URLs differing only in
   tracking parameters or fragments as the same source. Check topic/headline
   overlap too, since the same event can appear at multiple URLs. A genuine
   follow-up needs a new verified development and source.

## Write, check and publish

Write 5–8 worthwhile articles when sources support them; fewer is preferable to
padding. Use original prose, living Russian and idiomatic English, with inline
source links and the required ending sections. Put factual verification notes
in today's digest in your own words; do not copy whole source articles.

For a new day, create `index.md` with the next edition number after the latest
published cover. For the evening slot, append to the same day's directory and
continue article numbering. Update both editorials and the marked README
edition block. Do not rewrite earlier articles simply to create fresh content.

Run the guard with the **new article basenames** only, for example:

```bash
python3 scripts/publication_check.py --slot morning 01-first-story.md 02-second-story.md
python3 scripts/build_site.py
python3 -m unittest discover -s tests
git diff --check
```

The guard enforces the current Moscow date, today's digest, source provenance,
known duplicate URLs, article metadata and bilingual format. It cannot establish
whether a factual claim is true; source verification remains the editor's job.
Review the generated homepage, article pages, RSS and JSON feeds, and their
relative links. Prepare the Telegram summary as a file in `telegram/`; this
workflow does not send messages to subscribers.

After those checks pass, run the same guard with `--record`. Include its new
`publication_runs/` marker in the same commit as the edition, digest, README,
generated `docs/` and Telegram summary. The marker stores article checksums and
makes retries of that slot stop. It is a record of the batch, not proof that a
remote push or deployment succeeded.

Fetch again before pushing. If remote `main` changed, preserve those changes,
reconcile the edition and marker, rerun checks and rebuild. Never force-push.
Push normally, confirm remote `main` equals the intended commit, then wait for
the existing Pages deployment and read the live latest-edition endpoint. If a
push or deployment is uncertain, inspect remote state before retrying; do not
generate a second batch to compensate.

## Access and runner availability

The editor needs read/write access to this existing GitHub repository, open
source-page reads and Python 3.9+ with the system timezone database. No new model
API key or Claude subscription is required for these repository scripts. Use
the current authorized GitHub connection; do not export tokens or modify access.

A publisher running in the cloud can continue while the Mac is switched off
only if that automation has its own working GitHub access, source reads and
execution environment. A local Mac automation needs the Mac awake and online.
Verify the actual automation environment before promising unattended delivery.
The website itself is hosted by GitHub Pages and stays online independently.

## Restoration checkpoint

The last pre-restoration edition was №28, 2026-09-30. Digests and Pages builds
continued after that; the missing component was the external editor, which the
owner confirmed no longer runs. The original publisher prompt was not found in
the available Mac files; the schedule and format above come from the existing
repository requirements. No prior editor scheduler was recreated here.
