---
date: 2026-10-06
rubric: ai
title_ru: OpenAI вводит маркировку текста — детектор пока для исследователей
title_en: OpenAI starts text watermarking, with detector access limited to researchers
dek_ru: В API маркировка добровольная; внедрение в ChatGPT и Codex в ЕС займёт ближайшие недели.
dek_en: API watermarking is opt-in, while the EU rollout for ChatGPT and Codex is planned over the coming weeks.
source: https://openai.com/index/eu-text-provenance
generated: true
---

## Русская версия

OpenAI 5 октября [объявила](https://openai.com/index/eu-text-provenance) о поэтапном внедрении textGrain: добровольной маркировке текстовых ответов отдельных моделей API по всему миру и предстоящем внедрении в ChatGPT и Codex в ЕС. В API функция выключена по умолчанию. Заявки на детектор принимают от исследователей и экспертных организаций; общедоступного текстового проверяющего сервиса на старте нет. В одном тесте замена четверти слов синонимами снизила обнаружение с примерно 92% до 17%. Это оценка компании, привязанная к условиям эксперимента.

Как выглядит метка? В [справке OpenAI](https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content) описан статистический рисунок выбора слов и частей слов. Он не добавляет невидимые символы, пробелы или необычную пунктуацию. Сигнал происхождения также не удостоверяет правдивость, законность использования или личность автора. Наличие и отсутствие метки следует толковать с учётом поддерживаемого продукта и преобразований текста. Проверка изображений и аудио — отдельная возможность, которую нельзя автоматически считать проверкой прозы.

[Технический отчёт](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf) поясняет компромисс между силой сигнала и случайностью генерации. Метод связывает выбор токенов с псевдослучайностью секретного ключа, задавая бюджет потери энтропии. Вычисления проводят над блоками словаря, сохраняя относительные вероятности внутри блока. Для обнаружения нужны текст и ключ; бюджет, использованный при генерации, знать не требуется. Это описание механизма и его математических предпосылок, а не независимая проверка любого документа.

Еврокомиссия в [описании кодекса прозрачности](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) разделяет обязанности поставщиков по машинной маркировке и обязанности применяющих систему по раскрытию определённых видов контента. Технические решения должны учитывать ограничения форматов и достижимый уровень надёжности. Поэтому новость о выбранном компанией способе маркировки сама по себе не отвечает на все вопросы об обязанностях конкретной редакции или организации.

Наш редакционный вывод: стоит разделять происхождение, достоверность и ответственность. Представьте черновик, который человек перестроил, проверил и сократил. Статистический тест ищет технический след; редактор отвечает за утверждения и публикацию. Эти вопросы пересекаются, но требуют разной проверки. Для рабочего процесса полезно хранить исходный черновик, сведения о применённом инструменте и историю значимых правок. Тогда спор об участии помощника опирается на документы, а не на один индикатор, вырванный из контекста.

### Почему это важно

Появляется ещё один способ говорить о происхождении текста, однако его результат нужно сопровождать условиями проверки. Для читателя практический вопрос остаётся прежним: чем подтверждается конкретное утверждение? Для редакции добавляется второй: достаточно ли прозрачно описан процесс подготовки материала, чтобы человек мог понять роль инструментов и роль людей?

## English version

On October 5, OpenAI [announced](https://openai.com/index/eu-text-provenance) a phased introduction of textGrain: optional watermarking for selected API models worldwide, followed by eligible ChatGPT and Codex text outputs in the EU over the coming weeks. The API setting remains off by default. Detector applications initially target researchers and expert organizations, rather than a public text-checking service. In one company evaluation, replacing a quarter of the words with synonyms reduced detection from roughly 92% to 17%. Those figures describe a particular experiment, not every document.

The [help article](https://help.openai.com/en/articles/8912793-provenance-signals-in-openai-generated-content) describes a statistical pattern in word and token choices. The watermark does not insert invisible characters, spaces or unusual punctuation. Provenance signals also do not establish accuracy, lawful use or the creator's identity. Results need interpretation alongside product coverage and subsequent transformations. Image and audio verification is a separate capability; its availability should not be mistaken for general access to a prose detector.

The [technical report](https://cdn.openai.com/pdf/e9508624-d767-41b6-a26d-e34ca798ada6/textgrain-entropy-calibrated-watermarking-for-language-model-text.pdf) explains the tradeoff between signal strength and generation randomness. The method couples token choices to keyed randomness, using an entropy-loss budget. Vocabulary blocks reduce the computation while preserving relative probabilities within each block. Detection requires the text and key, without knowing the generation budget. This describes the mechanism and the assumptions behind its mathematics; it is not independent authentication of an arbitrary document.

The European Commission's [transparency code overview](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) distinguishes providers' machine-readable marking responsibilities from deployers' disclosure responsibilities for certain content. Technical solutions must account for format limitations and feasible reliability. A company's implementation announcement therefore cannot settle every compliance question for a particular publisher or organization. The announcement gives readers a product decision to examine, rather than a complete rulebook for their own situation.

Our editorial reading is that origin, accuracy and responsibility deserve separate questions. Imagine a draft that a person reorganizes, checks and shortens. A statistical detector looks for a technical trace; the editor takes responsibility for the claims and publication. Those inquiries overlap but call for different evidence. Keeping the original draft, a record of the tool used and a history of meaningful revisions would make a dispute about assistance easier to examine. One isolated indicator provides much less context.

### Why it matters

Text provenance now has another proposed signal, whose interpretation needs the conditions of the check. Readers should still ask what supports a particular assertion. Publishers have an additional practical question: whether their account of the writing process lets a person understand the contribution of tools and the judgment of humans. A watermark can inform that conversation; the surrounding documentation gives it meaning.
