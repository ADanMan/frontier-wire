---
date: 2026-10-28
rubric: ai
title_ru: Ai2 проверил, почему ИИ меняет вердикт о новизне научной идеи
title_en: Ai2 tests why AI changes its verdict on a research idea's novelty
dek_ru: Новый набор тестов показывает чувствительность оценок к формулировке вопроса, особенно для сгенерированных идей.
dek_en: A new benchmark reveals sensitivity to question wording, especially when evaluating generated ideas.
source: https://huggingface.co/blog/allenai/novelty-bench
generated: true
---

## Русская версия

Научную идею мало придумать: нужно понять, добавляет ли она что-то к уже известному. Когда эту проверку поручают языковой модели, несколько слов в вопросе могут заметно изменить ответ. Ai2 27 октября [представил исследование и тестовый набор для таких судей](https://huggingface.co/blog/allenai/novelty-bench). Авторы проверяли, как на оценку новизны влияют инструкции, поиск литературы и способ сравнения идей. Результат касается надёжности процедуры оценки, а не способности ИИ окончательно решить, что считать научным открытием.

В одном опыте GPT-5.4 сравнивал пары из человеческой и сгенерированной идеи. Инструкция, сообщавшая, что рецензенты признали новой ровно одну из них, давала 93,5 процента точности. После перехода к более простому вопросу показатель упал до 40,9 процента. Пары оставались прежними. Такое изменение показывает, что решение зависит от рамки задания; оно не означает, что сама научная ценность идеи поменялась между двумя запусками или что тот же эффект неизбежен у каждой модели.

Для человеческих идей команда использовала рецензии ICLR 2026. В группу с сильными свидетельствами новизны вошли 154 идеи, в противоположную — 145. Отбор учитывал явные суждения рецензентов, а не только принятие или отклонение статьи. Это содержательное различие: работа может быть полезной без большого нового результата, а оригинальная идея может иметь другие недостатки. Но такой отбор всё равно описывает конкретное научное сообщество и заданные правила включения в набор.

В отдельной части человеческие идеи сопоставили с идеями простого генератора без поиска и итераций. Предположение об их меньшей новизне авторы называют слабой разметкой, а не проверенным фактом о каждом примере. Дополнительная экспертная проверка охватила тридцать пар, преимущественно из трудных случаев. Эти ограничения не отменяют наблюдаемой смены ответов при переформулировке: саму нестабильность можно заметить даже без окончательного согласия, какой вариант в каждой паре действительно оригинальнее.

Больше поиска и вычислений также не обеспечивали устойчивого улучшения во всех рассмотренных настройках. Для читателя это повод раздельно оценивать источники, критерий и воспроизводимость суждения. Уверенно написанный отзыв ещё не показывает, какие работы были проверены и насколько вердикт сохраняется при разумной смене инструкции. Редакция опирается на полный институциональный разбор Ai2 и не выдаёт его результаты за собственное воспроизведение эксперимента или независимую экспертизу всех идей.

### Почему это важно

Автоматический отбор исследовательских направлений требует проверки самого оценщика. Если формулировка меняет порядок предпочтений, сравнение двух генераторов может отражать устройство судьи. Новый набор помогает сделать эту проблему измеримой. Практический вывод скромнее лозунга о замене рецензентов: прежде чем опираться на балл новизны, нужно выяснить его устойчивость и понять, на каких свидетельствах он основан. Иначе удобная цифра придаёт лишнюю определённость ещё открытому научному вопросу.

## English version

Generating a research idea leaves another task: establishing what it adds to existing knowledge. When a language model makes that judgement, a few words in the question can substantially change the answer. On October 27, Ai2 [introduced a study and benchmark for novelty judges](https://huggingface.co/blog/allenai/novelty-bench), examining prompts, literature retrieval and comparison formats. The findings concern the reliability of an evaluation procedure, rather than establishing that AI can definitively decide what counts as a scientific discovery across every field and research setting.

In one experiment, GPT-5.4 compared pairs containing a human-authored and a generated idea. An instruction saying reviewers had identified exactly one idea as novel produced 93.5 percent accuracy. Switching to a simpler question reduced it to 40.9 percent, with the same pairs. The change shows sensitivity to the task's framing. It does not mean the underlying contribution changed between runs or that every model will exhibit the same shift under every possible wording of the question.

For human-authored ideas, the researchers mined ICLR 2026 reviews. A pool with strong evidence of novelty contained 154 ideas; a lower-novelty pool contained 145. Selection used explicit reviewer statements rather than paper acceptance alone. That distinction matters: useful work can lack a major original contribution, while an original idea can have other weaknesses. The resulting sample nevertheless reflects a particular research community and specified inclusion rules, rather than providing an exhaustive standard for judging originality everywhere in science.

A separate setting paired human ideas with outputs from a simple generator operating without search or iterative feedback. The assumption that those generated ideas were less novel is described as weak labeling, not a verified judgement for every example. An additional expert check covered thirty pairs, weighted toward difficult cases. These limitations do not erase the observed verdict changes. Instability under rephrasing can be measured even without final agreement about which idea in every pair is genuinely more original.

More retrieval and computation did not consistently improve every evaluated setup either. Readers should therefore consider the evidence retrieved, the criterion applied and the repeatability of the judgement separately. A confident review does not establish which prior work was examined or whether the verdict survives reasonable prompt changes. Frontier Wire is reporting Ai2's complete institutional account, rather than independently reproducing its experiments or claiming to have conducted an expert review of all the ideas included in the benchmark.

### Why it matters

Automated selection of research directions requires evaluating the evaluator. If wording changes preferences, a comparison between two idea generators may partly measure how the judge was configured. The benchmark makes that problem easier to study. The practical implication is narrower than replacing peer review: before relying on a novelty score, establish how stable it is and which evidence supports it. Otherwise a convenient number gives an unresolved scientific question more certainty than the evaluation can justify.
