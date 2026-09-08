---
date: 2026-09-08
rubric: ai
title_ru: Аватар, который говорит и одновременно двигается: одна модель вместо двух
title_en: An avatar that talks and moves at once — from one model, not two
dek_ru: Новая работа Motion-Omni объединяет генерацию речи и движений всего тела говорящего аватара в единую модель — раньше эти задачи решались раздельными системами.
dek_en: A new paper called Motion-Omni merges speech generation and full-body motion for a talking avatar into a single model — a job previously split across separate systems.
source: https://huggingface.co/papers/2609.04250
generated: true
---

## Русская версия

Авторы Чэнцянь Ма, Вэй Тао, Хаою Чжан и Ивэнь Го опубликовали работу [Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue](https://huggingface.co/papers/2609.04250) — попытку объединить в одной модели две вещи, которые аватар в разговоре должен делать одновременно: решать, что сказать, и решать, как в этот момент двигаться.

Проблема, которую формулируют авторы, довольно точная: эти две способности исторически живут в разных семействах моделей. Модели диалоговой речи производят звук без движения, а модели co-speech motion — движения, синхронные с речью, — производят жесты и мимику, но не сам разговор. Получить обе способности одновременно и согласованно раньше можно было только склеив две отдельные системы, каждая со своей архитектурой, обучением и — что важнее всего для живого диалога — своим собственным чувством тайминга.

Motion-Omni предлагает end-to-end подход: одна модель, которая на входе получает диалоговый контекст и производит на выходе одновременно речь и движения всего тела говорящего аватара, а не двух разных потоков, которые потом нужно вручную синхронизировать. Идея в том, что если решение «что сказать» и решение «как двигаться в этот момент» принимаются внутри одной системы, а не двумя независимыми моделями, синхронность жестов и слов достигается естественным образом, а не постфактум-подгонкой.

Как и в случае с другими сегодняшними исследовательскими публикациями, в доступном на данный момент описании работы нет конкретных цифр качества — сравнения с базовыми co-speech-motion системами или диалоговыми моделями, метрик синхронности жестов с речью. Это значит, что пока рано делать вывод, насколько объединённая модель на практике выигрывает у связки «речевая модель + отдельная модель движений» по естественности и синхронности — статья описывает архитектурную идею, а не итоговый бенчмарк.

Тем не менее направление понятное: по мере того как аватары и агенты с «телом» — от инструментов создания видео до интерактивных ИИ-собеседников — становятся частью повседневных продуктов, разрыв между «что сказать» и «как это показать» превращается из мелкой инженерной неудобности в реальное узкое место качества.

### Почему это важно

Объединение речи и движения в одной модели убирает целый класс проблем с рассинхроном между тем, что говорит аватар, и тем, как он это показывает, — а это именно то, что делает синтетических собеседников либо убедительными, либо неловкими.

## English version

Authors Chengqian Ma, Wei Tao, Haoyu Zhang, and Yiwen Guo published [Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue](https://huggingface.co/papers/2609.04250), an attempt to merge two things a talking avatar has to do at the same time — decide what to say, and decide how to move while saying it — into a single model.

The problem the authors describe is precise: these two abilities have historically lived in separate model families. Spoken dialogue models produce speech without motion, while co-speech motion models produce gestures and expressions synced to speech but don't generate the conversation itself. Getting both at once, in a coordinated way, has meant stitching together two separate systems — each with its own architecture, its own training, and, crucially for a natural-feeling conversation, its own sense of timing.

Motion-Omni proposes an end-to-end approach instead: one model takes in a dialogue context and outputs both the speech and the full-body motion of the talking avatar together, rather than two separate streams that need to be manually synced afterward. The premise is that if the decision of what to say and the decision of how to move at that moment come out of the same system rather than two independent models, gesture-speech synchrony comes naturally instead of being patched in after the fact.

As with the other research paper covered today, the material currently available doesn't include quality numbers — no comparisons against baseline co-speech-motion systems or dialogue models, no synchrony metrics. So it's too early to say how much the unified model actually gains over a "speech model plus separate motion model" pipeline in naturalness or sync; the paper lays out an architectural idea, not a finished benchmark.

The direction is legible regardless: as avatars and "embodied" agents — from video-generation tools to interactive AI conversational partners — become part of everyday products, the gap between deciding what to say and deciding how to show it stops being a minor engineering inconvenience and becomes a real quality bottleneck.

### Why it matters

Merging speech and motion into one model removes a whole class of sync problems between what an avatar says and how it shows it — and that gap is exactly what makes synthetic conversation partners feel either convincing or uncanny.
