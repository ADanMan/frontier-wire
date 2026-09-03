# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №1 / Edition №1 — 2026-09-03** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[ИИ]** [ChatGPT, Grok и Claude легли одновременно — и это неудобный вопрос](editions/2026/09-03/01-ai-outage.md)
- **[ИИ]** [OpenAI назвала собственную модель критическим киберриском](editions/2026/09-03/02-astra-cybersecurity.md)
- **[Технологии]** [Google говорит, что её погодный ИИ стал точнее](editions/2026/09-03/03-google-weather-ai.md)
- **[Технологии]** [Репозиторий Anthropic со «скиллами» для агентов взлетел в топ GitHub](editions/2026/09-03/04-anthropic-skills-github.md)
- **[Наука]** [У Сатурна нашли десятиугольник на южном полюсе](editions/2026/09-03/05-saturn-decagon.md)
- **[Мир]** [30 танкеров в день через Ормузский пролив? Данные так не считают](editions/2026/09-03/06-hormuz-oil-data.md)
- **[Культура]** [Погоне на паровозе Бастера Китона — сто лет](editions/2026/09-03/07-buster-keaton-100.md)
- **[ИИ]** [Anthropic публикует системные промпты Claude — и там неожиданно много про тексты песен](editions/2026/09-03/08-claude-system-prompt-lyrics.md)
- **[Мир]** [Жертвы бойни в Шарпевиле спустя 66 лет требуют компенсации от властей ЮАР](editions/2026/09-03/09-sharpeville-massacre-compensation.md)
- **[Наука]** [Учёные впервые сфотографировали архею-«археарда» в тесной связке с бактерией](editions/2026/09-03/10-asgard-archaeon-living-fossils.md)
- **[Технологии]** [Взял машину в аренду — через несколько часов его права продавали на даркнет-сайте](editions/2026/09-03/11-drivers-license-breach.md)
- **[Мир]** [Почти половина фермеров мира каждый год травится пестицидами, показало исследование](editions/2026/09-03/12-pesticide-poisoning-farmers.md)
- **[Культура]** [Умерла Глория Стайнем — журналистка, изменившая представление о том, какой может быть женщина](editions/2026/09-03/13-gloria-steinem-obituary.md)
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

## Publisher

Made by [Danila Katalshov](https://adanman.github.io) —
[LinkedIn](https://www.linkedin.com/in/danilakatalshov) · [Telegram](https://t.me/adanman).
Sibling project: [agentic-frontier](https://github.com/ADanMan/agentic-frontier),
a personal learning-in-public log on AI engineering.

## License

[MIT](LICENSE) — take anything useful.
