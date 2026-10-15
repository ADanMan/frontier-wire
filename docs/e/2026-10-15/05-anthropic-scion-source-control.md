---
date: 2026-10-15
rubric: tech
title_ru: "Anthropic рассказала о Scion: серверном контроле версий для потока изменений от агентов"
title_en: "Anthropic details Scion, server-based version control for agent-scale changes"
dek_ru: "Внутренний переход с Git иллюстрирует особую нагрузку компании; универсальную замену Git она не предлагает."
dek_en: "The internal migration addresses an unusual workload; the company is not proposing a general Git replacement."
source: https://www.anthropic.com/engineering/redesigning-source-control
generated: true
---

## Русская версия

Anthropic в [инженерном отчёте от 13 октября](https://www.anthropic.com/engineering/redesigning-source-control) описала переход своего монорепозитория с Git на внутреннюю систему Scion. Компания сообщает, что число ежедневных слияний выросло с примерно 2500 в мае до более 30 тысяч в сентябре. Новый подход рассчитан на постоянно подключённых клиентов: значительная часть работы с историей и изменениями выполняется на сервере. Авторы подчёркивают, что их решение не является универсальной заменой Git.

Здесь важно правильно выбрать предмет сравнения. Речь идёт о том, как обслужить специфический поток операций внутри одной организации. Из количества слияний нельзя напрямую вывести качество продукта, полезность каждой правки или производительность отдельного разработчика. Это счётчик нагрузки, который помогает объяснить архитектурное решение, а не самостоятельная оценка успеха разработки.

Можно представить две библиотеки. В одной каждый посетитель уносит полный каталог и умеет работать с ним без связи. В другой посетитель отправляет вопросы центральной службе и получает только нужные ответы. Второй вариант способен сократить повторную работу, но делает доступность службы частью рабочего процесса. Аналогия упрощает устройство систем, зато помогает увидеть, что экономия и зависимость возникают одновременно.

Для инженерной команды главный вопрос поэтому звучит не «почему мы ещё не заменили Git». Сначала нужно понять, где действительно тратится время: на получение файлов, вычисление истории, ожидание проверки или что-то ещё. Имеет смысл измерить узкое место, прежде чем выбирать средство. Иначе крупная миграция рискует устранить проблему, которой в конкретном проекте почти нет.

Есть и вопрос переносимости опыта. У небольшой команды может оказаться совсем другая цена потери автономной работы, стоимость обслуживания центральной службы и частота запросов. Даже убедительное улучшение внутри одного монорепозитория не доказывает выгодность той же конструкции в другом. Полезно заимствовать постановку задачи и критерии измерения, не копируя организацию целиком.

Для читателя особенно интересна граница между автоматизацией написания кода и автоматизацией всей разработки. Если одна стадия ускоряется, остаётся проверить, выдерживают ли остальные: получение исходников, обсуждение изменений, тестирование, выпуск. Это аналитический вывод из описанного случая, а не обещание неизбежной перестройки каждой компании.

### Почему это важно

Scion делает видимой инфраструктурную сторону агентного программирования. Новость полезна как конкретный опыт с явно необычной нагрузкой. Применимый урок — следить за полным путём изменения и выбирать архитектуру по измеренным ограничениям, сохраняя различие между чужим внутренним результатом и доказанной выгодой для собственного проекта.

## English version

In an [engineering report dated October 13](https://www.anthropic.com/engineering/redesigning-source-control), Anthropic describes moving its monorepo from Git to an internal system called Scion. The company reports an increase from roughly 2,500 daily merges in May to more than 30,000 in September. Its design assumes clients remain online, with substantial history and change operations handled by servers. The authors explicitly reject presenting it as a general replacement for Git.

The subject of comparison matters. This is an account of serving a particular stream of operations inside one organization. Merge counts cannot directly establish product quality, the usefulness of each change, or an individual engineer's productivity. They are workload measurements that help explain an architectural decision, rather than an independent assessment of software development success.

Imagine two libraries. At one, every visitor carries away a complete catalogue and can consult it without a connection. At the other, visitors send questions to a central service and receive only the answers they need. The second arrangement could reduce repeated work, while making the availability of that service part of the process. The analogy simplifies the systems but illustrates how savings and dependence can arrive together.

For another engineering team, the useful question is therefore not why it has yet to replace Git. First it needs to identify where time actually goes: obtaining files, calculating history, waiting for a check, or something else. Measuring the constraint should come before selecting a remedy. Otherwise, a major migration could eliminate a problem that barely exists in that particular project.

Transferring the experience also requires care. A smaller team might face a very different cost for losing offline work, operating a central service, or handling repeated requests. A convincing improvement inside one monorepo does not demonstrate that the same arrangement is economical elsewhere. Borrowing the problem statement and measurement criteria may be more useful than copying the organization around them.

For readers, the case highlights a boundary between automating code production and automating development as a whole. When one stage becomes faster, the remaining stages still need examination: retrieving source, discussing changes, testing and delivery. That is an analytical implication of this case, rather than a prediction that every company must rebuild its infrastructure.

### Why it matters

Scion makes the infrastructure side of agentic programming visible. It is useful as a specific account of an explicitly unusual workload. The transferable lesson is to examine the entire path of a change and choose architecture around measured constraints, while keeping another company's internal result separate from demonstrated benefits for one's own project.
