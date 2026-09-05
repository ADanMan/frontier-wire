---
date: 2026-09-05
rubric: tech
title_ru: Поиск на Papers with Code теперь работает на собственной инфраструктуре Hugging Face
title_en: Papers with Code's search now runs on Hugging Face's own infrastructure
dek_ru: Hugging Face рассказала, как её Inference Endpoints, Jobs и Buckets обслуживают поиск на Papers with Code — вместо стороннего стека используется набор продуктов самой компании.
dek_en: Hugging Face explained how its Inference Endpoints, Jobs, and Buckets now serve search on Papers with Code — swapping a third-party stack for its own product lineup.
source: https://huggingface.co/blog/pwc-search
generated: true
---

## Русская версия

Hugging Face опубликовала пост о том, как её собственные продукты — [Inference Endpoints, Jobs и Buckets теперь обслуживают поиск на сайте Papers with Code](https://huggingface.co/blog/pwc-search). Автор поста, Нильс Рогге, описывает это как переезд поисковой функции сервиса на инфраструктуру самой компании вместо стороннего стека.

Papers with Code — площадка, которая связывает научные статьи с их кодом и результатами на бенчмарках; ей многие годы пользуются, чтобы быстро понять, чья реализация конкретного метода публична и как она соотносится с другими по метрикам. Поиск — одна из ключевых функций такой площадки: чем он быстрее и точнее, тем проще находить нужную статью среди тысяч.

Технически три продукта решают разные задачи: Inference Endpoints разворачивают модель как API без своей инфраструктуры, Jobs запускают разовые или периодические вычисления по расписанию, а Buckets — это хранилище файлов. Вместе они, судя по посту, закрывают весь путь от индексации контента до ответа на поисковый запрос.

Источник не приводит цифр — насколько вырос охват индекса, изменилась ли скорость ответа поиска или его стоимость по сравнению с прежним решением. Это скорее инженерный кейс о том, что компания использует собственные продукты для собственных же сервисов, чем новость с измеримым результатом.

### Почему это важно

Для самой Hugging Face это витрина: если Inference Endpoints, Jobs и Buckets достаточно надёжны для инфраструктуры Papers with Code, это косвенный аргумент в пользу того же стека для внешних разработчиков. Для пользователей Papers with Code изменение, скорее всего, останется незаметным, если только всё не заработало заметно хуже или лучше — судить об этом пока рано.

## English version

Hugging Face published a post explaining how its own products — [Inference Endpoints, Jobs, and Buckets now serve search on Papers with Code](https://huggingface.co/blog/pwc-search). Author Niels Rogge frames it as moving the site's search feature onto the company's own infrastructure instead of a third-party stack.

Papers with Code links academic papers to their code and benchmark results; it's long been a quick way to find a public implementation of a given method and see how it stacks up against others on the numbers. Search is one of the site's core functions — the faster and more precise it is, the easier it is to find the right paper among thousands.

Technically, the three products cover different jobs: Inference Endpoints deploy a model as an API without managing your own servers, Jobs run one-off or scheduled compute, and Buckets provide file storage. Together, per the post, they cover the whole path from indexing content to answering a search query.

The source doesn't give numbers — no figures on index coverage, response speed, or cost compared with the previous setup. It reads more as an engineering case study of a company running its own services on its own products than as news with a measurable outcome.

### Why it matters

For Hugging Face, this doubles as a showcase: if Inference Endpoints, Jobs, and Buckets are solid enough to run Papers with Code's infrastructure, that's an implicit pitch for the same stack to outside developers. For Papers with Code users, the change will likely go unnoticed unless something visibly gets faster, slower, better, or worse — too early to say which.
