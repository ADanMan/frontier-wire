---
date: 2026-09-04
rubric: ai
title_ru: Судьи для ИИ-агентов сами не проходили экзамен
title_en: The judges grading AI agents haven't been graded themselves
dek_ru: Новый бенчмарк AgentJudgeBench проверяет, насколько можно доверять языковым моделям, которые оценивают работу других агентов.
dek_en: A new benchmark called AgentJudgeBench tests how much you can actually trust the LLMs that grade other AI agents.
source: https://huggingface.co/papers/2608.26623
generated: true
---

## Русская версия

Абхигья Верма, Амит Кумар Саха, Сегнарасан Субраманиан и Сай Харшита Алуру опубликовали работу [«AgentJudgeBench»](https://huggingface.co/papers/2608.26623) — первый, по их словам, бенчмарк, который проверяет надёжность LLM-«судей» на структурированных, зависимых друг от друга агентных задачах разной сложности.

Суть проблемы в том, что LLM-судьи давно и широко используются для оценки агентных систем с вызовом инструментов — по сути, одна модель проверяет работу другой вместо дорогой и медленной ручной разметки. Но насколько эти судьи вообще надёжны на реалистичных, «многошаговых» сценариях, где один вызов инструмента зависит от результата предыдущего, авторы называют largely unexamined — то есть почти не изученным вопросом. Это довольно неудобное признание для целой индустрии, которая уже встроила автоматических судей в свои процессы оценки.

AgentJudgeBench устроен как набор задач разной сложности специально для того, чтобы найти границу, на которой судьи-модели начинают ошибаться. Дигест не раскрывает конкретных цифр точности из работы — но сама постановка вопроса важнее любого отдельного числа: индустрия строит целые пайплайны оценки на инструменте, чью надёжность на сложных сценариях до сих пор толком не проверяли.

### Почему это важно

Если методология «одна модель судит другую» станет стандартом контроля качества для агентных систем, тем важнее знать, где она даёт сбой. Бенчмарк, который честно ищет слепые пятна LLM-судей, — не менее ценен, чем очередная модель с рекордом на лидерборде.

## English version

Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, and Sai Harshitha Aluru published [the "AgentJudgeBench" paper](https://huggingface.co/papers/2608.26623), describing what they call the first benchmark testing how reliable LLM judges are on structured, dependency-driven agentic tasks across multiple difficulty levels.

The problem is that LLM judges are already widely used to evaluate agentic tool-calling systems — one model checking another's work, instead of slow and expensive manual review. But how reliable those judges actually are on realistic, multi-step scenarios, where one tool call depends on the result of the last, is what the authors describe as "largely unexamined." That's an uncomfortable admission for an industry that has already built automatic judging into its evaluation pipelines.

AgentJudgeBench is structured as a set of tasks spanning difficulty levels specifically to find where judge models start getting things wrong. The available material doesn't include the paper's actual accuracy numbers, but the framing matters more than any single figure: the industry is building whole evaluation pipelines on a tool whose reliability on hard, structured scenarios hadn't really been tested until now.

### Why it matters

If "one model judges another" becomes the standard quality check for agentic systems, it matters a lot where that check breaks down. A benchmark that honestly hunts for the blind spots of LLM judges is worth as much attention as another model topping a leaderboard.
