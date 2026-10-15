---
date: 2026-10-15
rubric: tech
title_ru: "TypeSafe представила Jev 1.14 и экспериментальные ответы о положении объектов на изображении"
title_en: "TypeSafe introduces Jev 1.14 and experimental image-location answers"
dek_ru: "Новый тип Box возвращает координаты прямоугольника, но корректный формат ответа ещё не гарантирует правильное распознавание."
dek_en: "The new Box type returns bounding coordinates, but a valid response structure does not guarantee correct recognition."
source: https://typesafe.ai/blog/jev-1-14
generated: true
---

## Русская версия

TypeSafe AI в [сообщении от 14 октября](https://typesafe.ai/blog/jev-1-14) выпустила Jev 1.14.0 через предварительный канал и открыла экспериментальные возможности работы с изображениями и длинным контекстом. Компания прямо отделяет эти функции от того, что готова рекомендовать для производственного применения. Это существенная часть новости: доступность эксперимента не равна обещанию устойчивой автоматизации. При оценке релиза этот статус нужно учитывать вместе с перечнем новых возможностей.

Особенно показателен новый тип ответа Box. Согласно [документации](https://docs.typesafe.ai/primitives/box), он задаёт четыре границы прямоугольника долями ширины и высоты изображения. Однако отдельного ответа «объект не найден» у него нет: даже при отсутствии цели возвращаются координаты. Разработчик предлагает отдельно спрашивать о наличии объекта. Поэтому типизированный ответ нельзя считать доказательством того, что нужный предмет действительно распознан.

Эта разница легко теряется в демонстрации. Приложение получает аккуратную структуру, успешно её разбирает и рисует рамку. На уровне обмена данными всё получилось. Но зритель может увидеть в этой рамке совсем другой объект или пустой участок. Формальная корректность полезна: она уменьшает неопределённость при соединении компонентов. Она не решает за систему задачу понимания картинки.

Представим прототип, который выделяет предмет для каталога. Ему мало узнать четыре числа. Нужно определить, есть ли предмет на снимке, какой именно экземпляр имелся в виду и не обрезана ли его важная часть. Если этих вопросов нет в критериях успеха, красивое выделение может скрыть ошибку. Это пример проектирования проверки, а не утверждение об уже измеренной ошибке Jev в таком приложении.

Тот же принцип относится к переходу от прототипа к реальному сервису. Стоит заранее определить, что делать при сомнительном результате: показать его человеку, запросить другой снимок или отказаться от дальнейшего действия. Такой выбор является частью приложения. Он не появляется автоматически вместе с новым форматом ответа или дополнительным параметром API.

Проверять подобную возможность лучше на неоднородной подборке: с отсутствующей целью, несколькими похожими предметами, частично закрытым объектом. Именно эти случаи позволяют понять, что означает успешная демонстрация на простом снимке. Полезно заранее записать допустимую ошибку и оценивать итоговую операцию, а не только факт получения ответа без сбоя.

### Почему это важно

Jev показывает интересный способ сделать визуальный ответ удобным для программы. Самое содержательное ограничение — необходимость отдельно проверить смысл полученных координат. Для разработчиков это напоминание: контракт данных помогает соединять системы, а критерии правильности всё равно нужно задавать на уровне задачи.

## English version

TypeSafe AI's [October 14 announcement](https://typesafe.ai/blog/jev-1-14) releases Jev 1.14.0 through a preview channel and opens experimental image and long-context features. The company explicitly separates those features from capabilities it is ready to recommend for production. That distinction is part of the news: making an experiment available is different from promising reliable automation.

The new Box answer type illustrates the boundary particularly well. Its [documentation](https://docs.typesafe.ai/primitives/box) describes four rectangle edges expressed as fractions of an image's width and height. However, it has no separate “not found” response: coordinates are returned even when the target is absent. The documentation suggests asking an additional presence question. A correctly typed answer is therefore not evidence, by itself, that the intended object has been recognized.

That distinction is easy to miss in a demonstration. An application receives a tidy structure, parses it successfully and draws a rectangle. The data exchange worked. A viewer might nevertheless see a different object inside the rectangle, or an empty patch. Structural correctness is valuable because it reduces uncertainty when connecting software components. It does not complete the visual interpretation task on their behalf.

Imagine a prototype that selects an item for a catalogue. Four numbers are insufficient: it also needs to establish whether the item exists in the picture, which instance was intended and whether an important part was cut off. Without those questions in the success criteria, an attractive selection could conceal an error. This is an example of how to design a check, rather than a claim about a measured Jev failure in such an application.

The same reasoning applies when a prototype becomes a service. Someone needs to decide what should happen after an uncertain result: show it to a person, request another image, or decline to continue. That choice belongs to the application. It does not arrive automatically with a new response format or an additional API parameter.

A useful evaluation would include varied examples: no target, several similar items and an object that is partly hidden. Those cases help establish what a successful demonstration on a straightforward image actually means. Recording an acceptable error criterion beforehand would also keep the assessment focused on the completed operation rather than merely receiving a response without a parsing failure.

### Why it matters

Jev offers an interesting way to make visual answers convenient for software. The most revealing limitation is the need to check the meaning of the coordinates separately. Data contracts help connect systems, while the definition of a correct outcome still has to come from the task itself.
