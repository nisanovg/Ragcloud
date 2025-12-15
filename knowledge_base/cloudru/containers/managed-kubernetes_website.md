---
title: Пример развертывания сайта
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__website
topic: containers
---
# Пример развертывания сайта

С помощью инструкции создадим образ с простым статическим сайтом.
Затем загрузим образ в Artifact Registry и развернем сайт в кластере Managed Kubernetes.

## Перед началом работы

1. Установите [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl и [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт с ролью «Администратор проекта».
3. [Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.
Рекомендуем сохранить ключи доступа в системе управления паролями, например [Secret Management](https://cloud.ru/docs/scsm/ug/index)Secret Management.
Они пригодятся для подключения к кластеру и аутентификации в Artifact Registry.
4. [Создайте кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер с публичным IP и [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.
5. [Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру.

Установите [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl и [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт с ролью «Администратор проекта».

[Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.

Рекомендуем сохранить ключи доступа в системе управления паролями, например [Secret Management](https://cloud.ru/docs/scsm/ug/index)Secret Management.
Они пригодятся для подключения к кластеру и аутентификации в Artifact Registry.

[Создайте кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер с публичным IP и [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.

[Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру.

## Подготовьте файлы сайта

Сайт в примере содержит два файла — index.html и pic.png.

## Подготовьте спецификации

Перед началом сборки образа создайте спецификации для nginx и Dockerfile:

1. Создайте каталог cloudru-app-example.
2. Переместите в созданный каталог файлы index.html и pic.png.
3. В каталоге cloudru-app-example создайте конфигурационный файл с названием nginx.conf.
4. Добавьте в nginx.conf спецификацию:
server { listen 8080 default_server; listen [::]:8080 default_server; root /usr/share/nginx/html; index index.html; location / { try_files $uri $uri/ =404; }}
5. В каталоге cloudru-app-example создайте файл с названием Dockerfile и добавьте спецификацию:
# nginx imageFROM nginx:stable# Port for start serviceEXPOSE 8080# nginx config (nginx.conf)COPY nginx.conf /etc/nginx/conf.d/nginx.conf# Site artifactsCOPY index.html /usr/share/nginx/html/index.htmlCOPY pic.png /usr/share/nginx/html/pic.pngSTOPSIGNAL SIGQUITCMD ["nginx", "-g", "daemon off;"]

Создайте каталог cloudru-app-example.

Переместите в созданный каталог файлы index.html и pic.png.

В каталоге cloudru-app-example создайте конфигурационный файл с названием nginx.conf.

Добавьте в nginx.conf спецификацию:

```bash
server
{
listen
8080
default_server
;
listen
[
::
]
:8080 default_server
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
/
=
404
;
}
}
```

В каталоге cloudru-app-example создайте файл с названием Dockerfile и добавьте спецификацию:

```bash
# nginx image
FROM nginx:stable
# Port for start service
EXPOSE
8080
# nginx config (nginx.conf)
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
# Site artifacts
COPY index.html /usr/share/nginx/html/index.html
COPY pic.png /usr/share/nginx/html/pic.png
STOPSIGNAL SIGQUIT
CMD
[
"nginx"
,
"-g"
,
"daemon off;"
]
```

## Соберите Docker-образ

1. Перейдите в каталог cloudru-app-example и запустите сборку образа с помощью команды:
docker build -t cloudru-app-example .
2. В Docker Desktop перейдите на вкладку Images → Local и проверьте, что образ cloudru-app-example появился в списке.

Перейдите в каталог cloudru-app-example и запустите сборку образа с помощью команды:

```bash
docker
build
-t
cloudru-app-example
.
```

В Docker Desktop перейдите на вкладку Images → Local и проверьте, что образ cloudru-app-example появился в списке.

## Загрузите образ в Artifact Registry

1. В Artifact Registry [создайте реестр](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)создайте реестр.
2. [Пройдите аутентификацию в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию в Artifact Registry для работы с Docker-образами.
Используйте сервисный аккаунт, полученный перед началом работы.
3. Выполните команду:
docker tag cloudru-app-example <uri_registry>/cloudru-app-example:v1

Где:

cloudru-app-example — образ с сайтом.
<uri_registry> — URI реестра Artifact Registry.
Чтобы посмотреть или скопировать URI реестра, в личном кабинете перейдите в Artifact Registry → Реестры.
URI реестра доступен в списке напротив нужного реестра.
4. Загрузите образ:
docker push <uri_registry>/cloudru-app-example:v1
5. Проверьте, что образ отобразился в списке репозитория.

В Artifact Registry [создайте реестр](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)создайте реестр.

[Пройдите аутентификацию в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию в Artifact Registry для работы с Docker-образами.
Используйте сервисный аккаунт, полученный перед началом работы.

Выполните команду:

```bash
docker
tag cloudru-app-example
<
uri_registry
>
/cloudru-app-example:v1
```

Где:

- cloudru-app-example — образ с сайтом.
- <uri_registry> — URI реестра Artifact Registry.
Чтобы посмотреть или скопировать URI реестра, в личном кабинете перейдите в Artifact Registry → Реестры.
URI реестра доступен в списке напротив нужного реестра.

cloudru-app-example — образ с сайтом.

<uri_registry> — URI реестра Artifact Registry.
Чтобы посмотреть или скопировать URI реестра, в личном кабинете перейдите в Artifact Registry → Реестры.
URI реестра доступен в списке напротив нужного реестра.

Загрузите образ:

```bash
docker
push
<
uri_registry
>
/cloudru-app-example:v1
```

Проверьте, что образ отобразился в списке репозитория.

[Загрузка Docker-образа в репозиторий Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__artifact-push)Загрузка Docker-образа в репозиторий Artifact Registry

## Подготовьте манифесты для приложения

1. Создайте файл cloudru-app-example.yaml и сохраните следующий манифест:
apiVersion: apps/v1kind: Deploymentmetadata: name: cloudru-app-examplespec: selector: matchLabels: run: cloudru-app-example replicas: 1 template: metadata: labels: run: cloudru-app-example spec: containers: - name: cloudru-app-example image: <uri_registry>/cloudru-app-example:v1 ports: - containerPort: 8080

Где:

spec.template.spec.containers.image — путь до образа в Artifact Registry.
spec.replicas — количество реплик приложения.

Создайте файл cloudru-app-example.yaml и сохраните следующий манифест:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
name: cloudru-app-example
spec:
selector:
matchLabels:
run: cloudru-app-example
replicas:
1
template:
metadata:
labels:
run: cloudru-app-example
spec:
containers:
- name: cloudru-app-example
image:
<
uri_registry
>
/cloudru-app-example:v1
ports:
- containerPort:
8080
```

Где:

- spec.template.spec.containers.image — путь до образа в Artifact Registry.
- spec.replicas — количество реплик приложения.

spec.template.spec.containers.image — путь до образа в Artifact Registry.

spec.replicas — количество реплик приложения.

В Managed Kubernetes автоматически создается секрет для Artifact Registry.
При создании ресурса этот секрет будет добавлен Admission-контроллером в поле imagePullSecret, если в манифесте поле не указано явно.

Чтобы использовать свой секрет, добавьте в манифест imagePullSecret:

```bash
imagePullSecrets
:
-
name
:
<your
-
secret
-
name
>
```

1. В корневом каталоге создайте cloudru-app-example-lb.yaml и добавьте следующую спецификацию:
apiVersion: v1kind: Servicemetadata: name: cloudru-app-example-lb labels: run: cloudru-app-examplespec: selector: run: cloudru-app-example ports: - port: 8080 targetPort: 8080 type: LoadBalancer

В корневом каталоге создайте cloudru-app-example-lb.yaml и добавьте следующую спецификацию:

```bash
apiVersion: v1
kind: Service
metadata:
name: cloudru-app-example-lb
labels:
run: cloudru-app-example
spec:
selector:
run: cloudru-app-example
ports:
- port:
8080
targetPort:
8080
type: LoadBalancer
```

## Разверните приложение

Чтобы развернуть приложение, выполните команды:

```bash
kubectl apply
-f
cloudru-app-example.yaml
kubectl apply
-f
cloudru-app-example-lb.yaml
```

Результат будет следующим:

```bash
deployment.apps/cloudru-app-example created
service/cloudru-app-example-lb created
```

Развертывание приложения займет 2–3 минуты.

Проверьте статус выполнения развертывания подов:

```bash
kubectl get pod
```

Если под с приложением находится в статусе «Running», развертывание прошло успешно.

Чтобы получить адрес для доступа к сайту, выполните команду:

```bash
kubectl get svc
```

В ответе будут доступны EXTERNAL-IP и PORT(S) для сервиса cloudru-app-example-lb.

Доступ к сайту можно получить по URL формата http://EXTERNAL-IP:PORT.
