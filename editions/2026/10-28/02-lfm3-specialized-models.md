---
date: 2026-10-28
rubric: ai
title_ru: LFM3 разводит текст, зрение и звук по компактным моделям с общей основой
title_en: LFM3 puts text, vision and audio models on a shared compact backbone
dek_ru: Liquid AI представила шесть вариантов семейства для специализации и работы рядом с приложением.
dek_en: Liquid AI introduced six variants intended for specialization and deployment close to the application.
source: https://huggingface.co/blog/LiquidAI/lfm3
generated: true
---

## Русская версия

Приложению, которое читает документы, и голосовому помощнику не обязательно нужна одна и та же модель. Liquid AI 27 октября [представила семейство LFM3](https://huggingface.co/blog/LiquidAI/lfm3): шесть компактных вариантов с общей языковой основой. В набор входят текстовая, визуальная, аудио- и объединённая мультимодальная модели, а также две модели структурированных решений. Главный ракурс анонса — возможность выбирать входные данные и специализацию, сохраняя общую основу семейства.

Базовая LFM3-1.7B объединяет короткие свёртки, локальное и глобальное внимание. Разные компоненты обрабатывают контекст разными способами, вместо того чтобы заставлять все слои работать одинаково. По описанию разработчика, это часть подхода к компактности и длинному контексту. Заявленное окно текстовой модели составляет 256 тысяч токенов. Но размер допустимого контекста сам по себе не устанавливает, насколько точно приложение извлечёт нужный факт из длинного документа или сколько памяти потребует конкретный запуск.

Визуальный вариант принимает текст, изображения и видео, а аудиоверсия работает с текстом и звуком и может отвечать речью. Omni объединяет эти входы. Для разработчика это выбор тракта обработки, а не просто новое имя общего чат-бота. Поддержка видео также не означает, что все варианты семейства видят кадры, а наличие речи у одной модели нельзя автоматически переносить на текстовый checkpoint. Различия между участниками нужно сохранять при обсуждении возможностей.

Два варианта d1 предназначены для структурированных решений по заданным вопросам. Они отличаются от свободного порождения длинного ответа: приложению могут требоваться выбор, оценка или координаты объекта. При этом качество такого решения нужно проверять на своей задаче. Упоминание калиброванных вероятностей в анонсе — характеристика, заявленная поставщиком, а не проведённый редакцией тест на новом наборе. Число в структурированном поле остаётся оценкой системы и не превращает неоднозначный вход в бесспорный факт.

Liquid AI делает акцент на дообучении каждого варианта на одной GPU и развёртывании на пользовательских устройствах. Это описание предлагаемого процесса, а не обещание одинаковых требований для любых данных и режимов. Ресурсы зависят от выбранной модели, точности представления и длины входа. Сравнения скорости и качества в публикации принадлежат разработчику. Мы не скачивали веса, не запускали код и не проверяли анонсированные результаты самостоятельно; приведённые примеры объясняют назначение семейства.

### Почему это важно

Семейство предлагает собирать приложение вокруг нужной модальности и узкого результата. Такой выбор может упростить обсуждение требований: какие данные поступают, какой ответ нужен и где выполняется обработка. Он не отменяет проверки ошибок, задержек и памяти на реальном сценарии. Содержательная часть анонса — связанный набор моделей для разных входов, который даёт разработчику варианты специализации. Преимущество конкретного варианта предстоит измерять в контексте будущего продукта.

## English version

An application reading documents and a voice assistant do not necessarily need the same model. On October 27, Liquid AI [introduced the LFM3 family](https://huggingface.co/blog/LiquidAI/lfm3): six compact variants sharing a language backbone. The release includes text, vision, audio and combined multimodal models, alongside two structured-decision variants. The central proposition is choosing the appropriate inputs and specialization while retaining a common foundation, rather than treating every application as a request for an identical general-purpose conversational system.

The LFM3-1.7B backbone combines short convolutions, sliding-window attention and global attention. Different components handle context in different ways instead of making every layer follow the same pattern. The developer presents this as part of its approach to compactness and long inputs. The text model has a stated context window of 256 thousand tokens. That limit alone does not establish how accurately an application retrieves a fact from a long document or how much memory a particular execution will require.

The vision variant accepts text, images and video; the audio model works with text and sound and can produce speech. Omni combines those inputs. This is a choice of processing path rather than merely another name for a chatbot. Video support does not mean every family member can inspect frames, and speech capabilities should not automatically be assigned to a text checkpoint. Those differences matter when translating a family-level announcement into requirements for a particular application or deployment environment.

The two d1 variants address structured decisions over supplied questions. Their output differs from open-ended long-form generation: an application may need a choice, score or object location. The quality of that decision still needs evaluation on the intended task. Calibrated probabilities are a supplier claim here, rather than a Frontier Wire test on an additional dataset. A number in a structured field remains an estimate from the system and does not turn an ambiguous input into an indisputable fact.

Liquid AI emphasizes single-GPU fine-tuning and deployment on end-user devices. That describes a proposed workflow, not identical requirements for every dataset and operating mode. Resource needs depend on the selected variant, numerical precision and input length. Performance comparisons in the release belong to the developer. We have not downloaded weights, executed the examples or independently checked the reported results; the examples explain the family's intended uses rather than establishing performance for a product that has not yet been evaluated.

### Why it matters

The family offers a way to organize an application around its required modality and output. That can make requirements more concrete: which data arrives, which result is needed and where processing happens. It leaves error, latency and memory testing essential on a real scenario. The substantive announcement is a related set of models supporting different inputs and specialization paths. Whether one is advantageous for a particular product remains a question to measure in that product's operating context.
