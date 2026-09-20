# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №18 / Edition №18 — 2026-09-20** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [FAA покупает ИИ-систему за 875 миллионов долларов для разгрузки воздушного движения](editions/2026/09-20/01-faa-ai-air-traffic-tool.md)
- **[Мир]** [Хуситы заявили об ударе баллистическими ракетами по Эр-Рияду](editions/2026/09-20/02-houthis-riyadh-missiles.md)
- **[Мир]** [Выжившие рассказали, как задыхались в нигерийской тюремной камере, где погибли 37 человек](editions/2026/09-20/03-nigeria-prison-cell-deaths.md)
- **[Наука]** [Лето 2026 года стало для Европы рекордным не только по жаре, но и по числу смертей](editions/2026/09-20/04-europe-summer-heat-deaths.md)
- **[Экономика]** [Розничные продажи в Великобритании неожиданно выросли на фоне жары и мрачных прогнозов](editions/2026/09-20/05-uk-retail-sales-bounce-back.md)
- **[Наука]** [Учёные назвали новый вид змеи в честь гитариста Guns N' Roses Слэша](editions/2026/09-20/06-snake-named-after-slash.md)
- **[Культура]** [Чиптюн-группа Anamanaguchi призналась, что у них открыто «слишком много вкладок в браузере»](editions/2026/09-20/07-anamanaguchi-interview.md)
- **[Экономика]** [Япония подняла ставку до 31-летнего максимума, догоняя ФРС и ЕЦБ](editions/2026/09-20/08-japan-rate-hike.md)
- **[Мир]** [Депортированных из США мужчин избили и держали в мешках на голове в отеле Экваториальной Гвинеи](editions/2026/09-20/09-equatorial-guinea-deportees.md)
- **[Мир]** [Полиция Гааги разогнала митинг ультраправых, скандировавших антисемитские лозунги](editions/2026/09-20/10-hague-far-right-protest.md)
- **[ИИ]** [Gemini взломал три компании во время теста на кибербезопасность, и Google молчал об этом месяцами](editions/2026/09-20/11-gemini-hacked-three-companies.md)
- **[Наука]** [Крошечный чип Caltech научился перенаправлять свет за 74 квадриллионных доли секунды](editions/2026/09-20/12-caltech-light-steering-chip.md)
- **[Наука]** [Рентгеновский телескоп XRISM впервые напрямую увидел, как пульсар «пьёт» ветер соседней звезды](editions/2026/09-20/13-xrism-pulsar-companion-wind.md)
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
