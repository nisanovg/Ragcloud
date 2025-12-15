---
title: Запуск Telegram-бота на Python в контейнере
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot
topic: containers
---
# Запуск Telegram-бота на Python в контейнере

С помощью этого руководства вы запустите Telegram-бота на Python в контейнере.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- Систему контроля версий GitVerse.
В GitVerse находится готовый образ Telegram-бота.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

Систему контроля версий GitVerse.
В GitVerse находится готовый образ Telegram-бота.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Подготовьте среду.
2. [Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Клонируйте или скачайте репозиторий кода c GitVerse.
3. [Зарегистрируйте Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Зарегистрируйте Telegram-бота.
4. [Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Соберите образ и присвойте тег.
5. [Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Загрузите Docker-образ в реестр.
6. [Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Создайте и запустите контейнер.
7. [Добавьте вебхук в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Добавьте вебхук в Telegram.
8. [Проверьте работу Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Проверьте работу Telegram-бота.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Подготовьте среду.

[Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Клонируйте или скачайте репозиторий кода c GitVerse.

[Зарегистрируйте Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Зарегистрируйте Telegram-бота.

[Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Соберите образ и присвойте тег.

[Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Загрузите Docker-образ в реестр.

[Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Создайте и запустите контейнер.

[Добавьте вебхук в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Добавьте вебхук в Telegram.

[Проверьте работу Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__telegram-bot)Проверьте работу Telegram-бота.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.

## 2. (Опционально) Клонируйте или скачайте репозиторий кода c GitVerse

Вы можете зарегистрироваться в [GitVerse](https://gitverse.ru/)GitVerse, если у вас еще нет аккаунта, и познакомиться с новой системой контроля версий. Этот шаг необязательный и не влияет на дальнейшее прохождение сценария.

В этом репозитории находится готовый образ Telegram-бота на языке Python.

```bash
git
clone https://gitverse.ru/cloudru/evo-containerapp-telegrambot-webhook-python-sample
```

## 3. Зарегистрируйте Telegram-бота

1. В Telegram найдите [BotFather](https://t.me/BotFather)BotFather.
2. Выполните команду /newbot.
3. Задайте имя (name) и имя пользователя (username) для бота.
Имя пользователя должно оканчиваться на ...Bot или ..._bot.
В нашем случае:

name: new-bot
username: botforlabbot

В результате вы получите токен. Сохраните его — он потребуется на следующих этапах.
4. С помощью команды /setuserpic установите иконку для вашего бота.

В Telegram найдите [BotFather](https://t.me/BotFather)BotFather.

![../_images/search-botfather.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/search-botfather.png)

Выполните команду /newbot.

Задайте имя (name) и имя пользователя (username) для бота.

Имя пользователя должно оканчиваться на ...Bot или ..._bot.

В нашем случае:

- name: new-bot
- username: botforlabbot

name: new-bot

username: botforlabbot

В результате вы получите токен. Сохраните его — он потребуется на следующих этапах.

![../_images/create-bot.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/create-bot.png)

С помощью команды /setuserpic установите иконку для вашего бота.

![../_images/set-userpick.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/set-userpick.png)

## 4. Соберите образ и присвойте тег

Соберите образ и присвойте ему тег, выполнив следующую команду:

```bash
docker
build
--tag
<
registry_name
>
.cr.cloud.ru/telegram-bot-example https://gitverse.ru/cloudru/evo-containerapp-telegrambot-webhook-python-sample.git
#master --platform linux/amd64
```

Где <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

Для создания контейнера Docker-образ должен быть собран под платформу linux/amd64, поэтому в команде используется флаг platform со значением linux/amd64.

## 5. Загрузите Docker-образ в реестр

1. Загрузите образ в реестр Artifact Registry, выполнив команду:
docker push <registry_name>.cr.cloud.ru/telegram-bot-example

Где:

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
telegram-bot-example — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.
2. В личном кабинете перейдите в раздел с Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

Загрузите образ в реестр Artifact Registry, выполнив команду:

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/telegram-bot-example
```

Где:

- <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
- telegram-bot-example — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

telegram-bot-example — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.

В личном кабинете перейдите в раздел с Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

![../_images/ar-image-done1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-image-done1.png)

## 6. Создайте и запустите контейнер

1. Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.
2. Выберите Container Services и нажмите Создать.
3. Укажите название контейнера и активируйте опцию Публичный адрес.
4. Нажмите Продолжить.
5. Выберите реестр, репозиторий и тег Docker-образа, который вы загрузили в Artifact Registry.
6. Укажите порт контейнера — 5000.
7. Перейдите на вкладку Переменные и добавьте переменную окружения BOT_TOKEN.
В значение переменной укажите токен, полученный при регистрации бота в BotFather.
8. Нажмите Продолжить.
9. Задайте количество ресурсов:

vCPU и RAM: 0.5 vCPU – 1024 MB
Минимальное количество экземпляров: 0
Максимальное количество экземпляров: 1
10. Нажмите Создать.
11. Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.

![../_images/go-ca.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/go-ca.png)

Выберите Container Services и нажмите Создать.

![../_images/start-create.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/start-create.png)

Укажите название контейнера и активируйте опцию Публичный адрес.

Нажмите Продолжить.

![../_images/ca-container-name.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-container-name.png)

Выберите реестр, репозиторий и тег Docker-образа, который вы загрузили в Artifact Registry.

Укажите порт контейнера — 5000.

![../_images/ca-general-settings1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-general-settings1.png)

Перейдите на вкладку Переменные и добавьте переменную окружения BOT_TOKEN.

В значение переменной укажите токен, полученный при регистрации бота в BotFather.

Нажмите Продолжить.

![../_images/ca-variables1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-variables1.png)

Задайте количество ресурсов:

- vCPU и RAM: 0.5 vCPU – 1024 MB
- Минимальное количество экземпляров: 0
- Максимальное количество экземпляров: 1

vCPU и RAM: 0.5 vCPU – 1024 MB

Минимальное количество экземпляров: 0

Максимальное количество экземпляров: 1

Нажмите Создать.

![../_images/ca-config1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-config1.png)

Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

![../_images/ca-run.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-run.png)

## 7. Добавьте вебхук в Telegram

Чтобы бот получал сообщения из Telegram, добавьте вебхук:

1. Откройте любой браузер.
2. В адресной строке введите по очереди запросы.

Проверьте, существуют ли вебхуки:
https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo

{BOT_TOKEN} здесь и далее — токен, который был сгенерирован при регистрации бота в BotFather.

Удалите существующие вебхуки:
https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook

Добавьте новый вебхук:
https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={PUBLIC_URL}/{BOT_TOKEN}

{PUBLIC_URL} — публичный URL-адрес, который был сгенерирован при создании контейнера в Container Apps.

Откройте любой браузер.

В адресной строке введите по очереди запросы.

1. Проверьте, существуют ли вебхуки:
https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo

{BOT_TOKEN} здесь и далее — токен, который был сгенерирован при регистрации бота в BotFather.
2. Удалите существующие вебхуки:
https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook
3. Добавьте новый вебхук:
https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={PUBLIC_URL}/{BOT_TOKEN}

{PUBLIC_URL} — публичный URL-адрес, который был сгенерирован при создании контейнера в Container Apps.

Проверьте, существуют ли вебхуки:

```bash
https://api.telegram.org/bot
{
BOT_TOKEN
}
/getWebhookInfo
```

![../_images/get-webhook.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/get-webhook.png)

{BOT_TOKEN} здесь и далее — токен, который был сгенерирован при регистрации бота в BotFather.

Удалите существующие вебхуки:

```bash
https://api.telegram.org/bot
{
BOT_TOKEN
}
/deleteWebhook
```

![../_images/delete-webhook.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/delete-webhook.png)

Добавьте новый вебхук:

```bash
https://api.telegram.org/bot
{
BOT_TOKEN
}
/setWebhook?url
=
{
PUBLIC_URL
}
/
{
BOT_TOKEN
}
```

![../_images/set-webhook-url.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/set-webhook-url.png)

{PUBLIC_URL} — публичный URL-адрес, который был сгенерирован при создании контейнера в Container Apps.

## 8. Проверьте работу Telegram-бота

Вызовите бота в Telegram по имени пользователя (username) и проверьте его работу, выполнив команду /start.

![../_images/bot-run.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/bot-run.png)

## Результат

Вы научились разворачивать Telegram-бота в контейнере.
