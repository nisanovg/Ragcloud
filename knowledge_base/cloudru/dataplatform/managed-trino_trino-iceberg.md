---
title: Подключение Trino к Iceberg
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__trino-iceberg
topic: dataplatform
---
# Подключение Trino к Iceberg

С помощью этого руководства вы подготовите инстанс Trino для работы с форматом данных Iceberg.

## Постановка задачи

1. Создать и заполнить таблицу с данными сотрудников.
2. Прочитать данные таблицы в определенной точке времени, используя формат данных Iceberg.

Создать и заполнить таблицу с данными сотрудников.

Прочитать данные таблицы в определенной точке времени, используя формат данных Iceberg.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте публичный SNAT-шлюз, чтобы обеспечить инстансу доступ в интернет и связь с внешними источниками.
3. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.
4. [Создайте секреты](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секреты в сервисе Secret Management для доступа к Object Storage.
Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).
5. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
6. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
Назовите кластер «dp-labs».
7. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
8. Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте публичный SNAT-шлюз, чтобы обеспечить инстансу доступ в интернет и связь с внешними источниками.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.

[Создайте секреты](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секреты в сервисе Secret Management для доступа к Object Storage.
Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

Назовите кластер «dp-labs».

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

Все сущности должны располагаться в одной

## Создайте инстанс Managed Metastore

1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Нажмите Создать инстанс.
3. В блоке Общие параметры заполните поля следующими значениями:

Название — iceberg-metastore-lab.
Кластер — dp-labs.
Лог-группа — [группа](https://cloud.ru/docs/client-log/ug/topics/working-groups)группа, в которой будут храниться логи инстанса.
Файловая система — S3 и выберите Object Storage.
Бакет — созданный бакет Object Storage.
4. Нажмите Продолжить.
5. В блоке Сетевые настройки выберите:

Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
6. Нажмите Создать.
7. Дождитесь, когда статус инстанса изменится на «Готов».
8. Откройте карточку инстанса.
Информация об инстансе понадобится при создании каталога Trino.

Перейдите в раздел Evolution и выберите сервис Managed Metastore.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля следующими значениями:

- Название — iceberg-metastore-lab.
- Кластер — dp-labs.
- Лог-группа — [группа](https://cloud.ru/docs/client-log/ug/topics/working-groups)группа, в которой будут храниться логи инстанса.
- Файловая система — S3 и выберите Object Storage.
- Бакет — созданный бакет Object Storage.

Название — iceberg-metastore-lab.

Кластер — dp-labs.

Лог-группа — [группа](https://cloud.ru/docs/client-log/ug/topics/working-groups)группа, в которой будут храниться логи инстанса.

Файловая система — S3 и выберите Object Storage.

Бакет — созданный бакет Object Storage.

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Зона доступности —

Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Нажмите Создать.

Дождитесь, когда статус инстанса изменится на «Готов».

Откройте карточку инстанса.
Информация об инстансе понадобится при создании каталога Trino.

## Создайте каталог

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Каталог.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:

Название — metastore_iceberg_lab.
Коннектор — Iceberg.
Каталог — Metastore.
Thrift URL — Thrift URL, скопированный с карточки Metastore.
Эндпоинт — https://s3.cloud.ru.
Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.
Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.
Регион S3 — ru-central-1.
5. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed Trino.

Откройте раздел Каталог.

Нажмите Создать каталог.

Заполните поля следующими значениями:

- Название — metastore_iceberg_lab.
- Коннектор — Iceberg.
- Каталог — Metastore.
- Thrift URL — Thrift URL, скопированный с карточки Metastore.
- Эндпоинт — https://s3.cloud.ru.
- Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.
- Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.
- Регион S3 — ru-central-1.

Название — metastore_iceberg_lab.

Коннектор — Iceberg.

Каталог — Metastore.

Thrift URL — Thrift URL, скопированный с карточки Metastore.

Эндпоинт — https://s3.cloud.ru.

Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.

Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management.

Регион S3 — ru-central-1.

Нажмите Создать.

На странице Managed Trino в разделе Каталог появится запись с названием «metastore_iceberg_lab».

## Создайте инстанс Trino

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:

Название — trino-iceberg-lab.
Кластер — dp-labs.
Вычислительные ресурсы — vCPU 4, RAM 16.
Количество node — 3.
5. Нажмите Продолжить.
6. В блоке Каталог выберите каталог Metastore с названием «metastore_iceberg_lab».
7. Нажмите Продолжить.
8. В блоке Сетевые настройки выберите:

Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — подсеть, в которой расположен инстанс Managed Metastore.
Подключить публичный хост — активируйте опцию.
Пользователь — имя пользователя.
Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
9. Нажмите Создать.
10. Дождитесь, когда статус инстанса изменится на «Готов».
11. Откройте карточку инстанса Trino.
Информация из нее понадобится при подключении к DBeaver.

Перейдите в раздел Evolution и выберите сервис Managed Trino.

Откройте раздел Инстансы.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля следующими значениями:

- Название — trino-iceberg-lab.
- Кластер — dp-labs.
- Вычислительные ресурсы — vCPU 4, RAM 16.
- Количество node — 3.

Название — trino-iceberg-lab.

Кластер — dp-labs.

Вычислительные ресурсы — vCPU 4, RAM 16.

Количество node — 3.

Нажмите Продолжить.

В блоке Каталог выберите каталог Metastore с названием «metastore_iceberg_lab».

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — подсеть, в которой расположен инстанс Managed Metastore.
- Подключить публичный хост — активируйте опцию.
- Пользователь — имя пользователя.
- Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Зона доступности —

Подсеть — подсеть, в которой расположен инстанс Managed Metastore.

Подключить публичный хост — активируйте опцию.

Пользователь — имя пользователя.

Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Нажмите Создать.

Дождитесь, когда статус инстанса изменится на «Готов».

Откройте карточку инстанса Trino.
Информация из нее понадобится при подключении к DBeaver.

## Подключите Trino к DBeaver

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
4. Нажмите Далее и на вкладке Главное заполните поля информацией из карточки инстанса:

Хост
Порт
Пользователь
Пароль
5. На вкладке Свойства драйвера измените значение свойства SSL на true.
6. Нажмите Тест соединения.
7. Нажмите Готово.

Откройте приложение DBeaver.

В панели сверху нажмите База данных → Новое соединение.

В списке соединений выберите Trino.

Нажмите Далее и на вкладке Главное заполните поля информацией из карточки инстанса:

- Хост
- Порт
- Пользователь
- Пароль

Хост

Порт

Пользователь

Пароль

![../_images/dbeaver__connection-1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-1.png)

На вкладке Свойства драйвера измените значение свойства SSL на true.

![../_images/dbeaver__connection-2.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-2.png)

Нажмите Тест соединения.

Нажмите Готово.

Слева в списке объектов появится база данных Metastore с названием «iceberg-metastore-lab».

## Отправьте SQL-запросы

1. Запустите DBeaver.
2. Создайте новый редактор SQL и введите команду:
SHOW CATALOGS;

В списке должен появиться коннектор «metastore_iceberg_lab».
3. Создайте схему:
CREATE SCHEMA IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg;
4. Создайте таблицу в каталоге Iceberg:
CREATE TABLE IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg.employees( id_employee INT, email VARCHAR(255))WITH ( format = 'PARQUET'
);
5. Вставьте данные в таблицу:
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employeesvalues (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com');
6. Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:
SELECT *FROM metastore_iceberg_lab.my_company_iceberg.employees;
7. Вставьте данные в таблицу:
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employeesvalues (4, 'ttt@example.com'), (5, 'ggg@example.com'), (6, 'iii@example.com');
8. Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:
SELECT *FROM metastore_iceberg_lab.my_company_iceberg.employees;
9. Прочитайте историю таблицы:
SELECT *FROM metastore_iceberg_lab.my_company_iceberg."employees$history"ORDER BY made_current_at;

В результате выполнения запроса будет выведена история изменений таблицы, содержащая записи о создании таблицы и добавлении в нее новых строк.
10. Добавьте данные в таблицу:
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employeesvalues (7, 'qqq@example.com'), (8, 'www@example.com'), (9, 'eee@example.com');
11. Прочитайте данные из таблицы, чтобы проверить, что появилась еще одна запись:
SELECT *FROM metastore_iceberg_lab.my_company_iceberg."employees$history"ORDER BY made_current_at;
12. Чтобы понаблюдать, как таблица менялась со временем, прочитайте данные из таблицы, подставляя в запрос различные значения из столбца made_current_at.
SELECT *FROM metastore_iceberg_lab.my_company_iceberg.employeesFOR TIMESTAMP AS OF TIMESTAMP 'YYYY-MM-DD HH:MM:SS.000 +0300';

Где YYYY-MM-DD HH:MM:SS.000 — скопированное время создания таблицы.

Запустите DBeaver.

Создайте новый редактор SQL и введите команду:

```bash
SHOW CATALOGS
;
```

В списке должен появиться коннектор «metastore_iceberg_lab».

Создайте схему:

```bash
CREATE SCHEMA IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg
;
```

Создайте таблицу в каталоге Iceberg:

```bash
CREATE TABLE IF NOT EXISTS metastore_iceberg_lab.my_company_iceberg.employees
(
id_employee INT,
email VARCHAR
(
255
)
)
WITH
(
format
=
'PARQUET'
)
;
```

Вставьте данные в таблицу:

```bash
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values
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

Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:

```bash
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees
;
```

Вставьте данные в таблицу:

```bash
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values
(
4
,
'ttt@example.com'
)
,
(
5
,
'ggg@example.com'
)
,
(
6
,
'iii@example.com'
)
;
```

Прочитайте данные из таблицы, чтобы убедиться, что данные записаны:

```bash
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees
;
```

Прочитайте историю таблицы:

```bash
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.
"employees
$history
"
ORDER BY made_current_at
;
```

В результате выполнения запроса будет выведена история изменений таблицы, содержащая записи о создании таблицы и добавлении в нее новых строк.

Добавьте данные в таблицу:

```bash
INSERT INTO metastore_iceberg_lab.my_company_iceberg.employees
values
(
7
,
'qqq@example.com'
)
,
(
8
,
'www@example.com'
)
,
(
9
,
'eee@example.com'
)
;
```

Прочитайте данные из таблицы, чтобы проверить, что появилась еще одна запись:

```bash
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.
"employees
$history
"
ORDER BY made_current_at
;
```

Чтобы понаблюдать, как таблица менялась со временем, прочитайте данные из таблицы, подставляя в запрос различные значения из столбца made_current_at.

```bash
SELECT *
FROM metastore_iceberg_lab.my_company_iceberg.employees
FOR TIMESTAMP AS OF TIMESTAMP
'YYYY-MM-DD HH:MM:SS.000 +0300'
;
```

Где YYYY-MM-DD HH:MM:SS.000 — скопированное время создания таблицы.
