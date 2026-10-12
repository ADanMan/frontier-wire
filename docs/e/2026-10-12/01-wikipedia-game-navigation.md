---
date: 2026-10-12
rubric: ai
title_ru: "Исследователи проверили навигацию ИИ по Wikipedia: добраться до цели и выбрать короткий путь — разные результаты"
title_en: "A Wikipedia navigation study separates reaching the target from finding a short route"
dek_ru: "В препринте от 9 октября сравнили языковые модели, эмбеддинги и человеческие попытки с разными ограничениями."
dek_en: "An October 9 preprint compares language models, embeddings and human attempts under different constraints."
source: https://arxiv.org/html/2610.13948v1
generated: true
---

## Русская версия

В [препринте от 9 октября](https://arxiv.org/html/2610.13948v1) исследователи Института Алана Тьюринга использовали Wikipedia Game для проверки навигации языковых моделей. Нужно перейти от начальной статьи к заданной, выбирая доступные ссылки. По отчёту авторов, лучшие из испытанных моделей приблизились к человеческой доле успехов в английской Wikipedia, но делали больше переходов. Это результат конкретного набора экспериментов, не рейтинг всех современных моделей.

Авторы [опубликовали код](https://github.com/alan-turing-institute/ARC-Wiki-Game) для подготовки графов Wikipedia и OpenAlex, запуска агентов и анализа результатов. В такой постановке можно проверить маршрут по локальному набору данных. Ответ в виде правдоподобного объяснения не заменяет достижение целевой вершины: выбранные переходы должны существовать в подготовленном графе.

Важная оговорка к человеческому сравнению: участвовали девять игроков, сообщившие о 109 попытках. Им давали десять минут; модельный успех ограничивали ста переходами. Условия не являются одинаковыми. Поэтому из сопоставимой доли успехов нельзя вывести равенство скорости, вычислительной цены или способности искать информацию вообще. Испытания также охватывали определённые модели, включая GPT-4o и более ранние открытые семейства, а не весь актуальный рынок.

Редакционный интерес — в различии между похожестью и полезностью следующего шага. Представьте мысленный маршрут от статьи о музыкальном инструменте к статье о редком материале. Ссылка, название которой больше всего похоже на конечную цель, может увести в тупик. Более общая страница иногда окажется мостом. Но это нужно проверить по доступным переходам; красивое рассуждение само не создаст нужной связи.

Такую игру удобно читать как ограниченную модель поиска. Вы знаете конечную цель и видите лишь ближайшие возможности. Это помогает обсуждать качество выбора шага отдельно от способности пересказать прочитанный текст. При этом решение задачи не доказывает, что агент умеет оценивать достоверность содержания страницы. Добраться до документа и убедиться в истинности его утверждений — разные проверки.

Для оценки рабочего инструмента мы бы сначала зафиксировали условия: какие документы доступны, что считается целью, какие действия разрешены и как измеряется затрата ресурса. Затем отдельно считали бы завершённые задания, длину маршрута и обращения к модели. Если оставить только процент побед, различия между быстрым путём и долгим блужданием потеряются.

### Почему это важно

Работа предлагает наблюдаемый результат для проверки поиска: маршрут, который можно воспроизвести. Практический вывод — выбирать критерий под свою задачу и сравнивать системы при понятных ограничениях. Совпадение одного показателя полезно, но не превращает небольшой эксперимент в доказательство универсального равенства человека и ИИ.

## English version

An [October 9 preprint](https://arxiv.org/html/2610.13948v1) from Alan Turing Institute researchers uses the Wikipedia Game to evaluate language-model navigation. Players must reach a target article by selecting available links. The authors report that the best tested models approached human success rates on English Wikipedia, while taking more steps. This is a finding from a particular set of experiments, rather than a ranking of every current model.

The authors also [released code](https://github.com/alan-turing-institute/ARC-Wiki-Game) for preparing Wikipedia and OpenAlex graphs, running agents and analyzing results. This setup makes a route checkable against a local dataset. A plausible explanation cannot substitute for reaching the target node: the chosen transitions have to exist in the prepared graph.

The human comparison needs qualification. Nine players self-reported 109 attempts, with a ten-minute allowance; model success was bounded by one hundred transitions. These are different constraints. Comparable success rates therefore cannot establish equal speed, computational cost or general information-retrieval ability. The experiments also cover a defined selection, including GPT-4o and earlier open model families, rather than the entire present market.

Our editorial interest concerns the difference between a similar-looking next step and a useful one. Imagine a hypothetical route from an article about a musical instrument to an article about a rare material. The link whose title most closely resembles the destination could lead into a dead end. A broader page might provide a bridge. That possibility must be checked against available transitions; an elegant explanation cannot create a missing connection.

The game is useful as a constrained model of search. The destination is known, but only nearby choices are visible. This lets researchers discuss the quality of the next move separately from the ability to summarize text. Completing the route does not establish that an agent can judge a page's reliability. Reaching a document and verifying the truth of its contents require separate evaluations.

For a working tool, we would first specify which documents are available, what counts as the destination, which actions are allowed and how resource use is measured. We would then track completion, route length and model requests separately. A win percentage alone loses the distinction between a direct path and a long series of detours. The comparison becomes more informative when that distinction stays visible rather than being compressed into one headline.

### Why it matters

The study offers an observable search result: a route that can be reproduced. The practical lesson is to choose criteria for the actual task and compare systems under explicit constraints. Agreement on one measure is useful, but it cannot turn a small experiment into evidence of universal equivalence between humans and AI.
