---
date: 2026-10-25
rubric: ai
title_ru: Decisions API выходит из беты с ответами из заданного набора
title_en: Decisions API leaves beta with answers from a bounded set
dek_ru: OpenAI предлагает отдельный интерфейс для классификации и выбора следующего шага, а не длинного ответа.
dek_en: OpenAI offers a dedicated interface for classification and next-step selection rather than long-form responses.
source: https://openai.com/index/decisions-api
generated: true
---

## Русская версия

В приложении с ИИ далеко не каждый запрос требует сочинения. Иногда нужно определить категорию документа, выбрать маршрут обращения или оценить признак по заранее заданной шкале. OpenAI 22 октября [объявила об общей доступности Decisions API](https://openai.com/index/decisions-api): интерфейса на базе GPT-6 Luna, рассчитанного именно на такие ограниченные вопросы. Вечерняя подборка обращается к этому анонсу как к обновлению последних дней, а не запуску, случившемуся сегодня.

Разработчик задаёт вопрос, контекст и допустимые ответы. На вход можно передавать текст, изображения и структурированные данные. Здесь полезно представить развилку в программе: вместо свободного объяснения ей нужен результат, с которым следующий участок кода умеет работать. Выбор следующего действия ещё не означает, что действие исполнено: это остаётся задачей приложения, которое получило ответ.

Поддерживаются три вида результата. Predicate оценивает вероятность условия числом от нуля до единицы. Choice выбирает один из предложенных вариантов и возвращает сведения о вероятностях и уверенности. Score оценивает вход по упорядоченным уровням рубрики. Эти формы отвечают разным вопросам: «есть ли признак», «какой вариант выбрать» и «насколько выражено свойство». От того, насколько внятно вы определили уровни и варианты, зависит, будет ли ответ полезен в вашем процессе.

После публичной беты появились нативный JSON на входе, изображения в инструкциях к вопросу и до 400 вопросов в одном запросе — вдвое больше прежнего лимита. Также объявлены кеширование повторяемого контекста и обработка в регионах США и ЕС. Для голосовых приложений добавлена интеграция с GPT-Live: результат решения может помогать выбирать дальнейшую реакцию во время разговора. Это описание возможностей поставщика, а не проведённый редакцией тест сервиса.

Компания заявляет ускорение до десяти раз относительно GPT-6 Luna через Responses API. Ключевые слова здесь — «до» и конкретное сравнение интерфейсов. Такая цифра не обещает десятикратного ускорения вашего приложения: в нём есть другие этапы, а ошибки классификации тоже имеют цену. Практический смысл отдельного интерфейса стоит проверять на знакомых примерах, включая неоднозначные случаи, для которых предусмотрена передача человеку.

### Почему это важно

Анонс показывает понятное направление развития прикладного ИИ: небольшое решение становится самостоятельной частью системы. Но узкий формат ответа не превращает вероятностную оценку в установленный факт. Для читателя, который строит такой процесс, полезный вопрос звучит просто: какой именно выбор можно доверить модели, как заметить ошибку и что произойдёт после неё? Ответы на эти вопросы говорят о качестве приложения больше, чем скорость одного вызова.

## English version

Many requests inside an AI application do not need an essay. They need a document category, a destination for a support request, or a rating against a predefined scale. On October 22, OpenAI [announced general availability of the Decisions API](https://openai.com/index/decisions-api), a dedicated interface built with GPT-6 Luna for questions with bounded answers. This evening's selection treats it as an update from the past few days, rather than a launch that happened today.

Developers supply a question, its permitted answers and the context needed to decide. Inputs can include text, images and structured data. Think of a branch in a program: the next piece of code needs a usable result rather than an open-ended explanation. Selecting an action does not itself execute that action. The application receiving the answer still determines what happens next, which is an essential distinction when evaluating an agent workflow.

There are three result types. A predicate estimates the probability that a condition holds, on a scale from zero to one. A choice selects one of the supplied options and includes probability and confidence information. A score evaluates an input against ordered rubric levels. These correspond to different questions: whether a feature is present, which option fits, and how strongly something is expressed. Their usefulness depends partly on whether the developer has defined meaningful categories and levels in the first place.

Changes since the public beta include native JSON input, images in question instructions and up to 400 questions per request, double the previous limit. OpenAI also announced caching for reused context and inference residency in the United States and European Union. A native GPT-Live integration supports decisions during voice conversations, where a result can help select the application's next response. These are the supplier's descriptions; Frontier Wire has not run a performance evaluation of the service.

OpenAI claims speeds up to ten times faster than using GPT-6 Luna through the Responses API. Both the qualification and the comparison matter. That does not promise a tenfold improvement for an entire application, whose other stages still take time and whose classification errors still carry consequences. A useful evaluation would examine familiar examples alongside ambiguous cases that should reach a reviewer, rather than considering response time alone.

### Why it matters

The announcement makes a practical direction visible: a small decision can become a distinct component of an AI system. A narrow output format, however, does not turn a probabilistic judgement into an established fact. For someone building that system, the useful questions are which choice the model should make, how an error becomes visible and what follows from it. Those answers say more about application quality than the speed of an individual call.
