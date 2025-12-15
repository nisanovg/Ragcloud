---
title: Подключение Trino к S3
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-trino__trino-s3
topic: dataplatform
---
# Подключение Trino к S3

В этом руководстве мы рассмотрим:

- сценарий взаимодействия между Managed Trino, [Managed Metastore](https://cloud.ru/docs/metastore/ug/index)Managed Metastore и [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage;
- отправку запросов через DBeaver;
- работу с управляемыми таблицами;
- работу с внешними таблицами.

сценарий взаимодействия между Managed Trino, [Managed Metastore](https://cloud.ru/docs/metastore/ug/index)Managed Metastore и [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage;

отправку запросов через DBeaver;

работу с управляемыми таблицами;

работу с внешними таблицами.

Все сущности должны располагаться в одной

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Ознакомьтесь с разделом [Управляемые и внешние таблицы](https://cloud.ru/docs/trino/ug/topics/concepts__external-internal-tables)Управляемые и внешние таблицы.
В следующих блоках вам будут встречаться термины «Управляемые таблицы» и «Внешние таблицы».
3. (Опционально) [Cоздайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Cоздайте публичный SNAT-шлюз, если необходим доступ в интернет.
4. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.
5. [Создайте секреты](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секреты в сервисе Secret Management для доступа к Object Storage.
Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).
6. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
7. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
Назовите кластер «dp-labs».
8. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
9. Установите JDBC-клиент DBeaver.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Ознакомьтесь с разделом [Управляемые и внешние таблицы](https://cloud.ru/docs/trino/ug/topics/concepts__external-internal-tables)Управляемые и внешние таблицы.
В следующих блоках вам будут встречаться термины «Управляемые таблицы» и «Внешние таблицы».

(Опционально) [Cоздайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Cоздайте публичный SNAT-шлюз, если необходим доступ в интернет.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться таблицы и схемы.

[Создайте секреты](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секреты в сервисе Secret Management для доступа к Object Storage.
Понадобится сохранить идентификатор ключа доступа (access key) и секретный ключ доступа (key secret).

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

Назовите кластер «dp-labs».

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Установите JDBC-клиент DBeaver.

## Создайте инстанс Managed Metastore

1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:

Название — metastore-lab.
Кластер — dp-labs.
Лог-группа — группа логов.
Файловая система — S3.
Источник — Object Storage.
Бакет — созданный бакет Object Storage.
5. Нажмите Продолжить.
6. В блоке Сетевые настройки выберите:

Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
7. Нажмите Создать.
8. Дождитесь, когда статус инстанса изменится на «Готов».
9. Нажмите Скопировать Thrift URL.

Перейдите в раздел Evolution и выберите сервис Managed Metastore.

Откройте раздел Инстансы.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля следующими значениями:

- Название — metastore-lab.
- Кластер — dp-labs.
- Лог-группа — группа логов.
- Файловая система — S3.
- Источник — Object Storage.
- Бакет — созданный бакет Object Storage.

Название — metastore-lab.

Кластер — dp-labs.

Лог-группа — группа логов.

Файловая система — S3.

Источник — Object Storage.

Бакет — созданный бакет Object Storage.

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Зона доступности —

Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Нажмите Создать.

Дождитесь, когда статус инстанса изменится на «Готов».

Нажмите Скопировать Thrift URL.

## Создайте каталог Metastore

1. Перейдите в раздел Evolution и выберите сервис Managed Metastore.
2. Откройте раздел Каталоги.
3. Нажмите Создать каталог.
4. Заполните поля следующими значениями:

Название — metastore_lab;
Коннектор — Metastore;
Thrift URL — Thrift URL, скопированный с карточки Metastore;
Эндпоинт — https://s3.cloud.ru;
Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;
Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;
Регион S3 — ru-central-1.
5. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed Metastore.

Откройте раздел Каталоги.

Нажмите Создать каталог.

Заполните поля следующими значениями:

- Название — metastore_lab;
- Коннектор — Metastore;
- Thrift URL — Thrift URL, скопированный с карточки Metastore;
- Эндпоинт — https://s3.cloud.ru;
- Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;
- Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;
- Регион S3 — ru-central-1.

Название — metastore_lab;

Коннектор — Metastore;

Thrift URL — Thrift URL, скопированный с карточки Metastore;

Эндпоинт — https://s3.cloud.ru;

Идентификатор ключа доступа — access key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;

Секретный ключ доступа — secret key, выбирается из [Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Management;

Регион S3 — ru-central-1.

Нажмите Создать.

На странице Managed Trino на вкладке Каталоги появится запись с названием «metastore_lab».

## Создайте инстанс Trino

1. Перейдите в раздел Evolution и выберите сервис Managed Trino.
2. Откройте раздел Инстансы.
3. Нажмите Создать инстанс.
4. В блоке Общие параметры заполните поля следующими значениями:

Название — trino-lab-2.
Вычислительные ресурсы — vCPU 4, RAM 16.
Количество нод — 3.
Каталоги — выберите из списка каталог Metastore с названием «metastore_lab».
5. Нажмите Продолжить.
6. В блоке Сетевые настройки выберите:

Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером, в которой расположен инстанс Managed Metastore.
Группа безопасности — группу безопасности.
Пользователь — введите имя пользователя.
Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
Подключить публичный хост — активируйте переключатель.
7. Нажмите Создать.
8. Дождитесь, когда статус инстанса изменится на «Готов».
9. Откройте карточку инстанса Trino.
Информация из него понадобится на следующих этапах.

Перейдите в раздел Evolution и выберите сервис Managed Trino.

Откройте раздел Инстансы.

Нажмите Создать инстанс.

В блоке Общие параметры заполните поля следующими значениями:

- Название — trino-lab-2.
- Вычислительные ресурсы — vCPU 4, RAM 16.
- Количество нод — 3.
- Каталоги — выберите из списка каталог Metastore с названием «metastore_lab».

Название — trino-lab-2.

Вычислительные ресурсы — vCPU 4, RAM 16.

Количество нод — 3.

Каталоги — выберите из списка каталог Metastore с названием «metastore_lab».

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, для которой создан SNAT-шлюз.
- Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером, в которой расположен инстанс Managed Metastore.
- Группа безопасности — группу безопасности.
- Пользователь — введите имя пользователя.
- Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.
- Подключить публичный хост — активируйте переключатель.

Зона доступности —

Подсеть — подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером, в которой расположен инстанс Managed Metastore.

Группа безопасности — группу безопасности.

Пользователь — введите имя пользователя.

Пароль — [секретный ключ](https://cloud.ru/docs/scsm/ug/topics/guides_secret)секретный ключ.

Подключить публичный хост — активируйте переключатель.

Нажмите Создать.

Дождитесь, когда статус инстанса изменится на «Готов».

Откройте карточку инстанса Trino.
Информация из него понадобится на следующих этапах.

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

Слева в списке объектов появится база данных Metastore с названием «metastore_lab».

![../_images/dbeaver__connection-ready-2.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/dbeaver__connection-ready-2.png)

## Работа с управляемыми таблицами

SQL-запросы в следующих шагах мы будем отправлять через DBeaver.

Ознакомьтесь с разделом [Управляемые и внешние таблицы](https://cloud.ru/docs/trino/ug/topics/concepts__external-internal-tables)Управляемые и внешние таблицы перед началом.

### Управляемая таблица в формате .orc

1. Создайте схему.
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.
2. Создайте таблицу.
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees (id_employee INT, email VARCHAR(255))

В S3 создастся каталог employees.
3. Заполните таблицу.
INSERT INTO metastore_lab.my_company.employees values (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com')
4. Проверьте результат.
SELECT * FROM metastore_lab.my_company.employees

В S3 появится файл в формате .orc.
5. Удалите таблицу.
DROP TABLE metastore_lab.my_company.employees

Создайте схему.

```bash
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.

Создайте таблицу.

```bash
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees
(
id_employee INT, email VARCHAR
(
255
))
```

В S3 создастся каталог employees.

Заполните таблицу.

```bash
INSERT INTO metastore_lab.my_company.employees values
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
```

Проверьте результат.

```bash
SELECT * FROM metastore_lab.my_company.employees
```

В S3 появится файл в формате .orc.

Удалите таблицу.

```bash
DROP TABLE metastore_lab.my_company.employees
```

В результате таблица удалена из Metastore, в S3 все данные вместе с каталогом employees также удалены.

### Управляемая таблица в текстовом формате

1. Создайте схему.
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.
2. Сохраните данные в текстовом формате.
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees_csv (id_employee INT, email VARCHAR(255))WITH (format = 'TEXTFILE')
3. Заполните таблицу.
INSERT INTO metastore_lab.my_company.employees_csv values (1, 'xxx@example.com'), (2, 'yyy@example.com'), (3, 'zzz@example.com')
4. Проверьте результат.
SELECT * FROM metastore_lab.my_company.employees_csv

В S3 появится файл в формате .gz.
5. Удалите таблицу.
DROP TABLE metastore_lab.my_company.employees_csv

Создайте схему.

```bash
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

В S3 автоматически создастся каталог warehouse и каталог со схемой my_company.db.

Сохраните данные в текстовом формате.

```bash
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.employees_csv
(
id_employee INT, email VARCHAR
(
255
))
WITH
(
format
=
'TEXTFILE'
)
```

Заполните таблицу.

```bash
INSERT INTO metastore_lab.my_company.employees_csv values
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
```

Проверьте результат.

```bash
SELECT * FROM metastore_lab.my_company.employees_csv
```

В S3 появится файл в формате .gz.

Удалите таблицу.

```bash
DROP TABLE metastore_lab.my_company.employees_csv
```

В результате таблица удалена из Metastore, в S3 все данные вместе с каталогом employees_csv также удалены.

## Работа с внешними таблицами

1. Откройте бакет S3.
2. Создайте каталог с названием data.
3. Подготовьте файл с данными в формате .csv:

колонки: id, email
значения в колонке id: 1, 2, 3
значения в колонке email: xxx@example.com, yyy@example.com, zzz@example.com
4. Добавьте файл в каталог «data» на S3.
5. Запустите DBeaver.
6. Через DBeaver создайте схему.
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
7. Создайте таблицу.
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.csv_external (id VARCHAR, email VARCHAR)WITH ( external_location = 's3a://bucket-4b8dce/data', format = 'CSV', csv_separator = ';', skip_header_line_count = 1)
8. Проверьте результат.
SELECT * FROM metastore_lab.my_company.csv_external
9. Подготовьте новый файл с данными в формате .csv:

колонки: id, email
значения в колонке id: 4, 5, 6
значения в колонке email: aaa@example.com, bbb@example.com, ccc@example.com
10. Добавьте файл в каталог «data» на S3.
В этом сценарии мы имитируем поступление новых данных из другой системы.
11. Проверьте результат.
SELECT * FROM metastore_lab.my_company.csv_external

Система считывает данные из двух разных файлов с одинаковой структурой и с одинаковым разрешением, как если бы это был один файл.
12. Удалите таблицу.
DROP TABLE metastore_lab.my_company.csv_external

Откройте бакет S3.

Создайте каталог с названием data.

Подготовьте файл с данными в формате .csv:

- колонки: id, email
- значения в колонке id: 1, 2, 3
- значения в колонке email: xxx@example.com, yyy@example.com, zzz@example.com

колонки: id, email

значения в колонке id: 1, 2, 3

значения в колонке email: xxx@example.com, yyy@example.com, zzz@example.com

Добавьте файл в каталог «data» на S3.

Запустите DBeaver.

Через DBeaver создайте схему.

```bash
CREATE SCHEMA IF NOT EXISTS metastore_lab.my_company
```

Создайте таблицу.

```bash
CREATE TABLE IF NOT EXISTS metastore_lab.my_company.csv_external
(
id VARCHAR, email VARCHAR
)
WITH
(
external_location
=
's3a://bucket-4b8dce/data'
,
format
=
'CSV'
,
csv_separator
=
';'
,
skip_header_line_count
=
1
)
```

Проверьте результат.

```bash
SELECT * FROM metastore_lab.my_company.csv_external
```

Подготовьте новый файл с данными в формате .csv:

- колонки: id, email
- значения в колонке id: 4, 5, 6
- значения в колонке email: aaa@example.com, bbb@example.com, ccc@example.com

колонки: id, email

значения в колонке id: 4, 5, 6

значения в колонке email: aaa@example.com, bbb@example.com, ccc@example.com

Добавьте файл в каталог «data» на S3.
В этом сценарии мы имитируем поступление новых данных из другой системы.

Проверьте результат.

```bash
SELECT * FROM metastore_lab.my_company.csv_external
```

Система считывает данные из двух разных файлов с одинаковой структурой и с одинаковым разрешением, как если бы это был один файл.

Удалите таблицу.

```bash
DROP TABLE metastore_lab.my_company.csv_external
```

В результате таблица удалена из Metastore.
В отличие от управляемых таблиц файлы в S3 остаются доступными.
