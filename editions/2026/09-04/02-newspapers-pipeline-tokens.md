---
date: 2026-09-04
rubric: ai
title_ru: Миллиарды токенов из старых газет: как ИИ учится на архивах
title_en: Billions of tokens from old newsprint: teaching AI on the archives
dek_ru: Исследователи представили конвейер, который превращает оцифрованные исторические газеты в качественные данные для обучения языковых моделей.
dek_en: Researchers unveiled a pipeline that turns digitized historical newspapers into high-quality training data for language models.
source: https://huggingface.co/papers/2608.18972
generated: true
---

## Русская версия

Группа авторов во главе с Маттео Каргнелутти опубликовала работу [«Institutional Newspapers Pipeline»](https://huggingface.co/papers/2608.18972) — конвейер, который извлекает из архивов исторических газет миллиарды качественных токенов для обучения языковых моделей. В числе соавторов — Кэтрин Бробстон, Эбен Инглиш, Джейк Сэдоу, Кейси Бейли и другие.

Проблема, которую решают авторы, звучит просто, а на деле упирается в детали: старые газеты — это огромный и малоиспользуемый архив живой речи и общественной жизни, но их плотная, нерегулярная и часто зашумлённая вёрстка делает компьютерную обработку таких материалов сложной и ограниченной задачей. Колонки наезжают друг на друга, шрифты плывут от скана к скану, OCR путает заголовки с подписями к фотографиям — извлечь из этого читаемый связный текст в промышленных масштабах не так тривиально, как кажется.

Именно это авторы и предлагают решить конвейером, который доводит необработанные сканы до чистых, пригодных для обучения текстов в объёме миллиардов токенов. Для индустрии, которая всё чаще упирается в дефицит качественных данных для обучения новых моделей, архивы библиотек и институтов — один из немногих ещё не выработанных источников, и эта работа — конкретный шаг к тому, чтобы сделать его пригодным для использования.

### Почему это важно

Гонка за данными для обучения ИИ давно вышла за пределы интернета в его нынешнем виде — компании и исследователи всё активнее смотрят на архивы, которые раньше были доступны разве что историкам с лупой в читальном зале. Если такие конвейеры заработают массово, качество и разнообразие обучающих данных может вырасти не за счёт новых источников в сети, а за счёт того, что уже давно лежит на бумаге.

## English version

A team led by Matteo Cargnelutti published [the "Institutional Newspapers Pipeline" paper](https://huggingface.co/papers/2608.18972), describing a pipeline that extracts billions of high-quality tokens from historical newspaper archives for training language models. Co-authors include Catherine Brobston, Eben English, Jake Sadow, Kacie Bailey, and others.

The problem they're tackling sounds simple but hides in the details: historical newspapers are an abundant record of public life and everyday language, but their dense, irregular, and often noisy layouts make computational access to these materials both challenging and limited. Columns bleed into each other, fonts drift from scan to scan, and OCR routinely confuses headlines with photo captions — turning that into clean, coherent text at scale is harder than it looks.

That's exactly what the pipeline is built to fix, turning raw scans into training-ready text at a scale measured in billions of tokens. For an industry increasingly running into a shortage of quality training data, library and institutional archives are one of the few genuinely untapped sources left, and this work is a concrete step toward making them usable.

### Why it matters

The race for AI training data has already moved past the open internet as it exists today — companies and researchers are looking harder at archives that used to be accessible mostly to historians with a magnifying glass in a reading room. If pipelines like this scale up, the next gains in training-data quality and diversity may come not from new sources online, but from what's already been sitting on paper for a century.
