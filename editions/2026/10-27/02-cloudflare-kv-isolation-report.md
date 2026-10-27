---
date: 2026-10-27
rubric: tech
title_ru: Cloudflare раскрыла исправленный сбой изоляции запросов GLM-5.3
title_en: Cloudflare discloses a repaired GLM-5.3 request-isolation failure
dek_ru: Компания сообщила о 155 затронутых ответах и объяснила, почему успешный HTTP-статус не подтверждал корректность обработки.
dek_en: The company reported 155 affected responses and explained why successful HTTP status did not establish correct processing.
source: https://blog.cloudflare.com/kv-cache-exposure-remediation/
generated: true
---

## Русская версия

Успешный код ответа сервера ещё не доказывает, что данные разных пользователей остались разделены. В [раскрытии от 26 октября Cloudflare](https://blog.cloudflare.com/kv-cache-exposure-remediation/) описала исправленный инцидент с моделью GLM-5.3 в Workers AI. По данным компании, с 27 августа по 9 сентября 155 ответов содержали данные из более ранних запросов других клиентов к той же модели. Это новая публикация о прежнем сбое, а не сообщение, что утечка впервые произошла сегодня.

Cloudflare связывает проблему с сочетанием конфигурации своей инфраструктуры и ошибки движка SGLang. Объявленное контекстное окно и фактическая ёмкость промежуточной памяти не были согласованы. Обработка запроса, который не помещался, должна была закончиться ошибкой, но в распределённой схеме завершалась некорректно. В результате генерация могла учитывать состояние, оставшееся от другой сессии. Здесь достаточно понимать нарушение владения памятью; техническая инструкция для воспроизведения читателю не нужна.

По отчёту, исследователь сообщил о проблеме 8 сентября. На следующий день компания воспроизвела её, ограничила доступ к модели, изменила конфигурацию и движок, затем восстановила сервис. Cloudflare утверждает, что другие размещённые в Workers AI модели этим конкретным инцидентом не затронуты. Эти границы важны: нельзя автоматически переносить вывод на любой сервис с GLM, на все модели платформы или на каждый вариант использования SGLang.

Компания также пишет, что не обнаружила свидетельств преднамеренной эксплуатации после исключения собственных проверок и действий исследователя. Это результат её расследования, а не доказательство математической невозможности незамеченного злоупотребления. Редакция не публикует содержимое чужих запросов, личности клиентов или собственные предположения о пострадавших. Число ответов тоже не следует подменять числом пользователей: это разные единицы учёта, и отчёт не даёт оснований считать их одинаковыми.

Самая полезная инженерная деталь касается испытаний. Перед запуском проверяли статусы HTTP и производительность длинных запросов, но этого оказалось недостаточно для проверки правильности ответа. После инцидента добавлены более прямые проверки конфигурации и обработчиков ошибок, а исправления согласованы с разработчиками SGLang. Более широкие способы контроля целостности памяти в отчёте частично остаются будущей работой. Их нельзя описывать как уже завершённую универсальную защиту от всех сходных ошибок.

### Почему это важно

Сервис может выглядеть работоспособным по внешним показателям и при этом нарушать более глубокое требование изоляции. Отчёт даёт конкретный пример разницы между доступностью, корректностью и конфиденциальностью. Для оценки инфраструктуры ИИ полезно спрашивать не только, вернулся ли ответ, но и как проверено происхождение состояния, из которого он получен. При этом нынешняя публикация остаётся отчётом оператора о расследовании и мерах, а не независимым аудитом всей платформы.

## English version

A successful server response does not establish that different users' data remained isolated. In an [October 26 disclosure, Cloudflare](https://blog.cloudflare.com/kv-cache-exposure-remediation/) described a repaired incident involving GLM-5.3 on Workers AI. The company reported that, between August 27 and September 9, 155 responses contained data from earlier requests by other customers using the same model. The new development is publication of the account, rather than a claim that the exposure first occurred today or remains active now.

Cloudflare attributes the problem to a combination of its infrastructure configuration and an SGLang inference-engine bug. The advertised context window and actual intermediate-memory capacity were not aligned. A request that could not fit should have produced an error, but the distributed processing path handled that outcome incorrectly. Generation could consequently use state left by another session. Understanding that failure of memory ownership is sufficient for this news account; reproducing the issue is not necessary to explain its significance.

According to the report, a researcher notified Cloudflare on September 8. The company reproduced the issue the following day, restricted access to the model, changed the configuration and engine, and restored service. Cloudflare says no other model hosted on Workers AI was affected by this particular incident. Those boundaries matter. The finding should not automatically be generalized to every GLM service, every model on the platform or every possible SGLang deployment, whose configurations and processing paths may differ.

The company also says it found no evidence of deliberate exploitation after excluding its own testing and the researcher's activity. That is a conclusion from its investigation, rather than proof that unobserved misuse was mathematically impossible. Frontier Wire is not reproducing other customers' request contents or speculating about affected identities. The reported response count should not become a user count either. They are different units, and the account does not establish that the two numbers are interchangeable.

The most useful engineering lesson concerns testing. Before launch, successful HTTP statuses and long-request performance had been checked, but those signals did not establish correct output. The response includes more direct configuration and error-path checks, alongside fixes coordinated with SGLang maintainers. Some broader memory-integrity measures described in the report remain future work. They should not be presented as an already completed, universal defense against every related failure that might arise in a distributed inference system.

### Why it matters

A service can appear healthy in external metrics while violating a deeper isolation requirement. The account provides a concrete distinction between availability, correctness and confidentiality. Evaluating AI infrastructure means asking not only whether a response arrived but how the provenance of the state behind it was checked. The disclosure remains the operator's account of an investigation and remediation, rather than an independent audit establishing the security of the entire platform under all conditions.
