---
date: 2026-11-13
rubric: ai
title_ru: LLMON размечает, где инструкция, а где данные
title_en: LLMON marks instructions and data as different context components
dek_ru: IBM представила экспериментальные Granite preview; обученное разделение не является принудительной гарантией защиты.
dek_en: IBM introduced experimental Granite previews, with learned separation distinct from enforced security guarantees.
source: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite
generated: true
---

## Русская версия

IBM Granite 12 ноября [представила LLMON и два экспериментальных preview](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite) на базе Granite 4.1 3B и 8B. Формат явно обозначает инструкции, данные и связи между частями контекста. Авторы исследуют устойчивость к косвенным prompt injection и прямо называют такое поведение обученным, а не принудительной гарантией. Preview предназначено для экспериментов, не production. Редакция не запускала модели. Сегодняшняя новость — предложение формата и доступных исследовательских инструментов, а не подтверждение, что проблема подмены инструкций решена во всех ситуациях.

Общий вопрос удобно объяснить на самостоятельном условном примере. Помощник получает документ для краткого пересказа. Внутри документа есть фраза, похожая на приказ изменить задачу. Для человека различие часто очевидно: это текст, который нужно прочитать, а не новое поручение автора запроса. У программы такое различие должно сохраняться на всём пути обработки. Это редакционная иллюстрация границы между содержимым и полномочием, а не воспроизведение атаки или дополнительный результат из опубликованных испытаний конкретной модели.

Явная структура полезна только вместе с корректным использованием. Если приложение неправильно пометит происхождение текста, аккуратный формат сам по себе не исправит ошибку. В условном испытании нужно отдельно проверить, как сформирован вход, что увидела модель и почему следующий шаг разрешён. Эти уровни отвечают на разные вопросы. Хорошее поведение на одном примере не устанавливает устойчивость всей системы. Особенно важно не делать из удобного обозначения обещание, что любые внешние данные автоматически становятся безопасными независимо от дальнейших действий приложения и его доступных возможностей.

Сравнение подходов требует одинаковой задачи. В нашем условном пилоте можно сохранить исходный документ, ожидаемый результат и критерии нарушения, затем рассмотреть разные способы передачи контекста. Если одновременно меняются модель, данные и оценщик, причину результата трудно установить. Это предложение по проверке, а не заявленный нами эксперимент. Полезно учитывать не только очевидные неудачи, но и случаи, когда ответ выглядит нормальным, однако теряет важное ограничение исходного поручения или начинает ссылаться на материал, который вообще не относится к поставленному вопросу.

Есть и вопрос сопровождения. Формат, модель и приложение должны одинаково понимать назначение передаваемых компонентов. В условном проекте документация должна объяснять, какие части входа приходят извне, а какие задаёт сама программа. Это не требует публиковать частные данные или истории разговоров. Достаточно описать схему и проверить её на разрешённых примерах. Такая работа помогает отличить свойства отдельной модели от свойств всей интеграции и не переносить исследовательские результаты на систему, в которой условия уже существенно отличаются от изученных авторами.

### Почему это важно

Структура контекста становится самостоятельным предметом обучения и оценки. LLMON предлагает способ сделать отношения между частями входа явнее, сохраняя экспериментальный статус. Практический вывод — проверять и формат, и поведение модели, и действия приложения; ни один из этих уровней не заменяет остальные одной формулировкой о защищённости.

## English version

IBM Granite [introduced LLMON and two experimental previews on November 12](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite), based on Granite 4.1 3B and 8B. The format explicitly marks instructions, data and relationships within context. The authors investigate indirect prompt-injection resistance while describing the behaviour as learned rather than an enforced guarantee. The previews are for experimentation, not production. We have not run the models. This is a format and research-tool announcement, not confirmation that instruction substitution has been solved in every setting.

An independent hypothetical example explains the boundary. An assistant receives a document to summarise, containing a sentence resembling an order to change the task. A person may readily distinguish material to read from a new instruction issued by the requester. A software workflow needs to preserve that distinction throughout processing. This is an editorial illustration of content and authority, not an attack reproduction or another result from the models' published evaluation. Keeping those concepts separate helps make the practical question understandable without inventing a new security finding.

Explicit structure also depends on correct application use. If software mislabels the origin of text, a tidy format alone cannot repair that mistake. A hypothetical assessment should separately inspect input construction, what the model receives and why a subsequent action is authorised. Those layers answer different questions. Good behaviour on one example cannot establish resilience of the complete system. It is particularly important not to turn a useful notation into a promise that arbitrary external data automatically become safe regardless of the application's later actions and available capabilities.

Comparisons need matching tasks. A local pilot could preserve the original document, expected result and violation criteria, then examine different ways of providing context. Changing the model, data and evaluator together would make the cause of an outcome difficult to identify. This is a testing suggestion, not an experiment conducted by this publication. Alongside obvious failures, an evaluator can consider apparently ordinary responses that lose a key requirement or rely on material unrelated to the question. Such cases help specify what successful handling should mean for the intended workflow.

Maintenance introduces another question. The format, model and application need a consistent interpretation of the supplied components. In a hypothetical project, documentation could identify which input parts originate externally and which the software supplies itself. That does not require publishing private data or conversation histories. A schema and authorised examples can support examination. This distinguishes properties of one model from those of an integration, avoiding automatic transfer of research results to a setting whose conditions differ substantially from the authors' evaluation or whose operating permissions introduce separate issues.

### Why it matters

Context structure becomes an explicit target for training and assessment. LLMON proposes clearer relationships between input components while retaining experimental status. Practical evaluation should consider the format, model behaviour and application actions together. No single layer replaces the others through a general statement about protection, and the announcement appropriately leaves room for further testing.
