---
date: 2026-10-10
rubric: tech
title_ru: "Голос помог написать функцию блога, но выпуск потребовал ревью и работы с клавиатурой"
title_en: "Voice helped build a blog feature; shipping still involved review and typing"
dek_ru: "Саймон Уиллисон описал конкретный опыт работы с Codex и показал публичный PR, а не универсальный тест скорости разработки."
dek_en: "Simon Willison describes a specific Codex workflow and links its public pull request, rather than a general productivity benchmark."
source: https://simonwillison.net/2026/Oct/9/built-using-my-voice/
generated: true
---

## Русская версия

Саймон Уиллисон 9 октября [описал разработку новой страницы рассылок голосом](https://simonwillison.net/2026/Oct/9/built-using-my-voice/). По его рассказу, примерно полчаса разговора с Codex во время приготовления ужина дали почти готовую функцию Django. Затем ещё примерно полчаса работы текстом ушли на доведение результата. Это опыт автора с конкретной задачей, не замер производительности на группе разработчиков.

В [публичном PR №719](https://github.com/simonw/simonwillisonblog/pull/719), объединённом 9 октября, виден отдельный этап ревью. Уиллисон отметил, что вызов Git из подпроцесса неудобен для его развёртывания на Heroku, и решил заменить механизм импорта обращением к API. Комментарии и последующие изменения подтверждают, что разговор не был последним этапом работы. Доступ к закрытым данным автора мы не проверяли и не переносили; для этой новости достаточно публичного рассказа и обсуждения кода.

Редакционный вывод из примера касается интерфейса, а не обещания писать любой продукт между делом. Голос позволяет быстро описать желаемое поведение. Но работа всё равно нуждается в критериях завершения. Если требование звучит как «показывай этот материал здесь, а там не показывай», полезно получить видимый результат и проверить оба места. Иначе плавный разговор создаст ощущение понятности, которое ещё не подтверждено приложением.

Воображаемый пример помогает увидеть границу: попросите добавить поле к форме. Рассказать, зачем поле нужно, можно устно. Проверка пустого значения, сохранения данных и старых записей требует увидеть поведение системы. Ни один способ ввода сам по себе не отвечает на эти вопросы. Голос, клавиатура и просмотр результата могут выполнять разные части одной работы, без необходимости объявлять один из них победителем.

Поэтому демонстрацию стоит разбирать по этапам: постановка задачи, получение изменений, просмотр и решение о выпуске. В каждом этапе можно спросить, что пользователь уже знает и чего ещё не проверил. Длинный устный сеанс сам по себе не показывает, что полученный код соответствует условиям реального развёртывания; для этого нужен отдельный источник подтверждения.

Для оценки подобных историй также важно различать удобство и экономию. Удобный способ освободить руки может оказаться полезным, даже если общая работа не стала быстрее. А сравнение времени требует одинаковых задач и понятной исходной линии. В этом случае разумнее говорить о показанном способе взаимодействия, чем вычислять прирост, которого автор не измерял.

### Почему это важно

Рассказ показывает практическое сочетание разговора с проверкой конкретных изменений. Наш вывод — оценивать новую форму общения по тому, насколько она помогает поставить задачу и увидеть результат. Готовность к выпуску определяется выполненными требованиями; эффектный способ дать поручение не должен подменять эту проверку.

## English version

Simon Willison [described building a newsletter page by voice](https://simonwillison.net/2026/Oct/9/built-using-my-voice/) on October 9. In his account, roughly half an hour talking to Codex while cooking produced a nearly complete Django feature. About another half-hour of text-based work followed. This is one author's experience with a particular task, rather than a productivity measurement across a group of developers.

The [public pull request, number 719](https://github.com/simonw/simonwillisonblog/pull/719), merged on October 9, shows a distinct review stage. Willison observed that invoking Git through a subprocess was unsuitable for his Heroku deployment and chose an API-based import instead. The comments and subsequent changes support a narrower point: the conversation was not the final stage of the work. We did not inspect or transfer his private data; the public account and code discussion suffice for this story.

Our editorial takeaway concerns the interface, rather than a promise to build any product while doing something else. Voice can communicate desired behavior quickly. The work still needs completion criteria. When a requirement amounts to showing content in one place but excluding it elsewhere, it helps to inspect the result in both places. Otherwise, a fluent conversation can produce a feeling of clarity that the application has not yet confirmed.

Consider a hypothetical request to add a form field. Explaining its purpose may work well aloud. Checking an empty value, saved data and existing records requires observing the system's behavior. No input method answers those questions by itself. Speech, typing and visual inspection can serve different parts of one workflow, without a need to declare a single winner.

That suggests reading demonstrations stage by stage: defining the task, obtaining changes, inspecting them and deciding whether to ship. At each point, ask what the user already knows and what remains unchecked. A long voice session cannot by itself demonstrate that the code meets the conditions of its eventual deployment. That requires another kind of evidence.

Convenience and savings also deserve separate treatment. A useful way to free your hands may have value even if the entire task is no faster. Establishing a speed improvement would require comparable assignments and a defined baseline. Here it is more accurate to discuss a demonstrated interaction pattern than to calculate a gain the author did not measure.

### Why it matters

The account shows conversation combined with inspection of concrete changes. Our takeaway is to judge a new interface by how well it helps specify the task and examine the result. Readiness to ship depends on fulfilled requirements. An impressive way of giving instructions should not substitute for checking whether those instructions were actually met.
