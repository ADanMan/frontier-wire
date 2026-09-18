# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №16 / Edition №16 — 2026-09-18** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [В Нигерии паленый алкоголь убил почти полсотни человек](editions/2026/09-18/01-nigeria-methanol-alcohol-deaths.md)
- **[Наука]** [Астрономы нашли самую молодую известную планету](editions/2026/09-18/02-youngest-known-planet-elias-2-24b.md)
- **[Культура]** [Ацтекский манускрипт вернулся в Мексику — но только в долг](editions/2026/09-18/03-aztec-manuscript-returns-mexico.md)
- **[Экономика]** [Настоящие богачи Америки прячутся не в списке Forbes](editions/2026/09-18/04-hidden-millionaires-planet-money.md)
- **[Технологии]** [Кто-то целенаправленно охотится за аккаунтами разработчиков Rust](editions/2026/09-18/05-rust-crates-targeted-attacks.md)
- **[ИИ]** [ИИ-индустрия тихо меняет фокус: с обучения на вывод](editions/2026/09-18/06-ai-inference-revolution.md)
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
