# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №9 / Edition №9 — 2026-09-11** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [В угандийском королевстве спорят о короне из-за «тайного сына»](editions/2026/09-11/01-uganda-royal-succession-dispute.md)
- **[Наука]** [Теорему о четырёх красках доказали заново — и без компьютерного «доверься мне»](editions/2026/09-11/02-four-color-theorem-new-proof.md)
- **[ИИ]** [Учёный ищет новые антибиотики с помощью Codex и ChatGPT](editions/2026/09-11/03-codex-antimicrobial-discovery.md)
- **[Наука]** [Инопланетную жизнь как будто нашли дважды — учёные в основном не верят](editions/2026/09-11/04-alien-life-scientist-survey.md)
- **[Культура]** [Шноор в Бремене: квартал, будто сошедший со страниц сказки](editions/2026/09-11/05-schnoor-bremen-old-quarter.md)
- **[Технологии]** [LinkedIn отбилась от исков о слежке за расширениями браузера](editions/2026/09-11/06-linkedin-browsergate-lawsuits.md)
- **[Мир]** [Верховный суд Бразилии досрочно закрылся на фоне политического хаоса](editions/2026/09-11/07-brazil-supreme-court-chaos.md)
- **[Наука]** [Оземпик и Вегови неожиданно снижают число приступов астмы](editions/2026/09-11/08-ozempic-wegovy-asthma-copd.md)
- **[Мир]** [Алжир разорвал дипотношения с ОАЭ и закрыл небо](editions/2026/09-11/09-algeria-uae-diplomatic-break.md)
- **[Наука]** [NASA вышло из венерианской миссии — Европа полетит одна](editions/2026/09-11/10-europe-venus-mission-solo.md)
- **[Культура]** [Стонущие пещеры Калифорнии: зал, куда влезла бы Статуя Свободы](editions/2026/09-11/11-moaning-caverns-california.md)
- **[Наука]** [Окаменевшее перо может объяснить, почему одни птицы пережили вымирание, а другие нет](editions/2026/09-11/12-fossil-feather-bird-extinction.md)
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
