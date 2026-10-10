# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №35 / Edition №35 — 2026-10-10** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Технологии]** [Deno присоединяется к Cloudflare и объявляет сроки поддержки своих продуктов](editions/2026/10-10/01-deno-cloudflare-transition.md)
- **[ИИ]** [Ai2 распределяет GPU по бюджетам времени и сообщает о сокращении очередей](editions/2026/10-10/02-ai2-gpu-time-budgets.md)
- **[Наука]** [NASA использует уходящий грузовой корабль для испытаний двенадцати теплозащитных капсул](editions/2026/10-10/03-krepe-heat-shield-tests.md)
- **[Экономика]** [NASA открыла приём предложений по коммерческим станциям на низкой орбите](editions/2026/10-10/04-commercial-stations-proposals.md)
- **[Наука]** [Living Planet Index снова показывает спад 73% — важно понимать, что именно он измеряет](editions/2026/10-10/05-living-planet-index-2026.md)
- **[Мир]** [Нобелевскую премию мира получила Нави Пиллэй — за укрепление международного права](editions/2026/10-10/06-pillay-peace-prize.md)
- **[ИИ]** [BrickBench проверяет, умеет ли ИИ спроектировать LEGO, а не просто показать красивую сборку](editions/2026/10-10/07-brickbench-design-checks.md)
- **[Экономика]** [Коды платежей CHAPS дают быстрый индикатор сделок с недвижимостью — но не индекс цен](editions/2026/10-10/08-chaps-property-indicator.md)
- **[Технологии]** [Голос помог написать функцию блога, но выпуск потребовал ревью и работы с клавиатурой](editions/2026/10-10/09-voice-coding-reviewed.md)
- **[ИИ]** [Asana связала экономию браузерного агента со стабильностью истории — число 76× требует контекста](editions/2026/10-10/10-asana-browser-cache-study.md)
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
