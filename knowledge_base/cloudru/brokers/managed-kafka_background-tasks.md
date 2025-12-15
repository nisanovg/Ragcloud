---
title: Использование Managed Kafka® для фоновой обработки задач
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks
topic: brokers
---
# Использование Managed Kafka® для фоновой обработки задач

С помощью этого руководства вы сконфигурируете Managed Kafka® как брокер сообщений, связав его с сервисами publisher и subscriber, работающими на виртуальной машине Ubuntu 22.04.
Вы будете использовать виртуальную сеть VPC и подсети для связи виртуальной машины и сервиса Managed Kafka®.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka®.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka®.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Разверните необходимые ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Настройте окружение на виртуальной машине.
3. [Разработайте сервисы publisher и subscriber](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Разработайте сервисы publisher и subscriber.
4. [Протестируйте работу очереди сообщений](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Протестируйте работу очереди сообщений.
5. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Удалите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Разверните необходимые ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Настройте окружение на виртуальной машине.

[Разработайте сервисы publisher и subscriber](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Разработайте сервисы publisher и subscriber.

[Протестируйте работу очереди сообщений](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Протестируйте работу очереди сообщений.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)Удалите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

## 1. Разверните необходимые ресурсы в облаке

1. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием pub-sub-VPC.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

Название: pub-sub-subnet.
Адрес: 10.10.1.0/24.
VPC: pub-sub-VPC.
DNS-серверы: 8.8.8.8

Убедитесь, что в личном кабинете на странице сервиса VPC:

отображается сеть pub-sub-VPC;
количество подсетей — 1;
подсеть pub-sub-subnet доступна.
3. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: pub-sub.
Образ: Публичные → Ubuntu 22.04.
Метод аутентификации: SSH-ключ и пароль.
SSH-ключ: ваш SSH-ключ.
Пароль: ваш пароль.
Имя хоста: pub-sub.
Подключить публичный IP: включено.
Тип IP-адреса: Прямой.
Группы безопасности: SSH-access_ru.AZ-1.
Подсеть: pub-sub-subnet.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина pub-sub в статуса «Запущена».
4. [Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/guides__cluster-creation)Создайте кластер Managed Kafka® со следующими параметрами:

Название: pub-sub.
Версия Kafka: 3.9.0.
Брокеры: 1.
vCPU: 4.
RAM: 16.
Подсеть: pub-sub-subnet.

Убедитесь, что в личном кабинете на странице сервиса Managed Kafka® отображается кластер pub-sub в статусе «Доступен».

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием pub-sub-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название: pub-sub-subnet.
- Адрес: 10.10.1.0/24.
- VPC: pub-sub-VPC.
- DNS-серверы: 8.8.8.8

Название: pub-sub-subnet.

Адрес: 10.10.1.0/24.

VPC: pub-sub-VPC.

DNS-серверы: 8.8.8.8

Убедитесь, что в личном кабинете на странице сервиса VPC:

- отображается сеть pub-sub-VPC;
- количество подсетей — 1;
- подсеть pub-sub-subnet доступна.

отображается сеть pub-sub-VPC;

количество подсетей — 1;

подсеть pub-sub-subnet доступна.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: pub-sub.
- Образ: Публичные → Ubuntu 22.04.
- Метод аутентификации: SSH-ключ и пароль.
- SSH-ключ: ваш SSH-ключ.
- Пароль: ваш пароль.
- Имя хоста: pub-sub.
- Подключить публичный IP: включено.
- Тип IP-адреса: Прямой.
- Группы безопасности: SSH-access_ru.AZ-1.
- Подсеть: pub-sub-subnet.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.

Название: pub-sub.

Образ: Публичные → Ubuntu 22.04.

Метод аутентификации: SSH-ключ и пароль.

SSH-ключ: ваш SSH-ключ.

Пароль: ваш пароль.

Имя хоста: pub-sub.

Подключить публичный IP: включено.

Тип IP-адреса: Прямой.

Группы безопасности: SSH-access_ru.AZ-1.

Подсеть: pub-sub-subnet.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина pub-sub в статуса «Запущена».

[Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/guides__cluster-creation)Создайте кластер Managed Kafka® со следующими параметрами:

- Название: pub-sub.
- Версия Kafka: 3.9.0.
- Брокеры: 1.
- vCPU: 4.
- RAM: 16.
- Подсеть: pub-sub-subnet.

Название: pub-sub.

Версия Kafka: 3.9.0.

Брокеры: 1.

vCPU: 4.

RAM: 16.

Подсеть: pub-sub-subnet.

Убедитесь, что в личном кабинете на странице сервиса Managed Kafka® отображается кластер pub-sub в статусе «Доступен».

## 2. Настройте окружение на виртуальной машине

1. Подключитесь к виртуальной машине pub-sub [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль.
2. [Активируйте сетевой интерфейс](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)Активируйте сетевой интерфейс:
sudo cloud-init cleansudo cloud-init init
3. [Подключитесь к виртуальной машине pub-sub по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине pub-sub по SSH.
4. Обновите систему и установите необходимые пакеты:
sudo apt update && sudo apt upgrade -ysudo apt install -y python3 python3-venv python3-pip kafkacat

Подключитесь к виртуальной машине pub-sub [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль.

[Активируйте сетевой интерфейс](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)Активируйте сетевой интерфейс:

```bash
sudo
cloud-init clean
sudo
cloud-init init
```

[Подключитесь к виртуальной машине pub-sub по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине pub-sub по SSH.

Обновите систему и установите необходимые пакеты:

```bash
sudo
apt
update
&&
sudo
apt
upgrade
-y
sudo
apt
install
-y
python3 python3-venv python3-pip kafkacat
```

## 3. Разработайте сервисы publisher и subscriber

1. Создайте директорию «pubsub» и перейдите в нее:
mkdir pubsubcd pubsub
2. Создайте файл publisher.py с помощью команды:
nano publisher.py
3. Скопируйте код в файл:
import argparseimport jsonimport osimport sysimport uuidfrom datetime import datetime, timezone
from kafka import KafkaProducerfrom dotenv import load_dotenv

def build_payload(message: str) -> str: """Return JSON-encoded message with id and timestamp.""" return json.dumps( { "id": str(uuid.uuid4()), "timestamp": datetime.now(timezone.utc).isoformat(), "message": message, } )

def main() -> None: load_dotenv()
 parser = argparse.ArgumentParser(description="Publish a message to Kafka.") parser.add_argument( "message", nargs="?", help="Message text; if omitted you will be prompted.", ) parser.add_argument( "--topic", default=os.getenv("TOPIC", "messages"), help="Kafka topic name (default: messages)", )
 args = parser.parse_args() msg_text = args.message or input("Enter your message: ")
 kafka_brokers = os.getenv("KAFKA_BROKERS", "").split(",") kafka_writer_username = os.getenv("KAFKA_WRITER_USERNAME") kafka_writer_password = os.getenv("KAFKA_WRITER_PASSWORD")
 if not kafka_brokers or not kafka_writer_username or not kafka_writer_password: print("Kafka brokers, writer username and writer password are required") sys.exit(1)
 try: producer_config = { 'bootstrap_servers': kafka_brokers, 'value_serializer': lambda v: v.encode('utf-8'), 'security_protocol': 'SASL_PLAINTEXT', # Changed from SASL_SSL 'sasl_mechanism': 'SCRAM-SHA-512', 'sasl_plain_username': kafka_writer_username, 'sasl_plain_password': kafka_writer_password, 'api_version': (2, 0, 0), }
 print(f"Connecting to Kafka brokers: {kafka_brokers}") producer = KafkaProducer(**producer_config)
 print(f"Sending message to topic: {args.topic}") future = producer.send(args.topic, build_payload(msg_text)) result = future.get(timeout=30)
 producer.flush() producer.close()
 print(f"Published to topic '{args.topic}' (partition: {result.partition}, offset: {result.offset}).")
 except Exception as exc: print(f"Kafka connection failed: {exc}", file=sys.stderr) sys.exit(1)

if __name__ == "__main__": main()
4. Создайте файл subscriber.py с помощью команды:
nano subscriber.py
5. Скопируйте код в файл:
import argparseimport jsonimport osimport sys
from kafka import KafkaConsumer, TopicPartitionfrom dotenv import load_dotenv

def pretty_print(raw: str) -> None: try: print(json.dumps(json.loads(raw), indent=2)) except json.JSONDecodeError: print(f"[non-JSON] {raw!r}")

def main() -> None: load_dotenv()
 parser = argparse.ArgumentParser(description="Subscribe without group coordination.") parser.add_argument("--topic", default=os.getenv("TOPIC", "messages")) args = parser.parse_args()
 brokers = os.getenv("KAFKA_BROKERS", "").split(",") username = os.getenv("KAFKA_READER_USERNAME") password = os.getenv("KAFKA_READER_PASSWORD")
 if not kafka_brokers or not kafka_writer_username or not kafka_writer_password: print("Kafka brokers, writer username and writer password are required") sys.exit(1)
 try: consumer = KafkaConsumer( bootstrap_servers=brokers, security_protocol="SASL_PLAINTEXT", sasl_mechanism="SCRAM-SHA-512", sasl_plain_username=username, sasl_plain_password=password, value_deserializer=lambda v: v.decode("utf-8"), auto_offset_reset="earliest", enable_auto_commit=False, group_id=None, # no group join api_version=(2, 0, 0), )
 parts = consumer.partitions_for_topic(args.topic) if not parts: print(f"Topic '{args.topic}' not found or no partitions.", file=sys.stderr) sys.exit(1)
 assignment = [TopicPartition(args.topic, p) for p in sorted(parts)] consumer.assign(assignment) consumer.seek_to_beginning(*assignment)
 print(f"Assigned without group to partitions: {assignment}") for msg in consumer: pretty_print(msg.value)
 except Exception as exc: print(f"Kafka connection failed: {exc}", file=sys.stderr) sys.exit(1)

if __name__ == "__main__": main()
6. Создайте файл requirements.txt с помощью команды:
nano requirements.txt
7. Скопируйте код в файл:
kafka-python==2.0.2python-dotenv==1.0.1
8. Создайте файл .env с помощью команды:
nano .env
9. Скопируйте код в файл:
KAFKA_BROKERS=<KAFKA_BROKER_IP>:9094KAFKA_WRITER_USERNAME=<KAFKA_WRITER_USERNAME>KAFKA_WRITER_PASSWORD=<KAFKA_WRITER_PASSWORD>KAFKA_READER_USERNAME=<KAFKA_READER_USERNAME>KAFKA_READER_PASSWORD=<KAFKA_READER_PASSWORD>TOPIC=messagesGROUP_ID=subscriber-group

Где:

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
<KAFKA_WRITER_USERNAME> — логин от кластера Managed Kafka® с ролью Writer.
<KAFKA_WRITER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Writer.
<KAFKA_READER_USERNAME> — логин от кластера Managed Kafka® с ролью Reader.
<KAFKA_READER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Reader.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.
10. Создайте и активируйте виртуальное окружение:
python3 -m venv venvsource venv/bin/activate
11. Установите зависимости:
pip install -r requirements.txt
12. Создайте топик:
echo "test message" | kafkacat -P -b <KAFKA_BROKER_IP>:9094 -X security.protocol=SASL_PLAINTEXT -X sasl.mechanism=SCRAM-SHA-512 -X sasl.username=<KAFKA_ADMIN_USERNAME> -X sasl.password=<KAFKA_ADMIN_PASSWORD> -t messages

Где:

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
<KAFKA_ADMIN_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.
<KAFKA_ADMIN_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.

Создайте директорию «pubsub» и перейдите в нее:

```bash
mkdir
pubsub
cd
pubsub
```

Создайте файл publisher.py с помощью команды:

```bash
nano
publisher.py
```

Скопируйте код в файл:

```bash
import
argparse
import
json
import
os
import
sys
import
uuid
from
datetime
import
datetime
,
timezone
from
kafka
import
KafkaProducer
from
dotenv
import
load_dotenv
def
build_payload
(
message
:
str
)
-
>
str
:
"""Return JSON-encoded message with id and timestamp."""
return
json
.
dumps
(
{
"id"
:
str
(
uuid
.
uuid4
(
)
)
,
"timestamp"
:
datetime
.
now
(
timezone
.
utc
)
.
isoformat
(
)
,
"message"
:
message
,
}
)
def
main
(
)
-
>
None
:
load_dotenv
(
)
parser
=
argparse
.
ArgumentParser
(
description
=
"Publish a message to Kafka."
)
parser
.
add_argument
(
"message"
,
nargs
=
"?"
,
help
=
"Message text; if omitted you will be prompted."
,
)
parser
.
add_argument
(
"--topic"
,
default
=
os
.
getenv
(
"TOPIC"
,
"messages"
)
,
help
=
"Kafka topic name (default: messages)"
,
)
args
=
parser
.
parse_args
(
)
msg_text
=
args
.
message
or
input
(
"Enter your message: "
)
kafka_brokers
=
os
.
getenv
(
"KAFKA_BROKERS"
,
""
)
.
split
(
","
)
kafka_writer_username
=
os
.
getenv
(
"KAFKA_WRITER_USERNAME"
)
kafka_writer_password
=
os
.
getenv
(
"KAFKA_WRITER_PASSWORD"
)
if
not
kafka_brokers
or
not
kafka_writer_username
or
not
kafka_writer_password
:
print
(
"Kafka brokers, writer username and writer password are required"
)
sys
.
exit
(
1
)
try
:
producer_config
=
{
'bootstrap_servers'
:
kafka_brokers
,
'value_serializer'
:
lambda
v
:
v
.
encode
(
'utf-8'
)
,
'security_protocol'
:
'SASL_PLAINTEXT'
,
# Changed from SASL_SSL
'sasl_mechanism'
:
'SCRAM-SHA-512'
,
'sasl_plain_username'
:
kafka_writer_username
,
'sasl_plain_password'
:
kafka_writer_password
,
'api_version'
:
(
2
,
0
,
0
)
,
}
print
(
f"Connecting to Kafka brokers:
{
kafka_brokers
}
"
)
producer
=
KafkaProducer
(
**
producer_config
)
print
(
f"Sending message to topic:
{
args
.
topic
}
"
)
future
=
producer
.
send
(
args
.
topic
,
build_payload
(
msg_text
)
)
result
=
future
.
get
(
timeout
=
30
)
producer
.
flush
(
)
producer
.
close
(
)
print
(
f"Published to topic '
{
args
.
topic
}
' (partition:
{
result
.
partition
}
, offset:
{
result
.
offset
}
)."
)
except
Exception
as
exc
:
print
(
f"Kafka connection failed:
{
exc
}
"
,
file
=
sys
.
stderr
)
sys
.
exit
(
1
)
if
__name__
==
"__main__"
:
main
(
)
```

Создайте файл subscriber.py с помощью команды:

```bash
nano
subscriber.py
```

Скопируйте код в файл:

```bash
import
argparse
import
json
import
os
import
sys
from
kafka
import
KafkaConsumer
,
TopicPartition
from
dotenv
import
load_dotenv
def
pretty_print
(
raw
:
str
)
-
>
None
:
try
:
print
(
json
.
dumps
(
json
.
loads
(
raw
)
,
indent
=
2
)
)
except
json
.
JSONDecodeError
:
print
(
f"[non-JSON]
{
raw
!r
}
"
)
def
main
(
)
-
>
None
:
load_dotenv
(
)
parser
=
argparse
.
ArgumentParser
(
description
=
"Subscribe without group coordination."
)
parser
.
add_argument
(
"--topic"
,
default
=
os
.
getenv
(
"TOPIC"
,
"messages"
)
)
args
=
parser
.
parse_args
(
)
brokers
=
os
.
getenv
(
"KAFKA_BROKERS"
,
""
)
.
split
(
","
)
username
=
os
.
getenv
(
"KAFKA_READER_USERNAME"
)
password
=
os
.
getenv
(
"KAFKA_READER_PASSWORD"
)
if
not
kafka_brokers
or
not
kafka_writer_username
or
not
kafka_writer_password
:
print
(
"Kafka brokers, writer username and writer password are required"
)
sys
.
exit
(
1
)
try
:
consumer
=
KafkaConsumer
(
bootstrap_servers
=
brokers
,
security_protocol
=
"SASL_PLAINTEXT"
,
sasl_mechanism
=
"SCRAM-SHA-512"
,
sasl_plain_username
=
username
,
sasl_plain_password
=
password
,
value_deserializer
=
lambda
v
:
v
.
decode
(
"utf-8"
)
,
auto_offset_reset
=
"earliest"
,
enable_auto_commit
=
False
,
group_id
=
None
,
# no group join
api_version
=
(
2
,
0
,
0
)
,
)
parts
=
consumer
.
partitions_for_topic
(
args
.
topic
)
if
not
parts
:
print
(
f"Topic '
{
args
.
topic
}
' not found or no partitions."
,
file
=
sys
.
stderr
)
sys
.
exit
(
1
)
assignment
=
[
TopicPartition
(
args
.
topic
,
p
)
for
p
in
sorted
(
parts
)
]
consumer
.
assign
(
assignment
)
consumer
.
seek_to_beginning
(
*
assignment
)
print
(
f"Assigned without group to partitions:
{
assignment
}
"
)
for
msg
in
consumer
:
pretty_print
(
msg
.
value
)
except
Exception
as
exc
:
print
(
f"Kafka connection failed:
{
exc
}
"
,
file
=
sys
.
stderr
)
sys
.
exit
(
1
)
if
__name__
==
"__main__"
:
main
(
)
```

Создайте файл requirements.txt с помощью команды:

```bash
nano
requirements.txt
```

Скопируйте код в файл:

```bash
kafka-python
==
2.0
.2
python-dotenv
==
1.0
.1
```

Создайте файл .env с помощью команды:

```bash
nano
.env
```

Скопируйте код в файл:

```bash
KAFKA_BROKERS
=
<
KAFKA_BROKER_IP
>
:9094
KAFKA_WRITER_USERNAME
=
<
KAFKA_WRITER_USERNAME
>
KAFKA_WRITER_PASSWORD
=
<
KAFKA_WRITER_PASSWORD
>
KAFKA_READER_USERNAME
=
<
KAFKA_READER_USERNAME
>
KAFKA_READER_PASSWORD
=
<
KAFKA_READER_PASSWORD
>
TOPIC
=
messages
GROUP_ID
=
subscriber-group
```

Где:

- <KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
- <KAFKA_WRITER_USERNAME> — логин от кластера Managed Kafka® с ролью Writer.
- <KAFKA_WRITER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Writer.
- <KAFKA_READER_USERNAME> — логин от кластера Managed Kafka® с ролью Reader.
- <KAFKA_READER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Reader.

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.

<KAFKA_WRITER_USERNAME> — логин от кластера Managed Kafka® с ролью Writer.

<KAFKA_WRITER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Writer.

<KAFKA_READER_USERNAME> — логин от кластера Managed Kafka® с ролью Reader.

<KAFKA_READER_PASSWORD> — пароль от кластера Managed Kafka® с ролью Reader.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.

Создайте и активируйте виртуальное окружение:

```bash
python3
-m
venv venv
source
venv/bin/activate
```

Установите зависимости:

```bash
pip
install
-r
requirements.txt
```

Создайте топик:

```bash
echo
"test message"
|
kafkacat
-P
-b
<
KAFKA_BROKER_IP
>
:9094
-X
security.protocol
=
SASL_PLAINTEXT
-X
sasl.mechanism
=
SCRAM-SHA-512
-X
sasl.username
=
<
KAFKA_ADMIN_USERNAME
>
-X
sasl.password
=
<
KAFKA_ADMIN_PASSWORD
>
-t
messages
```

Где:

- <KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
- <KAFKA_ADMIN_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.
- <KAFKA_ADMIN_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.

<KAFKA_ADMIN_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.

<KAFKA_ADMIN_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.

## 4. Протестируйте работу очереди сообщений с Managed Kafka®

1. Запустите сервис subscriber:
python subscriber.py
2. Откройте новое окно терминала, не закрывая текущий терминал.
3. [Подключитесь к виртуальной машине pub-sub по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине pub-sub по SSH.
4. Перейдите в директорию с сервисами:
cd pubsub
5. Активируйте виртуальное окружение:
source venv/bin/activate
6. Отправьте сообщение в очередь:
python publisher.py "Hello from Ubuntu!"
7. Переключитесь обратно на терминал 1 и проверьте, что сообщение успешно получено.

Запустите сервис subscriber:

```bash
python subscriber.py
```

Откройте новое окно терминала, не закрывая текущий терминал.

[Подключитесь к виртуальной машине pub-sub по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине pub-sub по SSH.

Перейдите в директорию с сервисами:

```bash
cd
pubsub
```

Активируйте виртуальное окружение:

```bash
source
venv/bin/activate
```

Отправьте сообщение в очередь:

```bash
python publisher.py
"Hello from Ubuntu!"
```

Переключитесь обратно на терминал 1 и проверьте, что сообщение успешно получено.

## 5. Удалите доступ по SSH для виртуальной машины

Так как для настроенного сервиса больше не требуется доступ по SSH, удалите доступ для повышения безопасности.

1. В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину pub-sub, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)на первом шаге.
2. Перейдите в раздел Сетевые параметры.
3. Нажмите на Изменить группы безопасности для публичного IP-адреса.
4. Удалите группу «SSH-access_ru».
5. Нажмите Сохранить.
6. Попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH и убедитесь, что доступ отсутствует.

В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину pub-sub, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__background-tasks)на первом шаге.

Перейдите в раздел Сетевые параметры.

Нажмите на Изменить группы безопасности для публичного IP-адреса.

Удалите группу «SSH-access_ru».

Нажмите Сохранить.

Попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH и убедитесь, что доступ отсутствует.

## Результат

Вы сконфигурировали Managed Kafka® для фоновой обработки задач, связали его с сервисами publisher и subscriber, работающими на виртуальной машине.
Вы получили опыт работы с очередями сообщений и безопасным доступом.
