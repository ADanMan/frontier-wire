---
date: 2026-10-05
rubric: ai
title_ru: Агент сказал «готово» — ThinkingBox проверяет, что осталось в базе
title_en: The agent said done — ThinkingBox checks the database
dek_ru: Открытый стенд отделяет правильный вызов инструмента от правильного результата и повторяемой работы.
dek_en: An open benchmark separates valid tool calls from correct outcomes and repeatable execution.
source: https://huggingface.co/blog/microsoft/thinkingbox
generated: true
---

## Русская версия

В совместном [материале Microsoft и Hugging Face](https://huggingface.co/blog/microsoft/thinkingbox), опубликованном 3 октября, ThinkingBox представлен через простой вопрос: после работы агента нужные записи действительно изменились? Теперь стенд доступен через OpenEnv. Это новый способ пользоваться проектом, а не исследование, впервые появившееся сегодня.

Разница существенная. Представьте, что помощник отвечает на просьбу изменить бронирование. Убедительная фраза в чате ещё не показывает, какую запись он обновил и не затронул ли соседнюю. В такой задаче полезно проверять сохранённый результат независимо от рассказа исполнителя. Именно эту границу делает видимой подход ThinkingBox.

[Работа команды Чжочунь Ли](https://arxiv.org/html/2608.19741v4), обновлённая 1 октября, описывает 507 синтетических сценариев из пяти деловых областей. Каждый проверяется по конечному состоянию и побочным изменениям. Но у стенда есть важное ограничение: в 477 задачах сам финальный ответ не оценивается; ещё 30 добавляют требования к ответу. Следовательно, успешный результат теста не всегда означает, что пользователь получил точное объяснение. Авторы также не называют выборку репрезентативной для всей корпоративной работы.

В октябрьском блоге отдельно разведены три показателя: доля удачных попыток, хотя бы один успех за двадцать запусков и буквально двадцать успешных запусков из двадцати. Для читателя таблиц это полезнее одного большого процента. Если демонстрацию можно повторять до удачного дубля, она отвечает на другой вопрос, чем проверка того, что процесс стабильно проходит с первого раза. Эти числа нельзя подменять друг другом.

[README самого фреймворка](https://github.com/microsoft/thinkingbox) объясняет устройство изолированных сессий. Прокси запускает и инициализирует инструменты для отдельного разговора, передаёт их схемы агенту, собирает изменения для оценки, затем освобождает окружение. Набор сценариев вынесен в отдельный репозиторий. Поэтому скачать движок и получить полноценное испытание делового процесса — разные этапы; небольшой встроенный пример прежде всего помогает проверить установку.

[Документация адаптера OpenEnv](https://huggingface.co/docs/openenv/environments/thinkingbox) уточняет: нынешняя интеграция предназначена для оценки. Канонические результаты используют закреплённый выпуск данных; собственные сценарии не становятся автоматически результатами ThinkingBox-Bench. Серверу нужны внешние компоненты, включая прокси, MCP-сервисы и модельные endpoints. Один запущенный контейнер не подтверждает готовность всей цепочки.

### Почему это важно

Для команды, внедряющей агента, отсюда следует практический вопрос: где независимый критерий завершения вашей задачи? Наш вывод — сначала описать требуемые изменения и допустимые побочные эффекты, затем выбирать показатель надёжности. ThinkingBox даёт воспроизводимый пример такой проверки. Он не выдаёт универсальный сертификат безопасности и не заменяет испытания на собственном процессе, особенно если важны качество общения и поведение пользователей вне заданного сценария.

## English version

In a joint [Microsoft and Hugging Face post](https://huggingface.co/blog/microsoft/thinkingbox) published on October 3, ThinkingBox is introduced through a practical question: did the agent actually leave the required records behind? The benchmark is now accessible through OpenEnv. That is an extension of how people can use the project, rather than a study first released today.

Consider an assistant asked to change a booking. A confident completion message does not establish which record changed or whether another record was altered unnecessarily. A useful evaluation would inspect the persistent result independently of the assistant's account. This is the distinction that makes a stateful benchmark interesting: the output being judged includes what the software did.

The [paper by Zhuochun Li and colleagues](https://arxiv.org/html/2608.19741v4), revised on October 1, describes 507 synthetic workflows across five business domains. Every task checks terminal state and side effects. There is a significant boundary, however: 477 tasks do not grade the final response itself, while 30 add response requirements. A passing result therefore need not imply an accurate explanation to the user. The authors also caution that their task collection does not represent the distribution of all enterprise work.

The October blog distinguishes average success per attempt, at least one success across twenty attempts, and the literal count of tasks that passed twenty out of twenty times. These measures answer different questions. A demonstration selected after retries can establish that a successful path exists. It cannot, by itself, establish that an unattended process will repeatedly follow that path. Readers should keep those meanings separate when comparing leaderboard columns.

The [framework README](https://github.com/microsoft/thinkingbox) describes the session machinery. A proxy spawns and initializes tools for an isolated conversation, exposes tool schemas, collects effects for judging, and destroys the session afterward. The substantial scenarios and tool packages live in a separate data repository. Downloading the framework and running a meaningful business evaluation are therefore separate steps; its small bundled example mainly checks that an installation is wired together.

The [OpenEnv adapter documentation](https://huggingface.co/docs/openenv/environments/thinkingbox) adds another qualification: the current adapter is designed for evaluation. Canonical coverage uses a pinned benchmark release; custom scenarios do not automatically count as ThinkingBox-Bench results. The API server needs external services, including the session proxy, MCP servers and model endpoints. A running API container does not establish that the entire evaluation environment is ready.

### Why it matters

For an implementation team, the actionable question is where its independent completion criterion lives. Our reading is that teams should specify the required state changes and acceptable side effects before choosing a reliability metric. ThinkingBox offers a reproducible example of that approach. It is not a universal safety certificate or a substitute for testing a team's own workflow, especially when communication quality and users outside the simulator's prescribed behavior matter.
