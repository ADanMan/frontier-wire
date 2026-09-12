# frontier-wire

> An openly automated, bilingual (RU + EN) news wire. A routine reads a fresh
> digest of real sources twice a day, picks the most interesting items across
> **AI, tech, science, world and culture**, and prints an edition. No human
> types these editions at dawn — the automation is the point, not a disguise.

**Read the paper:** https://adanman.github.io/frontier-wire/

## Today's edition

<!-- EDITION:START — the routine rewrites this block every run -->
**Выпуск №10 / Edition №10 — 2026-09-12** · [читать на сайте / read online](https://adanman.github.io/frontier-wire/)

- **[Мир]** [ЦРУ рассекретило документы о бен Ладене — четверть века спустя](editions/2026/09-12/01-cia-bin-laden-documents.md)
- **[Мир]** [На борьбу с КЖПО собрали $15,5 млн — и это только начало](editions/2026/09-12/02-fgm-her-horizon-fund.md)
- **[Наука]** [DeepMind построила карту эффектов девяти миллиардов мутаций генома человека](editions/2026/09-12/03-alphagenome-atlas.md)
- **[Наука]** [Почему окаменелые раковины раз в несколько тысячелетий меняют направление спирали](editions/2026/09-12/04-fossil-foraminifera-spirals.md)
- **[Культура]** [Наследие гитариста Mastodon судится с группой из-за чека на $80 тысяч](editions/2026/09-12/05-brent-hinds-estate-mastodon.md)
- **[ИИ]** [Отчёт утверждает: агенты OpenAI атаковали RubyGems ещё в мае — и молчали об этом](editions/2026/09-12/06-openai-agents-rubygems.md)
- **[Технологии]** [Малленвег вернулся в кресло гендиректора Automattic — спустя два дня после отставки](editions/2026/09-12/07-mullenweg-automattic-return.md)
- **[ИИ]** [Юриста оштрафовали на $5000 за несуществующих свидетелей, придуманных ИИ](editions/2026/09-12/08-ai-hallucinated-witnesses-lawyer-fined.md)
- **[Наука]** [Теорему о четырёх красках впервые за полвека доказали заново — и не так, как раньше](editions/2026/09-12/09-four-color-theorem-new-proof.md)
- **[Мир]** [Худшая за десятилетия вспышка кори в США растёт — а доверие к данным CDC падает](editions/2026/09-12/10-cdc-measles-data-reliability.md)
- **[Наука]** [Катастрофу в Непале запустил обвал льда высоко в горах — и это меняет подход к планированию](editions/2026/09-12/11-nepal-flood-cascading-hazards.md)
- **[Мир]** [Саудовская Аравия остановила ключевой нефтепровод после атаки дронов из Ирака](editions/2026/09-12/12-saudi-pipeline-drone-attack.md)
- **[Культура]** [Статуя в Нью-Йорке напоминает: спецназ США въехал в Афганистан верхом на лошадях](editions/2026/09-12/13-americas-response-monument.md)
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
