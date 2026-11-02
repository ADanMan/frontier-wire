---
date: 2026-11-02
rubric: tech
title_ru: Кто принимает ИИ-код, если тесты написала та же система
title_en: Who accepts AI-written code when the same system wrote the tests?
dek_ru: Новое авторское эссе отделяет генерацию реализации от инженерного решения; разбираем эту границу на примере проверки поведения.
dek_en: A new opinion essay separates implementation generation from engineering acceptance; a worked example illustrates the boundary.
source: https://picon.dev/en/publications/ai-assisted-engineering/
generated: true
---

## Русская версия

Армандо Пикон 1 ноября опубликовал [эссе об инженерии с помощью ИИ](https://picon.dev/en/publications/ai-assisted-engineering/). Его тезис: делегирование реализации не отменяет ответственности за выбор задачи и принятие результата. Автор прямо обозначает текст как рабочую позицию, а не контролируемое исследование. Поэтому из него нельзя вывести процент экономии времени или вывод о замене профессии. Для нашей подборки это повод разобрать один практический вопрос: какое свидетельство позволяет принять изменение, если его автором был агент?

Рассмотрим собственный условный пример редакции, не описанный как внедрение у автора. В интернет-магазине меняется расчёт суммы корзины: бесплатная доставка должна появляться только после достижения порога. Агент предлагает исправление и тест, который проверяет покупку заметно выше этого порога. Тест проходит. Но он ещё не отвечает, что происходит ровно на границе, ниже неё и после удаления товара. Зелёный результат подтверждает выбранный пример, а не автоматически весь смысл требования.

Теперь допустим, что тест копирует формулу из реализации. Если в обеих местах допущена одинаковая ошибка сравнения, совпадение будет устойчивым и повторяемым. Это полезный мысленный контрпример к привычке считать повторяемость достаточным признаком правильности. Нужен независимый ожидаемый исход, выведенный из правила продукта. В нашем примере можно заранее составить таблицу небольшого числа граничных корзин и проверить точную стоимость доставки для каждой. Это рассуждение об устройстве проверки, а не отчёт о найденном дефекте реального магазина.

Есть и другая граница. Даже правильная формула не доказывает, что выбранное правило вообще соответствует намерению владельца продукта. Возможно, порог считают после скидки, а возможно — до неё. Если это не определено, дополнительные прогоны не устранят неоднозначность. Здесь требуется решение человека, имеющего право определить поведение. Его следует сделать видимым, чтобы следующий разработчик или агент не восстанавливал условие из догадок. Количество сгенерированных строк не отвечает на вопрос, было ли принято такое решение.

Из этих примеров следует различать три вида свидетельств. Проверка конкретных значений устанавливает поведение на выбранных входах. Просмотр изменения помогает понять, не затронуты ли посторонние части системы. Оценка через интерфейс показывает, как результат предъявлен пользователю. Ни один вид не подменяет остальные. Для изменения текста достаточно одного масштаба проверки; для расчёта денег нужен другой. Соразмерность здесь важнее максимального числа автоматических действий, если они всё равно проверяют одно и то же предположение.

### Почему это важно

Новость — появление ясно оговорённой инженерной позиции, а не новое доказательство роста производительности. Её полезно обсуждать через конкретные примеры принятия результата. Агент может ускорить получение реализации и помочь собрать свидетельства, но заявление об успехе само по себе не добавляет им покрытия. Важный вопрос для команды остаётся проверяемым: какой исход требовался, какие случаи действительно проверили и какие решения ещё нельзя вывести из полученных результатов? Именно ответы делают передачу работы осмысленной.

## English version

Armando Picón published an [essay on AI-assisted engineering](https://picon.dev/en/publications/ai-assisted-engineering/) on November 1. Its central position is that delegating implementation does not remove responsibility for choosing the task and accepting the result. The author explicitly presents a working position rather than a controlled study. It cannot establish a percentage productivity gain or a conclusion about replacing a profession. For this edition, it provides a reason to examine one practical question: what evidence supports accepting a change when an agent produced it?

Consider an original hypothetical example from Frontier Wire, rather than a deployment reported by the essay's author. An online store changes its basket calculation so that delivery becomes free only after reaching a threshold. An agent supplies a patch and a test covering a purchase comfortably above that threshold. The test passes. It has not established what happens exactly at the boundary, just below it or after removing an item. A green result supports the selected case rather than automatically establishing the entire intended behavior.

Now suppose the test copies the implementation's formula. If both contain the same comparison error, agreement can be stable and repeatable. This is a useful counterexample to treating repeatability as sufficient evidence of correctness. The expected outcome needs an independent basis in the product rule. In this example, a small table of boundary baskets could be specified beforehand, with the exact delivery charge expected for each. That is reasoning about verification design, not an account of a defect discovered in a real shop or an experiment we performed against deployed commerce software.

There is another boundary. Even a correct formula does not show that the selected rule matches the product owner's intention. Perhaps the threshold applies after discounts, or perhaps before them. If that remains unspecified, additional runs will not resolve the ambiguity. Someone authorized to define the behavior needs to make the decision visible, so that a subsequent developer or agent does not reconstruct it by guessing. The number of generated lines cannot answer whether such a decision has been made, recorded or reflected in the implementation.

These examples distinguish several kinds of evidence. Testing specific values establishes behavior on selected inputs. Reviewing the change helps identify effects outside the intended scope. Exercising the interface shows how the result is presented to a user. None replaces the others. A wording change warrants a different scale of review from a monetary calculation. Proportionality matters more than maximizing the number of automated actions when those actions all test the same assumption. Repeating one narrow check cannot supply coverage of cases that were never included.

### Why it matters

The development is a clearly qualified engineering argument, not new proof of faster software delivery. Concrete acceptance examples make that argument useful to discuss. An agent can help produce implementation and gather evidence, but announcing success does not broaden the evidence's coverage. Teams still face testable questions: what outcome was required, which cases were actually checked, and which decisions cannot yet be inferred from the results? Answering them makes delegation meaningful without confusing generated work with accepted behavior.
