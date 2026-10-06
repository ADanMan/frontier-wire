---
date: 2026-10-06
rubric: ai
title_ru: Перенести блок-схему на слайд и сохранить её логику
title_en: Moving a flowchart onto a slide without losing its logic
dek_ru: Новый препринт предлагает три этапа и редактируемый XML вместо одной перерисованной картинки.
dek_en: A new preprint proposes three stages and editable XML instead of a single regenerated image.
source: http://arxiv.org/abs/2610.06852v1
generated: true
---

## Русская версия

Блок-схема хорошо смотрится в статье, но в вертикальном постере подписи становятся крошечными, а стрелки путаются. [Препринт от 5 октября](http://arxiv.org/abs/2610.06852v1) One Figure, Every Canvas рассматривает перенос существующей схемы между форматами как отдельную задачу. Авторы признают зависимость от закрытой модели, дополнительные затраты и отсутствие гарантированной сходимости. Итеративная проверка помогает, но не обещает идеальный результат. Это исследовательская система, которую редакции ещё предстоит оценить на собственных материалах.

На [странице проекта](https://onefigureeverycanvas.vercel.app/) показан конвейер Parse, Style и Layout: восстановление структуры, оформление и перестановка элементов. На каждом этапе агент работает с критиком, сочетающим визуальное суждение с детерминированными проверками. Выход — редактируемый XML draw.io. В подборке из 100 схем и пяти форматов авторы сообщают 68,6% Content Fidelity против 11,2–41,4% у сравниваемых методов. Это оценка их бенчмарка, не универсальный процент правильности для любых схем.

В [репозитории реализации](https://github.com/ChenCXxx/OneFigure-EveryCanvas) предусмотрены промежуточные XML, изображения и результаты критиков по итерациям. Итог сохраняется и картинкой, и самостоятельной XML-схемой. Для запуска нужны окружение Python, API-ключи и настольный интерфейс draw.io для командного рендеринга. SAM3 требуется, если заранее не заданы ограничивающие рамки объектов. Следовательно, открытый код здесь означает доступ к реализации; весь вычислительный стек не становится автономным приложением от одного скачивания.

Почему формат результата существенен? [Документация draw.io](https://www.drawio.com/docs/manual/advanced/diagram-source-edit/) объясняет, что XML описывает фигуры, соединители, стили и метаданные. Его можно открыть через Extras → Edit Diagram, поправить и применить обратно; некорректный XML вызывает ошибку. Это даёт пользователю способ исследовать и исправлять элементы отдельно. По нашему прочтению, такая возможность превращает результат генерации в рабочий документ, а не только в изображение для просмотра.

Представьте схему с развилкой «прошёл проверку» и «нужна доработка». При переносе на узкий экран важно, куда ведёт каждая ветка. Изменение её направления меняет объяснение процесса, даже если буквы читаются прекрасно. Поэтому мы бы проверяли сначала соответствие соединений исходнику, затем все подписи и только потом расположение и стиль. Это предлагаемая процедура редакторского приёма, а не дополнительный результат эксперимента. Сохранение исходного рисунка рядом с новой версией облегчает такую проверку и позволяет обсуждать конкретное расхождение.

### Почему это важно

Исследование ставит полезный вопрос: что должно пережить смену формата? Для объясняющей схемы ответ включает отношения между объектами. Редактируемый результат помогает исправлять найденную ошибку без повторной генерации всего изображения. Но финальное согласование остаётся содержательной работой: нужно понять, что схема утверждает, и сверить это с исходным объяснением.

## English version

A flowchart may fit a paper perfectly and become unreadable on a portrait poster. Shrinking it leaves tiny labels; rearranging it risks confusing the arrows. The October 5 [One Figure, Every Canvas preprint](http://arxiv.org/abs/2610.06852v1) treats adapting an existing diagram to a new canvas as a distinct task. Its authors acknowledge closed-model dependence, extra costs and no guaranteed convergence. Iterative checks help without promising perfection. This is a research system to assess on real editorial material.

The [project page](https://onefigureeverycanvas.vercel.app/) presents Parse, Style and Layout stages, covering structural reconstruction, appearance and arrangement. Each agent has a critic combining visual judgment with deterministic checks. Outputs remain editable draw.io XML. Across 100 flowcharts and five target ratios, the authors report 68.6% Content Fidelity, compared with 11.2–41.4% for their baselines. That is an assessment on their benchmark, rather than a universal accuracy figure for all diagrams or future installations.

The [implementation repository](https://github.com/ChenCXxx/OneFigure-EveryCanvas) retains intermediate XML, rendered images and critic results for individual iterations. The final result includes both an image and a self-contained XML diagram. Setup requires a Python environment, API keys and the draw.io desktop command-line renderer. SAM3 is needed when bounding boxes have not already been provided. Available source code therefore provides access to the implementation; downloading it does not turn the entire computational stack into a standalone application.

The output format deserves attention. [draw.io's documentation](https://www.drawio.com/docs/manual/advanced/diagram-source-edit/) explains that XML describes shapes, connectors, styles and metadata. Users can inspect it through Extras → Edit Diagram, make changes and apply them; invalid XML produces an error. Individual elements can therefore be examined and repaired. Our reading is that this turns a generated result into a working document, with an explicit route for correction, rather than only a picture to look at.

Consider a diagram with branches for “passed the check” and “needs revision.” On a narrow screen, the destination of each branch matters more than an attractive arrangement. Reversing one connection changes the explanation even when the lettering looks excellent. We would check connections against the original first, then labels, and finally placement and style. That is a proposed editorial acceptance procedure, not an additional experimental finding. Keeping the original beside the adaptation makes it easier to identify and discuss a specific discrepancy.

### Why it matters

The research asks a useful question: what must survive a change of format? For an explanatory diagram, the relationships between objects are part of the answer. Editable output makes a discovered error easier to repair without generating the whole picture again. Final approval still requires understanding what the diagram says and checking it against the explanation it is meant to convey.
