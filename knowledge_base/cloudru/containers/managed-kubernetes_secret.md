---
title: Работа с секретами при публикации приложений в Managed Kubernetes
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret
topic: containers
---
# Работа с секретами при публикации приложений в Managed Kubernetes

Приложения, развернутые в кластерах Kubernetes, часто требуют подключения к базам данных или внешним сервисам.
Однако чувствительные данные, например логины, пароли или ключи API, не следует хранить в открытом виде в манифестах.
Защищенное хранение таких данных — одна из ключевых задач обеспечения безопасности приложений.

С помощью этого руководства вы научитесь подключать Flask-приложение к PostgreSQL с использованием встроенных в Kubernetes секретов для хранения логина и пароля от базы данных PostgreSQL в сервисе Managed Kubernetes на платформе [Cloud.ru](https://cloud.ru/)Cloud.ru Evolution.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.
- [kubectl](https://kubernetes.io/docs/reference/kubectl)kubectl — инструмент командной строки, позволяющий запускать команды для кластеров Kubernetes.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.

[kubectl](https://kubernetes.io/docs/reference/kubectl)kubectl — инструмент командной строки, позволяющий запускать команды для кластеров Kubernetes.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Разверните необходимые ресурсы в облаке.
2. [Создайте секрет и базу данных PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Создайте секрет и базу данных PostgreSQL.
3. [Соберите и загрузите образ приложения в Artifact Registry Cloud.ru](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Соберите и загрузите образ приложения в Artifact Registry Cloud.ru.
4. [Разверните Flask-приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Разверните Flask-приложение в Managed Kubernetes.
5. [Проверьте результат](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Проверьте результат.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Разверните необходимые ресурсы в облаке.

[Создайте секрет и базу данных PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Создайте секрет и базу данных PostgreSQL.

[Соберите и загрузите образ приложения в Artifact Registry Cloud.ru](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Соберите и загрузите образ приложения в Artifact Registry Cloud.ru.

[Разверните Flask-приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Разверните Flask-приложение в Managed Kubernetes.

[Проверьте результат](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)Проверьте результат.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.

## 1. Разверните необходимые ресурсы в облаке

1. [Создайте кластер Managed Kubernetes с хотя бы одной группой узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes с хотя бы одной группой узлов.
2. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину в той же зоне доступности, что и кластер.
В сетевых настройках ВМ выберите параметр Подсеть с публичным IP.
С виртуальной машины вы будете подключаться к кластеру Managed Kubernetes.
3. Выполните подключение к кластеру Managed Kubernetes с ВМ:

[Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.
На ВМ установите [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl и [cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin.
[Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.
Проверьте подключение:
kubectl get nodes

Если отобразится список узлов, подключение настроено.
4. [Создайте sNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте sNAT-шлюз в той же зоне доступности, что и кластер.
Он понадобится для работы с внешними образами, например postgres.

[Создайте кластер Managed Kubernetes с хотя бы одной группой узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes с хотя бы одной группой узлов.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину в той же зоне доступности, что и кластер.

В сетевых настройках ВМ выберите параметр Подсеть с публичным IP.

С виртуальной машины вы будете подключаться к кластеру Managed Kubernetes.

Выполните подключение к кластеру Managed Kubernetes с ВМ:

1. [Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.
2. На ВМ установите [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl и [cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin.
3. [Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.
4. Проверьте подключение:
kubectl get nodes

Если отобразится список узлов, подключение настроено.

[Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.

На ВМ установите [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl и [cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin.

[Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.

Проверьте подключение:

```bash
kubectl get nodes
```

Если отобразится список узлов, подключение настроено.

[Создайте sNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте sNAT-шлюз в той же зоне доступности, что и кластер.

Он понадобится для работы с внешними образами, например postgres.

## 2. Создайте секрет и базу данных PostgreSQL

Этот шаг выполняется на виртуальной машине, с которой выполнено подключение к созданному кластеру Managed Kubernetes.

1. Создайте секрет, содержащий логин и пароль для PostgreSQL:
kubectl create secret generic pg-secret \ --from-literal=POSTGRES_USER=demo \ --from-literal=POSTGRES_PASSWORD=supersecret

Этот секрет будет использоваться как самой базой данных, так и приложением-клиентом для подключения.
Результат:
secret/pg-secret created
2. Создайте файл postgres-deployment.yaml:
apiVersion: apps/v1kind: Deploymentmetadata: name: postgresspec: replicas: 1 selector: matchLabels: app: postgres template: metadata: labels: app: postgres spec: containers: - name: postgres image: postgres:15 env: - name: POSTGRES_USER valueFrom: secretKeyRef: name: pg-secret key: POSTGRES_USER - name: POSTGRES_PASSWORD valueFrom: secretKeyRef: name: pg-secret key: POSTGRES_PASSWORD ports: - containerPort: 5432---apiVersion: v1kind: Servicemetadata: name: postgresspec: selector: app: postgres ports: - port: 5432 targetPort: 5432 clusterIP: ""
3. Примените манифест:
kubectl apply -f postgres-deployment.yaml

Результат:
deployment.apps/postgres createdservice/postgres created

Создайте секрет, содержащий логин и пароль для PostgreSQL:

```bash
kubectl create secret generic pg-secret
\
--from-literal
=
POSTGRES_USER
=
demo
\
--from-literal
=
POSTGRES_PASSWORD
=
supersecret
```

Этот секрет будет использоваться как самой базой данных, так и приложением-клиентом для подключения.

Результат:

```bash
secret/pg-secret created
```

Создайте файл postgres-deployment.yaml:

```bash
apiVersion
:
apps/v1
kind
:
Deployment
metadata
:
name
:
postgres
spec
:
replicas
:
1
selector
:
matchLabels
:
app
:
postgres
template
:
metadata
:
labels
:
app
:
postgres
spec
:
containers
:
-
name
:
postgres
image
:
postgres
:
15
env
:
-
name
:
POSTGRES_USER
valueFrom
:
secretKeyRef
:
name
:
pg
-
secret
key
:
POSTGRES_USER
-
name
:
POSTGRES_PASSWORD
valueFrom
:
secretKeyRef
:
name
:
pg
-
secret
key
:
POSTGRES_PASSWORD
ports
:
-
containerPort
:
5432
---
apiVersion
:
v1
kind
:
Service
metadata
:
name
:
postgres
spec
:
selector
:
app
:
postgres
ports
:
-
port
:
5432
targetPort
:
5432
clusterIP
:
""
```

Примените манифест:

```bash
kubectl apply
-f
postgres-deployment.yaml
```

Результат:

```bash
deployment.apps/postgres created
service/postgres created
```

## 3. Соберите и загрузите образ приложения в Artifact Registry Cloud.ru

На этом шаге вы создадите Docker-образ Flask-приложения, которое подключается к PostgreSQL, и загрузите его в Artifact Registry [Cloud.ru](https://cloud.ru/)Cloud.ru.
Использование собственного образа в Artifact Registry гарантирует, что приложение будет работать с нужными зависимостями и будет доступно для вашего кластера без внешних зависимостей.

Если вы хотите пропустить сборку, можете перейти к [шагу 4](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)шагу 4 и использовать тестовый образ kollekcioner47/secretapp из Docker Hub.
Однако в рамках этого практического руководства рекомендуется использовать свой образ в Artifact Registry, так как это целевой сценарий для продакшн-развертывания.

Если вы загрузите в реестр случайный или неполный образ без описанных ниже настроек Dockerfile, приложение не запустится, так как в нем не будут установлены необходимые библиотеки, например Flask, psycopg2-binary и другие.

1. Подготовьте приложение.
На отдельной виртуальной машине с установленным Docker создайте файл app.py:
import osimport psycopg2from flask import Flask
app = Flask(__name__)
@app.route("/")def index(): conn = psycopg2.connect( dbname="postgres", user=os.getenv("POSTGRES_USER"), password=os.getenv("POSTGRES_PASSWORD"), host="postgres", port="5432" ) cur = conn.cursor() cur.execute("SELECT version();") result = cur.fetchone() cur.close() conn.close() return f"Connected to PostgreSQL: {result}"
if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
2. Создайте Dockerfile:
FROM python:3.10-slimWORKDIR /appCOPY app.py .RUN apt-get update && apt-get install -y gcc libpq-dev && \ pip install flask psycopg2-binary && \ apt-get cleanCMD ["python", "app.py"]
3. Подготовьте среду для сборки образа приложения и его загрузки в Artifact Registry.
Для этого выполните шаги 2–6 [инструкции](https://cloud.ru/docs/container-apps-evolution/ug/topics/tutorials__before-work)инструкции.
4. Соберите и загрузите образ:
docker build -t <your-registry-uri>/secretapp:latest .docker push <your-registry-uri>/secretapp:latest

Где <your-registry-uri> — URI реестра из сервиса Artifact Registry.

Подготовьте приложение.
На отдельной виртуальной машине с установленным Docker создайте файл app.py:

```bash
import
os
import
psycopg2
from flask
import
Flask
app
=
Flask
(
__name__
)
@app.route
(
"/"
)
def index
(
)
:
conn
=
psycopg2.connect
(
dbname
=
"postgres"
,
user
=
os.getenv
(
"POSTGRES_USER"
)
,
password
=
os.getenv
(
"POSTGRES_PASSWORD"
)
,
host
=
"postgres"
,
port
=
"5432"
)
cur
=
conn.cursor
(
)
cur.execute
(
"SELECT version();"
)
result
=
cur.fetchone
(
)
cur.close
(
)
conn.close
(
)
return
f
"Connected to PostgreSQL: {result}"
if
__name__
==
"__main__"
:
app.run
(
host
=
"0.0.0.0"
,
port
=
5000
)
```

Создайте Dockerfile:

```bash
FROM python:3.10-slim
WORKDIR /app
COPY app.py
.
RUN
apt-get
update
&&
apt-get
install
-y
gcc libpq-dev
&&
\
pip
install
flask psycopg2-binary
&&
\
apt-get
clean
CMD
[
"python"
,
"app.py"
]
```

Подготовьте среду для сборки образа приложения и его загрузки в Artifact Registry.
Для этого выполните шаги 2–6 [инструкции](https://cloud.ru/docs/container-apps-evolution/ug/topics/tutorials__before-work)инструкции.

Соберите и загрузите образ:

```bash
docker
build
-t
<
your-registry-uri
>
/secretapp:latest
.
docker
push
<
your-registry-uri
>
/secretapp:latest
```

Где <your-registry-uri> — URI реестра из сервиса Artifact Registry.

## 4. Разверните Flask-приложение в Managed Kubernetes

На этом шаге вы развернете приложение, которое подключается к PostgreSQL с использованием Kubernetes Secret.

Если вы выполнили [шаг 3](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)шаг 3, используйте образ из своего Artifact Registry.
Если вы пропустили [шаг 3](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__secret)шаг 3, укажите тестовый образ kollekcioner47/secretapp из Docker Hub.
Работоспособность образа в этом случае не гарантируется при измененных настройках.

1. Создайте файл app-deployment.yaml:
apiVersion: apps/v1kind: Deploymentmetadata: name: pg-clientspec: replicas: 1 selector: matchLabels: app: pg-client template: metadata: labels: app: pg-client spec: containers: - name: pg-client image: <your-registry-uri>/secretapp:latest # basic scenario # image: kollekcioner47/secretapp # alternative scenario env: - name: POSTGRES_USER valueFrom: secretKeyRef: name: pg-secret key: POSTGRES_USER - name: POSTGRES_PASSWORD valueFrom: secretKeyRef: name: pg-secret key: POSTGRES_PASSWORD ports: - containerPort: 5000---apiVersion: v1kind: Servicemetadata: name: pg-client-servicespec: selector: app: pg-client ports: - port: 80 targetPort: 5000 type: LoadBalancer
2. Примените манифест:
kubectl apply -f app-deployment.yaml

Результат:
deployment.apps/pg-client createdservice/pg-client-service created

Создайте файл app-deployment.yaml:

```bash
apiVersion
:
apps/v1
kind
:
Deployment
metadata
:
name
:
pg
-
client
spec
:
replicas
:
1
selector
:
matchLabels
:
app
:
pg
-
client
template
:
metadata
:
labels
:
app
:
pg
-
client
spec
:
containers
:
-
name
:
pg
-
client
image
:
<your
-
registry
-
uri
>
/secretapp
:
latest
# basic scenario
# image: kollekcioner47/secretapp # alternative scenario
env
:
-
name
:
POSTGRES_USER
valueFrom
:
secretKeyRef
:
name
:
pg
-
secret
key
:
POSTGRES_USER
-
name
:
POSTGRES_PASSWORD
valueFrom
:
secretKeyRef
:
name
:
pg
-
secret
key
:
POSTGRES_PASSWORD
ports
:
-
containerPort
:
5000
---
apiVersion
:
v1
kind
:
Service
metadata
:
name
:
pg
-
client
-
service
spec
:
selector
:
app
:
pg
-
client
ports
:
-
port
:
80
targetPort
:
5000
type
:
LoadBalancer
```

Примените манифест:

```bash
kubectl apply
-f
app-deployment.yaml
```

Результат:

```bash
deployment.apps/pg-client created
service/pg-client-service created
```

## 5. Проверьте результат

Убедитесь, что приложение работает корректно.

1. Получите внешний IP:
kubectl get svc pg-client-service
2. Перейдите по адресу http://<external-ip> в браузере.
Если все настроено верно, в веб-интерфейсе отобразится текст с версией PostgreSQL, например:
Connected to PostgreSQL: ('PostgreSQL 15.14 (Debian 15.14-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit',)

Это означает, что Flask-приложение развернуто в Kubernetes и успешно подключено к базе данных: приложение выполняет SQL-запрос SELECT VERSION(), получает из PostgreSQL строку с номером версии и отображает ее на странице.

Получите внешний IP:

```bash
kubectl get svc pg-client-service
```

![../_images/s__external-ip.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__external-ip.png)

Перейдите по адресу http://<external-ip> в браузере.
Если все настроено верно, в веб-интерфейсе отобразится текст с версией PostgreSQL, например:

```bash
Connected to PostgreSQL:
(
'PostgreSQL 15.14 (Debian 15.14-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit'
,
)
```

![../_images/s__version-posgresql.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__version-posgresql.png)

Это означает, что Flask-приложение развернуто в Kubernetes и успешно подключено к базе данных: приложение выполняет SQL-запрос SELECT VERSION(), получает из PostgreSQL строку с номером версии и отображает ее на странице.

Таким образом, вы развернули контейнерное Flask-приложение в Kubernetes и использовали Secret для безопасного хранения логина и пароля к базе данных.

## Результат

Вы научились:

- Использовать Kubernetes Secrets для безопасного хранения логинов и паролей.
- Разворачивать базу данных PostgreSQL в Kubernetes.
- Собирать и использовать готовое Flask-приложение, читающее из базы данных.
- Подключать приложение к базе данных с помощью переменных среды из Secret.
- Использовать Service типа LoadBalancer для доступа к приложению.

Использовать Kubernetes Secrets для безопасного хранения логинов и паролей.

Разворачивать базу данных PostgreSQL в Kubernetes.

Собирать и использовать готовое Flask-приложение, читающее из базы данных.

Подключать приложение к базе данных с помощью переменных среды из Secret.

Использовать Service типа LoadBalancer для доступа к приложению.

Этот подход можно использовать в реальных проектах при развертывании микросервисов и работе с конфиденциальными данными.
