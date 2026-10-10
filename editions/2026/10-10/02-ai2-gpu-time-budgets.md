---
date: 2026-10-10
rubric: ai
title_ru: Ai2 распределяет GPU по бюджетам времени и сообщает о сокращении очередей
title_en: Ai2 allocates GPU time through budgets and reports shorter queues
dek_ru: Внутренний отчёт разделяет занятость оборудования, долю времени команды и пользу вычислений; результаты относятся к конкретному внедрению.
dek_en: An internal report distinguishes hardware occupancy, team allocations and useful computation, with results tied to its own deployment.
source: https://huggingface.co/blog/allenai/impactful-scheduling
generated: true
---

## Русская версия

Институт Ai2 [описал новую систему распределения GPU](https://huggingface.co/blog/allenai/impactful-scheduling) в отчёте от 9 октября. Вместо борьбы за постоянно повышаемый приоритет исследовательские команды получают бюджеты вычислительного времени. Планировщик учитывает, какую долю уже использовала каждая команда, и перераспределяет доступную мощность. Это рассказ о внедрении внутри института, а не независимый тест универсального продукта. При этом он показывает, как организационные правила могут менять доступ к тем же ускорителям без покупки нового оборудования.

В прежней системе, по объяснению Ai2, приоритет со временем переставал различать задания: все выбирали высокий. Отдельные постоянные квоты тоже создавали проблему — одна команда могла не готовить эксперименты, пока другая ждала свободной мощности. Новый подход распределяет долю GPU-времени, а не навсегда закрепляет конкретные карты. Бюджеты задаются иерархически, от исследовательских программ до проектов. Это внутренний учёт ресурса; речь не о денежной оплате каждого задания через публичный сервис.

Планировщик смотрит на использование долей в скользящем окне, по умолчанию за семь дней. Задания недополучивших время групп поднимаются выше заданий групп, уже превысивших свою долю. При этом свободные мощности можно занимать работой вне бюджета, которую разрешено прервать при появлении оплаченного долей запроса. Так система соединяет распределение по договорённости с возможностью использовать простаивающее оборудование. Постоянная занятость и соблюдение выделенных долей становятся отдельными проверяемыми свойствами.

Ещё один элемент — минимальное время работы задания. Пока оно не прошло, задача защищена от прерывания; затем её можно поставить обратно в очередь, если она умеет возобновляться. Для этого окна выбран максимальный предел восемь часов. Такой договор даёт место перераспределению длинных задач и обслуживанию неисправных узлов. Сама возможность остановить работу, однако, не делает восстановление бесплатным: нужна сохранённая точка продолжения и понятное поведение приложения после возвращения в очередь.

В тридцатидневном измерении Ai2 сообщает о предоставлении 98% причитающихся командам GPU-часов, а занятость кластера оставалась 98% до и после перехода. Для коротких отладочных задач наблюдаемый p90 ожидания уменьшился с двух часов до тридцати секунд. Авторы отдельно отличают эти значения от симуляции и предупреждают о меньшей исходной выборке отладочных запусков. Не всё улучшилось: прерывания мешали интерактивным сессиям с несохранённым состоянием. Восстанавливаемые сессии и отдельный CPU-кластер описаны как дальнейшие планы.

### Почему это важно

Высокая занятость GPU ещё не доказывает, что нужная работа получила время или использовала его эффективно. Ai2 разделяет эти вопросы и показывает результаты вместе с ограничениями. Для оценки инфраструктуры полезно смотреть не только на количество карт, но и на ожидание, доли проектов и стоимость возобновления. Отчёт описывает один практический вариант такого учёта; гарантировать те же показатели другой организации без её нагрузок и проверки нельзя.

## English version

Ai2 [described a new GPU allocation system](https://huggingface.co/blog/allenai/impactful-scheduling) in an October 9 report. Research teams receive compute-time budgets instead of competing through ever-higher job priorities. The scheduler considers how much of each allocation has already been used and redistributes available capacity. This is an account of the institute's own deployment, rather than an independent evaluation of a universal product. It shows how organizational rules can change access to existing accelerators without purchasing more hardware.

Under the previous system, Ai2 says priority eventually stopped distinguishing workloads because everyone selected the high setting. Permanent concurrent quotas created another problem: one team could have no experiments ready while another waited. The replacement allocates a share of GPU time, rather than permanently assigning particular devices. Budgets follow a hierarchy from research programs to projects. This is internal resource accounting, rather than payment for individual jobs through a public service.

The scheduler tracks allocation use over a sliding window, seven days by default. Work from under-served groups ranks above requests from groups that have exceeded their share. Idle capacity can also run unbudgeted work that is interruptible when an allocated request arrives. That connects agreed resource distribution with the ability to use otherwise idle hardware. Keeping the cluster occupied and delivering the promised shares become separate properties to evaluate.

A further element is each job's declared minimum runtime. The job is protected from interruption during that period, then may be requeued if it can resume. Ai2 chose an eight-hour maximum for this window. The agreement creates opportunities to rebalance long workloads and drain unhealthy hosts for maintenance. Being able to stop work does not make recovery free, however: applications still need saved progress and a defined way to continue after returning to the queue.

In a thirty-day measurement, Ai2 reports delivering 98% of the GPU hours owed to teams, while cluster occupancy remained at 98% before and after the change. Observed p90 queue time for short debugging jobs fell from two hours to thirty seconds. The authors distinguish those measurements from simulation results and note that the baseline debugging sample was smaller. Not every use case improved: interruptions disrupted interactive sessions with volatile state. Restorable sessions and a separate CPU cluster are described as future work.

### Why it matters

High GPU occupancy does not establish that important workloads received their share or used it efficiently. Ai2 separates those questions and reports outcomes together with limitations. Infrastructure assessment can look beyond device counts to queue times, project allocations and the cost of resuming work. This report presents one practical implementation of that accounting. Matching its figures elsewhere would require checking the other organization's workloads and behavior, rather than assuming the same policy produces identical results.
