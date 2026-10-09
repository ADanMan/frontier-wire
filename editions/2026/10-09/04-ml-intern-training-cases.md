---
date: 2026-10-09
rubric: ai
title_ru: Hugging Face показала обучение небольших моделей через ML Intern с проверками и бюджетом
title_en: Hugging Face reports small-model training with ML Intern, checks and budgets
dek_ru: В авторском разборе шести проектов есть базовые оценки, короткие пробные запуски и вычислительные расходы, но нет универсального прайс-листа.
dek_en: A six-project account includes baselines, short trial runs and compute charges, rather than a universal price list.
source: https://huggingface.co/blog/building-with-ml-intern
generated: true
---

## Русская версия

Hugging Face [опубликовала разбор шести проектов с ML Intern](https://huggingface.co/blog/building-with-ml-intern) 8 октября. Авторы описывают обучение и адаптацию моделей через режим в HuggingChat: пользователь формулирует задачу, агент планирует работу, запрашивает бюджет, пробует небольшой запуск, затем обучает, оценивает и публикует результат. Новость здесь — подробный отчёт о конкретных опытах. Он не доказывает, что любое обучение теперь можно свести к одному сообщению или выполнить за одинаковую сумму.

Самая полезная часть разбора — устройство задания. Авторы предлагают заранее назвать набор данных, исходную модель, ожидаемый результат и известные проверенные сведения. Две проверки особенно важны: измерить качество исходной модели до обучения и выполнить короткий пробный запуск перед большим. В одном из сценариев проверяется, что сохранённые веса действительно изменились. Это отделяет запуск программы без явной ошибки от обучения, результат которого можно содержательно сравнить с исходной точкой.

Один из проектов — компактная модель для переписывания запросов к генератору изображений. По отчёту, она имеет 0,8 миллиарда параметров вместо девятимиллиардного учителя и предлагается также в GGUF для CPU. В работе использовали ответы учителя для подготовки примеров, затем фильтрацию и обучение меньших моделей. Авторы называют около 16 долларов вычислительных расходов за весь этот проект. Это стоимость перечисленных заданий на CPU и GPU, а не универсальная цена создания любого помощника или гарантия одинакового качества на чужих запросах.

Другой сценарий — адаптация генератора изображений под персонажа. Команда сравнивала одинаковые запросы на промежуточных сохранениях обучения. По описанию, нужный образ появился раньше, чем нежелательные стилистические изменения стали заметны в несвязанных запросах. Это пример того, зачем выбирать контрольную точку по проверке результата, а не просто брать последнюю. Увеличение числа шагов может менять поведение модели и за пределами желаемой новой способности; в отчёте это показано как наблюдение конкретного опыта.

Разбор также включает изменение ракурса, редактирование по нарисованному контуру и сокращение числа шагов генератора. Авторы сообщают о неудачных заданиях из-за зависимостей или путей и о повторных запусках. В таблице суммарно указано примерно 103 доллара вычислительных расходов по шести проектам. Человеческая подготовка заданий, выбор данных и проверка результата описаны отдельно, поэтому эту сумму нельзя выдавать за полную цену работы. Наличие опубликованной модели тоже не заменяет оценку её пригодности для следующей задачи.

### Почему это важно

Агентное обучение становится убедительнее, когда рядом с моделью есть исходная оценка, пробный запуск, сравнение сохранений и понятная граница расходов. Отчёт показывает такой процесс на небольших примерах, а не обещает универсальную автоматизацию. Практический вывод — автоматизировать выполнение можно, сохраняя проверку цели и результата. Для оценки дальнейших проектов важны те же вопросы: что стало лучше, на каких примерах это видно и какие затраты действительно посчитаны.

## English version

Hugging Face [published an account of six projects using ML Intern](https://huggingface.co/blog/building-with-ml-intern) on October 8. The authors describe model training and adaptation through a HuggingChat mode: the user specifies a task, the agent plans the work, requests a budget, runs a small trial, then trains, evaluates and publishes a result. The development is a detailed report of particular experiments. It does not establish that every training job can be reduced to one message or completed for the same amount.

The most useful part is how assignments are framed. The authors recommend naming the dataset, base model, expected deliverables and facts already checked. Two tests are central: evaluate the base model before training, and run a short trial before a larger job. One scenario checks that saved weights have actually changed. That distinguishes a program finishing without an obvious error from training whose result can meaningfully be compared with its starting point.

One project produces a compact prompt rewriter for image generation. The reported student has 0.8 billion parameters, compared with a nine-billion-parameter teacher, and is also offered in GGUF form for CPU use. The process used teacher-generated examples, filtering and smaller-model training. The authors put total compute charges for this project at about $16. That describes the listed CPU and GPU jobs, rather than a universal price for creating an assistant or a guarantee of equivalent quality on someone else's requests.

Another project adapts an image generator to a character. The team compares the same prompts across training checkpoints. In the account, the desired character appears before unwanted stylistic changes become apparent in unrelated prompts. This illustrates why a checkpoint should be chosen by inspecting outputs, rather than automatically selecting the last one. Additional training can change behavior outside the intended new ability; the report presents that as an observation from this particular experiment.

The other examples include changing viewing angles, editing from a drawn outline and reducing an image generator's step count. The authors also describe failed jobs caused by dependencies or paths, followed by resubmissions. Their table totals approximately $103 in compute charges across the six projects. Human preparation of assignments, dataset choices and result checks is discussed separately, so that figure should not be presented as the complete cost of the work. Publishing a model likewise does not establish that it is suitable for the next task.

### Why it matters

Agent-assisted training is easier to assess when a model comes with a baseline, a trial run, checkpoint comparisons and an explicit spending boundary. The report illustrates that process through small examples, rather than promising universal automation. Execution can be automated while the purpose and outcome remain subject to checks. Future projects should answer the same questions: what improved, which examples demonstrate it, and which costs were actually counted?
