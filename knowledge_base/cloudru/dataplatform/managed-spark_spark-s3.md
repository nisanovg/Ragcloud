---
title: Обработка данных из Object Storage
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3
topic: dataplatform
---
# Обработка данных из Object Storage

С помощью этого руководства вы научитесь использовать сервис Managed Spark для обработки данных, хранящихся в [Evolution Object Storage](https://cloud.ru/docs/s3e/ug/index)Evolution Object Storage.

В качестве примера вы построите витрину данных, отражающую полную информацию о клиентах и продажах.

Будут использоваться данные из двух таблиц:

- Таблица client.csv содержит информацию о клиентах: номер заказа, дату, город, имя и фамилию клиента, модель автомобиля и др.
- Таблица sales.csv содержит информацию о продажах: номер заказа и его сумму.

Таблица client.csv содержит информацию о клиентах: номер заказа, дату, город, имя и фамилию клиента, модель автомобиля и др.

Таблица sales.csv содержит информацию о продажах: номер заказа и его сумму.

В результате получится таблица, в которой данные объединены по номеру заказа.

Вы будете использовать следующие сервисы:

- [Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

[Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

Шаги:

1. [Подготовьте файл CSV](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Подготовьте файл CSV.
2. [Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Подготовьте скрипт задачи.
3. [Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Создайте задачу Managed Spark.
4. [Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Наблюдайте за ходом выполнения задачи.

[Подготовьте файл CSV](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Подготовьте файл CSV.

[Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Подготовьте скрипт задачи.

[Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Создайте задачу Managed Spark.

[Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-s3)Наблюдайте за ходом выполнения задачи.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
5. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. [Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.

[Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.

## 1. Подготовьте файл CSV

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте [sales.csv](https://xbox.cloud.ru/index.php/s/DNxrstydHJCAazM)sales.csv и [client.csv](https://xbox.cloud.ru/index.php/s/9WKDXHgQMqEMff5)client.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.
3. В папке создайте папку car-sales.
4. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицы в папку car-sales.

Скачайте [sales.csv](https://xbox.cloud.ru/index.php/s/DNxrstydHJCAazM)sales.csv и [client.csv](https://xbox.cloud.ru/index.php/s/9WKDXHgQMqEMff5)client.csv: нажмите Скачать в правом верхнем углу.

В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.

В папке создайте папку car-sales.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицы в папку car-sales.

## 2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл spark-sales-etl.py.
import timefrom pyspark.sql import SparkSessionfrom pyspark.sql.types import StructType, StructField, StringType, IntegerTypefrom pyspark.sql.functions import countfrom pyspark.sql.types import IntegerType,BooleanType,DateTypefrom pyspark.sql.functions import colfrom pyspark.sql.functions import sum,avg,max
bucket_name = 'your-bucket-name'
spark = (SparkSession.builder .appName("sales") .getOrCreate() )
df_sales = spark.read \ .format("csv") \ .option("header", "true") \ .option("inferSchema", "true") \ .option("delimiter", ";") \ .load(f"s3a://{bucket_name}/input/car-sales/sales.csv")
df_client = spark.read \ .format("csv") \ .option("header", "true") \ .option("inferSchema", "true") \ .option("delimiter", ";") \ .load(f"s3a://{bucket_name}/input/car-sales/client.csv")
df_result = df_sales \ .join(df_client, df_sales.order_number == df_client.order_number,"inner") \ .select( \ df_client.order_number, \ df_client.order_date, \ df_client.phone, \ df_client.address_line1, \ df_client.address_line2, \ df_client.city, \ df_client.state, \ df_client.postal_code, \ df_client.country, \ df_client.territory, \ df_client.contact_last_name, \ df_client.contact_first_name, \ df_client.deal_size, \ df_client.car, \ df_sales.sales \ )
df_result.write.mode('overwrite').csv(f"s3a://{bucket_name}/output/sales")
2. В строке bucket_name = 'your-bucket-name' замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку jobs.
4. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите скрипт в папку jobs.

Скопируйте скрипт и назовите файл spark-sales-etl.py.

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
StructType
,
StructField
,
StringType
,
IntegerType
from
pyspark
.
sql
.
functions
import
count
from
pyspark
.
sql
.
types
import
IntegerType
,
BooleanType
,
DateType
from
pyspark
.
sql
.
functions
import
col
from
pyspark
.
sql
.
functions
import
sum
,
avg
,
max
bucket_name
=
'your-bucket-name'
spark
=
(
SparkSession
.
builder
.
appName
(
"sales"
)
.
getOrCreate
(
)
)
df_sales
=
spark
.
read \
.
format
(
"csv"
)
\
.
option
(
"header"
,
"true"
)
\
.
option
(
"inferSchema"
,
"true"
)
\
.
option
(
"delimiter"
,
";"
)
\
.
load
(
f"s3a://
{
bucket_name
}
/input/car-sales/sales.csv"
)
df_client
=
spark
.
read \
.
format
(
"csv"
)
\
.
option
(
"header"
,
"true"
)
\
.
option
(
"inferSchema"
,
"true"
)
\
.
option
(
"delimiter"
,
";"
)
\
.
load
(
f"s3a://
{
bucket_name
}
/input/car-sales/client.csv"
)
df_result
=
df_sales \
.
join
(
df_client
,
df_sales
.
order_number
==
df_client
.
order_number
,
"inner"
)
\
.
select
(
\
df_client
.
order_number
,
\
df_client
.
order_date
,
\
df_client
.
phone
,
\
df_client
.
address_line1
,
\
df_client
.
address_line2
,
\
df_client
.
city
,
\
df_client
.
state
,
\
df_client
.
postal_code
,
\
df_client
.
country
,
\
df_client
.
territory
,
\
df_client
.
contact_last_name
,
\
df_client
.
contact_first_name
,
\
df_client
.
deal_size
,
\
df_client
.
car
,
\
df_sales
.
sales \
)
df_result
.
write
.
mode
(
'overwrite'
)
.
csv
(
f"s3a://
{
bucket_name
}
/output/sales"
)
```

В строке bucket_name = 'your-bucket-name' замените your-bucket-name на название бакета Object Storage.

В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку jobs.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите скрипт в папку jobs.

В результате получится следующая структура бакета с файлами:

- <bucket>

input

car-sales

client.csv
sales.csv

jobs

spark-sales-etl.py

<bucket>

- input

car-sales

client.csv
sales.csv
- jobs

spark-sales-etl.py

input

- car-sales

client.csv
sales.csv

car-sales

- client.csv
- sales.csv

client.csv

sales.csv

jobs

- spark-sales-etl.py

spark-sales-etl.py

## 3. Создайте задачу Managed Spark

На этом шаге вы запустите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например spark-sales.
6. В блоке Скрипт приложения:

В поле Тип запускаемой задачи выберите Python.
В поле Путь к запускаемому файлу укажите путь к файлу spark-sales-etl.py.
В данном случае путь s3a://{bucket_name}/jobs/spark-sales-etl.py, где {bucket_name} — название созданного бакета Object Storage.
7. Нажмите Создать.

Перейдите в сервис Managed Spark.

Откройте созданный ранее инстанс.

Перейдите на вкладку Задачи.

Нажмите Создать задачу.

В блоке Общие параметры введите название задачи, например spark-sales.

В блоке Скрипт приложения:

- В поле Тип запускаемой задачи выберите Python.
- В поле Путь к запускаемому файлу укажите путь к файлу spark-sales-etl.py.
В данном случае путь s3a://{bucket_name}/jobs/spark-sales-etl.py, где {bucket_name} — название созданного бакета Object Storage.

В поле Тип запускаемой задачи выберите Python.

В поле Путь к запускаемому файлу укажите путь к файлу spark-sales-etl.py.
В данном случае путь s3a://{bucket_name}/jobs/spark-sales-etl.py, где {bucket_name} — название созданного бакета Object Storage.

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

![../_images/spark-ui__timeline.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/spark-ui__timeline.png)

![../_images/spark-ui__completed-jobs.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/spark-ui__completed-jobs.png)

## Результат

Когда задача перейдет в статус «Выполнено», откройте бакет Object Storage.
В бакете появятся:

- новая папка sales;
- таблица с объединенными данными из sales.csv и client.csv.

новая папка sales;

таблица с объединенными данными из sales.csv и client.csv.

Вы обработали данные из Object Storage с помощью сервиса Managed Spark и получили таблицу с объединенными данными.
