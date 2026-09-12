---
date: 2026-09-12
rubric: science
title_ru: DeepMind построила карту эффектов девяти миллиардов мутаций генома человека
title_en: DeepMind mapped the effects of nine billion possible mutations in the human genome
dek_ru: AlphaGenome Atlas предсказывает молекулярные последствия почти каждой возможной точечной замены в ДНК.
dek_en: AlphaGenome Atlas predicts the molecular effects of nearly every possible single-letter DNA change.
source: https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
generated: true
---

## Русская версия

DeepMind выпустила AlphaGenome Atlas — карту, которая предсказывает молекулярные эффекты 9 миллиардов возможных однобуквенных замен в геноме человека, [сообщает компания](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/). Речь не об уже найденных в природе мутациях, а именно о предсказании — что произойдёт, если в конкретной позиции ДНК одна буква (A, T, G или C) заменится на другую, для практически всех позиций генома сразу.

Масштаб цифры стоит удерживать в голове трезво: 9 миллиардов вариантов — это не 9 миллиардов открытий, а 9 миллиардов прогонов модели через одну и ту же вычислительную модель. Сила такого атласа не в том, что кто-то «нашёл» все эти мутации в живых людях, а в том, что теперь для любой замены, которую обнаружат у пациента, — в клинике, в исследовании рака, при поиске причины редкого заболевания — есть готовое предсказание её вероятного молекулярного эффекта, а не догадка с нуля.

Сегодня генетика регулярно упирается именно в эту стену: секвенировать геном пациента стало быстро и относительно дёшево, а понять, какие из тысяч найденных у него вариантов вообще что-то значат, — по-прежнему трудоёмкая, часто ручная работа. Предиктивные модели вроде AlphaGenome не отменяют экспериментальную проверку — предсказание есть предсказание, — но резко сужают список кандидатов, которые вообще стоит проверять в лаборатории.

Стоит держать в уме и обратную сторону: чем масштабнее и автоматизированнее такие предсказания, тем выше цена систематической ошибки модели — если она стабильно неверно оценивает целый класс мутаций, эта ошибка будет незаметно тиражироваться во всех последующих исследованиях, которые на неё опираются.

### Почему это важно

Атлас переводит поиск причин генетических болезней из режима «искать иголку в стоге сена вручную» в режим «сверяться со справочником» — но справочник хорош ровно настолько, насколько надёжны предсказания модели, которая его составила.

## English version

DeepMind has released AlphaGenome Atlas, a map predicting the molecular effects of 9 billion possible single-letter changes across the human genome, [the company says](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/). This isn't about mutations already found in nature — it's a prediction of what happens if one DNA letter (A, T, G, or C) at a given position gets swapped for another, across nearly every position in the genome at once.

It's worth keeping the scale of that number in perspective: 9 billion variants isn't 9 billion discoveries, it's 9 billion runs of the same predictive model. The value of an atlas like this isn't that someone "found" all these mutations in living people — it's that for any variant a clinician or researcher does find in a patient, whether in cancer research or a rare-disease workup, there's now a ready-made prediction of its likely molecular effect instead of a guess from scratch.

Genetics keeps hitting exactly this wall today: sequencing a patient's genome has become fast and relatively cheap, but figuring out which of the thousands of variants found actually mean anything remains slow, often manual work. Predictive models like AlphaGenome don't replace experimental verification — a prediction is still a prediction — but they sharply narrow the list of candidates worth checking in a lab in the first place.

The flip side is worth keeping in mind too: the bigger and more automated these predictions get, the more expensive a systematic model error becomes — if it's consistently wrong about an entire class of mutations, that error quietly propagates through every downstream study that relies on it.

### Why it matters

The atlas turns the search for the causes of genetic disease from manually hunting for a needle in a haystack into checking a reference table — but the table is only as good as the model's predictions behind it.
