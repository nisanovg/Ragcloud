---
title: Чтение сообщений из топиков Managed Kafka®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming
topic: dataplatform
---
# Чтение сообщений из топиков Managed Kafka®

С помощью этого руководства вы настроите чтение сообщений из топика Managed Kafka® и отображение полученных данных в логах задачи Managed Spark.
Вы создадите две задачи Managed Spark c использованием скриптов для разового и для непрерывного чтения данных.

В результате вы получите возможность просматривать сообщения из топиков Managed Kafka® в логах задачи Managed Spark.

Вы будете использовать следующие сервисы:

- [Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.
- [Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka® в инфраструктуре платформы Evolution.

[Managed Spark](https://cloud.ru/docs/spark/ug/index)Managed Spark — сервис, который позволяет развернуть кластерное вычислительное решение на основе Apache Spark для распределенной обработки данных.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — сервис для хранения данных любого типа и объема. Будет использоваться в качестве хранилища для скриптов.

[Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka® в инфраструктуре платформы Evolution.

Шаги:

1. [Подготовьте скрипты, которые будут обращаться к топику Managed Kafka®](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Подготовьте скрипты, которые будут обращаться к топику Managed Kafka®.
2. [Cоздайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Cоздайте задачу Managed Spark.
3. [Проверьте информацию в логах](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Проверьте информацию в логах.
4. [Запустите непрерывное чтение топика Managed Kafka®](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Запустите непрерывное чтение топика Managed Kafka®.

[Подготовьте скрипты, которые будут обращаться к топику Managed Kafka®](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Подготовьте скрипты, которые будут обращаться к топику Managed Kafka®.

[Cоздайте задачу Managed Spark](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Cоздайте задачу Managed Spark.

[Проверьте информацию в логах](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Проверьте информацию в логах.

[Запустите непрерывное чтение топика Managed Kafka®](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-spark__spark-streaming)Запустите непрерывное чтение топика Managed Kafka®.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.
3. [Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
5. [Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.
6. Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.
7. [Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.
8. Убедитесь, что в проекте, где будет запускаться задача Managed Spark, доступен сервис Managed Kafka®.
9. [Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/quickstart)Создайте кластер Managed Kafka®. На шаге Сетевые настройки в списке Подсеть выберите подсеть, указанную при создании инстанса Managed Spark.
10. [Подключитесь к кластеру Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/quickstart)Подключитесь к кластеру Managed Kafka® и отправьте несколько сообщений в топик.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru. Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте бакет Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет Object Storage, в котором будут храниться необходимые файлы и логи.

[Настройте DNS-сервер и подсеть](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)Настройте DNS-сервер и подсеть.

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

[Скачайте и установите root-сертификат](https://cloud.ru/docs/dataplatform/ug/topics/guides__root-certificate)Скачайте и установите root-сертификат на устройство.

Создайте пароль и добавьте его в [Secret Manager](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Secret Manager. Этот секрет станет паролем для доступа к интерфейсу Managed Spark.

[Создайте инстанс Managed Spark](https://cloud.ru/docs/spark/ug/topics/guides__instance-creation)Создайте инстанс Managed Spark.

Убедитесь, что в проекте, где будет запускаться задача Managed Spark, доступен сервис Managed Kafka®.

[Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/quickstart)Создайте кластер Managed Kafka®. На шаге Сетевые настройки в списке Подсеть выберите подсеть, указанную при создании инстанса Managed Spark.

[Подключитесь к кластеру Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/quickstart)Подключитесь к кластеру Managed Kafka® и отправьте несколько сообщений в топик.

## 1. Подготовьте скрипт задачи

На этом шаге вы загрузите в хранилище Object Storage файлы, содержащие скрипты для чтения топика Managed Kafka®.
Скрипт из файла kafka_spark.py выполняет однократное чтение сообщений из топика, а скрипт из файла kafka_spark_streaming.py — непрерывное.

1. Скопируйте скрипт и назовите файл kafka_spark.py.
from pyspark.sql import SparkSessionimport os
kafka_user = os.environ["KAFKA_USER"]kafka_pass = os.environ["KAFKA_PASS"]kafka_topic = os.environ["KAFKA_TOPIC"]kafka_server = os.environ["KAFKA_SERVER"]
spark = SparkSession.builder.appName("kafka").getOrCreate()
df = ( spark.read.format("kafka") .option("kafka.bootstrap.servers", kafka_server) .option("kafka.security.protocol", "SASL_PLAINTEXT") .option("kafka.sasl.mechanism", "SCRAM-SHA-512") .option( "kafka.sasl.jaas.config", f'org.apache.kafka.common.security.scram.ScramLoginModule required username="{kafka_user}" password="{kafka_pass}";', ) .option("subscribe", kafka_topic) .option("startingOffsets", "earliest") .option("endingOffsets", "latest") .load())
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")df.show(truncate=False)spark.stop()
2. Скопируйте скрипт и назовите файл kafka_spark_streaming.py.
from pyspark.sql import SparkSessionimport os
kafka_user = os.environ["KAFKA_USER"]kafka_pass = os.environ["KAFKA_PASS"]kafka_topic = os.environ["KAFKA_TOPIC"]kafka_server = os.environ["KAFKA_SERVER"]
spark = ( SparkSession.builder.appName("kafka") .getOrCreate())
df = ( spark .readStream .format("kafka") .option("kafka.bootstrap.servers", kafka_server) .option("kafka.security.protocol", "SASL_PLAINTEXT") .option("kafka.sasl.mechanism", "SCRAM-SHA-512") .option( "kafka.sasl.jaas.config", f'org.apache.kafka.common.security.scram.ScramLoginModule required username="{kafka_user}" password="{kafka_pass}";', ) .option("subscribe", kafka_topic) .option("startingOffsets", "earliest") .load() )
df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")сonsole = (df .writeStream .outputMode('append') .format('console') .start() )console.awaitTermination()spark.stop()
3. Откройте ранее созданный бакет Object Storage.
4. [Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите файлы со скриптами.

Скопируйте скрипт и назовите файл kafka_spark.py.

```bash
from
pyspark
.
sql
import
SparkSession
import
os
kafka_user
=
os
.
environ
[
"KAFKA_USER"
]
kafka_pass
=
os
.
environ
[
"KAFKA_PASS"
]
kafka_topic
=
os
.
environ
[
"KAFKA_TOPIC"
]
kafka_server
=
os
.
environ
[
"KAFKA_SERVER"
]
spark
=
SparkSession
.
builder
.
appName
(
"kafka"
)
.
getOrCreate
(
)
df
=
(
spark
.
read
.
format
(
"kafka"
)
.
option
(
"kafka.bootstrap.servers"
,
kafka_server
)
.
option
(
"kafka.security.protocol"
,
"SASL_PLAINTEXT"
)
.
option
(
"kafka.sasl.mechanism"
,
"SCRAM-SHA-512"
)
.
option
(
"kafka.sasl.jaas.config"
,
f'org.apache.kafka.common.security.scram.ScramLoginModule required username="
{
kafka_user
}
" password="
{
kafka_pass
}
";'
,
)
.
option
(
"subscribe"
,
kafka_topic
)
.
option
(
"startingOffsets"
,
"earliest"
)
.
option
(
"endingOffsets"
,
"latest"
)
.
load
(
)
)
df
.
selectExpr
(
"CAST(key AS STRING)"
,
"CAST(value AS STRING)"
)
df
.
show
(
truncate
=
False
)
spark
.
stop
(
)
```

Скопируйте скрипт и назовите файл kafka_spark_streaming.py.

```bash
from
pyspark
.
sql
import
SparkSession
import
os
kafka_user
=
os
.
environ
[
"KAFKA_USER"
]
kafka_pass
=
os
.
environ
[
"KAFKA_PASS"
]
kafka_topic
=
os
.
environ
[
"KAFKA_TOPIC"
]
kafka_server
=
os
.
environ
[
"KAFKA_SERVER"
]
spark
=
(
SparkSession
.
builder
.
appName
(
"kafka"
)
.
getOrCreate
(
)
)
df
=
(
spark
.
readStream
.
format
(
"kafka"
)
.
option
(
"kafka.bootstrap.servers"
,
kafka_server
)
.
option
(
"kafka.security.protocol"
,
"SASL_PLAINTEXT"
)
.
option
(
"kafka.sasl.mechanism"
,
"SCRAM-SHA-512"
)
.
option
(
"kafka.sasl.jaas.config"
,
f'org.apache.kafka.common.security.scram.ScramLoginModule required username="
{
kafka_user
}
" password="
{
kafka_pass
}
";'
,
)
.
option
(
"subscribe"
,
kafka_topic
)
.
option
(
"startingOffsets"
,
"earliest"
)
.
load
(
)
)
df
.
selectExpr
(
"CAST(key AS STRING)"
,
"CAST(value AS STRING)"
)
сonsole
=
(
df
.
writeStream
.
outputMode
(
'append'
)
.
format
(
'console'
)
.
start
(
)
)
console
.
awaitTermination
(
)
spark
.
stop
(
)
```

Откройте ранее созданный бакет Object Storage.

[Загрузите](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)Загрузите файлы со скриптами.

## 2. Создайте задачу Managed Spark

На этом шаге вы создадите задачу Managed Spark с использованием подготовленного скрипта.
Скрипт выполнит чтение сообщений, отправленных в топик Managed Kafka®, и выведет данные из них в логи задачи Managed Spark.

Для продолжения работы убедитесь, что статус инстанса Managed Spark изменился на «Готов».

1. Перейдите в сервис Managed Spark.
2. Откройте созданный ранее инстанс.
3. Перейдите на вкладку Задачи.
4. Нажмите Создать задачу.
5. В блоке Общие параметры введите название задачи, например kafka-spark-streaming.
6. В блоке Образ выберите базовый образ Spark-3.5.0.
7. В блоке Скрипт приложения:

В поле Тип запускаемой задачи выберите Python.
В поле Путь к запускаемому файлу укажите путь к файлу kafka_spark.py.
8. В блоке Настройки активируйте опцию Добавить параметры окружения. Добавьте следующие параметры и их значения:
 ПараметрЗначениеKAFKA_USERЛогин для подключения к кластеру Managed Kafka®, например, cloud-admin.KAFKA_PASSПароль для подключения к кластеру Managed Kafka® с указанным логином.KAFKA_TOPICИмя топика Managed Kafka®.KAFKA_SERVERВнутренний IP-адрес кластера Managed Kafka®.
Чтобы узнать внутренний IP-адрес, логин и пароль, откройте сервис Managed Kafka® в отдельной вкладке, в списке кластеров нажмите на название созданного ранее кластера и перейдите в блок Данные для подключения.
9. В блоке Настройки активируйте опцию Добавить Spark конфигурацию (–conf).

В поле Аргумент укажите spark.jars.packages.
В поле Значение укажите org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0.
10. Нажмите Создать.

Перейдите в сервис Managed Spark.

Откройте созданный ранее инстанс.

Перейдите на вкладку Задачи.

Нажмите Создать задачу.

В блоке Общие параметры введите название задачи, например kafka-spark-streaming.

В блоке Образ выберите базовый образ Spark-3.5.0.

В блоке Скрипт приложения:

- В поле Тип запускаемой задачи выберите Python.
- В поле Путь к запускаемому файлу укажите путь к файлу kafka_spark.py.

В поле Тип запускаемой задачи выберите Python.

В поле Путь к запускаемому файлу укажите путь к файлу kafka_spark.py.

В блоке Настройки активируйте опцию Добавить параметры окружения. Добавьте следующие параметры и их значения:

Параметр

Значение

KAFKA_USER

Логин для подключения к кластеру Managed Kafka®, например, cloud-admin.

KAFKA_PASS

Пароль для подключения к кластеру Managed Kafka® с указанным логином.

KAFKA_TOPIC

Имя топика Managed Kafka®.

KAFKA_SERVER

Внутренний IP-адрес кластера Managed Kafka®.

Чтобы узнать внутренний IP-адрес, логин и пароль, откройте сервис Managed Kafka® в отдельной вкладке, в списке кластеров нажмите на название созданного ранее кластера и перейдите в блок Данные для подключения.

В блоке Настройки активируйте опцию Добавить Spark конфигурацию (–conf).

- В поле Аргумент укажите spark.jars.packages.
- В поле Значение укажите org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0.

В поле Аргумент укажите spark.jars.packages.

В поле Значение укажите org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0.

Нажмите Создать.

Задача Managed Spark начнет выполняться и отобразится на странице инстанса во вкладке Задачи.

Подробнее о развертывании [на официальном сайте](https://spark.apache.org/docs/3.5.1/structured-streaming-kafka-integration.html)на официальном сайте.

## 3. Проверьте логи

На этом шаге вы проверите логи задачи Managed Spark и отображение в них данных из топика Managed Kafka®.

Для продолжения работы убедитесь, что статус задачи Managed Spark изменился на «Завершена».

1. В строке задачи нажмите и выберите Перейти к логам.
2. Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®.

В строке задачи нажмите и выберите Перейти к логам.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®.

Пример данных, полученных из топика Managed Kafka®:

![Данные, полученные из топика Managed Kafka®.](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/kafka-topic-in-spark-logs.png)

## 4. Запустите непрерывное чтение топика Managed Kafka®

На этом шаге вы создадите вторую задачу Managed Spark с использованием скрипта, который будет непрерывно поддерживать соединение с топиком Managed Kafka® и выполнять чтение поступающих в него сообщений.

1. В строке задачи Managed Spark, выполненной ранее, нажмите и выберите Скопировать задачу.
2. В блоке Скрипт приложения в поле Путь к запускаемому файлу укажите путь к файлу kafka_spark_streaming.py.
3. Нажмите Создать.
4. Дождитесь, пока статус задачи изменится на «Выполняется».
5. В строке задачи нажмите и выберите Перейти к логам.
6. Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®. Если в топик Managed Kafka® не поступают новые данные, в логах будут только отправленные ранее сообщения и информация об ожидании.
7. Отправьте новое сообщение в топик Managed Kafka®.
8. Посмотрите в логах задачи Managed Spark информацию о новом сообщении.
9. Задача Managed Spark c данными параметрами будет выполняться, пока вы ее не завершите. Чтобы завершить задачу, в строке задачи нажмите и выберите Остановить.

В строке задачи Managed Spark, выполненной ранее, нажмите и выберите Скопировать задачу.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

В блоке Скрипт приложения в поле Путь к запускаемому файлу укажите путь к файлу kafka_spark_streaming.py.

Нажмите Создать.

Дождитесь, пока статус задачи изменится на «Выполняется».

В строке задачи нажмите и выберите Перейти к логам.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Используйте [фильтр](https://cloud.ru/docs/client-log/ug/topics/working-logs)фильтр, чтобы найти логи, содержащие сообщения из топика Managed Kafka®. Если в топик Managed Kafka® не поступают новые данные, в логах будут только отправленные ранее сообщения и информация об ожидании.

Отправьте новое сообщение в топик Managed Kafka®.

Посмотрите в логах задачи Managed Spark информацию о новом сообщении.

Задача Managed Spark c данными параметрами будет выполняться, пока вы ее не завершите. Чтобы завершить задачу, в строке задачи нажмите и выберите Остановить.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

## Результат

Вы настроили чтение сообщений из топика Managed Kafka® и вывод полученных данных в логи задачи Managed Spark с помощью скриптов.
