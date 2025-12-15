---
title: Развертывание backend-приложения в контейнере
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app
topic: containers
---
# Развертывание backend-приложения в контейнере

С помощью этого руководства вы научитесь разворачивать backend-приложение в контейнере.
Вы будете использовать репозиторий GitVerse с исходным кодом готовых backend-приложений на языках Python, Go, JavaScript, C#.
Каждое приложение является простым примером реализации REST API, которое возвращает список значений с демонстрационными данными.
На примере развертывания backend-приложения вы познакомитесь с дополнительными настройками сервиса [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- Систему контроля версий GitVerse.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

Систему контроля версий GitVerse.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Подготовьте среду.
2. [Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Клонируйте или скачайте репозиторий кода c GitVerse.
3. [Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Соберите образ и присвойте тег.
4. [Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Загрузите Docker-образ в реестр.
5. [Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Создайте и запустите контейнер.
6. [Проверьте работоспособность развернутого приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Проверьте работоспособность развернутого приложения.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Подготовьте среду.

[Клонируйте или скачайте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Клонируйте или скачайте репозиторий кода c GitVerse.

[Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Соберите образ и присвойте тег.

[Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Загрузите Docker-образ в реестр.

[Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Создайте и запустите контейнер.

[Проверьте работоспособность развернутого приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-backend-app)Проверьте работоспособность развернутого приложения.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.

## 2. (Опционально) Клонируйте или скачайте репозиторий кода c GitVerse

Вы можете зарегистрироваться в [GitVerse](https://gitverse.ru/)GitVerse, если у вас еще нет аккаунта, и познакомиться с новой системой контроля версий. Этот шаг необязательный и не влияет на дальнейшее прохождение сценария.

В этом репозитории находится исходный код простого REST API приложения, написанного на разных языках: JavaScript, Python, Go, C#.

```bash
git
clone https://gitverse.ru/cloudru/evo-containerapp-restapi-js-go-python-dotnet-sample
```

## 3. Соберите образ и присвойте тег

Убедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.

Используйте реестр, созданный [на этапе подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)на этапе подготовки среды.
Выполните команду для сборки образа:

```bash
docker
build
--tag
<
registry_name
>
.cr.cloud.ru/restapi-python https://gitverse.ru/cloudru/evo-containerapp-restapi-js-go-python-dotnet-sample.git
#master:restapi-python/src --platform linux/amd64
```

Для создания контейнера Docker-образ должен быть собран под платформу linux/amd64, поэтому в команде используется флаг platform со значением linux/amd64.

## 4. Загрузите Docker-образ в реестр

Загрузите образ в реестр Artifact Registry, выполнив команду:

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/restapi-python
```

Где:

- <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
- restapi-python — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа..

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

restapi-python — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа..

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
Автоматическое развертывание — активируйте опцию, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.
3. Нажмите Создать.

Откройте меню загруженного образа и нажмите Создать Container App.

![../_images/ar-create-container-restapi.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-create-container-restapi.png)

Заполните поля и активируйте опции:

![../_images/ar-create-container-advanced-settings-restapi.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-create-container-advanced-settings-restapi.png)

- Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене *.containers.cloud.ru.
- Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этом сценарии используем порт 8080.

server { listen 8080; root /usr/share/nginx/html; index index.html;
 location / { try_files $uri $uri/ /index.html; }}
- vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.
- Минимальное и максимальное количество экземпляров при масштабировании сервиса. По умолчанию происходит масштабирование с 0, что может вызывать небольшую задержку при старте вашего приложения. Установите минимальное количество экземпляров — 0, а максимальное — 1.
- Публичный адрес — активируйте опцию, чтобы получить URL-адрес для вызова приложения из интернета.
- Автоматическое развертывание — активируйте опцию, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.

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

Автоматическое развертывание — активируйте опцию, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.

Нажмите Создать.

Откроется страница сервиса Container Apps.
Контейнер будет запущен в течение нескольких секунд.

Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

![../_images/ca-container-run-restapi.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-container-run-restapi.png)

## 6. Проверьте работоспособность развернутого приложения

Дождитесь появления публичного URL, скопируйте его и вставьте в адресную строку браузера.

![../_images/ca-public-url-restapi.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-public-url-restapi.png)

## Результат

Вы научились:

- создавать репозитории в существующих реестрах Artifact Registry;
- создавать и запускать контейнер через быстрое меню в Artifact Registry;
- управлять настройками масштабирования контейнера.

создавать репозитории в существующих реестрах Artifact Registry;

создавать и запускать контейнер через быстрое меню в Artifact Registry;

управлять настройками масштабирования контейнера.
