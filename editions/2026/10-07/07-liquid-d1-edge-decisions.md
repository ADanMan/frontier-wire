---
date: 2026-10-07
rubric: ai
title_ru: Liquid AI выпускает компактные модели для решений без длинного ответа
title_en: Liquid AI releases compact models for decisions without long answers
dek_ru: Открытые веса d1-3B и экспериментальной d1-omni-600M сопровождаются разными режимами и ограничениями.
dek_en: Open weights for d1-3B and experimental d1-omni-600M come with distinct modes and limits.
source: https://huggingface.co/blog/LiquidAI/open-d1
generated: true
---

## Русская версия

Liquid AI 7 октября [объявила выпуск d1-3B и d1-omni-600M](https://huggingface.co/blog/LiquidAI/open-d1) с открытыми весами. Это модели для структурированных решений: они не сочиняют последовательность выходных токенов, а отвечают за один проход. d1-3B принимает текст и изображения; экспериментальная omni-версия работает с текстом и изображениями либо аудио. Компания не приводит замеры скорости для меньшей модели, подчёркивая раннюю исследовательскую стадию. Следовательно, компактность и быстродействие двух выпусков нельзя автоматически считать одинаково подтверждёнными. Заявленные результаты принадлежат авторам; наша редакция эти модели не запускала и собственных оценок качества не имеет.

[Карточка d1-3B](https://huggingface.co/LiquidAI/d1-3b) показывает зависимость скорости от нагрузки. Для Apple M5 Pro один вопрос указан как 30 миллисекунд, а состояние длиной около 3,4 тысячи токенов — 640 миллисекунд. Измеряются прогретые вызовы. В описании GPU-режима отдельно отмечено, что первая новая форма входа может требовать выбора ядра или компиляции. Поэтому короткое время отдельного вопроса нельзя переносить на любой запрос, запуск приложения целиком или первое обращение к модели. Важно сохранить рядом число, устройство, вид входа и режим измерения.

У [d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) свои ограничения. Карточка уточняет 587 миллионов параметров, аудиофрагменты до 30 секунд и обучение аудиозадач на запросах англоязычного говорящего к помощнику. Изображения и аудио не передаются одновременно в одном запросе. Для выбора режима это полезнее общего слова «мультимодальная»: оно не обещает произвольное сочетание всех данных. Поддержка нескольких типов входа, качество на каждом типе и удобство интеграции остаются отдельными свойствами. Особенно не стоит читать пример успешного ответа как доказательство универсальной работы на незнакомом языке или другой записи.

Наше прочтение: такие модели интересны там, где заранее понятен набор допустимых решений. Представьте распределение технических обращений по нескольким командам. Система должна выбрать категорию, а не написать убедительный абзац о выборе. Это наш пример применения, а не готовое внедрение из релиза. Проверять его мы бы начали с реальных формулировок и сложных пограничных случаев, включая обращения, которые не подходят ни одной категории. Отдельно измерили бы первый и повторные вызовы. Цена ошибочного распределения тоже входит в оценку полезности, даже если сам ответ получен очень быстро.

### Почему это важно

Релиз расширяет выбор инструментов для коротких решений рядом с генеративными моделями. Наш вывод — сравнивать их по конкретной задаче и условиям выполнения. Нулевое число выходных токенов описывает способ получения ответа; оно не отменяет вычисления, проверку качества или ограничения входа. Именно это различие помогает обсуждать компактную модель без обещаний универсальной замены чат-ассистента.

## English version

Liquid AI [announced open-weight d1-3B and d1-omni-600M on October 7](https://huggingface.co/blog/LiquidAI/open-d1). These models make structured decisions in a single forward pass instead of composing a sequence of output tokens. d1-3B accepts text and images; the experimental omni version uses text with images or audio. The company reports no speed measurements for the smaller model, emphasizing its early research status. Compact size and latency therefore cannot be treated as equally established properties of both releases. Reported evaluations belong to the authors; we have not run these models or produced independent quality measurements.

The [d1-3B model card](https://huggingface.co/LiquidAI/d1-3b) demonstrates the relationship between latency and workload. On an Apple M5 Pro, it lists 30 milliseconds for one question and 640 milliseconds for a state of roughly 3,400 tokens. These are warm calls. Its GPU description separately notes that a first new input shape can incur kernel selection or compilation. A short single-question time consequently cannot be generalized to every input, total application startup or the first model invocation. The number belongs alongside its device, input type and measurement conditions, rather than in isolation.

The [d1-omni-600M card](https://huggingface.co/LiquidAI/d1-omni-600M) sets different boundaries. It specifies 587 million parameters, audio clips limited to 30 seconds and audio training tasks involving an English speaker's requests to an assistant. Images and audio cannot appear together in one request. That is more useful for selecting a mode than the broad word multimodal: it does not promise arbitrary combinations of all data types. Input support, quality on each modality and ease of integration remain separate properties. A successful example should especially not be read as evidence of universal performance on another language or recording style.

Our reading is that such models are interesting where the allowable decision set is known in advance. Imagine routing technical requests among a few teams. The system needs to choose a category rather than write a persuasive paragraph about its choice. This is our application example, not an existing deployment from the release. We would begin evaluating it with real wording and difficult boundary cases, including requests that fit none of the categories. Cold and repeated calls would receive separate measurements. The cost of a wrong routing decision also belongs in the assessment, even when the answer itself arrives quickly.

### Why it matters

The release expands the selection of short-decision tools alongside generative models. Our conclusion is to compare them on a specific task under specified operating conditions. Zero output tokens describes how an answer is obtained; it does not eliminate computation, quality checks or input limits. Keeping that distinction visible allows compact models to be discussed without promising a universal replacement for conversational assistants.
