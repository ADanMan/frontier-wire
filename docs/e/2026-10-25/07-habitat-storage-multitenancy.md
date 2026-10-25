---
date: 2026-10-25
rubric: tech
title_ru: Habitat возвращает общие базы с защитой от слишком шумных соседей
title_en: Habitat returns to shared storage with stronger noisy-neighbor controls
dek_ru: Вторая часть инженерного разбора OpenAI объясняет компромисс между изоляцией нагрузок и планированием ресурсов.
dek_en: OpenAI's second engineering installment examines the tradeoff between workload isolation and capacity planning.
source: https://openai.com/index/scaling-storage-one-billion-users-part-two
generated: true
---

## Русская версия

Хранилище можно разделить между многими командами, но тогда особенно прожорливый сосед способен испортить жизнь остальным. Можно выдать каждому собственную площадку, но её придётся отдельно рассчитывать и обслуживать. OpenAI 23 октября опубликовала [вторую часть истории Habitat](https://openai.com/index/scaling-storage-one-billion-users-part-two), где объясняет возвращение к общим контейнерам Azure Cosmos DB после периода разделения нагрузок. Это продолжение сентябрьского материала Frontier Wire о платформе, с новыми подробностями устройства баз данных.

Контейнер здесь — единица организации данных и выделенной пропускной способности базы, а не пользовательская папка. При совместной работе разные задачи конкурируют за реальные ресурсы под логическим разделением. Поэтому аккуратная граница в интерфейсе ещё не гарантирует, что тяжёлая фоновая операция не помешает интерактивному запросу. Именно это имеют в виду под «шумным соседом»: проблема касается распределения мощности, а не смешивания пользовательских документов.

Выделение отдельных контейнеров уменьшило область возможного сбоя, но принесло другой счёт. Каждой продуктовой команде пришлось планировать собственные потребности, а рост новой функции перестал сглаживаться общей нагрузкой. Резервировать достаточно мощности для неожиданного всплеска и одновременно не держать лишние ресурсы — разные цели. Рассказ интересен тем, что авторы не представляют изоляцию универсальным ответом: организационные издержки тоже влияют на надёжность.

Возврат к совместному размещению, по описанию инженеров, сопровождался ограничением наиболее горячих ключей и приоритетами запросов. Фоновую работу можно притормозить раньше, чем операции, которых ждёт человек. Это меняет смысл общей базы: она становится управляемой очередью потребностей с разной срочностью, а не обещанием всем одинаковой скорости при любом поведении соседей. Перенос данных между вариантами размещения остаётся отдельной частью платформы.

Авторы также разбирают задержки чтения. Близость данных, кеширование и сокращение накладных расходов сервиса работают вместе; выводить всё улучшение из одного языка программирования было бы неверно. В частности, обновление кешей связано с потоком изменений базы. Полезно различать доступный рядом сохранённый объект и запрос, которому всё-таки нужно идти в основное хранилище: ускорение обычного случая не делает все обращения одинаковыми.

### Почему это важно

Разбор даёт практическую картину решений, которые редко видны за ответом ИИ-приложения. Это рассказ самих операторов системы, а не независимый сравнительный тест облачных баз. Его стоит читать как набор компромиссов: кому принадлежит планирование, какая работа получает приоритет и как система ведёт себя при перегрузке. Для собственной инфраструктуры полезнее перенести эти вопросы, чем копировать название базы или архитектуру компании другого масштаба. Удобство продукта зависит и от таких приземлённых решений.

## English version

A shared database lets many teams use the same capacity, but an unusually demanding neighbor can disrupt everyone else. Give each team its own allocation and someone must plan and operate each one separately. On October 23, OpenAI published [the second installment of its Habitat engineering account](https://openai.com/index/scaling-storage-one-billion-users-part-two), explaining a return to shared Azure Cosmos DB containers after a period of separating workloads. It adds database-level detail to the platform story Frontier Wire covered in September.

A container here is a unit of database organization and allocated throughput, rather than a folder belonging to a user. Different workloads can compete for physical resources beneath their logical boundaries. A tidy separation in an interface therefore does not guarantee that a heavy background operation cannot affect an interactive request. That is the noisy-neighbor problem in this account: contention for capacity, rather than a claim that users' documents are mixed together.

Separate containers reduced the potential scope of failures but introduced another bill. Product teams had to plan their own requirements, and the growth of a new feature no longer disappeared into the aggregate load. Keeping enough spare capacity for an unexpected surge and avoiding excessive reservations are different objectives. The account is useful because it does not treat isolation as a universal answer. The organizational work required to maintain it also shapes operational reliability.

According to the engineers, the move back to sharing involved throttling the hottest keys and assigning requests different priorities. Background processing can be slowed before operations that a person is actively waiting for. A shared database then becomes a managed allocation among demands of differing urgency, rather than a promise of identical performance regardless of neighboring behavior. Moving data between placements remains a separate capability of the platform rather than something this arrangement makes unnecessary.

The authors also examine read latency. Locating data nearby, caching and reducing service overhead work together; crediting the result entirely to a programming-language change would miss that combination. Cache updates are tied to a feed of database changes. It is helpful to distinguish a nearby cached object from a request that still needs the underlying store. Improving the typical path does not make every request equally fast or eliminate the consequences of distance.

### Why it matters

The account describes decisions that sit behind an AI application's visible answer. It comes from the system's operators and is not an independent comparison of cloud databases. Its value is in the tradeoffs: who owns capacity planning, which work gets priority and how overload is handled. For another organization, those questions are more transferable than a database brand or an architecture built for a different scale. Product usability depends on this ordinary infrastructure work as well as on the model generating a response.
