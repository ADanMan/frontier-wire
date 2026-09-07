---
date: 2026-09-07
rubric: science
title_ru: Учёным сделали «домашнюю лабораторию» для ИИ-агентов — теперь со Slurm и менеджером литературы
title_en: Scientists get a local AI research workbench — now with Slurm clusters and a reference library
dek_ru: Open Science обновился до версии 0.26.0: поддержка HPC-кластеров, менеджер научной литературы и 22 готовых скилла вроде AlphaFold2 и DiffDock.
dek_en: Open Science just shipped version 0.26.0, adding HPC cluster support, a literature manager, and 22 ready-made skills like AlphaFold2 and DiffDock.
source: https://github.com/aipoch/open-science
generated: true
---

## Русская версия

Открытый проект [Open Science](https://github.com/aipoch/open-science) от команды AIPOCH называет себя «домашней лабораторией» для учёных: локальное, model-agnostic приложение, где ИИ-агент читает файлы, ищет в вебе, запускает код на Python и R и обращается к научным базам данных, а результат остаётся с полной историей происхождения. Проект бесплатный, лицензирован по Apache 2.0 и работает на macOS, Windows и Linux. Сегодня он попал в тренды GitHub, набрав 145 звёзд за сутки.

Повод — свежий релиз v0.26.0 (вышел в сентябре 2026-го). Главные новые вещи две. Первая — «HPC-класс вычислений»: теперь можно подключать удалённые вычислительные хосты не только по прямому SSH, но и через персональный режим выполнения на Slurm, то есть отправлять задачи в очередь настоящего кластера. Вторая — менеджер литературы: библиотека ссылок с импортом по DOI, PubMed ID или arXiv ID, автоматическим поиском полнотекстовых PDF через открытые источники (Europe PMC, PMC, OpenAlex, arXiv, Unpaywall), склейкой дублей и форматированием цитат. В этом же релизе среди провайдеров моделей появился Apodex — рядом с последними моделями OpenAI и Anthropic.

Внутри — 22 готовых научных скилла: свёртка белков (AlphaFold2, ESMFold2, OpenFold3, Boltz, Chai-1), докинг лигандов (DiffDock, LigandMPNN, SolubleMPNN, ProteinMPNN), геномика одной клетки (scGPT, scvi-tools) и работа с текстом самой науки — обзор литературы, «рассказ» о статье, компоновка рисунков. К ним прилагаются 24 встроенных коннектора к базам данных: PubMed, bioRxiv, ChEMBL, ZINC, реестр клинических испытаний и ещё два десятка источников — каждый под отдельным разрешением («всегда разрешать», «спрашивать каждый раз», «блокировать»).

Отдельно авторы гордятся результатом на бенчмарке BiomniBench-DA: в подкатегории Public 50 проект помечен как занимающий первое место. У проекта даже есть DOI через Zenodo — редкая деталь для GitHub-репозитория, которая явно нацелена на то, чтобы его можно было цитировать в статьях наравне с другими инструментами.

Самое интересное решение — как проект обращается с недостающими данными. Каждый сгенерированный агентом артефакт хранится как неизменяемая, проверенная контрольной суммой версия, а во вкладке «Provenance» видно, на основе какого кода, каких входных файлов и в каком окружении он получен. Если что-то из этой цепочки не удалось восстановить, интерфейс так и пишет — «недоступно», а не додумывает историю от себя. Для инструмента, который претендует на роль лабораторного журнала для ИИ-агентов, это едва ли не более важная деталь, чем список подключённых баз данных.

### Почему это важно

Научные лаборатории годами боролись за воспроизводимость экспериментов ещё до появления ИИ-агентов, а с ними эта задача только усложнилась: агент может запустить код, обратиться к базе данных и сгенерировать график за секунды, но без честной записи, откуда что взялось, результату нельзя доверять. Инструменты вроде Open Science пытаются встроить эту дисциплину в сам рабочий процесс, а не оставлять её на совесть исследователя.

## English version

The open-source [Open Science](https://github.com/aipoch/open-science) project from the AIPOCH team bills itself as a local "home lab" for researchers: a model-agnostic desktop app where an AI agent reads files, searches the web, runs Python and R code, and queries scientific databases, with every result kept alongside a full record of how it was produced. It's free, Apache 2.0-licensed, and runs on macOS, Windows, and Linux. It landed on GitHub's trending list today, picking up 145 stars in a single day.

The trigger is a fresh release, v0.26.0, shipped in September 2026. Two additions stand out. First, "HPC-class compute": remote compute hosts can now be reached not just over direct SSH but through a per-host Slurm execution mode, meaning jobs can be submitted straight to a real cluster's queue. Second, a literature manager: a reference library that imports by DOI, PubMed ID, or arXiv ID, automatically finds open-access full-text PDFs across Europe PMC, PMC, OpenAlex, arXiv, and Unpaywall, merges duplicate records, and formats citations. The same release adds Apodex as a model provider alongside the latest OpenAI and Anthropic models.

Under the hood sit 22 ready-made scientific skills: protein folding (AlphaFold2, ESMFold2, OpenFold3, Boltz, Chai-1), ligand docking (DiffDock, LigandMPNN, SolubleMPNN, ProteinMPNN), single-cell genomics (scGPT, scvi-tools), and tools for the writing side of science, like literature review and figure composition. Alongside them are 24 built-in data connectors — PubMed, bioRxiv, ChEMBL, ZINC, a clinical-trials registry, and about twenty more sources — each gated by its own permission setting ("always allow," "ask each time," or "block").

The project also flags a benchmark result: it claims the top spot in the Public 50 category of the BiomniBench-DA leaderboard. It even carries a Zenodo DOI, an unusual touch for a GitHub repo, clearly meant to make it citable in papers the same way any other research tool would be.

The more telling design choice is how it handles missing information. Every artifact an agent generates is stored as an immutable, checksummed version, and a "Provenance" tab shows the code, input files, and environment behind it. When part of that chain can't be verified, the interface says so — "unavailable" — instead of guessing. For a tool positioning itself as a lab notebook for AI agents, that may matter more than the length of its connector list.

### Why it matters

Scientific labs struggled with reproducibility long before AI agents arrived, and agents make the problem sharper: one can run code, query a database, and generate a chart in seconds, but the result is only as trustworthy as the record of where it came from. Tools like Open Science try to build that discipline into the workflow itself, rather than leaving it to a researcher's memory.
