---
date: 2026-09-13
rubric: tech
title_ru: Как OpenAI выдерживает миллиард пользователей ChatGPT и 22 миллиона запросов в секунду
title_en: How OpenAI keeps storage running for a billion ChatGPT users and 22 million requests a second
dek_ru: Внутренняя система Habitat выросла из питоновской библиотеки в глобальную платформу.
dek_en: An internal Python library called Habitat grew into a globally distributed platform.
source: https://openai.com/index/scaling-storage-one-billion-users-part-one
generated: true
---

## Русская версия

OpenAI опубликовала инженерный разбор того, как компания довела внутреннюю систему хранения данных под названием Habitat от обычной библиотеки на Python до глобально распределённой платформы, которая сейчас обслуживает более миллиарда пользователей ChatGPT и выдерживает 22 миллиона запросов в секунду, [говорится в блоге компании](https://openai.com/index/scaling-storage-one-billion-users-part-one). Это первая часть серии постов, посвящённой именно инфраструктуре хранения, а не моделям.

Цифра в 22 миллиона запросов в секунду — это не про генерацию текста моделью, а про операции чтения и записи данных: настройки аккаунта, история переписки, метаданные, кеши — всё то, что должно быть готово мгновенно при каждом обращении к продукту, независимо от того, сколько людей одновременно открыли приложение. Именно рост числа пользователей ChatGPT — с миллионов до более чем миллиарда — превратил Habitat из внутреннего инструмента в критическую часть инфраструктуры, отказ которой останавливает продукт целиком.

Путь «от библиотеки к платформе» — узнаваемый паттерн в истории больших технологических компаний: инструмент, написанный для решения локальной задачи одной команды, со временем становится общей зависимостью для десятков систем, и в какой-то момент его приходится переписывать не потому, что он плохо работал, а потому, что нагрузка выросла на порядки быстрее, чем архитектура, рассчитанная на изначальный масштаб.

Пост OpenAI не раскрывает конкретные технические решения — судя по формату «part one», это, скорее, введение в тему перед более подробными постами о конкретных архитектурных решениях. Судить о том, насколько инновационны эти решения, по одному вводному материалу преждевременно.

### Почему это важно

Инфраструктурные посты вроде этого редко попадают в заголовки рядом с анонсами новых моделей, но именно такая «скучная» инженерия хранения данных определяет, будет ли у миллиарда людей рабочий ChatGPT завтра утром или глобальный сбой.

## English version

OpenAI published an engineering write-up describing how the company grew an internal storage system called Habitat from a plain Python library into a globally distributed platform that now serves more than a billion ChatGPT users and handles 22 million requests per second, [according to the company's blog](https://openai.com/index/scaling-storage-one-billion-users-part-one). This is the first installment in a series focused specifically on storage infrastructure rather than models.

The 22-million-requests-per-second figure isn't about the model generating text — it's about data reads and writes: account settings, conversation history, metadata, caches — everything that has to be instantly available on every interaction with the product, regardless of how many people have the app open at once. It's the growth in ChatGPT's user base, from millions to over a billion, that turned Habitat from an internal tool into a critical piece of infrastructure whose failure would stop the entire product.

The "library that grew into a platform" arc is a familiar pattern in the history of large tech companies: a tool built to solve one team's local problem gradually becomes a shared dependency for dozens of systems, and at some point it has to be rebuilt — not because it worked poorly, but because load grew by orders of magnitude faster than an architecture designed for the original scale could handle.

OpenAI's post doesn't get into specific technical decisions — given the "part one" framing, this reads more like an introduction ahead of more detailed posts on the actual architecture. Judging how innovative those decisions are based on a single introductory post would be premature.

### Why it matters

Infrastructure posts like this rarely make headlines next to new model launches, but it's exactly this kind of unglamorous storage engineering that determines whether a billion people have a working ChatGPT tomorrow morning or a global outage.
