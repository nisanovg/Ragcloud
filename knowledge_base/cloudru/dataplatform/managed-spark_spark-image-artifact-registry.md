---
title: Работа с пользовательским образом
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry
topic: dataplatform
---
# Работа с пользовательским образом

С помощью этого руководства вы научитесь обрабатывать данные, применяя [пользовательский образ](https://cloud.ru/docs/spark/ug/topics/concepts__user-image)пользовательский образ Spark.
Вы примените пользовательский образ, включающий библиотеки для работы с Object Storage и библиотеку NumPy.
Для обработки данных вы используете скрипт, который объединит информацию о заказах из двух таблиц в единую витрину данных, найдет среднюю стоимость заказа и подсчитает разницу с ней для каждого заказа.

Вы будете использовать следующие сервисы:

- [Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry — сервис для хранения и распространения артефактов.

[Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry — сервис для хранения и распространения артефактов.

Шаги:

1. [Подготовьте файлы с данными](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте файлы с данными.
2. [Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте скрипт задачи.
3. [Подготовьте образ в Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте образ в Artifact Registry.
4. [Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Создайте задачу Managed Spark.
5. [Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Наблюдайте за ходом выполнения задачи.

[Подготовьте файлы с данными](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте файлы с данными.

[Подготовьте скрипт задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте скрипт задачи.

[Подготовьте образ в Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Подготовьте образ в Artifact Registry.

[Создайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Создайте задачу Managed Spark.

[Наблюдайте за ходом выполнения задачи](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-image-artifact-registry)Наблюдайте за ходом выполнения задачи.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
5. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. [Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.
8. [Создайте реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте реестр Artifact Registry, в котором будет храниться пользовательский образ Managed Spark.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.

[Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.

[Создайте реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте реестр Artifact Registry, в котором будет храниться пользовательский образ Managed Spark.

## 1. Подготовьте файлы с данными

На этом шаге вы загрузите в хранилище Object Storage файлы с данными для обработки.

1. Скачайте CSV-таблицы [client-spark-image.csv](https://xbox.cloud.ru/index.php/s/mq9XKcKm4sJdsrm)client-spark-image.csv и [sales-spark-image.csv](https://xbox.cloud.ru/index.php/s/3fsX3aPTrN4Q2D8)sales-spark-image.csv: нажмите Скачать в правом верхнем углу.
2. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.
3. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицы в папку input.

Скачайте CSV-таблицы [client-spark-image.csv](https://xbox.cloud.ru/index.php/s/mq9XKcKm4sJdsrm)client-spark-image.csv и [sales-spark-image.csv](https://xbox.cloud.ru/index.php/s/3fsX3aPTrN4Q2D8)sales-spark-image.csv: нажмите Скачать в правом верхнем углу.

В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку input.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите CSV-таблицы в папку input.

## 2. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файл, содержащий скрипт для обработки данных из CSV-таблицы.

1. Скопируйте скрипт и назовите файл script-spark-image.py.

import numpy as npimport time
from pyspark.sql import SparkSessionfrom pyspark.sql.types import FloatTypefrom pyspark.sql.functions import lit, udf
bucket_name = 'your-bucket-name'
spark = (SparkSession.builder .appName("sales") .getOrCreate() )
# Read the source data from csvdf_sales = spark.read \.format("csv") \.option("header", "true") \.option("inferSchema", "true") \.option("delimiter", ";") \.load(f"s3a://{bucket_name}/input/sales-spark-image.csv")
df_client = spark.read \.format("csv") \.option("header", "true") \.option("inferSchema", "true") \.option("delimiter", ";") \.load(f"s3a://{bucket_name}/input/client-spark-image.csv")
# get average cost for all salesnp_arr = np.array(df_sales.select('sales').collect())avg = np.average(np_arr)print(f'Average cost: {avg}')# define UDF
@udf(returnType=FloatType())def calc_diff_avg(avg, val): return val - avg# Create result with sale price and diff between sale price and average price
df_result = df_sales \.join(df_client, df_sales.order_number == df_client.order_number,"inner") \.select( \ df_client.order_number, \ df_client.order_date, \ df_client.phone, \ df_client.address_line1, \ df_client.address_line2, \ df_client.city, \ df_client.state, \ df_client.postal_code, \ df_client.country, \ df_client.territory, \ df_client.contact_last_name, \ df_client.contact_first_name, \ df_client.deal_size, \ df_client.car, \ df_sales.sales, \ calc_diff_avg(lit(avg), df_sales.sales).alias("diff_with_avg") \)
# Write the result to csv filedf_result.write.mode('overwrite').option("header","true").csv(f"s3a://{bucket_name}/output/sales")
2. В строке bucket_name = 'your-bucket-name' замените your-bucket-name на название бакета Object Storage.
3. В ранее созданном бакете Object Storage [создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)создайте папку jobs.
4. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите скрипт в папку jobs.

Скопируйте скрипт и назовите файл script-spark-image.py.

```bash
import
numpy
as
np
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
FloatType
from
pyspark
.
sql
.
functions
import
lit
,
udf
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
# Read the source data from csv
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
/input/sales-spark-image.csv"
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
/input/client-spark-image.csv"
)
# get average cost for all sales
np_arr
=
np
.
array
(
df_sales
.
select
(
'sales'
)
.
collect
(
)
)
avg
=
np
.
average
(
np_arr
)
print
(
f'Average cost:
{
avg
}
'
)
# define UDF
@udf
(
returnType
=
FloatType
(
)
)
def
calc_diff_avg
(
avg
,
val
)
:
return
val
-
avg
# Create result with sale price and diff between sale price and average price
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
sales
,
\
calc_diff_avg
(
lit
(
avg
)
,
df_sales
.
sales
)
.
alias
(
"diff_with_avg"
)
\
)
# Write the result to csv file
df_result
.
write
.
mode
(
'overwrite'
)
.
option
(
"header"
,
"true"
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

sales-spark-image.csv
client-spark-image.csv

jobs

script-spark-image.py

<bucket>

- input

sales-spark-image.csv
client-spark-image.csv
- jobs

script-spark-image.py

input

- sales-spark-image.csv
- client-spark-image.csv

sales-spark-image.csv

client-spark-image.csv

jobs

- script-spark-image.py

script-spark-image.py

## 3. Подготовьте образ в Artifact Registry

На этом шаге вы подготовите пользовательский образ Managed Spark и загрузите его в сервис Artifact Registry.

1. Создайте Dockerfile для сборки образа.
FROM apache/spark:3.5.0-scala2.12-java11-python3-ubuntu
# add S3 libsRUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar -o /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jarRUN curl https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar -o /opt/spark/jars/hadoop-aws-3.3.4.jar
ARG spark_uid=rootUSER ${spark_uid}
# install compatible numpy versionRUN pip install numpy==1.21.6
2. Чтобы собрать образ, выполните команду:
docker build . --tag <IMAGE-NAME>:<TAG> --platform linux/amd64

Где:

<IMAGE-NAME> — имя образа.
<TAG> — тег образа.
3. Откройте сервис Artifact Registry.
4. [Создайте репозиторий](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__repository-create)Создайте репозиторий.
5. [Загрузите образ](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__artifact-push)Загрузите образ.

Создайте Dockerfile для сборки образа.

```bash
FROM apache/spark:3.5.0-scala2.12-java11-python3-ubuntu
# add S3 libs
RUN
curl
https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
-o
/opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar
RUN
curl
https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
-o
/opt/spark/jars/hadoop-aws-3.3.4.jar
ARG
spark_uid
=
root
USER
${spark_uid}
# install compatible numpy version
RUN pip
install
numpy
==
1.21
.6
```

Чтобы собрать образ, выполните команду:

```bash
docker
build
.
--tag
<
IMAGE-NAME
>
:
<
TAG
>
--platform
linux/amd64
```

Где:

- <IMAGE-NAME> — имя образа.
- <TAG> — тег образа.

<IMAGE-NAME> — имя образа.

<TAG> — тег образа.

Откройте сервис Artifact Registry.

[Создайте репозиторий](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__repository-create)Создайте репозиторий.

[Загрузите образ](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__artifact-push)Загрузите образ.

## 4. Создайте задачу Managed Spark

На этом шаге вы запустите задачу Managed Spark с использованием подготовленного скрипта.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например spark-image-sales.
6. В блоке Образ:

Выберите Пользовательский.
Под полем URI образа нажмите Выбрать из реестра и выберите добавленный ранее образ.
7. В блоке Скрипт приложения:

В поле Тип запускаемой задачи выберите Python.
В поле Путь к запускаемому файлу укажите путь к файлу script-spark-image.py.
В данном случае путь s3a://{bucket_name}/jobs/script-spark-image.py, где {bucket_name} — название созданного бакета Object Storage.
8. Нажмите Создать.

Перейдите в сервис Managed Spark.

Откройте созданный ранее инстанс.

Перейдите на вкладку Задачи.

Нажмите Создать задачу.

В блоке Общие параметры введите название задачи, например spark-image-sales.

В блоке Образ:

1. Выберите Пользовательский.
2. Под полем URI образа нажмите Выбрать из реестра и выберите добавленный ранее образ.

Выберите Пользовательский.

Под полем URI образа нажмите Выбрать из реестра и выберите добавленный ранее образ.

В блоке Скрипт приложения:

- В поле Тип запускаемой задачи выберите Python.
- В поле Путь к запускаемому файлу укажите путь к файлу script-spark-image.py.
В данном случае путь s3a://{bucket_name}/jobs/script-spark-image.py, где {bucket_name} — название созданного бакета Object Storage.

В поле Тип запускаемой задачи выберите Python.

В поле Путь к запускаемому файлу укажите путь к файлу script-spark-image.py.
В данном случае путь s3a://{bucket_name}/jobs/script-spark-image.py, где {bucket_name} — название созданного бакета Object Storage.

Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

## 5. Наблюдайте за ходом выполнения задачи

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

## Результат

Когда задача перейдет в статус «Выполнено», откройте [файловый менеджер Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager)файловый менеджер Object Storage.
В бакете появится новая папка output, в которой будет храниться сводная таблица данных.

Вы применили пользовательский образ Managed Spark и скрипт для обработки данных и получили объединенную таблицу со всеми данными.
