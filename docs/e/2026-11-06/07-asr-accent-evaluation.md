---
date: 2026-11-06
rubric: ai
title_ru: Open ASR Leaderboard добавил египетский и нигерийский английский
title_en: Open ASR Leaderboard adds Egyptian and Nigerian English
dek_ru: Новые закрытые выборки расширяют проверку акцентов, но не представляют всё разнообразие речи.
dek_en: New private test splits broaden accent coverage without representing every kind of speech.
source: https://huggingface.co/blog/open-asr-leaderboard-liva
generated: true
---

## Русская версия

Hugging Face и Liva AI 6 ноября [объявили о двух новых закрытых выборках](https://huggingface.co/blog/open-asr-leaderboard-liva) для Open ASR Leaderboard: разговорный английский с египетским и нигерийским акцентами. Их длительность — 1,34 и 1,55 часа соответственно. Это расширение набора проверок распознавания речи, а не выпуск новой модели. Из объявления нельзя вывести, что какая-либо система теперь одинаково хорошо понимает всех говорящих: для такого утверждения потребовались бы существенно более широкие данные.

Смысл новости удобно объяснить на нашем условном примере. Допустим, сервис расшифровывает рабочие звонки. Общая оценка выглядит высокой, но внутри неё могут скрываться разные результаты для разных групп пользователей. Если одна группа представлена гораздо чаще, среднее число мало рассказывает о качестве для остальных. Поэтому покупателю полезно видеть не только общий рейтинг, но и состав теста. Это вопрос применимости измерения к вашей задаче, а не соревнование национальностей или попытка оценивать людей по произношению.

Объём выборки тоже требует внимания. Небольшой набор способен выявить проблему, но не обязан охватить все условия будущего использования. В нашем примере это могли бы быть шумная переговорная, телефонная связь, длинный разговор или профессиональные термины. Мы не утверждаем, что опубликованные записи содержат такие ситуации. Напротив, это вопросы, которые стоит задать до переноса результата в собственный продукт. Отсутствие определённого сценария в проверке не доказывает ни хорошей, ни плохой работы в нём.

Ещё один самостоятельный критерий — цена конкретной ошибки. Для поиска по архиву пропущенный предлог может оказаться терпимым, а неверно записанное имя затруднит нахождение нужного фрагмента. Поэтому одинаковое количество ошибок не обязательно означает одинаковую полезность двух расшифровок. Практическая проверка может отдельно учитывать важные слова и возможность исправить текст. Такие критерии нужно согласовать до сравнения поставщиков, чтобы удачный результат не подбирался задним числом под уже выбранное решение.

Закрытые тестовые данные ставят и вопрос доверия к процедуре. Внешнему читателю важно понимать, как результаты воспроизводятся и какие сведения организатор раскрывает об оценке. При этом закрытый набор не следует путать с разрешением отправлять туда чужие записи. Для собственного пилота нужны подходящие согласия и условия обработки данных. Это общие рекомендации для покупателя, а не дополнительные сведения о договорённостях участников сегодняшнего объявления или о том, как собирались конкретные записи.

### Почему это важно

Более разнообразный тест помогает поставить правильный вопрос: будет ли распознавание работать для ваших пользователей. Ответ стоит искать в разрезах результатов и небольшом собственном пилоте с понятными критериями. Позиция в общей таблице полезна как ориентир, но сама по себе не заменяет такую проверку.

## English version

Hugging Face and Liva AI [announced two private test splits on November 6](https://huggingface.co/blog/open-asr-leaderboard-liva) for the Open ASR Leaderboard: conversational English with Egyptian and Nigerian accents, lasting 1.34 and 1.55 hours respectively. This expands speech-recognition evaluation rather than introducing a new model. The announcement does not establish that any system understands every speaker equally well. Such a claim would require considerably broader evidence than the addition of two test sets.

An independent hypothetical example explains the practical issue. Suppose a service transcribes work calls. Its overall score looks strong, but different user groups may experience different results. If one group contributes far more examples, the average offers limited guidance about the others. A buyer therefore needs to consider the composition of the test as well as its headline ranking. This concerns whether a measurement fits a particular use case, rather than comparing nationalities or assigning value to people's pronunciation.

Sample size also deserves attention. A small collection can expose a problem without covering all conditions a future deployment will encounter. In our example, those might include a noisy meeting room, a telephone connection, long conversations or specialist terminology. We are not suggesting that the announced recordings contain those situations. They are questions to ask before applying a published result to a product. An untested scenario supports neither a favourable nor an unfavourable conclusion about performance in that setting.

A further independent consideration is the cost of an error. In an archive search, a missing preposition might be tolerable while a wrongly transcribed name could make the relevant passage difficult to locate. Equal error counts need not imply equal usefulness. A practical assessment could therefore examine important terms separately and consider how easily someone can correct the transcript. Criteria should be agreed before suppliers are compared, so that a favourable measure is not selected retrospectively to justify an existing choice.

Private evaluation data also raise procedural questions for readers. It matters how results can be checked and what the organiser discloses about its methods. A private test should never be confused with permission to upload somebody else's recordings. Any local pilot needs appropriate consent and suitable data-handling arrangements. These are general considerations for prospective users, not additional claims about the participants' agreements or the collection process behind today's announcement. The distinction keeps advice separate from reported facts.

### Why it matters

Broader testing helps ask whether speech recognition will serve the people who actually use a product. Useful answers come from examining result breakdowns and running a suitable pilot with explicit criteria. An overall league table can guide that work, but its ranking alone cannot replace an assessment of the intended setting.
