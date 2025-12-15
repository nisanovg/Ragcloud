---
title: Установка Onlyoffice Community на выделенный сервер Bare Metal
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice
topic: compute
---
# Установка Onlyoffice Community на выделенный сервер Bare Metal

С помощью этого руководства вы развернете экосистему приложений для совместной работы Onlyoffice.
Доступ к приложениям обеспечивается через онлайн-портал.

Вы установите и настроите два модуля пакета Onlyoffice Community Edition:

- Сервер документов
- Сервер совместной работы

Сервер документов

Сервер совместной работы

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Разверните инфраструктуру.
2. [Настройте систему для работы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте систему для работы.
3. [Настройте базу данных](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте базу данных.
4. [Настройте контейнеры с модулями Onlyoffice](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте контейнеры с модулями Onlyoffice.
5. [Запустите и настройте Onlyoffice](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Запустите и настройте Onlyoffice.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Разверните инфраструктуру.

[Настройте систему для работы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте систему для работы.

[Настройте базу данных](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте базу данных.

[Настройте контейнеры с модулями Onlyoffice](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Настройте контейнеры с модулями Onlyoffice.

[Запустите и настройте Onlyoffice](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__onlyoffice)Запустите и настройте Onlyoffice.

## 1. Разверните инфраструктуру

1. [Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal.
В блоке Сетевые параметры выберите подсеть по умолчанию и активируйте опцию Подключить публичный IP:
2. Убедитесь, что на сервере работает интернет:
3. [Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.
4. [Установите Docker](https://docs.docker.com/engine/install)Установите Docker.
Пример установки Docker на ОС Debian 10:

[Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal.
В блоке Сетевые параметры выберите подсеть по умолчанию и активируйте опцию Подключить публичный IP:

![../_images/onlyoffice_network_settings.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/onlyoffice_network_settings.png)

Убедитесь, что на сервере работает интернет:

[Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

[Установите Docker](https://docs.docker.com/engine/install)Установите Docker.

Пример установки Docker на ОС Debian 10:

## 2. Настройте систему для работы

1. Подготовьте каталоги для проекта:
sudo mkdir -p "/app/onlyoffice/mysql/conf.d";sudo mkdir -p "/app/onlyoffice/mysql/data";sudo mkdir -p "/app/onlyoffice/mysql/initdb";sudo mkdir -p "/app/onlyoffice/mysql/logs";chown 999:999 /app/onlyoffice/mysql/logs;
sudo mkdir -p "/app/onlyoffice/CommunityServer/data";sudo mkdir -p "/app/onlyoffice/CommunityServer/logs";
sudo mkdir -p "/app/onlyoffice/DocumentServer/data";sudo mkdir -p "/app/onlyoffice/DocumentServer/logs";
2. Создайте сеть для связности Docker-контейнеров:
sudo docker network create --driver bridge onlyoffice

Подготовьте каталоги для проекта:

```bash
sudo
mkdir
-p
"/app/onlyoffice/mysql/conf.d"
;
sudo
mkdir
-p
"/app/onlyoffice/mysql/data"
;
sudo
mkdir
-p
"/app/onlyoffice/mysql/initdb"
;
sudo
mkdir
-p
"/app/onlyoffice/mysql/logs"
;
chown
999
:999 /app/onlyoffice/mysql/logs
;
sudo
mkdir
-p
"/app/onlyoffice/CommunityServer/data"
;
sudo
mkdir
-p
"/app/onlyoffice/CommunityServer/logs"
;
sudo
mkdir
-p
"/app/onlyoffice/DocumentServer/data"
;
sudo
mkdir
-p
"/app/onlyoffice/DocumentServer/logs"
;
```

Создайте сеть для связности Docker-контейнеров:

```bash
sudo
docker
network create
--driver
bridge onlyoffice
```

## 3. Настройте базу данных

1. Создайте файл с конфигурацией SQL-сервера:
echo "[mysqld]sql_mode = 'NO_ENGINE_SUBSTITUTION'max_connections = 1000max_allowed_packet = 1048576000group_concat_max_len = 2048log-error = /var/log/mysql/error.log" > /app/onlyoffice/mysql/conf.d/onlyoffice.cnfsudo chmod 0644 /app/onlyoffice/mysql/conf.d/onlyoffice.cnf

ПримечаниеВ примере использованы минимальные настройки.
Для лучшей производительности рекомендуется использовать mysqltuner и другие инструменты оптимизации.
2. Создайте файл для оптимизации создания пользователей:
echo "CREATE USER 'onlyoffice_user'@'localhost' IDENTIFIED BY 'onlyoffice_pass';CREATE USER 'mail_admin'@'localhost' IDENTIFIED BY '<password>';GRANT ALL PRIVILEGES ON * . * TO 'root'@'%' IDENTIFIED BY '<password>';GRANT ALL PRIVILEGES ON * . * TO 'onlyoffice_user'@'%' IDENTIFIED BY '<password>';GRANT ALL PRIVILEGES ON * . * TO 'mail_admin'@'%' IDENTIFIED BY '<password>';FLUSH PRIVILEGES;" > /app/onlyoffice/mysql/initdb/setup.sql

Где <password> — пароли пользователей.
3. Установите и запустите контейнер с базой данных:
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-mysql-server -p 3306:3306 \-v /app/onlyoffice/mysql/conf.d:/etc/mysql/conf.d \-v /app/onlyoffice/mysql/data:/var/lib/mysql \-v /app/onlyoffice/mysql/initdb:/docker-entrypoint-initdb.d \-v /app/onlyoffice/mysql/logs:/var/log/mysql \-e MYSQL_ROOT_PASSWORD=my-secret-pw \-e MYSQL_DATABASE=onlyoffice \mysql:5.7

Создайте файл с конфигурацией SQL-сервера:

```bash
echo
"[mysqld]
sql_mode = 'NO_ENGINE_SUBSTITUTION'
max_connections = 1000
max_allowed_packet = 1048576000
group_concat_max_len = 2048
log-error = /var/log/mysql/error.log"
>
/app/onlyoffice/mysql/conf.d/onlyoffice.cnf
sudo
chmod
0644 /app/onlyoffice/mysql/conf.d/onlyoffice.cnf
```

В примере использованы минимальные настройки.
Для лучшей производительности рекомендуется использовать mysqltuner и другие инструменты оптимизации.

Создайте файл для оптимизации создания пользователей:

```bash
echo
"CREATE USER 'onlyoffice_user'@'localhost' IDENTIFIED BY 'onlyoffice_pass';
CREATE USER 'mail_admin'@'localhost' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON * . * TO 'root'@'%' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON * . * TO 'onlyoffice_user'@'%' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON * . * TO 'mail_admin'@'%' IDENTIFIED BY '<password>';
FLUSH PRIVILEGES;"
>
/app/onlyoffice/mysql/initdb/setup.sql
```

Где <password> — пароли пользователей.

Установите и запустите контейнер с базой данных:

```bash
sudo
docker
run
--net
onlyoffice
-i
-t
-d
--restart
=
always
--name
onlyoffice-mysql-server
-p
3306
:3306
\
-v
/app/onlyoffice/mysql/conf.d:/etc/mysql/conf.d
\
-v
/app/onlyoffice/mysql/data:/var/lib/mysql
\
-v
/app/onlyoffice/mysql/initdb:/docker-entrypoint-initdb.d
\
-v
/app/onlyoffice/mysql/logs:/var/log/mysql
\
-e
MYSQL_ROOT_PASSWORD
=
my-secret-pw
\
-e
MYSQL_DATABASE
=
onlyoffice
\
mysql:5.7
```

Пример выполнения команд:

## 4. Настройте контейнеры с модулями Onlyoffice

1. Установите и запустите контейнер с сервером документов:
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-document-server \-v /app/onlyoffice/DocumentServer/logs:/var/log/onlyoffice \-v /app/onlyoffice/DocumentServer/data:/var/www/onlyoffice/Data \-v /app/onlyoffice/DocumentServer/lib:/var/lib/onlyoffice \-v /app/onlyoffice/DocumentServer/db:/var/lib/postgresql \onlyoffice/documentserver
2. Установите и запустите контейнер с сервером совместной работы:
sudo docker run --net onlyoffice -i -t -d --restart=always --name onlyoffice-community-server -p 80:80 -p 443:443 -p 5222:5222 \-e MYSQL_SERVER_ROOT_PASSWORD=my-secret-pw \-e MYSQL_SERVER_DB_NAME=onlyoffice \-e MYSQL_SERVER_HOST=onlyoffice-mysql-server \-e MYSQL_SERVER_USER=onlyoffice_user \-e MYSQL_SERVER_PASS=onlyoffice_pass \-e DOCUMENT_SERVER_PORT_80_TCP_ADDR=onlyoffice-document-server \-v /app/onlyoffice/CommunityServer/data:/var/www/onlyoffice/Data \-v /app/onlyoffice/CommunityServer/logs:/var/log/onlyoffice \onlyoffice/communityserver

Установите и запустите контейнер с сервером документов:

```bash
sudo
docker
run
--net
onlyoffice
-i
-t
-d
--restart
=
always
--name
onlyoffice-document-server
\
-v
/app/onlyoffice/DocumentServer/logs:/var/log/onlyoffice
\
-v
/app/onlyoffice/DocumentServer/data:/var/www/onlyoffice/Data
\
-v
/app/onlyoffice/DocumentServer/lib:/var/lib/onlyoffice
\
-v
/app/onlyoffice/DocumentServer/db:/var/lib/postgresql
\
onlyoffice/documentserver
```

Установите и запустите контейнер с сервером совместной работы:

```bash
sudo
docker
run
--net
onlyoffice
-i
-t
-d
--restart
=
always
--name
onlyoffice-community-server
-p
80
:80
-p
443
:443
-p
5222
:5222
\
-e
MYSQL_SERVER_ROOT_PASSWORD
=
my-secret-pw
\
-e
MYSQL_SERVER_DB_NAME
=
onlyoffice
\
-e
MYSQL_SERVER_HOST
=
onlyoffice-mysql-server
\
-e
MYSQL_SERVER_USER
=
onlyoffice_user
\
-e
MYSQL_SERVER_PASS
=
onlyoffice_pass
\
-e
DOCUMENT_SERVER_PORT_80_TCP_ADDR
=
onlyoffice-document-server
\
-v
/app/onlyoffice/CommunityServer/data:/var/www/onlyoffice/Data
\
-v
/app/onlyoffice/CommunityServer/logs:/var/log/onlyoffice
\
onlyoffice/communityserver
```

## 5. Запустите и настройте Onlyoffice

1. В браузере перейдите на страницу https://<IP-адрес_сервера>:4443. Дождитесь окончания загрузки:

 
 Если загрузка не завершается 
 
Откроется окно с настройками Onlyoffice:
2. В блоке Password введите пароль.
3. В поле Language выберите язык.
4. В поле Time Zone выберите часовой пояс.
5. Нажмите Continue.

В браузере перейдите на страницу https://<IP-адрес_сервера>:4443. Дождитесь окончания загрузки:

![../_images/onlyoffice_loading.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/onlyoffice_loading.webp)

Откроется окно с настройками Onlyoffice:

![../_images/onlyoffice_setup.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/onlyoffice_setup.webp)

В блоке Password введите пароль.

В поле Language выберите язык.

В поле Time Zone выберите часовой пояс.

Нажмите Continue.

Вы попадете в главное меню Onlyoffice, из которого можно настроить все необходимые компоненты для совместной работы.
Установка и настройка завершена.
