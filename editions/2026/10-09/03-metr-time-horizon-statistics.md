---
date: 2026-10-09
rubric: ai
title_ru: Статистики предлагают читать горизонты ИИ вместе с графиками сложности задач
title_en: Statisticians argue AI time horizons need task-difficulty diagnostics
dek_ru: Новый препринт пересчитывает данные METR и показывает, почему одинаковое увеличение времени не всегда означает одинаковый рост возможностей.
dek_en: A new preprint reanalyzes METR data and explains why equal time multipliers need not represent equal capability gains.
source: https://arxiv.org/html/2610.12466v1
generated: true
---

## Русская версия

Дрю Нгуен и Уильям Фитиан из Калифорнийского университета в Беркли [опубликовали статистический разбор горизонтов ИИ](https://arxiv.org/html/2610.12466v1). Первая версия препринта датирована 8 октября. Авторы повторно анализируют данные METR по 228 программным задачам и 26 системам, предлагая более гибкие способы оценки. Их вопрос касается измерительной шкалы: насколько время, нужное человеку, помогает описывать сложность задания для ИИ. Это исследование методики, а не объявление нового рекорда конкретной модели.

Горизонт с вероятностью успеха 50% имеет довольно точный смысл. Это длительность человеческой работы над задачами, которые ИИ выполняет примерно в половине попыток. Число не равно времени, которое агент способен непрерывно работать без ошибок, и не гарантирует половину любого произвольного проекта. Оно получается из выбранных заданий и статистической модели. Поэтому красивый график в минутах или часах остаётся оценкой, а не прямым показанием секундомера автономности.

Авторы ослабляют предположение о линейной связи сложности для ИИ с логарифмом человеческого времени. Для этого они используют гибкую кривую и методы теории ответов на задания, позволяющие учитывать различия между задачами и их семействами. В полученной зависимости заметен почти плоский участок между примерно двумя и тридцатью минутами. По их интерпретации, увеличение человеческого времени в этой области не сопровождается таким же ростом трудности для ИИ, как на других участках шкалы.

Понятный пример из работы: переход горизонта от трёх к тридцати минутам не равноценен переходу от тридцати минут к пяти часам. В обоих случаях множитель равен десяти, но найденная связь времени со сложностью различается. Это не означает, что развитие систем исчезло из данных. Авторы прямо отделяют пересмотр оценок и их интерпретации от отрицания наблюдаемого роста. Критика направлена на то, какой смысл читатель приписывает расстояниям на графике.

Новые оценки команда проверяет по прогнозам успеха на отложенных семействах задач, используя перекрёстную проверку и несколько способов статистического оценивания. По результатам авторов, предложенные подходы улучшают точечные оценки по использованным метрикам. Они также предлагают смотреть на графики преобразования времени в сложность и условной вероятности успеха. При этом исследование остаётся препринтом и разбором определённого набора программных задач; перенос вывода на всю экономику, робототехнику или любые профессии требует отдельной проверки.

### Почему это важно

Человеческие часы делают достижения ИИ понятными, но понятная единица ещё не делает шкалу одинаковой на всех участках. Работа предлагает сохранить полезный показатель и добавить диагностику, показывающую его ограничения. Для читателя это повод спрашивать, какие задачи стоят за цифрой, как оценена их трудность и проверяется ли прогноз успеха. Так можно обсуждать прогресс содержательно, не превращая один статистический график в обещание надёжно выполненного проекта.

## English version

Drew Nguyen and William Fithian of UC Berkeley [published a statistical analysis of AI time horizons](https://arxiv.org/html/2610.12466v1), with its first preprint version dated October 8. They reanalyze METR data covering 228 software tasks and 26 AI systems, proposing more flexible estimation methods. Their question concerns the measurement scale: how well does the time a human needs describe difficulty for an AI? This is methodological research, rather than the announcement of a new record for a particular model.

A 50% time horizon has a specific meaning. It is the human completion time of tasks that an AI succeeds at with roughly even odds. It does not measure how long an agent can continuously operate without mistakes, nor guarantee success on half of an arbitrary project. The number is estimated from selected tasks and a statistical specification. A chart expressed in minutes or hours therefore remains an estimate, rather than a direct stopwatch reading of autonomy.

The authors relax the assumption that AI task difficulty depends linearly on the logarithm of human time. They use flexible curves and item-response methods that account for differences between tasks and task families. The resulting relationship has a nearly flat region between approximately two and thirty minutes. Their interpretation is that greater human completion time within this region does not imply the same increase in AI difficulty seen elsewhere on the scale.

The paper illustrates the point with two tenfold changes: moving from three to thirty minutes, and moving from thirty minutes to five hours. The multiplier is identical, but the estimated relationship between time and difficulty differs. That does not mean progress has disappeared from the data. The authors explicitly distinguish revised estimates and interpretation from a rejection of the observed growth. Their critique addresses what readers infer from distances between points on the chart.

The team evaluates its estimates against success predictions on held-out task families, using cross-validation and multiple statistical scoring measures. According to the authors, the proposed approaches improve point estimates across the evaluation metrics used. They also recommend time-to-difficulty conversion plots and conditional success trajectories alongside the headline horizons. The study remains a preprint and an analysis of a particular software-task collection. Applying its conclusions to the entire economy, robotics or arbitrary occupations would require separate validation.

### Why it matters

Human hours make AI performance easier to communicate, but an understandable unit does not ensure that the scale behaves uniformly. This work proposes retaining a useful measure while adding diagnostics that reveal its limitations. Readers can ask which tasks support the number, how their difficulty is estimated and whether success predictions hold up. That supports a more informative discussion of progress without turning a statistical chart into a promise that a real project will be completed reliably.
