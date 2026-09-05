---
date: 2026-09-05
rubric: tech
title_ru: Не всё, что в трендах GitHub, — новый ИИ-хайп: библиотеке форматирования строк уже больше десяти лет
title_en: Not everything trending on GitHub is fresh AI hype — this string-formatting library is over a decade old
dek_ru: {fmt} десять с лишним лет тихо разгоняет C++-код в MongoDB, PyTorch и Windows Terminal — и сегодня внезапно снова в топе трендов.
dek_en: {fmt} has spent over a decade quietly speeding up C++ code in MongoDB, PyTorch, and Windows Terminal — and today it's back on the trending page.
source: https://github.com/fmtlib/fmt
generated: true
---

## Русская версия

Пока в трендах GitHub соревнуются свежие ИИ-агентные фреймворки с сотнями тысяч звёзд за считанные месяцы, рядом с ними на третьем месте оказался [fmtlib/fmt](https://github.com/fmtlib/fmt) — библиотека форматирования строк для C++, у которой почти 7 976 коммитов истории и куда более скромные 25 462 звезды, из них 25 за последние сутки.

{fmt} реализует функциональность `std::format` из C++20 и `std::print` из C++23 — по сути, современную, безопасную и быструю замену старому доброму `printf` и потоковому выводу C++. Авторы заявляют, что библиотека работает от «десятков процентов» до в 20–30 раз быстрее `sprintf` и iostreams, при этом даёт позиционные аргументы для локализации, поддержку Unicode и расширяемость под собственные типы данных. Скомпилированный бинарник с {fmt} по размеру сравним с обычным `printf` — то есть скорость не куплена ценой раздутого кода.

Библиотеку уже используют FoundationDB (Apple), ClickHouse, MongoDB, PyTorch, Windows Terminal и Battle.net от Blizzard — список достаточно длинный и разнородный, чтобы говорить не о моде, а о инфраструктурной зависимости. Именно поэтому появление {fmt} в трендах — хороший повод напомнить: алгоритм трендов GitHub время от времени поднимает не свежий хайп, а зрелые, скучные на вид инструменты, на которых давно и тихо всё держится.

### Почему это важно

Разница между {fmt} и соседними по трендам агентными фреймворками — это разница между библиотекой, чью пользу можно проверить по списку реальных проектов, использующих её годами, и репозиторием, чья ценность пока измеряется только счётчиком звёзд. Не всё новое — хайп, но и не всё старое — скука: иногда скучное и есть самое надёжное.

## English version

While fresh AI-agent frameworks with hundreds of thousands of stars racked up in a few months compete for attention on GitHub's trending page, sitting at #3 today is [fmtlib/fmt](https://github.com/fmtlib/fmt) — a C++ string-formatting library with nearly 7,976 commits of history and a far more modest 25,462 stars, 25 of them gained in the last day.

{fmt} implements C++20's `std::format` and C++23's `std::print` — a modern, safe, fast replacement for old-school `printf` and C++ iostreams. The project claims performance ranging from "tens of percent" up to 20–30 times faster than `sprintf` and iostreams, while adding positional arguments for localization, Unicode support, and extensibility for custom types. A compiled binary using {fmt} comes out about the same size as one using plain `printf` — the speed isn't bought with code bloat.

The library is already used by FoundationDB (Apple), ClickHouse, MongoDB, PyTorch, Windows Terminal, and Blizzard's Battle.net — a long and varied enough list to call this infrastructure dependency rather than fashion. That's exactly why {fmt} showing up in the trending list is a good reminder: GitHub's trending algorithm occasionally surfaces not fresh hype but mature, boring-looking tools that a lot of software has quietly depended on for years.

### Why it matters

The gap between {fmt} and the agent frameworks trending alongside it is the gap between a library whose value you can check against a list of real projects that have used it for years, and a repository whose value is currently measured mostly by its star counter. Not everything new is hype, and not everything old is boring — sometimes boring is exactly what's most reliable.
