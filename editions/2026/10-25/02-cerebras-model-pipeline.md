---
date: 2026-10-25
rubric: tech
title_ru: "Cerebras объяснила, как раскладывает большую модель по цепочке вычислительных пластин"
title_en: "Cerebras explains a wafer pipeline for large-model inference"
dek_ru: "Иллюстративный расчёт для Kimi K3 связывает размещение весов, кэш запросов и число одновременно обслуживаемых пользователей."
dek_en: "An illustrative Kimi K3 calculation connects weight placement, request-state memory and concurrency."
source: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras
generated: true
---

## Русская версия

Cerebras [опубликовала инженерный разбор размещения крупных моделей](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) на своих wafer-scale ускорителях. Материал датирован 22 октября. Главный вопрос простой: как поместить веса триллионного масштаба в систему, если на одной пластине WSE-3T доступно 44 гигабайта встроенной памяти? Ответ компании — распределить модель по нескольким пластинам и организовать прохождение промежуточных результатов через последовательность стадий.

Иллюстрацией служит Kimi K3, а не вчерашняя K3.1 Pro. Для расчёта приняты четыре бита на вес, восьмибитный KV-кэш и средний запрос на 256 тысяч токенов. Это исходные допущения примера, не универсальные параметры каждого развёртывания. При изменении точности хранения, длины контекста или устройства модели меняются и требования к памяти, поэтому итоговое число ускорителей нельзя переносить на произвольный сервис.

В упрощённой раскладке авторы оценивают слой примерно в 16 гигабайт. На пластине с полным вниманием оставляют один слой и место под KV-кэш запросов. Для слоёв линейного внимания используется другое состояние, не растущее таким же образом с длиной контекста; в примере помещают два слоя на пластину. Из 69 линейных и 24 остальных слоёв получается иллюстративная конфигурация на 59 пластинах. Она объясняет ход расчёта, а не является независимым аудитом готовой установки.

После размещения весов между стадиями передаются активации — промежуточные результаты вычисления. Веса соответствующих слоёв остаются на своих местах. Это похоже на последовательность рабочих постов: один запрос проходит дальше, но каждый пост может одновременно заниматься другим запросом. Поэтому последовательное устройство модели не означает, что вся система обязательно ждёт завершения единственного пользователя.

Каждая стадия может обрабатывать и небольшую группу запросов. При меньших группах приоритетом становится скорость отдельного ответа; увеличение группы помогает суммарной пропускной способности. Одновременно каждый активный запрос требует собственного состояния на пластинах с полным вниманием. Свободная память под такой кэш ограничивает число запросов в работе, даже если вычислительные стадии способны принимать больше задач.

Компания отдельно подчёркивает, что конкурентность и размер группы не исчерпывают оценку эффективности. Сравнивать нужно и общий выпуск токенов, энергопотребление и скорость отдельного потока при сопоставимых условиях. Мы не проводили испытаний и не превращаем заявленные поставщиком скорости в общий рейтинг ускорителей. Полезный результат публикации — возможность увидеть, какие именно допущения стоят за рассказом о большой модели на маленькой относительно её весов памяти одного чипа.

### Почему это важно

Размер модели сам по себе не говорит, как устроен обслуживающий её кластер. Разбор связывает память весов, память состояния и движение данных. Это помогает задавать более точные вопросы о задержке и нагрузке вместо сравнения систем по одному эффектному числу токенов в секунду.

## English version

Cerebras has [published an engineering explanation of large-model deployment](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras) on wafer-scale accelerators. Dated October 22, it addresses a basic question: how can trillion-scale model weights fit into a system whose individual WSE-3T wafer contains 44 GB of on-chip memory? The company's answer distributes layers across wafers and passes intermediate results through a pipeline.

The illustrative model is Kimi K3, rather than the newly announced K3.1 Pro. The calculation assumes four-bit weights, an eight-bit KV cache and an average 256,000-token request. Those are example assumptions, not universal deployment settings. Storage precision, context length and model architecture change the memory requirements, so the resulting accelerator count cannot simply be applied to an arbitrary service.

The simplified mapping estimates approximately 16 GB per layer. A wafer with a full-attention layer reserves additional space for request KV caches. Linear-attention layers use a different state that does not grow in the same way with context length; the example places two such layers on a wafer. With 69 linear-attention and 24 remaining layers, the illustration yields 59 wafers. It explains the calculation rather than providing an independent audit of an operating installation.

Once weights are placed, activations travel between stages while the corresponding layer weights remain resident. Think of successive workstations: a request advances, but each station can simultaneously process another request. A sequential model therefore does not require the entire system to wait for one user to finish before another begins.

Each stage can also process a small group of requests. Smaller groups prioritise individual response speed, while larger ones can improve aggregate throughput. Meanwhile, every active request needs its own state on full-attention wafers. The memory available for that cache limits concurrency even when compute stages could accept more work.

The company notes that concurrency and group size do not fully describe efficiency. Aggregate token output, power consumption and individual stream speed must be considered under comparable conditions. We have not tested the system or converted supplier-reported speeds into a universal accelerator ranking. The useful contribution is making assumptions visible behind the account of a model much larger than one chip's memory.

### Why it matters

Model size alone does not explain the cluster serving it. This account connects weight storage, request-state memory and data movement. Those distinctions support more useful questions about latency and load than comparing systems through one striking tokens-per-second figure.
