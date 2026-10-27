---
date: 2026-10-27
rubric: ai
title_ru: IBM объединяет четыре модели Granite для прогнозирования временных рядов
title_en: IBM combines four Granite models for time-series forecasting
dek_ru: Рецепт без дообучения сокращает выбор между архитектурами, но не гарантирует лучший прогноз на каждом ряду.
dek_en: A recipe without retraining reduces architecture selection, but does not guarantee a better forecast on every series.
source: https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1
generated: true
---

## Русская версия

Предобученная модель временного ряда избавляет от части работы с обучением, но оставляет вопрос: какую архитектуру выбрать для ваших данных? В [разборе IBM Research от 22 октября](https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1) представлен ансамбль из четырёх моделей Granite. В сегодняшнем дайджесте это первое для нашего архива рассмотрение рецепта последних дней. Он объединяет прогнозы готовых моделей, а не превращает их веса в одну новую нейросеть и не требует подгонки весов ансамбля по тестовым ответам.

По умолчанию участники получают одинаковое влияние при объединении вероятностных прогнозов. На выходе доступны медиана и квантили — несколько уровней распределения возможных исходов. Практический смысл ансамбля в том, что ошибки разных архитектур не обязаны совпадать. Однако это аргумент в пользу проверки комбинации, а не доказательство, что любое добавление модели улучшит результат. Качество участников и их различия остаются существенными, даже если интерфейс объединения выглядит простым.

Предложен и альтернативный вариант IQR: больший вес получают модели с более узким прогнозным разбросом. Здесь авторы прямо отмечают ловушку — узкий интервал может означать самоуверенность, а не высокую точность. Система способна предпочесть такой прогноз именно потому, что он выглядит определённым. Поэтому выбор между равным влиянием и адаптивным взвешиванием следует делать по наблюдаемой работе на подходящих данных, а не по внешней привлекательности более узкого диапазона.

В сравнении на 97 конфигурациях GIFT-Eval оба ансамбля улучшили агрегированную ошибку точечного прогноза MASE относительно отдельных участников. Но преимущество над лучшей одиночной моделью невелико: 0,683 против 0,685 у варианта по умолчанию. При этом лучшая агрегированная вероятностная метрика осталась за отдельной PatchTST-FM-r2. Это результаты разработчиков на срезе таблицы от 20 октября, а не независимый тест редакции или универсальное первое место среди всех возможных систем.

Удобство имеет цену: нужно загрузить четыре набора весов, что увеличивает время и потребление памяти по сравнению с одним участником. Каналы многомерного ряда в текущем рецепте прогнозируются независимо, без использования связей между ними. Номинальный интервал между квантилями 0,1 и 0,9 также ещё не доказывает фактическое покрытие восьмидесяти процентов будущих значений. Такое покрытие нужно измерять, особенно когда распределение данных меняется после внедрения.

### Почему это важно

Ансамбль предлагает разумную стартовую гипотезу для случая, когда заранее неизвестно, какая архитектура подойдёт лучше. Его ценность легче оценить сравнением на одинаковых исторических окнах с сильной одиночной моделью. Ошибка центрального прогноза, качество интервалов и затраты ресурсов — отдельные характеристики. Простая комбинация может быть удобна, но удобство выбора не отменяет проверки того, насколько прогноз помогает именно вашей задаче и какие ошибки для неё наиболее существенны.

## English version

A pretrained time-series model removes some training work but leaves a choice: which architecture fits the data? An [IBM Research explanation published October 22](https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1) presents an ensemble of four Granite models. Today's digest brings the recipe its first coverage in our archive. It combines forecasts from existing members rather than merging their weights into one new neural network, and the aggregation does not require fitting ensemble weights to test answers or retraining the participating models.

The default recipe gives members equal influence when pooling probabilistic forecasts. Outputs include the median and quantiles, representing different levels of the predicted distribution. The rationale is that errors from different architectures need not coincide. That supports testing a combination, rather than proving that adding any model must improve a forecast. Member quality and diversity still matter even when the interface makes combining their predictions appear straightforward and hides much of the configuration from the downstream application.

An alternative IQR recipe gives more influence to forecasts with a narrower spread. The authors explicitly identify a trap: a narrow interval can reflect overconfidence rather than accuracy. A system may favor that forecast precisely because it appears more certain. Choosing between equal influence and adaptive weighting therefore requires observed performance on representative data. The visual appeal of a tighter range does not establish that the range is well calibrated or that it will contain the outcomes people actually observe.

Across 97 GIFT-Eval configurations, both ensembles improved aggregate point-forecast MASE relative to their individual members. The default recipe's margin over the strongest single member was small: 0.683 against 0.685. Meanwhile, the best aggregate probabilistic score remained with the individual PatchTST-FM-r2 model. These are developer-reported comparisons using an October 20 leaderboard snapshot, rather than an independent Frontier Wire test or a universal first-place ranking among every forecasting system that could be considered.

Convenience has a resource cost. The recipe loads four checkpoints, increasing inference time and memory relative to a single member. In the current implementation, channels of a multivariate series are forecast independently, without cross-channel information. An interval between the 0.1 and 0.9 quantiles also does not establish actual eighty-percent coverage of future observations. That coverage needs to be measured, particularly when the data distribution changes after deployment and previously useful uncertainty estimates may cease to match reality.

### Why it matters

The ensemble provides a reasonable starting hypothesis when the best architecture is unknown in advance. Its value is easier to judge against a strong individual model on identical historical forecast windows. Central-prediction error, interval quality and resource requirements are separate properties. A simple combination can make model selection more convenient, while leaving the essential task intact: checking whether its forecasts help with the specific decisions being made and which kinds of error matter most in that setting.
