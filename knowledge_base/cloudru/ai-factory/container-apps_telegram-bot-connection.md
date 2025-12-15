---
title: Подключение ИИ из Foundation Models к nocode Telegram-боту на основе Container Apps или Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection
topic: ai-factory
---
# Подключение ИИ из Foundation Models к nocode Telegram-боту на основе Container Apps или Notebooks

С помощью этого руководства вы запустите приложение n8n в Container Apps или в Notebooks.
На базе этого приложения создадите Telegram-бота, который будет интегрирован с сервисом Foundation Models.

С помощью Foundation Models вы сможете отправлять запросы в различные AI-модели и обрабатывать пользовательские запросы.

В рамках этого сценария мы будем оценивать эмоциональный окрас сообщения пользователя.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
Будет использоваться в качестве хранилища для контейнера.
- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [n8n](https://n8n.io/)n8n — платформа с открытым кодом для автоматизации рабочих процессов и интеграции сервисов. Подходит для экспериментов и пет-проектов.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
Будет использоваться в качестве хранилища для контейнера.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[n8n](https://n8n.io/)n8n — платформа с открытым кодом для автоматизации рабочих процессов и интеграции сервисов. Подходит для экспериментов и пет-проектов.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Подготовьте среду.
2. [Создайте Telegram-бота с помощью n8n и Container Apps](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Создайте Telegram-бота с помощью n8n и Container Apps.
3. [Удалите шаг отправки сообщения пользователю](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Удалите шаг отправки сообщения пользователю.
4. [Добавьте и настройте клиент OpenAI для подключения к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Добавьте и настройте клиент OpenAI для подключения к Foundation Models.
5. [Отправьте ответ модели в Telegram-бот](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Отправьте ответ модели в Telegram-бот.
6. [Проверьте работу бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Проверьте работу бота.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Подготовьте среду.

[Создайте Telegram-бота с помощью n8n и Container Apps](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Создайте Telegram-бота с помощью n8n и Container Apps.

[Удалите шаг отправки сообщения пользователю](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Удалите шаг отправки сообщения пользователю.

[Добавьте и настройте клиент OpenAI для подключения к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Добавьте и настройте клиент OpenAI для подключения к Foundation Models.

[Отправьте ответ модели в Telegram-бот](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Отправьте ответ модели в Telegram-бот.

[Проверьте работу бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)Проверьте работу бота.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.
2. Убедитесь, что у вас есть доступ к Foundation Models.
3. Убедитесь, что баланс в личном кабинете положительный.
Если он нулевой или отрицательный — [пополните баланс](https://cloud.ru/docs/billing/ug/topics/guides__payment_fl)пополните баланс.
Небольшое количество запросов в Foundation Models будет стоить не больше рубля, подробнее — [в тарифах](https://cloud.ru/documents/tariffs/evolution/foundation-models.html)в тарифах.
4. [Создайте сервисный аккаунт и API-ключ для аутентификации в API Foundation Models](https://cloud.ru/docs/foundation-models/ug/topics/api-ref__authentication)Создайте сервисный аккаунт и API-ключ для аутентификации в API Foundation Models.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.

Убедитесь, что у вас есть доступ к Foundation Models.

Убедитесь, что баланс в личном кабинете положительный.
Если он нулевой или отрицательный — [пополните баланс](https://cloud.ru/docs/billing/ug/topics/guides__payment_fl)пополните баланс.
Небольшое количество запросов в Foundation Models будет стоить не больше рубля, подробнее — [в тарифах](https://cloud.ru/documents/tariffs/evolution/foundation-models.html)в тарифах.

[Создайте сервисный аккаунт и API-ключ для аутентификации в API Foundation Models](https://cloud.ru/docs/foundation-models/ug/topics/api-ref__authentication)Создайте сервисный аккаунт и API-ключ для аутентификации в API Foundation Models.

## 2. Создайте Telegram-бота с помощью n8n и Container Apps

Выполните сценарий, описанный в практическом руководстве [Создание Telegram-бота без написания кода с помощью n8n и Container Apps или Notebooks](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__nocode-telegram-bot)Создание Telegram-бота без написания кода с помощью n8n и Container Apps или Notebooks.

Тестовый образ n8n создан в версии [n8n@1.116.2](https://docs.n8n.io/release-notes)n8n@1.116.2.
Если вы создаете и разворачиваете кастомный образ, рекомендуется использовать версию n8n 1.116.2 для стабильной работы образа с Container Apps и Foundation Models.

## 3. Удалите шаг отправки сообщения пользователю

Бот будет отправлять ответ от LLM-модели.
Поэтому отправка ботом пользователю его же сообщения больше не нужна.
Удалите последний шаг SEND A TEXT MESSAGE в созданном рабочем процессе.

## 4. Добавьте и настройте клиент OpenAI для подключения к Foundation Models

1. Справа от действия Send a chat action нажмите +.
2. На вкладке справа в поле поиска введите openai и выберите OpenAI в результатах поиска.
3. В списке выберите Message a model.
4. В окне свойств действия нажмите иконку карандаша рядом с полем Credential to connect with.
5. В поле API Key введите API-ключ, полученный на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)подготовки среды.
6. В поле Organization ID (optional) введите [идентификатор вашего проекта](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)идентификатор вашего проекта.
7. В поле Base URL введите https://foundation-models.api.cloud.ru/v1.
8. Нажмите Save и закройте окно учетных данных OpenAI.
9. В окне свойств действия раскройте выпадающий список Model, выберите By ID и введите название модели openai/gpt-oss-120b.
10. В секции Messages в поле Prompt введите:
{{ $('Telegram Trigger').item.json.message.text }}
11. Нажмите Add Message.
12. В выпадающем списке Role выберите System.
13. В поле Prompt для добавленного сообщения вставьте:
You are an expert in text sentiment analysis. When solving a task, FIRST think step-by-step in private to reach your answer. Do NOT reveal these private thoughts. Instead, output ONLY a JSON object with three keys: 1. "result" – one of: "positive", "negative", "neutral" 2. "confidence" – number between 0 and 1 (e.g. 0.87). Calibrate it so the three classes are equally likely a priori. 3. "explanation" – a brief, public rationale (1-3 sentences) that cites the pivotal phrases.Use Russian language to provide explanation. Follow the format of the few-shot examples exactly: nothing before or after the JSON. Don't use json

ПримечаниеС помощью промта модель анализирует эмоциональный окрас сообщения и возвращает ответ в формате JSON.
Он содержит три поля:
result — результат оценки эмоционального окраса сообщения: негативный, нейтральный или позитивный;
confidence — уверенность в оценке от 0 до 1;
explanation — объяснение оценки.
14. Включите опцию Output Content as JSON.
15. Сверху нажмите Test step.
16. Нажмите Back to canvas.

Справа от действия Send a chat action нажмите +.

На вкладке справа в поле поиска введите openai и выберите OpenAI в результатах поиска.

В списке выберите Message a model.

В окне свойств действия нажмите иконку карандаша рядом с полем Credential to connect with.

В поле API Key введите API-ключ, полученный на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)подготовки среды.

В поле Organization ID (optional) введите [идентификатор вашего проекта](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)идентификатор вашего проекта.

В поле Base URL введите https://foundation-models.api.cloud.ru/v1.

Нажмите Save и закройте окно учетных данных OpenAI.

В окне свойств действия раскройте выпадающий список Model, выберите By ID и введите название модели openai/gpt-oss-120b.

![../_images/tg-bot-connect-model-n8n.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/tg-bot-connect-model-n8n.webp)

В секции Messages в поле Prompt введите:

```bash
{
{
$(
'Telegram Trigger'
)
.item.json.message.text
}
}
```

Нажмите Add Message.

В выпадающем списке Role выберите System.

В поле Prompt для добавленного сообщения вставьте:

```bash
You are an expert
in
text sentiment analysis. When solving a task, FIRST think step-by-step
in
private to reach your answer. Do NOT reveal these private thoughts. Instead, output ONLY a JSON object with three keys:
1
.
"result"
– one of:
"positive"
,
"negative"
,
"neutral"
2
.
"confidence"
– number between
0
and
1
(
e.g.
0.87
)
. Calibrate it so the three classes are equally likely a priori.
3
.
"explanation"
– a brief, public rationale
(
1
-3 sentences
)
that cites the pivotal phrases.Use Russian language to provide explanation. Follow the
format
of the few-shot examples exactly: nothing before or after the JSON. Don't use json
```

С помощью промта модель анализирует эмоциональный окрас сообщения и возвращает ответ в формате JSON.
Он содержит три поля:

- result — результат оценки эмоционального окраса сообщения: негативный, нейтральный или позитивный;
- confidence — уверенность в оценке от 0 до 1;
- explanation — объяснение оценки.

result — результат оценки эмоционального окраса сообщения: негативный, нейтральный или позитивный;

confidence — уверенность в оценке от 0 до 1;

explanation — объяснение оценки.

Включите опцию Output Content as JSON.

Сверху нажмите Test step.

Нажмите Back to canvas.

## 5. Отправьте ответ модели в Telegram-бот

Добавьте новое действие для стартового триггера Telegram:

1. Справа от действия, [добавленного на шаге 4](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)добавленного на шаге 4, нажмите +.
2. На вкладке справа в поле поиска введите telegram и выберите Telegram.
3. В списке выберите Send a text message.
4. В окне свойств действия измените наименование действия на Отправляем ответ.
5. В поле Chat ID вставьте:
{{ $('Telegram Trigger').item.json.message.chat.id }}
6. В поле Text вставьте:
Эмоциональный окрас сообщения --- {{ $json.message.content.result }}Объяснение решения --- {{ $json.message.content.explanation }}
7. Нажмите Add Field и выберите Reply To Message ID.
8. Слева найдите раздел Telegram Trigger и перетащите оттуда параметр message | message_id в поле добавленного параметра Reply To Message ID.
9. Нажмите Test step.
Справа вы увидите тело отправленного сообщения, а в Telegram-бот должно прийти тестовое сообщение с ответом.
10. Нажмите Back to canvas.

Справа от действия, [добавленного на шаге 4](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot-connection)добавленного на шаге 4, нажмите +.

На вкладке справа в поле поиска введите telegram и выберите Telegram.

В списке выберите Send a text message.

В окне свойств действия измените наименование действия на Отправляем ответ.

В поле Chat ID вставьте:

```bash
{
{
$(
'Telegram Trigger'
)
.item.json.message.chat.id
}
}
```

В поле Text вставьте:

```bash
Эмоциональный окрас сообщения ---
{
{
$json
.message.content.result
}
}
Объяснение решения ---
{
{
$json
.message.content.explanation
}
}
```

Нажмите Add Field и выберите Reply To Message ID.

Слева найдите раздел Telegram Trigger и перетащите оттуда параметр message | message_id в поле добавленного параметра Reply To Message ID.

Нажмите Test step.

Справа вы увидите тело отправленного сообщения, а в Telegram-бот должно прийти тестовое сообщение с ответом.

Нажмите Back to canvas.

## 6. Проверьте работу бота

1. Сверху проверьте, что переключатель находится в состоянии Active.
2. Перейдите в Telegram-бот и отправьте любой вопрос.
Должен вернуться ответ от подключенной LLM.

Сверху проверьте, что переключатель находится в состоянии Active.

Перейдите в Telegram-бот и отправьте любой вопрос.
Должен вернуться ответ от подключенной LLM.

## Результат

Вы создали Telegram-бота в Container Apps или Notebooks, который интегрирован с сервисом Foundation Models и может отправлять запросы в различные AI-модели.
Решение можно использовать для автоматического уведомления о новых комментариях на сайте и об их эмоциональном окрасе.
