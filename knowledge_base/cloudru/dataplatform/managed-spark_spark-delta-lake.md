---
title: Работа с таблицами Delta Lake
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake
topic: dataplatform
---
# Работа с таблицами Delta Lake

С помощью этого руководства вы научитесь использовать сервис Managed Spark для обработки таблиц формата [Delta Lake](https://docs.delta.io/latest/index.html)Delta Lake.

Вы построите витрину данных, отражающую полную информацию о клиентах и их пути, сохраните результат в формате Delta Lake и выгрузите историю изменений таблицы в логи.

Вы будете использовать следующие сервисы:

- [Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

[Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

Шаги:

1. [Подготовьте файл CSV](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Подготовьте файл CSV.
2. [Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Подготовьте скрипт задачи.
3. [Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Создайте задачу Managed Spark.
4. [Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Наблюдайте за ходом выполнения задачи.

[Подготовьте файл CSV](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Подготовьте файл CSV.

[Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Подготовьте скрипт задачи.

[Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Создайте задачу Managed Spark.

[Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-delta-lake)Наблюдайте за ходом выполнения задачи.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
5. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. [Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.
8. [Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте публичный SNAT-шлюз для доступа инстанса к внешним источникам.
9. [Сверьте совместимость версий](https://cloud.ru/docs/spark/ug/topics/concepts__spark-version-compatibility)Сверьте совместимость версий Spark и Delta Lake.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.

[Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.

[Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте публичный SNAT-шлюз для доступа инстанса к внешним источникам.

[Сверьте совместимость версий](https://cloud.ru/docs/spark/ug/topics/concepts__spark-version-compatibility)Сверьте совместимость версий Spark и Delta Lake.

## 1. Подготовьте файл CSV

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте CSV-таблицу [delta-table.csv](https://xbox.cloud.ru/index.php/s/78pLoAZMBKiGnFd)delta-table.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.
3. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицу в папку input.

Скачайте CSV-таблицу [delta-table.csv](https://xbox.cloud.ru/index.php/s/78pLoAZMBKiGnFd)delta-table.csv: нажмите Скачать в правом верхнем углу.

В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицу в папку input.

## 2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл delta-script.py.

import time
from pyspark.sql import SparkSessionfrom pyspark.sql.types import DoubleType, FloatType, LongType, StructType,StructField, StringTypefrom delta import *
spark = (SparkSession.builder .appName('Delta test') .enableHiveSupport() .getOrCreate() )
SCHEMA = StructType([ StructField("vendor_id", LongType(), True), StructField("trip_id", LongType(), True), StructField("trip_distance", FloatType(), True), StructField("fare_amount", DoubleType(), True), StructField("store_and_fwd_flag", StringType(), True)])
TABLE_TIME = time.strftime('%Y_%m_%d__%H_%M_%S')TABLE_NAME = "delta_lab" + TABLE_TIMEROOT_PATH = "s3a://your-bucket-name/"CSV_PATH = ROOT_PATH + "input/delta-table.csv"FULL_PATH_DELTA_TABLE = ROOT_PATH + "warehouse_delta/" + TABLE_NAME
def read_csv_to_table(): _csv_df = ( spark .read .option("delimiter", ";") .option("header", True) .csv(CSV_PATH, schema=SCHEMA) ) _csv_df.show() return _csv_df
def insert_data_to_table(df): df.write.format("delta").save(FULL_PATH_DELTA_TABLE)
def read_data_from_table(): df = spark.read.format("delta").load(FULL_PATH_DELTA_TABLE) df.show()
def update_delta_table(): delta_table = DeltaTable.forPath(spark, FULL_PATH_DELTA_TABLE)
 delta_table.update( condition="vendor_id % 2 = 0", set={ "trip_distance": "trip_distance + 2" } )
def show_history_delta(): delta_table = DeltaTable.forPath(spark, FULL_PATH_DELTA_TABLE) history = delta_table.history() history.show()
def read_specific_version_delta(version: int): df = spark.read.format("delta").option("versionAsOf", version).load(FULL_PATH_DELTA_TABLE) df.show()
if __name__ == "__main__": csv_df = read_csv_to_table() insert_data_to_table(df=csv_df) read_data_from_table()
 update_delta_table() read_data_from_table()
 update_delta_table() read_data_from_table()
 show_history_delta()
 read_specific_version_delta(version=1)
 spark.stop()
2. В строке ROOT_PATH = "s3a://your-bucket-name/" скрипта замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку jobs.
4. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите скрипт в папку jobs.

Скопируйте скрипт и назовите файл delta-script.py.

```bash
import
time
from
pyspark
.
sql
import
SparkSession
from
pyspark
.
sql
.
types
import
DoubleType
,
FloatType
,
LongType
,
StructType
,
StructField
,
StringType
from
delta
import
*
spark
=
(
SparkSession
.
builder
.
appName
(
'Delta test'
)
.
enableHiveSupport
(
)
.
getOrCreate
(
)
)
SCHEMA
=
StructType
(
[
StructField
(
"vendor_id"
,
LongType
(
)
,
True
)
,
StructField
(
"trip_id"
,
LongType
(
)
,
True
)
,
StructField
(
"trip_distance"
,
FloatType
(
)
,
True
)
,
StructField
(
"fare_amount"
,
DoubleType
(
)
,
True
)
,
StructField
(
"store_and_fwd_flag"
,
StringType
(
)
,
True
)
]
)
TABLE_TIME
=
time
.
strftime
(
'%Y_%m_%d__%H_%M_%S'
)
TABLE_NAME
=
"delta_lab"
+
TABLE_TIME
ROOT_PATH
=
"s3a://your-bucket-name/"
CSV_PATH
=
ROOT_PATH
+
"input/delta-table.csv"
FULL_PATH_DELTA_TABLE
=
ROOT_PATH
+
"warehouse_delta/"
+
TABLE_NAME
def
read_csv_to_table
(
)
:
_csv_df
=
(
spark
.
read
.
option
(
"delimiter"
,
";"
)
.
option
(
"header"
,
True
)
.
csv
(
CSV_PATH
,
schema
=
SCHEMA
)
)
_csv_df
.
show
(
)
return
_csv_df
def
insert_data_to_table
(
df
)
:
df
.
write
.
format
(
"delta"
)
.
save
(
FULL_PATH_DELTA_TABLE
)
def
read_data_from_table
(
)
:
df
=
spark
.
read
.
format
(
"delta"
)
.
load
(
FULL_PATH_DELTA_TABLE
)
df
.
show
(
)
def
update_delta_table
(
)
:
delta_table
=
DeltaTable
.
forPath
(
spark
,
FULL_PATH_DELTA_TABLE
)
delta_table
.
update
(
condition
=
"vendor_id % 2 = 0"
,
set
=
{
"trip_distance"
:
"trip_distance + 2"
}
)
def
show_history_delta
(
)
:
delta_table
=
DeltaTable
.
forPath
(
spark
,
FULL_PATH_DELTA_TABLE
)
history
=
delta_table
.
history
(
)
history
.
show
(
)
def
read_specific_version_delta
(
version
:
int
)
:
df
=
spark
.
read
.
format
(
"delta"
)
.
option
(
"versionAsOf"
,
version
)
.
load
(
FULL_PATH_DELTA_TABLE
)
df
.
show
(
)
if
__name__
==
"__main__"
:
csv_df
=
read_csv_to_table
(
)
insert_data_to_table
(
df
=
csv_df
)
read_data_from_table
(
)
update_delta_table
(
)
read_data_from_table
(
)
update_delta_table
(
)
read_data_from_table
(
)
show_history_delta
(
)
read_specific_version_delta
(
version
=
1
)
spark
.
stop
(
)
```

В строке ROOT_PATH = "s3a://your-bucket-name/" скрипта замените your-bucket-name на название бакета Object Storage.

В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку jobs.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите скрипт в папку jobs.

В результате получится следующая структура бакета с файлами:

- <bucket>

input

delta-table.csv

jobs

delta-script.py

<bucket>

- input

delta-table.csv
- jobs

delta-script.py

input

- delta-table.csv

delta-table.csv

jobs

- delta-script.py

delta-script.py

## 3. Создайте задачу Managed Spark

На этом шаге вы создадите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например delta.
6. В блоке Скрипт приложения:

В поле Тип запускаемой задачи выберите Python.
В поле Путь к запускаемому файлу укажите путь к файлу delta-script.py.
В данном случае путь s3a://{bucket_name}/jobs/delta-script.py, где {bucket_name} — название созданного бакета Object Storage.
7. В блоке Настройки активируйте опцию Добавить Spark-конфигурацию (–conf). Добавьте следующие параметры и их значения:
 ПараметрЗначениеspark.jars.packagesio.delta:delta-spark_2.12:3.2.0spark.sql.extensionsio.delta.sql.DeltaSparkSessionExtensionspark.sql.catalog.spark_catalogorg.apache.spark.sql.delta.catalog.DeltaCatalogspark.log.levelERROR
8. Нажмите Создать.

Перейдите в сервис Managed Spark.

Откройте созданный ранее инстанс.

Перейдите на вкладку Задачи.

Нажмите Создать задачу.

В блоке Общие параметры введите название задачи, например delta.

В блоке Скрипт приложения:

- В поле Тип запускаемой задачи выберите Python.
- В поле Путь к запускаемому файлу укажите путь к файлу delta-script.py.
В данном случае путь s3a://{bucket_name}/jobs/delta-script.py, где {bucket_name} — название созданного бакета Object Storage.

В поле Тип запускаемой задачи выберите Python.

В поле Путь к запускаемому файлу укажите путь к файлу delta-script.py.
В данном случае путь s3a://{bucket_name}/jobs/delta-script.py, где {bucket_name} — название созданного бакета Object Storage.

В блоке Настройки активируйте опцию Добавить Spark-конфигурацию (–conf). Добавьте следующие параметры и их значения:

Параметр

Значение

spark.jars.packages

io.delta:delta-spark_2.12:3.2.0

spark.sql.extensions

io.delta.sql.DeltaSparkSessionExtension

spark.sql.catalog.spark_catalog

org.apache.spark.sql.delta.catalog.DeltaCatalog

spark.log.level

ERROR

Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

## 4. Наблюдайте за ходом выполнения задачи

На этом шаге вы будете наблюдать за ходом выполнения задачи, просматривая информацию, поступающую в логи.

Вы можете посмотреть логи задачи, когда задача находится в статусах «Выполняется» и «Готово», то есть как в процессе выполнения, так и по завершению задачи.

### Перейдите к логам

1. В строке задачи нажмите и выберите Перейти к логам.
2. Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, например, за определенное время.

В строке задачи нажмите и выберите Перейти к логам.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, например, за определенное время.

### Перейдите в Spark UI

1. Откройте инстанс Managed Spark.
2. Во вкладке Задачи нажмите Spark UI. В соседней вкладке откроется интерфейс Spark UI.
3. Вернитесь в инстанс и откройте вкладку Информация.
4. Скопируйте данные из блока Настройки доступа.
5. Введите данные инстанса:

Username — значение поля Пользователь.
Password — значение секрета в поле Пароль.

Откройте инстанс Managed Spark.

Во вкладке Задачи нажмите Spark UI. В соседней вкладке откроется интерфейс Spark UI.

Вернитесь в инстанс и откройте вкладку Информация.

Скопируйте данные из блока Настройки доступа.

Введите данные инстанса:

- Username — значение поля Пользователь.
- Password — значение секрета в поле Пароль.

Username — значение поля Пользователь.

Password — значение секрета в поле Пароль.

В интерфейсе Spark UI вы найдете информацию о ходе выполнения задачи.

![../_images/spark-ui__delta-timeline.PNG](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/spark-ui__delta-timeline.PNG)

![../_images/spark-ui__delta-completed-jobs.PNG](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/spark-ui__delta-completed-jobs.PNG)

## Результат

Когда задача перейдет в статус «Выполнено», откройте бакет Object Storage.
В бакете появится новая папка с названием формата delta-lab_<TIME_STAMP>.
В этой папке хранятся:

- версии таблицы «delta-table.csv»;
- папка _delta_log с логами задачи.

версии таблицы «delta-table.csv»;

папка _delta_log с логами задачи.

Чтобы посмотреть историю изменений таблицы с помощью метода history():

1. Откройте сервис Managed Spark.
2. Перейдите на вкладку Задачи.
3. Скопируйте ID задачи.
4. Нажмите и выберите Перейти к логам.
5. В поле Запрос введите labels.spark_job_id="ID", где ID — идентификатор задачи, скопированный ранее.
6. Нажмите Скачать журнал логов.
7. Выберите формат файла.
8. Нажмите Скачать.
9. Откройте скачанный файл.

Откройте сервис Managed Spark.

Перейдите на вкладку Задачи.

Скопируйте ID задачи.

Нажмите и выберите Перейти к логам.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

В поле Запрос введите labels.spark_job_id="ID", где ID — идентификатор задачи, скопированный ранее.

Нажмите Скачать журнал логов.

Выберите формат файла.

Нажмите Скачать.

Откройте скачанный файл.

История изменений отображается в нескольких сообщениях.

Вы обработали таблицу формата Delta Lake с помощью сервиса Managed Spark и просмотрели информацию об изменениях в таблице.
