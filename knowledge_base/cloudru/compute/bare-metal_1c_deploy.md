---
title: Развертывание 1С на сервере Bare Metal
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy
topic: compute
---
# Развертывание 1С на сервере Bare Metal

С помощью этого руководства вы развернете и настроите программу «1С: Предприятие» на сервере Bare Metal с ОС Ubuntu 22.04.
Для управления базой данных используем СУБД PostgreSQL.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Разверните инфраструктуру.
2. [Установите кластер 1С](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Установите кластер 1С.
3. [Настройте PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Настройте PostgreSQL.
4. [Запустите и настройте сервер 1С](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Запустите и настройте сервер 1С.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Разверните инфраструктуру.

[Установите кластер 1С](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Установите кластер 1С.

[Настройте PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Настройте PostgreSQL.

[Запустите и настройте сервер 1С](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__1c_deploy)Запустите и настройте сервер 1С.

## 1. Разверните инфраструктуру

1. [Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
Для корректной работы 1С выбирайте конфигурации с:

количеством CPU от 4;
объемом оперативной памяти не менее 16 ГБ;
объемом дискового пространства от 150 ГБ.
2. [Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.
3. Установите дополнительные пакеты для работы:
sudo apt updatesudo apt install -y wget curl unzip nano htop
4. Установите зависимости для работы с 1С:
sudo apt install -y libstdc++6 libgtk2.0-0 libxslt1.1 libcanberra-gtk-module
5. Установите PostgreSQL:
sudo apt install -y postgresql postgresql-contrib

[Подробнее об установке PostgeSQL](https://cloud.ru/docs/bare-metal-evolution/ug/topics/use-cases__postgre_deploy)Подробнее об установке PostgeSQL.

[Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
Для корректной работы 1С выбирайте конфигурации с:

- количеством CPU от 4;
- объемом оперативной памяти не менее 16 ГБ;
- объемом дискового пространства от 150 ГБ.

количеством CPU от 4;

объемом оперативной памяти не менее 16 ГБ;

объемом дискового пространства от 150 ГБ.

[Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

Установите дополнительные пакеты для работы:

```bash
sudo
apt
update
sudo
apt
install
-y
wget
curl
unzip
nano
htop
```

Установите зависимости для работы с 1С:

```bash
sudo
apt
install
-y
libstdc++6 libgtk2.0-0 libxslt1.1 libcanberra-gtk-module
```

Установите PostgreSQL:

```bash
sudo
apt
install
-y
postgresql postgresql-contrib
```

[Подробнее об установке PostgeSQL](https://cloud.ru/docs/bare-metal-evolution/ug/topics/use-cases__postgre_deploy)Подробнее об установке PostgeSQL.

## 2. Установите кластер 1С

1. [Скачайте](https://releases.1c.ru/)Скачайте дистрибутив 1С с официального сайта.
2. Установите дистрибутив:
sudo dpkg -i 1C_Enterprise_*.debsudo apt --fix-broken install
3. Проверьте установку:
rac cluster list

В результате должны отобразиться параметры кластера 1С.

[Скачайте](https://releases.1c.ru/)Скачайте дистрибутив 1С с официального сайта.

Установите дистрибутив:

```bash
sudo
dpkg
-i
1C_Enterprise_*.deb
sudo
apt
--fix-broken
install
```

Проверьте установку:

```bash
rac cluster list
```

В результате должны отобразиться параметры кластера 1С.

## 3. Настройте PostgreSQL

1. Войдите в консоль PostgreSQL:
sudo -u postgres psql
2. Создайте базу данных и пользователя для нее:
CREATE USER <user_name> WITH PASSWORD '<password>';CREATE DATABASE <db_name> OWNER <user_name>;\q

Где:

<user_name> — имя пользователя БД.
<password> — пароль пользователя БД.
<db_name> — название БД.
3. Откройте файл с конфигурацией аутентификации пользователей:
sudo nano /etc/postgresql/<postrgesql_version>/main/pg_hba.conf
4. Добавьте в конец файла строку:
host all all 0.0.0.0/0 md5
5. Перезагрузите PostgreSQL:
sudo systemctl restart postgresql
6. Проверьте работу PostgreSQL:
sudo systemctl status postgresql

Войдите в консоль PostgreSQL:

```bash
sudo
-u
postgres psql
```

Создайте базу данных и пользователя для нее:

```bash
CREATE
USER
<
user_name
>
WITH PASSWORD
'<password>'
;
CREATE DATABASE
<
db_name
>
OWNER
<
user_name
>
;
\
q
```

Где:

- <user_name> — имя пользователя БД.
- <password> — пароль пользователя БД.
- <db_name> — название БД.

<user_name> — имя пользователя БД.

<password> — пароль пользователя БД.

<db_name> — название БД.

Откройте файл с конфигурацией аутентификации пользователей:

```bash
sudo
nano
/etc/postgresql/
<
postrgesql_version
>
/main/pg_hba.conf
```

Добавьте в конец файла строку:

```bash
host
all all
0.0
.0.0/0 md5
```

Перезагрузите PostgreSQL:

```bash
sudo
systemctl restart postgresql
```

Проверьте работу PostgreSQL:

```bash
sudo
systemctl status postgresql
```

## 4. Запустите и настройте сервер 1С

1. Запустите службу сервера 1С и проверьте его статус:
sudo systemctl start srv1cv83sudo systemctl enable srv1cv83sudo systemctl status srv1cv83
2. Получите информацию о кластере:
rac cluster list

Результат:
cluster : <1C_cluster_UUID>host : baremetal-1cport : 1541name : "Локальный кластер"expiration-timeout : 60lifetime-limit : 0max-memory-size : 0max-memory-time-limit : 0security-level : 0

Где <1C_cluster_UUID> — идентификатор кластера 1С.
3. Создайте информационную базу:
rac infobase create --cluster=<1C_cluster_UUID> \ --create-database \ --name=db1c \ --descr=BaseForBareMetal \ --dbms=PostgreSQL \ --db-server=baremetal-1c \ --db-name=db1c --locale=ru \ --db-user=usr1c --db-pwd='password' \ --license-distribution=allow --scheduled-jobs-deny=on
4. Проверьте создание информационной базы:
rac infobase --cluster=<1C_cluster_UUID> summary list
5. Настройте UFW для ограничения доступа к серверу:
sudo ufw allow sshsudo ufw allow 1540-1560/tcpsudo ufw enable
6. Настройте регулярное резервное копирование баз данных:
pg_dump -U usr1c -d db1c > backup.sql

Запустите службу сервера 1С и проверьте его статус:

```bash
sudo
systemctl start srv1cv83
sudo
systemctl
enable
srv1cv83
sudo
systemctl status srv1cv83
```

Получите информацию о кластере:

```bash
rac cluster list
```

Результат:

```bash
cluster
:
<
1C_cluster_UUID
>
host
:
baremetal-1c
port
:
1541
name
:
"Локальный кластер"
expiration-timeout
:
60
lifetime-limit
:
0
max-memory-size
:
0
max-memory-time-limit
:
0
security-level
:
0
```

Где <1C_cluster_UUID> — идентификатор кластера 1С.

Создайте информационную базу:

```bash
rac infobase create
--cluster
=
<
1C_cluster_UUID
>
\
--create-database
\
--name
=
db1c
\
--descr
=
BaseForBareMetal
\
--dbms
=
PostgreSQL
\
--db-server
=
baremetal-1c
\
--db-name
=
db1c
--locale
=
ru
\
--db-user
=
usr1c --db-pwd
=
'password'
\
--license-distribution
=
allow --scheduled-jobs-deny
=
on
```

Проверьте создание информационной базы:

```bash
rac infobase
--cluster
=
<
1C_cluster_UUID
>
summary list
```

Настройте UFW для ограничения доступа к серверу:

```bash
sudo
ufw allow
ssh
sudo
ufw allow
1540
-1560/tcp
sudo
ufw
enable
```

Настройте регулярное резервное копирование баз данных:

```bash
pg_dump
-U
usr1c
-d
db1c
>
backup.sql
```

Сервер 1С развернут и готов к работе.
