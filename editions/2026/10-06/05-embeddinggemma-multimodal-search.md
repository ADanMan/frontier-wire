---
date: 2026-10-06
rubric: ai
title_ru: EmbeddingGemma 2 объединяет текст, звук и видео для локального поиска
title_en: EmbeddingGemma 2 brings text, sound and video into local search
dek_ru: Открытая модель строит общий векторный индекс; экономия памяти требует выбора режима и проверки качества.
dek_en: The open model supports a shared vector index, with memory savings depending on configuration and quality checks.
source: https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/
generated: true
---

## Русская версия

Google 6 октября [представила EmbeddingGemma 2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/) — открытую модель для поиска по тексту, коду, изображениям, видео и аудио в общем пространстве представлений. Полная конфигурация содержит 740 миллионов параметров и распространяется под Apache 2.0. Компания ориентирует её на устройства пользователей. Это модель эмбеддингов: она превращает входные материалы в векторы для сопоставления, а не пишет ответы сама. В анонсе заявлены возможности локального поиска; считать любой готовый продукт полностью автономным только по этому описанию было бы преждевременно.

[Карточка модели](https://huggingface.co/google/embeddinggemma-2) показывает цену сжатия: в её таблице показатель MMEB Overall снижается с 59,01 при 768 измерениях до 45,65 при 128. Это результаты авторской оценки, а не измерения нашей редакции. Карточка также предупреждает о неодинаковом качестве для разных языков, зависимости от обучающих данных и сложности неоднозначных формулировок. Режим float16 не рекомендован из-за диапазона активаций; указаны bfloat16 или float32. Поэтому одной цифры размера недостаточно для выбора рабочего режима.

В [руководстве разработчика](https://developers.googleblog.com/en/embeddinggemma-2-the-developer-guide/) описана модульная загрузка: текстовый режим использует 270 миллионов параметров, а зрительный и звуковой кодировщики подключаются по необходимости. Векторы можно сокращать, но после обрезки их нужно нормализовать, а запросы и документы сравнивать в одинаковой размерности. Все виды входа делят окно из 8 192 токенов. Максимум для одного типа данных нельзя одновременно обещать каждому типу в смешанном запросе.

Практический смысл, по нашему прочтению, — возможность построить единый способ поиска для разнородной коллекции. Представьте архив проекта: описание задачи, снимок стенда и запись обсуждения. Пользователь мог бы сформулировать вопрос словами, а приложение предложить подходящие материалы разных типов. Здесь важно, что сходство — только этап отбора. Найденная запись может содержать устаревшее решение, а похожая фотография — другой прибор. Приложению всё равно понадобятся названия, даты, понятные ссылки на оригиналы и проверка того, почему результат попал в выдачу.

Мы бы оценивали такую систему на собственной небольшой подборке запросов, где известны нужные документы и трудные похожие примеры. Отдельно стоит сравнить полный и сокращённый индекс: сколько места удалось сэкономить и какие материалы перестали находиться. Это предлагаемая проверка для внедрения, а не заявление о проведённом нами бенчмарке. Рекламное «для устройства» становится полезным инженерным свойством только вместе с выбранной конфигурацией и конкретной нагрузкой.

### Почему это важно

Модель расширяет набор материалов, доступных одному поисковому механизму, и даёт разработчику несколько способов управлять затратами. Но хороший поиск определяется тем, что человек действительно нашёл нужное. Проверка выдачи и сохранение контекста оригинала остаются столь же существенными, как компактность модели.

## English version

Google [introduced EmbeddingGemma 2 on October 6](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/), an open model mapping text, code, images, video and audio into a shared representation space. Its full configuration has 740 million parameters and an Apache 2.0 license. The company targets consumer devices. This is an embedding model: it produces vectors for comparison, rather than writing answers itself. The announcement describes local search capabilities; it does not establish that every application using the model will run entirely offline.

The [model card](https://huggingface.co/google/embeddinggemma-2) makes the compression tradeoff visible. Its MMEB Overall score falls from 59.01 at 768 dimensions to 45.65 at 128. These are the authors' evaluations, not our measurements. The card also identifies uneven language performance, training-data dependence and difficulty with ambiguous wording. It advises against float16 because of activation range, recommending bfloat16 or float32 instead. Model size alone therefore cannot determine a suitable operating configuration.

The [developer guide](https://developers.googleblog.com/en/embeddinggemma-2-the-developer-guide/) describes modular loading: the text configuration has 270 million parameters, with vision and audio encoders added as needed. Vectors can be shortened, but require normalization after truncation; queries and documents must share a dimension. All input types share an 8,192-token window. Single-modality maxima should not be promised simultaneously for every component of a mixed input. These choices affect the actual system a developer assembles, beyond the headline parameter count.

Our reading is that the opportunity lies in creating one search method for a mixed collection. Imagine a project archive containing a task description, a photograph of a test bench and an audio recording of a discussion. A written question could lead an application to offer relevant materials in several formats. Similarity would still be a selection step. A recording might contain an obsolete decision, and a similar photograph might show a different instrument. Names, dates, clear links to originals and an explanation of the result remain valuable parts of the interface.

We would assess such a system on a small set of real queries with known relevant documents and deliberately confusing alternatives. Comparing full and shortened indexes would then show both storage savings and the materials no longer retrieved. This is a proposed adoption check, not a benchmark we claim to have performed. The promise of device-friendly operation becomes a useful engineering property only alongside a chosen configuration and a concrete workload.

### Why it matters

The model broadens the types of material one search mechanism can handle and offers several ways to control resource use. Successful retrieval is still measured by whether a person finds what they need. Checking the results and preserving the original material's context matter alongside compact weights.
