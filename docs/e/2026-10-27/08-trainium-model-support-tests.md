---
date: 2026-10-27
rubric: tech
title_ru: Таблица Trainium показывает, какие модели прошли конкретный короткий тест
title_en: A Trainium support table shows which models passed a specific short test
dek_ru: Hugging Face публикует версии стека, скрипты и результаты; статус PASS не измеряет скорость и длинные генерации.
dek_en: Hugging Face publishes stack versions, scripts and outcomes, while PASS does not measure throughput or long generations.
source: https://huggingface.co/blog/torch-neuronx-model-support
generated: true
---

## Русская версия

После анонса нового backend возникает практический вопрос: какие модели действительно удалось запустить в проверенной конфигурации? В [материале Hugging Face от 23 октября](https://huggingface.co/blog/torch-neuronx-model-support) описана публичная таблица совместимости Transformers с AWS Trainium через torch-neuronx. Это продолжение истории TorchNeuron, о которой Frontier Wire писал 20 октября. Новое здесь — результаты конкретных запусков, их версии и воспроизводимые скрипты, а не повторное объявление самого вычислительного backend.

В интерфейсе можно искать модель и выбирать версии компилятора Neuron и библиотеки Transformers. Строка показывает исход проверки, число ядер, время запуска с учётом компиляции и пиковое потребление памяти устройства. Наличие модели в популярных списках не означает, что её обязательно проверили. Для пропущенных позиций может быть указана причина: недостаточный приоритет и реальная несовместимость — разные ситуации. Поэтому пустое место или отсутствие успешного результата нельзя читать как один универсальный диагноз.

Тест на момент публикации ограничен моделями Transformers для генерации текста и преобразования изображения с текстом в текст. Проверяются варианты, помещающиеся на четырёх устройствах Trainium2, максимум шестнадцати ядрах. Другие задачи и библиотеки обозначены как планы расширения. Такая граница важна: имя общей платформы не превращает выборку испытанных конфигураций в полный каталог возможностей любого ускорителя или любой модели, которую можно найти в Hub. Список имеет заявленную область покрытия.

Сам запуск генерирует тридцать два токена и проверяет результат. На одном ядре токены сравниваются с выполнением того же checkpoint на CPU. При распределённом запуске небольшая модель-судья оценивает связность английского текста. Эти два критерия не одинаковы: проверка связности не доказывает полное численное совпадение и не измеряет качество решения произвольной пользовательской задачи. Авторы отдельно говорят, что PASS ничего не утверждает о пропускной способности или длинных продолжениях.

Результаты хранятся в публичном наборе данных вместе с ошибками, версиями компонентов и использованным скриптом. Это позволяет изучать конкретную конфигурацию, а не полагаться на устное обещание поддержки. Время первого запуска включает компиляцию, поэтому его также нельзя напрямую выдавать за скорость обычного запроса после прогрева. Редакция читала описание методики, но не арендовала Trainium, не запускала модели и не воспроизводила опубликованные строки независимо на собственном оборудовании.

### Почему это важно

Таблица полезна как проверяемая отправная точка перед переносом нагрузки. Она уточняет, что именно запускали и по какому признаку сочли результат успешным. Для практического решения останутся отдельные вопросы: нужная длина контекста, корректность на своих данных, скорость и стоимость. Хороший каталог совместимости помогает поставить эти проверки точнее, но не заменяет их словом PASS и не обещает одинакового поведения после смены версии стека.

## English version

A backend announcement leaves a practical question: which models have actually run in a tested configuration? A [Hugging Face article published October 23](https://huggingface.co/blog/torch-neuronx-model-support) describes a public support table for Transformers models on AWS Trainium through torch-neuronx. This follows the TorchNeuron introduction Frontier Wire covered on October 20. The new development is a collection of specific outcomes, versions and reproducible scripts, rather than another announcement of the backend itself or an assumption that every Hub model already works.

The interface lets readers search for a model and choose Neuron compiler and Transformers versions. Each row reports the outcome, core count, wall time including compilation and peak device memory. Appearing in a popularity ranking does not establish that a model has been tested. Omitted entries can have different reasons, including lack of prioritization or actual incompatibility. An absent result should therefore not be interpreted as one universal failure diagnosis, especially without checking the explanation and the version combination being displayed.

At publication, coverage is limited to Transformers text-generation and image-text-to-text models. Tested configurations fit on four Trainium2 devices, or at most sixteen cores. Other tasks and libraries are described as possible extensions. Those boundaries matter: a platform's general name does not turn a selected set of runs into an exhaustive catalogue of every accelerator configuration or model available on the Hub. The table has an explicit coverage area that readers need to preserve when discussing what its results imply.

The test generates thirty-two tokens and checks them. On a single core, tokens are compared with a CPU execution of the same checkpoint. For sharded models, a small judge model checks whether the text is fluent English. These are different criteria. Fluency does not demonstrate complete numerical agreement, and neither procedure establishes performance on every user task. The authors explicitly state that PASS makes no claim about throughput or longer generations, even if the short demonstration produces readable output.

Results are stored in a public dataset together with errors, component versions and the script used. That makes a particular configuration inspectable instead of leaving support as an informal promise. First-run wall time includes compilation, so it should not be presented directly as the speed of an ordinary request after warm-up. Frontier Wire has read the methodology account but has not rented Trainium hardware, run the models or independently reproduced the published rows on its own infrastructure.

### Why it matters

The table offers an evidence-based starting point before moving a workload. It identifies what was run and which criterion defined success. Actual deployment still raises separate questions about required context length, correctness on relevant data, speed and cost. A useful compatibility catalogue makes those tests more specific without replacing them with a PASS label or promising unchanged behavior after a different stack version is selected for a future run.
