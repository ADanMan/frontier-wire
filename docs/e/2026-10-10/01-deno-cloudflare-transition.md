---
date: 2026-10-10
rubric: tech
title_ru: Deno присоединяется к Cloudflare и объявляет сроки поддержки своих продуктов
title_en: Deno joins Cloudflare and sets transition timelines for its products
dek_ru: Команда оставляет год обновлений runtime и шесть месяцев работы Deploy; будущую платформу связывает с Workers и Durable Objects.
dek_en: The team sets a year of runtime updates and six more months for Deploy, while directing future work toward Workers and Durable Objects.
source: https://deno.com/blog/cloudflare
generated: true
---

## Русская версия

Команда Deno [объявила о присоединении к Cloudflare](https://deno.com/blog/cloudflare) 9 октября. Runtime получит ещё год ежемесячных исправлений и обновлений безопасности, затем команда прекратит его разработку, сохранив открытый код. Deno Deploy продолжит работу шесть месяцев; платным клиентам обещана помощь с переходом на Workers. Это разные сроки для разных продуктов. Открытость кода и продолжение работы управляемого сервиса также следует рассматривать отдельно: одно само по себе не гарантирует другое.

Практический вопрос для команды, использующей Deno, — определить, от какой части системы зависит её приложение. Код, исполняемый в runtime, и приложение, размещённое в Deploy, могут иметь разные планы дальнейшей работы. Срок поддержки не сообщает автоматически объём переноса конкретного проекта. Для этого нужны сведения о его зависимостях, хранении данных, развёртывании и проверках. Это редакционный вывод из объявленного перехода, а не утверждение, что любой проект обязательно придётся полностью переписать.

В [совместном объяснении Cloudflare](https://blog.cloudflare.com/deno-joins-cloudflare/) будущая работа связана с объединением celld и workerd для самостоятельного размещения Workers и Durable Objects. Авторы описывают Durable Object как отдельно адресуемый объект с состоянием и базой SQLite. Одновременно они признают ограничение нынешнего самостоятельного workerd: поддержка этих объектов работает в одной инстанции. Распределённый вариант и более удобная эксплуатация на собственной инфраструктуре обозначены целью дальнейшей работы. Это направление проекта, а не готовый результат всей интеграции.

Различие между опубликованным кодом и полноценно работающей распределённой системой существенно. Возможность прочитать или запустить компонент ещё не отвечает на вопросы размещения состояния, восстановления после сбоя и сопровождения нескольких узлов. Здесь объявление интересно как попытка сделать сам способ построения приложения частью решения. Проверять такую идею стоит по доступным реализациям и поведению под нагрузкой, а не только по тому, сколько инфраструктурных деталей обещает скрыть новый интерфейс.

Для читателя важно и разделение фактов во времени. Присоединение команды объявлено сейчас; прекращение отдельных направлений и дальнейшая интеграция описаны как следующие этапы. Эти новости нельзя сокращать до утверждения, что все приложения Deno уже перестали работать. Из открытого кода также нельзя вывести гарантированное появление новой команды сопровождения. Такой переход меняет основание для планирования, но не сообщает заранее судьбу каждого проекта, который использует технологию.

### Почему это важно

Разработчики выбирают не только язык или удобный API, но и модель сопровождения программы и сервиса. Объявленные сроки помогают отдельно оценить поддержку runtime, размещение приложения и будущую архитектуру. Полезный результат такого разбора — понятный список зависимостей и проверяемый путь продолжения работы. Новость даёт основания для этой оценки; решение по конкретному приложению требует знания самого приложения, а не общего вывода о победе или поражении одного подхода к JavaScript.

## English version

The Deno team [announced that it is joining Cloudflare](https://deno.com/blog/cloudflare) on October 9. Its runtime will receive monthly fixes and security updates for another year, after which the team's development will end while the code stays open. Deno Deploy will operate for six more months, with migration help promised to paying customers moving to Workers. These are separate product timelines. Open code and a managed service continuing to operate are also distinct matters: one does not automatically guarantee the other.

For a team using Deno, a practical question is which part of the system its application depends on. Code executed by the runtime and an application hosted on Deploy may require different continuation plans. A support window does not itself establish how much migration a particular project needs. That assessment requires its dependencies, data storage, deployment and tests. This is an editorial implication of the transition, rather than a claim that every project must be rewritten completely.

The [joint Cloudflare explanation](https://blog.cloudflare.com/deno-joins-cloudflare/) describes future work combining celld and workerd to support self-hosted Workers and Durable Objects. The authors describe a Durable Object as an individually addressable, stateful unit with a SQLite database. They also acknowledge a current self-hosted workerd limitation: its Durable Objects support is single-instance. Distributed operation and easier management on users' own infrastructure are objectives of the work ahead, rather than established outcomes of the entire integration.

Published source code and a fully operational distributed system are different achievements. Being able to inspect or start a component does not settle questions about placing state, recovering from failures and maintaining multiple nodes. The announcement is interesting as an effort to make the programming model itself part of that solution. The idea can be assessed through available implementations and behavior under load, rather than only through the number of infrastructure details a proposed interface promises to hide.

The timeline also needs careful reading. The team transition is announced now; the ending of particular activities and further integration are subsequent stages. That should not be condensed into a statement that every Deno application has already stopped working. Open code likewise does not establish that a replacement maintenance team will appear. The announcement changes the basis for planning, without determining the future of each project built with the technology.

### Why it matters

Developers choose a maintenance arrangement as well as a language or convenient API. The stated timelines allow runtime support, application hosting and future architecture to be considered separately. A useful assessment produces a clear dependency inventory and a continuation path that can be tested. The announcement provides a reason to make that assessment; decisions about a particular application still require understanding the application itself, rather than declaring one JavaScript approach a universal winner or loser.
