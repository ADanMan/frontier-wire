---
date: 2026-09-09
rubric: ai
title_ru: «Один симптом, три рычага»: свежая работа ставит под сомнение модный метод дообучения ИИ
title_en: "One symptom, three levers": a new paper questions a trendy way to fine-tune AI models
dek_ru: Новая статья на arXiv разбирает on-policy self-distillation — популярный способ дообучать языковые модели на их же ответах — и обещает свести его проблемы к одному общему симптому и трём возможным рычагам.
dek_en: A new arXiv paper takes apart on-policy self-distillation, a popular way to fine-tune language models on their own output, and promises to trace its problems to one shared symptom and three possible fixes.
source: https://huggingface.co/papers/2608.25936
generated: true
---

## Русская версия

Свежая статья на arXiv «[One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation](https://huggingface.co/papers/2608.25936)» (Джастин Робер и Рахил Кадер) разбирает метод, который за последний год стал одним из любимых инструментов для дообучения языковых моделей после базового претрейна, — on-policy self-distillation, самодистилляцию «на своих ответах».

Суть метода в двух предложениях, как её формулируют сами авторы: модель генерирует собственные ответы, а модель-учитель оценивает их построчно, точнее — по каждому токену. Получается гибрид: от imitation learning метод берёт плотную, «на каждом шаге», обратную связь, а от reinforcement learning — то, что модель учится на своих же, а не на чужих генерациях (on-policy sampling). На бумаге это звучит как лучшее из двух миров: не нужно, как в классическом RL, ждать разреженного сигнала в конце длинной генерации, и не нужно, как в обычной дистилляции, тащить модель к чужому распределению ответов.

Но у метода есть цена, и именно с неё, судя по всему, начинается критика в статье: оценка каждого токена требует второго прохода — а значит, второй модели, которая должна быть под рукой на каждом шаге обучения. Название работы прямо обещает свести накопившиеся претензии к методу к одному общему «симптому» и предложить три рычага, которыми его можно снять, — но конкретные формулировки этого симптома и рычагов в доступном описании статьи не приведены, так что гадать о деталях раньше времени мы не будем.

Важно здесь именно то, что это критический разбор, а не очередной рапорт о новом рекорде: авторы разбирают устоявшийся, уже широко применяемый метод, а не предлагают с нуля ещё один. Пока post-training языковых моделей превращается в отдельную, быстро растущую дисциплину, а on-policy дистилляция — в один из её стандартных инструментов, такая ревизия полезнее очередного громкого релиза: она помогает понять, где метод ломается, прежде чем на нём выстроят следующий слой инфраструктуры.

### Почему это важно

Индустрия последние два года штампует методы дообучения быстрее, чем успевает их проверять; статья, которая честно называет слабое место популярного подхода, а не рекламирует его, — редкий и полезный жанр.

## English version

A new arXiv paper — "[One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation](https://huggingface.co/papers/2608.25936)," by Justin Robert and Raheel Qader — takes a critical look at a technique that's become one of the go-to tools for post-training language models over the past year: on-policy self-distillation.

The method in two sentences, as the authors themselves frame it: a model generates its own outputs, and a teacher model scores them token by token. That makes it a hybrid — it borrows imitation learning's dense, step-by-step feedback signal, and reinforcement learning's on-policy sampling, meaning the model trains on its own generations rather than someone else's. On paper, that sounds like the best of both worlds: no waiting for a sparse reward at the end of a long generation the way plain RL does, and no dragging the model toward someone else's answer distribution the way ordinary distillation does.

But the method has a cost, and that appears to be where the paper's critique starts: scoring every token requires a second forward pass — which means a second model has to be on hand at every training step. The paper's title promises to trace the accumulated complaints about the method down to one shared "symptom," and to offer three levers for addressing it — but the exact wording of that symptom and those levers isn't in the abstract available to us, so we won't guess at specifics ahead of the full text.

What matters here is the genre: this is a critical review, not another paper announcing a new record. The authors are picking apart an already widely used method rather than proposing yet another one from scratch. With post-training now a fast-growing discipline in its own right, and on-policy distillation one of its standard tools, that kind of audit is more useful than another splashy release — it helps show where the method breaks before another layer of infrastructure gets built on top of it.

### Why it matters

The industry has been churning out fine-tuning methods faster than anyone can properly stress-test them; a paper that honestly names a popular method's weak point instead of promoting it is a rare and useful genre.
