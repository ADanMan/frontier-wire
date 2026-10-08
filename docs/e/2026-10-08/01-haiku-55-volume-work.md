---
date: 2026-10-08
rubric: ai
title_ru: Haiku 5.5 делает ставку на массовые задачи и разную цену длинного контекста
title_en: Haiku 5.5 targets high-volume work with separate long-prompt pricing
dek_ru: Anthropic выпустила новую малую модель, но дешёвый запрос и дешёвая завершённая задача остаются разными вещами.
dek_en: Anthropic has released a new small model, with economics that depend on prompt length and the work being completed.
source: https://www.anthropic.com/claude-haiku-5-5
generated: true
---

## Русская версия

Anthropic [представила Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) 7 октября. Компания адресует модель большим потокам относительно коротких задач: сводкам, классификации, сжатию контекста и вспомогательной работе внутри более крупных агентных систем. Это важный поворот в разговоре об ИИ: полезность определяется не только самым впечатляющим ответом, но и тем, сколько одинаковых операций можно выполнить с приемлемой скоростью и стоимостью.

В объявлении есть две ценовые ступени. Для промптов до 100 тысяч токенов включительно миллион входных токенов стоит 0,10 доллара, выходных — 0,50. Выше этого порога указаны 0,50 и 2,50 доллара соответственно. Это тарифы Claude Platform из анонса, а не цена подписки на чат. Поэтому фраза «новый Haiku дешевле» требует уточнения: длинный контекст попадает в другой режим расчёта, а длина ответа тоже влияет на счёт.

У модели впервые в линейке Haiku появилась регулируемая интенсивность вычислений, effort. Пользователь может выбирать компромисс между расходами и способностью решать сложную задачу. Здесь нет универсальной настройки, автоматически выгодной для любого потока. Если система обрабатывает тысячи однотипных запросов, разумный предмет сравнения — качество именно этих операций при выбранном effort, включая повторные попытки и проверку результата. Это редакционный вывод о способе оценки, не обещание производителя.

Anthropic также показывает улучшения относительно Haiku 4.5 в собственных тестах. Но сама компания оставляет Sonnet 5.5 и Opus 5.5 более подходящими вариантами для сложной агентной работы с кодом. Получается понятное разделение труда: меньшая модель может разбирать отдельные фрагменты, пока большая ведёт задачу целиком. Само слово «агент» не делает все поручения одинаковыми по сложности; классификация письма и исправление многошаговой сборки требуют разных проверок.

Модель уже доступна через Claude Platform и облачные платформы, перечисленные в анонсе, включая AWS, Google Cloud и Microsoft Azure. Идентификатор API — `claude-haiku-5-5`. Сопутствующее снижение цены чтения кэша Sonnet объявлено действующим с 7 октября. Ежемесячные API-кредиты для подписчиков Max и Team обещаны к развёртыванию в течение недели: это отдельная программа, которую нельзя считать уже начисленной каждому аккаунту.

### Почему это важно

Дешёвая малая модель расширяет набор задач, которые вообще имеет смысл автоматизировать. Но цена токена ещё не показывает цену готового результата. Для читателя, сравнивающего системы, полезнее увидеть пример своего рабочего потока: сколько запросов потребовалось, какие ответы пришлось переделать и что проверил человек. Именно такая оценка превращает новую тарифную таблицу в понятный инструмент выбора, а не в ещё один рекорд рекламного слайда.

## English version

Anthropic [introduced Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) on October 7. The company positions the small model for high-volume work such as summaries, classification, context compaction and supporting tasks within larger agent systems. The interesting shift is toward routine operations. A model can be useful because it handles a repeated job economically, even when it is not the strongest choice for the most demanding assignment.

The announcement separates pricing by prompt length. For prompts up to and including 100,000 tokens, a million input tokens costs $0.10 and a million output tokens costs $0.50. Above that threshold, the listed rates are $0.50 and $2.50. These are Claude Platform rates in the launch announcement, rather than a chat subscription price. A comparison therefore needs to account for both the prompt bracket and the volume of generated text.

Haiku now also has an adjustable effort setting. It lets users trade computational spending against capability, instead of assuming one setting is right for every workload. Our reading is that repeated tasks should be evaluated at the setting actually intended for production. The relevant question is whether the model completes that particular operation reliably, including retries and verification. A lower rate on the price sheet alone does not answer it.

Anthropic reports improvements over Haiku 4.5 in its evaluations, while explicitly retaining Sonnet 5.5 and Opus 5.5 as better choices for complex agentic coding. That distinction suggests a division of labor: a small model can handle a bounded piece of work while a larger one coordinates the whole assignment. It also prevents the label “agent” from hiding the difference between sorting a document and resolving a difficult software problem. Those jobs need different evidence of success.

Availability is described as immediate across the Claude Platform and the cloud platforms named in the announcement, including AWS, Google Cloud and Microsoft Azure. The API identifier is `claude-haiku-5-5`. The accompanying cut in Sonnet cache-read pricing is effective from October 7. Monthly API credits for Max and Team subscribers are a separate rollout promised during the week; the announcement does not establish that every eligible account has already received them.

### Why it matters

A cheaper small model can make previously uneconomic workflows worth trying. The useful unit of comparison, however, is a completed and checked task. For a reader assessing an AI system, a representative workflow can reveal how many calls it required, how often an answer needed revision and where a person still reviewed the output. That turns a launch into an operational question rather than a contest between headline prices. Haiku's new pricing and effort controls provide more choices, but choosing well still depends on the work being done.
