# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №17 / Edition №17 — 2026-09-19** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [ИИ Google сам взломал три компании — и сам же остановился](editions/2026/09-19/01-gemini-ai-hacks-three-companies.md)
- **[Технологии]** [Виргиния — «столица дата-центров мира» — решила притормозить их стройку](editions/2026/09-19/02-virginia-ai-data-center-task-force.md)
- **[Мир]** [США и Дания договорились по Гренландии — но не факт, что об одном и том же](editions/2026/09-19/03-us-denmark-greenland-deal.md)
- **[Мир]** [Депортированных из США людей избили в отеле-тюрьме в Экваториальной Гвинее](editions/2026/09-19/04-equatorial-guinea-deportees-beaten.md)
- **[Экономика]** [Япония подняла ставку до максимума за 31 год — инфляцию туда занесло войной в Иране](editions/2026/09-19/05-japan-interest-rate-31-year-high.md)
- **[Наука]** [Крошечный чип Caltech перенаправляет свет за 74 квадриллионных долей секунды](editions/2026/09-19/06-caltech-light-steering-chip.md)
- **[Наука]** [Ядерные испытания Северной Кореи, похоже, ещё годами трясли землю](editions/2026/09-19/07-north-korea-nuclear-tests-earthquakes.md)
- **[ИИ]** [Документы суда: OpenAI и Microsoft сами знали, что запускают «петлю гибели» для веба](editions/2026/09-19/08-openai-microsoft-doom-loop.md)
- **[Мир]** [Макрон: гибридные атаки России на Европу усиливаются](editions/2026/09-19/09-macron-russia-hybrid-attacks.md)
- **[Экономика]** [Пшеница подорожала до максимума за три года — а фермеры всё равно не в плюсе](editions/2026/09-19/10-us-wheat-farmers-drought.md)
- **[Культура]** [Толстые медведи Аляски выходят на самый массовый турнир Fat Bear Week](editions/2026/09-19/11-fat-bear-week-2026.md)
- **[Наука]** [Физики нашли способ проверить, действует ли гравитация Эйнштейна на «вторую копию» электрона](editions/2026/09-19/12-muonium-einstein-gravity-test.md)
- **[Мир]** [Похищенную в Малави британку освободили после перестрелки с похитителями](editions/2026/09-19/13-malawi-kidnapping-rescue.md)
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
