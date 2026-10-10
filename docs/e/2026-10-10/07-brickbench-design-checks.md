---
date: 2026-10-10
rubric: ai
title_ru: "BrickBench проверяет, умеет ли ИИ спроектировать LEGO, а не просто показать красивую сборку"
title_en: "BrickBench separates buildable LEGO designs from attractive images"
dek_ru: "Препринт от 8 октября сравнивает физическую допустимость, соответствие заданию и качество дизайна — это разные проверки."
dek_en: "An October 8 preprint treats physical validity, prompt alignment and design quality as separate tests."
source: https://arxiv.org/html/2610.12452v1
generated: true
---

## Русская версия

В [препринте BrickBench, поданном 8 октября](https://arxiv.org/html/2610.12452v1), исследователи предложили проверять кодирующих ИИ-агентов на проектировании LEGO. Важная оговорка касается слова «собираемый»: симулятор не моделирует прочность соединений. Проект, который проходит его проверку, ещё не получает гарантии, что настоящая конструкция не провиснет или не развалится.

На [странице проекта авторов](https://www.brickben.ch/) описаны 300 заданий и три режима. В Model разрешено до 400 деталей, в Set — от 400 до 4000, а Alt-Build ограничивает выбор содержимым определённого набора. Среда BrickAgent даёт средства размещать детали, смотреть результат и проверять ошибки. Отдельно оцениваются допустимость конструкции, соответствие описанию и относительное качество дизайна. Это не один универсальный балл, заменяющий все остальные.

Авторы статьи также сообщают о сравнении с человеческими моделями: участники определили человеческий вариант в 323 из 360 оценок. Пары подбирали по количеству деталей, но не по одинаковому заданию. Это ограничивает вывод: исследование не является соревнованием человека и агента, которым выдали одну и ту же инструкцию. Мы не превращаем результат такого теста в оценку всей человеческой или машинной креативности.

Редакционный интерес здесь — возможность сделать провал конкретным. Представьте, что вы просите спроектировать небольшой мост. Один вариант хорошо выглядит на картинке, но детали пересекаются. Другой физически допустим, однако изображает не мост. Третий выполняет формальные условия, но выглядит скучно. Это разные причины не принять работу, и исправления для них тоже потребуются разные. Один красивый рендер не позволяет понять, с каким вариантом вы имеете дело.

Такой мысленный пример показывает пользу раздельных проверок. Если агент видит локальную ошибку соединения, можно обсуждать исправление соединения. Если не выполнен пункт задания, нужен возврат к требованиям. Если всё проверяемое выполнено, остаётся дизайнерский выбор: пропорции, выразительность и уместность. Требовать от одного показателя ответа на все эти вопросы — значит заранее потерять часть информации.

Но и набор проверок стоит оценивать критически. Проверяющая программа видит только заложенные в неё условия. Добавление ещё одного теста может изменить понятие успеха, даже если сама модель останется прежней. Для читателя таблицы результатов это повод спросить не только о месте агента, но и о том, какие ошибки вообще могли попасть в оценку.

### Почему это важно

BrickBench даёт понятный повод обсуждать качество работы ИИ через готовый результат и условия его проверки. Наш вывод: перед сравнением баллов сформулируйте, что вы хотите получить и что признаете ошибкой. Проект из деталей хорошо показывает, почему соответствие инструкции, отсутствие обнаруженных дефектов и удачный дизайн нельзя автоматически считать синонимами.

## English version

The [BrickBench preprint submitted on October 8](https://arxiv.org/html/2610.12452v1) evaluates coding agents on LEGO design. An important qualification concerns the word buildable: the simulator does not model connection strength. Passing its checks therefore provides no guarantee that a real assembly will avoid sagging or falling apart.

The authors' [project page](https://www.brickben.ch/) describes 300 prompts and three settings. Model permits up to 400 parts; Set requires 400–4000; Alt-Build restricts agents to the inventory of a particular retail set. BrickAgent supplies tools to place parts, inspect the assembly and check failures. Physical validity, agreement with the description and relative design quality receive separate assessments. No single score makes the others redundant.

The paper also reports a comparison with human designs: raters identified the human version in 323 of 360 judgments. Pairs were matched by part count rather than by an identical assignment. This limits the interpretation: it was not a contest in which a person and an agent received the same instructions. We would not turn this result into a measurement of all human or machine creativity.

Our editorial interest is the opportunity to make failure specific. Imagine asking for a small bridge. One output looks convincing in an image but contains intersecting pieces. Another meets physical constraints but depicts something other than a bridge. A third satisfies the formal requirements yet makes an uninspired design. These are different reasons to reject an output, requiring different fixes. An attractive rendering alone cannot tell you which case you have.

This hypothetical example illustrates why separate checks are useful. A reported connection error invites a connection repair. An unmet requirement calls for revisiting the brief. Once the verifiable conditions are satisfied, questions of proportion, expression and suitability remain. Asking one metric to settle every question discards information before the comparison begins.

The checks themselves deserve scrutiny too. A validator can see only the conditions built into it. Adding a test can change what counts as success without changing the underlying model. When reading a results table, it is therefore worth asking which defects could enter the evaluation, as well as where an agent ranks. That question is especially useful when a score is presented as an all-purpose measure of capability.

### Why it matters

BrickBench offers an accessible way to discuss AI output through the finished object and the conditions used to inspect it. Our takeaway is to define the desired result and the failures that would make it unacceptable before comparing scores. A design made of parts makes clear why following instructions, having no detected defects and producing a compelling design should never automatically be treated as the same achievement.
