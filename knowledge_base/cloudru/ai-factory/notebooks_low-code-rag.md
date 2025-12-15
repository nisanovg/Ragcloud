---
title: Создание Telegram-бота для поиска информации из Jira на основе Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag
topic: ai-factory
---
# Создание Telegram-бота для поиска информации из Jira на основе Notebooks

С помощью этого руководства вы настроите парсинг Jira, создадите базу знаний в сервисе [Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG и разработаете Telegram-бота для интерактивной работы с данными.
В результате вы получите готовое решение для поиска информации в задачах Jira на базе образа N8N в сервисе Notebooks.

Вы будете использовать следующие сервисы:

- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.
- [Jira](https://www.atlassian.com/software/Jira)Jira — инструмент управления проектами для планирования и отслеживания работы в команде.
- [Telegram](https://telegram.org/)Telegram — чат-платформа.
- [N8N](https://n8n.io/)N8N — платформа для автоматизации рабочих процессов и интеграции сервисов.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.

[Jira](https://www.atlassian.com/software/Jira)Jira — инструмент управления проектами для планирования и отслеживания работы в команде.

[Telegram](https://telegram.org/)Telegram — чат-платформа.

[N8N](https://n8n.io/)N8N — платформа для автоматизации рабочих процессов и интеграции сервисов.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Подготовьте среду.
2. [Настройте воркфлоу в N8N для парсинга Jira](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Настройте воркфлоу в N8N для парсинга Jira.
3. [Создайте базу знаний и получите токен доступа](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Создайте базу знаний и получите токен доступа.
4. [Настройте Telegram-бота для взаимодействия с RAG](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Настройте Telegram-бота для взаимодействия с RAG.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Подготовьте среду.

[Настройте воркфлоу в N8N для парсинга Jira](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Настройте воркфлоу в N8N для парсинга Jira.

[Создайте базу знаний и получите токен доступа](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Создайте базу знаний и получите токен доступа.

[Настройте Telegram-бота для взаимодействия с RAG](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)Настройте Telegram-бота для взаимодействия с RAG.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

## 1. Подготовьте среду

1. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
2. [Сгенерируйте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте API-ключ.
3. Для хранения данных [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage.
Укажите класс хранения Стандартный.
4. [Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

Конфигурация — ncpu.medium.4.
Образ — Cloud.ru Jupyter N8n.

После создания ноутбука на главной странице сервиса Notebooks в строке нужного ноутбука нажмите JupyterLab.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.

[Сгенерируйте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте API-ключ.

Для хранения данных [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage.
Укажите класс хранения Стандартный.

[Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

- Конфигурация — ncpu.medium.4.
- Образ — Cloud.ru Jupyter N8n.

Конфигурация — ncpu.medium.4.

Образ — Cloud.ru Jupyter N8n.

После создания ноутбука на главной странице сервиса Notebooks в строке нужного ноутбука нажмите JupyterLab.

## 2. Настройте воркфлоу в N8N для парсинга Jira

На этом шаге вы настроите воркфлоу в N8N для извлечения данных из Jira и преобразования их в текстовый файл.

1. На главной странице JupyterLab в разделе Other нажмите на N8N.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__low-code-rag1.png)
2. Дождитесь загрузки сервиса.
3. Пройдите регистрацию и нажмите Next.
4. (Опционально) Заполните следующую форму и нажмите Get started.
5. Нажмите Create Workflow.
6. Нажмите Add first step.
7. Выберите триггер Trigger manually.
8. Добавьте ноду HTTP Request со следующими параметрами:

Method: GET
URL: http://<jira_ip>/rest/api/2/search?jql=&maxResults=1000
Где <jira_ip> — IP-адрес вашего Jira-сервера.

Authentication: Authentication
Generic Auth Type: Basic Auth
Добавьте credentials — логин и пароль от аккаунта в Jira.
9. Добавьте справа ноду Code, указав Language — JavaScript.
10. В ноду Code добавьте код:

let rows = [];for (const item of items) { if (!item.json || !Array.isArray(item.json.issues)) continue; for (const issue of item.json.issues) { let id = issue.id ?? ''; let key = issue.key ?? ''; let desc = issue.fields?.description ?? ''; let creator = issue.fields?.creator?.name ?? ''; rows.push([id, key, desc, creator].join(',')); }}return [{ json: { text: rows.join('\n\n') } }];
11. Добавьте справа ноду Aggregate.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__low-code-rag3.png)
12. Добавьте ноду Convert to File со следующими параметрами:

Operation: Convert to Text File
Text Input Field: text
Put Output File in Field: data

В результате вы получите файл, в котором будет находиться текстовая выжимка из полей description, id, key, creator.
13. Добавьте полученный файл в бакет Object Storage, [созданный при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданный при подготовке среды.

На главной странице JupyterLab в разделе Other нажмите на N8N.

![../_images/s__low-code-rag1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag1.png)

Дождитесь загрузки сервиса.

Пройдите регистрацию и нажмите Next.

![../_images/s__low-code-rag2.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag2.png)

(Опционально) Заполните следующую форму и нажмите Get started.

Нажмите Create Workflow.

Нажмите Add first step.

Выберите триггер Trigger manually.

Добавьте ноду HTTP Request со следующими параметрами:

- Method: GET
- URL: http://<jira_ip>/rest/api/2/search?jql=&maxResults=1000
Где <jira_ip> — IP-адрес вашего Jira-сервера.
- Authentication: Authentication
- Generic Auth Type: Basic Auth
- Добавьте credentials — логин и пароль от аккаунта в Jira.

Method: GET

URL: http://<jira_ip>/rest/api/2/search?jql=&maxResults=1000

Где <jira_ip> — IP-адрес вашего Jira-сервера.

Authentication: Authentication

Generic Auth Type: Basic Auth

Добавьте credentials — логин и пароль от аккаунта в Jira.

Добавьте справа ноду Code, указав Language — JavaScript.

В ноду Code добавьте код:

```bash
let
rows
=
[
]
;
for
(
const
item
of
items
)
{
if
(
!
item
.
json
||
!
Array
.
isArray
(
item
.
json
.
issues
)
)
continue
;
for
(
const
issue
of
item
.
json
.
issues
)
{
let
id
=
issue
.
id
??
''
;
let
key
=
issue
.
key
??
''
;
let
desc
=
issue
.
fields
?.
description
??
''
;
let
creator
=
issue
.
fields
?.
creator
?.
name
??
''
;
rows
.
push
(
[
id
,
key
,
desc
,
creator
]
.
join
(
','
)
)
;
}
}
return
[
{
json
:
{
text
:
rows
.
join
(
'\n\n'
)
}
}
]
;
```

Добавьте справа ноду Aggregate.

![../_images/s__low-code-rag3.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag3.png)

Добавьте ноду Convert to File со следующими параметрами:

- Operation: Convert to Text File
- Text Input Field: text
- Put Output File in Field: data

Operation: Convert to Text File

Text Input Field: text

Put Output File in Field: data

![../_images/s__low-code-rag4.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag4.png)

В результате вы получите файл, в котором будет находиться текстовая выжимка из полей description, id, key, creator.

Добавьте полученный файл в бакет Object Storage, [созданный при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданный при подготовке среды.

Вы можете продумать, какие поля вам нужны, как лучше расположить данные в файле.
В этом практическом руководстве приведен пример для реализации быстрого старта.

## 3. Создайте базу знаний и получите токен доступа

На этом шаге вы создадите базу знаний в сервисе Managed RAG на основе данных, полученных из Jira.

1. В личном кабинете перейдите в сервис AI → Managed RAG.
2. Нажмите Создать базу знаний.
3. Укажите путь к папке в бакете Object Storage, [созданном при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданном при подготовке среды.
Для обработки ваших файлов будет создан сервисный аккаунт.
4. Выберите расширение загруженных файлов.
5. Активируйте опцию Вручную настроить обработку документов и модель.
6. Включите аутентификацию и выберите сервисный аккаунт, [созданный при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданный при подготовке среды.
7. Нажмите Продолжить.
8. Укажите настройки для экстракторов — парсеры, которые извлекают содержимое из файлов выбранного типа.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__low-code-rag5.png)
9. Нажмите Продолжить.
10. Выберите модель, которая преобразует содержимое документов в векторное представление, например, Qwen/Qwen3-Embedding-0.6B.
11. Нажмите Создать.
Вы будете перенаправлены на страницу сервиса Managed RAG.
База знаний будет создана и запущена в течение нескольких минут.
Дождитесь, когда база знаний перейдет в статус «Активная» и появится публичный URL-адрес.
12. [Создайте токен доступа для запросов к версии базы знаний](https://cloud.ru/docs/rag/ug/topics/guides__access-token)Создайте токен доступа для запросов к версии базы знаний.
13. Скопируйте полученный токен — значение из поля access token.

В личном кабинете перейдите в сервис AI → Managed RAG.

Нажмите Создать базу знаний.

Укажите путь к папке в бакете Object Storage, [созданном при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданном при подготовке среды.
Для обработки ваших файлов будет создан сервисный аккаунт.

Выберите расширение загруженных файлов.

Активируйте опцию Вручную настроить обработку документов и модель.

Включите аутентификацию и выберите сервисный аккаунт, [созданный при подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__low-code-rag)созданный при подготовке среды.

Нажмите Продолжить.

Укажите настройки для экстракторов — парсеры, которые извлекают содержимое из файлов выбранного типа.

![../_images/s__low-code-rag5.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag5.png)

Нажмите Продолжить.

Выберите модель, которая преобразует содержимое документов в векторное представление, например, Qwen/Qwen3-Embedding-0.6B.

Нажмите Создать.

Вы будете перенаправлены на страницу сервиса Managed RAG.
База знаний будет создана и запущена в течение нескольких минут.
Дождитесь, когда база знаний перейдет в статус «Активная» и появится публичный URL-адрес.

[Создайте токен доступа для запросов к версии базы знаний](https://cloud.ru/docs/rag/ug/topics/guides__access-token)Создайте токен доступа для запросов к версии базы знаний.

Скопируйте полученный токен — значение из поля access token.

## 4. Настройте Telegram-бота для взаимодействия с RAG

На этом шаге вы создадите Telegram-бота и настроите его взаимодействие с базой знаний через Managed RAG.

1. Зарегистрируйте бота в Telegram:

В Telegram найдите бота BotFather.
Выполните команду /newbot.
Задайте имя (name) и имя пользователя (username) для бота.
Имя пользователя должно заканчиваться на «Bot» или «_bot».
Сохраните токен бота, который предоставит BotFather.
Убедитесь, что в Telegram созданный бот отображается в результатах поиска по имени.
2. Вернитесь в N8N и в том же воркфлоу выберите Telegram Trigger: Updates message.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__low-code-rag6.png)
3. Создайте credentials, вставив токен вашего бота.
4. Проверьте работоспособность webhook.
5. Добавьте ноду HTTP Request со следующими параметрами:

Method: POST
URL: перейдите в Managed RAG → Название вашей базы знаний → API и скопируйте URL после слова «POST».
Выберите один из методов:

retrieve — если нужны только ссылки.
retrieve_generate — если нужен быстрый ответ и точность не важна.
retrieve_rerank — когда важна точность ранжирования.
retrieve_rerank_generate — точность ранжирования + готовый ответ.

 
 Пример 
 

Добавьте код в формате JSON:

{ "project_id": "<project_id>", "query": "{{ $json.message.text }}", "llm_settings": { "model_settings": { "model": "openai/gpt-oss-120b" }, "system_prompt": "Вы полезный помощник, который отвечает на вопросы, основываясь на предоставленном контексте.", "temperature": 1 }, "retrieve_limit": 3, "n_chunks_in_context": 3, "rag_version": "<your_rag_version>"}

Где:

<project_id> — идентификатор вашего проекта.
<your_access_token> — токен доступа, полученный ранее.
<your_rag_version> — версия RAG из вкладки Информация о версии.

Подробнее о параметрах — [в документации Managed RAG](https://cloud.ru/docs/rag/ug/topics/quickstart)в документации Managed RAG.
6. Отправьте запрос и убедитесь, что получаете корректный ответ от сервиса.
7. Добавьте ноду Telegram send message.
8. В правом верхнем углу установите переключатель в положение Activate.

Зарегистрируйте бота в Telegram:

1. В Telegram найдите бота BotFather.
2. Выполните команду /newbot.
3. Задайте имя (name) и имя пользователя (username) для бота.
Имя пользователя должно заканчиваться на «Bot» или «_bot».
4. Сохраните токен бота, который предоставит BotFather.
5. Убедитесь, что в Telegram созданный бот отображается в результатах поиска по имени.

В Telegram найдите бота BotFather.

Выполните команду /newbot.

Задайте имя (name) и имя пользователя (username) для бота.
Имя пользователя должно заканчиваться на «Bot» или «_bot».

Сохраните токен бота, который предоставит BotFather.

Убедитесь, что в Telegram созданный бот отображается в результатах поиска по имени.

Вернитесь в N8N и в том же воркфлоу выберите Telegram Trigger: Updates message.

![../_images/s__low-code-rag6.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag6.png)

Создайте credentials, вставив токен вашего бота.

![../_images/s__low-code-rag7.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag7.png)

Проверьте работоспособность webhook.

![../_images/s__low-code-rag8.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag8.png)

Добавьте ноду HTTP Request со следующими параметрами:

- Method: POST
- URL: перейдите в Managed RAG → Название вашей базы знаний → API и скопируйте URL после слова «POST».
- Выберите один из методов:

retrieve — если нужны только ссылки.
retrieve_generate — если нужен быстрый ответ и точность не важна.
retrieve_rerank — когда важна точность ранжирования.
retrieve_rerank_generate — точность ранжирования + готовый ответ.

 
 Пример
- Добавьте код в формате JSON:

Method: POST

URL: перейдите в Managed RAG → Название вашей базы знаний → API и скопируйте URL после слова «POST».

Выберите один из методов:

- retrieve — если нужны только ссылки.
- retrieve_generate — если нужен быстрый ответ и точность не важна.
- retrieve_rerank — когда важна точность ранжирования.
- retrieve_rerank_generate — точность ранжирования + готовый ответ.

retrieve — если нужны только ссылки.

retrieve_generate — если нужен быстрый ответ и точность не важна.

retrieve_rerank — когда важна точность ранжирования.

retrieve_rerank_generate — точность ранжирования + готовый ответ.

Добавьте код в формате JSON:

```bash
{
"project_id"
:
"<project_id>"
,
"query"
:
"{{ $json.message.text }}"
,
"llm_settings"
:
{
"model_settings"
:
{
"model"
:
"openai/gpt-oss-120b"
}
,
"system_prompt"
:
"Вы полезный помощник, который отвечает на вопросы, основываясь на предоставленном контексте."
,
"temperature"
:
1
}
,
"retrieve_limit"
:
3
,
"n_chunks_in_context"
:
3
,
"rag_version"
:
"<your_rag_version>"
}
```

Где:

- <project_id> — идентификатор вашего проекта.
- <your_access_token> — токен доступа, полученный ранее.
- <your_rag_version> — версия RAG из вкладки Информация о версии.

<project_id> — идентификатор вашего проекта.

<your_access_token> — токен доступа, полученный ранее.

<your_rag_version> — версия RAG из вкладки Информация о версии.

Подробнее о параметрах — [в документации Managed RAG](https://cloud.ru/docs/rag/ug/topics/quickstart)в документации Managed RAG.

![../_images/s__low-code-rag9.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag9.png)

Отправьте запрос и убедитесь, что получаете корректный ответ от сервиса.

Добавьте ноду Telegram send message.

![../_images/s__low-code-rag10.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag10.png)

В правом верхнем углу установите переключатель в положение Activate.

![../_images/s__low-code-rag11.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag11.png)

Теперь вы можете получать релевантные ответы по своей базе знаний интерактивно прямо в Telegram.

Например, нас интересует информация о деятельносты Ирины Сидоровой.
Такой правильный ответ мы получаем.

![../_images/s__low-code-rag12.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__low-code-rag12.png)

## Результат

В ходе лабораторной работы вы создали LOW-Code RAG-систему на базе данных из Jira, настроили воркфлоу в N8N для извлечения данных, создали базу знаний в Managed RAG и разработали Telegram-бота для интерактивного взаимодействия с информацией.
