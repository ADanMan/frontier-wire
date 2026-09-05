---
date: 2026-09-05
rubric: ai
title_ru: Когда ИИ дообучает сам себя, ему нужно уметь забывать чужой опыт
title_en: When AI retrains itself, it needs to know which lessons not to keep
dek_ru: Новая работа предлагает автономным системам дообучения решать не только что переиспользовать из прошлых попыток, но и когда лучше не переиспользовать ничего.
dek_en: A new paper asks autonomous post-training systems to decide not just what to reuse from past attempts, but when reusing nothing at all is the right call.
source: https://huggingface.co/papers/2608.26730
generated: true
---

## Русская версия

Тинъюнь Ли, Вэньфэн Фэн, Вэйцин Ли, Абудукелиму Вуэркайси, Гохуа Лю и соавторы опубликовали работу [«Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training»](https://huggingface.co/papers/2608.26730). Речь о системах, которые сами дообучают большие языковые модели под новые домены, инструменты и требования: такие автономные пайплайны сами предлагают обновления, тренируют кандидатов и по фидбэку выбирают, что оставить.

Проблема, на которую указывают авторы: раз дообучение приходится повторять снова и снова при каждом изменении требований, у системы естественным образом накапливается опыт прошлых итераций — удачные и неудачные варианты обновлений, метрики, отклики оценщиков. Логично попробовать этот опыт переиспользовать в следующий раз, чтобы не начинать с нуля. Но авторы делают акцент именно на обратной стороне: слепое переиспользование чужого опыта может быть вредным, если новая задача на самом деле отличается от предыдущей сильнее, чем кажется на поверхности.

Отсюда и название — «знать, когда НЕ переиспользовать». Вместо того чтобы всегда тащить прошлый опыт в новую итерацию, авторы предлагают делать это условно: система должна сама оценивать, насколько релевантен накопленный опыт конкретной новой задаче, и в части случаев отказываться от переноса вовсе, полагаясь на свежее обучение. Дигест не даёт количественных результатов — насколько именно такой отбор улучшает качество дообучения по сравнению с «переносить всегда» или «не переносить никогда», остаётся судить по [самой статье](https://huggingface.co/papers/2608.26730).

### Почему это важно

Автономные системы, которые сами себя дообучают без постоянного присмотра человека, всё активнее продвигаются как способ ускорить адаптацию моделей. Но у самообучающейся системы есть соблазн: чем больше накопленного опыта, тем сильнее тянет его переиспользовать — даже там, где это заведёт не туда. Работа напоминает не самую эффектную, но важную вещь: умение вовремя отбросить прошлый опыт — часть интеллекта системы, а не её слабое место.

## English version

Tingyun Li, Wenfeng Feng, Weiqing Li, Abudukelimu Wuerkaixi, Guohua Liu, and co-authors published [the "Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training" paper](https://huggingface.co/papers/2608.26730). It looks at systems that retrain large language models on their own as domains, tools, and requirements shift — autonomous pipelines that propose updates, train candidate versions, and pick what to keep based on evaluation feedback.

The problem the authors flag: since post-training has to be repeated every time requirements change, such a system naturally accumulates experience from past rounds — which update variants worked, which didn't, what the metrics and evaluator feedback said. Reusing that experience for the next round sounds like an obvious way to skip starting from scratch. But the authors focus on the flip side: blindly reusing past experience can actively hurt results if the new task differs from the old one more than it looks on the surface.

Hence the title — knowing when *not* to reuse. Instead of always carrying past experience into a new round, the authors propose doing it conditionally: the system should judge how relevant its accumulated experience actually is to the specific new task, and in some cases skip the transfer entirely, training fresh instead. No quantitative results made it into the available summary — how much this selective approach improves on "always transfer" or "never transfer" as baselines is a question for [the paper itself](https://huggingface.co/papers/2608.26730).

### Why it matters

Autonomous systems that retrain themselves without constant human oversight are increasingly pitched as a way to speed up model adaptation. But a self-training system has a built-in temptation: the more experience it accumulates, the harder it pulls toward reusing it — even where that leads somewhere wrong. The paper is a reminder of something unglamorous but real: knowing when to throw out past experience is part of a system's intelligence, not a gap in it.
