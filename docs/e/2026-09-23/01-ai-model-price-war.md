---
date: 2026-09-23
rubric: ai
title_ru: За два дня вышли пять новых ИИ-моделей — и это больше похоже на войну цен, чем на прорыв
title_en: Five new AI models landed in two days — this looks like a price war, not a breakthrough
dek_ru: Grok 4.7, MiMo v2.6, Claude Opus 5.5 и два GPT-6 — Sol и Luna — вышли почти одновременно.
dek_en: Grok 4.7, MiMo v2.6, Claude Opus 5.5, and two GPT-6 models — Sol and Luna — arrived almost back to back.
source: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
generated: true
---

## Русская версия

За два дня подряд рынок больших языковых моделей получил сразу пять релизов. Как отмечает разработчик и блогер Саймон Уиллисон в [своей заметке](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/), накануне вышли Grok 4.7 и MiMo v2.6 (Flash и Pro), а на следующий день Anthropic выпустила Claude Opus 5.5, и буквально через час после этого OpenAI представила сразу две модели — GPT-6 Sol и GPT-6 Luna.

Сам Уиллисон честно признаёт: чтобы понять, чем эти модели реально отличаются друг от друга, потребуется время — тестировать пять моделей одновременно сложно физически. Но сама плотность релизов говорит сама за себя. OpenAI в [собственном анонсе](https://openai.com/index/introducing-gpt-6-sol-and-luna) описывает Sol и Luna как модели, которые «приносят интеллект уровня фронтира в повседневную работу с разным балансом возможностей и стоимости» — то есть речь не о рывке в качестве, а о линейке под разные бюджеты.

Показательна и вторая деталь: одновременно с новыми моделями OpenAI выкатила обновлённое [кэширование промптов для GPT-6](https://openai.com/index/better-prompt-caching-for-gpt-6) — с более высоким процентом попаданий в кэш, новой диагностикой и явными точками разбивки запроса. Такие вещи запускают не ради красивых бенчмарков, а ради снижения задержки и, главное, стоимости обращения к модели для разработчиков. Это ровно то, что происходит, когда несколько лабораторий конкурируют не за звание «самой умной модели», а за то, кто дешевле и быстрее обслужит один и тот же класс задач.

Пока рано делать выводы о том, какая из пяти моделей окажется лучше в конкретных задачах — независимых тестов на равных условиях ещё не было. Но сам факт, что пять крупных лабораторий выпустили обновления практически одновременно, — уже сигнал: рынок ИИ-моделей вошёл в фазу, где скорость релизов и цена становятся не менее важным оружием, чем сырые возможности.

### Почему это важно

Когда пять моделей выходят за 48 часов, а одна из компаний в тот же день чинит систему кэширования ради экономии, это признак насыщающегося рынка: differentiation по чистому качеству исчерпывается, и конкуренция смещается в сторону цены и удобства использования — то есть в сторону обычного, довольно скучного рынка облачных сервисов.

## English version

The large language model market got five releases in two days. As developer and blogger Simon Willison notes [in his post](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/), Grok 4.7 and MiMo v2.6 (Flash and Pro) landed the day before, and the next day Anthropic shipped Claude Opus 5.5 — followed about an hour later by OpenAI releasing two models at once, GPT-6 Sol and GPT-6 Luna.

Willison is upfront that it will take a while to get a real read on how these models differ — testing five models at once is simply a lot of work. But the sheer density of releases says something on its own. In [its own announcement](https://openai.com/index/introducing-gpt-6-sol-and-luna), OpenAI describes Sol and Luna as models that "bring frontier intelligence to everyday work with different balances of capability and cost" — language that points to a product lineup for different budgets, not a single leap in quality.

A second detail is telling too: alongside the new models, OpenAI also rolled out improved [prompt caching for GPT-6](https://openai.com/index/better-prompt-caching-for-gpt-6), with higher cache hit rates, new diagnostics, and explicit cache breakpoints. Labs don't ship that kind of infrastructure work for flashy benchmarks — they ship it to cut latency and, more importantly, the cost developers pay per call. That's exactly what happens when several labs stop competing purely on "smartest model" and start competing on who serves the same class of task cheaper and faster.

It's too early to say which of the five models actually wins on real tasks — no independent, apples-to-apples benchmarks exist yet. But the fact that five major labs shipped updates within roughly two days is itself a signal: the AI model market has entered a phase where release speed and price are becoming weapons just as important as raw capability.

### Why it matters

When five models ship inside 48 hours, and one of the companies spends that same day patching its caching system to save money, that's a sign of a maturing market: pure quality differentiation is running out, and competition is shifting toward price and convenience — in other words, toward an ordinary, fairly boring cloud-services market.
