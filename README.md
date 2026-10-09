# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №34 / Edition №34 — 2026-10-09** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [Falcon ASR делает ставку на арабские диалекты и отметки времени для каждого слова](editions/2026/10-09/01-falcon-arabic-asr.md)
- **[Технологии]** [SSPICY готовится осмотреть неработающие объекты на орбите без стыковки](editions/2026/10-09/02-sspicy-orbital-inspection.md)
- **[ИИ]** [Статистики предлагают читать горизонты ИИ вместе с графиками сложности задач](editions/2026/10-09/03-metr-time-horizon-statistics.md)
- **[ИИ]** [Hugging Face показала обучение небольших моделей через ML Intern с проверками и бюджетом](editions/2026/10-09/04-ml-intern-training-cases.md)
- **[Экономика]** [Исследование 50 карточных наборов обнаружило нехватку сведений о шансах на редкие карты](editions/2026/10-09/05-trading-card-odds.md)
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
