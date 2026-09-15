# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №13 / Edition №13 — 2026-09-15** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [Африканский миллиардер выводит нефтезавод на биржу — и может заработать $23 млрд](editions/2026/09-15/01-dangote-refinery-ipo.md)
- **[Мир]** [Старейшая больница Лондона стоит на деньгах работорговцев](editions/2026/09-15/02-st-barts-slave-trade-donors.md)
- **[Наука]** [Чума убивала целыми семьями за 5500 лет до Чёрной смерти](editions/2026/09-15/03-ancient-plague-siberia.md)
- **[Наука]** [«Красные точки» Уэбба: чёрные дыры или звёзды размером с чёрную дыру?](editions/2026/09-15/04-webb-little-red-dots.md)
- **[Культура]** [Шахматы доедут до Южного полюса — и это не первоапрельская шутка](editions/2026/09-15/05-antarctica-chess-tournament.md)
- **[Культура]** [Macklemore сняли с тура Эда Ширана за слова в поддержку Палестины](editions/2026/09-15/06-macklemore-ed-sheeran-tour.md)
- **[ИИ]** [«Тимми», «Рен» и «Джеки» — ИИ-боты, которые сами признаются, что они боты](editions/2026/09-15/07-ai-agents-social-slop.md)
- **[Мир]** [Верховный суд США заблокировал попытку Трампа ограничить голосование по почте](editions/2026/09-15/08-supreme-court-mail-voting-trump.md)
- **[Мир]** [Свадьбу Трампа-младшего оплатил бизнесмен, которого Путин наградил Орденом Дружбы](editions/2026/09-15/09-kremlin-oligarch-trump-jr-wedding.md)
- **[Наука]** [Учебники химии почти сто лет ошибались насчёт того, как атомы влияют друг на друга](editions/2026/09-15/10-chemistry-textbooks-inductive-effect.md)
- **[Наука]** [Рак молодеет — и, возможно, дело в том, что тела людей стареют быстрее](editions/2026/09-15/11-cancer-younger-adults-biological-aging.md)
- **[Культура]** [Oasis едут в новый тур 2027 года — с возвращением в Небворт](editions/2026/09-15/12-oasis-2027-tour.md)
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
