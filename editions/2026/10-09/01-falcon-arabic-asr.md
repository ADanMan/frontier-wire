---
date: 2026-10-09
rubric: ai
title_ru: Falcon ASR делает ставку на арабские диалекты и отметки времени для каждого слова
title_en: Falcon ASR targets Arabic dialects with word-level timestamps
dek_ru: TII опубликовал результаты модели на арабских и английских тестах; сравнения относятся к выбранным наборам и датам.
dek_en: TII reports Arabic and English evaluation results, with comparisons tied to specific datasets and a dated leaderboard snapshot.
source: https://huggingface.co/blog/tiiuae/falcon-asr
generated: true
---

## Русская версия

Technology Innovation Institute [представил Falcon ASR](https://huggingface.co/blog/tiiuae/falcon-asr) — модель распознавания речи с 1,6 миллиарда параметров и особым вниманием к эмиратскому диалекту арабского языка. Полный анонс опубликован 7 октября. Модель также поддерживает английский, французский, испанский и португальский. Это система для получения текста из записи, а не переводчик: авторы прямо указывают, что результат остаётся на языке исходной речи. Для всех пяти языков используются одни веса, без отдельного флага языка.

Причина выделить диалект вполне практическая. По объяснению разработчиков, успешная расшифровка формальной новости ещё не означает хорошего результата на обычном разговоре или телефонной записи. Различаются произношение, словарь и условия звука. TII сообщает об обучении на эмиратском диалекте, литературном арабском, других арабских и заливных диалектах и английском. Авторы также включали шум, музыку, наложение голосов, реверберацию и эффекты телефонной связи, чтобы расширить набор условий записи.

Главный публичный показатель в анонсе — средняя доля ошибок в словах, WER, на шести арабских тестовых наборах. TII сообщает 20,92% против 23,17% у лучшего опубликованного результата в использованном снимке таблицы, проверенном 30 сентября. Разница составляет 2,25 процентного пункта. Важны и единица сравнения, и дата: это не утверждение о превосходстве над всеми системами на любой записи. Наборы в среднем имеют одинаковый вес, а результаты относятся к указанному протоколу.

Дополнительно команда приводит внутренний тест эмиратской и заливной речи: 22,73% WER и 10,19% ошибок в символах. По её данным, Falcon ASR показал лучшие значения среди сравнивавшихся систем. Это отдельная оценка на отложенных записях с проверенными людьми расшифровками; её нельзя незаметно объединять с публичной таблицей. Для английского разработчики указывают средний WER 5,74% по семи открытым тестам. Числа описывают свои наборы, а не вероятность правильного распознавания конкретной вашей фразы.

Есть и полезная функция вне соревнования метрик: отметки времени на уровне отдельных слов. Они связывают расшифровку с местом в аудио, поэтому текст можно сверять с записью. Авторы предлагают демонстрацию на Hugging Face, тогда как API и отдельные приложения описывают как будущие планы. Доступность демо не следует принимать за состоявшийся запуск всех способов интеграции. В этой заметке результаты атрибутированы разработчикам; самостоятельного сравнения систем редакция не проводила.

### Почему это важно

Качество распознавания речи зависит от того, какие голоса и условия представляют испытания. Внимание к диалекту делает этот вопрос заметным, а временные отметки помогают проверять итог. Содержательный следующий шаг для оценки продукта — сравнить расшифровки на подходящих записях и понять типы ошибок. Средняя метрика полезна как ориентир, когда рядом сохранены её набор данных, протокол и границы интерпретации.

## English version

The Technology Innovation Institute [introduced Falcon ASR](https://huggingface.co/blog/tiiuae/falcon-asr), a 1.6-billion-parameter speech-recognition model with a particular focus on Emirati Arabic. The full announcement was published on October 7. The model also supports English, French, Spanish and Portuguese. Its output is a transcript rather than a translation: the developers specify that it remains in the language spoken. All five languages use the same model weights, without requiring a separate language flag.

The focus on dialect addresses a practical problem. As the developers explain, a system that transcribes a formal broadcast well may still struggle with an everyday conversation or a phone recording. Vocabulary, pronunciation and recording conditions differ. TII reports training on Emirati, Modern Standard Arabic, other Arabic and Gulf dialects, and English. The training also included noise, music, overlapping speech, reverberation and telephony effects to expose the system to a wider range of audio conditions.

The headline public result is the average word error rate, or WER, across six Arabic test sets. TII reports 20.92%, compared with 23.17% for the best published result in the leaderboard snapshot it checked on September 30. That is a difference of 2.25 percentage points. Both the comparison unit and the date matter: this is not a claim of superiority over every system on every recording. The test sets receive equal weight in the average, and the figures refer to a specified evaluation protocol.

The team separately reports an internal evaluation of Emirati and Gulf speech, with 22.73% WER and a 10.19% character error rate. According to TII, Falcon ASR achieved the lowest values among the systems compared. This assessment uses held-out recordings and human-validated transcripts; it should not be silently merged with the public leaderboard. For English, the developers report a mean WER of 5.74% across seven public tests. Those figures describe their datasets, rather than the probability that any particular sentence will be transcribed correctly.

One useful feature sits outside the leaderboard contest: word-level timestamps connect the transcript to positions in the audio, making it easier to check the text against the recording. The announcement offers a Hugging Face demonstration, while API access and native applications remain planned. Availability of the demonstration should not be read as a completed launch of every integration method. This article attributes evaluation results to the developers; the newsroom has not run an independent comparison.

### Why it matters

Speech-recognition quality depends on which speakers and conditions a test represents. The emphasis on dialect makes that question visible, while timestamps help users inspect the output. A meaningful evaluation should compare transcripts on appropriate recordings and examine the errors they contain. An average score becomes more informative when its dataset, protocol and interpretation limits remain attached.
