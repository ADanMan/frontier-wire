---
date: 2026-09-08
rubric: ai
title_ru: Контекст ИИ-агента раздувается — новый инструмент обещает сократить его на 98%
title_en: AI agents are drowning in context — a new tool claims a 98% cut
dek_ru: Репозиторий context-mode занял третье место в сегодняшних трендах GitHub — инструмент «песочит» вывод инструментов агента и утверждает, что режет объём данных в контексте на 98% сразу на 17 платформах.
dek_en: The context-mode repo landed at #3 on today's GitHub trending list — it sandboxes an agent's tool output and claims a 98% cut in what ends up in the context window, across 17 platforms.
source: https://github.com/mksglu/context-mode
generated: true
---

## Русская версия

Третье место в сегодняшних трендах GitHub занял [mksglu/context-mode](https://github.com/mksglu/context-mode) — новый инструмент для управления контекстным окном ИИ-агентов, набравший 147 звёзд за день. Разработчик описывает его как «песочницу» для вывода инструментов: результат работы каждого вызова инструмента изолируется и обрабатывается отдельно, прежде чем попасть в контекст модели, а не сваливается туда целиком.

По заявлению автора, это позволяет сократить объём данных, которые агент тащит в контекст, на 98%, а также сохранять память сессии между запусками и — что интереснее — единообразно маршрутизировать это поведение через MCP и хуки сразу на 17 платформах. То есть речь не о разовом трюке под конкретный ИИ-инструмент, а о попытке сделать управление контекстом сквозной прослойкой, работающей поверх разных агентных сред одинаково.

Проблема, которую решает этот класс инструментов, знакома всем, кто пользовался агентами дольше пары дней: контекстное окно — ресурс конечный и дорогой, а вывод инструментов — команд, поисковых запросов, содержимого файлов — легко его забивает мусором, из-за которого агент теряет нить задачи или начинает работать медленнее и дороже. Отсюда и волна инструментов вроде context-mode: не улучшить саму модель, а отфильтровать то, что до неё вообще доходит.

Число «98%» стоит воспринимать как маркетинговую цифру автора, а не как независимо подтверждённый бенчмарк — в описании репозитория нет ссылки на методологию замера. 147 звёзд за один день — тоже скорее сигнал любопытства сообщества, чем доказательство, что инструмент реально приживётся в продакшен-агентах. Но сам факт, что именно такой инструмент попал в топ-3 трендов вместе с конвертером документов от Microsoft и видеоинструментом HeyGen, показывает: сегодняшний день на GitHub — это день не новых моделей, а инфраструктуры вокруг них.

### Почему это важно

Управление контекстным окном становится отдельной инженерной дисциплиной внутри разработки агентов: по мере того как агентам поручают всё более длинные и сложные задачи, то, что́ именно остаётся в их «памяти» между шагами, всё сильнее определяет, насколько они вообще способны довести задачу до конца.

## English version

Today's #3 spot on GitHub's trending list went to [mksglu/context-mode](https://github.com/mksglu/context-mode), a new tool for managing what ends up in an AI agent's context window, with 147 stars in a day. Its author describes it as a sandbox for tool output: the result of each tool call gets isolated and processed separately before it reaches the model's context, rather than dumping in whole.

According to the author, that cuts the volume of data an agent drags into its context by 98%, while also persisting session memory across runs and — more notably — routing that behavior consistently through MCP and hooks across 17 platforms. So this isn't a one-off trick for a single AI tool; it's an attempt to make context management a cross-cutting layer that works the same way across different agent environments.

The problem this class of tool addresses is familiar to anyone who's used an agent for more than a couple of days: the context window is a finite, expensive resource, and tool output — command results, search hits, file contents — fills it with noise fast enough to make an agent lose the thread of a task or just get slower and more expensive to run. Hence the wave of tools like context-mode: not making the model smarter, but filtering what reaches it in the first place.

The "98%" figure is worth treating as the author's own marketing number rather than an independently verified benchmark — the repo description doesn't link to a measurement methodology. 147 stars in a day is likewise more a sign of community curiosity than proof the tool will stick in production agent setups. Still, the fact that this kind of tool landed in the top three alongside Microsoft's document converter and HeyGen's video tool says something: today on GitHub was a day about the infrastructure around models, not about new models themselves.

### Why it matters

Context-window management is turning into its own engineering discipline within agent development: as agents get handed longer, more complex tasks, exactly what stays in their "memory" between steps increasingly determines whether they can actually finish the job.
