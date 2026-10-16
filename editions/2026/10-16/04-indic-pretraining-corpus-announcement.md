---
date: 2026-10-16
rubric: ai
title_ru: "NVIDIA и AI4Bharat анонсировали корпус на 2,8 трлн токенов для индийских языков"
title_en: "NVIDIA and AI4Bharat announce a 2.8-trillion-token Indic corpus"
dek_ru: "Материалы охватывают 22 языка, но основной корпус ещё обещан к выпуску, а переводы не заменяют местные оригинальные тексты."
dek_en: "The resource covers 22 languages, but the main corpus is still forthcoming and translations do not replace locally authored text."
source: https://huggingface.co/blog/nvidia/scaling-indic-pretraining
generated: true
---

## Русская версия

В [публикации от 16 октября](https://huggingface.co/blog/nvidia/scaling-indic-pretraining) NVIDIA и AI4Bharat из IIT Madras описали Nemotron-pretraining-Indic-v1 — корпус примерно на 2,8 триллиона токенов для 22 индийских языков. Авторы одновременно раскрывают рецепт генерации и проверки данных. При этом сам большой корпус обозначен как ожидаемый к выпуску: новость нельзя читать как подтверждение, что весь набор уже доступен для скачивания.

Важен не только объём, но и происхождение текста. Это преимущественно перенос отобранных англоязычных материалов в другие языки, с отдельными вариантами записи латиницей для части языков. Авторы сохраняют идентификаторы исходных документов и описывают проверки перевода. Такой процесс позволяет проследить происхождение записи, но не превращает её в независимый оригинальный текст местного автора.

Для всех 22 языков заявлены данные в собственных письменностях; для двенадцати предусмотрена также латинская запись. Речь о разных формах индийского текста, не об английском переводе. Число токенов также требует определения. В публикации оно связано с конкретным токенизатором и учитывает разные переводы и варианты письменности. Несколько записей могут выражать содержание одного источника. Поэтому большой итог нельзя напрямую сравнивать с числом уникальных документов или считать числом различных идей. Для обучения существенны и объём, и разнообразие содержимого.

В двенадцатиязычной части процесса переводчик одновременно выступает автоматическим оценщиком. Есть выборочные проверки людьми, однако авторы отмечают различие их охвата между языками и сохранение возможных ошибок. Оценка по внутренней шкале качества не означает соответствующий процент истинности или точности. Это правило отбора внутри конкретного процесса, которое само нуждается в проверке.

Отдельно показано улучшение нескольких показателей после этапа дополнительного обучения с индийскими языками. Но на этом этапе использовалась смесь синтетического и естественного текста. Поэтому приписывать весь прирост только новому синтетическому корпусу было бы сильнее представленных данных. Такой вывод потребовал бы сравнения, в котором остальные условия действительно удерживаются одинаковыми.

Для читателя можно сформулировать практическое различие. Перевод учебного объяснения делает это объяснение доступнее на другом языке. Он не добавляет автоматически знания о местной истории, разговорной норме или культурном контексте, отсутствовавшие в исходнике. Эти задачи требуют другого состава материалов. Именно поэтому авторы рассматривают синтетические данные как дополнение, а не замену естественным текстам.

### Почему это важно

Анонс интересен масштабом и описанием воспроизводимого процесса. Следующий содержательный шаг — проверить доступность основной поставки, её условия использования и качество по каждому языку. Один общий счётчик токенов не показывает, насколько хорошо будущая модель будет понимать конкретное сообщество и его задачи.

## English version

In an [October 16 post](https://huggingface.co/blog/nvidia/scaling-indic-pretraining), NVIDIA and AI4Bharat at IIT Madras describe Nemotron-pretraining-Indic-v1, an approximately 2.8-trillion-token corpus covering 22 Indian languages. They also describe the generation and quality-assessment recipe. The main corpus is explicitly presented as forthcoming, so the announcement should not be read as confirmation that the entire collection is already available to download.

Its provenance matters as much as its size. The resource largely transfers curated English material into other languages, with Latin-script variants for some of them. The authors retain source-document identifiers and describe translation checks. This makes records traceable, but does not turn a translation into an independently authored local source.

Native-script data is described for all 22 languages, with romanized text for twelve. These are alternative forms of Indic text, not English translations. The token total also needs a definition. In the announcement, it depends on a particular tokenizer and includes translations and script variants that can share the same underlying source. A larger count is therefore not directly a count of unique documents or distinct ideas. Both quantity and content diversity matter when interpreting a proposed training resource.

In the twelve-language workflow, the translating model also serves as an automated quality judge. Human checks are sampled, their coverage varies between languages, and errors may remain. A score on an internal quality rubric is not the corresponding percentage of factual accuracy. It is an acceptance rule within a particular process, and that rule needs evaluation too.

The announcement separately reports improvements after a continued-pretraining stage involving Indian languages. That stage used a mixture of synthetic and naturally authored text. Attributing its entire benefit to the new synthetic corpus would therefore exceed the comparison. Establishing that contribution would require holding the other relevant conditions constant.

A practical distinction helps explain the scope. Translating a technical explanation makes that explanation accessible in another language. It does not automatically add knowledge of local history, conversational conventions or cultural context missing from the source. Those needs call for different material. The authors accordingly present synthetic data as a complement to natural text, rather than a substitute.

For anyone evaluating the eventual release, per-language inspection would be more informative than relying on the overall total. It would also be useful to distinguish a model that follows a preferred writing system from one that has acquired the knowledge needed for a particular application. Those outcomes can overlap without being identical.

### Why it matters

The announcement combines scale with an explicit account of how data is produced. The next meaningful steps are checking the main release's availability, terms and language-specific quality. A single token counter cannot establish how well a future model will serve a particular community or task.
