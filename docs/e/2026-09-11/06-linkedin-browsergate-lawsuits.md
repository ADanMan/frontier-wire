---
date: 2026-09-11
rubric: tech
title_ru: LinkedIn отбилась от исков о слежке за расширениями браузера
title_en: LinkedIn beats lawsuits over scanning users' browser extensions
dek_ru: Судья счёл, что истцы не доказали реального нарушения приватности.
dek_en: A judge ruled plaintiffs failed to allege any real privacy violation.
source: https://arstechnica.com/tech-policy/2026/09/linkedin-beats-browsergate-lawsuits-over-scanning-users-chrome-extensions/
generated: true
---

## Русская версия

LinkedIn выиграла серию исков, объединённых под названием «BrowserGate» — они касались того, что сервис якобы сканировал установленные у пользователей расширения Chrome. Как пишет [Ars Technica](https://arstechnica.com/tech-policy/2026/09/linkedin-beats-browsergate-lawsuits-over-scanning-users-chrome-extensions/), судья отклонил иски, посчитав, что истцы не смогли доказать какое-либо реальное нарушение приватности.

Суть претензий сводилась к тому, что сайт LinkedIn при загрузке страницы способен технически определить, какие расширения установлены в браузере посетителя — это давно известная категория веб-техник, основанная на побочных эффектах работы расширений (например, на том, что некоторые расширения внедряют в страницу собственные элементы или файлы, которые можно обнаружить скриптом). Сама по себе такая возможность существует у множества сайтов, а не только у LinkedIn, и относится скорее к дырам в архитектуре браузерных расширений, чем к специфической злонамеренности конкретного сервиса.

Ключевой вопрос в подобных делах — не «происходило ли технически обнаружение расширений», а «причинило ли это измеримый вред пользователю». Американские суды в делах о цифровой приватности регулярно требуют от истцов показать не абстрактный факт сбора данных, а конкретные последствия — финансовый ущерб, украденную информацию, доказанное злоупотребление собранными данными. Если иск строится только на технической возможности слежки, без доказательства того, что данные были использованы во вред, у него мало шансов пройти дальше стадии рассмотрения — что и произошло в этом деле.

Это не первый случай, когда громкое название иска («геймдейт», «-гейт» вообще любимый суффикс юридического маркетинга) расходится с реальной судебной перспективой дела: журналистский или адвокатский ярлык создаёт ощущение скандала, но стандарт доказывания в суде остаётся прежним и требует показать конкретный вред, а не только сам факт технической возможности сбора данных.

### Почему это важно

Дело показывает разрыв между тем, что технически возможно в вебе, и тем, что закон реально признаёт нарушением: обнаружение расширений браузера — распространённая практика, и без доказанного вреда компании продолжат её использовать безнаказанно.

## English version

LinkedIn has won a series of lawsuits bundled under the "BrowserGate" label, which alleged the company was scanning users' installed Chrome extensions. According to [Ars Technica](https://arstechnica.com/tech-policy/2026/09/linkedin-beats-browsergate-lawsuits-over-scanning-users-chrome-extensions/), a judge tossed the suits, ruling that plaintiffs failed to allege any real privacy violation.

The core claim was that LinkedIn's site could technically detect which extensions a visitor's browser has installed — a well-known category of web technique that relies on side effects of how extensions run (for instance, some extensions inject their own elements or files into a page that a script can then detect). That capability exists on plenty of sites, not just LinkedIn, and is more a gap in browser extension architecture than something specific to one company's ill intent.

The key question in cases like this isn't whether extension detection happened technically — it's whether it caused measurable harm to a user. US courts handling digital privacy cases routinely require plaintiffs to show more than the abstract fact of data collection: they need concrete consequences — financial loss, stolen information, proven misuse of the collected data. A suit built purely on the technical possibility of tracking, without evidence the data was used to cause harm, rarely survives past the initial review stage — which is exactly what happened here.

This isn't the first time a catchy lawsuit label ("-gate" is a favorite suffix of legal marketing) has diverged from the case's actual legal footing: a journalistic or attorney-coined tag creates a sense of scandal, but the courtroom standard of proof stays the same and demands concrete harm, not just the technical possibility of data collection.

### Why it matters

The case highlights the gap between what's technically possible on the web and what the law actually treats as a violation: browser extension detection is common practice, and without proven harm, companies will keep using it without consequence.
