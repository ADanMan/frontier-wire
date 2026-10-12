---
date: 2026-10-12
rubric: tech
title_ru: "HashiCorp архивировала Boundary CE и не планирует новые обновления этой редакции"
title_en: "HashiCorp archives Boundary CE and plans no further updates for that edition"
dek_ru: "Код и прежние бинарные файлы остаются доступны; компания направляет развитие в HCP Boundary и Enterprise."
dek_en: "Existing code and binaries remain available while development shifts to HCP Boundary and Enterprise."
source: https://github.com/hashicorp/boundary
generated: true
---

## Русская версия

В [репозитории HashiCorp Boundary](https://github.com/hashicorp/boundary) теперь указано, что Community Edition больше не развивается активно, а новые исправления и обновления безопасности не планируются. Код и прежние бинарные файлы остаются доступны. Будущую разработку компания связывает с HCP Boundary и Boundary Enterprise. README называет дату архивирования 8 октября, тогда как баннер GitHub — 9 октября; состояние архива подтверждено при проверке 12 октября.

По [документации GitHub](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories), архивирование переводит репозиторий и его рабочие разделы в режим чтения. Это характеристика площадки разработки. Она сама по себе не выключает уже запущенную программу и не сообщает о доступности каждой коммерческой версии продукта. Для этих вопросов нужны сведения о соответствующей поставке, а не только отметка у исходного кода.

Редакционный вывод из новости касается зависимости от будущего сопровождения. У работающей системы есть текущая версия, а есть ожидание, что обнаруженные позже ошибки кто-то исправит. Прекращение планов обновления меняет именно вторую часть. При этом по одному сообщению об архиве нельзя заявлять ни о немедленной неисправности всех установок, ни об их гарантированной безопасности на неопределённый срок.

Для команды полезно сначала понять, какую редакцию и версию она использует, а затем отделить свои ожидания от обещаний поставщика. Если речь шла о получении будущих патчей CE, нынешнее сообщение меняет это ожидание. Если обсуждается иной вариант продукта, необходимо сверить его собственные условия. Смешивание названий редакций создаёт лишнюю неопределённость там, где источник довольно конкретен.

Мысленный пример: сервис продолжает выполнять вчерашние операции, но план следующего обновления исчезает. Эти два наблюдения вполне совместимы. Первое описывает работоспособность сегодня, второе — путь исправлений завтра. Решение о дальнейшем использовании потребует оценки именно этой разницы, с учётом роли сервиса и доступных вариантов сопровождения. Сам архив не выбирает такое решение за пользователя.

Существующий код также не равен существующей команде поддержки. Теоретическая возможность продолжить разработку другой командой требует людей, компетенций и собственных проверок. Она не появляется автоматически от того, что файлы можно прочитать. Поэтому возможное продолжение стоит обсуждать как отдельный проект, а не как гарантированную замену прежнего сопровождения.

### Почему это важно

Новость даёт конкретную границу планов для Boundary CE. Практический вывод — проверять поддержку на уровне используемой редакции и версии, а не общего названия продукта. Сегодняшняя работоспособность и будущие исправления отвечают на разные вопросы; план эксплуатации должен учитывать оба, не опираясь на неподтверждённые обещания.

## English version

The [HashiCorp Boundary repository](https://github.com/hashicorp/boundary) now says Community Edition is no longer under active development and that further fixes and security updates are not planned. Existing code and binaries remain available. The company directs future development toward HCP Boundary and Boundary Enterprise. Its README names October 8 as the archiving date, while GitHub's banner names October 9; the archived state was confirmed when checked on October 12.

According to [GitHub's documentation](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories), archiving makes the repository and its working sections read-only. This describes a development venue. It does not by itself switch off running software or establish the availability of every commercial edition. Those questions require information about the relevant offering, beyond the label attached to a source repository.

Our editorial takeaway concerns dependence on future maintenance. A working system has a current version and an expectation that someone will fix subsequently discovered problems. Ending update plans changes the second part. One archive notice cannot establish either immediate failure across all installations or indefinite safety for them.

A team would benefit from identifying its actual edition and version, then separating its expectations from the supplier's stated commitments. If it expected future CE patches, the current notice changes that expectation. If it uses another offering, that offering's own terms need to be checked. Merging edition names creates unnecessary ambiguity where the source is fairly specific about its scope.

Consider a hypothetical service that continues yesterday's operations while its next-update plan disappears. Those observations are compatible. One describes operation today; the other describes the route to fixes tomorrow. A decision about continued use would need to assess the difference, taking account of the service's role and available maintenance options. The archive itself does not make that decision for the user.

Available source also should not be confused with an available support team. Continuing development under another team requires people, skills and its own checks. That capability does not arise automatically because the files can be read. A possible continuation should therefore be discussed as a separate project, rather than a guaranteed substitute for the previous maintenance arrangement.

### Why it matters

The notice establishes a concrete boundary around plans for Boundary CE. The useful lesson is to check support for the edition and version actually in use, rather than for a product name in general. Present operation and future fixes answer different questions. An operating plan needs to address both without relying on unsupported promises about what will happen next.
