---
date: 2026-09-05
rubric: tech
title_ru: «Оптимизируй окно контекста, остальное запомни» — ещё одна попытка приручить ИИ-агентов
title_en: "Optimize the context window. Persist everything else." — another attempt to tame AI coding agents
dek_ru: Репозиторий ECC обещает превратить хаотичного ИИ-агента в дисциплинированного инженера: план, тесты, ревью, память — 68 агентов и 286 навыков вместо одного длинного промпта.
dek_en: The ECC repository promises to turn a chaotic AI agent into a disciplined engineer: plan, test, review, memory — 68 agents and 286 skills instead of one long prompt.
source: https://github.com/affaan-m/ECC
generated: true
---

## Русская версия

Репозиторий [affaan-m/ECC](https://github.com/affaan-m/ECC) вошёл в топ трендов GitHub, прибавив 141 звезду за сутки и перевалив по счётчику за 248 тысяч. Проект описывает себя как «систему оптимизации производительности агентного харнесса» — то есть не отдельный ИИ-инструмент, а обвязку поверх Claude Code, Codex, Cursor, OpenCode, Gemini, Zed и других агентных сред.

Проблема, которую решают авторы, знакома всем, кто пробовал регулярно работать с кодогенерирующими агентами: агент неплохо пишет код в моменте, но у него нет согласованной инженерной системы вокруг — контекст теряется между сессиями, проверки качества выполняются от случая к случаю, а полезные паттерны, найденные вчера, сегодня приходится придумывать заново. ECC предлагает зашить в агента фиксированный рабочий цикл: план → тест → реализация → ревью → верификация → запоминание → улучшение — и устанавливать это один раз как часть того, как агент вообще работает, а не переписывать в каждом промпте заново.

Внутри — 68 специализированных под-агентов (планирование, ревью, безопасность, архитектура, доменные задачи) и 286 навыков, которые подгружаются по требованию: TDD, исследование, безопасность, документация, фронтенд, данные, ML, операции. Отдельно заявлен модуль AgentShield — сканирование промптов, хуков, конфигурации MCP, прав доступа и секретов на предмет проблем безопасности. Проект держит открытую лицензию MIT, а разработка финансируется через GitHub Sponsors и отдельное коммерческое приложение для приватных репозиториев.

### Почему это важно

Счётчики звёзд у подобных агентных фреймворков в GitHub-трендах в последнее время достигают величин, которые стоит воспринимать со здоровым скепсисом, — сотни тысяч звёзд для узкоспециализированного инструмента для разработчиков через несколько месяцев после запуска выглядят необычно на фоне куда более известных проектов с похожими цифрами, копившимися годами. Сама идея зашить в агента дисциплину — тесты, ревью, память между сессиями — не нова и решает реальную боль, но судить о том, работает ли конкретно эта реализация, стоит по опыту использования, а не по счётчику на странице репозитория.

## English version

The [affaan-m/ECC](https://github.com/affaan-m/ECC) repository landed on GitHub's trending page, adding 141 stars in a day and pushing its total star count past 248,000. The project describes itself as an "agent harness performance optimization system" — not a standalone AI tool, but a layer on top of Claude Code, Codex, Cursor, OpenCode, Gemini, Zed, and other agentic environments.

The problem the authors are solving is familiar to anyone who has worked with code-generating agents regularly: an agent can write decent code in the moment, but there's no coordinated engineering system around it — context gets lost between sessions, quality checks happen inconsistently, and useful patterns discovered yesterday have to be reinvented today. ECC bakes a fixed workflow into the agent instead: plan → test → implement → review → verify → remember → improve — installed once as part of how the agent works, rather than rebuilt in every prompt.

Under the hood are 68 specialized sub-agents (planning, review, security, architecture, domain-specific work) and 286 skills loaded on demand: TDD, research, security, documentation, frontend, data, ML, operations. A separate module called AgentShield is billed as scanning prompts, hooks, MCP configuration, permissions, and secrets for security issues. The project stays MIT-licensed and open-source, with development funded through GitHub Sponsors and a separate commercial app for private repositories.

### Why it matters

Star counts on agent-framework repos trending on GitHub lately reach numbers worth reading with real skepticism — hundreds of thousands of stars for a niche developer tool a few months after launch look unusual next to far better-known projects that took years to accumulate similar figures. Baking discipline into an agent — tests, review, memory across sessions — isn't a new idea and does address a real pain point, but whether this particular implementation actually delivers is something to judge from hands-on use, not from the counter on the repo's page.
