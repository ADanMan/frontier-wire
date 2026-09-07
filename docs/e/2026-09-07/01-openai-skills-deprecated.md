---
date: 2026-09-07
rubric: ai
title_ru: OpenAI закрывает каталог скиллов для Codex — как раз когда скилл-паки бьют рекорды на GitHub
title_en: OpenAI shuts down its Codex skills catalog just as third-party skill packs blow up on GitHub
dek_ru: Официальный репозиторий помечен «deprecated» и отправляет разработчиков к плагинам, а сторонний каталог маркетинговых скиллов тем временем собрал почти 400 звёзд за сутки.
dek_en: The official repo got tagged "deprecated" and redirected to plugins, while a third-party marketing-skills catalog picked up hundreds of stars in a single day.
source: https://github.com/openai/skills
generated: true
---

## Русская версия

В репозитории [openai/skills](https://github.com/openai/skills) — каталоге агентных скиллов для Codex — с сегодняшнего дня висит предупреждение: «Этот репозиторий устарел». Дальше в README прямая инструкция: идите в новый репозиторий [openai/plugins](https://github.com/openai/plugins) или используйте гайд по созданию плагинов, где объясняется, как оформить скилл в виде отдельного плагина.

Сама идея скиллов простая: папка с инструкциями, скриптами и ресурсами, которую агент может подключить и переиспользовать — «напиши один раз, используй везде». В Codex такие папки жили в трёх категориях: `.system` ставились автоматически вместе с последней версией Codex, `.curated` и `.experimental` — через команду `$skill-installer`. Теперь этот механизм сворачивается в пользу более широкой системы плагинов, где скилл — лишь один из компонентов пакета: рядом с ним могут идти MCP-серверы, конфигурации агентов, хуки и команды, упакованные в единый манифест `.codex-plugin/plugin.json`.

Забавно, что даже с пометкой «deprecated» репозиторий сегодня всё равно попал в топ трендов GitHub — с 44 новыми звёздами за сутки. Но настоящий рекорд дня поставил не он, а сторонний каталог [marketingskills](https://github.com/coreyhaines31/marketingskills) — коллекция скиллов для маркетологов (SEO, копирайтинг, CRO, реклама, аналитика), которую можно подключить к Claude Code, Codex, Cursor или Windsurf. За один день он собрал 355 звёзд — больше, чем любой другой репозиторий в сегодняшней подборке трендов.

Каталог формально бесплатный и лицензирован по MIT, но по сути это витрина. Автор Кори Хейнс встраивает в README ссылки на свои платные продукты — агентство Conversion Factory, курс по ИИ-маркетингу и автономного агента-«CMO» под названием Magister, — а часть работы над репозиторием финансируют «проверенные партнёры», сервисы Converly и Ploy. Если убрать хайп вокруг слова «скиллы», получится обычная воронка лидогенерации, просто упакованная в открытый исходный код.

Вывод простой: формат скиллов явно прижился как способ упаковки знаний для агентов, но пока индустрия спорит, где ему место — в официальном каталоге платформы или в системе плагинов, — открытые репозитории на GitHub продолжают расти сами по себе, независимо от того, что решит OpenAI.

### Почему это важно

Скиллы стали стандартным способом расширять ИИ-агентов без переобучения моделей, и то, куда крупные платформы решают их поместить — в основной продукт, в отдельную систему плагинов или вовсе списать в архив, — определяет, будет ли экосистема сторонних каталогов держаться на официальной поддержке или продолжит жить в диком поле GitHub, как сейчас.

## English version

The [openai/skills](https://github.com/openai/skills) repository — Codex's catalog of agent skills — now carries a banner: "This repository is deprecated." The README points straight to the new [openai/plugins](https://github.com/openai/plugins) repo, or to the plugin-building guide that explains how to package a skill as a standalone plugin instead.

The idea behind skills is simple: a folder of instructions, scripts, and resources an agent can pick up and reuse — "write once, use everywhere." In Codex, these folders lived in three tiers: `.system` skills installed automatically with the latest Codex release, while `.curated` and `.experimental` ones went in through the `$skill-installer` command. That model is now folding into a broader plugin system, where a skill is just one piece of a bundle that can also include MCP servers, agent configs, hooks, and commands, all wrapped in a single `.codex-plugin/plugin.json` manifest.

Oddly enough, even tagged deprecated, the repo still landed on GitHub's trending list today, picking up 44 new stars. But the real record of the day went to a different catalog: [marketingskills](https://github.com/coreyhaines31/marketingskills), a collection of skills for marketers — SEO, copywriting, CRO, ads, analytics — built for Claude Code, Codex, Cursor, and Windsurf. It gained 355 stars in a single day, more than any other repo in today's trending roundup.

The catalog is free and MIT-licensed, but it's also a funnel. Creator Corey Haines links his README to paid products: his Conversion Factory agency, an AI-marketing course, and an autonomous "CMO" agent called Magister, with "verified partners" Converly and Ploy helping fund the project. Strip away the word "skills" and what's left is a fairly ordinary lead-generation setup, just shipped as open source.

The takeaway: skills have clearly stuck as a format for packaging knowledge into agents, but while the industry argues over where they belong — a platform's official catalog or a broader plugin system — open repos on GitHub keep growing on their own, regardless of what OpenAI decides.

### Why it matters

Skills have become the default way to extend AI agents without retraining models, and where the big platforms choose to put them — folded into the core product, spun into a separate plugin system, or shelved entirely — decides whether the ecosystem of third-party catalogs rides on official support or keeps living wild on GitHub, the way it does today.
