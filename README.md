# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №11 / Edition №11 — 2026-09-13** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Наука]** [Hayabusa2 впервые в истории измерил лазером расстояние до астероида на пролёте](editions/2026/09-13/01-hayabusa2-laser-ranging-asteroid.md)
- **[Наука]** [Оземпик продлил жизнь мышам и улучшил им память — но это ещё не рецепт для людей](editions/2026/09-13/02-ozempic-semaglutide-mice-aging.md)
- **[Мир]** [Короля Ойо похоронили в Уганде — а спор о его преемнике так и не решён](editions/2026/09-13/03-king-oyo-burial-uganda-succession.md)
- **[Мир]** [Шестерых нигерийцев экстрадировали в США за romance-схему на $6 миллионов](editions/2026/09-13/04-nigerians-extradited-romance-scam.md)
- **[ИИ]** [Альтман назвал IPO OpenAI в 2026 году «плохо продуманным» — но не отказался от него навсегда](editions/2026/09-13/05-altman-openai-ipo-ill-advised.md)
- **[Культура]** [Bon Iver написал джингл для бара в Миннесоте — про панировочные палочки из фарша](editions/2026/09-13/06-bon-iver-meatloaf-jingle.md)
- **[Технологии]** [Как OpenAI выдерживает миллиард пользователей ChatGPT и 22 миллиона запросов в секунду](editions/2026/09-13/07-openai-storage-scaling-billion-users.md)
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
