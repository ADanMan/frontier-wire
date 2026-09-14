# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №12 / Edition №12 — 2026-09-14** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [Anthropic просит притормозить ИИ. Белый дом отвечает — не дождётесь](editions/2026/09-14/01-ai-slowdown-trump-amodei.md)
- **[Технологии]** [Apple делает геймпады для iPhone — и, похоже, под брендом Beats](editions/2026/09-14/02-apple-iphone-game-controllers.md)
- **[Наука]** [Большой опрос физиков показал: согласия по устройству Вселенной нет](editions/2026/09-14/03-physicists-disagree-universe-survey.md)
- **[Наука]** [У болезни Альцгеймера нашли скрытый слой — в укладке ДНК](editions/2026/09-14/04-alzheimers-genome-3d-layer.md)
- **[Мир]** [На борьбу с калечащими операциями собрали $15,5 млн из нужных $100 млн](editions/2026/09-14/05-her-horizon-fund-fgm.md)
- **[Культура]** [Легенды британского панка The Raincoats, X-Ray Spex и The Slits собрались в супергруппу](editions/2026/09-14/06-raincoats-xray-spex-slits-supergroup.md)
- **[Мир]** [В Турции за выходные задержали 162 человека на рейдах против ЛГБТК+](editions/2026/09-14/07-turkey-lgbtq-raids.md)
- **[Мир]** [Выборы в Швеции: левый блок вырывается вперёд, крайне правые теряют голоса](editions/2026/09-14/08-sweden-election-left-bloc.md)
- **[Наука]** [Учёные скрещивают электронный микроскоп с квантовым компьютером](editions/2026/09-14/09-quantum-computer-microscope.md)
- **[Наука]** [ИИ нашёл в 400 000 постов на Reddit неожиданные побочки Оземпика](editions/2026/09-14/10-ozempic-reddit-side-effects.md)
- **[Культура]** [Как обычное надгробие в Шропшире стало «могилой Скруджа»](editions/2026/09-14/11-scrooge-gravestone-shropshire.md)
- **[Культура]** [Lil Durk оправдан по делу о заказном убийстве](editions/2026/09-14/12-lil-durk-acquitted-murder-for-hire.md)
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
