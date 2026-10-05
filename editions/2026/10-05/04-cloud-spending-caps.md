---
date: 2026-10-05
rubric: economy
title_ru: Письмо о перерасходе или остановка: облачные лимиты становятся частью разговора об агентах
title_en: An overspending email or a stop: cloud limits join the conversation about agents
dek_ru: Саймон Уиллисон предлагает жёсткие ограничения по умолчанию; у AWS и Google уже есть механизмы с разным охватом и условиями.
dek_en: Simon Willison argues for hard limits by default; AWS and Google already offer mechanisms with different scopes and conditions.
source: https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/
generated: true
---

## Русская версия

Агент может быстро написать полезную программу, но её последующие обращения к платным сервисам оплачиваются отдельно. В [заметке от 3 октября](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) разработчик Саймон Уиллисон предлагает сделать жёсткие ограничения расходов обычным поведением таких сервисов. Его тезис прост: уведомление о достигнутом бюджете и прекращение платной работы — разные функции. Это предложение автора, а не объявленное общее правило облачного рынка.

Повод проверить тезис есть в документации поставщиков. В [анонсе нового опыта AWS от 16 сентября](https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience/) описан ежемесячный лимит для проекта после перехода на платный план. При достижении суммы проект приостанавливается. У отдельных проектов могут быть собственные ограничения. Сентябрьский анонс здесь служит контекстом к новой дискуссии, а не выдаётся за релиз 5 октября.

[Текущая инструкция AWS](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html) уточняет границы: новый опыт пока доступен ограниченному числу клиентов; лимит управляется владельцем проекта и требует платного плана. При остановке данные сохраняются, но отсутствие действий в течение 90 дней после паузы ведёт к их удалению. Для возобновления нужно увеличить лимит; некоторые ресурсы придётся запускать вручную. Поэтому остановка расходов не означает бессрочное хранение отключённого проекта.

У Google другой масштаб ограничения. В [описании Spend Caps от 28 июля](https://cloud.google.com/blog/topics/cost-management/new-early-anomalies-and-spend-caps-on-google-cloud-budgets) публичный предварительный режим охватывает конкретный сервис внутри одного проекта на фиксированный месяц. При достижении порога блокируется дальнейшее платное использование этого сервиса. Остальные сервисы вне области лимита не затрагиваются. При этом фиксированные договорные платежи, например за зарезервированную пропускную способность, продолжаются; cap не обнуляет весь счёт.

Сравнение показывает, почему одного слова «бюджет» в интерфейсе недостаточно. Важно знать область действия и последствие достижения порога. Ограничение проекта может остановить несколько связанных частей приложения. Ограничение отдельного сервиса оставляет другую инфраструктуру работающей, но приложение всё равно должно учитывать недоступность нужной операции. Это практический вывод из различий двух описанных механизмов, а не результат испытаний конкретного приложения редакцией.

Для читателя, который оценивает новый инструмент, полезен вопрос о поведении после остановки. Сохраняется ли состояние задачи? Видно ли пользователю, почему она прервана? Как возобновляется работа? Наличие лимита не отвечает автоматически на эти вопросы: платформа управляет расходами, а понятное поведение приложения требует отдельного проектирования. Быстрый старт с помощью агента эту часть работы не отменяет.

### Почему это важно

Обсуждение переносит внимание с скорости создания программы на условия её дальнейшей работы. Хороший контроль расходов должен иметь понятные границы и объяснимое действие при их достижении. Документы AWS и Google показывают реальные варианты, но не универсальную гарантию против любых платежей. Судить о механизме стоит по его области, доступности и правилам восстановления, сохраняя различие между уведомлением, остановкой использования и итоговым счётом.

## English version

An agent can quickly write a useful application, while the application's later calls to paid services are billed separately. In an [October 3 post](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/), developer Simon Willison argues that hard spending limits should be the default for such services. His distinction is straightforward: a budget notification and an actual stop to billable work are different features. This is his proposal, rather than a new rule adopted across the cloud market.

Providers' documentation offers concrete examples. An [AWS announcement dated September 16](https://aws.amazon.com/about-aws/whats-new/2026/09/New-AWS-Builder-Experience/) describes monthly project spending limits after upgrading to a paid plan. Reaching the chosen amount pauses the project. Additional projects can have their own limits. That earlier announcement is context for the current discussion; it is not presented here as a release made on October 5.

[AWS's current instructions](https://docs.aws.amazon.com/accounts/latest/reference/create-spend-limit.html) add qualifications. The new experience is available to a limited number of customers, requires a paid plan and gives project owners control of the limit. Data survives a pause, but is permanently deleted if no action is taken within 90 days. Reactivation requires increasing the limit, and some resources may need manual restarting. Pausing expenditure does not promise indefinite storage.

Google's mechanism has a different scope. Its [July 28 description of Spend Caps](https://cloud.google.com/blog/topics/cost-management/new-early-anomalies-and-spend-caps-on-google-cloud-budgets) says the public preview applies to a particular service in one project for a fixed month. The threshold blocks further billable use of that service, leaving services outside the budget's scope unaffected. Fixed contractual commitments, such as provisioned throughput charges, continue to bill. A cap therefore does not eliminate every component of an invoice.

The comparison shows why the word “budget” alone is insufficient. The scope and the action at the threshold matter. A project limit can interrupt several connected components. A service limit leaves other infrastructure running, but the application still needs to account for its missing operation. That is a practical inference from the two documented designs, rather than a result from testing a particular application for this article.

For someone assessing a new tool, the next questions concern behaviour after the stop. Is the task's state preserved? Can the user understand why it stopped? How does work resume? A spending mechanism does not automatically answer those questions. The platform controls usage, while the application needs its own understandable interruption and recovery behaviour. Building faster with an agent does not remove that design work.

### Why it matters

The discussion shifts attention from creating software quickly to the conditions under which it keeps running. Useful spending controls need clear boundaries and understandable enforcement. AWS and Google document real options, with different availability and recovery rules, rather than a universal guarantee against every charge. Their practical value depends on distinguishing an alert, a usage stop and the final bill.
