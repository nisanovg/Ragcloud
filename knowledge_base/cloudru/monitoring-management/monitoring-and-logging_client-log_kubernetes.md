---
title: Передача логов с кластера Managed Kubernetes
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__kubernetes
topic: monitoring-management
---
# Передача логов с кластера Managed Kubernetes

С помощью инструкции подготовим и настроим передачу логов с кластера Managed Kubernetes в сервис «Клиентское логирование».

## Перед началом работы

1. [Создайте и настройте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте и настройте лог-группу.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

в блоке Проект — «Пользователь сервисов»;
в блоке Сервисы — «logaas.writer».
3. Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.

[Создайте и настройте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте и настройте лог-группу.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

- в блоке Проект — «Пользователь сервисов»;
- в блоке Сервисы — «logaas.writer».

в блоке Проект — «Пользователь сервисов»;

в блоке Сервисы — «logaas.writer».

Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.

## Шаг 1. Выбор стратегии логирования

В инструкции рассмотрим две стратегии настройки логирования — с DaemonSet и с Sidecar.

Отличия между ними:

Характеристика

Подход с DaemonSet

Подход с Sidecar

Использование ресурсов

1 экземпляр на узел

1 экземпляр на под

Область сбора логов

Логи всех подов на узле

Только логи текущего пода

Конфигурация

Централизованная

Индивидуальная для пода

Оптимальный сценарий

Логирование всего кластера

Изоляция логов отдельных подов

Масштабируемость

Зависит от количества узлов

Зависит от количества подов

Задержка логирования

Минимальная (локальный сбор)

Возможна задержка из-за дополнительных шагов (сбор + передача)

Надежность

Высокая (отказоустойчивость на уровне узла, переживает перезапуски подов)

Зависит от стабильности пода

Сложность настройки

Проще (единая конфигурация)

Сложнее (индивидуальные настройки)

Влияние на сеть

Низкое (логи агрегируются на узле)

Выше (каждый sidecar передает логи)

Гибкость обработки

Ограничена (общие правила)

Высокая (возможность применять уникальные Lua-скрипты или фильтры для каждого пода)

Безопасность

Риск смешения логов

Изоляция логов в рамках пода (меньше риск несанкционированного доступа и утечки)

Таким образом, вам может подойти:

- DaemonSet — для централизованного сбора логов всего кластера.
Это подходит для мониторинга системных компонентов или всех сервисов на узлах.
- Sidecar — для изоляции логов отдельных подов.
Например, если вам нужна отдельная обработка логов для критичных микросервисов или мультитенантных сред.

DaemonSet — для централизованного сбора логов всего кластера.
Это подходит для мониторинга системных компонентов или всех сервисов на узлах.

Sidecar — для изоляции логов отдельных подов.
Например, если вам нужна отдельная обработка логов для критичных микросервисов или мультитенантных сред.

## Шаг 2. Определение структуры проекта

В процессе настройки передачи логов с кластера Managed Kubernetes вы создадите на вашем локальном компьютере или виртуальной машине следующие файлы:

```bash
├── app/
# Ваше Python-приложение
│ ├── generator.py
# Основной код приложения
│ └── Dockerfile
# Dockerfile для сборки приложения
├── fluent-bit-logaas/
# Кастомный образ Fluent Bit с плагином logaas
│ └── Dockerfile
# Dockerfile для сборки fluent-bit-logaas
│
├── k8s/
# Файлы конфигурации Kubernetes
│ ├── deployment.yaml
# Основной Deployment приложения (без логирования)
│ ├── service.yaml
# Конфигурация сервиса
│ └── logging/
# Конфигурации для логирования
│ ├── fluent-bit/
│ │ ├── daemonset.yaml
# DaemonSet для Fluent Bit
│ │ ├── configmap.yaml
# ConfigMap для Fluent Bit
│ │ ├── fluent-bit.conf
# Основной конфиг Fluent Bit
│ │ └── parsers.conf
# Дополнительные парсеры (опционально)
│ │
│ └── sidecar/
# Альтернативный подход с sidecar
│ └── deployment-with-sidecar.yaml
# Deployment app с sidecar-контейнером
```

## Шаг 3. Подготовка окружения

Исходные данные для развертывания можно подготовить в любой из сред: Windows, macOS, Linux на локальном устройстве, Linux на виртуальной машине.
ПО для управления развертыванием также доступно для всех сред.

### Установка Docker

- Windows/macOS: [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop (включает Docker Engine);
- Linux: [Docker Engine](https://docs.docker.com/engine/install)Docker Engine.

Windows/macOS: [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop (включает Docker Engine);

Linux: [Docker Engine](https://docs.docker.com/engine/install)Docker Engine.

### Создание Artifact Registry

1. [Создайте реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/quickstart)Создайте реестр в Artifact Registry.
В примере в инструкции мы назовем его your-registry.
2. Создайте репозитории:

simple-logging-app — для приложения-генератора логов;
fluent-bit-logaas — для кастомизированного Fluent Bit.

[Создайте реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/quickstart)Создайте реестр в Artifact Registry.
В примере в инструкции мы назовем его your-registry.

Создайте репозитории:

- simple-logging-app — для приложения-генератора логов;
- fluent-bit-logaas — для кастомизированного Fluent Bit.

simple-logging-app — для приложения-генератора логов;

fluent-bit-logaas — для кастомизированного Fluent Bit.

Пример URL реестра: your-registry.cr.cloud.ru. Замените его на URL вашего реестра.

### Настройка кластера Managed Kubernetes

1. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.
2. [Добавьте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Добавьте группу узлов.
3. [Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру.

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.

[Добавьте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Добавьте группу узлов.

[Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру.

## Шаг 4. Создание базового приложения для генерации логов

Модуль генератора логов app/generator.py:

```bash
import
random
import
json
import
socket
import
os
from datetime
import
datetime, timezone
import
time
LOG_LEVELS
=
[
'DEBUG'
,
'INFO'
,
'WARN'
,
'ERROR'
,
'FATAL'
]
MESSAGE_TEMPLATES
=
[
"Data received [ID: {id}]"
,
"Processing request from user {user}"
,
"Failed to connect to database {db}"
,
"Connection timeout after {sec} seconds"
,
"File {file} not found"
,
"Authentication failed for {service}"
,
"Received {size} bytes from {ip}"
,
"Task {task} completed in {ms}ms"
,
"Cache miss for key {key}"
,
"Starting backup process {job_id}"
]
def generate_message
(
)
:
template
=
random.choice
(
MESSAGE_TEMPLATES
)
replacements
=
{
'id'
:
lambda: random.randint
(
1000
,
9999
)
,
'user'
:
lambda: f
"user_{random.randint(100, 999)}"
,
'db'
:
lambda: random.choice
(
[
"primary"
,
"replica"
,
"archive"
]
)
,
'sec'
:
lambda: random.randint
(
1
,
30
)
,
'file'
:
lambda: f
"/var/log/{random.choice(['app', 'system', 'auth'])}.log"
,
'service'
:
lambda: random.choice
(
[
"API"
,
"SSH"
,
"Database"
]
)
,
'size'
:
lambda: random.randint
(
512
,
4096
)
,
'ip'
:
lambda:
"."
.join
(
map
(
str,
[
random.randint
(
1
,
255
)
for
_
in
range
(
4
)
]
))
,
'task'
:
lambda: random.choice
(
[
"cleanup"
,
"backup"
,
"sync"
]
)
,
'ms'
:
lambda: random.randint
(
100
,
5000
)
,
'key'
:
lambda: hex
(
random.getrandbits
(
128
))
[
2
:10
]
,
'job_id'
:
lambda: f
"JOB-{random.randint(10000, 99999)}"
}
return
template.format
(
**
{
k: v
(
)
for
k,
v
in
replacements.items
(
)
if
k
in
template
}
)
def generate_log
(
)
:
return
{
"timestamp"
:
datetime.now
(
timezone.utc
)
.isoformat
(
timespec
=
'milliseconds'
)
.replace
(
'+00:00'
,
'Z'
)
,
"level"
:
random.choice
(
LOG_LEVELS
)
,
"labels"
:
{
"app"
:
"logger"
,
"host"
:
socket.gethostname
(
)
,
"pid"
:
os.getpid
(
)
,
"random"
:
random.randint
(
1
,
1000
)
}
,
"message"
:
generate_message
(
)
}
if
__name__
==
"__main__"
:
while
True: log_entry
=
generate_log
(
)
print
(
json.dumps
(
log_entry
))
time.sleep
(
random.uniform
(
0.1
,
2.0
))
```

Docker-образ приложения app/Dockerfile:

```bash
FROM python:3.13-alpine
WORKDIR /app
COPY log_generator.py
.
CMD
[
"python"
,
"./log_generator.py"
]
```

## Шаг 5. Сборка кастомизированного образа Fluent Bit

Docker-образ с плагином logaas — fluent-bit-logaas/Dockerfile:

```bash
ARG
fluebtbit_ver
=
3.2
.0
FROM debian:bullseye-slim as builder
RUN
apt-get
update
&&
apt-get
install
-y
--no-install-recommends
\
wget
\
ca-certificates
\
&&
rm
-rf
/var/lib/apt/lists/*
WORKDIR /build
RUN
wget
https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaas.so
-O
./logaas.so
FROM fluent/fluent-bit:
${fluebtbit_ver}
as fluentbit
COPY
--from
=
builder /build/logaas.so /fluent-bit/bin/
ENTRYPOINT
[
"/fluent-bit/bin/fluent-bit"
,
"-e"
,
"/fluent-bit/bin/logaas.so"
]
CMD
[
"-c"
,
"/fluent-bit/etc/fluent-bit.conf"
]
```

## Шаг 6. Публикация образов в Artifact Registry

Сборка и публикация образа приложения:

```bash
docker
build
-t
your-registry.cr.cloud.ru/simple-logging-app:latest
-f
app/Dockerfile app/
docker
push your-registry.cr.cloud.ru/simple-logging-app:latest
```

Сборка и публикация кастомного образа Fluent Bit:

```bash
docker
build
-t
your-registry.cr.cloud.ru/fluent-bit-logaas:latest
-f
fluent-bit-logaas/Dockerfile fluent-bit-logaas/
docker
push your-registry.cr.cloud.ru/fluent-bit-logaas:latest
```

Не забудьте заменить URL реестра с your-registry.cr.cloud.ru на URL вашего реестра.

## Шаг 7. Подготовка развертывания базового приложения в Managed Kubernetes

Создайте базовые файлы:

- k8s/deployment.yaml:

apiVersion: apps/v1kind: Deploymentmetadata: name: python-appspec: replicas: 2 selector: matchLabels: app: python-app template: metadata: labels: app: python-app spec: containers: - name: main-app image: your-registry.cr.cloud.ru/simple-logging-app:latest ports: - containerPort: 5000
- k8s/service.yaml:

apiVersion: v1kind: Servicemetadata: name: python-app-servicespec: selector: app: python-app ports: - protocol: TCP port: 80 targetPort: 5000 type: LoadBalancer

k8s/deployment.yaml:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
name: python-app
spec:
replicas:
2
selector:
matchLabels:
app: python-app
template:
metadata:
labels:
app: python-app
spec:
containers:
- name: main-app
image: your-registry.cr.cloud.ru/simple-logging-app:latest
ports:
- containerPort:
5000
```

k8s/service.yaml:

```bash
apiVersion: v1
kind: Service
metadata:
name: python-app-service
spec:
selector:
app: python-app
ports:
- protocol: TCP
port:
80
targetPort:
5000
type: LoadBalancer
```

## Шаг 8. Настройка развертывания логирования через Fluent Bit

Выберите, какая стратегия настройки логирования подходит вам больше.
Мы рекомендуем подход с DaemonSet.

В этом варианте запускается один экземпляр Fluent Bit на каждом узле.

Для этого подхода требуется доступ к логам узла: /var/log.

Заполните содержимое файлов:

- k8s/logging/fluent-bit/configmap.yaml:
apiVersion: v1kind: ConfigMapmetadata: name: fluent-bit-config labels: k8s-app: fluent-bitdata: fluent-bit.conf: | [SERVICE] Flush 5 Log_Level info Daemon off Parsers_File /fluent-bit/etc/parsers.conf
 [INPUT] Name tail Path /var/log/containers/*.log Parser docker Tag kube.* Refresh_Interval 5
 [FILTER] Name kubernetes Match kube.* Kube_URL https://kubernetes.default.svc:443 Kube_CA_File /var/run/secrets/kubernetes.io/serviceaccount/ca.crt Kube_Token_File /var/run/secrets/kubernetes.io/serviceaccount/token Kube_Tag_Prefix kube.var.log.containers. Merge_Log On
 [OUTPUT] Name logaas Match * address https://console.cloud.ru/ iam_address https://auth.iam.sbercloud.ru/ iam_client_id REPLACE_TO_LOGGING_SA_KEY_ID iam_client_secret REPLACE_TO_LOGGING_SA_SECRET default_project_id REPLACE_TO_PROJECT_ID default_group_id REPLACE_TO_LOG_GROUP_ID default_labels {"some_label":"default_value"}

Добавьте в файл свои данные:

REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».
REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.
- k8s/logging/fluent-bit/daemonset.yaml:
apiVersion: apps/v1kind: DaemonSetmetadata: name: fluent-bit labels: k8s-app: fluent-bitspec: selector: matchLabels: k8s-app: fluent-bit template: metadata: labels: k8s-app: fluent-bit spec: containers: - name: fluent-bit image: your-registry.cr.cloud.ru/fluent-bit-logaas:latest volumeMounts: - name: varlog mountPath: /var/log - name: config mountPath: /fluent-bit/etc/ volumes: - name: varlog hostPath: path: /var/log - name: config configMap: name: fluent-bit-config

k8s/logging/fluent-bit/configmap.yaml:

```bash
apiVersion: v1
kind: ConfigMap
metadata:
name: fluent-bit-config
labels:
k8s-app: fluent-bit
data:
fluent-bit.conf:
|
[
SERVICE
]
Flush
5
Log_Level info
Daemon off
Parsers_File /fluent-bit/etc/parsers.conf
[
INPUT
]
Name
tail
Path /var/log/containers/*.log
Parser
docker
Tag kube.*
Refresh_Interval
5
[
FILTER
]
Name kubernetes
Match kube.*
Kube_URL https://kubernetes.default.svc:443
Kube_CA_File /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
Kube_Token_File /var/run/secrets/kubernetes.io/serviceaccount/token
Kube_Tag_Prefix kube.var.log.containers.
Merge_Log On
[
OUTPUT
]
Name logaas
Match *
address https://console.cloud.ru/
iam_address https://auth.iam.sbercloud.ru/
iam_client_id REPLACE_TO_LOGGING_SA_KEY_ID
iam_client_secret REPLACE_TO_LOGGING_SA_SECRET
default_project_id REPLACE_TO_PROJECT_ID
default_group_id REPLACE_TO_LOG_GROUP_ID
default_labels
{
"some_label"
:
"default_value"
}
```

Добавьте в файл свои данные:

- REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».
- REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
- default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».

REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.

default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

k8s/logging/fluent-bit/daemonset.yaml:

```bash
apiVersion: apps/v1
kind: DaemonSet
metadata:
name: fluent-bit
labels:
k8s-app: fluent-bit
spec:
selector:
matchLabels:
k8s-app: fluent-bit
template:
metadata:
labels:
k8s-app: fluent-bit
spec:
containers:
- name: fluent-bit
image: your-registry.cr.cloud.ru/fluent-bit-logaas:latest
volumeMounts:
- name: varlog
mountPath: /var/log
- name: config
mountPath: /fluent-bit/etc/
volumes:
- name: varlog
hostPath:
path: /var/log
- name: config
configMap:
name: fluent-bit-config
```

## Шаг 9. Развертывание приложения и логирования в Managed Kubernetes

Для PROD-стенда добавьте права RBAC для Fluent Bit.

1. Разверните основное приложение:
kubectl apply -f k8s/deployment.yamlkubectl apply -f k8s/service.yaml
2. Разверните логирование Fluent Bit:
Подход с DaemonSetПодход с Sidecarkubectl apply -f k8s/logging/fluent-bit/configmap.yamlkubectl apply -f k8s/logging/fluent-bit/daemonset.yaml

Разверните основное приложение:

```bash
kubectl apply
-f
k8s/deployment.yaml
kubectl apply
-f
k8s/service.yaml
```

Разверните логирование Fluent Bit:

```bash
kubectl apply
-f
k8s/logging/fluent-bit/configmap.yaml
kubectl apply
-f
k8s/logging/fluent-bit/daemonset.yaml
```

## Шаг 10. Просмотр логов

Логи появятся в сервисе «Клиентское логирование» вскоре после успешного развертывания приложения и логирования.

Вы можете [посмотреть логи в лог-группах](https://cloud.ru/docs/client-log/ug/topics/working-groups)посмотреть логи в лог-группах.
Логи можно [отфильтровать с помощью языка фильтрующих выражений](https://cloud.ru/docs/client-log/ug/topics/concepts__filter)отфильтровать с помощью языка фильтрующих выражений и выгрузить как файл.

## После окончания работы

Если кластер Managed Kubernetes, реестр в Artifact Registry и его логи стали неактуальными, вы можете удалить их:

- [Удалить кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)Удалить кластер Managed Kubernetes
- [Удалить реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-delete)Удалить реестр в Artifact Registry
- [Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу
- [Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект

[Удалить кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)Удалить кластер Managed Kubernetes

[Удалить реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-delete)Удалить реестр в Artifact Registry

[Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу

[Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект
