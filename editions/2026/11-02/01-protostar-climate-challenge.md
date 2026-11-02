---
date: 2026-11-02
rubric: science
title_ru: ProtoStar начинает климатический конкурс с проверкой на уже наблюдавшихся годах
title_en: ProtoStar starts a climate challenge tested against observed years
dek_ru: Старт назначен на 2 ноября; текущие правила задают 2019–2025 годы, уточняя горизонт первоначального анонса.
dek_en: The challenge is scheduled to start November 2, with current rules specifying 2019–2025 rather than the initial announcement's horizon.
source: https://huggingface.co/blog/announcing-project-protostar
generated: true
---

## Русская версия

На 2 ноября назначен старт первого конкурса ProtoStar — инициативы по повторному использованию открытых научных материалов. В [анонсе от 29 октября](https://huggingface.co/blog/announcing-project-protostar) организаторы представили климатическую задачу, которую проводит Carnegie Mellon. Она предлагает проверять прогнозы на известных наблюдениях, а не ждать десятилетия, чтобы узнать, сработала ли модель. На момент утреннего выпуска мы проверили доступную страницу правил, но не регистрировали команду и не отправляли прогнозы от имени владельца сайта.

Между анонсом и [текущими условиями конкурса](https://cmu-ospo-protostar-challenge-climate-risk-intelligence.hf.space/) есть важное расхождение. Первый описывает горизонт до 2026 года, тогда как страница задания требует прогнозировать 2019–2025 годы по сведениям, доступным до конца 2018-го. Именно второй диапазон использован в этой статье. Само наличие более подробной страницы не объясняет причину изменения; предполагать её или обещать будущие сроки оценки из старого текста было бы неверно. Перед участием условия следует сверить ещё раз.

Данные охватывают 210 городов США. Четыре показателя — средняя годовая температура, годовые осадки, самый жаркий день и градусо-дни охлаждения, связанные с потребностью в кондиционировании. Срок конкурса указан как 2–13 ноября. Текущая страница отделяет промежуточную проверку 2019–2021 годов от итоговой 2022–2025; таблица лидеров пока обозначена как ожидаемая. Это правила предстоящего сравнения, а не уже опубликованный результат превосходства какого-либо метода.

Интерес задачи — в устройстве проверки. Рассмотрим простой мысленный пример: система всегда повторяет среднее прошлых лет. Такая система может выглядеть скучно, но задаёт ясную точку отсчёта. Более сложная модель должна показать, какую дополнительную информацию она извлекла, вместо того чтобы выигрывать только за счёт большего числа параметров. Если предсказание хуже простой базы, сложность сама по себе не даёт основания считать подход полезнее. Это методологическое рассуждение, а не оценка ещё не представленных конкурсных решений.

Вторая трудность — утечка будущего. Например, данные о потреблении электричества за прогнозируемый жаркий год могут косвенно подсказать температуру даже без колонки с погодой. Такое сравнение уже отвечало бы на другой вопрос: можно ли восстановить известный исход по его последствиям? Для честного прогноза нужно сохранить границу доступной информации. Полезно также отделять качество численного предсказания от разумности предлагаемой меры адаптации: небольшая ошибка модели не доказывает эффективность конкретного городского решения.

### Почему это важно

Открыть набор данных недостаточно, чтобы показать его исследовательскую ценность. Конкурс предлагает конкретный способ проверить повторное использование: указать информационную границу, получить воспроизводимые прогнозы и сравнить их с базой. Результаты ещё впереди. Пока наиболее содержательная новость — старт проверяемой задачи и доступные правила, включая уточнённый горизонт. Это позволяет обсуждать будущие выводы на уровне условий эксперимента, а не заранее объявленной победы ИИ над статистикой.

## English version

November 2 is the scheduled opening of the first ProtoStar challenge, part of an initiative supporting reuse of open scientific resources. The [October 29 announcement](https://huggingface.co/blog/announcing-project-protostar) introduced a climate task hosted by Carnegie Mellon. It proposes testing predictions against observations that already exist, rather than waiting decades to discover whether a model worked. For this morning edition, we checked the available rules page but did not register a team or submit forecasts on the site owner's behalf.

There is a material difference between the announcement and the [current challenge instructions](https://cmu-ospo-protostar-challenge-climate-risk-intelligence.hf.space/). The former describes a horizon through 2026, while the task page specifies forecasts for 2019–2025 using information available through the end of 2018. This article uses the latter range. The existence of more detailed instructions does not explain why the horizon changed. Inferring a reason, or carrying forward evaluation dates from the older account, would go beyond the evidence. Participants should check the rules again before entering.

The task covers 210 US cities and four indicators: annual average temperature, total precipitation, the hottest day and cooling degree days associated with air-conditioning demand. The stated competition dates are November 2–13. The current page separates a live evaluation period of 2019–2021 from final evaluation on 2022–2025, and still labels its leaderboard as coming soon. These are arrangements for a comparison, rather than published evidence that any particular method has already won. Availability of the instructions is not the same event as completion of the evaluation.

The design of that comparison is the interesting part. Consider a hypothetical system that always repeats a historical average. It may appear unambitious, but it supplies a clear reference. A more complex model has to establish what additional information it extracts, rather than relying on its parameter count to suggest an advantage. If its predictions are worse than that simple reference, complexity alone does not make it more useful. This is a methodological observation, not an assessment of challenge entries that have yet to be presented or evaluated.

Another difficulty is information leakage. Electricity consumption during a hot target year, for example, could indirectly reveal temperature without containing a weather column. That would answer a different question: can an outcome be reconstructed from its consequences? A genuine forecast needs to preserve the boundary of available information. Numerical accuracy should also be separated from the merits of an adaptation proposal. A small prediction error does not establish that a particular urban intervention will be effective or justify conclusions about its practical consequences without further evidence.

### Why it matters

Publishing data alone does not demonstrate its research value. This challenge offers a concrete way to examine reuse: specify an information boundary, produce reproducible predictions and compare them with a reference. Results remain ahead. The substantive development now is a scheduled, testable task with accessible rules and a clarified horizon. That provides a basis for discussing experimental conditions without declaring in advance that AI has defeated conventional statistical approaches.
