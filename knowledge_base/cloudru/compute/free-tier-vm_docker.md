---
title: Запуск контейнеризированного приложения на виртуальной машине с помощью Docker и Docker Compose
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker
topic: compute
---
# Запуск контейнеризированного приложения на виртуальной машине с помощью Docker и Docker Compose

С помощью этого руководства вы соберете контейнерное приложение и запустите его на виртуальной машине.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к приложению из интернета.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к приложению из интернета.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Шаги:

1. [Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте виртуальную машину.
2. [Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Настройте группу безопасности.
3. [Установите Docker Engine](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Установите Docker Engine.
4. [Создайте и запустите контейнер с помощью средств Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте и запустите контейнер с помощью средств Docker.
5. [Создайте приложение с помощью Docker Compose](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте приложение с помощью Docker Compose.

[Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте виртуальную машину.

[Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Настройте группу безопасности.

[Установите Docker Engine](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Установите Docker Engine.

[Создайте и запустите контейнер с помощью средств Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте и запустите контейнер с помощью средств Docker.

[Создайте приложение с помощью Docker Compose](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__docker)Создайте приложение с помощью Docker Compose.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Создайте виртуальную машину

1. [Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару.
2. [Загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичный ключ в облако.
3. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

В поле Название укажите название виртуальной машины, например docker-server.
На вкладке Публичные выберите образ Ubuntu 22.04.
Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.
В поле Логин укажите логин пользователя виртуальной машины, например user1.
Выберите метод аутентификации — публичный ключ.
В поле Публичный ключ выберите ключ, загруженный на предыдущем шаге.

[Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару.

[Загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичный ключ в облако.

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например docker-server.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.
4. В поле Логин укажите логин пользователя виртуальной машины, например user1.
5. Выберите метод аутентификации — публичный ключ.
6. В поле Публичный ключ выберите ключ, загруженный на предыдущем шаге.

В поле Название укажите название виртуальной машины, например docker-server.

На вкладке Публичные выберите образ Ubuntu 22.04.

Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.

В поле Логин укажите логин пользователя виртуальной машины, например user1.

Выберите метод аутентификации — публичный ключ.

В поле Публичный ключ выберите ключ, загруженный на предыдущем шаге.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина docker-server;
- статус виртуальной машины — «Запущена»;
- виртуальной машине назначен публичный IP-адрес.

отображается виртуальная машина docker-server;

статус виртуальной машины — «Запущена»;

виртуальной машине назначен публичный IP-адрес.

## 2. Настройте группу безопасности

Группы безопасности в облаке Evolution позволяют контролировать входящий и исходящий трафик для создаваемых ресурсов.

Вы настроите правила фильтрации трафика — разрешите весь входящий трафик по порту 80 и весь исходящий трафик.
[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины docker-server.
2. Укажите Название группы безопасности, например docker-server.
3. Добавьте правила входящего и исходящего трафика.
Правило входящего трафика:

Протокол — TCP.
Порт — 80.
Тип источника — IP-адрес.
Источник — 0.0.0.0/0.

Правило исходящего трафика:

Протокол — Любой.
Порт — оставьте пустым.
Тип адресата — IP-адрес.
Адресат — 0.0.0.0/0.
4. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине docker-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины docker-server.

Укажите Название группы безопасности, например docker-server.

Добавьте правила входящего и исходящего трафика.

Правило входящего трафика:

- Протокол — TCP.
- Порт — 80.
- Тип источника — IP-адрес.
- Источник — 0.0.0.0/0.

Протокол — TCP.

Порт — 80.

Тип источника — IP-адрес.

Источник — 0.0.0.0/0.

Правило исходящего трафика:

- Протокол — Любой.
- Порт — оставьте пустым.
- Тип адресата — IP-адрес.
- Адресат — 0.0.0.0/0.

Протокол — Любой.

Порт — оставьте пустым.

Тип адресата — IP-адрес.

Адресат — 0.0.0.0/0.

[Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине docker-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» в разделе Сетевые параметры отображается группа безопасности.

## 3. Установите Docker Engine

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.
2. В командной строке выполните команду:
curl -fsSL get.docker.com -o get-docker.sh && sudo sh get-docker.sh

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.

В командной строке выполните команду:

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

## 4. Создайте и запустите контейнер с помощью средств Docker

1. Создайте директорию containerapp и перейдите в нее.
В командной строке выполните команду:
mkdir containerapp && cd containerapp
2. Создайте файл Dockerfile:
sudo nano Dockerfile
3. В открывшемся редакторе nano вставьте текст:
FROM tiangolo/uwsgi-nginx-flask:python3.12COPY ./app /app
4. Нажмите комбинацию клавиш Ctrl + O, чтобы сохранить файл.
5. Нажмите комбинацию клавиш Ctrl + X, чтобы выйти из редактора nano.
6. Создайте директорию для приложения app и перейдите в нее:
mkdir app && cd app
7. Создайте python-файл приложения:
sudo nano main.py
8. В открывшемся окне редактора вставьте код:
from flask import Flaskapp = Flask(__name__)@app.route("/")def hello(): return "Hello World from Flask"if __name__ == "__main__": app.run(host='0.0.0.0', debug=True, port=80)
9. Вернитесь на уровень выше — в директорию containerapp:
cd ..
10. Соберите образ контейнера:
sudo docker build -t containerapp .
11. После того как сборка образа закончится, запустите контейнер на виртуальной машине:
sudo docker run -d --name containerapp -p 80:80 containerapp
12. Убедитесь, что созданный мини-сайт доступен по публичному адресу виртуальной машины.
В браузере перейдите по адресу http://<публичный_IP_виртуальной_машины> — откроется страница с текстом «Hello World from Flask».

Создайте директорию containerapp и перейдите в нее.
В командной строке выполните команду:

```bash
mkdir
containerapp
&&
cd
containerapp
```

Создайте файл Dockerfile:

```bash
sudo
nano
Dockerfile
```

В открывшемся редакторе nano вставьте текст:

```bash
FROM tiangolo/uwsgi-nginx-flask:python3.12
COPY ./app /app
```

Нажмите комбинацию клавиш Ctrl + O, чтобы сохранить файл.

Нажмите комбинацию клавиш Ctrl + X, чтобы выйти из редактора nano.

Создайте директорию для приложения app и перейдите в нее:

```bash
mkdir
app
&&
cd
app
```

Создайте python-файл приложения:

```bash
sudo
nano
main.py
```

В открывшемся окне редактора вставьте код:

```bash
from
flask
import
Flask
app
=
Flask
(
__name__
)
@app
.
route
(
"/"
)
def
hello
(
)
:
return
"Hello World from Flask"
if
__name__
==
"__main__"
:
app
.
run
(
host
=
'0.0.0.0'
,
debug
=
True
,
port
=
80
)
```

Вернитесь на уровень выше — в директорию containerapp:

```bash
cd
..
```

Соберите образ контейнера:

```bash
sudo
docker
build
-t
containerapp
.
```

После того как сборка образа закончится, запустите контейнер на виртуальной машине:

```bash
sudo
docker
run
-d
--name
containerapp
-p
80
:80 containerapp
```

Убедитесь, что созданный мини-сайт доступен по публичному адресу виртуальной машины.
В браузере перейдите по адресу http://<публичный_IP_виртуальной_машины> — откроется страница с текстом «Hello World from Flask».

## 5. Создайте приложение с помощью Docker Compose

1. Остановите и удалите контейнер Docker.
В командной строке выполните команду:
sudo docker rm -f containerapp
2. Установите docker-compose:
sudo apt install docker-compose
3. Создайте файл docker-compose в директории containerapp:
sudo nano docker-compose.yaml
4. Вставьте в созданный файл описание создаваемого контейнера:
version: '3.8'services: flask-app: image: tiangolo/uwsgi-nginx-flask:python3.12 ports: - "80:80" volumes: - ./app/main.py:/app/main.py
5. Запустите контейнер с помощью docker-compose:
sudo docker-compose up -d flask-app
6. Убедитесь, что приложение успешно запущено, — в браузере перейдите по адресу http://<публичный_IP_виртуальной_машины>.
Если все предыдущие шаги были выполнены корректно, на странице браузера отобразится следующий текст:

Остановите и удалите контейнер Docker.
В командной строке выполните команду:

```bash
sudo
docker
rm
-f
containerapp
```

Установите docker-compose:

```bash
sudo
apt
install
docker-compose
```

Создайте файл docker-compose в директории containerapp:

```bash
sudo
nano
docker-compose.yaml
```

Вставьте в созданный файл описание создаваемого контейнера:

```bash
version
:
'3.8'
services
:
flask-app
:
image
:
tiangolo/uwsgi
-
nginx
-
flask
:
python3.12
ports
:
-
"80:80"
volumes
:
-
./app/main.py
:
/app/main.py
```

Запустите контейнер с помощью docker-compose:

```bash
sudo
docker-compose
up
-d
flask-app
```

Убедитесь, что приложение успешно запущено, — в браузере перейдите по адресу http://<публичный_IP_виртуальной_машины>.
Если все предыдущие шаги были выполнены корректно, на странице браузера отобразится следующий текст:

![../_images/img__docker__hello-page.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__docker__hello-page.png)

## Результат

Вы создали виртуальную машину и запустили контейнерное приложение с помощью Docker и Docker Compose.
