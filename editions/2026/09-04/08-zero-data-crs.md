---
date: 2026-09-04
rubric: science
title_ru: Можно ли научить рекомендательного бота вести диалог без единого примера диалога
title_en: Can you teach a recommendation bot to hold a conversation without a single example dialogue
dek_ru: Новое исследование систематически проверяет, работают ли диалоговые рекомендательные системы в доменах, где нет ни одного размеченного диалога для обучения.
dek_en: A new study systematically tests whether conversational recommender systems can work in domains with zero labeled training dialogues.
source: https://huggingface.co/papers/2504.15476
generated: true
---

## Русская версия

Диалоговые рекомендательные системы (CRS) — это боты, которые не просто выдают список товаров или фильмов по запросу, а ведут с пользователем разговор, уточняя вкусы и сужая выбор. Проблема в том, что обучить такого бота обычно можно только на специально размеченных диалогах для конкретного домена — а такие данные дорогие, редкие и почти никогда не существуют для новой предметной области. Команда авторов — Рохан Сурана, Джунда Ву, Чжоуханг Се, Ю Ся, Натан Каллус и другие — опубликовала работу [«An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Systems»](https://huggingface.co/papers/2504.15476), где систематически проверяют, насколько CRS вообще способны работать без единого обучающего диалога, полагаясь только на существующие возможности больших языковых моделей.

Сама постановка вопроса важна для практики: компании, которые хотят запустить диалогового рекомендателя в новой нише — от подбора вина до подбора репетитора, — сегодня либо тратятся на разметку данных с нуля, либо просто отказываются от идеи. Авторы систематически исследуют, где именно в этой цепочке (понимание запроса, уточняющие вопросы, финальная рекомендация) zero-data подход справляется, а где начинает давать сбои. Конкретных цифр по итоговому качеству в доступном описании работы авторы не приводят — это скорее картирование проблемы, чем готовый рецепт с гарантированным приростом метрик.

Такие эмпирические работы редко попадают в заголовки, но именно они определяют, стоит ли бизнесу вообще пытаться разворачивать CRS без разметки — или проще подождать, пока появится более зрелый метод.

### Почему это важно

Если окажется, что диалоговые рекомендатели действительно можно бутстрапить без данных, это резко снижает порог входа для маленьких компаний и нишевых сервисов — не нужно будет нанимать разметчиков и собирать тысячи диалогов, чтобы запустить работающего рекомендательного бота.

## English version

Conversational recommender systems (CRS) are bots that don't just spit out a list of products or movies on request — they hold an actual conversation, asking clarifying questions and narrowing down preferences. The catch is that training one usually requires domain-specific labeled dialogue data, which is expensive, scarce, and almost never exists for a brand-new domain. A team of researchers — Rohan Surana, Junda Wu, Zhouhang Xie, Yu Xia, Nathan Kallus, and others — published [«An Empirical Study on Zero-Data Bootstrapping for Conversational Recommender Systems»](https://huggingface.co/papers/2504.15476), systematically testing how far CRS can go with zero training dialogues, relying only on what large language models already know.

The question matters in practice: a company that wants to launch a conversational recommender in a new niche — wine pairing, tutor matching, whatever it is — today either pays to build a labeled dataset from scratch or drops the idea. The authors map out, step by step (query understanding, clarifying questions, the final recommendation), exactly where a zero-data approach holds up and where it breaks down. The available description of the work doesn't give final quality numbers — this reads as a systematic mapping of the problem rather than a recipe with guaranteed metric gains.

Empirical studies like this rarely make headlines, but they're exactly what determines whether a business should even attempt a data-free CRS deployment or wait for a more mature method to show up.

### Why it matters

If conversational recommenders really can be bootstrapped without training data, that sharply lowers the barrier to entry for small companies and niche services — no need to hire annotators and collect thousands of dialogues just to get a working recommendation bot off the ground.
