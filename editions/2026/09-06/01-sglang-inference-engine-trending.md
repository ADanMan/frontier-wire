---
date: 2026-09-06
rubric: ai
title_ru: SGLang снова в трендах GitHub — и растёт куда правдоподобнее конкурентов
title_en: SGLang is trending on GitHub again — and growing far more plausibly than its rivals
dek_ru: Движок для быстрой раздачи больших моделей прибавил 1 237 звёзд за сутки; по собственным данным проекта, на новом железе NVIDIA он ускоряет инференс в 25 раз.
dek_en: The engine for fast LLM serving added 1,237 stars in a day; the project claims a 25x inference speedup on new NVIDIA hardware.
source: https://github.com/sgl-project/sglang
generated: true
---

## Русская версия

Проект [sgl-project/sglang](https://github.com/sgl-project/sglang) снова попал в топ трендов GitHub: за сутки счётчик звёзд вырос с 34 257 до 35 494 — плюс 1 237, форков у репозитория уже 8 563. В трендах он идёт под категорией «Transformer», и это по сути верно: SGLang — движок для inference-раздачи больших языковых и мультимодальных моделей, от одной видеокарты до распределённых кластеров.

В основе движка — RadixAttention, механизм кеширования общих префиксов запросов, который избавляет от повторных вычислений там, где промпты пользователей пересекаются. К нему добавлены планирование на CPU без лишних задержек, разделение фаз prefill и decode, спекулятивное декодирование и непрерывный батчинг — набор техник, которые в сумме и дают заявленный прирост скорости. Проект поддерживает как языковые модели (Llama, Qwen, DeepSeek, Kimi, GLM), так и модели эмбеддингов, reward-модели и диффузионные модели, а по железу работает не только с видеокартами NVIDIA и AMD, но и с процессорами Intel Xeon, TPU от Google и NPU Ascend.

По собственным данным проекта, на архитектуре NVIDIA GB300 движок показывает 25-кратный прирост производительности инференса — это обновление февраля 2026 года — а среди пользователей называются xAI, NVIDIA, AMD, Google Cloud и Microsoft Azure. Разработчики утверждают, что через SGLang ежедневно проходят триллионы токенов на более чем 400 тысячах видеокарт. Развивает проект некоммерческая организация LMSYS — та же группа, что стоит за Chatbot Arena.

### Почему это важно

На фоне вороха свежих «мета-харнессов» для ИИ-агентов, чьи счётчики звёзд в последние дни доходили до сотен тысяч за считаные месяцы существования, рост SGLang выглядит куда правдоподобнее: чуть больше тысячи звёзд в день — это похоже на органический интерес разработчиков, а не на аномалию счётчика. Гонка движков для инференса — SGLang, vLLM и другие — определяет не то, какая модель самая умная, а то, во сколько компаниям обходится каждый токен ответа. Для индустрии сейчас это едва ли не важнее самих моделей.

## English version

The [sgl-project/sglang](https://github.com/sgl-project/sglang) repository is trending on GitHub again: its star count climbed from 34,257 to 35,494 in a day, up 1,237, with 8,563 forks. GitHub lists it under the "Transformer" category, which is fair enough — SGLang is a serving engine for large language and multimodal models, scaling from a single GPU to distributed clusters.

At its core is RadixAttention, a caching mechanism for shared request prefixes that avoids recomputing work when users' prompts overlap. On top of that sit zero-overhead CPU scheduling, prefill-decode separation, speculative decoding, and continuous batching — a combination of techniques that together produce the claimed speed gains. The project supports language models (Llama, Qwen, DeepSeek, Kimi, GLM) alongside embedding models, reward models, and diffusion models, and runs not just on NVIDIA and AMD GPUs but on Intel Xeon CPUs, Google TPUs, and Ascend NPUs.

By the project's own account, SGLang delivers a 25x inference speedup on NVIDIA's GB300 architecture, an update from February 2026, with adopters including xAI, NVIDIA, AMD, Google Cloud, and Microsoft Azure. The developers say the engine now handles trillions of tokens a day across more than 400,000 GPUs. SGLang is maintained by LMSYS, the nonprofit also behind Chatbot Arena.

### Why it matters

Against a pile of freshly trending AI-agent "meta-harnesses" whose star counts have hit hundreds of thousands within months of launch, SGLang's growth looks far more believable: just over a thousand stars a day reads like organic developer interest rather than a counter anomaly. The race between inference engines — SGLang, vLLM, and others — doesn't decide which model is smartest; it decides how much each answer costs companies to generate. For the industry right now, that may matter more than the models themselves.
