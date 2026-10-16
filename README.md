# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №38 / Edition №38 — 2026-10-16** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/e/2026-10-16/)

- **[Наука]** [NASA описала свой вклад в MMX перед планируемым запуском к спутникам Марса](editions/2026/10-16/01-mmx-nasa-launch-preparations.md)
- **[Экономика]** [Исследователи Банка Англии применили языковую модель к рассказам компаний об изменении цен](editions/2026/10-16/02-inflation-business-narratives.md)
- **[ИИ]** [FLUX.3 Image Klein появился в Diffusers с управлением расположением частей изображения](editions/2026/10-16/03-flux3-layout-generation.md)
- **[ИИ]** [NVIDIA и AI4Bharat анонсировали корпус на 2,8 трлн токенов для индийских языков](editions/2026/10-16/04-indic-pretraining-corpus-announcement.md)
- **[ИИ]** [IBM представила Granite Switch 4.1: речь, диалог и классификация в одной сборке](editions/2026/10-16/05-granite-switch-modular-models.md)
<!-- EDITION:END -->

[Full archive →](editions/)

## How it works

1. `python3 scripts/digest.py` pulls RSS/Atom feeds from [`feeds.txt`](feeds.txt),
   arXiv and trending repos into `digests/<year>/<date>.md`. Every item carries a
   real source URL; nothing is invented downstream.
2. A scheduled editor reads the digest, verifies the full sources, and writes 5–8 articles into
   `editions/<year>/<mm-dd>/` (format: [`FORMAT.md`](FORMAT.md)), updates this
   README, rebuilds the site (`python3 scripts/build_site.py` → `docs/`), and pushes.
   The editor follows [`tasks/publishing.md`](tasks/publishing.md); a current-day
   check and per-slot record prevent duplicate batches. Repository scripts need
   no Claude installation. The owning assistant configures one editor schedule
   at 07:00 and 19:00 `Europe/Moscow`.
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
