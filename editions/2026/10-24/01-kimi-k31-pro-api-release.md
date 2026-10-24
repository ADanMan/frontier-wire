---
date: 2026-10-24
rubric: ai
title_ru: "Kimi K3.1 Pro появился в сервисах Moonshot; публикация весов обещана к 4 ноября"
title_en: "Kimi K3.1 Pro reaches Moonshot services, with weights promised by November 4"
dek_ru: "Анонс разделяет доступ через сервис и будущий выпуск весов; результаты тестов остаются заявлениями разработчика."
dek_en: "The announcement separates service access from a future weight release, with benchmark results attributed to the developer."
source: https://www.kimi.ai/blog/kimi-k3-1-pro
generated: true
---

## Русская версия

Moonshot [представила Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro), первую модель новой серии K3.1, с заявленным окном контекста в миллион токенов. Анонс 23 октября сообщает о доступности в продуктах Kimi и через API. Одновременно компания обещает опубликовать полные веса к 4 ноября 2026 года. Это два разных этапа: пользоваться удалённым сервисом можно раньше, чем получить модель для собственного запуска.

Основой стала Kimi K3 после дополнительного обучения. Разработчик описывает увеличение вычислительных затрат на этот этап и совместную работу над обучающими средами, длинным контекстом и инфраструктурой экспериментов. Среди заявленных направлений улучшения — программирование, создание трёхмерных объектов и многошаговая работа с документами. Такая формулировка описывает цели и оценки команды, а не независимо установленное превосходство в каждой из этих областей.

Отдельно представлена версия Highspeed. Moonshot заявляет для неё скорость в два–три раза выше обычной K3.1 Pro. Это характеристика из анонса, без нашего собственного измерения задержки. При оценке подобного предложения важно заранее определить, что именно считать скоростью: ожидание первого ответа, генерацию текста или завершение всей задачи с инструментами. Один множитель без такого контекста не отвечает на все эти вопросы.

В технических материалах есть и проверяемые детали методики. Например, для Terminal-Bench 4.0 компания приводит результат 65,7 процента и указывает использование оболочки Claude Code. Для большинства оценок по умолчанию выбран максимальный уровень рассуждений. Сравнения с другими системами местами используют опубликованные ими результаты. Поэтому таблицу нельзя автоматически читать как один полностью одинаковый эксперимент над всеми участниками.

Демонстрации трёхмерного моделирования и программирования показывают возможный рабочий процесс с инструментами. Они полезны как примеры того, какой результат предлагает проверить разработчик, но не сообщают частоту успешного завершения любых пользовательских проектов. Аналогично большой контекст задаёт вместимость входа, а не гарантию безошибочного использования каждого документа на всей его длине. Это граница нашего прочтения характеристик, не новый тест модели.

Каналы доступа перечислены раздельно: веб-продукт, приложения, Kimi Work, Kimi Code и API. Для корпоративной среды администратор должен отдельно включить новую модель; в анонсе указано, что первоначально доступ выключен. Обещание весов также следует проверять по факту будущей публикации и её условиям. Мы не запускали платные запросы, не скачивали модель и не подтверждаем её производительность собственным бенчмарком.

### Почему это важно

Новая модель расширяет выбор сервисов для сложных задач, но доступность, открытость и качество измеряются по-разному. Полезная точка отсчёта здесь — доступный сервис сегодня, документированная процедура тестирования и отдельно назначенный срок публикации весов. Эти различия помогают оценивать релиз без преждевременного объявления уже состоявшейся открытой поставки.

## English version

Moonshot has [introduced Kimi K3.1 Pro](https://www.kimi.ai/blog/kimi-k3-1-pro), the first model in its K3.1 series, with a stated one-million-token context window. The October 23 announcement says it is available in Kimi products and through the API. Full model weights are promised by November 4, 2026. Those are separate milestones: access to a hosted service can precede a model's availability for self-hosting.

K3.1 Pro builds on Kimi K3 through additional post-training. The developer describes increased compute for that stage alongside work on training environments, long-context inference and experimentation infrastructure. Coding, three-dimensional creation and multi-step document work are among the reported areas of improvement. These are the team's claims and assessments, rather than independently established superiority in every domain.

A separate Highspeed version is also announced. Moonshot says it runs two to three times faster than standard K3.1 Pro. We have not measured that claim. Assessing such a figure requires deciding what speed means: time to the first response, text generation rate, or completion time for an entire tool-assisted task. One multiplier cannot answer all those questions without further context.

The technical material provides useful methodological details. For Terminal-Bench 4.0, Moonshot reports 65.7% using the Claude Code harness. Most evaluations default to maximum reasoning effort. Some comparisons draw competing systems' scores from their published reports. The resulting table should therefore not automatically be interpreted as one identically configured experiment across every participant.

The coding and 3D demonstrations illustrate potential workflows involving tools. They provide examples of outcomes that readers can investigate, rather than an observed success rate for arbitrary user projects. Likewise, a large context window specifies input capacity, not error-free use of every document throughout that window. This is a boundary on our interpretation of the specifications, not an additional model evaluation.

Access channels are listed separately: the web product, apps, Kimi Work, Kimi Code and API. Enterprise administrators must enable the model, with access initially switched off according to the announcement. The promised weights should also be assessed when they are actually published and their terms can be examined. We have not made paid API calls, downloaded the model or independently benchmarked it.

### Why it matters

The release adds another service for complex tasks, while availability, openness and quality remain separate questions. The useful starting points are present hosted access, documented evaluation procedures and a distinct future date for the weights. Keeping those boundaries explicit avoids presenting a promised open release as an already completed delivery.
