---
title: Миграция PostgreSQL с помощью Trino
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__migration-postgresql
topic: dataplatform
---
# Миграция PostgreSQL с помощью Trino

С помощью этого руководства вы выполните миграцию таблиц между двумя источниками PostgreSQL с помощью Trino.

## Постановка задачи

1. Создать таблицу-источник и целевую таблицу.
2. Перенести данные в целевую таблицу с помощью:

JDBC-клиента (DBeaver);
Python-скрипта.

Создать таблицу-источник и целевую таблицу.

Перенести данные в целевую таблицу с помощью:

- JDBC-клиента (DBeaver);
- Python-скрипта.

JDBC-клиента (DBeaver);

Python-скрипта.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
3. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
Назовите кластер «dp-labs».
4. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
5. Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

Назовите кластер «dp-labs».

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

Все сущности должны располагаться в одной

## Подготовка инфраструктуры

Подготовьте базу данных и таблицы, которые будете переносить, а также каталоги и инстанс Trino.

### Создайте Managed PostgreSQL®

1. [Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL.
2. [Создайте две базы данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте две базы данных с названиями:

pg_1 — это исходная база данных, которая содержит таблицы для миграции;
pg_2 — это целевая база данных, куда нужно перенести таблицы из pg_1.
3. Сохраните пароль из карточки кластера в сервисе [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager.

[Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL.

[Создайте две базы данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте две базы данных с названиями:

- pg_1 — это исходная база данных, которая содержит таблицы для миграции;
- pg_2 — это целевая база данных, куда нужно перенести таблицы из pg_1.

pg_1 — это исходная база данных, которая содержит таблицы для миграции;

pg_2 — это целевая база данных, куда нужно перенести таблицы из pg_1.

Сохраните пароль из карточки кластера в сервисе [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager.

### Создайте каталог Managed Trino

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Каталоги.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:

Название:

pg_1 — для исходной базы данных pg_1;
pg_2 — для целевой базы данных pg_2.

Коннектор — PostgreSQL.
Хост — внутренний IP, указанный в карточке кластера Managed PostgreSQL®.
Порт — порт, указанный в карточке кластера Managed PostgreSQL®.
Название базы данных:

pg_1
pg_2

Логин — логин, указанный в карточке кластера Managed PostgreSQL®.
Пароль — выберите секрет с паролем кластера Managed PostgreSQL®.
5. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed Trino.

Откройте раздел Каталоги.

Нажмите Создать каталог.

Заполните поля следующими значениями:

- Название:

pg_1 — для исходной базы данных pg_1;
pg_2 — для целевой базы данных pg_2.
- Коннектор — PostgreSQL.
- Хост — внутренний IP, указанный в карточке кластера Managed PostgreSQL®.
- Порт — порт, указанный в карточке кластера Managed PostgreSQL®.
- Название базы данных:

pg_1
pg_2
- Логин — логин, указанный в карточке кластера Managed PostgreSQL®.
- Пароль — выберите секрет с паролем кластера Managed PostgreSQL®.

Название:

- pg_1 — для исходной базы данных pg_1;
- pg_2 — для целевой базы данных pg_2.

pg_1 — для исходной базы данных pg_1;

pg_2 — для целевой базы данных pg_2.

Коннектор — PostgreSQL.

Хост — внутренний IP, указанный в карточке кластера Managed PostgreSQL®.

Порт — порт, указанный в карточке кластера Managed PostgreSQL®.

Название базы данных:

- pg_1
- pg_2

pg_1

pg_2

Логин — логин, указанный в карточке кластера Managed PostgreSQL®.

Пароль — выберите секрет с паролем кластера Managed PostgreSQL®.

Нажмите Создать.

### Создайте инстанс Managed Trino

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля:

Название — trino-instance-migration.
Кластер — db-labs.
Вычислительные ресурсы — vCPU 4, RAM 16.
Количество node — 3.
5. Нажмите Продолжить.
6. На шаге Каталоги выберите каталоги «pg_1» и «pg_2».
7. Нажмите Продолжить.
8. В блоке Сетевые настройки заполните поля:

Зона доступности — выберите [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
Подключить публичный хост — активируйте опцию.
Пользователь — задайте имя пользователя для доступа к Trino.
Пароль — создайте пароль в сервисе [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Manager, нажав Создать секрет, и выберите его.
9. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed Trino.

Откройте раздел Инстансы.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля:

- Название — trino-instance-migration.
- Кластер — db-labs.
- Вычислительные ресурсы — vCPU 4, RAM 16.
- Количество node — 3.

Название — trino-instance-migration.

Кластер — db-labs.

Вычислительные ресурсы — vCPU 4, RAM 16.

Количество node — 3.

Нажмите Продолжить.

На шаге Каталоги выберите каталоги «pg_1» и «pg_2».

Нажмите Продолжить.

В блоке Сетевые настройки заполните поля:

- Зона доступности — выберите [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
- Подключить публичный хост — активируйте опцию.
- Пользователь — задайте имя пользователя для доступа к Trino.
- Пароль — создайте пароль в сервисе [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Manager, нажав Создать секрет, и выберите его.

Зона доступности — выберите

Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Подключить публичный хост — активируйте опцию.

Пользователь — задайте имя пользователя для доступа к Trino.

Пароль — создайте пароль в сервисе [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Manager, нажав Создать секрет, и выберите его.

Нажмите Создать.

### Создайте структуру данных

Выполните команды:

```bash
CREATE SCHEMA IF NOT EXISTS pg_1.lab_migration
;
CREATE TABLE IF NOT EXISTS pg_1.lab_migration.users
(
id_user INT, email VARCHAR
(
255
))
;
INSERT INTO pg_1.lab_migration.users values
(
1
,
'one@example.com'
)
,
(
2
,
'two@example.com'
)
,
(
3
,
'three@example.com'
)
;
```

## Миграция

Рассмотрим два способа миграции таблиц c помощью:

- [JDBC-клиента DBeaver](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__migration-postgresql)JDBC-клиента DBeaver;
- [Python-скрипта](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__migration-postgresql)Python-скрипта.

[JDBC-клиента DBeaver](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__migration-postgresql)JDBC-клиента DBeaver;

[Python-скрипта](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__migration-postgresql)Python-скрипта.

### С помощью DBeaver

1. [Подключите инстанс к DBeaver](https://cloud.ru/docs/trino/ug/topics/guides__instance-jdbc)Подключите инстанс к DBeaver.
2. Чтобы подготовить данные, в DBeaver выполните SQL-запросы:
CREATE SCHEMA IF NOT EXISTS pg_1.lab_migration;
CREATE TABLE IF NOT EXISTS pg_1.lab_migration.users (id_user INT, email VARCHAR(255));
INSERT INTO pg_1.lab_migration.users values (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com');

Можете создать дополнительные таблицы с данными в схеме «lab_migration» в базе данных «pg_1».
3. Выполните:
Миграция таблицы с даннымиМиграция таблицы без данных (только структура)CREATE TABLE pg_2.lab_migration.users ASSELECT * FROM pg_1.lab_migration.users;
4. Автоматизируйте миграцию таблиц.

Чтобы сгенерировать SQL-запросы для каждой таблицы, выполните:
SELECT 'CREATE TABLE pg_2.lab_migration.' || table_name || ' AS SELECT * FROM pg_1.lab_migration.' || table_name || ';'FROM pg_1.information_schema.tablesWHERE table_schema = 'lab_migration';

Скопируйте полученные строки.
Выполните их по очереди.

[Подключите инстанс к DBeaver](https://cloud.ru/docs/trino/ug/topics/guides__instance-jdbc)Подключите инстанс к DBeaver.

Чтобы подготовить данные, в DBeaver выполните SQL-запросы:

```bash
CREATE SCHEMA IF NOT EXISTS pg_1.lab_migration
;
CREATE TABLE IF NOT EXISTS pg_1.lab_migration.users
(
id_user INT, email VARCHAR
(
255
))
;
INSERT INTO pg_1.lab_migration.users values
(
1
,
'xxx@example.com'
)
,
(
2
,
'yyy@example.com'
)
,
(
3
,
'zzz@example.com'
)
;
```

Можете создать дополнительные таблицы с данными в схеме «lab_migration» в базе данных «pg_1».

Выполните:

```bash
CREATE TABLE pg_2.lab_migration.users AS
SELECT * FROM pg_1.lab_migration.users
;
```

Автоматизируйте миграцию таблиц.

1. Чтобы сгенерировать SQL-запросы для каждой таблицы, выполните:
SELECT 'CREATE TABLE pg_2.lab_migration.' || table_name || ' AS SELECT * FROM pg_1.lab_migration.' || table_name || ';'FROM pg_1.information_schema.tablesWHERE table_schema = 'lab_migration';
2. Скопируйте полученные строки.
3. Выполните их по очереди.

Чтобы сгенерировать SQL-запросы для каждой таблицы, выполните:

```bash
SELECT
'CREATE TABLE pg_2.lab_migration.'
||
table_name
||
' AS SELECT * FROM pg_1.lab_migration.'
||
table_name
||
';'
FROM pg_1.information_schema.tables
WHERE table_schema
=
'lab_migration'
;
```

Скопируйте полученные строки.

Выполните их по очереди.

### С помощью скрипта

1. В командной строке выполните:
python3 -m venv venvsource venv/bin/activatepip install trino
2. Скопируйте скрипт, введите необходимые значения и сохраните файл с названием trino_pg_migration.py:
 
 Скрипт Python
3. Запустите скрипт:
python trino_pg_migration.py

В командной строке выполните:

```bash
python3
-m
venv venv
source
venv/bin/activate
pip
install
trino
```

Скопируйте скрипт, введите необходимые значения и сохраните файл с названием trino_pg_migration.py:

Запустите скрипт:

```bash
python trino_pg_migration.py
```

## Проверка результата

В DBeaver выполните следующие запросы:

- Чтобы проверить, что таблицы созданы:
SHOW TABLES IN pg_2.lab_migration;
- Чтобы проверить количество строк в каждой таблице:
SELECT COUNT(*) FROM pg_2.lab_migration.users;SELECT COUNT(*) FROM pg_2.lab_migration.products;SELECT COUNT(*) FROM pg_2.lab_migration.orders;
- Чтобы проверить содержимое (первые 10 строк):
SELECT * FROM pg_2.lab_migration.users LIMIT 10;SELECT * FROM pg_2.lab_migration.products LIMIT 10;SELECT * FROM pg_2.lab_migration.orders LIMIT 10;

Чтобы проверить, что таблицы созданы:

```bash
SHOW TABLES IN pg_2.lab_migration
;
```

Чтобы проверить количество строк в каждой таблице:

```bash
SELECT COUNT
(
*
)
FROM pg_2.lab_migration.users
;
SELECT COUNT
(
*
)
FROM pg_2.lab_migration.products
;
SELECT COUNT
(
*
)
FROM pg_2.lab_migration.orders
;
```

Чтобы проверить содержимое (первые 10 строк):

```bash
SELECT * FROM pg_2.lab_migration.users LIMIT
10
;
SELECT * FROM pg_2.lab_migration.products LIMIT
10
;
SELECT * FROM pg_2.lab_migration.orders LIMIT
10
;
```
