# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №2 / Edition №2 — 2026-09-04** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Технологии]** [«Skills» для ИИ-агентов ворвались в тренды GitHub — сразу два репозитория](editions/2026/09-04/01-agent-skills-github-trend.md)
- **[ИИ]** [Миллиарды токенов из старых газет: как ИИ учится на архивах](editions/2026/09-04/02-newspapers-pipeline-tokens.md)
- **[ИИ]** [Судьи для ИИ-агентов сами не проходили экзамен](editions/2026/09-04/03-agentjudgebench.md)
- **[ИИ]** [Не «похоже», а «то самое»: как научить ИИ узнавать редкие объекты на фото](editions/2026/09-04/04-entity-aligned-vqa.md)
<!-- EDITION:END -->

[Full archive →](editions/)

## How it works

1. `python3 scripts/digest.py` pulls RSS/Atom feeds from [`feeds.txt`](feeds.txt),
   arXiv and trending repos into `digests/<year>/<date>.md`. Every item carries a
   real source URL; nothing is invented downstream.
2. A scheduled cloud routine reads the digest, writes 5–8 articles into
   `editions/<year>/<mm-dd>/` (format: [`FORMAT.md`](FORMAT.md)), updates this
   README, rebuilds the site (`python3 scripts/build_site.py` → `docs/`), and pushes.
3. Once a week the routine runs the **feed-gardener** skill
   ([`.claude/skills/feed-gardener/`](.claude/skills/feed-gardener/SKILL.md)):
   prunes dead feeds and plants new sources in `feeds.txt` — the garden idea
   borrowed from [OpenPlanter](https://github.com/ShinMegamiBoson/OpenPlanter).

The routine's sandbox can only reach `raw.githubusercontent.com`, so `feeds.txt`
leads with RSS mirrors hosted there; the open-network sources below them enrich
the digest whenever the scripts run on a normal connection and are skipped
silently otherwise.

## Run it yourself

No API keys needed:

```bash
python3 scripts/digest.py      # fetch today's raw material
python3 scripts/build_site.py  # rebuild the static site into docs/
```

## Publisher

Made by [Danila Katalshov](https://adanman.github.io) —
[LinkedIn](https://www.linkedin.com/in/danilakatalshov) · [Telegram](https://t.me/adanman).
Sibling project: [agentic-frontier](https://github.com/ADanMan/agentic-frontier),
a personal learning-in-public log on AI engineering.

## License

[MIT](LICENSE) — take anything useful.
