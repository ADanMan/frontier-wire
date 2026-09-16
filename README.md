# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №14 / Edition №14 — 2026-09-16** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Технологии]** [SpaceX объявила дату первого орбитального полёта Starship](editions/2026/09-16/01-spacex-starship-orbital-launch.md)
- **[Мир]** [Власти ДРК заявили, что вспышка Эболы прошла пик](editions/2026/09-16/02-ebola-drc-outbreak-peaked.md)
- **[ИИ]** [Лидеры ИИ-индустрии просят регуляций, Трамп называет тревогу «фейками»](editions/2026/09-16/03-ai-regulation-trump-hoaxes.md)
- **[Наука]** [Извержение вулкана Тонга неожиданно уничтожало метан в атмосфере](editions/2026/09-16/04-tonga-volcano-methane.md)
- **[Мир]** [В Пенсильвании от осложнения кори умер 18-летний подросток](editions/2026/09-16/05-measles-death-pennsylvania.md)
- **[Наука]** [Что такое загадочная программа Ленглендса — и почему математики о ней спорят десятилетиями](editions/2026/09-16/06-langlands-program-explainer.md)
- **[Культура]** [Стратегический нефтяной резерв США устроен как гигантская подземная архитектура](editions/2026/09-16/07-strategic-oil-reserve-architecture.md)
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
