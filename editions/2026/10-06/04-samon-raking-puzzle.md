---
date: 2026-10-06
rubric: culture
title_ru: Samon превращает узор на песке в проверяемую головоломку
title_en: Samon turns patterns in sand into a puzzle with checkable answers
dek_ru: У браузерного прототипа есть 148 садов, строгий счёт поворотов и подсказки о маршруте самого игрока.
dek_en: The browser prototype offers 148 gardens, an explicit turn score and hints about the player’s own route.
source: https://gwern.net/doc/design/2026-10-03-gwern-samon.html
generated: true
---

## Русская версия

Монах входит в песчаный сад и должен выйти, сгребая собственные следы: одним непрерывным маршрутом посетить каждую свободную клетку ровно один раз. Из этого правила выросла [Samon — дизайнерский документ и браузерный прототип](https://gwern.net/doc/design/2026-10-03-gwern-samon.html), опубликованные на сайте Gwern. Страница развивает набросок 2023 года; нынешняя версия датирована интервалом до 5 октября 2026 года и помечена как работа в процессе. Поэтому речь идёт о доступном прототипе, а не о завершённом коммерческом релизе.

На первый взгляд достаточно заполнить поле змейкой. Автор проверил это интуитивное ощущение решателем: у пустого сада 7×7 с входом в углу получилось 1 510 446 допустимых маршрутов. Случайные камни тоже не обеспечивали хорошую головоломку автоматически: часто они делали сад либо невозможным, либо слишком свободным. Здесь математическая проверка помогает отличить правило, которое звучит занятно, от ограничения, которое действительно заставляет думать.

Решение — считать повороты. Минимум, называемый par, определяется решателем; прохождение с этим числом поворотов получает печать. Для того же пустого поля 7×7 минимум равен 12, и его достигают 66 маршрутов. Другой вариант — широкие грабли, запрещающие разворот на открытом песке без опоры на камень или стену. Такие правила делают физический образ сада частью задачи. При этом автор прямо предупреждает: малое число поворотов не гарантирует красивый рисунок в любом расположении препятствий.

Особенно интересны подсказки. Они оценивают уже начатый маршрут игрока: можно ли ещё достичь par, можно ли хотя бы закончить сад или следует отступить. Если поиск не успел доказать ответ, система должна сообщить неопределённость. Подсказанный результат отмечается серой, а самостоятельный оптимальный — красной печатью. Прогресс и готовый маршрут можно переносить ссылкой; принятие чужого прогресса требует отдельного действия, а просмотр чужого решения не записывает его как ваше достижение.

Прототип содержит 148 садов, ежедневный сад и свободный режим для рисования граблями. После прохождения появляется классическое японское стихотворение с источником оригинала. Предусмотрены клавиатурное управление и учёт настройки уменьшенного движения; полноценную невизуальную доступность автор ещё предлагает проверять со специалистами. Документ, собственный код и дизайн опубликованы под CC0. Это даёт возможность изучать реализацию и развивать идеи, но не означает, что все предусмотренные производственным планом проверки уже завершены.

### Почему это важно

Наш вывод из этого проекта: понятная эстетическая цель может стать измеримой задачей без непрозрачного судьи. Игрок видит повороты и способен объяснить, где потратил лишний. Однако доказанный минимум и удовольствие от игры — разные проверки. Автор оставляет в плане реальные испытания на телефонах и наблюдение за игроками, чтобы выяснить, учатся ли они правилу, а не просто копируют показанный маршрут.

## English version

A monk enters a sand garden and must rake his footprints away on the way out, visiting every free cell exactly once along an unbroken route. That rule becomes [Samon, a design document and playable browser prototype](https://gwern.net/doc/design/2026-10-03-gwern-samon.html) published on Gwern's website. The page develops a 2023 sketch; its current date range extends to October 5, 2026, and its status remains work in progress. This is an available prototype, rather than a finished commercial release.

Simply filling the board with a winding path sounds easy. The author tested that intuition with a solver: an empty 7×7 garden with a corner gate has 1,510,446 valid routes. Random stones did not automatically create satisfying puzzles. They often made gardens either impossible or excessively open. Mathematical checking helps distinguish a rule that sounds engaging from a constraint that actually demands thought. The design account gives readers both the proposed experience and the measurements used to examine it.

One solution is to count turns. A solver establishes the minimum, called par, and completing a garden at that score earns a seal. For the same empty 7×7 board, par is 12 turns, achieved by 66 routes. Another rule uses a wide rake: no U-turn on open sand without bracing against a stone or wall. Physical imagery becomes part of the puzzle. The author nevertheless warns that fewer turns do not guarantee an attractive pattern under every arrangement of obstacles.

The hints are particularly interesting. They examine the player's existing route: can it still reach par, can it at least finish, or should the player step back? If a search cannot establish an answer within its budget, it should acknowledge uncertainty. Helped optimal solutions receive a grey seal; unaided ones receive vermilion. Routes and progress can travel in links. Accepting another player's progress requires an explicit action, while viewing a shared solution does not record it as your own achievement.

The prototype includes 148 gardens, a daily garden and an unrestricted raking practice area. Completing a garden reveals a classical Japanese poem with a source for the original. Keyboard controls and reduced-motion preferences are supported; the author still proposes testing fully nonvisual accessibility with relevant users. The document, original code and design are released under CC0. That allows others to study the implementation and develop the ideas, without implying that every check in the production plan has been completed.

### Why it matters

Our reading is that a legible aesthetic objective can become a measurable challenge without an opaque judge. Players can count the turns and explain where an unnecessary one occurred. A proven optimum and an enjoyable experience still require different kinds of evidence. The production plan retains testing on real phones and observation of players, to establish whether they learn the rule rather than merely copying a demonstrated path.
