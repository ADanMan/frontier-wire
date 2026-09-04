---
date: 2026-09-04
rubric: ai
title_ru: DeepSeek выкатила свой agent-фреймворк — и сразу с 211 тысячами звёзд
title_en: DeepSeek ships its own agent framework — and it already has 211,000 stars
dek_ru: DeepSeek Harness построен по принципу «всё — плагин»: за сутки проект набрал больше полутора тысяч новых звёзд на GitHub.
dek_en: DeepSeek Harness is built on an "everything is a plugin" principle and gained over 1,500 new GitHub stars in a single day.
source: https://github.com/deepseek-ai/deepseek-harness
generated: true
---

## Русская версия

DeepSeek выпустила [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) — открытый фреймворк для ИИ-агентов, построенный на архитектуре «всё — это плагин» поверх внутреннего движка Cordis. За последние сутки репозиторий прибавил 1 521 звезду и перевалил за 210 тысяч — сейчас у проекта 211,3 тысячи звёзд, 24,7 тысячи форков и почти 15 тысяч коммитов в основной ветке.

Идея фреймворка простая: вместо монолитного агента с зашитой логикой — ядро плюс экосистема плагинов, которые можно ставить, комбинировать и публиковать под тегом `dsh-plugin`. Поставить и запустить можно одной командой (`npx @deepseek-ai/dsh web`), после чего открывается веб-интерфейс на локальном порту. Проект пока в статусе developer preview: авторы честно предупреждают, что архитектура может меняться и обратная совместимость не гарантирована.

Лицензия — MIT, что для DeepSeek уже привычная практика: компания системно публикует свои инструменты как открытый код, в отличие от многих конкурентов, которые держат agent-обвязку внутри закрытых продуктов. На фоне того, что в последние дни в трендах GitHub одновременно оказались несколько репозиториев про «навыки» и «плагины» для агентов, выход харнесса от DeepSeek — ещё один сигнал, что крупные лаборатории делают ставку не столько на саму модель, сколько на архитектуру вокруг неё.

### Почему это важно

Когда модель одна и та же (или почти одна), конкуренция смещается в обвязку: кто предложит агенту более удобную, расширяемую и открытую платформу. DeepSeek с её историей открытых релизов имеет здесь фору — и почти четверть миллиона звёзд за короткое время показывают, что спрос на такую инфраструктуру уже есть, а не только предполагается.

## English version

DeepSeek has released [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`), an open-source agent framework built on an "everything is a plugin" architecture running on its internal Cordis engine. The repository gained 1,521 stars in the last 24 hours alone, crossing 210,000 — it now sits at 211,300 stars, 24,700 forks, and nearly 15,000 commits on its main branch.

The pitch is simple: instead of a monolithic agent with hardcoded logic, there's a core plus an ecosystem of plugins that can be installed, combined, and published under the `dsh-plugin` tag. Getting started takes one command (`npx @deepseek-ai/dsh web`), which opens a web UI on a local port. The project is still labeled developer preview, and the maintainers are upfront that the architecture may change with breaking updates.

It ships under the MIT license, consistent with DeepSeek's pattern of releasing tools as open source rather than keeping agent tooling locked inside closed products, unlike many competitors. The timing lines up with several other "skills" and "plugin" repositories for agents trending on GitHub the same week — another sign that major labs are competing less on the model itself and more on the scaffolding built around it.

### Why it matters

When the underlying model is roughly the same across labs, competition shifts to tooling: whoever offers agents a more flexible, extensible, open platform wins developer mindshare. DeepSeek's track record of open releases gives it an edge here, and gaining a quarter-million stars this fast shows the demand for that kind of infrastructure is already real, not just theoretical.
