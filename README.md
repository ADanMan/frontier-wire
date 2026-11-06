# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №51 / Edition №51 — 2026-11-06** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/e/2026-11-06/)

- **[ИИ и технологии]** [Cosmos 3 разводит генерацию сцены и проверку физического мира](editions/2026/11-06/01-cosmos-interactive-worlds.md)
- **[ИИ и технологии]** [Gemini Omni 1.2 Flash удлиняет клипы и предлагает правки разговором](editions/2026/11-06/02-omni-longer-video.md)
- **[ИИ и технологии]** [Австралийские университеты связывают доступ к ИИ с правилами оценки знаний](editions/2026/11-06/03-university-ai-assessment.md)
- **[Наука]** [NASA представило X-70 как перенастраиваемую платформу лётных испытаний](editions/2026/11-06/04-x70-research-platform.md)
- **[Наука]** [NASA выбрало три компании для разработки Ka-band ретрансляции](editions/2026/11-06/05-ka-band-relay-concepts.md)
- **[ИИ и технологии]** [ToyBlocks превращает кубики в стенд для проверки роботов](editions/2026/11-06/06-toyblocks-controlled-robotics.md)
- **[ИИ и технологии]** [Open ASR Leaderboard добавил египетский и нигерийский английский](editions/2026/11-06/07-asr-accent-evaluation.md)
- **[ИИ и технологии]** [LeRobot 0.7 добавил диалог с работающей политикой робота](editions/2026/11-06/08-lerobot-interactive-release.md)
- **[Наука]** [МКС завершила установку восьми дополнительных солнечных батарей](editions/2026/11-06/09-iss-final-solar-array.md)
- **[Наука]** [Снимок Goosenecks показывает реку, врезавшуюся в старые изгибы](editions/2026/11-06/10-goosenecks-orbital-view.md)
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
