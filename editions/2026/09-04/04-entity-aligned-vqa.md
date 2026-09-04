---
date: 2026-09-04
rubric: ai
title_ru: Не «похоже», а «то самое»: как научить ИИ узнавать редкие объекты на фото
title_en: Not "looks like" but "is that": teaching AI to recognize rare objects in photos
dek_ru: Новый метод выравнивания сущностей нацелен на вопросы по изображениям, где обычный поиск по визуальному сходству регулярно промахивается.
dek_en: A new entity-alignment method targets visual questions where plain image-similarity search keeps missing the mark.
source: https://huggingface.co/papers/2608.21450
generated: true
---

## Русская версия

Ханруй Сюй, Чжэнсянь У, Юньяо Юй, Чжохун Чэнь, Жуй Кун и соавторы опубликовали работу [«Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering»](https://huggingface.co/papers/2608.21450), посвящённую задаче «визуальных вопросов на основе знаний» (KB-VQA) — когда системе нужно ответить не просто «что на картинке», а что-то, требующее внешних знаний о конкретной, редко встречающейся сущности.

Авторы указывают на слабое место существующих подходов: большинство систем поиска для таких вопросов опираются на модели вроде CLIP, которые ищут изображения, похожие визуально, а не сущности, совпадающие фактически. Проблема в том, что визуальное сходство и фактическое совпадение — разные вещи. Два разных здания могут выглядеть архитектурно похожими, но быть совершенно разными объектами с разной историей; система, ищущая «похожее», в таком случае система найдёт не то, что нужно.

Решение, которое предлагают авторы, — «выравнивание по сущностям» вместо поиска по визуальному сходству: вместо того чтобы искать картинки, похожие на данную, система пытается напрямую сопоставить объект на фото с конкретной сущностью в базе знаний. Особенно это должно помочь с «длинным хвостом» — редкими объектами, которых мало в обучающих данных и которые визуальное сходство склонно путать с чем-то более распространённым.

### Почему это важно

Системы, которые отвечают на вопросы по изображениям, всё активнее используют в поиске, ассистентах и обработке документов. Пока такие системы путают «похоже» с «то же самое», они будут ошибаться именно там, где точность важнее всего — на редких, специфичных случаях, а не на типовых котиках и автомобилях, на которых легко получить хороший результат.

## English version

Hangrui Xu, Zhengxian Wu, Yunyao Yu, Zhuohong Chen, Rui Cong, and co-authors published [the "Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering" paper](https://huggingface.co/papers/2608.21450), tackling knowledge-based visual question answering (KB-VQA) — questions that require external knowledge about a specific, often rare entity, not just a description of what's in a photo.

The authors point to a weak spot in existing systems: most retrieval pipelines for this task rely on CLIP-style models, which retrieve images that look visually similar rather than entities that actually match. The problem is that visual similarity and factual identity aren't the same thing. Two different buildings can look architecturally alike while being completely different landmarks with different histories; a system searching for "similar-looking" images will retrieve the wrong one.

Their proposed fix is entity-aligned retrieval instead of similarity search: rather than looking for images that resemble the query, the system tries to match the object in the photo directly to a specific entity in a knowledge base. That should matter most for the long tail — rare objects underrepresented in training data, which visual-similarity search tends to confuse with something more common.

### Why it matters

Visual question-answering systems are increasingly showing up in search, assistants, and document processing. As long as those systems confuse "looks like" with "is," they'll keep failing exactly where accuracy matters most — on rare, specific cases, not on the generic cats and cars that are easy to get right.
