---
date: 2026-11-03
rubric: tech
title_ru: OpenAI повышает bug bounty и готовит новый защитный спринт
title_en: OpenAI raises bug bounties and prepares another defensive sprint
dek_ru: Обновлённые стимулы для внешних исследователей сопровождают план совместной проверки с Cathedral; это не сообщение об обнаруженной атаке.
dek_en: New incentives for external researchers accompany a planned collaboration with Cathedral, rather than reporting a newly discovered attack.
source: https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties
generated: true
---

## Русская версия

OpenAI 2 ноября [объявила об увеличении вознаграждений в Security Bug Bounty](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties). В отдельном [сообщении о следующем защитном спринте](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) компания описала план работы своих команд с исследователями Cathedral. Это два связанных способа искать слабые места: внешняя программа сообщений и организованный этап внутренней проверки. Ни один анонс сам по себе не является сообщением о новой атаке, утечке данных или доказанном результате ещё не проведённого спринта.

В новых диапазонах обычная критическая находка в основном продукте может получить до 30 тысяч долларов. Для исключительных критических случаев сохраняется предел до 100 тысяч, а с бонусами верхний ориентир достигает примерно 172 тысяч. Это разные категории, а не обещание максимальной суммы за любое сообщение. Компания вводит стимулы за качество отчёта, длительное сотрудничество и приоритетные кампании. Приведённые в анонсе расчёты прямо обозначены как иллюстрации; читать их как перечень подтверждённых реальных инцидентов нельзя.

Здесь полезно различать обнаружение и сообщение, пригодное для исправления. Исследователь может заметить странное поведение, но команде ещё нужно понять, воспроизводится ли оно, где находится граница проблемы и что изменится после исправления. Чем точнее это установлено в рамках разрешённой проверки, тем меньше неоднозначности на следующем этапе. Такая связь объясняет интерес к качеству отчёта. Она не превращает публичное объявление программы в разрешение произвольно проверять любые системы или затрагивать данные других людей вне установленных условий.

Второй анонс относится к будущей совместной работе с Cathedral. Компания отделяет этот план от предыдущего спринта, где инженеры применяли модели для исследования находок, воспроизведения в изолированных условиях и подготовки исправлений к просмотру. Для читателя важна последовательность: гипотеза о слабом месте, подтверждение, изменение и проверка результата. Автоматизация одного этапа не доказывает, что остальные выполнены. Публикация не даёт оснований заранее объявлять систему свободной от уязвимостей или считать модель заменой всей защитной практики.

Оценивать результат таких мер стоит не по одному размеру премии. Нужны сведения о том, насколько сообщения помогают исправлению, как быстро устраняются подтверждённые проблемы и возвращаются ли они после изменений. Это возможные направления оценки, а не статистика, уже представленная редакцией. Даже рост числа сообщений допускает несколько объяснений: больше интереса к программе, более широкий охват или иной профиль находок. Сам по себе он ещё не измеряет изменение безопасности для пользователей и требует контекста.

### Почему это важно

Вознаграждения и защитные спринты воздействуют на разные части одного процесса. Первые привлекают внешнее внимание и поощряют полезное описание находок, вторые организуют проверку и исправление внутри команды. Свежие объявления меняют стимулы и описывают следующий шаг. Доказательством эффективности станут результаты работы, а не само наличие программы. Такое разделение помогает читать новости о безопасности без неподтверждённых обвинений и без противоположной крайности — обещания полной защищённости на основании одного анонса.

## English version

On November 2, OpenAI [announced increased Security Bug Bounty rewards](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties). A separate [post about its next defensive sprint](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai) described planned work between its teams and researchers from Cathedral. These are related approaches to finding weaknesses: an external reporting program and an organized internal testing effort. Neither announcement is itself a disclosure of a new attack, a data leak or demonstrated results from a sprint that has yet to take place. Their dates and prospective status should remain clear.

Under the new ranges, a standard critical finding in a core product can earn up to $30,000. Exceptional critical cases remain eligible for up to $100,000, with a maximum of approximately $172,000 when bonuses apply. These are different categories, not a promise of the highest amount for every submission. Incentives address report quality, sustained collaboration and priority campaigns. The announcement explicitly labels its payout calculations as illustrative. They should not be converted into a list of verified real incidents or assumed to identify events that actually occurred.

Discovery and an actionable report are different stages. A researcher might notice unusual behavior, while the receiving team still needs to establish reproducibility, locate the problem's boundary and determine what a fix would change. Greater precision within authorized testing reduces ambiguity at the next stage. That relationship helps explain interest in report quality. It does not turn the public existence of a program into permission to test arbitrary systems or access other people's information outside the program's defined conditions and scope. No such testing was performed for this article.

The second announcement concerns future collaboration with Cathedral. OpenAI distinguishes that plan from an earlier sprint in which engineers used models to investigate findings, reproduce them in isolated environments and prepare patches for review. The relevant sequence is a hypothesis, confirmation, a change and verification of its outcome. Automating one stage does not establish completion of the others. The account cannot support a declaration that a system has become vulnerability-free or that a model substitutes for every part of defensive practice. Those would be broader claims than either announcement makes.

Evaluating these measures requires more than looking at the largest reward. Relevant questions include how reports contribute to fixes, how quickly confirmed problems are addressed and whether they recur after changes. These are possible assessment dimensions, not statistics produced by this publication. Even an increase in submissions could reflect several factors: more interest, broader coverage or a different mix of findings. That number alone would not establish a change in user security without additional context about what was found, confirmed and resolved.

### Why it matters

Rewards and defensive sprints affect different parts of one process. The former attract outside attention and encourage useful reports; the latter organize investigation and repair within a team. These announcements change incentives and describe a next step. Evidence of effectiveness will come from the work's results rather than the existence of a program. Keeping those levels separate avoids both unsupported allegations and the opposite mistake of promising complete protection on the basis of an announcement alone.
