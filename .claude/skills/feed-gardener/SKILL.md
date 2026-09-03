---
name: feed-gardener
description: Weekly tending of feeds.txt — prune dead feeds, plant new sources, hunt for sandbox-reachable RSS mirrors. Use when asked to update, garden, or expand the publication's sources.
---

# Feed gardener

Tend `feeds.txt` the way OpenPlanter tends a garden: keep what bears fruit,
pull what died, plant something new every visit.

## Procedure

1. **Census.** For every URL in `feeds.txt`, try fetching it (10s timeout).
   Classify: alive (parses as RSS/Atom with items), dead (404/parse error for
   the 3rd consecutive week), blocked (network refuses — normal in the sandbox
   for anything that is not raw.githubusercontent.com; NOT dead).
2. **Prune.** Remove only feeds that are *dead*, never ones that are merely
   *blocked*. Note removals in the commit message.
3. **Plant.** Add 1–3 new sources per visit. Priorities, in order:
   a. **raw.githubusercontent.com mirrors** of general-news/science/culture
      feeds — the standing quest; these are the only feeds the sandbox can
      read, and today's mirrors are tech-only. Search GitHub for repos that
      rebuild RSS mirrors on a schedule (recent commits = alive).
   b. Well-known open-network feeds in under-represented rubrics
      (world, culture, science).
4. **Order.** Mirrors stay at the top of the file — digest.py walks top-down
   and caps totals. Keep the section comments intact; every new URL gets an
   inline `# note`.
5. **Verify.** Run `python3 scripts/digest.py` (delete today's digest first if
   it exists) and confirm the item count did not drop.
6. Commit `feeds: garden <date> (+N, -M)` and push.

## Hard rules

- Never remove the raw.githubusercontent mirror block wholesale.
- Never add feeds requiring auth or keys.
- A blocked fetch inside the sandbox proves nothing — when in doubt, keep.
