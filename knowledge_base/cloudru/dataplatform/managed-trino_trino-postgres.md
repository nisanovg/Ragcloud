---
title: Подключение Trino к PostgreSQL®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__trino-postgres
topic: dataplatform
---
# Подключение Trino к PostgreSQL®

С помощью этого руководства вы выполните:

- подключение инстанса Managed Trino к [PostgreSQL®](https://cloud.ru/docs/paas-postgresql/ug/index)PostgreSQL®;
- отправку запроса через популярный JDBC-клиент DBeaver;
- создание, заполнение таблиц и объединение данных из двух таблиц через SQL-запрос.

подключение инстанса Managed Trino к [PostgreSQL®](https://cloud.ru/docs/paas-postgresql/ug/index)PostgreSQL®;

отправку запроса через популярный JDBC-клиент DBeaver;

создание, заполнение таблиц и объединение данных из двух таблиц через SQL-запрос.

Все сущности должны располагаться в одной

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. (Опционально) [Cоздайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Cоздайте публичный SNAT-шлюз, если необходим доступ в интернет.
3. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
Назовите кластер «dp-labs».
5. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
6. Установите JDBC-клиент DBeaver.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

(Опционально) [Cоздайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Cоздайте публичный SNAT-шлюз, если необходим доступ в интернет.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

Назовите кластер «dp-labs».

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Установите JDBC-клиент DBeaver.

## Создайте базу данных Managed PostgreSQL®

1. Откройте сервис Managed PostgreSQL®, в правом верхнем углу нажмите Создать кластер.
2. Создайте две базы данных, следуя шагам, описанным в документации [Managed PostgreSQL®](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL®.
Задайте следующие названия:

Названия кластеров DBaaS-PG-1 и DBaaS-PG-2.
Названия баз данных dbaas_pg_1 и dbaas_pg_2.
3. Дождитесь, когда статус обоих кластеров изменится на «Доступен».
4. Откройте карточки созданных кластеров PostgreSQL®.
Информация из них понадобится на следующих этапах.

Откройте сервис Managed PostgreSQL®, в правом верхнем углу нажмите Создать кластер.

Создайте две базы данных, следуя шагам, описанным в документации [Managed PostgreSQL®](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL®.

Задайте следующие названия:

- Названия кластеров DBaaS-PG-1 и DBaaS-PG-2.
- Названия баз данных dbaas_pg_1 и dbaas_pg_2.

Названия кластеров DBaaS-PG-1 и DBaaS-PG-2.

Названия баз данных dbaas_pg_1 и dbaas_pg_2.

Дождитесь, когда статус обоих кластеров изменится на «Доступен».

Откройте карточки созданных кластеров PostgreSQL®.
Информация из них понадобится на следующих этапах.

## Создайте каталог

1. Откройте сервис Managed Trino.
2. Откройте раздел Каталоги.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:

Название — postgres_1.
Коннектор — PostgreSQL.
Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-1.
Порт — порт, указанный в карточке кластера DBaaS-PG-1.
Название базы данных — dbaas_pg_1.
Логин — логин, указанный в карточке кластера DBaaS-PG-1.
Пароль — секретный ключ сервиса [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Management.
Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.
5. Нажмите Создать.
6. Создайте второй каталог и заполните поля следующими значениями:

Название — postgres_2.
Коннектор — PostgreSQL.
Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-2.
Порт — порт, указанный в карточке кластера DBaaS-PG-2.
Название базы данных — dbaas_pg_2.
Логин — логин, указанный в карточке кластера DBaaS-PG-2.
Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.
7. Нажмите Создать.

Откройте сервис Managed Trino.

Откройте раздел Каталоги.

Нажмите Создать каталог.

Заполните поля следующими значениями:

- Название — postgres_1.
- Коннектор — PostgreSQL.
- Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-1.
- Порт — порт, указанный в карточке кластера DBaaS-PG-1.
- Название базы данных — dbaas_pg_1.
- Логин — логин, указанный в карточке кластера DBaaS-PG-1.
- Пароль — секретный ключ сервиса [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Management.
Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.

Название — postgres_1.

Коннектор — PostgreSQL.

Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-1.

Порт — порт, указанный в карточке кластера DBaaS-PG-1.

Название базы данных — dbaas_pg_1.

Логин — логин, указанный в карточке кластера DBaaS-PG-1.

Пароль — секретный ключ сервиса [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides_secret)Secret Management.

Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.

![../_images/trino__connection-creation-postgresql.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/trino__connection-creation-postgresql.png)

Нажмите Создать.

Создайте второй каталог и заполните поля следующими значениями:

- Название — postgres_2.
- Коннектор — PostgreSQL.
- Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-2.
- Порт — порт, указанный в карточке кластера DBaaS-PG-2.
- Название базы данных — dbaas_pg_2.
- Логин — логин, указанный в карточке кластера DBaaS-PG-2.
- Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.

Название — postgres_2.

Коннектор — PostgreSQL.

Хост — внутренний IP, указанный в карточке кластера DBaaS-PG-2.

Порт — порт, указанный в карточке кластера DBaaS-PG-2.

Название базы данных — dbaas_pg_2.

Логин — логин, указанный в карточке кластера DBaaS-PG-2.

Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Если нужного секрета нет, [создайте новый](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)создайте новый, нажав Создать новый секрет.

Нажмите Создать.

На странице Managed Trino на вкладке Каталоги появится две записи с названиями «postgres_1» и «postgres_2».

![../_images/trino__connection-ready-postgres.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/trino__connection-ready-postgres.png)

## Создайте инстанс Managed Trino

1. Откройте сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля:

Название — trino-instance-lab-1.
Кластер — db-labs.
Вычислительные ресурсы — vCPU 4, RAM 16.
Количество node — 3.
5. Нажмите Продолжить.
6. На шаге Каталоги выберите каталоги postgres_1 и postgres_2.
7. Нажмите Продолжить.
8. В блоке Сетевые настройки заполните поля:

Зона доступности — выберите [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
В этой подсети должен располагаться инстанс Managed Metastore.
Подключить публичный хост — активируйте опцию.
Пользователь — введите имя пользователя.
Пароль — выберите [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
9. Нажмите Создать.
10. Дождитесь, когда статус инстанса изменится на «Готов».
11. Откройте карточку инстанса Managed Trino.
Информация из него понадобится на следующих этапах.

Откройте сервис Managed Trino.

Откройте раздел Инстансы.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля:

- Название — trino-instance-lab-1.
- Кластер — db-labs.
- Вычислительные ресурсы — vCPU 4, RAM 16.
- Количество node — 3.

Название — trino-instance-lab-1.

Кластер — db-labs.

Вычислительные ресурсы — vCPU 4, RAM 16.

Количество node — 3.

Нажмите Продолжить.

На шаге Каталоги выберите каталоги postgres_1 и postgres_2.

Нажмите Продолжить.

В блоке Сетевые настройки заполните поля:

- Зона доступности — выберите [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
В этой подсети должен располагаться инстанс Managed Metastore.
- Подключить публичный хост — активируйте опцию.
- Пользователь — введите имя пользователя.
- Пароль — выберите [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Зона доступности — выберите

Подсеть — выберите подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
В этой подсети должен располагаться инстанс Managed Metastore.

Подключить публичный хост — активируйте опцию.

Пользователь — введите имя пользователя.

Пароль — выберите [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Нажмите Создать.

Дождитесь, когда статус инстанса изменится на «Готов».

Откройте карточку инстанса Managed Trino.
Информация из него понадобится на следующих этапах.

![../_images/trino__instance-ready-postgres.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/trino__instance-ready-postgres.png)

## Подключите Managed Trino к DBeaver

### Добавьте сертификат в Java KeyStore

1. Запустите терминал и перейдите в директорию, где хотите сохранить JKS-файл.
2. Введите команду:
keytool -importcert -alias cloudru-root -file <PATH>/dp-cert.crt -keystore <PATH>/cloudru-truststore.jks -storetype JKS -storepass <YOUR-PASSWORD> -noprompt

В строке -file вместо <PATH> укажите путь до скачанного ранее root-сертификата.
В строке -keystore вместо <PATH> укажите путь до места, где будет храниться JKS-файл.
Сохраните путь.
Он понадобится при добавлении JKS-файла в DBeaver.

В строке -storepass вместо <YOUR-PASSWORD> задайте пароль для сертификата.
Сохраните пароль.
Он понадобится при добавлении JKS-файла в DBeaver.

Запустите терминал и перейдите в директорию, где хотите сохранить JKS-файл.

Введите команду:

```bash
keytool
-importcert
-alias
cloudru-root
-file
<
PATH
>
/dp-cert.crt
-keystore
<
PATH
>
/cloudru-truststore.jks
-storetype
JKS
-storepass
<
YOUR-PASSWORD
>
-noprompt
```

- В строке -file вместо <PATH> укажите путь до скачанного ранее root-сертификата.
- В строке -keystore вместо <PATH> укажите путь до места, где будет храниться JKS-файл.
Сохраните путь.
Он понадобится при добавлении JKS-файла в DBeaver.
- В строке -storepass вместо <YOUR-PASSWORD> задайте пароль для сертификата.
Сохраните пароль.
Он понадобится при добавлении JKS-файла в DBeaver.

В строке -file вместо <PATH> укажите путь до скачанного ранее root-сертификата.

В строке -keystore вместо <PATH> укажите путь до места, где будет храниться JKS-файл.

Сохраните путь.
Он понадобится при добавлении JKS-файла в DBeaver.

В строке -storepass вместо <YOUR-PASSWORD> задайте пароль для сертификата.

Сохраните пароль.
Он понадобится при добавлении JKS-файла в DBeaver.

### Подключите DBeaver

1. Откройте приложение DBeaver.
2. В панели сверху нажмите База данных → Новое соединение.
3. В списке соединений выберите Trino.
4. Нажмите Далее заполните поля на вкладке Главное:

Хост — публичный хост, указанный в карточке инстанса.
Порт — порт, указанный в карточке инстанса.
Пользователь — пользователь, указанный в карточке инстанса.
Пароль — пароль, указанный в карточке инстанса.
5. На вкладке Свойства драйвера измените значение свойства SSL на true.
6. Нажмите Тест соединения.
7. Нажмите Готово.

Откройте приложение DBeaver.

В панели сверху нажмите База данных → Новое соединение.

В списке соединений выберите Trino.

Нажмите Далее заполните поля на вкладке Главное:

- Хост — публичный хост, указанный в карточке инстанса.
- Порт — порт, указанный в карточке инстанса.
- Пользователь — пользователь, указанный в карточке инстанса.
- Пароль — пароль, указанный в карточке инстанса.

Хост — публичный хост, указанный в карточке инстанса.

Порт — порт, указанный в карточке инстанса.

Пользователь — пользователь, указанный в карточке инстанса.

Пароль — пароль, указанный в карточке инстанса.

![../_images/dbeaver__connection-1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-1.png)

На вкладке Свойства драйвера измените значение свойства SSL на true.

![../_images/dbeaver__connection-2.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-2.png)

Нажмите Тест соединения.

Нажмите Готово.

Слева в списке объектов появится две базы данных PostgreSQL® с названиями «postgres_1» и «postgres_2».

![../_images/dbeaver__connection-ready-1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-ready-1.png)

## Отправьте SQL-запрос

1. Создайте схемы.

Для первой БД dbaas_pg_1:
CREATE SCHEMA IF NOT EXISTS postgres_1.lab

Для второй БД dbaas_pg_2:
CREATE SCHEMA IF NOT EXISTS postgres_2.lab
2. Создайте таблицы в базах данных.

Для первой БД dbaas_pg_1:
CREATE TABLE IF NOT EXISTS postgres_1.lab.brand (id INT, name VARCHAR(255))

Для второй БД dbaas_pg_2:
CREATE TABLE IF NOT EXISTS postgres_2.lab.car (id INT, name VARCHAR(255), brand_id INT)
3. Заполните таблицы.

Для первой БД dbaas_pg_1:
INSERT INTO postgres_1.lab.brand values (1, 'Mazda'), (2, 'BMW'), (3, 'Kia')

Для второй БД dbaas_pg_2:
INSERT INTO postgres_2.lab.car values (1, 'CX-5', 1), (2, 'CX-9', 1), (3, 'Rio', 3), (4, 'X3', 2), (5, 'X5', 2)
4. Объедините таблицу с брендами в первой БД dbaas_pg_1 с названиями авто во второй БД dbaas_pg_2.
select c.name as car, b.name as brandfrom postgres_2.lab.car cleft join postgres_1.lab.brand bon c.brand_id = b.id

Создайте схемы.

- Для первой БД dbaas_pg_1:
CREATE SCHEMA IF NOT EXISTS postgres_1.lab
- Для второй БД dbaas_pg_2:
CREATE SCHEMA IF NOT EXISTS postgres_2.lab

Для первой БД dbaas_pg_1:

```bash
CREATE SCHEMA IF NOT EXISTS postgres_1.lab
```

Для второй БД dbaas_pg_2:

```bash
CREATE SCHEMA IF NOT EXISTS postgres_2.lab
```

Создайте таблицы в базах данных.

- Для первой БД dbaas_pg_1:
CREATE TABLE IF NOT EXISTS postgres_1.lab.brand (id INT, name VARCHAR(255))
- Для второй БД dbaas_pg_2:
CREATE TABLE IF NOT EXISTS postgres_2.lab.car (id INT, name VARCHAR(255), brand_id INT)

Для первой БД dbaas_pg_1:

```bash
CREATE TABLE IF NOT EXISTS postgres_1.lab.brand
(
id INT, name VARCHAR
(
255
))
```

Для второй БД dbaas_pg_2:

```bash
CREATE TABLE IF NOT EXISTS postgres_2.lab.car
(
id INT, name VARCHAR
(
255
)
, brand_id INT
)
```

Заполните таблицы.

- Для первой БД dbaas_pg_1:
INSERT INTO postgres_1.lab.brand values (1, 'Mazda'), (2, 'BMW'), (3, 'Kia')
- Для второй БД dbaas_pg_2:
INSERT INTO postgres_2.lab.car values (1, 'CX-5', 1), (2, 'CX-9', 1), (3, 'Rio', 3), (4, 'X3', 2), (5, 'X5', 2)

Для первой БД dbaas_pg_1:

```bash
INSERT INTO postgres_1.lab.brand values
(
1
,
'Mazda'
)
,
(
2
,
'BMW'
)
,
(
3
,
'Kia'
)
```

Для второй БД dbaas_pg_2:

```bash
INSERT INTO postgres_2.lab.car values
(
1
,
'CX-5'
,
1
)
,
(
2
,
'CX-9'
,
1
)
,
(
3
,
'Rio'
,
3
)
,
(
4
,
'X3'
,
2
)
,
(
5
,
'X5'
,
2
)
```

Объедините таблицу с брендами в первой БД dbaas_pg_1 с названиями авто во второй БД dbaas_pg_2.

```bash
select
c.name as car, b.name as brand
from postgres_2.lab.car c
left
join
postgres_1.lab.brand b
on c.brand_id
=
b.id
```

![../_images/dbeaver__request-result.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__request-result.png)
