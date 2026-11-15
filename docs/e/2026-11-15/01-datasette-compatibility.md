---
date: 2026-11-15
rubric: tech
title_ru: Datasette обновляет подключение моделей и старый плагин графиков
title_en: Datasette updates model connections and a longstanding chart plugin
dek_ru: Два релиза от 14 ноября расширяют совместимость на разных участках работы с данными.
dek_en: Two November 14 releases improve compatibility at different stages of working with data.
source: https://simonwillison.net/2026/Nov/14/datasette-llm/
generated: true
---

## Русская версия

Два небольших обновления Datasette попали в сегодняшний digest. В [заметке о datasette-llm 0.1a11](https://simonwillison.net/2026/Nov/14/datasette-llm/) от 14 ноября Саймон Уиллисон сообщает о поддержке OpenAI-совместимых адресов API. В отдельной [заметке о datasette-vega 0.7](https://simonwillison.net/2026/Nov/14/datasette-vega/) он описывает возвращение совместимости плагина графиков с последними альфа-версиями Datasette. Это новости автора проекта, а не результаты независимого тестирования редакции. Дата подборки — 15 ноября; даты самих сообщений мы сохраняем, не выдавая вчерашние релизы за сегодняшние объявления.

У двух плагинов разные задачи. Datasette-llm служит промежуточным слоем настройки языковых моделей для других плагинов. Новая поддержка относится к способу обращения к модели через совместимый интерфейс. В сообщении приведён пример запуска Datasette Agent с локальной моделью и перечислены LM Studio, Ollama и llama.cpp. Из этого не следует, что любая модель одинаково хорошо справится с любым запросом: доступность соединения и качество ответа остаются разными вопросами.

Datasette-vega отвечает за другой участок работы: визуализацию данных таблицы или пользовательского запроса через Vega-Lite. По словам Уиллиссона, предыдущий релиз вышел в июле 2018 года. Нынешнее обновление добавляет совместимость с актуальными альфа-версиями Datasette и косметические изменения для Datasette Lite. Автор также сообщает, что Lite теперь умеет запускать подобные JavaScript-плагины, и ведёт на демонстрацию из README. Мы прочитали сообщения полностью, но эту демонстрацию и локальный запуск не проверяли.

Практический смысл можно объяснить на условной рабочей задаче. Есть таблица, которую нужно изучить, а затем показать результат коллеге. Подключение модели помогает организовать один способ взаимодействия с данными, график — другой. Однако красивое представление не подтверждает корректность выбранных строк. Если пользователь попросил сравнить периоды, сначала стоит понять, какие записи попали в каждый период, и лишь затем интерпретировать получившуюся картинку. Это редакционный пример, а не заявленная новая функция этих релизов.

Так же следует читать слово «совместимость». Оно указывает на конкретную границу между компонентами, а не обещает отсутствие различий во всех остальных частях системы. Для собственного проекта полезно отдельно проверить выбранный сервер модели, запрос к данным и итоговое представление. Небольшой проверяемый пример даст больше оснований для решения об обновлении, чем один удачный снимок экрана. В этих заметках нет сравнительного измерения точности моделей или скорости построения диаграмм, поэтому таких выводов мы не делаем.

### Почему это важно

Поддержка привычных интерфейсов и обновление старых расширений способны вернуть пользу уже существующим инструментам. Эти два релиза показывают разные стороны такой работы: выбор места запуска модели и сохранение доступа к визуализации. Пользователю остаётся проверять весь путь от исходной таблицы до объяснения результата, сохраняя возможность разобраться в нём без доверия к одной только убедительной форме.

## English version

Two small Datasette updates enter today's digest. In his [datasette-llm 0.1a11 release note](https://simonwillison.net/2026/Nov/14/datasette-llm/) dated November 14, Simon Willison announces support for OpenAI-compatible API endpoints. A separate [datasette-vega 0.7 note](https://simonwillison.net/2026/Nov/14/datasette-vega/) describes restoring the charting plugin's compatibility with recent Datasette alphas. These are the project's own announcements, rather than independently tested results. This edition is dated November 15; both source dates remain explicit instead of turning yesterday's releases into announcements supposedly made today.

The plugins perform different jobs. Datasette-llm provides an intermediate configuration layer for language models used by other Datasette plugins. The addition concerns how software reaches a model through a compatible interface. Willison supplies an example running Datasette Agent against a local model and names LM Studio, Ollama and llama.cpp. That does not establish that every reachable model will perform equally well on every task. Connecting successfully and producing a correct answer are separate questions.

Datasette-vega handles another part of the workflow: charts built with Vega-Lite from table data or a custom query. Willison says its previous release was in July 2018. The update brings compatibility with current Datasette alphas and cosmetic adjustments for Datasette Lite. He also reports that Lite can now run JavaScript plugins of this kind, with the README's live demonstration pointing to a Lite example. We read both release notes in full but did not independently run the demonstration or local setup.

Consider a hypothetical assignment: explore a table and explain the result to a colleague. A model connection provides one way of interacting with data, while a chart provides another. Neither a fluent explanation nor a polished visual establishes that the right records were selected. If the assignment compares periods, understanding which rows belong to each period comes before interpreting the picture. This is an editorial illustration of the workflow, not a claim that either release introduces a particular analytical feature.

Compatibility also needs a precise reading. It describes a boundary between components, rather than promising identical behaviour throughout an application. Someone evaluating an upgrade can separately check the chosen model server, the data query and the final presentation. A small, inspectable example offers stronger grounds for that decision than a persuasive screenshot alone. Neither announcement provides a comparative measurement of model accuracy or chart performance, so we draw no such conclusions from them.

### Why it matters

Maintaining familiar interfaces and older extensions can make existing tools useful again. These releases address different pieces of that effort: choosing where a model runs and keeping a visualisation route available. Users still need an understandable path from the original table to the explanation, with enough evidence to inspect the result rather than trusting its presentation alone.
