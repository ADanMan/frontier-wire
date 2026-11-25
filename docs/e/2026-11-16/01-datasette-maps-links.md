---
date: 2026-11-16
rubric: tech
title_ru: Datasette добавляет географические превью и ссылки между приложениями
title_en: Datasette adds geospatial previews and links between applications
dek_ru: Два новых релиза соединяют обзор данных с переходом к подробностям.
dek_en: Two new releases offer ways to connect data overviews with detailed views.
source: https://simonwillison.net/2026/Nov/15/datasette-maplibre/
generated: true
---

## Русская версия

В сегодняшнем digest появились два новых способа показывать данные внутри Datasette. В [сообщении о datasette-maplibre 0.1a0](https://simonwillison.net/2026/Nov/15/datasette-maplibre/) Саймон Уиллисон представил географический плагин на основе MapLibre GL и OpenFreeMap. Отдельный [релиз datasette-apps 0.4a0](https://simonwillison.net/2026/Nov/15/datasette-apps/) добавил ссылки между приложениями. Оба первоисточника датированы 15 ноября и прочитаны полностью для выпуска за 16 ноября. Это новые изменения, отличные от вчерашних новостей о подключении моделей и плагине графиков; мы не выдаём дату подборки за дату объявления.

В географическом плагине автор выделяет способ предварительного показа фигур GeoJSON. Сначала пользователь видит SVG-превью, а WebGL-представление загружается, когда объект попадает в видимую область. В заметке также есть ссылка на пример, где фигуры и точки с широтой и долготой показаны вместе. Такой интерфейс позволяет рассматривать разные виды географических данных рядом. Но сообщение не содержит сравнительного теста быстродействия, поэтому утверждать, что новый плагин ускоряет любую карту, было бы преждевременно.

Уиллисон пишет, что большую часть плагина создал с помощью одного запроса к Claude Fable 5.2, опираясь на существующие расширения. Это его описание процесса разработки, а не измерение надёжности полученного кода. Автор предлагает демонстрацию в актуальном Datasette Lite: плагин и пример базы загружаются в браузере через Pyodide и WebAssembly. Редакция прочитала описание, но самостоятельно не запускала демонстрацию и не проверяла её на разных устройствах. Граница между опубликованной возможностью и нашим тестом здесь существенна.

Другое обновление касается переходов между небольшими приложениями. Datasette Apps — это HTML- и JavaScript-приложения внутри Datasette, которые, согласно описанию автора, могут выполнять SQL-запросы к данным. Версия 0.4a0 позволяет приложению получать и использовать фрагмент адреса после знака решётки. Поддерживаемые схемы адресов также сообщаются Datasette Agent, чтобы он мог помогать создавать связанные приложения. Пример автора — отдельный поиск записей, ведущий в другое приложение с подробностями конкретной записи.

Эти две новости можно связать условным редакционным примером, не приписывая релизам готовую интеграцию. Представьте каталог объектов: карта помогает выбрать интересующую область, а отдельный экран объясняет выбранную запись. Чтобы такой путь был полезен, человеку нужно понимать, какой объект он открыл и как вернуться к исходному выбору. Наличие карты и ссылки само по себе не подтверждает правильность координат, полноту каталога или соответствие записи выбранной точке. Проверять эти свойства придётся на собственных данных.

### Почему это важно

Инструмент исследования становится удобнее, когда обзор и подробности можно соединить понятным переходом. Новые релизы предлагают элементы такого взаимодействия: предварительный показ геометрии и адресуемые состояния приложений. Пользователю стоит оценивать их вместе с качеством исходных данных и ясностью навигации, сохраняя различие между возможностями интерфейса и достоверностью результата.

## English version

Today's digest brings two new ways of presenting data inside Datasette. In his [datasette-maplibre 0.1a0 announcement](https://simonwillison.net/2026/Nov/15/datasette-maplibre/), Simon Willison introduces a geospatial plugin combining MapLibre GL and OpenFreeMap. A separate [datasette-apps 0.4a0 release](https://simonwillison.net/2026/Nov/15/datasette-apps/) adds links between applications. Both primary sources are dated November 15 and were read in full for this November 16 edition. These developments differ from yesterday's model-connection and chart-plugin coverage; the digest date does not replace the original announcement dates.

For the geospatial plugin, Willison highlights how GeoJSON shapes are previewed. SVG previews appear first, with a WebGL preview loaded when the item scrolls into view. His note also links to an example showing shapes and latitude/longitude points on the same map. That offers a way to inspect different geographical representations together. The announcement does not provide a comparative performance benchmark, however, so it would be premature to claim that the plugin makes every map faster or reduces every workload by a measured amount.

Willison says he built most of the plugin with one prompt to Claude Fable 5.2, using existing extensions as references. This is his account of the development process, rather than a reliability assessment of the resulting code. He supplies a demonstration for current Datasette Lite, loading the plugin and a sample database in the browser through Pyodide and WebAssembly. We read the description but did not independently run that demonstration or test it across devices. The distinction between an announced capability and our own verified runtime result remains explicit.

The other update concerns moving between small applications. Datasette Apps are HTML and JavaScript applications within Datasette that, according to the author, can execute SQL queries against the data. Version 0.4a0 lets an application receive and use a URL fragment. Supported URL schemes are also reported to Datasette Agent so it can help build applications that link to each other. Willison's example separates an application that searches records from another that displays the details of an individual record.

A hypothetical editorial example connects the two ideas without claiming a ready-made integration. Imagine a catalogue where a map offers an overview and a separate screen explains a selected entry. For that journey to work, a reader needs to understand which object was opened and how to return to the original selection. Having a map and a link does not establish coordinate accuracy, catalogue completeness or a correct match between the selected point and the record. Those properties require checks against the actual dataset.

### Why it matters

Exploration becomes more useful when an overview and its underlying details can be connected intelligibly. These releases supply pieces of that interaction: geometry previews and addressable application states. Users should assess them alongside source-data quality and clear navigation, keeping interface capabilities separate from confidence in the result.
