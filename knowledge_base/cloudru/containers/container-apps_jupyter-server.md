---
title: Развертывание Jupyter Server в контейнере
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server
topic: containers
---
# Развертывание Jupyter Server в контейнере

С помощью этого руководства вы научитесь разворачивать Jupyter Server в контейнере.
На примере развертывания Jupyter Server вы познакомитесь с созданием контейнера через интерфейс сервиса [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps и дополнительными настройками контейнера.
[Смотрите обучающее видео](https://www.youtube.com/watch)Смотрите обучающее видео о Jupyter Server.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- Систему контроля версий GitVerse.
В GitVerse находится готовый образ Jupyter Server.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

Систему контроля версий GitVerse.
В GitVerse находится готовый образ Jupyter Server.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Подготовьте среду.
2. [Клонируйте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Клонируйте репозиторий кода c GitVerse.
3. [Соберите образ, присвойте тег и загрузите образ](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Соберите образ, присвойте тег и загрузите образ.
4. [Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Создайте и запустите контейнер.
5. [Проверьте работу Jupyter Server](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Проверьте работу Jupyter Server.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Подготовьте среду.

[Клонируйте репозиторий кода c GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Клонируйте репозиторий кода c GitVerse.

[Соберите образ, присвойте тег и загрузите образ](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Соберите образ, присвойте тег и загрузите образ.

[Создайте и запустите контейнер](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Создайте и запустите контейнер.

[Проверьте работу Jupyter Server](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__jupyter-server)Проверьте работу Jupyter Server.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду, если не сделали этого ранее.

## 2. Клонируйте репозиторий кода c GitVerse

Чтобы использовать образ Jupyter Server, склонируйте репозиторий:

```bash
git
clone https://gitverse.ru/cloudru/evo-containerapp-jupyter-server-sample
```

## 3. Соберите образ, присвойте тег и загрузите образ

1. Перейдите в локальную папку с репозиторием:
cd evo-containerapp-jupyter-server-sample
2. Соберите образ:
ВниманиеУбедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.
docker build --platform linux/amd64 -t jupyter-server -f dist/jupyter-server/Dockerfile

Перейдите в локальную папку с репозиторием:

```bash
cd
evo-containerapp-jupyter-server-sample
```

Соберите образ:

Убедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.

```bash
docker
build
--platform
linux/amd64
-t
jupyter-server
-f
dist/jupyter-server/Dockerfile
```

Для создания контейнера Docker-образ должен быть собран под платформу linux/amd64, поэтому в команде используется флаг platform со значением linux/amd64.

1. Присвойте образу тег:
docker tag jupyter-server <registry_name>.cr.cloud.ru/jupyter-server
2. Загрузите образ в реестр.
Используйте реестр, созданный [на этапе подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)на этапе подготовки среды.
docker push <registry_name>.cr.cloud.ru/jupyter-server

Где:

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
jupyter-server — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа..
3. В личном кабинете перейдите в раздел Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

Присвойте образу тег:

```bash
docker
tag jupyter-server
<
registry_name
>
.cr.cloud.ru/jupyter-server
```

Загрузите образ в реестр.

Используйте реестр, созданный [на этапе подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)на этапе подготовки среды.

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/jupyter-server
```

Где:

- <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
- jupyter-server — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа..

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

jupyter-server — название будущего репозитория в Artifact Registry. Название репозитория соответствует имени Docker-образа..

В личном кабинете перейдите в раздел Реестры → Репозитории → Артефакты сервиса Artifact Registry и убедитесь, что образ загружен.

![../_images/ar-image-done.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-image-done.png)

## 4. Создайте и запустите контейнер

1. Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.
2. Выберите Container Services и нажмите Создать.
3. Укажите название контейнера и активируйте опцию Публичный адрес.
4. Нажмите Продолжить.
5. Выберите реестр, репозиторий и тег Docker-образа, который вы загрузили в Artifact Registry.
6. Укажите порт контейнера — 8888.
7. (Опционально) На вкладке Переменные для ключа GIT_CLONE_REPO в качестве значения укажите адрес вашего репозитория, если хотите после запуска Jupyter Server сразу работать с исходным кодом.
8. Нажмите Продолжить.
9. Задайте количество ресурсов:

vCPU и RAM: 0.1 vCPU – 256 MB
Минимальное количество экземпляров: 1
Максимальное количество экземпляров: 1
10. Нажмите Создать.
11. Дождитесь, когда контейнер и ревизия перейдут в статус Выполняется.

Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.

![../_images/go-ca1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/go-ca1.png)

Выберите Container Services и нажмите Создать.

![../_images/start-create.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/start-create.png)

Укажите название контейнера и активируйте опцию Публичный адрес.

Нажмите Продолжить.

![../_images/ca-general-settings.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-general-settings.png)

Выберите реестр, репозиторий и тег Docker-образа, который вы загрузили в Artifact Registry.

Укажите порт контейнера — 8888.

![../_images/ca-image-settings.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-image-settings.png)

(Опционально) На вкладке Переменные для ключа GIT_CLONE_REPO в качестве значения укажите адрес вашего репозитория, если хотите после запуска Jupyter Server сразу работать с исходным кодом.

![../_images/ca-variables.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-variables.png)

Нажмите Продолжить.

Задайте количество ресурсов:

- vCPU и RAM: 0.1 vCPU – 256 MB
- Минимальное количество экземпляров: 1
- Максимальное количество экземпляров: 1

vCPU и RAM: 0.1 vCPU – 256 MB

Минимальное количество экземпляров: 1

Максимальное количество экземпляров: 1

Нажмите Создать.

![../_images/ca-config.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-config.png)

Дождитесь, когда контейнер и ревизия перейдут в статус Выполняется.

![../_images/ca-container-run1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-container-run1.png)

## 5. Проверьте работу Jupyter Server

Дождитесь появления публичного URL, скопируйте его и вставьте в адресную строку браузера.
Откроется интерфейс Jupyter Server.

![../_images/ca-jupyter.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ca-jupyter.png)

Вы развернули Jupyter Server облачном контейнере.

## Результат

Вы научились:

- создавать контейнер из интерфейса сервиса Container Apps;
- настраивать переменные контейнера.

создавать контейнер из интерфейса сервиса Container Apps;

настраивать переменные контейнера.
