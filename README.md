# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №26 / Edition №26 — 2026-09-28** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [В Южной Африке за одни выходные расстреляли 27 человек — в двух разных местах](editions/2026/09-28/01-south-africa-mass-shootings.md)
- **[Мир]** [Вучич уходит с поста президента Сербии — но метит в премьеры](editions/2026/09-28/02-serbia-vucic-resignation.md)
- **[Экономика]** [Польша заливает деньгами оборонку. Экономике это поможет или навредит?](editions/2026/09-28/03-poland-defense-boom-economy.md)
- **[Наука]** [Популярную добавку для суставов связали с более быстрым развитием деменции](editions/2026/09-28/04-glucosamine-alzheimers-risk.md)
- **[ИИ]** [Глава Anthropic впервые сядет ужинать с Трампом один на один](editions/2026/09-28/05-amodei-trump-dinner.md)
- **[Культура]** [2300 часов в бейсбольном симуляторе — и это не даже не MLB The Show](editions/2026/09-28/06-ootp-baseball-review.md)
- **[Наука]** [У берегов Канады нашли два новых вида морских пауков](editions/2026/09-28/07-sea-spiders-new-species.md)
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
