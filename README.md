# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №27 / Edition №27 — 2026-09-29** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [OpenAI сама остановила выпуск GPT-6.1 Astra](editions/2026/09-29/01-openai-astra-safety-pause.md)
- **[Мир]** [В Конго убили политика за призыв беречься от Эболы](editions/2026/09-29/02-drc-politician-ebola-killed.md)
- **[Мир]** [Венгрия сняла неприкосновенность с действующего премьера](editions/2026/09-29/03-hungary-lifts-magyar-immunity.md)
- **[Экономика]** [США и Китай снижают пошлины — но не на самое важное](editions/2026/09-29/04-china-us-tariff-cuts.md)
- **[Наука]** [Математики закрыли гипотезу, которой было 55 лет](editions/2026/09-29/05-juggling-conjecture-solved.md)
- **[Культура]** [Умер Майти Спэрроу — король калипсо](editions/2026/09-29/06-mighty-sparrow-calypso-king-dies.md)
- **[Мир]** [В ЮАР за один уик-энд застрелили 27 человек](editions/2026/09-29/07-south-africa-mass-shootings.md)
- **[ИИ]** [Флорида судится с OpenAI из-за рисков вымирания человечества](editions/2026/09-29/08-florida-sues-openai-frontier-ai.md)
- **[Наука]** [Вселенная плоская — но не факт, что бесконечная](editions/2026/09-29/09-is-the-universe-infinite.md)
- **[Экономика]** [Канцлер Хили обещает реиндустриализировать Британию](editions/2026/09-29/10-healey-reindustrialise-britain.md)
- **[Мир]** [Иранского адвоката Насрин Сотудэ наградили премией имени Гавела](editions/2026/09-29/11-sotoudeh-havel-prize.md)
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

## MCP server

`mcp/server.py` is a minimal stdlib-only MCP server (stdio transport) exposing three
read-only tools over the published site: `get_latest_edition`, `get_feed`, and
`search_articles`. Clone the repo, then register it in Claude Code:

```bash
claude mcp add frontier-wire -- python3 /path/to/frontier-wire/mcp/server.py
```

## Publisher

Made by [Danila Katalshov](https://adanman.github.io) —
[LinkedIn](https://www.linkedin.com/in/danilakatalshov) · [Telegram](https://t.me/adanman).
Sibling project: [agentic-frontier](https://github.com/ADanMan/agentic-frontier),
a personal learning-in-public log on AI engineering.

## License

[MIT](LICENSE) — take anything useful.
