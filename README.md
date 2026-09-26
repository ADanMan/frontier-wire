# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №24 / Edition №24 — 2026-09-26** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [Суд разрешил Трампу «чернить» Anthropic за отказ снимать ограничения с Claude](editions/2026/09-26/01-anthropic-blacklist-court-ruling.md)
- **[Технологии]** [Франция запретила соцсети детям до 15 — подросткам этого мало](editions/2026/09-26/02-france-social-media-ban-kids.md)
- **[Мир]** [Глава властей Йемена призвал к всеобщей мобилизации против хуситов](editions/2026/09-26/03-yemen-houthis-mobilization.md)
- **[Наука]** [Учёные впервые засняли, как тектоническая плита рвётся на куски у берегов Канады](editions/2026/09-26/04-pacific-northwest-subduction-zone.md)
- **[Наука]** [CRISPR научили бить по раку крови, не задевая здоровые клетки](editions/2026/09-26/05-crispr-blood-cancer-trial.md)
- **[Экономика]** [Экономист Банка Англии предложила считать риски жилья не средней ценой, а веером сценариев](editions/2026/09-26/06-uk-housing-market-risk-model.md)
- **[Культура]** [Азербайджанский роман «My Dreadful Body» переводит телесность в язык — и получает редкие похвалы](editions/2026/09-26/07-dreadful-body-azerbaijan-novel.md)
- **[Мир]** [Военный самолёт рухнул на жилой квартал в Конго — погибли больше десяти человек](editions/2026/09-26/08-dr-congo-plane-crash.md)
- **[Экономика]** [Индийский миллиардер готовит крупнейшее IPO в Лондоне за много лет](editions/2026/09-26/09-airtel-money-london-ipo.md)
- **[Наука]** [ЦЕРН начал отключать Большой адронный коллайдер ради магнитов на 40% мощнее](editions/2026/09-26/10-cern-lhc-upgrade-disconnect.md)
- **[Технологии]** [Присяжные признали Facebook виновной в обмане пользователей по делу Cambridge Analytica](editions/2026/09-26/11-facebook-cambridge-analytica-liable.md)
- **[ИИ]** [Кто отвечает, если взломал не человек, а ИИ-агент](editions/2026/09-26/12-ai-agents-hacking-accountability.md)
- **[Мир]** [Верховный суд США заблокировал округа Миссури, перекроенные в пользу Трампа](editions/2026/09-26/13-scotus-missouri-map-blocked.md)
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
