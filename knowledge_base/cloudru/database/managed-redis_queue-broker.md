---
title: Использование Managed Redis® как брокера сообщений
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker
topic: database
---
# Использование Managed Redis® как брокера сообщений

С помощью этого руководства вы сконфигурируете Managed Redis® как брокер сообщений, связав его с сервисами publisher и subscriber, работающими на виртуальной машине Ubuntu 22.04.
Вы будете использовать виртуальную сеть VPC и подсети для связи виртуальной машины и сервиса Managed Redis®.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Разверните необходимые ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Настройте окружение на виртуальной машине.
3. [Разработайте сервисы publisher и subscriber](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Разработайте сервисы publisher и subscriber.
4. [Протестируйте работу очереди сообщений с Managed Redis](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Протестируйте работу очереди сообщений с Managed Redis.
5. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Удалите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Разверните необходимые ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Настройте окружение на виртуальной машине.

[Разработайте сервисы publisher и subscriber](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Разработайте сервисы publisher и subscriber.

[Протестируйте работу очереди сообщений с Managed Redis](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Протестируйте работу очереди сообщений с Managed Redis.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)Удалите доступ по SSH для виртуальной машины.

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
DNS-серверы : 8.8.8.8.

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
4. [Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

Название кластера: pub-sub.
Версия Redis: v7.2.11.
vCPU: 2.
RAM: 4.
Подсеть: pub-sub-subnet.

Убедитесь, что в личном кабинете на странице сервиса Managed Redis отображается кластер pub-sub в статусе «Доступен».

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием pub-sub-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название: pub-sub-subnet.
- Адрес: 10.10.1.0/24.
- VPC: pub-sub-VPC.
- DNS-серверы : 8.8.8.8.

Название: pub-sub-subnet.

Адрес: 10.10.1.0/24.

VPC: pub-sub-VPC.

DNS-серверы : 8.8.8.8.

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

[Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

- Название кластера: pub-sub.
- Версия Redis: v7.2.11.
- vCPU: 2.
- RAM: 4.
- Подсеть: pub-sub-subnet.

Название кластера: pub-sub.

Версия Redis: v7.2.11.

vCPU: 2.

RAM: 4.

Подсеть: pub-sub-subnet.

Убедитесь, что в личном кабинете на странице сервиса Managed Redis отображается кластер pub-sub в статусе «Доступен».

## 2. Настройте окружение на виртуальной машине

1. Подключитесь к виртуальной машине pub-sub [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль.
2. [Активируйте сетевой интерфейс](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)Активируйте сетевой интерфейс:
sudo cloud-init cleansudo cloud-init init
3. [Подключитесь к виртуальной машине pub-sub по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине pub-sub по SSH.
4. Обновите систему и установите необходимые пакеты:
sudo apt update && sudo apt upgrade -ysudo apt install -y python3 python3-venv python3-pip

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
python3 python3-venv python3-pip
```

## 3. Разработайте сервисы publisher и subscriber

1. Создайте директорию pubsub и перейдите в неё:
mkdir pubsubcd pubsub
2. Создайте файл publisher.py и вставьте в него следующий код:
nano publisher.py

Содержимое файла:
import argparseimport jsonimport osimport sysimport uuidfrom datetime import datetime, timezone
import redisfrom dotenv import load_dotenv
def build_payload(message: str) -> str: """Return JSON-encoded message with id and timestamp.""" return json.dumps( { "id": str(uuid.uuid4()), "timestamp": datetime.now(timezone.utc).isoformat(), "message": message, } )
def main() -> None: load_dotenv()
 parser = argparse.ArgumentParser(description="Publish a message to Redis.") parser.add_argument( "message", nargs="?", help="Message text; if omitted you will be prompted.", ) parser.add_argument( "--channel", default=os.getenv("CHANNEL", "messages"), help="Redis Pub/Sub channel name (default: messages)", ) args = parser.parse_args()
 msg_text = args.message or input("Enter your message: ")
 redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0") try: r = redis.from_url(redis_url) sent = r.publish(args.channel, build_payload(msg_text)) except redis.ConnectionError as exc: print(f"Redis connection failed: {exc}", file=sys.stderr) sys.exit(1)
 print( f"Published to channel '{args.channel}' " f"(delivered to {sent} subscriber[s])." )
if __name__ == "__main__": main()
3. Создайте файл subscriber.py и вставьте в него следующий код:
nano subscriber.py

Содержимое файла:
import argparseimport jsonimport osimport sys
import redisfrom dotenv import load_dotenv
def pretty_print(raw: bytes) -> None: """Attempt to pretty-print a JSON message; fall back to raw bytes.""" try: obj = json.loads(raw) print(json.dumps(obj, indent=2)) except json.JSONDecodeError: print(f"[non-JSON] {raw!r}")
def main() -> None: load_dotenv()
 parser = argparse.ArgumentParser(description="Subscribe to a Redis channel.") parser.add_argument( "--channel", default=os.getenv("CHANNEL", "messages"), help="Redis Pub/Sub channel name (default: messages)", ) args = parser.parse_args()
 redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0") try: r = redis.from_url(redis_url) pubsub = r.pubsub(ignore_subscribe_messages=True) pubsub.subscribe(args.channel) except redis.ConnectionError as exc: print(f"Redis connection failed: {exc}", file=sys.stderr) sys.exit(1)
 print(f"Subscribed to '{args.channel}'. Waiting for messages… (Ctrl+C to quit)") try: for message in pubsub.listen(): if message and message.get("type") == "message": pretty_print(message["data"]) except KeyboardInterrupt: print("\nExiting subscriber.")
if __name__ == "__main__": main()
4. Создайте файл requirements.txt и вставьте следующее содержимое:
nano requirements.txt

Содержимое файла:
redis==6.2.0python-dotenv==1.0.1
5. Создайте файл .env и вставьте следующее содержимое:
nano .env

Содержимое файла:
REDIS_URL=redis://:<REDIS_PASSWORD>@<REDIS_IP>:6379

Где:

<REDIS_IP> — IP-адрес сервиса Managed Redis®.
<REDIS_PASSWORD> — пароль от кластера Managed Redis®.

IP-адрес и пароль можно найти на странице информации о кластере в блоке Данные для подключения.
6. Создайте и активируйте виртуальное окружение:
python3 -m venv venvsource venv/bin/activate
7. Установите зависимости:
pip install -r requirements.txt

Создайте директорию pubsub и перейдите в неё:

```bash
mkdir
pubsub
cd
pubsub
```

Создайте файл publisher.py и вставьте в него следующий код:

```bash
nano
publisher.py
```

Содержимое файла:

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
import
redis
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
"Publish a message to Redis."
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
"--channel"
,
default
=
os
.
getenv
(
"CHANNEL"
,
"messages"
)
,
help
=
"Redis Pub/Sub channel name (default: messages)"
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
redis_url
=
os
.
getenv
(
"REDIS_URL"
,
"redis://localhost:6379/0"
)
try
:
r
=
redis
.
from_url
(
redis_url
)
sent
=
r
.
publish
(
args
.
channel
,
build_payload
(
msg_text
)
)
except
redis
.
ConnectionError
as
exc
:
print
(
f"Redis connection failed:
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
print
(
f"Published to channel '
{
args
.
channel
}
' "
f"(delivered to
{
sent
}
subscriber[s])."
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

Создайте файл subscriber.py и вставьте в него следующий код:

```bash
nano
subscriber.py
```

Содержимое файла:

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
redis
from
dotenv
import
load_dotenv
def
pretty_print
(
raw
:
bytes
)
-
>
None
:
"""Attempt to pretty-print a JSON message; fall back to raw bytes."""
try
:
obj
=
json
.
loads
(
raw
)
print
(
json
.
dumps
(
obj
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
"Subscribe to a Redis channel."
)
parser
.
add_argument
(
"--channel"
,
default
=
os
.
getenv
(
"CHANNEL"
,
"messages"
)
,
help
=
"Redis Pub/Sub channel name (default: messages)"
,
)
args
=
parser
.
parse_args
(
)
redis_url
=
os
.
getenv
(
"REDIS_URL"
,
"redis://localhost:6379/0"
)
try
:
r
=
redis
.
from_url
(
redis_url
)
pubsub
=
r
.
pubsub
(
ignore_subscribe_messages
=
True
)
pubsub
.
subscribe
(
args
.
channel
)
except
redis
.
ConnectionError
as
exc
:
print
(
f"Redis connection failed:
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
print
(
f"Subscribed to '
{
args
.
channel
}
'. Waiting for messages… (Ctrl+C to quit)"
)
try
:
for
message
in
pubsub
.
listen
(
)
:
if
message
and
message
.
get
(
"type"
)
==
"message"
:
pretty_print
(
message
[
"data"
]
)
except
KeyboardInterrupt
:
print
(
"\nExiting subscriber."
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

Создайте файл requirements.txt и вставьте следующее содержимое:

```bash
nano
requirements.txt
```

Содержимое файла:

```bash
redis
==
6.2
.0
python-dotenv
==
1.0
.1
```

Создайте файл .env и вставьте следующее содержимое:

```bash
nano
.env
```

Содержимое файла:

```bash
REDIS_URL
=
redis://:
<
REDIS_PASSWORD
>
@
<
REDIS_IP
>
:6379
```

Где:

- <REDIS_IP> — IP-адрес сервиса Managed Redis®.
- <REDIS_PASSWORD> — пароль от кластера Managed Redis®.

<REDIS_IP> — IP-адрес сервиса Managed Redis®.

<REDIS_PASSWORD> — пароль от кластера Managed Redis®.

IP-адрес и пароль можно найти на странице информации о кластере в блоке Данные для подключения.

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

## 4. Протестируйте работу очереди сообщений с Managed Redis®

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

![../_images/subscriber.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/subscriber.png)

## 5. Удалите доступ по SSH для виртуальной машины

Так как для настроенного сервиса больше не требуется доступ по SSH, удалите доступ для повышения безопасности.

1. В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину pub-sub, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)на первом шаге.
2. Перейдите в раздел Сетевые параметры.
3. Нажмите на Изменить группы безопасности для публичного IP-адреса.
4. Удалите группу «SSH-access_ru».
5. Нажмите Сохранить.
6. Попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH и убедитесь, что доступ отсутствует.

В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину pub-sub, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__queue-broker)на первом шаге.

Перейдите в раздел Сетевые параметры.

Нажмите на Изменить группы безопасности для публичного IP-адреса.

Удалите группу «SSH-access_ru».

Нажмите Сохранить.

Попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH и убедитесь, что доступ отсутствует.

## Результат

Вы сконфигурировали Managed Redis® как брокер сообщений, связали его с сервисами publisher и subscriber, работающими на виртуальной машине.
Вы получили опыт работы с очередями сообщений и безопасным доступом.
