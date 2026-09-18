---
date: 2026-09-18
rubric: tech
title_ru: Кто-то целенаправленно охотится за аккаунтами разработчиков Rust
title_en: Someone is targeting Rust developers' accounts
dek_ru: Команда безопасности crates.io предупредила о кампании против известных участников rust-lang и владельцев популярных крейтов.
dek_en: The crates.io security team warns of an ongoing campaign against prominent rust-lang members and popular crate maintainers.
source: https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/
generated: true
---

## Русская версия

Команда безопасности crates.io выпустила предупреждение о продолжающейся кампании атак на видных участников сообщества rust-lang и владельцев популярных крейтов. Об этом [пишет разработчик Саймон Уиллисон](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) со ссылкой на заявление Адама Харви и команды безопасности crates.

По имеющимся данным, атакующие пытаются скомпрометировать устройства и аккаунты конкретных людей — не случайным фишингом по широкой базе, а целенаправленно, выбирая тех, у кого есть доступ на публикацию пакетов в экосистему Rust. Логика такой атаки понятна: захватить учётку мейнтейнера популярного крейта — значит получить возможность протолкнуть вредоносный код напрямую в цепочку поставок тысяч проектов, которые этот крейт используют, часто без какой-либо дополнительной проверки со стороны разработчиков ниже по цепочке.

Похожие кампании против npm и PyPI за последние годы уже показали, насколько эффективна эта тактика: одна скомпрометированная учётка — и вредоносный код автоматически расходится по огромному количеству чужих сборок. Rust с его репутацией «безопасного по умолчанию» языка тут не исключение: crates.io — точно такая же публичная экосистема пакетов с той же фундаментальной уязвимостью — человеческим фактором на стороне мейнтейнеров.

### Почему это важно

Атаки на цепочку поставок опенсорса не про уязвимости в коде — они про то, что достаточно скомпрометировать одного человека с нужным доступом. Чем популярнее экосистема, тем больше в ней целей и тем выше цена одной успешной атаки — а значит, каждому мейнтейнеру популярного пакета стоит относиться к своей учётке как к части инфраструктуры, а не личному аккаунту.

## English version

The crates.io security team has issued a warning about an ongoing campaign targeting prominent members of the rust-lang community and maintainers of popular crates. [Developer Simon Willison flagged the warning](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/), citing a statement from Adam Harvey and the crates security team.

According to the warning, attackers are attempting to compromise specific people's devices and accounts — not broad, spray-and-pray phishing, but targeted efforts aimed at those with publishing access to the Rust package ecosystem. The logic is straightforward: hijack a popular crate maintainer's account, and you get a direct route to push malicious code into the supply chain of every project that depends on that crate — often with no further review from developers downstream.

Similar campaigns against npm and PyPI have shown how effective this tactic can be: compromise one account, and malicious code propagates automatically into an enormous number of other people's builds. Rust's reputation for being "safe by default" as a language doesn't help here — crates.io is a public package ecosystem just like the others, with the same underlying weak point: the humans who maintain it.

### Why it matters

Open-source supply-chain attacks aren't about bugs in the code — they're about how little it takes to compromise one person with the right access. The more popular an ecosystem gets, the more targets it has and the higher the payoff for a single successful breach — which means every maintainer of a widely used package should treat their account as infrastructure, not a personal login.
