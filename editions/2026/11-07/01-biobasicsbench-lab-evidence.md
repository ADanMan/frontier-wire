---
date: 2026-11-07
rubric: science
title_ru: BioBasicsBench проверяет, когда лабораторные данные не дают ответа
title_en: BioBasicsBench tests when laboratory evidence cannot support an answer
dek_ru: OpenAI представила набор из 100 задач; баллы за анализ не равны готовности к самостоятельной работе в лаборатории.
dek_en: OpenAI introduced 100 tasks, while analysis scores remain distinct from readiness for independent laboratory work.
source: https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science
generated: true
---

## Русская версия

OpenAI 6 ноября [представила BioBasicsBench](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science), созданный вместе с Ligo набор из 100 задач по интерпретации исходных лабораторных данных. Компания сообщает для GPT-6 Astra на xhigh 66,7% доступных баллов против 43,8% у GPT-5.6 Sol. Это средняя оценка по критериям, а не доля полностью решённых задач или независимое подтверждение надёжности. Редакция не воспроизводила эксперимент и не проверяла модели на собственных лабораторных материалах.

Самостоятельный пример помогает понять, почему различие существенно. Представим таблицу измерений, в которой подписаны образцы, но не указаны единицы. Система может аккуратно прочитать каждое число и всё равно не иметь оснований для итогового сравнения. Полезный ответ здесь должен отделять извлечённые данные от недостающей информации. Уверенный вывод не становится лучше от гладкой формулировки. Иногда правильный следующий шаг — задать уточняющий вопрос, а не достраивать обстоятельства по наиболее привычному шаблону из памяти.

Для оценки такого помощника стоит заранее определить, за что начисляется результат. Один критерий может касаться чтения записи, другой — выбора допустимого сравнения, третий — признания неопределённости. Это наша иллюстрация возможной проверки, а не пересказ конкретного задания нового набора. Если объединить всё в одно слово «верно», будет трудно понять, что именно улучшилось. Если считать только отдельные правильные фрагменты, можно упустить несовместимость итогового ответа с ними. Оба уровня требуют внимания при разборе отчёта.

Важно различать способность анализировать предоставленный материал и право принимать решение о дальнейшей работе. Даже хороший ответ на ограниченный вопрос не устанавливает, как система поведёт себя при неполном описании, неверной подписи или новых условиях. Эти случаи следует проверять отдельно. Для собственного пилота полезно сохранить исходный файл, формулировку вопроса, ответ и обоснование оценки. Тогда спорный результат можно рассмотреть повторно, не полагаясь на память участника или пересказ того, что модель якобы увидела в прошлый раз.

Есть и вопрос о том, как выбирать следующий тест. Если проверять только примеры, похожие на удачную демонстрацию, можно получить слишком удобную картину. Более информативно заранее включить случаи, где для уверенного ответа чего-то не хватает. Оценщик должен отличать осторожность по делу от пустого отказа: система обязана объяснить, какое свидетельство отсутствует и почему без него вывод не следует. Это общий редакционный критерий полезности, а не дополнительный измеренный результат OpenAI или совет по проведению биологического эксперимента.

### Почему это важно

Новость предлагает конкретный способ обсуждать лабораторного ИИ-помощника через качество работы с доказательствами. Читателю стоит смотреть на смысл балла, условия проверки и оставшиеся ошибки. Умение сказать «данных недостаточно» может быть важнее убедительного ответа, если именно такой ответ не поддерживается предоставленными наблюдениями.

## English version

OpenAI [introduced BioBasicsBench on November 6](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science), a collection developed with Ligo comprising 100 tasks involving raw laboratory evidence. It reports 66.7% of available credit for GPT-6 Astra at xhigh, compared with 43.8% for GPT-5.6 Sol. This is a mean rubric score, rather than the proportion of completely solved tasks or independent certification of reliability. We have not reproduced the experiment or tested the models using our own laboratory materials.

An independent hypothetical example explains why that distinction matters. Imagine a measurement table with labelled samples but no units. A system could read every number accurately while lacking grounds for the requested comparison. A useful response would separate extracted observations from missing information. A confident conclusion does not improve merely because it is fluently expressed. Sometimes the appropriate next step is a clarification question rather than completing the circumstances with the most familiar pattern from memory. Correct reading and justified inference are different achievements.

An evaluation should specify what earns credit before an answer is examined. One criterion might concern reading a record, another choosing a legitimate comparison, and a third recognising uncertainty. This is our illustration of a possible assessment, not a description of a particular task in the new collection. Collapsing everything into a single correct-or-incorrect label can obscure what improved. Counting only individually correct fragments can miss an incompatible final conclusion. Both levels deserve attention when interpreting a report or comparing systems.

Analysing supplied material should also remain distinct from deciding what work to undertake next. A strong response to a constrained question does not establish behaviour under incomplete descriptions, incorrect labels or unfamiliar conditions. Those cases need separate assessment. A local pilot benefits from preserving the original file, question, response and scoring rationale. A disputed outcome can then be reconsidered without relying on someone's recollection or a paraphrase of what the model supposedly observed during an earlier attempt. Traceability supports a more specific discussion of failure.

Selecting the next test matters too. Restricting evaluation to cases resembling a successful demonstration can produce an unduly comfortable picture. A more informative design includes examples where some evidence needed for a confident answer is absent. The evaluator should distinguish justified caution from an empty refusal: the system needs to identify what is missing and why the conclusion does not follow without it. This is an editorial criterion for usefulness, not another measured OpenAI result or advice for performing a biological experiment.

### Why it matters

The announcement offers a concrete way to discuss laboratory assistance in terms of evidence handling. Readers should examine what a score measures, the test conditions and the remaining errors. Saying that the data are insufficient can be more valuable than supplying a persuasive answer that the observations do not support.
