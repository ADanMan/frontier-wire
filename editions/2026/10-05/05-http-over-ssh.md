---
date: 2026-10-05
rubric: tech
title_ru: Показать локальный сайт через SSH: два привычных инструмента вместо отдельного клиента
title_en: Showing a local site over SSH: two familiar tools instead of another client
dek_ru: Венсан Берна описал собственный туннель на OpenSSH и nginx; протоколы поясняют, где заканчивается доставка и начинается контроль доступа.
dek_en: Vincent Bernat describes a self-hosted OpenSSH and nginx tunnel; the protocols explain where delivery ends and access control begins.
source: https://vincent.bernat.ch/en/blog/2026-http-over-ssh
generated: true
---

## Русская версия

Венсан Берна [описал 3 октября собственный туннель на OpenSSH и nginx](https://vincent.bernat.ch/en/blog/2026-http-over-ssh). Он позволяет показать локальный сайт через внешний адрес без отдельного специализированного клиента. Это конкретная реализация на существующих инструментах. Чтобы понять её устройство, полезно отдельно посмотреть, какую роль выполняет каждый компонент.

Первую часть объясняет [руководство OpenSSH](https://man.openbsd.org/ssh). Удалённое перенаправление создаёт слушающий порт на сервере и передаёт соединения через защищённый канал к назначению на стороне клиента. При выборе номера порта 0 сервер выделяет свободный номер динамически. По умолчанию серверный TCP-порт слушает только loopback-интерфейс, то есть не становится напрямую доступным всему интернету.

Вторая часть — обычное проксирование. [Документация nginx](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) описывает передачу HTTP-запроса другому серверу с заданным протоколом, адресом и портом. В таком сочетании nginx принимает внешний запрос и отправляет его на серверный конец SSH-перенаправления. Ответ возвращается тем же путём. Так разделяются публичная точка входа и транспорт к локальному приложению.

Однако появление внешнего адреса ещё не отвечает на вопрос, кому разрешено им пользоваться. [Модуль Secure Link](https://nginx.org/en/docs/http/ngx_http_secure_link_module.html) проверяет подлинность ссылки и может ограничивать время её действия. Проверка срока позволяет отличить отсутствующее или неверное подтверждение от уже просроченного. Модуль не включён в сборку nginx по умолчанию — это отдельное условие для реализации, которая на него опирается.

Есть и другой механизм. [HTTP Basic Authentication в nginx](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html) ограничивает доступ проверкой имени пользователя и пароля. Сам протокол, согласно [RFC 7617](https://www.rfc-editor.org/rfc/rfc7617), не защищает эти сведения без внешнего защищённого транспорта, например TLS. Поэтому доставка по SSH на одном участке и защита браузерного соединения решают разные части задачи.

Берна публикует конфигурацию и вспомогательный скрипт, объединяющие элементы в схему со ссылкой ограниченного срока. Это реализация автора; поведение её компонентов поясняют приведённые первичные документы.

Практический вывод из разделения ролей — удобство и доступ нужно оценивать независимо. Возможность открыть страницу из браузера проверяет маршрут. Возможность закрыть её после завершения просмотра проверяет другое свойство. Это полезное различие даже для короткой демонстрации: «сайт доступен» и «сайт доступен только нужным людям в нужное время» описывают разные требования.

### Почему это важно

Пример показывает, как знакомые протоколы складываются в небольшой сервис для совместной работы. Привлекательность такого варианта зависит от уже имеющегося сервера и готовности его обслуживать; собственного хостинга недостаточно, чтобы автоматически получить все удобства готового сервиса. Оценивать стоит понятность каждой границы: где принимается запрос, куда он передаётся и чем подтверждается право доступа. Эта схема помогает задавать вопросы к реализации, не заменяя проверку самой конфигурации.

## English version

Vincent Bernat [described a self-hosted OpenSSH and nginx tunnel on October 3](https://vincent.bernat.ch/en/blog/2026-http-over-ssh). It makes a local website reachable through an external address without a separate specialist client. This is a particular implementation using established tools. Understanding it means examining the distinct role of each component.

The first part is documented in the [OpenSSH manual](https://man.openbsd.org/ssh). Remote forwarding creates a listening port on the server and carries connections over the secure channel to a destination reached from the client. Choosing port 0 makes the server allocate an available number dynamically. By default, the server-side TCP listener binds only to loopback, so that port is not directly exposed to the whole internet.

The second part is ordinary proxying. The [nginx documentation](https://nginx.org/en/docs/http/ngx_http_proxy_module.html) describes passing HTTP requests to another server using a specified protocol, address and port. In this arrangement, nginx receives the external request and sends it to the server end of the SSH forward. The response returns along the same route. The public entry point and the transport to the local application have distinct roles.

An external address does not, however, decide who may use it. The [Secure Link module](https://nginx.org/en/docs/http/ngx_http_secure_link_module.html) checks a link's authenticity and can restrict its lifetime. Its expiry check distinguishes missing or invalid confirmation from a link whose validity has ended. The module is not built into nginx by default, which is a separate prerequisite for an implementation that depends on it.

Another mechanism is [nginx HTTP Basic Authentication](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html), which checks a username and password to restrict access. As [RFC 7617](https://www.rfc-editor.org/rfc/rfc7617) explains, that protocol does not protect those credentials without an external secure transport such as TLS. Securing the SSH segment and protecting the browser's connection therefore address different parts of the path.

Bernat publishes a configuration and helper script combining these pieces into a scheme with a time-limited link. That is his implementation; the primary documents linked here explain its components' behaviour.

The practical inference is to assess convenience and access independently. Opening the page from a browser checks the route. Closing access after the review checks another property. Even for a short demonstration, “the site is reachable” and “the right people can reach it for the intended period” are distinct requirements.

### Why it matters

The example shows familiar protocols forming a small collaboration service. Its appeal depends on an existing server and willingness to maintain it; self-hosting does not automatically reproduce every convenience of a managed service. The useful questions concern each boundary: where a request arrives, where it goes next and how access is authorised. Understanding that division helps evaluate a design without substituting for verification of the actual configuration.
