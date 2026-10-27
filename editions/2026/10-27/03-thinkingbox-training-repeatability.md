---
date: 2026-10-27
rubric: ai
title_ru: ThinkingBox использует проверку базы как награду для обучения агента
title_en: ThinkingBox turns database checks into agent-training rewards
dek_ru: В новом разборе важен не только средний успех Qwen, но и число задач, решённых во всех двадцати попытках.
dek_en: The follow-up examines both average Qwen success and tasks completed correctly in all twenty attempts.
source: https://huggingface.co/blog/microsoft/thinkingbox-training
generated: true
---

## Русская версия

Если агент говорит «готово», это ещё не значит, что нужная запись появилась в базе. Об этой идее ThinkingBox Frontier Wire уже писал в начале октября. В [продолжении Microsoft и Hugging Face от 22 октября](https://huggingface.co/blog/microsoft/thinkingbox-training) проверку сохранённого результата используют уже как награду при дообучении. Это новый этап работы с фреймворком, а не повторный анонс исходного стенда. Сегодня рассматриваем его с явно указанной датой публикации.

Для задачи с конкретным итоговым состоянием можно проверить, что действительно изменилось после работы агента. Правильный результат даёт положительную награду, отсутствующее или лишнее изменение — отказ. При этом не обязательно требовать единственную последовательность вызовов инструментов. Агент может найти другой путь, если тот приводит к допустимому состоянию. Это полезное разделение: оценивать цель процесса и проверять его побочные эффекты можно независимо от того, насколько убедительно исполнитель описывает собственную работу.

Авторы сообщают, что после пятидесяти шагов обучения Qwen3.8-27B средний успех вырос с 51,70 до 60,78 процента. Число задач, выполненных правильно во всех двадцати зафиксированных попытках, увеличилось с 38 до 107 из 507. Последний показатель — наблюдавшаяся повторяемость на заданном наборе, а не обещание безошибочности при любом будущем запуске. Двадцать успешных испытаний конечны и не превращаются в универсальную гарантию производственного поведения.

Есть и менее эффектная, но важная оговорка: охват задач, решённых хотя бы однажды за двадцать попыток, немного снизился. Иными словами, модель стала стабильнее на части заданий, но это не означает одинакового расширения всех способностей. Разные показатели отвечают на разные вопросы. Для редкой исследовательской находки может быть интересен хотя бы один успех; для повторяющейся операции над записью базы важнее, насколько часто правильный исход воспроизводится.

Обучающие задачи отделены от тестового набора, однако сохраняют общий фреймворк, стиль заданий и часть инфраструктуры. Поэтому перенос нельзя растягивать до вывода о надёжности любых деловых процессов. Кроме того, большинство проверок исполнимы напрямую, но меньшая часть использует модельного судью для узких требований. Публичные примеры не равны частному обучающему пулу исследования. Редакция не запускала обучение и не проверяла заявленные результаты независимо; это отчёт авторов.

### Почему это важно

Работа связывает критерий завершения задачи с обучением, а не оставляет его только финальным экзаменом. Главный практический вопрос — какое состояние означает успех и какие изменения недопустимы. Определив это, можно обсуждать и среднюю точность, и повторяемость, не подменяя одно другим. Рост показателя в конкретном стенде полезен как свидетельство метода, но применять вывод к собственному процессу следует через отдельную проверку его условий и последствий.

## English version

An agent saying that work is complete does not establish that the correct database record exists. Frontier Wire covered that ThinkingBox idea earlier in October. In a [Microsoft and Hugging Face follow-up published October 22](https://huggingface.co/blog/microsoft/thinkingbox-training), checks of the saved outcome become rewards for post-training. This is a further use of the framework rather than another announcement of the original benchmark. Today's coverage keeps the source date explicit instead of presenting the experiment as newly conducted this morning.

For a task with a specified terminal state, the system can inspect what changed after the agent worked. A correct outcome earns a positive reward; missing, wrong or extra effects fail. The evaluator need not demand one particular sequence of tool calls. An agent can find another acceptable route to the same outcome. That separates the goal and side effects of a process from how persuasively the agent describes its work, or whether its chosen sequence resembles a reference solution.

The authors report that fifty training steps raised Qwen3.8-27B's average success from 51.70 to 60.78 percent. Tasks passed on every one of twenty recorded attempts increased from 38 to 107 out of 507. The latter measures observed repeatability on a particular benchmark. It does not promise perfect behavior in every future execution. Twenty successful trials remain a finite observation, rather than becoming a universal guarantee about production reliability under different users, tools, policies or operating conditions.

There is a less spectacular but important qualification: coverage of tasks solved at least once in twenty attempts declined slightly. The model became more repeatable on part of the task set without uniformly broadening every capability. Different metrics address different needs. A research search may value finding one solution eventually; a recurring operation on a database record may depend more on how consistently the correct result can be reproduced. Neither purpose can be reduced to a single headline success number.

Training tasks are separate from the benchmark, but share its framework, task style and some infrastructure. Transfer should therefore not be generalized to every business workflow. Most outcome checks are directly executable, while a minority invoke a model judge for narrow requirements. Public samples are also not the private training pool used in the experiment. Frontier Wire has not run the training or independently reproduced the results; these are the authors' reported findings and methodological limits.

### Why it matters

The work connects task completion criteria with learning instead of reserving them for a final examination. The practical starting question is what state counts as success and which other changes are unacceptable. Once that is explicit, average accuracy and repeatability can be discussed separately. An improvement in this environment is evidence about an approach, while extending it to another process requires checking that process's own conditions and consequences rather than assuming the same gain will carry over.
