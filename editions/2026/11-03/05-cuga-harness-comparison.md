---
date: 2026-11-03
rubric: ai
title_ru: IBM сравнила три агентские оболочки с одной моделью
title_en: IBM compares three agent harnesses using the same model
dek_ru: Новый разбор CUGA, Hermes и Deep Agents показывает влияние окружения; тест не измеряет соблюдение корпоративных правил.
dek_en: A new CUGA, Hermes and Deep Agents comparison examines the surrounding system, without measuring business-policy enforcement.
source: https://huggingface.co/blog/ibm-research/cuga-harness
generated: true
---

## Русская версия

IBM Research 3 ноября [опубликовала сравнение CUGA, Hermes и Deep Agents](https://huggingface.co/blog/ibm-research/cuga-harness) с одной моделью на AppWorld. Авторы указывают различия конфигураций, ограниченную выборку и отсутствие проверки механизмов политик в этих запусках. Это исследование команды CUGA, а не независимая сертификация. Его полезно читать как конкретный пример влияния агентского окружения, не превращая результат в универсальный рейтинг для разработки кода, личного помощника и корпоративного процесса одновременно.

Под оболочкой здесь понимается система вокруг модели, которая организует шаги и взаимодействие с инструментами. Чтобы оценить значение такой организации, рассмотрим собственный условный пример редакции. Помощнику нужно найти все записи определённого типа в приложении с постраничной выдачей. Модель может правильно понять запрос, но конечный список всё равно окажется неполным, если программа остановится после первой страницы. Ошибка результата в этом случае не сводится к знанию фактов или качеству языка: важен порядок получения и проверки данных.

Теперь добавим требование перед изменением записи показать её человеку. Получение полного списка не доказывает соблюдение этого требования. Система может успешно завершить задачу по одному критерию и нарушить другой. Поэтому полезно отдельно оценивать способность выполнить работу и механизм, который ограничивает допустимые действия. Наш пример не описывает реальный платёж или доступ к чьим-либо аккаунтам. Он показывает, почему показатель завершения задач нельзя без дополнительной проверки читать как показатель соблюдения всех правил эксплуатации.

Одинаковая модель — полезное условие сравнения, но не единственное. Для интерпретации нужны настройки инструментов, способы восстановления после ошибки, лимиты и критерии успеха. Если сравниваются разные готовые конфигурации, вывод относится прежде всего к этим конфигурациям в выбранной задаче. Он не отвечает автоматически на вопрос, что получится после другой настройки или в иной предметной области. Это не отменяет ценность опыта: он помогает поставить следующий проверяемый вопрос вместо поиска безусловного победителя по одному числу.

Есть и важное различие между демонстрацией и повторяемой оценкой. Один удачный запуск показывает возможность. Серия вариантов помогает увидеть устойчивость. Но даже устойчивость на тестовых приложениях ещё не доказывает готовность к реальной системе с её состоянием, правами и последствиями ошибок. Для переноса результата понадобятся собственные случаи и понятные границы проверки. Полезно заранее определить, что считается неполной работой, допустим ли повтор и какие изменения требуют отдельного решения, а не восстанавливать эти условия после неожиданного поведения.

### Почему это важно

Новости об агентах часто называют модель так, словно она одна объясняет всё поведение. Новый разбор напоминает об окружающей программе и её настройках, одновременно обозначая границы опыта. Для читателя практический вопрос конкретен: какой набор модели, инструментов и правил проверяли на какой работе? Ответ помогает понять применимость результата. Без него даже аккуратно подсчитанный процент не объясняет, подойдёт ли система для задачи, где цена неполного списка или лишнего действия совсем другая.

## English version

On November 3, IBM Research [published a comparison of CUGA, Hermes and Deep Agents](https://huggingface.co/blog/ibm-research/cuga-harness) using one model on AppWorld. The authors identify configuration differences, a limited sample and the absence of policy-enforcement testing in those runs. This is a study by the CUGA team rather than independent certification. It offers a concrete example of how an agent's surrounding system matters, without establishing one universal ranking for coding, personal assistance and enterprise processes at the same time.

A harness is the system around a model that organizes steps and tool interactions. An original hypothetical example illustrates why that organization matters. Suppose an assistant must find every record of a certain kind in an application with paginated results. The model could correctly understand the request, yet the final list would still be incomplete if the program stopped after the first page. The failure would not reduce to factual knowledge or language quality. The order in which information is obtained and checked would matter to the outcome.

Now add a requirement to show a record to a person before changing it. Retrieving the complete list does not establish compliance with that requirement. A system could finish the task under one criterion while failing another. Capability to perform work and enforcement of permitted actions consequently deserve separate evaluation. This example describes no real payment or account access. It demonstrates why task completion cannot be read as compliance with every operational rule without additional checks designed to measure those rules and the points where they must hold.

Holding the model constant is useful but does not hold everything constant. Tool settings, recovery behavior, limits and success criteria are needed to interpret the comparison. When different ready-made configurations are evaluated, the finding applies first to those configurations on the chosen workload. It does not automatically answer what would happen after tuning or in a different domain. That limitation does not remove the experiment's value: it helps formulate the next testable question rather than selecting an unconditional winner from a single reported number or a broad product description.

Demonstration and repeatable evaluation are also distinct. One successful run establishes possibility; variants help examine consistency. Consistency on test applications still does not prove readiness for a real system with its own state, permissions and consequences of failure. Transferring a result requires suitable cases and a defined verification boundary. Teams can specify in advance what counts as incomplete work, whether retries are acceptable and which changes require a separate decision. Reconstructing those conditions only after unexpected behavior would make the acceptance process much harder to interpret and reproduce.

### Why it matters

Agent coverage often names the model as though it explained the whole system's behavior. This comparison draws attention to the surrounding program and its configuration while qualifying the experiment's scope. The useful question is concrete: which combination of model, tools and rules was evaluated on what work? Its answer makes a result interpretable. Without that context, even a carefully calculated completion rate cannot establish suitability for a task where an incomplete list or an extra action has different consequences.
