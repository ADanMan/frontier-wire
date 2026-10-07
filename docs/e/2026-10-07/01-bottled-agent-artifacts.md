---
date: 2026-10-07
rubric: ai
title_ru: Сильный ответ ИИ ещё не означает хороший массовый инструмент
title_en: A strong AI answer does not guarantee a good batch tool
dek_ru: Bottled проверяет, сможет ли агент превратить свои знания в дешёвое повторяемое решение.
dek_en: Bottled tests whether an agent can turn its capabilities into a cheap reusable solution.
source: http://arxiv.org/abs/2610.08775v1
generated: true
---

## Русская версия

В [препринте Agent in a Bottle от 6 октября](http://arxiv.org/abs/2610.08775v1) исследователи предлагают проверять отдельное умение ИИ: собрать экономное решение для повторяющейся задачи. Агент получает весь массив входных данных без правильных ответов, ограниченные ресурсы и должен выдать результат для каждого случая. В эксперименте 48 из 60 запусков оказались ниже доверительного интервала качества соответствующей модели, отвечающей на примеры напрямую. Это авторский результат ограниченного бенчмарка, а не оценка всех существующих агентов и не проверка нашей редакции.

[Открытый репозиторий Bottled](https://github.com/aktsonthalia/bottled) содержит отдельные сценарии агентного решения, прямого вызова модели и обучения небольшой модели на ответах учителя. Есть конфигурации задач, подготовка данных и учёт затрат. README пока отмечает две части как будущие дополнения: проверку загрязнения данных и оценку Jev. Поэтому опубликованный код помогает рассмотреть устройство эксперимента, но ещё не означает, что весь описанный в статье анализ можно воспроизвести одной готовой командой. Сам факт открытия репозитория полезно отделять от полноты воспроизведения.

Наше прочтение этой постановки: у удачного ответа и у рабочего инструмента разные критерии успеха. Представьте каталог, в котором нужно выделять материал товара. Несколько правильных примеров показывают, что модель понимает запрос. Для обработки целой коллекции дополнительно нужны устойчивый формат, сохранение результатов и понятное поведение на описаниях без нужного свойства. Это иллюстрация задачи, а не свидетельство о конкретном магазине или готовом коммерческом внедрении Bottled. Коллекция может содержать и простые случаи, и редкие формулировки; средний красивый ответ эту разницу скрывает.

Для собственной проверки мы бы сначала подготовили отдельную контрольную выборку, которую разработчик решения не использует при подборе правил. Затем сравнили бы прямые ответы модели и итоговый инструмент на одинаковых входах. Отдельно отметили бы пропуски, неподходящий формат и случаи, где правильный ответ отсутствует в исходном тексте. В таком сравнении важна цена завершённой обработки, включая создание решения, а не только цена одного последующего вызова. Здесь описан предлагаемый порядок проверки; мы его не выполняли и результатов не заявляем.

### Почему это важно

Исследование добавляет полезный вопрос к выбору ИИ: что остаётся после его работы и насколько надёжно это можно повторить? Для массовой задачи пригодность определяется проверенным результатом на всей нагрузке. Наш вывод — обсуждать качество ответа, полноту обработки и стоимость как отдельные свойства. Тогда экономия не маскирует потерянные строки, а успех на нескольких примерах не превращается в обещание готовой автоматизации.

## English version

The [October 6 preprint Agent in a Bottle](http://arxiv.org/abs/2610.08775v1) proposes testing a distinct AI capability: constructing an economical solution for a repetitive workload. An agent receives the complete unlabeled input collection, limited resources and a requirement to return a result for every instance. In the authors' experiment, 48 of 60 runs fell below the confidence interval of the corresponding model answering examples directly. This is a reported result from a limited benchmark, rather than a verdict on every existing agent or an experiment performed by this publication.

The [open Bottled repository](https://github.com/aktsonthalia/bottled) includes separate workflows for agent solutions, direct model calls and training a small model on teacher answers. It provides task configurations, data preparation and cost accounting. Its README still lists contamination judging and Jev evaluation as forthcoming additions. The code therefore helps readers inspect the experimental machinery, but its availability does not establish that every analysis described in the paper can already be reproduced with a single complete command. Openness and completeness are separate properties worth checking.

Our reading of the setup is that a successful answer and a working tool need different acceptance criteria. Imagine a catalog in which the task is to extract each product's material. A few correct examples demonstrate understanding of the question. Processing the entire collection also requires consistent formatting, saved outputs and appropriate handling of descriptions that never mention a material. This is an illustrative workload, rather than evidence about a particular store or an existing commercial Bottled deployment. Easy instances and unusual wording can coexist within the collection; a polished sample answer conceals that distribution.

For an independent assessment, we would first prepare a held-out reference set that the solution's builder cannot use to tune its rules. We would then compare direct model answers and the final tool on identical inputs. Missing outputs, invalid formats and cases where the requested information is absent would receive separate attention. The relevant cost is completed processing, including construction of the solution, rather than just one subsequent invocation. This is a proposed evaluation procedure. We have not run it and claim no results from it, savings included.

### Why it matters

The research adds a useful question to AI selection: what remains after the agent has worked, and how reliably can it be reused? Suitability for a batch task depends on verified results across the workload. Our conclusion is to discuss answer quality, completion and cost separately. That prevents cheap execution from concealing missing rows, or success on a handful of examples from becoming an unsupported promise of ready-made automation.
