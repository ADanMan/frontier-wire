---
date: 2026-10-19
rubric: tech
title_ru: "Два обновления LLM затронули зависимости плагина Datasette и отладочный подсчёт токенов"
title_en: "Two LLM updates address a Datasette dependency and simulated token accounting"
dek_ru: "Исправление llm-tools-datasette и релиз llm-echo решают разные задачи совместимости и диагностики."
dek_en: "The llm-tools-datasette fix and llm-echo release address separate compatibility and debugging tasks."
source: https://simonwillison.net/2026/Oct/18/llm-tools-datasette/
generated: true
---

## Русская версия

Саймон Уиллисон 18 октября выпустил два небольших обновления вокруг своей программы LLM. В [llm-tools-datasette 0.1.1](https://simonwillison.net/2026/Oct/18/llm-tools-datasette/) исправлена зависимость: переход основной программы на httpx2 оставил без нужного пакета плагины, которые использовали httpx, но не объявляли его самостоятельно. Автор прямо называет Datasette одним из затронутых плагинов.

Второй релиз, [llm-echo 0.5](https://simonwillison.net/2026/Oct/18/llm-echo/), касается отладки. Этот плагин предоставляет имитацию модели: она возвращает переданный запрос, не обращаясь к настоящей языковой модели. Обновление учитывает в симулированном использовании токенов вызовы инструментов, системные запросы и токены рассуждения. Слово «симулированном» здесь принципиально: речь не о проверке реального счёта какого-либо облачного провайдера.

Оба изменения напоминают, что работа инструмента складывается из нескольких контрактов. Плагин может правильно формировать запрос и при этом не запускаться из-за отсутствующей зависимости. Отладочная модель может возвращать ожидаемый текст, но не воспроизводить часть служебных показателей. Внешне похожая неисправность поэтому способна находиться на разных уровнях системы.

У проблемы с зависимостью есть понятная механика. Если приложение случайно обеспечивает наличие пакета, расширение может работать до тех пор, пока приложение не меняет собственный набор библиотек. Сам факт вчерашнего успешного запуска не означает, что расширение описало все свои требования. Этот случай показывает, почему совместимость зависит не только от публичного интерфейса, но и от того, какие условия объявлены явно.

Для воспроизводимой диагностики также полезно записать версии основной программы и расширения, состав окружения и точный способ запуска: тогда исправление можно проверить повторно в сопоставимых условиях. Отладочный двойник решает другую задачу: позволяет отделить обработку запроса от качества ответа живой модели. Например, разработчик может проверить, что нужный системный текст и параметры вообще дошли до следующего слоя. Это редакционный пример применения, а не наш запуск обновления. Такая проверка полезна именно потому, что не требует одновременно объяснять поведение модели и программы вокруг неё.

Однако имитация не превращается в полноценное измерение всех свойств настоящего сервиса. Она может помочь проверить путь данных и вывод статистики, но сама по себе не подтверждает точность ответа, задержку или стоимость у другого поставщика. Для каждого из этих свойств нужен соответствующий источник измерения.

### Почему это важно

Небольшие релизы делают видимыми части инфраструктуры, которые легко пропустить за обсуждением моделей. Здесь конкретно исправлены установка зависимости и полнота отладочной имитации. Полезный вывод — проверять совместимость и диагностику отдельно, чтобы сбой одного слоя не принимать за недостаток другого.

## English version

Simon Willison published two small updates around his LLM application on October 18. [llm-tools-datasette 0.1.1](https://simonwillison.net/2026/Oct/18/llm-tools-datasette/) fixes a dependency issue: moving the main application to httpx2 affected plugins that used httpx without declaring their own dependency. The author identifies the Datasette plugin as one affected example.

The second release, [llm-echo 0.5](https://simonwillison.net/2026/Oct/18/llm-echo/), concerns debugging. It provides a stand-in model that repeats a supplied prompt without calling an actual language model. Its updated simulated token usage accounts for tool calls, system prompts and reasoning tokens. “Simulated” matters: this is not verification of a real cloud provider's bill.

Together, the changes illustrate several different contracts within a tool. A plugin might construct a request correctly but fail to start because a dependency is missing. A debugging model might return the expected text while omitting part of the supporting statistics. Failures that appear similar from outside can therefore arise at different layers.

The dependency mechanism is straightforward. If an application happens to provide a library, an extension may keep working until the application's own package choices change. A successful run yesterday does not establish that the extension declared all its requirements. This case shows why compatibility depends on explicit conditions as well as on the visible interface.

For reproducible diagnosis, recording the application and extension versions, environment and invocation also helps make a later comparison meaningful. A debugging double addresses a different question: separating request handling from the quality of a live model's response. For example, a developer could inspect whether the intended system text and parameters reached the next layer at all. That is an editorial illustration, rather than our execution of the release. The check is useful precisely because it avoids having to explain model behaviour and surrounding software simultaneously.

The simulation nevertheless does not measure every property of a genuine service. It can help inspect the data path and presentation of usage information, without establishing response accuracy, latency or cost at another provider. Each of those properties requires an appropriate measurement source.

A disciplined investigation can therefore narrow the problem before changing the model. First establish whether the plugin loads and receives the expected input; then investigate what a real provider does with that input. The releases provide concrete fixes for parts of this process, rather than a universal assurance that every extension is compatible.

### Why it matters

Small releases expose infrastructure that is easy to overlook in discussions of models. Here, the concrete improvements concern dependency installation and the completeness of a debugging simulation. Checking compatibility and diagnostics separately helps avoid attributing a failure in one layer to the wrong component.
