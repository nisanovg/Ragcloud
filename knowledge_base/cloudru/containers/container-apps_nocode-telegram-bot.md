---
title: Создание Telegram-бота без написания кода с помощью n8n на основе Container Apps или Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot
topic: containers
---
# Создание Telegram-бота без написания кода с помощью n8n на основе Container Apps или Notebooks

С помощью этого руководства вы развернете платформу для создания рабочих процессов без написания кода и создадите Telegram-бота, который будет повторять сообщения пользователя.

Вы можете развернуть платформу на основе сервиса Container Apps или Notebooks.

Вы будете использовать следующие сервисы:

- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
Будет использоваться в качестве постоянного хранилища для запущенного контейнера.
- [n8n](https://n8n.io/)n8n — платформа с открытым кодом для автоматизации рабочих процессов и интеграции сервисов. Подходит для экспериментов и пет-проектов.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
Будет использоваться в качестве постоянного хранилища для запущенного контейнера.

[n8n](https://n8n.io/)n8n — платформа с открытым кодом для автоматизации рабочих процессов и интеграции сервисов. Подходит для экспериментов и пет-проектов.

Шаги:

1. [Создайте бакет в сервисе Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте бакет в сервисе Object Storage.
2. [Создайте контейнер / ноутбук с образом n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте контейнер / ноутбук с образом n8n.
3. [Зарегистрируйте бота в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Зарегистрируйте бота в Telegram.
4. [Запустите n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Запустите n8n.
5. [Настройте параметры подключения к Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Настройте параметры подключения к Telegram.
6. [Создайте триггер Telegram в n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте триггер Telegram в n8n.
7. [Добавьте в чат статус «… печатает / … typing»](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Добавьте в чат статус «… печатает / … typing».
8. [Настройте ответ пользователю от бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Настройте ответ пользователю от бота.
9. [Убедитесь, что бот работает](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Убедитесь, что бот работает.

[Создайте бакет в сервисе Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте бакет в сервисе Object Storage.

[Создайте контейнер / ноутбук с образом n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте контейнер / ноутбук с образом n8n.

[Зарегистрируйте бота в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Зарегистрируйте бота в Telegram.

[Запустите n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Запустите n8n.

[Настройте параметры подключения к Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Настройте параметры подключения к Telegram.

[Создайте триггер Telegram в n8n](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создайте триггер Telegram в n8n.

[Добавьте в чат статус «… печатает / … typing»](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Добавьте в чат статус «… печатает / … typing».

[Настройте ответ пользователю от бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Настройте ответ пользователю от бота.

[Убедитесь, что бот работает](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Убедитесь, что бот работает.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Создайте бакет в сервисе Object Storage

В сервисе Object Storage [создайте новый бакет](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте новый бакет со следующими параметрами:

- Название — <your_name>-n8n, например name-n8n.
- Доменное имя — <your_name>-n8n, например name-n8n.
- Класс хранения по умолчанию — Стандартный.
- Максимальный размер — отключите или укажите на свое усмотрение.

Название — <your_name>-n8n, например name-n8n.

Доменное имя — <your_name>-n8n, например name-n8n.

Класс хранения по умолчанию — Стандартный.

Максимальный размер — отключите или укажите на свое усмотрение.

Убедитесь, что в личном кабинете на странице сервиса Object Storage:

- в списке бакетов отображается созданный вами бакет;
- класс хранения — Стандартный.

в списке бакетов отображается созданный вами бакет;

класс хранения — Стандартный.

## 2. Создайте контейнер / ноутбук с образом n8n

В личном кабинете создайте контейнер n8n из готового образа с помощью Container Apps:

Тестовый образ n8n создан в версии [n8n@1.116.2](https://docs.n8n.io/release-notes)n8n@1.116.2.
Если вы создаете и разворачиваете кастомный образ, рекомендуется использовать версию n8n 1.116.2 для стабильной работы образа с Container Apps.

1. Перейдите на страницу сервиса Container Apps, выберите Container Services и нажмите Создать.
2. Укажите Название создаваемого Container Service, например container-app-n8n-name.
3. Включите Тестовый образ и выберите Ворклфлоу-приложение на n8n.
На вкладке Общие параметры отобразятся параметры тестового образа:

Конфигурация — 0.2 vCPU - 512 RAM.
Название контейнера, например n8n-container.
Порт контейнера — 5678.

Тестовый образ содержит следующие переменные:

Ключ — N8N_PROTOCOL, Значение — https.
Ключ — N8N_HOST, Значение — <container_app_name>.containerapps.ru, например container-app-n8n-name.containerapps.ru.
Ключ — WEBHOOK_URL, Значение — https://<container_app_name>.containerapps.ru, например https://container-app-n8n-name.containerapps.ru.
Ключ — GENERIC_TIMEZONE, Значение — Europe/Moscow или другая временная зона.

Переменные не отображаются в мастере создания контейнера.
4. На вкладке Тома создайте новый том со следующими параметрами:

Тип — Постоянный.
Название — например n8n-volume.
Бакет из Object Storage — выберите бакет сервиса Object Storage, который вы создали [на шаге 1](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 1.
Путь (path) — /synced/n8n.
5. Нажмите Следующий шаг.
6. В поле Мин. кол-во экземпляров укажите значение 1.
7. Нажмите Создать.
8. Убедитесь, что в личном кабинете на странице созданного Container Service:

отображается одна ревизия;
статус ревизии — «Создается».
9. Дождитесь, когда статус ревизии изменится на «Выполняется».

Перейдите на страницу сервиса Container Apps, выберите Container Services и нажмите Создать.

Укажите Название создаваемого Container Service, например container-app-n8n-name.

Включите Тестовый образ и выберите Ворклфлоу-приложение на n8n.
На вкладке Общие параметры отобразятся параметры тестового образа:

- Конфигурация — 0.2 vCPU - 512 RAM.
- Название контейнера, например n8n-container.
- Порт контейнера — 5678.

Конфигурация — 0.2 vCPU - 512 RAM.

Название контейнера, например n8n-container.

Порт контейнера — 5678.

![../_images/test_image_n8n_container.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/test_image_n8n_container.webp)

Тестовый образ содержит следующие переменные:

- Ключ — N8N_PROTOCOL, Значение — https.
- Ключ — N8N_HOST, Значение — <container_app_name>.containerapps.ru, например container-app-n8n-name.containerapps.ru.
- Ключ — WEBHOOK_URL, Значение — https://<container_app_name>.containerapps.ru, например https://container-app-n8n-name.containerapps.ru.
- Ключ — GENERIC_TIMEZONE, Значение — Europe/Moscow или другая временная зона.

Ключ — N8N_PROTOCOL, Значение — https.

Ключ — N8N_HOST, Значение — <container_app_name>.containerapps.ru, например container-app-n8n-name.containerapps.ru.

Ключ — WEBHOOK_URL, Значение — https://<container_app_name>.containerapps.ru, например https://container-app-n8n-name.containerapps.ru.

Ключ — GENERIC_TIMEZONE, Значение — Europe/Moscow или другая временная зона.

Переменные не отображаются в мастере создания контейнера.

На вкладке Тома создайте новый том со следующими параметрами:

- Тип — Постоянный.
- Название — например n8n-volume.
- Бакет из Object Storage — выберите бакет сервиса Object Storage, который вы создали [на шаге 1](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 1.
- Путь (path) — /synced/n8n.

Тип — Постоянный.

Название — например n8n-volume.

Бакет из Object Storage — выберите бакет сервиса Object Storage, который вы создали [на шаге 1](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 1.

Путь (path) — /synced/n8n.

![../_images/container-volume.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/container-volume.webp)

Нажмите Следующий шаг.

В поле Мин. кол-во экземпляров укажите значение 1.

Нажмите Создать.

Убедитесь, что в личном кабинете на странице созданного Container Service:

- отображается одна ревизия;
- статус ревизии — «Создается».

отображается одна ревизия;

статус ревизии — «Создается».

Дождитесь, когда статус ревизии изменится на «Выполняется».

![../_images/container-exist.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/container-exist.png)

## 3. Зарегистрируйте бота в Telegram

Для работы вам потребуется зарегистрировать нового бота в Telegram и получить токен для него.

1. В Telegram найдите бота [BotFather](https://t.me/BotFather)BotFather.
2. Выполните команду /newbot.
3. Задайте для бота имя (name) и имя пользователя (username).
Имя пользователя должно оканчиваться на Bot или _bot.
В нашем случае:

name: new-bot
username: nocodelabbot

В Telegram найдите бота [BotFather](https://t.me/BotFather)BotFather.

Выполните команду /newbot.

Задайте для бота имя (name) и имя пользователя (username).

Имя пользователя должно оканчиваться на Bot или _bot.

В нашем случае:

- name: new-bot
- username: nocodelabbot

name: new-bot

username: nocodelabbot

В результате вы получите токен.
Сохраните его — он потребуется на следующих этапах.

Токен является секретом.
Не публикуйте его и не передавайте третьим лицам.

## 4. Запустите n8n

Со страницы созданного [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 2 Container Service:

1. Нажмите на публичный URL.
Откроется интерфейс сервиса n8n с формой регистрации нового пользователя.
2. Заполните поля формы регистрации и нажмите Next.
3. В следующих окнах нажмите Get Started и Skip.

Нажмите на публичный URL.

Откроется интерфейс сервиса n8n с формой регистрации нового пользователя.

Заполните поля формы регистрации и нажмите Next.

В следующих окнах нажмите Get Started и Skip.

После регистрации в n8n вы будете перенаправлены в веб-интерфейс n8n.

## 5. Настройте параметры подключения к Telegram

В личном кабинете n8n создайте и настройте учетные данные для подключения к Telegram:

1. В правом верхнем углу личного кабинета раскройте меню Create Workflow и выберите Create Credentials.
2. В следующем окне в качестве типа создаваемой учетной записи выберите Telegram API и нажмите Continue.
Откроется диалоговое окно создания учетной записи.
3. В поле Access Token вставьте токен бота, полученный [на шаге 3](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 3.
4. В правом верхнем углу диалогового окна нажмите Save.
5. Дождитесь, когда вверху окна появится подтверждение об успешном тестовом подключении, и закройте диалоговое окно.

В правом верхнем углу личного кабинета раскройте меню Create Workflow и выберите Create Credentials.

В следующем окне в качестве типа создаваемой учетной записи выберите Telegram API и нажмите Continue.

Откроется диалоговое окно создания учетной записи.

В поле Access Token вставьте токен бота, полученный [на шаге 3](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 3.

![../_images/n8n-token.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-token.png)

В правом верхнем углу диалогового окна нажмите Save.

Дождитесь, когда вверху окна появится подтверждение об успешном тестовом подключении, и закройте диалоговое окно.

При ошибках в работе n8n обращайтесь к [документации разработчика n8n](https://docs.n8n.io/)документации разработчика n8n.

## 6. Создайте триггер Telegram в n8n

В личном кабинете n8n создайте триггер для Telegram-бота:

1. В правом верхнем углу личного кабинета нажмите Create Workflow.
2. В центре рабочей области My workflow нажмите Add first step.
3. На вкладке выбора триггеров в поле поиска введите telegram и выберите Telegram в результатах поиска.
4. В появившемся списке выберите On message.
5. В открывшемся диалоговом окне убедитесь, что в поле Credential to connect with выбрана учетная запись, созданная [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 5.
6. Чтобы закрыть диалоговое окно, в левом верхнем углу интерфейса нажмите Back to canvas.
В центре рабочей области появится блок Telegram Trigger с новым триггером.
7. Нажмите дважды на добавленный триггер.
8. В открывшемся окне свойств триггера нажмите Execute step или Test step, в зависимости от версии n8n.
9. Нажмите Execute step.
Слева появится всплывающее уведомление о том, что n8n отслеживает сообщения, отправленные в Telegram-бота.
10. Отправьте любое сообщение в Telegram-бота.

В правом верхнем углу личного кабинета нажмите Create Workflow.

В центре рабочей области My workflow нажмите Add first step.

На вкладке выбора триггеров в поле поиска введите telegram и выберите Telegram в результатах поиска.

![../_images/n8n-trigger.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-trigger.png)

В появившемся списке выберите On message.

В открывшемся диалоговом окне убедитесь, что в поле Credential to connect with выбрана учетная запись, созданная [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 5.

![../_images/n8n-onmessage.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-onmessage.png)

Чтобы закрыть диалоговое окно, в левом верхнем углу интерфейса нажмите Back to canvas.

В центре рабочей области появится блок Telegram Trigger с новым триггером.

Нажмите дважды на добавленный триггер.

В открывшемся окне свойств триггера нажмите Execute step или Test step, в зависимости от версии n8n.

Нажмите Execute step.

Слева появится всплывающее уведомление о том, что n8n отслеживает сообщения, отправленные в Telegram-бота.

![../_images/n8n-tg-notification.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-tg-notification.png)

Отправьте любое сообщение в Telegram-бота.

После этого на странице триггера в секции Output появятся данные отправленного сообщения.

![../_images/n8n-message-data.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-message-data.png)

## 7. Добавьте в чат статус «… печатает / … typing»

1. Нажмите Back to canvas.
2. Нажмите + справа от стартового триггера.
3. На вкладке выбора триггеров введите в поле поиска telegram и выберите Telegram в результатах поиска.
4. В появившемся списке выберите Send a chat action.
5. В открывшемся диалоговом окне убедитесь, что:

в поле Credential to connect with выбрана учетная запись, которую вы создали [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 5;
в левой области окна отображены параметры, которые вы получили [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 6 для стартового триггера, после того как нажали Execute step.

Если вы не видите этих данных, то нажмите Back to canvas, повторно откройте стартовый триггер и протестируйте шаг.
6. Перетащите параметр message | chat | id в поле Chat ID.
7. Нажмите Execute step.
В правой части окна отобразится результат выполнения true.

Нажмите Back to canvas.

Нажмите + справа от стартового триггера.

На вкладке выбора триггеров введите в поле поиска telegram и выберите Telegram в результатах поиска.

В появившемся списке выберите Send a chat action.

В открывшемся диалоговом окне убедитесь, что:

- в поле Credential to connect with выбрана учетная запись, которую вы создали [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 5;
- в левой области окна отображены параметры, которые вы получили [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 6 для стартового триггера, после того как нажали Execute step.

в поле Credential to connect with выбрана учетная запись, которую вы создали [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 5;

в левой области окна отображены параметры, которые вы получили [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на шаге 6 для стартового триггера, после того как нажали Execute step.

![../_images/n8n-check-trigger.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-check-trigger.png)

Если вы не видите этих данных, то нажмите Back to canvas, повторно откройте стартовый триггер и протестируйте шаг.

Перетащите параметр message | chat | id в поле Chat ID.

![../_images/n8n-dnd-id.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-dnd-id.png)

Нажмите Execute step.

В правой части окна отобразится результат выполнения true.

## 8. Настройте ответ пользователю от бота

Настройте бота, чтобы он отправлял текст сообщения пользователя обратно:

1. Нажмите Back to canvas.
2. Нажмите + справа от созданного [на предыдущем шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на предыдущем шаге действия Send a chat action.
3. В открывшейся справа вкладке вновь найдите и выберите Telegram.
4. В списке Actions выберите Send a text message.
5. В открывшемся диалоговом окне введите параметры:

Chat ID — укажите {{ $node["Telegram Trigger"].json["message"]["chat"]["id"] }};
Text — укажите {{ $node["Telegram Trigger"].json["message"]["text"] }}.
6. Чтобы вернуться к рабочей области, в левом верхнем углу нажмите Back to canvas.
7. В верхней строке нажмите Save.
8. В верхней строке активируйте бот.

Нажмите Back to canvas.

Нажмите + справа от созданного [на предыдущем шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)на предыдущем шаге действия Send a chat action.

В открывшейся справа вкладке вновь найдите и выберите Telegram.

В списке Actions выберите Send a text message.

В открывшемся диалоговом окне введите параметры:

- Chat ID — укажите {{ $node["Telegram Trigger"].json["message"]["chat"]["id"] }};
- Text — укажите {{ $node["Telegram Trigger"].json["message"]["text"] }}.

Chat ID — укажите {{ $node["Telegram Trigger"].json["message"]["chat"]["id"] }};

Text — укажите {{ $node["Telegram Trigger"].json["message"]["text"] }}.

![../_images/n8n-parameters.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-parameters.png)

Чтобы вернуться к рабочей области, в левом верхнем углу нажмите Back to canvas.

В верхней строке нажмите Save.

В верхней строке активируйте бот.

![../_images/n8n-active.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/n8n-active.png)

Созданный вами Telegram-бот активирован.

## 9. Убедитесь, что бот работает

Отправьте в Telegram любое сообщение боту.
Бот должен прислать обратно ваше сообщение.

![../_images/check-bot.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/check-bot.png)

## Результат

Вы развернули платформу для создания рабочих процессов без написания кода в сервисе Container Apps или Notebooks и создали с ее помощью Telegram-бота.

Дальше вы можете:

- настроить логику работы бота с помощью действий, доступных в n8n;
- [добавить интеграцию с LLM](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)добавить интеграцию с LLM.

настроить логику работы бота с помощью действий, доступных в n8n;

[добавить интеграцию с LLM](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)добавить интеграцию с LLM.
