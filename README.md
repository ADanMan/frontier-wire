# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №19 / Edition №19 — 2026-09-21** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [Партия Мерца потерпела историческое поражение на выборах в двух землях Германии](editions/2026/09-21/01-german-state-elections-merz.md)
- **[Наука]** [Через десять лет запечатанный конверт открыли — а гравитация так и не сошлась](editions/2026/09-21/02-nist-gravitational-constant.md)
- **[Мир]** [Администрация Трампа готовит новые санкции против Международного уголовного суда](editions/2026/09-21/03-trump-icc-sanctions.md)
- **[Наука]** [Гигантский кратер может раскрыть тайну происхождения обречённой луны Марса](editions/2026/09-21/04-phobos-crater-origin.md)
- **[Культура]** [Британская кухня XVIII века была не унылой, а мультикультурной и острой](editions/2026/09-21/05-british-food-history-myth.md)
- **[ИИ]** [Трамп заявил, что хочет создать «силы ИИ» во главе с «ИИ-царём»](editions/2026/09-21/06-trump-ai-force-czar.md)
- **[Экономика]** [Производительность труда в Британии оказалась вдвое выше прежних оценок](editions/2026/09-21/07-uk-productivity-revised.md)
- **[Мир]** [В нигерийской тюремной камере задохнулись 37 человек — в основном подозреваемых старателей](editions/2026/09-21/08-nigeria-prison-deaths.md)
- **[Мир]** [Похищенную в Малави британку освободили в перестрелке, четверо похитителей погибли](editions/2026/09-21/09-malawi-kidnapping-rescue.md)
- **[Наука]** [Учёные нашли восемь пищевых добавок, связанных с гипертонией и болезнями сердца](editions/2026/09-21/10-food-additives-blood-pressure.md)
- **[Экономика]** [Падение поставок нефти разгоняет цены на серу — и бьёт по стоимости еды](editions/2026/09-21/11-sulfur-food-costs.md)
- **[Культура]** [Подкаст об истории музыки No Dogs in Space возвращается после двухлетней паузы](editions/2026/09-21/12-no-dogs-in-space-returns.md)
- **[Технологии]** [Аналитик Google под прикрытием проник в ближний круг хакерской группы TeamPCP](editions/2026/09-21/13-google-analyst-infiltrates-hackers.md)
- **[ИИ]** [DeepMind выпустила карту предсказанных эффектов для 9 миллиардов вариантов ДНК](editions/2026/09-21/14-alphagenome-atlas.md)
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
