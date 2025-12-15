---
title: Развертывание отказоустойчивого веб-приложения с разделением компонентов во фреймворке Docker Swarm
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm
topic: compute
---
# Развертывание отказоустойчивого веб-приложения с разделением компонентов во фреймворке Docker Swarm

С помощью этого руководства вы научитесь разворачивать в кластере Docker Swarm микросервисное веб-приложение, состоящее из трех компонентов: frontend, backend и база данных.
Приложение будет работать с веб-интерфейсом, API-сервисом и централизованным хранилищем данных.

Отказоустойчивость архитектуры будет обеспечена за счет следующих технологий:

- репликация сервисов frontend и backend на нескольких виртуальных машинах, объединенных в один кластер;
- использование базы данных MySQL, развернутой как сервис внутри Swarm;
- хранение данных в томах для обеспечения их устойчивости к сбоям контейнеров.

репликация сервисов frontend и backend на нескольких виртуальных машинах, объединенных в один кластер;

использование базы данных MySQL, развернутой как сервис внутри Swarm;

хранение данных в томах для обеспечения их устойчивости к сбоям контейнеров.

В конце вы сможете протестировать доступность системы при отключении одного из узлов кластера.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальным машинам через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- [Load Balancer](https://cloud.ru/docs/nlb/ug/index)Load Balancer — балансировщик нагрузки для виртуальных машин.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальным машинам через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Load Balancer](https://cloud.ru/docs/nlb/ug/index)Load Balancer — балансировщик нагрузки для виртуальных машин.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Разверните ресурсы в облаке.
2. [Настройте виртуальные машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте виртуальные машины.
3. [Создайте Docker Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте Docker Swarm.
4. [Создайте структуру каталогов и файлы](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте структуру каталогов и файлы.
5. [Создайте backend-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте backend-приложение.
6. [Создайте Dockerfile для backend-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте Dockerfile для backend-приложения.
7. [Создайте frontend-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте frontend-приложение.
8. [Настройте структуру базы данных](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте структуру базы данных.
9. [Создайте файл для запуска приложения в Docker Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте файл для запуска приложения в Docker Swarm.
10. [Разверните приложение в Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Разверните приложение в Swarm.
11. [Настройте балансировщик нагрузки](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте балансировщик нагрузки.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Разверните ресурсы в облаке.

[Настройте виртуальные машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте виртуальные машины.

[Создайте Docker Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте Docker Swarm.

[Создайте структуру каталогов и файлы](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте структуру каталогов и файлы.

[Создайте backend-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте backend-приложение.

[Создайте Dockerfile для backend-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте Dockerfile для backend-приложения.

[Создайте frontend-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте frontend-приложение.

[Настройте структуру базы данных](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте структуру базы данных.

[Создайте файл для запуска приложения в Docker Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Создайте файл для запуска приложения в Docker Swarm.

[Разверните приложение в Swarm](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Разверните приложение в Swarm.

[Настройте балансировщик нагрузки](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__docker-swarm)Настройте балансировщик нагрузки.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.
3. [Создайте реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте реестр в Artifact Registry.
Скопируйте полученный URI реестра, он будет нужен для выполнения дальнейших шагов.
4. [Получите ключи доступа сервисного аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Получите ключи доступа сервисного аккаунта.
Запишите Key ID (логин) и Key Secret (пароль), они будут нужны для выполнения дальнейших шагов.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.

[Создайте реестр в Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте реестр в Artifact Registry.
Скопируйте полученный URI реестра, он будет нужен для выполнения дальнейших шагов.

[Получите ключи доступа сервисного аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Получите ключи доступа сервисного аккаунта.
Запишите Key ID (логин) и Key Secret (пароль), они будут нужны для выполнения дальнейших шагов.

## 1. Разверните ресурсы в облаке

Все создаваемые ресурсы должны располагаться в одной

1. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.
2. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием swarm-vpc.
3. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть swarm-subnet в виртуальной сети swarm-vpc.
4. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием swarm-sg и добавьте в нее правило входящего трафика со следующими параметрами:
 ПротоколПортТип источникаИсточникTCP8080IP-адрес0.0.0.0/0
5. [Создайте три виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте три виртуальные машины со следующими параметрами:

Название — docker-swarm-manager-1, docker-swarm-worker-1 и docker-swarm-worker-2.
Зона доступности — та же, что у подсети и группы безопасности.
Образ — публичный образ Ubuntu 22.04.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
VPC — swarm-vpc.
Подсеть — swarm-subnet.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте группу swarm-sg.
Метод аутентификации — выберите публичный ключ и укажите SSH-ключ, созданный ранее.
6. Запишите публичные IP-адреса каждой виртуальной машины.
В этом руководстве используются следующие IP-адреса:

docker-swarm-manager-1 — 176.123.162.37;
docker-swarm-worker-1 — 176.109.104.79;
docker-swarm-worker-2 — 176.123.162.146.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием swarm-vpc.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть swarm-subnet в виртуальной сети swarm-vpc.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием swarm-sg и добавьте в нее правило входящего трафика со следующими параметрами:

Протокол

Порт

Тип источника

Источник

TCP

8080

IP-адрес

0.0.0.0/0

[Создайте три виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте три виртуальные машины со следующими параметрами:

- Название — docker-swarm-manager-1, docker-swarm-worker-1 и docker-swarm-worker-2.
- Зона доступности — та же, что у подсети и группы безопасности.
- Образ — публичный образ Ubuntu 22.04.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- VPC — swarm-vpc.
- Подсеть — swarm-subnet.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте группу swarm-sg.
- Метод аутентификации — выберите публичный ключ и укажите SSH-ключ, созданный ранее.

Название — docker-swarm-manager-1, docker-swarm-worker-1 и docker-swarm-worker-2.

Зона доступности — та же, что у подсети и группы безопасности.

Образ — публичный образ Ubuntu 22.04.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

VPC — swarm-vpc.

Подсеть — swarm-subnet.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте группу swarm-sg.

Метод аутентификации — выберите публичный ключ и укажите SSH-ключ, созданный ранее.

Запишите публичные IP-адреса каждой виртуальной машины.
В этом руководстве используются следующие IP-адреса:

- docker-swarm-manager-1 — 176.123.162.37;
- docker-swarm-worker-1 — 176.109.104.79;
- docker-swarm-worker-2 — 176.123.162.146.

docker-swarm-manager-1 — 176.123.162.37;

docker-swarm-worker-1 — 176.109.104.79;

docker-swarm-worker-2 — 176.123.162.146.

## 2. Настройте виртуальные машины

В терминале для каждой из созданных машин выполните действия:

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH с использованием публичного IP-адреса.
2. Установите Docker:
curl -fsSL get.docker.com -o get-docker.sh && sudo sh get-docker.sh
3. [Пройдите аутентификацию для работы с реестром Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию для работы с реестром Artifact Registry.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH с использованием публичного IP-адреса.

Установите Docker:

```bash
curl
-fsSL
get.docker.com
-o
get-docker.sh
&&
sudo
sh
get-docker.sh
```

[Пройдите аутентификацию для работы с реестром Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию для работы с реестром Artifact Registry.

## 3. Создайте кластер Docker Swarm

1. Откройте сессию терминала с подключением к виртуальной машине docker-swarm-manager-1.
2. Создайте кластер при помощи команды:
sudo docker swarm init --default-addr-pool 192.168.100.0/16 --advertise-addr 176.123.162.37

Где:

--default-addr-pool — адрес overlay-сети, которая соединит контейнеры на разных машинах в одну виртуальную сеть.
Без нее распределенные приложения в Swarm работать не будут.
Адрес overlay-сети не должен совпадать с адресом подсети, к которой подключены виртуальные машины.
--advertise-addr — IP-адрес, который менеджер Swarm будет использовать для связи с другими узлами.
Укажите здесь публичный IP-адрес основной машины.
В этом руководстве — 176.123.162.37.

В ответе вернется сообщение, что текущая машина является менеджером кластера, и команда для добавления узлов в кластер:
Swarm initialized: current node (zbjlb49a21tzg3ae0qthjsb7r) is now a manager.
To add a worker to this swarm, run the following command:
 docker swarm join --token SWMTKN-1-example123 176.123.162.37:2377
To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
3. Скопируйте команду для добавления узлов.
4. Для виртуальных машин docker-swarm-worker-1 и docker-swarm-worker-2 в терминале выполните скопированную команду под корневым пользователем:
sudo docker swarm join --token SWMTKN-1-example123 176.123.162.37:2377

В ответе вернется сообщение, что машина назначена worker-узлом в кластере.
5. Убедитесь, что в кластер добавлены нужные узлы.
Для этого перейдите в сессию терминала docker-swarm-manager-1 и выполните команду:
sudo docker node ls

В ответе вернется список узлов:
ID HOSTNAME STATUS AVAILABILITY MANAGER STATUS ENGINE VERSION2vl32ofyer2w7fmx6m5sjldjz * docker-swarm-manager-1 Ready Active Leader 28.3.235r3qrtgb7l4nq3n0ykughkdw docker-swarm-worker-1 Ready Active 28.3.2cllbe9vic7tihon6qqjd9usz5 docker-swarm-worker-2 Ready Active 28.3.20--100

Откройте сессию терминала с подключением к виртуальной машине docker-swarm-manager-1.

Создайте кластер при помощи команды:

```bash
sudo
docker
swarm init --default-addr-pool
192.168
.100.0/16 --advertise-addr
176.123
.162.37
```

Где:

- --default-addr-pool — адрес overlay-сети, которая соединит контейнеры на разных машинах в одну виртуальную сеть.
Без нее распределенные приложения в Swarm работать не будут.
Адрес overlay-сети не должен совпадать с адресом подсети, к которой подключены виртуальные машины.
- --advertise-addr — IP-адрес, который менеджер Swarm будет использовать для связи с другими узлами.
Укажите здесь публичный IP-адрес основной машины.
В этом руководстве — 176.123.162.37.

--default-addr-pool — адрес overlay-сети, которая соединит контейнеры на разных машинах в одну виртуальную сеть.
Без нее распределенные приложения в Swarm работать не будут.
Адрес overlay-сети не должен совпадать с адресом подсети, к которой подключены виртуальные машины.

--advertise-addr — IP-адрес, который менеджер Swarm будет использовать для связи с другими узлами.
Укажите здесь публичный IP-адрес основной машины.
В этом руководстве — 176.123.162.37.

В ответе вернется сообщение, что текущая машина является менеджером кластера, и команда для добавления узлов в кластер:

```bash
Swarm initialized: current
node
(
zbjlb49a21tzg3ae0qthjsb7r
)
is now a manager.
To
add
a worker to this swarm, run the following command:
docker
swarm
join
--token
SWMTKN-1-example123
176.123
.162.37:2377
To
add
a manager to this swarm, run
'docker swarm join-token manager'
and follow the instructions.
```

Скопируйте команду для добавления узлов.

Для виртуальных машин docker-swarm-worker-1 и docker-swarm-worker-2 в терминале выполните скопированную команду под корневым пользователем:

```bash
sudo
docker
swarm
join
--token
SWMTKN-1-example123
176.123
.162.37:2377
```

В ответе вернется сообщение, что машина назначена worker-узлом в кластере.

Убедитесь, что в кластер добавлены нужные узлы.
Для этого перейдите в сессию терминала docker-swarm-manager-1 и выполните команду:

```bash
sudo
docker
node
ls
```

В ответе вернется список узлов:

```bash
ID
HOSTNAME
STATUS AVAILABILITY MANAGER STATUS ENGINE VERSION
2vl32ofyer2w7fmx6m5sjldjz * docker-swarm-manager-1 Ready Active Leader
28.3
.2
35r3qrtgb7l4nq3n0ykughkdw docker-swarm-worker-1 Ready Active
28.3
.2
cllbe9vic7tihon6qqjd9usz5 docker-swarm-worker-2 Ready Active
28.3
.20--100
```

## 4. Создайте структуру каталогов и файлы проекта

1. На виртуальной машине docker-swarm-manager-1 создайте новую директорию для проекта и перейдите в нее:
mkdir swarm-appcd swarm-app
2. Создайте директории для всех компонентов приложения и хранения файлов базы данных:
mkdir backend frontend mysql_data mysql-init
3. Убедитесь, что структура каталогов веб-приложения создана верно, выполнив команду ls.
4. Перейдите в директорию backend и создайте файлы для приложения на Flask:
cd backendtouch app.py requirements.txt Dockerfilecd ..

Где:

app.py — исходный код сервера backend;
requirements.txt — список зависимостей Python;
Dockerfile — инструкции для сборки образа backend-приложения.
5. Перейдите в директорию frontend и создайте файлы для frontend-приложения:
cd frontendtouch default.conf Dockerfilecd ..

Где:

default.conf — конфигурационный файл nginx;
Dockerfile — инструкции для сборки образа frontend-приложения.
6. Перейдите в директорию mysql-init и создайте файлы для frontend-приложения:
cd mysql-inittouch init.sqlcd ..
7. Создайте в корне проекта файл docker-swarm.yml, который будет описывать стек приложения:
touch docker-swarm.yml

На виртуальной машине docker-swarm-manager-1 создайте новую директорию для проекта и перейдите в нее:

```bash
mkdir
swarm-app
cd
swarm-app
```

Создайте директории для всех компонентов приложения и хранения файлов базы данных:

```bash
mkdir
backend frontend mysql_data mysql-init
```

Убедитесь, что структура каталогов веб-приложения создана верно, выполнив команду ls.

Перейдите в директорию backend и создайте файлы для приложения на Flask:

```bash
cd
backend
touch
app.py requirements.txt Dockerfile
cd
..
```

Где:

- app.py — исходный код сервера backend;
- requirements.txt — список зависимостей Python;
- Dockerfile — инструкции для сборки образа backend-приложения.

app.py — исходный код сервера backend;

requirements.txt — список зависимостей Python;

Dockerfile — инструкции для сборки образа backend-приложения.

Перейдите в директорию frontend и создайте файлы для frontend-приложения:

```bash
cd
frontend
touch
default.conf Dockerfile
cd
..
```

Где:

- default.conf — конфигурационный файл nginx;
- Dockerfile — инструкции для сборки образа frontend-приложения.

default.conf — конфигурационный файл nginx;

Dockerfile — инструкции для сборки образа frontend-приложения.

Перейдите в директорию mysql-init и создайте файлы для frontend-приложения:

```bash
cd
mysql-init
touch
init.sql
cd
..
```

Создайте в корне проекта файл docker-swarm.yml, который будет описывать стек приложения:

```bash
touch
docker-swarm.yml
```

Проверьте итоговую структуру каталогов.
На этом этапе она должна иметь следующий вид:

```bash
swarm-app/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── default.conf
│ └── Dockerfile
├── mysql_data/
# directory for volume MySQL
├── mysql-init/
│ └── init.sql
└── docker-swarm.yml
```

## 5. Создайте backend-приложение

1. Перейдите в директорию backend и откройте файл requirements.txt:
cd backendnano requirements.txt
2. Добавьте код для определения зависимости вашего приложения и сохраните изменения:
flaskflask-mysqldb
3. Откройте файл backend/app.py:
nano app.py
4. Добавьте минимальный рабочий код Flask-приложения с подключением к MySQL:
from flask import Flask, request, redirect, url_for, render_template_stringfrom flask_mysqldb import MySQL
app = Flask(__name__)
# MySQL connection settingsapp.config['MYSQL_HOST'] = 'db'app.config['MYSQL_USER'] = 'user'app.config['MYSQL_PASSWORD'] = 'password'app.config['MYSQL_DB'] = 'appdb'
# Initializing MySQLmysql = MySQL(app)
# HTML-template with BootstrapHTML_TEMPLATE = '''<!DOCTYPE html><html lang="ru"><head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Notes in Docker Swarm</title> <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"></head><body class="bg-light"><div class="container py-5"> <h1 class="mb-4 text-center">📝 Notes in Swarm</h1>
 <form method="post" action="/" class="mb-4"> <div class="input-group"> <input type="text" name="note" class="form-control" placeholder="Enter a new note" required> <button class="btn btn-primary" type="submit">Add</button> </div> </form>
 <div class="card shadow"> <div class="card-body"> {% if notes %} <ul class="list-group"> {% for id, content in notes %} <li class="list-group-item d-flex justify-content-between align-items-center"> <span>{{ content }}</span> <span class="badge bg-secondary rounded-pill">#{{ id }}</span> </li> {% endfor %} </ul> {% else %} <p class="text-muted">There are no notes yet...</p> {% endif %} </div> </div></div></body></html>'''
@app.route('/', methods=['GET', 'POST'])def index(): conn = mysql.connection cursor = conn.cursor() if request.method == 'POST': # читаем поле note из формы note = request.form.get('note') if note: cursor.execute("INSERT INTO entries (name) VALUES (%s)", (note,)) conn.commit() return redirect(url_for('index'))
 # GET: cursor.execute("SELECT id, name FROM entries ORDER BY id") notes = cursor.fetchall() cursor.close()
 return render_template_string(HTML_TEMPLATE, notes=notes)
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)

Перейдите в директорию backend и откройте файл requirements.txt:

```bash
cd
backend
nano
requirements.txt
```

Добавьте код для определения зависимости вашего приложения и сохраните изменения:

```bash
flask
flask
-
mysqldb
```

Откройте файл backend/app.py:

```bash
nano
app.py
```

Добавьте минимальный рабочий код Flask-приложения с подключением к MySQL:

```bash
from
flask
import
Flask
,
request
,
redirect
,
url_for
,
render_template_string
from
flask_mysqldb
import
MySQL
app
=
Flask
(
__name__
)
# MySQL connection settings
app
.
config
[
'MYSQL_HOST'
]
=
'db'
app
.
config
[
'MYSQL_USER'
]
=
'user'
app
.
config
[
'MYSQL_PASSWORD'
]
=
'password'
app
.
config
[
'MYSQL_DB'
]
=
'appdb'
# Initializing MySQL
mysql
=
MySQL
(
app
)
# HTML-template with Bootstrap
HTML_TEMPLATE
=
'''
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Notes in Docker Swarm</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container py-5">
<h1 class="mb-4 text-center">📝 Notes in Swarm</h1>
<form method="post" action="/" class="mb-4">
<div class="input-group">
<input type="text" name="note" class="form-control" placeholder="Enter a new note" required>
<button class="btn btn-primary" type="submit">Add</button>
</div>
</form>
<div class="card shadow">
<div class="card-body">
{% if notes %}
<ul class="list-group">
{% for id, content in notes %}
<li class="list-group-item d-flex justify-content-between align-items-center">
<span>{{ content }}</span>
<span class="badge bg-secondary rounded-pill">#{{ id }}</span>
</li>
{% endfor %}
</ul>
{% else %}
<p class="text-muted">There are no notes yet...</p>
{% endif %}
</div>
</div>
</div>
</body>
</html>
'''
@app
.
route
(
'/'
,
methods
=
[
'GET'
,
'POST'
]
)
def
index
(
)
:
conn
=
mysql
.
connection
cursor
=
conn
.
cursor
(
)
if
request
.
method
==
'POST'
:
# читаем поле note из формы
note
=
request
.
form
.
get
(
'note'
)
if
note
:
cursor
.
execute
(
"INSERT INTO entries (name) VALUES (%s)"
,
(
note
,
)
)
conn
.
commit
(
)
return
redirect
(
url_for
(
'index'
)
)
# GET:
cursor
.
execute
(
"SELECT id, name FROM entries ORDER BY id"
)
notes
=
cursor
.
fetchall
(
)
cursor
.
close
(
)
return
render_template_string
(
HTML_TEMPLATE
,
notes
=
notes
)
if
__name__
==
'__main__'
:
app
.
run
(
host
=
'0.0.0.0'
,
port
=
5000
)
```

## 6. Создайте Dockerfile для backend-приложения

1. Откройте Dockerfile в редакторе:
nano Dockerfile
2. Вставьте в Dockerfile следующий код:
FROM python:3.9-slim
# Installing dependencies for compiling mysqlclientRUN apt-get update && apt-get install -y \ gcc \ default-libmysqlclient-dev \ pkg-config \ && rm -rf /var/lib/apt/lists/*
WORKDIR /appCOPY requirements.txt requirements.txtRUN pip install --no-cache-dir -r requirements.txtCOPY . .CMD ["python", "app.py"]
3. Соберите образ и загрузите его в реестр:
sudo docker build . -t <registry_name>.cr.cloud.ru/backend:1.0 --platform linux/amd64sudo docker push <registry_name>.cr.cloud.ru/backend:1.0

Где:

<registry_name>.cr.cloud.ru — URI реестра, в котором находится репозиторий.
backend — название репозитория, соответствует названию загружаемого образа.
platform linux/amd64 — флаг указывает, что образ должен быть собран для платформы linux/amd64.
Это требуется для создания контейнера.
1.0 — тег образа.

Откройте Dockerfile в редакторе:

```bash
nano
Dockerfile
```

Вставьте в Dockerfile следующий код:

```bash
FROM python
:
3.9
-
slim
# Installing dependencies for compiling mysqlclient
RUN apt
-
get update
&
&
apt
-
get install
-
y \
gcc \
default
-
libmysqlclient
-
dev \
pkg
-
config \
&
&
rm
-
rf
/
var
/
lib
/
apt
/
lists
/
*
WORKDIR
/
app
COPY requirements
.
txt requirements
.
txt
RUN pip install
-
-
no
-
cache
-
dir
-
r requirements
.
txt
COPY
.
.
CMD
[
"python"
,
"app.py"
]
```

Соберите образ и загрузите его в реестр:

```bash
sudo
docker
build
.
-t
<
registry_name
>
.cr.cloud.ru/backend:1.0
--platform
linux/amd64
sudo
docker
push
<
registry_name
>
.cr.cloud.ru/backend:1.0
```

Где:

- <registry_name>.cr.cloud.ru — URI реестра, в котором находится репозиторий.
- backend — название репозитория, соответствует названию загружаемого образа.
- platform linux/amd64 — флаг указывает, что образ должен быть собран для платформы linux/amd64.
Это требуется для создания контейнера.
- 1.0 — тег образа.

<registry_name>.cr.cloud.ru — URI реестра, в котором находится репозиторий.

backend — название репозитория, соответствует названию загружаемого образа.

platform linux/amd64 — флаг указывает, что образ должен быть собран для платформы linux/amd64.
Это требуется для создания контейнера.

1.0 — тег образа.

## 7. Создайте frontend-приложение

1. Перейдите в директорию frontend, создайте файл default.conf и откройте его:
cd ../frontendnano default.conf
2. Вставьте следующий код:
server { listen 80;
 # Proxy all requests (GET, POST, etc.) to backend location / { proxy_pass http://backend:5000; proxy_http_version 1.1; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; }}
3. Создайте файл Dockerfile:
nano Dockerfile
4. Вставьте следующий код:
FROM nginx:1.27.5-alpine # Using nginx as a web serverCOPY default.conf /etc/nginx/conf.d/default.conf # Copy the HTML file to the standart nginx directory
5. Соберите ваш образ и загрузите его в реестр:
sudo docker build . -t <registry_name>.cr.cloud.ru/frontend:1.0 --platform linux/amd64sudo docker push <registry_name>.cr.cloud.ru/frontend:1.0

Перейдите в директорию frontend, создайте файл default.conf и откройте его:

```bash
cd
..
/frontend
nano
default.conf
```

Вставьте следующий код:

```bash
server
{
listen
80
;
# Proxy all requests (GET, POST, etc.) to backend
location /
{
proxy_pass http://backend:5000
;
proxy_http_version
1.1
;
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
proxy_set_header X-Forwarded-Proto
$scheme
;
}
}
```

Создайте файл Dockerfile:

```bash
nano
Dockerfile
```

Вставьте следующий код:

```bash
FROM nginx:1.27.5-alpine
# Using nginx as a web server
COPY default.conf /etc/nginx/conf.d/default.conf
# Copy the HTML file to the standart nginx directory
```

Соберите ваш образ и загрузите его в реестр:

```bash
sudo
docker
build
.
-t
<
registry_name
>
.cr.cloud.ru/frontend:1.0
--platform
linux/amd64
sudo
docker
push
<
registry_name
>
.cr.cloud.ru/frontend:1.0
```

## 8. Настройте структуру базы данных

1. Создайте файл mysql-init/init.sql и перейдите к его редактированию:
cd ../mysql-initnano init.sql
2. Вставьте код, который создает целевую таблицу:
CREATE DATABASE IF NOT EXISTS appdb;USE appdb;
CREATE TABLE IF NOT EXISTS entries ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);
3. Сохраните файл mysql-init/init.sql и вернитесь на уровень выше, выполнив команду cd ...

Создайте файл mysql-init/init.sql и перейдите к его редактированию:

```bash
cd
..
/mysql-init
nano
init.sql
```

Вставьте код, который создает целевую таблицу:

```bash
CREATE DATABASE IF NOT EXISTS appdb
;
USE appdb
;
CREATE TABLE IF NOT EXISTS entries
(
id
INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR
(
255
)
NOT NULL
)
;
```

Сохраните файл mysql-init/init.sql и вернитесь на уровень выше, выполнив команду cd ...

## 9. Создайте файл для запуска приложения в Docker Swarm

Файл должен содержать декларацию трех компонентов проекта в Docker Swarm:

- frontend — перенаправление к приложению, 2 реплики, подключен к overlay-сети;
- backend — Flask-приложение (API), 2 реплики, подключен к overlay-сети;
- база данных — MySQL, 1 реплика, подключена к overlay-сети, хранение данных в томе mysql_data.

frontend — перенаправление к приложению, 2 реплики, подключен к overlay-сети;

backend — Flask-приложение (API), 2 реплики, подключен к overlay-сети;

база данных — MySQL, 1 реплика, подключена к overlay-сети, хранение данных в томе mysql_data.

1. Откройте файл в корне проекта:
nano docker-swarm.yml
2. Вставьте следующий код:
services: db: image: mysql:8.0 environment: MYSQL_ROOT_PASSWORD: rootpass MYSQL_DATABASE: appdb MYSQL_USER: user MYSQL_PASSWORD: password volumes: - db-data:/var/lib/mysql - ./mysql-init:/docker-entrypoint-initdb.d networks: - appnet deploy: placement: constraints: [node.role == manager]
 backend: image: <registry_name>.cr.cloud.ru/backend:1.0 depends_on: - db environment: MYSQL_DATABASE_HOST: db MYSQL_DATABASE_USER: user MYSQL_DATABASE_PASSWORD: password MYSQL_DATABASE_NAME: appdb networks: - appnet deploy: replicas: 2 restart_policy: condition: on-failure
 frontend: image: <registry_name>.cr.cloud.ru/frontend:1.0 ports: - "8080:80" networks: - appnet depends_on: - backend deploy: replicas: 2 restart_policy: condition: on-failure
volumes: db-data:
networks: appnet: driver: overlay

Где:

<registry_name> — название реестра.
volumes: db-data — сохраняет базу между перезапусками.
deploy.replicas — создает отказоустойчивость фронтенда и бэкенда.
networks.overlay — дает сервисам доступ друг к другу по имени, например http://backend:5000.
placement.constraints — закрепляет базу только за менеджером, где том будет доступен локально.

Это простое решение — более сложное потребует использования Galera или Vitess.

Откройте файл в корне проекта:

```bash
nano
docker-swarm.yml
```

Вставьте следующий код:

```bash
services
:
db
:
image
:
mysql
:
8.0
environment
:
MYSQL_ROOT_PASSWORD
:
rootpass
MYSQL_DATABASE
:
appdb
MYSQL_USER
:
user
MYSQL_PASSWORD
:
password
volumes
:
-
db
-
data
:
/var/lib/mysql
-
./mysql
-
init
:
/docker
-
entrypoint
-
initdb.d
networks
:
-
appnet
deploy
:
placement
:
constraints
:
[
node.role == manager
]
backend
:
image
:
<registry_name
>
.cr.cloud.ru/backend
:
1.0
depends_on
:
-
db
environment
:
MYSQL_DATABASE_HOST
:
db
MYSQL_DATABASE_USER
:
user
MYSQL_DATABASE_PASSWORD
:
password
MYSQL_DATABASE_NAME
:
appdb
networks
:
-
appnet
deploy
:
replicas
:
2
restart_policy
:
condition
:
on
-
failure
frontend
:
image
:
<registry_name
>
.cr.cloud.ru/frontend
:
1.0
ports
:
-
"8080:80"
networks
:
-
appnet
depends_on
:
-
backend
deploy
:
replicas
:
2
restart_policy
:
condition
:
on
-
failure
volumes
:
db-data
:
networks
:
appnet
:
driver
:
overlay
```

Где:

- <registry_name> — название реестра.
- volumes: db-data — сохраняет базу между перезапусками.
- deploy.replicas — создает отказоустойчивость фронтенда и бэкенда.
- networks.overlay — дает сервисам доступ друг к другу по имени, например http://backend:5000.
- placement.constraints — закрепляет базу только за менеджером, где том будет доступен локально.

<registry_name> — название реестра.

volumes: db-data — сохраняет базу между перезапусками.

deploy.replicas — создает отказоустойчивость фронтенда и бэкенда.

networks.overlay — дает сервисам доступ друг к другу по имени, например http://backend:5000.

placement.constraints — закрепляет базу только за менеджером, где том будет доступен локально.

Это простое решение — более сложное потребует использования Galera или Vitess.

## 10. Разверните приложение в Swarm

1. Разверните ваше приложение в Swarm, используя команду:
sudo docker stack deploy -c docker-swarm.yml --with-registry-auth myapp
2. Подождите несколько минут, пока загрузятся образы и запустится приложение.
3. Проверьте статус с помощью команды:
sudo docker service ls

Разверните ваше приложение в Swarm, используя команду:

```bash
sudo
docker
stack deploy
-c
docker-swarm.yml --with-registry-auth myapp
```

Подождите несколько минут, пока загрузятся образы и запустится приложение.

Проверьте статус с помощью команды:

```bash
sudo
docker
service
ls
```

Все контейнеры должны быть в статусе «replicated» и с полным количеством реплик.

## 11. Настройте балансировщик нагрузки

Отвяжите публичные адреса от виртуальных машин и добавьте балансировщик нагрузки, чтобы приложение было доступно при выходе из строя рабочего сервера:

1. [Отвяжите публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__unbind-ip)Отвяжите публичный IP-адрес от каждой из трех виртуальных машин.
2. [Создайте балансировщик нагрузки](https://cloud.ru/docs/nlb/ug/topics/guides__create-lb)Создайте балансировщик нагрузки со следующими параметрами:

Зона доступности — та же, в которой расположены виртуальные машины.
VPC — та же, в которой расположены виртуальные машины.
Тип балансировщика — выберите внешний тип балансировщика.
Правило балансировки трафика:

Создайте новую backend-группу и добавьте в нее три созданные виртуальные машины.
Порт балансировщика — 80.
Порт backend группы — 8080.
Включите проверку доступности:

Порт — 8080.
Интервал — 10.
Таймаут — 5.
Порог успешных ответов — 3.
Порог неуспешных ответов — 3.
3. Дождитесь, когда балансировщик нагрузки перейдет в статус «Активен».

[Отвяжите публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__unbind-ip)Отвяжите публичный IP-адрес от каждой из трех виртуальных машин.

[Создайте балансировщик нагрузки](https://cloud.ru/docs/nlb/ug/topics/guides__create-lb)Создайте балансировщик нагрузки со следующими параметрами:

- Зона доступности — та же, в которой расположены виртуальные машины.
- VPC — та же, в которой расположены виртуальные машины.
- Тип балансировщика — выберите внешний тип балансировщика.
- Правило балансировки трафика:

Создайте новую backend-группу и добавьте в нее три созданные виртуальные машины.
Порт балансировщика — 80.
Порт backend группы — 8080.
Включите проверку доступности:

Порт — 8080.
Интервал — 10.
Таймаут — 5.
Порог успешных ответов — 3.
Порог неуспешных ответов — 3.

Зона доступности — та же, в которой расположены виртуальные машины.

VPC — та же, в которой расположены виртуальные машины.

Тип балансировщика — выберите внешний тип балансировщика.

Правило балансировки трафика:

- Создайте новую backend-группу и добавьте в нее три созданные виртуальные машины.
- Порт балансировщика — 80.
- Порт backend группы — 8080.
- Включите проверку доступности:

Порт — 8080.
Интервал — 10.
Таймаут — 5.
Порог успешных ответов — 3.
Порог неуспешных ответов — 3.

Создайте новую backend-группу и добавьте в нее три созданные виртуальные машины.

Порт балансировщика — 80.

Порт backend группы — 8080.

Включите проверку доступности:

- Порт — 8080.
- Интервал — 10.
- Таймаут — 5.
- Порог успешных ответов — 3.
- Порог неуспешных ответов — 3.

Порт — 8080.

Интервал — 10.

Таймаут — 5.

Порог успешных ответов — 3.

Порог неуспешных ответов — 3.

Дождитесь, когда балансировщик нагрузки перейдет в статус «Активен».

## Протестируйте отказоустойчивость и работоспособность приложения

1. Проверьте работоспособность приложения при активности всех рабочих узлов:

Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.
Убедитесь, что:

Загружается веб-интерфейс.
Отображаются записи, если добавлялись.

Добавьте новую запись — она должна сохраниться и отобразиться после обновления.
2. Проверьте работу отказоустойчивости при выходе из строя одного из рабочих узлов:

Выключите виртуальную машину docker-swarm-worker-2.
Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.
Убедитесь, что:

Загружается веб-интерфейс.
Отображаются записи, если добавлялись.

Добавьте новую запись — она должна сохраниться и отобразиться после обновления.

Проверьте работоспособность приложения при активности всех рабочих узлов:

1. Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.
2. Убедитесь, что:

Загружается веб-интерфейс.
Отображаются записи, если добавлялись.
3. Добавьте новую запись — она должна сохраниться и отобразиться после обновления.

Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.

Убедитесь, что:

- Загружается веб-интерфейс.
- Отображаются записи, если добавлялись.

Загружается веб-интерфейс.

Отображаются записи, если добавлялись.

Добавьте новую запись — она должна сохраниться и отобразиться после обновления.

Проверьте работу отказоустойчивости при выходе из строя одного из рабочих узлов:

1. Выключите виртуальную машину docker-swarm-worker-2.
2. Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.
3. Убедитесь, что:

Загружается веб-интерфейс.
Отображаются записи, если добавлялись.
4. Добавьте новую запись — она должна сохраниться и отобразиться после обновления.

Выключите виртуальную машину docker-swarm-worker-2.

Откройте в браузере страницу с адресом публичного IP балансировщика — http://<load_balancer_public_ip>.

Убедитесь, что:

- Загружается веб-интерфейс.
- Отображаются записи, если добавлялись.

Загружается веб-интерфейс.

Отображаются записи, если добавлялись.

Добавьте новую запись — она должна сохраниться и отобразиться после обновления.

[Подробнее о повышении отказоустойчивости Swarm](https://docs.docker.com/engine/swarm/admin_guide)Подробнее о повышении отказоустойчивости Swarm.

## Результат

Вы научились:

- настраивать кластер Docker Swarm и объединять узлы;
- разворачивать многокомпонентные приложения с помощью docker stack deploy;
- использовать overlay-сети для взаимодействия сервисов;
- конфигурировать работу Flask-приложения с внешней базой MySQL;
- обеспечивать сохранность данных с помощью Docker Volumes;
- проверять отказоустойчивость путем симуляции отказа узлов;
- диагностировать состояние кластера и отдельных компонентов с помощью команд Docker.

настраивать кластер Docker Swarm и объединять узлы;

разворачивать многокомпонентные приложения с помощью docker stack deploy;

использовать overlay-сети для взаимодействия сервисов;

конфигурировать работу Flask-приложения с внешней базой MySQL;

обеспечивать сохранность данных с помощью Docker Volumes;

проверять отказоустойчивость путем симуляции отказа узлов;

диагностировать состояние кластера и отдельных компонентов с помощью команд Docker.
