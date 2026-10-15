---
date: 2026-10-15
rubric: ai
title_ru: "Liquid AI выпустила LFM2.5-24B-A2B для локальных агентов"
title_en: "Liquid AI releases LFM2.5-24B-A2B for on-device agents"
dek_ru: "Компания показывает высокую скорость генерации, но её измерения не заменяют проверку полного рабочего сценария."
dek_en: "The company reports fast generation, but its measurements do not replace testing an entire workflow."
source: https://www.liquid.ai/blog/lfm2-5-24b-a2b
generated: true
---

## Русская версия

Liquid AI в [анонсе от 13 октября](https://www.liquid.ai/blog/lfm2-5-24b-a2b) представила LFM2.5-24B-A2B — модель с открытыми весами для локальных агентов. Компания сообщает о 24 миллиардах параметров, из которых при обработке токена активируется лишь часть, и показывает собственные измерения скорости. В таблице испытаний есть как преимущества на отдельных задачах работы с инструментами, так и отставание на других тестах. Единого доказательства превосходства над всеми соседними моделями анонс не даёт.

В [карточке модели](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) перечислены разные варианты поставки, включая GGUF и MLX, и контекст до 131 072 токенов. Там же указаны 2,45 миллиарда активных параметров: обозначение A2B в названии не следует принимать за точную характеристику памяти. Карточка описывает текстовую модель с поддержкой вызова инструментов; доступность весов не означает наличия готового помощника с подключёнными сервисами.

Для читателя здесь важнее не спор о самом большом числе в таблице, а различие между скоростью шага и временем выполнения задачи. Агент может быстро предложить следующий вызов и затем долго ждать внешнюю систему. Может написать короткий ответ после ошибочного поиска. Может сделать несколько лишних попыток. Измерение генерации само по себе не говорит, какой из этих сценариев получится у конкретного пользователя.

Поэтому полезный сравнительный эксперимент выглядел бы иначе: одинаковая задача, одинаковые инструменты, одинаковое ограничение времени и заранее определённый правильный результат. Следовало бы учитывать все попытки, а не только удачный прогон. Это редакционный критерий для чтения таких анонсов, а не заявление о проведённом нами независимом тестировании новинки.

Отдельного внимания требует слово «локальный». Оно отвечает на вопрос о месте вычисления модели. Но если построенный вокруг неё агент отправляет запрос к внешнему поиску или другой службе, нужно отдельно выяснять, что именно передаётся туда. Эти свойства не противоречат друг другу: локальное вычисление и сетевые инструменты могут сосуществовать. Просто обещание приватности нельзя вывести из одного лишь места хранения весов.

Разумно также разделять возможность разместить модель и удобство её повседневного использования. Для первого достаточно подходящего формата и ресурсов. Для второго нужны понятная обработка ошибок, контроль длительности и проверка результата. Ни один размер модели не отменяет этих вопросов; зато небольшая стоимость отдельного шага может сделать эксперименты с ними доступнее.

### Почему это важно

Релиз расширяет выбор основы для помощников на собственном оборудовании. Практический вывод стоит делать по завершённым задачам: насколько устойчив результат, сколько времени он занял и какие данные покидали устройство. Именно это превращает быстрые токены в полезный инструмент.

## English version

Liquid AI's [October 13 announcement](https://www.liquid.ai/blog/lfm2-5-24b-a2b) introduces LFM2.5-24B-A2B, an open-weight model aimed at on-device agents. The company reports 24 billion total parameters, with only a subset activated for each token, and publishes its own speed measurements. Its evaluation table contains both advantages on some tool-use tasks and weaker results elsewhere. It does not establish universal superiority over competing models.

The [model card](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) lists deployment formats including GGUF and MLX, alongside a context window of 131,072 tokens. It specifies 2.45 billion active parameters: the A2B label should not be mistaken for a precise memory requirement. This is a text model with tool-calling support, rather than a complete assistant with services already connected.

For a potential user, the important distinction is between the speed of one step and the time needed to finish a task. An agent might propose a tool call quickly and then wait for an external service. It might produce a short answer after a mistaken search, or make several unnecessary attempts. Generation speed alone cannot tell you which experience a particular workflow will deliver.

A useful comparison would hold the task, available tools, time limit and definition of success constant. It would count unsuccessful attempts as well as the most attractive run. That is an editorial criterion for interpreting announcements like this, rather than a claim that we independently tested the new model. Without such a comparison, a throughput number answers a narrower question than the user is likely to be asking.

The word “local” also needs a specific interpretation. It identifies where the model computation takes place. If an agent built around that model sends a query to search or another remote service, the information transmitted there needs separate examination. Local inference and network tools can coexist perfectly well; a privacy guarantee simply cannot be inferred from the location of the model weights alone.

It is helpful to distinguish being able to fit a model onto a device from finding it comfortable to use every day. The former requires a suitable format and enough resources. The latter requires clear error handling, time limits and a way to check the result. Model size does not remove those questions, although cheaper individual steps could make experimentation more accessible.

### Why it matters

The release adds another foundation for assistants running on users' own hardware. The practical judgment should concern completed work: whether the result is reliable, how long it took, and which information left the device. Those are the properties that turn rapid token generation into a useful tool.
