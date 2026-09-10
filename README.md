# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №8 / Edition №8 — 2026-09-10** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [OpenAI выпустила GPT-6 Astra — и тут же выяснилось, как она устроена](editions/2026/09-10/01-gpt-6-astra-launch.md)
- **[Технологии]** [Apple наконец показала складной iPhone — и им же дебютирует новый гендиректор](editions/2026/09-10/02-apple-iphone-duo-foldable.md)
- **[Наука]** [Межзвёздная комета 3I/ATLAS оказалась залита метанолом](editions/2026/09-10/03-comet-atlas-methanol.md)
- **[Наука]** [Телескоп «Чандра» нашёл рентгеновские объекты, которые не укладываются ни в одну известную категорию](editions/2026/09-10/04-chandra-xray-objects.md)
- **[Мир]** [У берегов Филиппин сгорел паром со 134 пассажирами и членами экипажа на борту](editions/2026/09-10/05-philippines-ferry-fire.md)
- **[Мир]** [В Китае юристы и архитекторы подрабатывают, обучая ИИ своей же профессии](editions/2026/09-10/06-china-gig-experts-train-ai.md)
- **[Культура]** [«Монастырь десяти тысяч Будд» в Гонконге — это не монастырь, и Будд там больше 12 000](editions/2026/09-10/07-ten-thousand-buddhas-monastery.md)
- **[Мир]** [Дрон едва не столкнулся с самолётом Зеленского на пути в Осло](editions/2026/09-10/08-norway-zelenskyy-drone.md)
- **[Мир]** [Уганда вышла из Игр Инвиктус «из уважения к королю Карлу»](editions/2026/09-10/09-uganda-invictus-games.md)
- **[Наука]** [Учёные нашли «переключатель» роста костей, способный побороть остеопороз](editions/2026/09-10/10-bone-building-switch-osteoporosis.md)
- **[Наука]** [У детей матерей с анемией при рождении мозг оказался меньше](editions/2026/09-10/11-anaemia-babies-brain-size.md)
- **[Культура]** [Собор в Белизе, который построили, чтобы приструнить бывших пиратов](editions/2026/09-10/12-saint-john-cathedral-belize.md)
- **[Культура]** [Синдаров обыграл Фирузджу и вывел свою команду в лидеры Global Chess League](editions/2026/09-10/13-sindarov-beats-firouzja-chess-league.md)
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
