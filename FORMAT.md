# Edition format

One edition = one folder: `editions/<YYYY>/<MM-DD>/`. Two runs a day append to the
same folder (article numbering continues); the edition is simply "today's paper".

## Cover — `index.md`

```markdown
---
date: 2026-09-03
edition: 1
---

## От редакции

2–4 предложения: чем сегодня пахнет день. По-русски, живо, без пафоса.

## Editorial

Same 2–4 sentences in idiomatic English.
```

`edition` is a running integer (edition № since launch).

## Articles — `NN-slug.md`

`NN` = 01, 02, … in the order written. `slug` = short kebab-case.

```markdown
---
date: 2026-09-03
rubric: science          # one of: ai | tech | science | world | culture
title_ru: Русский заголовок
title_en: English headline
dek_ru: Одно предложение-подводка.
dek_en: One-sentence dek.
source: https://real-source-url          # REQUIRED, from the digest, never invented
image: https://…                          # optional, the source's og:image from the digest
generated: true
---

## Русская версия

350–550 слов. Живой русский, «на пальцах», «вы», скепсис к хайпу, без мата.
Источник — инлайн-ссылкой в тексте, не сноской. В конце: `### Почему это важно`.

## English version

Same substance, idiomatic English, inline source links. Ends with `### Why it matters`.
```

## Hard rules

- Every fact comes from the day's digest (`digests/<year>/<date>.md`); nothing invented.
- Every article carries a real `source:` URL.
- Rubrics with no worthy items are simply absent — no filler.
- 5–8 articles per run is the healthy range; fewer beats padding.
