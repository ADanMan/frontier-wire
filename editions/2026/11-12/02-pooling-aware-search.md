---
date: 2026-11-12
rubric: ai
title_ru: Поисковую модель предлагают обучать сразу под сжатое представление
title_en: Training search models for the compressed representation they will use
dek_ru: Пример Sentence Transformers сравнивает качество при одинаковом числе векторов; результат не заменяет проверку своего корпуса.
dek_en: A Sentence Transformers example compares quality at a matched vector budget without settling results for another corpus.
source: https://huggingface.co/blog/token-pooling
generated: true
---

## Русская версия

Том Аарсен 11 ноября [описал обучение с учётом token pooling](https://huggingface.co/blog/token-pooling) для многовекторного поиска. В его примере объединение векторов документов сопровождается специальной обучающей целью. При одинаковом бюджете сжатия показатель NanoBEIR nDCG@10 вырос с 49,03 до 51,23. Это результат автора на определённой конфигурации, а не наша независимая проверка. Он не означает одинакового выигрыша на любом наборе документов или автоматического уменьшения всех расходов поискового сервиса в той же пропорции.

Общий вопрос понятен и без деталей модели. В самостоятельном условном примере архив содержит подробные документы, а поиску нужно отличать два похожих запроса. Если сократить представление, можно сохранить общую тему и потерять небольшое, но важное различие. Тогда индекс станет компактнее, однако нужный результат опустится ниже. Такой пример объясняет, почему экономию места полезно оценивать вместе с качеством поиска. Он не описывает конкретную ошибку опубликованной модели и не добавляет к эксперименту несуществующий набор измерений.

Для собственной проверки стоит сначала определить, что означает успешный поиск. Один пользователь ищет конкретную запись, другой — несколько источников по широкой теме. Показатель, удобный для первого сценария, может недостаточно описывать второй. Поэтому полезно заранее собрать запросы и ожидаемые релевантные документы, включая трудные различия. Это редакционная рекомендация по испытанию, а не утверждение о составе авторского набора. Фиксированный список случаев позволяет увидеть, какие ответы изменились после сжатия, а не ограничиваться впечатлением от среднего числа.

Сравнение должно сохранять условия. Если одновременно заменить модель, документы и способ оценки, станет трудно понять причину улучшения. В нашем условном пилоте можно сначала сравнить два представления на одном корпусе, а затем отдельно проверить перенос на новые материалы. Особенно полезны случаи, где различие между хорошим и плохим результатом мало заметно по общей теме. Тогда компактность проверяется не только на очевидных примерах, но и на тех деталях, ради которых пользователь вообще задаёт уточняющий запрос.

Ещё один вопрос — полный размер и стоимость системы. Меньше векторов не означает автоматически такую же экономию во всём приложении. Для собственного проекта нужно отдельно учитывать данные, индекс, подготовку и выдачу результата. Мы не вычисляли эти расходы для опубликованного примера и не приписываем автору универсальную оценку. Практически полезно записать, какие именно ресурсы измеряются и на каком этапе. Тогда техническая оптимизация не превратится в обещание, которое относится к другой части системы и не подтверждается экспериментом.

### Почему это важно

Сжатое представление становится частью того, чему учат модель, а не только последующим ограничением. Проверять такой подход стоит на одинаковом бюджете и реальных поисковых задачах. Новость даёт воспроизводимую отправную точку, но полезность для другого корпуса определяется сохранёнными различиями и качеством результатов, которые нужны его пользователям.

## English version

Tom Aarsen [described token-pooling-aware training on November 11](https://huggingface.co/blog/token-pooling) for multi-vector retrieval. His example combines merged document vectors with a corresponding training objective. At a matched compression budget, NanoBEIR nDCG@10 rises from 49.03 to 51.23. That is the author's result under specified conditions, not our independent reproduction. It does not imply identical gains on every document collection or that every cost of operating a search service decreases in the same proportion. Those are separate claims requiring separate measurements.

The underlying question can be understood without model details. In an independent hypothetical archive, search must distinguish two similar requests within detailed documents. A smaller representation might retain the general subject but lose a small, important distinction. The index would become more compact while the needed result moves down the ranking. That explains why storage should be assessed alongside retrieval quality. It does not describe a particular failure of the released model or add an experiment and measurements that the author never reported.

A local assessment should first establish what successful retrieval means. One user needs a specific record, while another wants several sources on a broad topic. A metric useful for the first scenario may not fully describe the second. It helps to prepare queries and expected relevant documents beforehand, including difficult distinctions. That is an editorial testing suggestion, not a claim about the author's evaluation collection. A fixed set makes it possible to inspect which answers changed after compression instead of relying on an impression created by one average score.

Comparisons also need stable conditions. Replacing the model, documents and evaluation procedure together would make the cause of an improvement difficult to identify. A hypothetical pilot could first compare representations on one corpus, then separately test transfer to new material. Cases where good and poor results share almost the same general topic can be especially informative. Compression is then examined on the details motivating a precise query, rather than only on obvious examples that would be easy for many representations to distinguish correctly.

Total system size and operating cost deserve their own measurements. Fewer vectors do not automatically imply a proportional saving throughout an application. A local project should distinguish document storage, index storage, preparation and result delivery. We have not calculated those costs for the published example or attributed a universal estimate to its author. Specifying the resource and processing stage helps prevent a technical optimisation from becoming a promise about a different component that the experiment did not measure. Clear accounting improves the usefulness of the comparison.

### Why it matters

The compressed representation becomes part of what the model learns, rather than only a later constraint. The approach deserves assessment at matched budgets and on actual retrieval tasks. It provides a reproducible starting point, while value on another corpus depends on preserving distinctions and returning the results its users need.
