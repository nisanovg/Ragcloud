---
title: Развертывание frontend-приложения в контейнере
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app
topic: containers
---
# Развертывание frontend-приложения в контейнере

С помощью этого руководства вы получите практический опыт использования облачных сервисов для запуска контейнерных приложений — [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps и [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry.

Схема развертывания приложения:

![../_images/dev_experience.svg](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dev_experience.svg)

1. Разработчик загружает (push) Docker-образ приложения в Artifact Registry.
2. Создает контейнер из загруженного образа в Container Apps.
3. Приложение запускается в контейнере и доступно всем пользователям из интернета.

Разработчик загружает (push) Docker-образ приложения в Artifact Registry.

Создает контейнер из загруженного образа в Container Apps.

Приложение запускается в контейнере и доступно всем пользователям из интернета.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Подготовьте среду.
2. [Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Клонируйте или скачайте репозиторий кода c GitVerse.
3. [Соберите и подготовьте Docker-образ](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Соберите и подготовьте Docker-образ.
4. [Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Загрузите Docker-образ в реестр.
5. [Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Создайте и запустите контейнер.
6. [Проверьте работоспособность развернутого приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Проверьте работоспособность развернутого приложения.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Подготовьте среду.

[Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Клонируйте или скачайте репозиторий кода c GitVerse.

[Соберите и подготовьте Docker-образ](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Соберите и подготовьте Docker-образ.

[Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Загрузите Docker-образ в реестр.

[Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Создайте и запустите контейнер.

[Проверьте работоспособность развернутого приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-frontend-app)Проверьте работоспособность развернутого приложения.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.

## 2. (Опционально) Клонируйте или скачайте репозиторий кода c GitVerse

Вы можете зарегистрироваться в [GitVerse](https://gitverse.ru/)GitVerse, если у вас еще нет аккаунта, и познакомиться с новой системой контроля версий. Этот шаг необязательный и не влияет на дальнейшее прохождение сценария.

![../_images/gitverse_clone.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/gitverse_clone.png)

Клонируйте репозиторий:

1. Перейдите в нужную директорию на локальном компьютере.
2. Выполните команду в терминале GitBash:
git clone https://gitverse.ru/cloudru/evo-containerapp-react-sample

Перейдите в нужную директорию на локальном компьютере.

Выполните команду в терминале GitBash:

```bash
git
clone https://gitverse.ru/cloudru/evo-containerapp-react-sample
```

## 3. Соберите и подготовьте Docker-образ

Убедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.

Cоберите на локальном компьютере готовый Docker-образ из репозитория GitVerse, выполнив в терминале следующую команду:

```bash
docker
build
--tag
<
registry_name
>
.cr.cloud.ru/react-hello-world https://gitverse.ru/cloudru/evo-containerapp-react-sample.git
#master --platform linux/amd64
```

Команда собирает образ и тегирует его для дальнейшей загрузки в реестр.
По умолчанию используется тег latest.
Для создания контейнера Docker-образ должен быть собран под платформу linux/amd64, поэтому в команде используется флаг platform со значением linux/amd64.

## 4. Загрузите Docker-образ в реестр Artifact Registry

1. Загрузите образ в реестр Artifact Registry, выполнив команду:
docker push <registry_name>.cr.cloud.ru/react-hello-world

Где:

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
react-hello-world — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.
2. В личном кабинете перейдите в раздел Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

Загрузите образ в реестр Artifact Registry, выполнив команду:

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/react-hello-world
```

Где:

- <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
- react-hello-world — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

react-hello-world — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа.

В личном кабинете перейдите в раздел Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

![../_images/ar-repository-sucess.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-repository-sucess.png)

## 5. Создайте и запустите контейнер

1. Откройте меню загруженного образа и нажмите Создать Container App.
2. Заполните поля и активируйте опции:

Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене *.containers.cloud.ru.
Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этом сценарии используем порт 8080.

server { listen 8080; root /usr/share/nginx/html; index index.html;
 location / { try_files $uri $uri/ /index.html; }}

vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.
Минимальное и максимальное количество экземпляров при масштабировании сервиса. По умолчанию происходит масштабирование с 0, что может вызывать небольшую задержку при старте вашего приложения. Установите минимальное количество экземпляров — 0, а максимальное — 1.
Публичный адрес — активируйте опцию, чтобы получить URL-адрес для вызова приложения из интернета.
3. Нажмите Создать.
Откроется страница сервиса Container Apps.

Откройте меню загруженного образа и нажмите Создать Container App.

![../_images/ar-create-container.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-create-container.png)

Заполните поля и активируйте опции:

![../_images/ar-container-params.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-container-params.png)

- Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене *.containers.cloud.ru.
- Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этом сценарии используем порт 8080.

server { listen 8080; root /usr/share/nginx/html; index index.html;
 location / { try_files $uri $uri/ /index.html; }}
- vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.
- Минимальное и максимальное количество экземпляров при масштабировании сервиса. По умолчанию происходит масштабирование с 0, что может вызывать небольшую задержку при старте вашего приложения. Установите минимальное количество экземпляров — 0, а максимальное — 1.
- Публичный адрес — активируйте опцию, чтобы получить URL-адрес для вызова приложения из интернета.

Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене *.containers.cloud.ru.

Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этом сценарии используем порт 8080.

```bash
server
{
listen
8080
;
root /usr/share/nginx/html
;
index index.html
;
location /
{
try_files
$uri
$uri
/ /index.html
;
}
}
```

vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.

Минимальное и максимальное количество экземпляров при масштабировании сервиса. По умолчанию происходит масштабирование с 0, что может вызывать небольшую задержку при старте вашего приложения. Установите минимальное количество экземпляров — 0, а максимальное — 1.

Публичный адрес — активируйте опцию, чтобы получить URL-адрес для вызова приложения из интернета.

Нажмите Создать.
Откроется страница сервиса Container Apps.

Контейнер будет запущен в течение нескольких секунд.
Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

![../_images/ca-container-run.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-container-run.png)

## 6. Проверьте работоспособность развернутого приложения

Дождитесь появления публичного URL, скопируйте его и вставьте в адресную строку браузера.
Откроется страница приложения.

![../_images/app-go.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/app-go.png)

## Результат

Вы научились:

- загружать Docker-образ в Artifact Registry;
- создавать и запускать контейнер из быстрого меню в Artifact Registry.

загружать Docker-образ в Artifact Registry;

создавать и запускать контейнер из быстрого меню в Artifact Registry.
