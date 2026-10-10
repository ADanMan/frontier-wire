---
date: 2026-10-10
rubric: ai
title_ru: "Asana связала экономию браузерного агента со стабильностью истории — число 76× требует контекста"
title_en: "Asana links browser-agent savings to stable history, with qualifications around its 76× claim"
dek_ru: "Исследование одной задачи различает смену модели, настройку кэша, цену токенов и полноту конечного ответа."
dek_en: "A single-task study separates model changes, caching policy, token costs and the completeness of the final answer."
source: https://asana.com/inside-asana/cut-browsers-agent-cost
generated: true
---

## Русская версия

Asana 8 октября [опубликовала разбор оптимизации браузерного агента](https://asana.com/inside-asana/cut-browsers-agent-cost). Компания меняла работу с историей и кэшем: увеличила допустимый объём текста и стала удалять старые скриншоты группами, а не на каждом шаге. Так более длинные участки запроса оставались неизменными. Это отчёт разработчика о собственной системе, не независимый сравнительный тест всех агентов.

[Кейс OpenAI от 9 октября](https://openai.com/index/asana-browser-agent) выносит в заголовок снижение расчётной стоимости в 76 раз и ускорение примерно в пять раз. Сравнение относится к исходной настройке на анонимизированной Model B и оптимизированной на GPT-6.1 Sol. По тому же кейсу, настройка самой Model B дала снижение стоимости в 29 раз. Значит, большой множитель нельзя целиком приписать ни замене модели, ни одному переключателю кэширования.

В [техническом отчёте](https://assets.asana.biz/asset/fb86cc8e-6611-4404-b7c6-172692a724bb/How-Asana-used-Codex-to-optimize-browser-agent-costs-and-runtime.pdf) описаны 144 основных прогона задачи сбора сведений о 32 книгах. На каждую комбинацию приходилось обычно три прогона. Межмодельное сравнение автор называет описательным из-за различий протокола; стоимость вычислена по токенам, без серверов и песочниц. Есть и оговорка о качестве: увидеть нужные сведения не равно выдать запрошенную таблицу. Sol давал правильную общую сумму, но вместо полной таблицы возвращал краткое резюме.

Наш редакционный вывод: интереснее рекламного множителя здесь устройство сравнения. Если одновременно меняются программа, модель и настройки, итоговое число отвечает на вопрос о двух готовых конфигурациях. Для понимания причины нужны промежуточные сравнения. Иначе команда может повторить заметную часть изменений и не получить ожидаемого эффекта, потому что важной окажется другая часть.

Это удобно объяснить мысленным примером. Пусть обработка задания включает много повторений одинакового материала. Уменьшение цены одного повторения и уменьшение числа повторений дают разные виды экономии. Если сохранить оба эффекта в одном итоговом показателе, станет труднее решить, какое изменение проверять следующим. Поэтому полезно отдельно смотреть на цену шага, число шагов и завершение задачи.

Так же стоит определить успех до оптимизации. Правильная сумма, полный набор строк и соблюдение требуемого формата — три возможных условия, которые нельзя автоматически заменить друг другом. Дешёвый ответ можно сравнивать с дорогим только после явного решения, какие условия обязательны. Иначе низкая цена рискует описывать менее полный результат.

### Почему это важно

Отчёт предлагает проверяемую инженерную гипотезу о повторном использовании истории, а не гарантию многократной экономии для любого продукта. Практический вывод — измерять стоимость рядом с полнотой результата и указывать базу сравнения. Показатель на тестовой задаче не становится суммой экономии всей компании и не отменяет проверки на другом процессе.

## English version

Asana [published an analysis of browser-agent optimization](https://asana.com/inside-asana/cut-browsers-agent-cost) on October 8. It changed history and caching policies, allowing more text and removing older screenshots in batches rather than at every step. Longer portions of successive requests consequently remained unchanged. This is a developer's report about its own system, not an independent comparison of every browser agent.

An [OpenAI case study dated October 9](https://openai.com/index/asana-browser-agent) highlights 76-fold lower estimated costs and roughly fivefold faster runs. That comparison crosses from the original configuration on an anonymized Model B to an optimized configuration on GPT-6.1 Sol. The same case study says optimizing Model B itself reduced costs 29-fold. The larger multiplier therefore cannot be attributed entirely to changing the model or to one caching switch.

The [technical report](https://assets.asana.biz/asset/fb86cc8e-6611-4404-b7c6-172692a724bb/How-Asana-used-Codex-to-optimize-browser-agent-costs-and-runtime.pdf) describes 144 main runs collecting information about 32 books, generally three runs per condition. Its author calls cross-model comparisons descriptive because protocols differ. Token-based costs exclude servers and sandboxes. Quality has a qualification too: encountering the required facts is not identical to delivering the requested table. Sol returned correct price totals but a short summary instead of the full table.

Our editorial interest is the comparison's structure, rather than the promotional multiplier. When code, models and settings change together, the final number compares two complete configurations. Understanding causes requires intermediate comparisons. Otherwise, a team might repeat the most visible change without obtaining the expected effect, because another change contributed substantially to the result.

A hypothetical example makes the distinction easier to see. Suppose completing a task involves repeatedly processing the same material. Lowering the price of each repetition and reducing the number of repetitions produce different forms of savings. Combining both into one headline obscures which intervention deserves the next experiment. It is more informative to inspect the price per step, the number of steps and whether the task was completed as intended.

Success should also be defined before optimization. A correct total, a complete set of rows and compliance with the requested format can be three separate conditions. They cannot automatically stand in for one another. Comparing an inexpensive answer with an expensive one requires deciding which conditions are mandatory. Otherwise, the apparent bargain may represent a less complete output.

### Why it matters

The report offers a testable engineering hypothesis about reusing history, rather than a guarantee of large savings for any product. The useful lesson is to measure cost alongside output completeness and state the comparison baseline. A result on a development task is not a measure of company-wide savings, and it does not remove the need to check another workflow.
