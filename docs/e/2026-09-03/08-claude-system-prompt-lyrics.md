---
date: 2026-09-03
rubric: ai
title_ru: Anthropic публикует системные промпты Claude — и там неожиданно много про тексты песен
title_en: Anthropic publishes Claude's system prompts — and song lyrics get oddly special treatment
dek_ru: Компания открыто выкладывает инструкции для Claude.ai и мобильных приложений вместе с историей правок.
dek_en: The company openly publishes the instructions behind Claude.ai and its mobile apps, changelog included.
source: https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/
generated: true
---

## Русская версия

Разработчик Саймон Уиллисон [обратил внимание](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) на любопытную деталь в очередном обновлении системного промпта Claude: модель теперь особенно настойчиво избегает воспроизведения текстов песен. Сама по себе новость не о том, что Claude вдруг стал бояться музыки, — это часть куда более крупной и, честно говоря, редкой для индустрии практики Anthropic: компания публично выкладывает системные промпты своих потребительских продуктов, Claude.ai и мобильных приложений, причём не только текущую версию, но и историю изменений.

Для тех, кто не в теме: системный промпт — это набор скрытых инструкций, который разработчик подкладывает модели перед каждым разговором с пользователем. Именно там прописано, как модели вести себя, чего избегать, на какие темы реагировать осторожнее. Обычно такие вещи компании прячут — это по сути часть продуктовой логики и конкурентного преимущества. Anthropic вместо этого делает противоположное, и Уиллисон, который давно и придирчиво следит за индустрией ИИ, называет это редким примером прозрачности, которую он бы хотел видеть чаще.

Есть, впрочем, оговорка: под раздачу не попадают Claude Cowork и Claude Code — продукты для разработчиков и командной работы, чьи промпты остаются закрытыми. То есть прозрачность распространяется на потребительские сценарии, но не на инструменты, которыми пользуются профессионалы и которые как раз чаще всего разбирают по косточкам сами разработчики.

Возвращаясь к текстам песен: ограничение выглядит как прямое следствие вечной головной боли всех разработчиков LLM — авторского права. Тексты песен защищены точно так же, как любой другой литературный материал, и воспроизведение их целиком моделью — это прямой путь к юридическим претензиям от лейблов и правообладателей, которые в последние годы особенно активно судятся с ИИ-компаниями за использование защищённого контента. Судя по всему, для Anthropic это стало достаточно значимой темой, чтобы явно прописать её в промпте, а не полагаться на общие инструкции про уважение к авторским правам.

Само по себе публикование системных промптов — практика, которая позволяет сторонним разработчикам и исследователям понимать, почему модель ведёт себя так, а не иначе, и отслеживать, как меняется поведение продукта со временем. Для индустрии, где большинство компаний держат такие детали в секрете, это скорее исключение, чем правило.

### Почему это важно

Публикация системных промптов — редкий случай, когда пользователь ИИ-продукта может буквально прочитать, что ему запрещено делать и почему. Это не решает вопрос авторских прав в генеративном ИИ, но делает конкретные компромиссы компании видимыми — а не спрятанными за корпоративной формулировкой «мы соблюдаем законы об авторском праве».

## English version

Developer Simon Willison [noticed](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) a specific detail in the latest update to Claude's system prompt: the model now goes out of its way to avoid reproducing song lyrics. That detail isn't really the story, though — it's a symptom of a much larger and genuinely unusual practice at Anthropic: the company publicly publishes the system prompts behind its consumer products, Claude.ai and the mobile apps, including a running history of changes over time.

For anyone unfamiliar with the term: a system prompt is the hidden set of instructions a developer feeds a model before every conversation with a user. It's where behavior gets specified — what to avoid, what to be cautious about, how to respond in edge cases. Most companies treat this as a trade secret. Anthropic does the opposite, and Willison, who has tracked the AI industry closely for years, calls it a rare example of the transparency he wishes were more common.

There's a carve-out, though: Claude Cowork and Claude Code, the developer- and team-facing products, keep their prompts private. So the transparency covers consumer-facing use cases but not the tools professional developers actually rely on and would most want to inspect.

As for the song lyrics restriction, it reads like a direct response to the perennial headache for LLM developers: copyright. Song lyrics are protected the same way any other literary work is, and having a model reproduce them wholesale is a fast route to legal trouble from labels and rights holders, who have been increasingly aggressive about suing AI companies over the use of copyrighted material. It seems this became significant enough for Anthropic to spell out explicitly in the prompt rather than leave it to general copyright-respecting language.

The broader practice of publishing system prompts lets outside developers and researchers understand why a model behaves the way it does, and track how that behavior shifts over time. In an industry where most companies keep these details under wraps, this is the exception rather than the rule.

### Why it matters

Publishing system prompts is a rare case where a user of an AI product can literally read what they're being kept from doing, and why. It doesn't resolve the copyright question in generative AI, but it makes the company's specific tradeoffs visible instead of hiding them behind boilerplate about respecting copyright law.
