---
date: 2026-09-25
rubric: ai
title_ru: Google тихо выкатил open source рантайм для ИИ-агентов — и он уже в топ-5 трендов GitHub
title_en: Google quietly shipped an open-source AI agent runtime — and it's already top 5 on GitHub
dek_ru: Репозиторий google/ax за день набрал 166 звёзд и поднялся на четвёртое место в трендах.
dek_en: The google/ax repo gained 166 stars in a day and climbed to fourth place in the trends.
source: https://github.com/google/ax
generated: true
---

## Русская версия

Среди сегодняшних трендов GitHub — новый проект от Google под названием ax, который сам себя описывает коротко: открытый рантайм для оркестрации ИИ-агентов. За последний отслеживаемый период число звёзд репозитория выросло с 10 303 до 10 469 — это плюс 166 за один день, и этого хватило, чтобы попасть на четвёртое место в списке самых обсуждаемых проектов на платформе. Написан ax на Go.

«Рантайм для оркестрации агентов» — это не готовый чат-бот и не конечный продукт, а инфраструктурный слой: то, что разработчики используют, чтобы собирать системы из нескольких ИИ-агентов, которые вызывают друг друга, инструменты и внешние сервисы по заданной логике. То, что такой проект выпускает именно Google, а не только стартапы вроде тех, что тоже мелькают сегодня в трендах, — сигнал, что крупные игроки не просто следят за модой на мультиагентные системы, а выкладывают в открытый доступ собственную инфраструктуру для них.

Выбор Go как языка тоже говорит сам за себя: это язык, который обычно выбирают для системного, производительного, конкурентного по нагрузке кода — то есть Google явно целится не в прототипы для исследователей, а в инфраструктуру, которую можно ставить в продакшен.

Место в трендах GitHub само по себе не гарантирует, что проект приживётся: подобные списки взлетают и гаснут регулярно. Но для рынка мультиагентных систем — области, где ещё год-два назад не было устоявшихся стандартов, — выход открытого рантайма от компании такого масштаба, как Google, может стать ориентиром, вокруг которого начнут выстраиваться остальные инструменты.

### Почему это важно

Инфраструктура для ИИ-агентов сейчас переживает тот же этап, что веб-фреймворки лет пятнадцать назад: единого стандарта нет, и каждый крупный игрок пробует застолбить свой. Открытый релиз от Google — это заявка на то, чтобы стать одним из таких стандартов, а не просто ещё одним экспериментом.

## English version

Among today's GitHub trends is a new Google project called ax, which describes itself in one line as an open-source runtime for orchestrating AI agents. Over the tracked period, the repo's star count climbed from 10,303 to 10,469 — a gain of 166 in a single day, enough to land it in fourth place among the platform's most-discussed projects. It's written in Go.

An "agent orchestration runtime" isn't a finished chatbot or a consumer product — it's an infrastructure layer, the kind of thing developers use to build systems made of multiple AI agents that call each other, invoke tools, and coordinate with external services according to defined logic. The fact that this particular project comes from Google, rather than one of the startups also showing up in today's trends, is a signal that large players aren't just watching the multi-agent trend from the sidelines — they're open-sourcing their own infrastructure for it.

The choice of Go as the language says something too: it's a language typically picked for systems-level, performance-sensitive, concurrency-heavy code — meaning Google isn't targeting research prototypes here, it's targeting infrastructure meant to run in production.

A spot on GitHub's trending list doesn't guarantee a project sticks around; lists like this rise and fade constantly. But for the multi-agent tooling space — a field that didn't have settled standards even a year or two ago — an open-source runtime from a company the size of Google could become the reference point other tools start building around.

### Why it matters

AI agent infrastructure is going through the same phase web frameworks went through fifteen years ago: no single standard exists yet, and every major player is trying to stake a claim. An open-source release from Google is a bid to become one of those standards, not just another experiment.
