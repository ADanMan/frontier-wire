---
date: 2026-10-24
rubric: tech
title_ru: "Разбор MPS в PyTorch 2.15 показывает, где Mac терял скорость и память"
title_en: "A PyTorch 2.15 MPS review traces performance and memory bottlenecks on Macs"
dek_ru: "Команда Hugging Face описала FP8, специализированные Metal-ядра и исправление расхода памяти при декодировании видео."
dek_en: "Hugging Face's team details FP8, specialised Metal kernels and a video-decoding driver-memory fix."
source: https://huggingface.co/blog/mps-pytorch-2-15
generated: true
---

## Русская версия

Команда PyTorch в Hugging Face [опубликовала разбор изменений MPS в версии 2.15](https://huggingface.co/blog/mps-pytorch-2-15). Материал датирован 20 октября и впервые попадает в нашу подборку сегодня. Он посвящён выполнению моделей на Apple silicon через графический backend MPS. Авторы предлагают проверять кандидат выпуска отдельно; мы не представляем эту публикацию как подтверждение уже завершённого стабильного релиза или автоматического обновления компьютеров читателей.

Одна группа изменений касается перехода от MPSGraph к специализированным ядрам Metal. Команда ищет узкие места на реальных моделях и переносит соответствующие операции в более подходящий путь выполнения. При последовательной генерации текста это особенно заметно на маленьких порциях данных: вычисления очередного токена отличаются от обработки большого начального запроса. Поэтому ускорение отдельной операции и сокращение времени полного ответа — связанные, но разные измерения.

Самый наглядный пример — декодирование видео в Wan2.2. Для указанного в статье 28-частного прохода VAE пиковая память драйвера снизилась примерно с 270 до 8 гигабайт после изменения операции дополнения тензоров. В той же таблице пик текущих выделений под тензоры меняется гораздо меньше: примерно с 4,42 до 4,10 гигабайта. Речь не об уменьшении размера самой модели в десятки раз, а об устранении конкретного расхода в пути выполнения.

Другое направление — хранение значений FP8 и масштабированное матричное умножение. Один байт на значение занимает вдвое меньше места, чем двухбайтовые FP16 или BF16. Однако из этой арифметики не следует, что вся программа потребует ровно половину прежней памяти. В ней остаются другие данные и промежуточные результаты; численный формат также нужно оценивать вместе с качеством вычисления для своей задачи.

В разборе приведены улучшения линейной алгебры, свёрток, потоков MPS и корректности отдельных операций. Есть и опубликованные измерения скорости, но они привязаны к формам тензоров, модели и оборудованию. Особенно осторожно следует читать общий множитель для языковых моделей: внутри материала описаны разные уровни сравнения. Мы не переносим одно число на все Mac и не выдаём его за собственное измерение.

Требования указаны явно: Apple silicon, macOS 15 или новее и Python 3.11 или новее. Отдельная часть статьи посвящена будущей 2.16, включая изменения, ещё находящиеся на рассмотрении. Эти планы нельзя зачислять в уже доступные возможности 2.15. Здесь полезнее следить за точной версией и конкретной исправленной операцией, чем за общим обещанием «всё стало быстрее».

### Почему это важно

Локальная модель может упираться в программный путь, а не только в размер памяти или характеристики чипа. Разбор показывает, как искать причину по слоям измерения. Для практической оценки нужны корректный результат, воспроизводимая нагрузка и раздельный учёт тензоров, резервов и памяти драйвера.

## English version

Hugging Face's PyTorch team has [reviewed MPS changes in PyTorch 2.15](https://huggingface.co/blog/mps-pytorch-2-15). Published on October 20, the article receives its first coverage here today. It concerns model execution on Apple silicon through the MPS backend. The authors invite testing a release candidate separately; this feature does not establish that a stable release has already been completed or readers' computers updated.

One group of changes replaces MPSGraph paths with specialised Metal kernels. The team investigates bottlenecks in real models and moves relevant operations to more suitable implementations. During sequential text generation, the small workload for each new token differs from processing a large initial prompt. A faster operation and a faster complete response are therefore related but distinct measurements.

The clearest example concerns Wan2.2 video decoding. For the article's specified 28-tile VAE decode, peak driver memory falls from roughly 270 GiB to 8 GiB after a padding change. In the same table, peak current tensor allocation changes much less, from about 4.42 GiB to 4.10 GiB. This is not a manyfold reduction in the model's own size. It addresses a particular memory cost in its execution path.

Another development adds FP8 value storage and scaled matrix multiplication. One byte per value takes half the space of two-byte FP16 or BF16. That arithmetic does not establish that an entire application will need exactly half its former memory. Other data and intermediate results remain, while a numerical format must also be assessed against the workload's required output quality.

The review covers linear algebra, convolutions, MPS streams and correctness fixes. It includes speed measurements tied to tensor shapes, models and hardware. Overall language-model speedup figures deserve particular care because the article discusses different comparison levels. We do not apply a single multiplier to every Mac or present the published measurements as our own tests.

Requirements are explicit: Apple silicon, macOS 15 or later and Python 3.11 or later. A separate section looks ahead to 2.16, including work still under review. Those plans should not be counted as delivered 2.15 features. Tracking the exact version and corrected operation is more informative than a blanket claim that everything has become faster.

### Why it matters

A local model can be constrained by its software execution path as well as memory capacity and chip specifications. This review illustrates how to investigate the cause through separate measurements. A practical assessment needs correct output, a reproducible workload and distinctions between tensor allocations, reserved space and driver memory.
