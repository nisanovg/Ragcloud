---
title: Резервное копирование и восстановление базы данных
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump
topic: database
---
# Резервное копирование и восстановление базы данных

С помощью этого руководства вы создадите

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Разверните необходимые ресурсы в облаке.
2. [Создайте дамп базы данных](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Создайте дамп базы данных.
3. [Восстановите базу данных из дампа](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Восстановите базу данных из дампа.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Разверните необходимые ресурсы в облаке.

[Создайте дамп базы данных](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Создайте дамп базы данных.

[Восстановите базу данных из дампа](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-postgresql__pg_dump)Восстановите базу данных из дампа.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте SSH-ключ и загрузите его в облачный каталог](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте SSH-ключ и загрузите его в облачный каталог.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте SSH-ключ и загрузите его в облачный каталог](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте SSH-ключ и загрузите его в облачный каталог.

## 1. Разверните необходимые ресурсы в облаке

1. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с ОС Ubuntu 24.04 в том же проекте, зоне доступности и подсети, где будет располагаться кластер Managed PostgreSQL®.
2. [Назначьте виртуальной машине публичный IP-адрес](https://cloud.ru/docs/virtual-machines/ug/topics/guides__bind-public-ip)Назначьте виртуальной машине публичный IP-адрес.
3. Убедитесь, что вы можете [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
4. [Создайте кластер](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте кластер.
5. [Подключитесь к базе данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__connecting-to-database)Подключитесь к базе данных.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с ОС Ubuntu 24.04 в том же проекте, зоне доступности и подсети, где будет располагаться кластер Managed PostgreSQL®.

[Назначьте виртуальной машине публичный IP-адрес](https://cloud.ru/docs/virtual-machines/ug/topics/guides__bind-public-ip)Назначьте виртуальной машине публичный IP-адрес.

Убедитесь, что вы можете [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.

[Создайте кластер](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте кластер.

[Подключитесь к базе данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__connecting-to-database)Подключитесь к базе данных.

## 2. Создайте дамп базы данных

Перенос пользователей через дамп базы данных невозможен.

Вы можете создать пользователей через [личный кабинет](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__users__creating-user)личный кабинет или API.
Не используйте имена dbadmin, postgres, cnpg__pooler__pgbouncer, streaming_replica, а также имена, начинающиеся на pg_, так как эти имена зарезервированы сервисом Managed PostgreSQL®.

Утилита [pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)pg_dump — встроенный инструмент для создания резервных копий в PostgreSQL®.

Используйте команду:

```bash
pg_dump
\
--dbname
=
<
database_name
>
\
--file
=
<
dump_file_path
>
\
--format
=
c
\
--inserts
\
--disable-triggers
\
--clean
\
--if-exists
\
--username
=
<
database_user_name
>
\
--host
=
<
database_host
>
\
--port
=
<
database_port
>
\
-O
\
-x
\
-v
```

Где:

- <database_name> — имя базы данных.
- <dump_file_path> — путь до файла дампа.
- <database_user_name> — имя пользователя базы данных.
- <database_host> — хост базы данных.
- <database_port> — порт базы данных.

<database_name> — имя базы данных.

<dump_file_path> — путь до файла дампа.

<database_user_name> — имя пользователя базы данных.

<database_host> — хост базы данных.

<database_port> — порт базы данных.

## 3. Восстановите базу данных из дампа

Утилита [pg_restore](https://www.postgresql.org/docs/13/app-pgrestore.html)pg_restore восстанавливает данные из резервных копий, которые были созданы с помощью pg_dump.

У пользователя dbadmin нет прав на CREATE DATABASE, поэтому восстановление можно выполнить только в существующую базу данных.
Вы можете создать базу данных через [личный кабинет](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)личный кабинет или API.

```bash
pg_restore
-O
-x
\
--dbname
=
<
database_name
>
\
--username
=
<
database_user_name
>
\
--host
=
<
database_host
>
\
--port
=
<
database_port
>
\
--disable-triggers
\
--clean
\
--if-exists
\
<
dump_file_path
>
\
-v
```

Где:

- <database_name> — имя базы данных.
- <database_user_name> — имя пользователя базы данных.
- <database_host> — хост базы данных.
- <database_port> — порт базы данных.
- <dump_file_path> — путь до файла дампа.

<database_name> — имя базы данных.

<database_user_name> — имя пользователя базы данных.

<database_host> — хост базы данных.

<database_port> — порт базы данных.

<dump_file_path> — путь до файла дампа.

## Результат

Вы создали дамп базы данных PostgreSQL® с помощью утилиты pg_dump, а затем восстановили базу с помощью pg_restore.
