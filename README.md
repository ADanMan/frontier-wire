# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №7 / Edition №7 — 2026-09-09** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [«Один симптом, три рычага»: свежая работа ставит под сомнение модный метод дообучения ИИ](editions/2026/09-09/01-on-policy-self-distillation-critique.md)
- **[Наука]** [Учёные учат нейросети находить изменения на спутниковых снимках — не хватает самих снимков](editions/2026/09-09/02-remote-sensing-change-synthesis.md)
- **[Наука]** [OpenAI заявила, что ИИ решил задачу Навье — Стокса за миллион долларов. Математики спорят, кому это засчитывать](editions/2026/09-09/03-navier-stokes-ai-proof-controversy.md)
- **[Культура]** [Глава Смитсоновского института уходит в отставку после 38 лет службы](editions/2026/09-09/04-smithsonian-bunch-retires.md)
- **[Мир]** [Из французского музея Ренуара похитили картины на 2,5 миллиона долларов — двое из четырёх грабители обронили при побеге](editions/2026/09-09/05-renoir-museum-heist.md)
- **[Мир]** [В Китае юристы, архитекторы и инженеры подрабатывают, обучая ИИ собственной профессии](editions/2026/09-09/06-china-gig-ai-trainers.md)
- **[Наука]** [Учёные нашли в крови гремучих змей белки, которые нейтрализуют яд в 10 раз эффективнее нынешних антидотов](editions/2026/09-09/07-rattlesnake-antivenom.md)
- **[Технологии]** [Microsoft закрыла рекордные 972 уязвимости за один патч-вторник — 112 из них критические](editions/2026/09-09/08-microsoft-patch-tuesday-record.md)
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
