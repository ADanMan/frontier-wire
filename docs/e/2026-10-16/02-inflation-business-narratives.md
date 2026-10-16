---
date: 2026-10-16
rubric: economy
title_ru: "Исследователи Банка Англии применили языковую модель к рассказам компаний об изменении цен"
title_en: "Bank of England researchers use a language model to examine firms’ pricing narratives"
dek_ru: "Работа превращает тексты встреч с бизнесом в показатели, но не устанавливает причинный вклад факторов в общую инфляцию."
dek_en: "The study turns company-visit narratives into indicators without identifying causal contributions to aggregate inflation."
source: https://bankunderground.co.uk/2026/10/15/artificial-intelligence-meets-business-intelligence-the-anatomy-of-inflation/
generated: true
---

## Русская версия

В [публикации Bank Underground от 15 октября](https://bankunderground.co.uk/2026/10/15/artificial-intelligence-meets-business-intelligence-the-anatomy-of-inflation/) сотрудники Банка Англии описали применение GPT-5.4 к текстам встреч с компаниями. Задача — извлечь из объяснений бизнеса показатели изменения отпускных цен и факторов, которые сами компании связывают с этими решениями. Это исследовательский материал авторов, а не заявление комитета по денежной политике и не новый официальный индекс потребительских цен.

Исходный архив содержит 66 820 отчётов за период с января 2005-го по сентябрь 2026-го. Для ограничения затрат авторы берут случайную треть более ранних материалов и полный набор за 2026 год. Они отдельно отмечают, что производственные предприятия и компании среднего размера представлены несколько шире, чем в экономике страны в целом. Поэтому число документов не означает репрезентативную перепись всех фирм.

Модель должна учитывать фактор лишь тогда, когда текст явно связывает его с ценообразованием. Само упоминание роста зарплат не даёт основания автоматически записать его в причины повышения цены. Такой подход важен для задачи извлечения: система размечает рассказ собеседника, а не получает прямой доступ к реальному механизму принятия решения внутри компании.

Представьте две записи встречи. В одной директор говорит, что выросли расходы, но цена осталась прежней из-за слабого спроса. В другой — что дополнительные затраты переложены на покупателя. Это редакционный пример, однако он показывает, почему простой счётчик слов «расходы» и «подорожание» потерял бы существенную разницу. Смысл работы — сохранить связь между событиями в тексте.

Авторы сопоставляют агрегированные оценки с другими рядами, включая инфляцию и ручные оценки сотрудников. При чтении графиков существенна оговорка: часть рядов центрирована и приведена к сопоставимому масштабу. Визуальное совпадение линий после такого преобразования нельзя считать отдельным доказательством точного прогноза. Вопрос о том, содержат ли ожидания компаний опережающую информацию, авторы оставляют для дальнейшего исследования.

Есть и более общая граница. Если многие контакты называют энергию причиной изменения цен, это полезное свидетельство о восприятии бизнеса. Но для утверждения о причинном вкладе энергетического шока в общую инфляцию нужны другие основания. Между систематизированным рассказом и причинным объяснением остаётся исследовательская работа.

### Почему это важно

Языковая модель здесь помогает читать большой архив, сохраняя различия между объяснениями компаний. Сильная сторона подхода — дополнительный измерительный инструмент. Его стоит оценивать по качеству разметки, составу выборки и устойчивости сигналов, не превращая полученные оценки в готовый прогноз цен или инвестиционную рекомендацию.

## English version

In an [October 15 Bank Underground post](https://bankunderground.co.uk/2026/10/15/artificial-intelligence-meets-business-intelligence-the-anatomy-of-inflation/), Bank of England staff describe using GPT-5.4 to examine company-visit reports. They extract indicators of output-price changes and the factors firms themselves connect with those decisions. This is the authors' research account, rather than a monetary-policy committee statement or a new official consumer-price index.

The underlying archive contains 66,820 reports spanning January 2005 to September 2026. To contain costs, the researchers use a random third of earlier material and the full 2026 sample. They also note that manufacturing and medium-sized businesses are somewhat overrepresented relative to the wider business population. A large document count should therefore not be read as a representative census of all firms.

The model is instructed to assign a contribution only when a report explicitly connects a factor with pricing. Mentioning higher wages, for instance, does not automatically establish that wages caused a price rise. This distinction is central to extraction: the system is classifying a contact's account, rather than observing the company's actual decision mechanism directly.

Consider two hypothetical meeting notes. In one, a manager says costs increased but prices were held because demand was weak. In the other, additional costs were passed on to customers. This is an editorial example, but it shows why simply counting words about costs and increases would miss an important difference. The point of the method is to preserve relationships within an account.

The authors compare aggregated scores with other series, including inflation and staff assessments. An important qualification accompanies the charts: some series are demeaned and rescaled for comparison. Visually similar lines after that transformation are not a separate demonstration of forecasting precision. Whether firms' expectations contain leading information is explicitly left for further research.

There is also a broader evidential boundary. If many contacts describe energy as a reason for changing prices, that is useful information about business perceptions. Establishing the causal contribution of an energy shock to aggregate inflation requires additional evidence. Systematizing accounts does not, by itself, convert them into causal identification.

The sensible interpretation is therefore complementary. A narrative indicator can help an analyst decide which questions to investigate, while the sampling and classification process still need scrutiny. More accessible text does not eliminate the need to ask whose experiences were recorded and which businesses were absent.

### Why it matters

The language model helps researchers read a large archive without discarding distinctions between firms' explanations. The contribution is an additional measurement tool. Its value depends on annotation quality, sample composition and signal stability, rather than treating the resulting scores as a ready-made price forecast or investment recommendation.
