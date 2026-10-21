---
date: 2026-10-21
rubric: tech
title_ru: "Hugging Face описал нативную поддержку Google TPU через TorchTPU"
title_en: "Hugging Face details native Google TPU support through TorchTPU"
dek_ru: "Новый backend сохраняет интерфейсы PyTorch; доля успешных тестов и ускорение отдельных ядер требуют собственного контекста."
dek_en: "The backend preserves PyTorch interfaces, while reported test coverage and kernel speedups need their own context."
source: https://huggingface.co/blog/hf-torchtpu
generated: true
---

## Русская версия

Hugging Face [описал интеграцию TorchTPU](https://huggingface.co/blog/hf-torchtpu), нативного backend PyTorch для ускорителей Google TPU. Публикация датирована 20 октября. Transformers, Diffusers и библиотека Kernels получают путь к этим устройствам через привычные интерфейсы. Основное обещание касается программной совместимости: разработчику не нужно превращать модель в отдельный проект на другом фреймворке, чтобы начать проверять её на TPU.

Прежний путь для пользователей PyTorch шёл через PyTorch/XLA. В материале отмечены особенности отложенного выполнения и повторной компиляции, затруднявшие отладку. Optimum TPU помогал скрывать часть этой сложности. Теперь команда говорит, что эта дополнительная прослойка больше не требуется для работы моделей Hugging Face через Transformers и Diffusers. Это изменение маршрута интеграции, а не заявление об исчезновении всех ограничений оборудования.

TorchTPU представляет TPU как устройство `tpu`, поддерживает обычное немедленное выполнение, распределённую работу и `torch.compile`. В примере Transformers выбирается соответствующее размещение модели. В Diffusers сначала можно перенести конвейер на устройство для отладки, а затем отдельно включить компиляцию. Первая компилируемая генерация и повторный вызов с теми же размерами используют разные этапы работы, поэтому их нельзя без пояснений считать одинаковыми измерениями задержки.

В [первичном README проекта](https://github.com/google-pytorch/torch_tpu) перечислены реализации операций, кэш компиляции, примеры обучения и вывода и инструменты диагностики. Указана поддержка Python 3.11 и новее, а примеры ориентированы на виртуальную машину с TPU. Доступность исходников под Apache 2.0 позволяет изучить устройство backend, но не превращает обычный компьютер в TPU и не подтверждает совместимость каждой модели автоматически.

Команда Hugging Face сообщает о 96,5 процента успешных тестов среди тех, которые запускаются на TPU. Важно сохранить знаменатель: это не доля всех существующих моделей, гарантированно работающих без изменений. Ночные проверки и открытая публикация результатов ещё описаны как работа в процессе. Поиск ошибок при таком переходе — часть объявленного состояния интеграции, а не свидетельство уже законченного покрытия.

Есть и результаты отдельных оптимизированных ядер. Они относятся к определённым моделям, оборудованию и размеру пакета, а не к универсальному сравнению TPU со всеми другими ускорителями. Мы не переносим эти множители на произвольную задачу и не проводили собственный запуск. При выборе backend полезно отдельно измерить корректность, прогрев, устойчивую производительность и требования к памяти.

### Почему это важно

Ускоритель становится практичнее, когда разработчик может использовать знакомые библиотеки и инструменты отладки. TorchTPU расширяет такой выбор для PyTorch. Проверять нужно конкретный рабочий путь: наличие нативного интерфейса помогает начать, а измерения показывают, подходит ли он вашей нагрузке.

## English version

Hugging Face has [outlined its TorchTPU integration](https://huggingface.co/blog/hf-torchtpu), a native PyTorch backend for Google's TPU accelerators. The October 20 article describes familiar interfaces in Transformers, Diffusers and Kernels reaching the hardware. Its central proposition concerns software compatibility: developers can begin testing models on TPUs without turning them into separate projects written for another framework.

The earlier PyTorch route relied on PyTorch/XLA. The announcement discusses lazy execution and recompilation behaviour that could complicate debugging. Optimum TPU helped hide some of that complexity. Hugging Face now says this additional layer is no longer required to run its models through Transformers and Diffusers. That changes the integration path; it does not establish that every hardware constraint has disappeared.

TorchTPU exposes a `tpu` device, supports eager execution, distributed workloads and `torch.compile`. The Transformers example selects that device when loading a model. Diffusers users can move a pipeline to the device for debugging and separately enable compilation. The initial compiled generation and a later call with the same dimensions involve different stages of execution, so they should not be treated as interchangeable latency measurements.

The project's [primary README](https://github.com/google-pytorch/torch_tpu) lists operator implementations, a compilation cache, training and inference examples, and diagnostic utilities. It specifies Python 3.11 or later and describes examples running on a TPU virtual machine. Apache 2.0 source availability permits inspection of the backend. It neither supplies TPU hardware to an ordinary computer nor establishes automatic support for every model.

Hugging Face reports that 96.5% of tests running on TPU pass. Keeping the denominator attached matters: this is not a claim that 96.5% of all existing models work unchanged. Nightly testing and public results are described as work in progress. Discovering and fixing failures is part of the integration's announced state, rather than evidence that complete coverage has already been achieved.

The article also reports results for particular optimised kernels. Those belong to specified models, hardware and batch sizes, not a universal comparison between TPU and every other accelerator. We have not extrapolated their multipliers to arbitrary workloads or performed an independent run. Correctness, warmup behaviour, steady-state performance and memory requirements remain separate evaluation questions.

### Why it matters

An accelerator becomes more usable when developers retain familiar libraries and debugging tools. TorchTPU broadens that option for PyTorch users. Native interfaces provide a starting point; measurements on the actual workload determine whether that path is useful in practice.
