---
date: 2026-09-18
rubric: ai
title_ru: ИИ-индустрия тихо меняет фокус: с обучения на вывод
title_en: The AI industry is quietly shifting from training to inference
dek_ru: Пять лет гонка шла за размером моделей при обучении. Теперь решающим становится то, что происходит уже после — когда модель отвечает.
dek_en: For five years the race was about training bigger models. Now what happens after training — at inference time — is what matters most.
source: https://spectrum.ieee.org/inference-hardware-revolution
generated: true
---

## Русская версия

С 2020 года индустрия ИИ была одержима размером моделей при обучении: языковые модели раздулись с миллионов до триллионов параметров. Подход работал — самая крупная версия GPT-3 от OpenAI, вышедшая в 2020-м, правильно отвечала лишь на 43,9% вопросов в одном из тестов. Но, как [пишет IEEE Spectrum](https://spectrum.ieee.org/inference-hardware-revolution), центр тяжести гонки сместился: теперь решающим становится не то, насколько велика модель при обучении, а то, что происходит потом — во время вывода (inference), когда модель уже отвечает пользователю.

Разница на пальцах такая: обучение — это разовые огромные вычислительные затраты на создание модели, которые оплачивает разработчик. Вывод — это вычисления, которые повторяются миллиарды раз каждый день, каждый раз, когда кто-то отправляет модели запрос. Чем больше людей и продуктов реально пользуются моделями, тем больше суммарных денег и энергии уходит именно на вывод, а не на обучение. В какой-то момент это перевешивает — и именно на это железо, инфраструктуру и архитектурные решения теперь и переориентируется индустрия.

Число 43,9% из статьи — не просто историческая деталь. Это точка отсчёта, показывающая, насколько далеко ушли модели с тех пор, и одновременно — напоминание, что весь этот прогресс на этапе обучения был лишь половиной уравнения. Вторая половина — как дёшево и быстро потом этот прогресс можно доставить до конечного пользователя — долго оставалась в тени и выходит на первый план только сейчас.

### Почему это важно

Если экономика ИИ определяется вычислениями на вывод, а не на обучение, то и конкурентное преимущество смещается: выигрывает не тот, у кого самая большая модель, а тот, кто дешевле и быстрее её обслуживает в масштабе. Это меняет расклад сил — от чипмейкеров до облачных провайдеров — куда сильнее, чем очередной рекорд по числу параметров.

## English version

Since 2020, the AI industry has been obsessed with model size at training time: language models ballooned from millions of parameters to trillions. The approach worked — the largest version of OpenAI's GPT-3, released in 2020, correctly answered just 43.9 percent of questions on one benchmark. But as [IEEE Spectrum reports](https://spectrum.ieee.org/inference-hardware-revolution), the center of gravity has shifted: what matters most now isn't how big a model is during training, but what happens afterward, at inference time, when the model is actually answering a user.

The distinction, in plain terms: training is a one-time, enormous compute cost the developer pays to build the model. Inference is compute that repeats billions of times a day, every single time someone sends the model a query. The more people and products actually use these models, the more total money and energy goes toward inference rather than training. At some point that balance tips — and that's exactly where the industry's hardware, infrastructure and architecture decisions are now being redirected.

The 43.9 percent figure isn't just a historical footnote. It's a baseline that shows how far models have come since — and a reminder that all that training-time progress was only half the equation. The other half — how cheaply and quickly that progress can then be delivered to an actual user — stayed in the background for years and is only now moving to center stage.

### Why it matters

If AI economics are increasingly defined by inference compute rather than training compute, competitive advantage shifts too: the winner isn't whoever has the biggest model, but whoever can serve it cheapest and fastest at scale. That reshuffles the pecking order — from chipmakers to cloud providers — more than any new parameter-count record ever could.
