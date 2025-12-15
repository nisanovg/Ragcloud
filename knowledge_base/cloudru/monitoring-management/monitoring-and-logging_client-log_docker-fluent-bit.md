---
title: Передача логов с виртуальной машины с помощью Docker-контейнера плагина Fluent Bit
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit
topic: monitoring-management
---
# Передача логов с виртуальной машины с помощью Docker-контейнера плагина Fluent Bit

Передача логов в сервис «Клиентское логирование» с помощью Docker-контейнера доступна для разных операционных систем.
В этой инструкции мы приводим пример настройки отправки логов на созданной виртуальной машине.

## Перед началом работы

1. [Создайте и настройте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте и настройте лог-группу.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

в блоке Проект — «Пользователь сервисов»;
в блоке Сервисы — «logaas.writer».
3. Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu 22.04.
5. [Подключитесь к созданной виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к созданной виртуальной машине по SSH.

[Создайте и настройте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте и настройте лог-группу.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

- в блоке Проект — «Пользователь сервисов»;
- в блоке Сервисы — «logaas.writer».

в блоке Проект — «Пользователь сервисов»;

в блоке Сервисы — «logaas.writer».

Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu 22.04.

[Подключитесь к созданной виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к созданной виртуальной машине по SSH.

## Шаг 1. Установка Docker

1. Установите необходимые зависимости:
sudo apt updatesudo apt install ca-certificates curl gnupg software-properties-common
2. Установите ключ GPG:
sudo mkdir -p /etc/apt/keyringscurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
3. Добавьте Docker-репозиторий:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
4. Установите Docker:
sudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
5. Запустите Docker как службу:
sudo systemctl enable docker # Enable auto-start on bootsudo systemctl start docker # Start Docker immediately
6. Проверьте, что Docker запущен:
sudo docker run hello-world

При проверке появится сообщение c подтверждением успешного запуска.

Установите необходимые зависимости:

```bash
sudo
apt
update
sudo
apt
install
ca-certificates
curl
gnupg software-properties-common
```

Установите ключ GPG:

```bash
sudo
mkdir
-p
/etc/apt/keyrings
curl
-fsSL
https://download.docker.com/linux/ubuntu/gpg
|
sudo
gpg
--dearmor
-o
/etc/apt/keyrings/docker.gpg
```

Добавьте Docker-репозиторий:

```bash
echo
"deb [arch=
$(
dpkg --print-architecture
)
signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu
$(
lsb_release
-cs
)
stable"
|
sudo
tee
/etc/apt/sources.list.d/docker.list
>
/dev/null
```

Установите Docker:

```bash
sudo
apt
update
sudo
apt
install
docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Запустите Docker как службу:

```bash
sudo
systemctl
enable
docker
# Enable auto-start on boot
sudo
systemctl start
docker
# Start Docker immediately
```

Проверьте, что Docker запущен:

```bash
sudo
docker
run hello-world
```

При проверке появится сообщение c подтверждением успешного запуска.

## Шаг 2. Определение структуры проекта

Для записи логов через Docker-образ создайте простой проект, который будет включать в себя:

- [генератор логов](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)генератор логов,
- [настройки программы логирования fluent-bit](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)настройки программы логирования fluent-bit,
- [файл docker-compose](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)файл docker-compose, который все объединит.

[генератор логов](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)генератор логов,

[настройки программы логирования fluent-bit](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)настройки программы логирования fluent-bit,

[файл docker-compose](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__docker-fluent-bit)файл docker-compose, который все объединит.

Корневая рабочая директория проекта — /usr/local/bin/myproject:

```bash
.
├── app
│ ├── Dockerfile
│ └── log_generator.py
├── docker-compose.yml
└── fluent-bit-settings
├── fluent-bit.conf
├── logaas.so
├── parsers.conf
└── plugins.conf
```

## Шаг 3. Создание приложения — тестового источника логов

1. Создайте рабочую директорию /usr/local/bin/myproject/app, в которой нужно описать структуру приложения и файлы с настройками:
.├── app│ ├── Dockerfile│ └── log_generator.py
2. Создайте скрипт-генератор логов log_generator.py:
import randomimport jsonimport socketimport osfrom datetime import datetime, timezoneimport time
LOG_LEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']MESSAGE_TEMPLATES = [ "Data received [ID: {id}]", "Processing request from user {user}", "Failed to connect to database {db}", "Connection timeout after {sec} seconds", "File {file} not found", "Authentication failed for {service}", "Received {size} bytes from {ip}", "Task {task} completed in {ms}ms", "Cache miss for key {key}", "Starting backup process {job_id}"]

def generate_message(): template = random.choice(MESSAGE_TEMPLATES) replacements = { 'id': lambda: random.randint(1000, 9999), 'user': lambda: f"user_{random.randint(100, 999)}", 'db': lambda: random.choice(["primary", "replica", "archive"]), 'sec': lambda: random.randint(1, 30), 'file': lambda: f"/var/log/{random.choice(['app', 'system', 'auth'])}.log", 'service': lambda: random.choice(["API", "SSH", "Database"]), 'size': lambda: random.randint(512, 4096), 'ip': lambda: ".".join(map(str, [random.randint(1, 255) for _ in range(4)])), 'task': lambda: random.choice(["cleanup", "backup", "sync"]), 'ms': lambda: random.randint(100, 5000), 'key': lambda: hex(random.getrandbits(128))[2:10], 'job_id': lambda: f"JOB-{random.randint(10000, 99999)}" }
 return template.format(**{k: v() for k, v in replacements.items() if k in template})

def generate_log(): return { "timestamp": datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'), "level": random.choice(LOG_LEVELS), "labels": { "app": "logger", "host": socket.gethostname(), "pid": os.getpid(), "random": random.randint(1, 1000) }, "message": generate_message() }

if __name__ == "__main__": while True: log_entry = generate_log() print(json.dumps(log_entry)) time.sleep(random.uniform(0.1, 2.0))
3. Для запуска этого приложения создайте файл Dockerfile:
FROM python:3.13-alpineWORKDIR /appCOPY log_generator.py .CMD ["python", "./log_generator.py"]
4. Соберите образ:
sudo docker build -t my-app:1.0 .
5. Запустите контейнер на основе собранного образа:
sudo docker run -d --name my_running_app1 my-app:1.0

Будет выдан ID запущенного контейнера — например, 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b.
По этому ID вы сможете посмотреть логи.
6. Запросите логи одним из способов:

по имени контейнера:
sudo docker logs -f my_running_app1

по ID контейнера:
sudo docker logs -f 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b

Создайте рабочую директорию /usr/local/bin/myproject/app, в которой нужно описать структуру приложения и файлы с настройками:

```bash
.
├── app
│ ├── Dockerfile
│ └── log_generator.py
```

Создайте скрипт-генератор логов log_generator.py:

```bash
import
random
import
json
import
socket
import
os
from datetime
import
datetime, timezone
import
time
LOG_LEVELS
=
[
'DEBUG'
,
'INFO'
,
'WARN'
,
'ERROR'
,
'FATAL'
]
MESSAGE_TEMPLATES
=
[
"Data received [ID: {id}]"
,
"Processing request from user {user}"
,
"Failed to connect to database {db}"
,
"Connection timeout after {sec} seconds"
,
"File {file} not found"
,
"Authentication failed for {service}"
,
"Received {size} bytes from {ip}"
,
"Task {task} completed in {ms}ms"
,
"Cache miss for key {key}"
,
"Starting backup process {job_id}"
]
def generate_message
(
)
:
template
=
random.choice
(
MESSAGE_TEMPLATES
)
replacements
=
{
'id'
:
lambda: random.randint
(
1000
,
9999
)
,
'user'
:
lambda: f
"user_{random.randint(100, 999)}"
,
'db'
:
lambda: random.choice
(
[
"primary"
,
"replica"
,
"archive"
]
)
,
'sec'
:
lambda: random.randint
(
1
,
30
)
,
'file'
:
lambda: f
"/var/log/{random.choice(['app', 'system', 'auth'])}.log"
,
'service'
:
lambda: random.choice
(
[
"API"
,
"SSH"
,
"Database"
]
)
,
'size'
:
lambda: random.randint
(
512
,
4096
)
,
'ip'
:
lambda:
"."
.join
(
map
(
str,
[
random.randint
(
1
,
255
)
for
_
in
range
(
4
)
]
))
,
'task'
:
lambda: random.choice
(
[
"cleanup"
,
"backup"
,
"sync"
]
)
,
'ms'
:
lambda: random.randint
(
100
,
5000
)
,
'key'
:
lambda: hex
(
random.getrandbits
(
128
))
[
2
:10
]
,
'job_id'
:
lambda: f
"JOB-{random.randint(10000, 99999)}"
}
return
template.format
(
**
{
k: v
(
)
for
k,
v
in
replacements.items
(
)
if
k
in
template
}
)
def generate_log
(
)
:
return
{
"timestamp"
:
datetime.now
(
timezone.utc
)
.isoformat
(
timespec
=
'milliseconds'
)
.replace
(
'+00:00'
,
'Z'
)
,
"level"
:
random.choice
(
LOG_LEVELS
)
,
"labels"
:
{
"app"
:
"logger"
,
"host"
:
socket.gethostname
(
)
,
"pid"
:
os.getpid
(
)
,
"random"
:
random.randint
(
1
,
1000
)
}
,
"message"
:
generate_message
(
)
}
if
__name__
==
"__main__"
:
while
True:
log_entry
=
generate_log
(
)
print
(
json.dumps
(
log_entry
))
time.sleep
(
random.uniform
(
0.1
,
2.0
))
```

Для запуска этого приложения создайте файл Dockerfile:

```bash
FROM python:3.13-alpine
WORKDIR /app
COPY log_generator.py
.
CMD
[
"python"
,
"./log_generator.py"
]
```

Соберите образ:

```bash
sudo
docker
build
-t
my-app:1.0
.
```

Запустите контейнер на основе собранного образа:

```bash
sudo
docker
run
-d
--name
my_running_app1 my-app:1.0
```

Будет выдан ID запущенного контейнера — например, 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b.
По этому ID вы сможете посмотреть логи.

Запросите логи одним из способов:

- по имени контейнера:
sudo docker logs -f my_running_app1
- по ID контейнера:
sudo docker logs -f 41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b

по имени контейнера:

```bash
sudo
docker
logs
-f
my_running_app1
```

по ID контейнера:

```bash
sudo
docker
logs
-f
41f8a276da1dc3b6f03bd98f55e13786c33937a453c40a07701c94fd10d0433b
```

Чтобы остановить запущенный контейнер:

1. Выведите список контейнеров:
sudo docker ps

Список запущенных контейнеров отображается в виде:
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMESe75bb4ff0ca0 my-app:1.0 "python ./log_genera…" 5 seconds ago Up 5 seconds my_running_app1
2. Остановите запущенный контейнер одним из способов:

по имени контейнера:
sudo docker stop my_running_app1

по ID контейнера:
sudo docker stop e75bb4ff0ca0

Выведите список контейнеров:

```bash
sudo
docker
ps
```

Список запущенных контейнеров отображается в виде:

```bash
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
e75bb4ff0ca0 my-app:1.0
"python ./log_genera…"
5
seconds ago Up
5
seconds my_running_app1
```

Остановите запущенный контейнер одним из способов:

- по имени контейнера:
sudo docker stop my_running_app1
- по ID контейнера:
sudo docker stop e75bb4ff0ca0

по имени контейнера:

```bash
sudo
docker
stop my_running_app1
```

по ID контейнера:

```bash
sudo
docker
stop e75bb4ff0ca0
```

Запущенный контейнер можно удалить по его ID:

```bash
sudo
docker
rm
e75bb4ff0ca0
```

## Шаг 4. Настройка Fluent Bit для передачи логов

Содержимое директории с настройками fluent-bit будет иметь следующий вид:

```bash
└── fluent-bit-settings
├── fluent-bit.conf - файл с общими настройками
├── logaas.so - бинарная библиотека для записи логов в сервис
"Клиентское логирование"
├── parsers.conf - файл с настройками парсеров
└── plugins.conf - пути к используемым плагинам
```

1. Создайте директорию /usr/local/bin/myproject/fluent-bit-settings:
sudo mkdir /usr/local/bin/myproject/fluent-bit-settings
2. Скачайте плагин logaas.so, который вместе с fluent-bit будет отвечать за отправку логов в сервис «Клиентское логирование»:
sudo wget https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaas.so -O /usr/local/bin/myproject/fluent-bit-settings/logaas.so
3. Создайте файлы настроек:
sudo touch /usr/local/bin/myproject/fluent-bit-settings/{fluent-bit,parsers,plugins}.conf
4. Откройте файл с настройками плагинов plugins.conf с помощью редактора nano:
sudo nano /usr/local/bin/myproject/fluent-bit-settings/plugins.conf

В файл добавьте путь до плагина logaas.so:
[PLUGINS] Path /etc/fluent-bit/logaas.so
5. Откройте файл fluent-bit.conf:
sudo nano /usr/local/bin/myproject/fluent-bit-settings/fluent-bit.conf

Добавьте в него данные в виде:
[SERVICE] Daemon Off Flush 1 Log_Level info Plugins_File plugins.conf Parsers_File parsers.conf
[INPUT] Name tail Path <path-to-log/logfile.log> Parser docker
[OUTPUT] Name logaas Match * address https://console.cloud.ru/ iam_address https://auth.iam.sbercloud.ru/ iam_client_id REPLACE_TO_LOGGING_SA_KEY_ID iam_client_secret REPLACE_TO_LOGGING_SA_SECRET default_project_id REPLACE_TO_PROJECT_ID default_group_id REPLACE_TO_LOG_GROUP_ID default_labels {"some_label":"default_value"}

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.
В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.
Измените файл, подставив в него свои данные:

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».
REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

Пример для настройки отправки логов, собираемых из приложения — тестового источника логов:
[SERVICE] Daemon Off Flush 1 Log_Level info Plugins_File plugins.conf Parsers_File parsers.conf
[INPUT] Name tail Path /var/log/myapp.log Parser docker
[OUTPUT] Name logaas Match * address https://console.cloud.ru/ iam_address https://auth.iam.sbercloud.ru/ iam_client_id 30dce000000000000000000000f6b8e0 iam_client_secret 18a4f000000000000000000000098414 default_project_id 00000000-1111-2222-3333-444444444444 default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee default_labels {"source":"docker-image", "logger":"fluentbit"}
6. Откройте файл parsers.conf:
sudo nano /usr/local/bin/myproject/fluent-bit-settings/parsers.conf

Добавьте в файл данные:
[PARSER] Name docker Format json Time_Key time Time_Format %Y-%m-%dT%H:%M:%S.%L Time_Keep On Time_System_Timezone true

Создайте директорию /usr/local/bin/myproject/fluent-bit-settings:

```bash
sudo
mkdir
/usr/local/bin/myproject/fluent-bit-settings
```

Скачайте плагин logaas.so, который вместе с fluent-bit будет отвечать за отправку логов в сервис «Клиентское логирование»:

```bash
sudo
wget
https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaas.so
-O
/usr/local/bin/myproject/fluent-bit-settings/logaas.so
```

Создайте файлы настроек:

```bash
sudo
touch
/usr/local/bin/myproject/fluent-bit-settings/
{
fluent-bit,parsers,plugins
}
.conf
```

Откройте файл с настройками плагинов plugins.conf с помощью редактора nano:

```bash
sudo
nano
/usr/local/bin/myproject/fluent-bit-settings/plugins.conf
```

В файл добавьте путь до плагина logaas.so:

```bash
[
PLUGINS
]
Path /etc/fluent-bit/logaas.so
```

Откройте файл fluent-bit.conf:

```bash
sudo
nano
/usr/local/bin/myproject/fluent-bit-settings/fluent-bit.conf
```

Добавьте в него данные в виде:

```bash
[
SERVICE
]
Daemon Off
Flush
1
Log_Level info
Plugins_File plugins.conf
Parsers_File parsers.conf
[
INPUT
]
Name
tail
Path
<
path-to-log/logfile.log
>
Parser
docker
[
OUTPUT
]
Name logaas
Match *
address https://console.cloud.ru/
iam_address https://auth.iam.sbercloud.ru/
iam_client_id REPLACE_TO_LOGGING_SA_KEY_ID
iam_client_secret REPLACE_TO_LOGGING_SA_SECRET
default_project_id REPLACE_TO_PROJECT_ID
default_group_id REPLACE_TO_LOG_GROUP_ID
default_labels
{
"some_label"
:
"default_value"
}
```

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.

Измените файл, подставив в него свои данные:

- <path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
- REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».
- REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
- default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.

REPLACE_TO_LOGGING_SA_KEY_ID и REPLACE_TO_LOGGING_SA_SECRET — Key ID (логин) и Key Secret (пароль) сервисного аккаунта с ролью «logaas.writer» для получения токена и отправки логов.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны проект «Пользователь сервисов» и роль «logaas.writer».

REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.

default_labels — необязательный раздел. В нем вы можете указать метки, которые будут добавлены ко всем логам.

Пример для настройки отправки логов, собираемых из приложения — тестового источника логов:

```bash
[
SERVICE
]
Daemon Off
Flush
1
Log_Level info
Plugins_File plugins.conf
Parsers_File parsers.conf
[
INPUT
]
Name
tail
Path /var/log/myapp.log
Parser
docker
[
OUTPUT
]
Name logaas
Match *
address https://console.cloud.ru/
iam_address https://auth.iam.sbercloud.ru/
iam_client_id 30dce000000000000000000000f6b8e0
iam_client_secret 18a4f000000000000000000000098414
default_project_id 00000000-1111-2222-3333-444444444444
default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
default_labels
{
"source"
:
"docker-image"
,
"logger"
:
"fluentbit"
}
```

Откройте файл parsers.conf:

```bash
sudo
nano
/usr/local/bin/myproject/fluent-bit-settings/parsers.conf
```

Добавьте в файл данные:

```bash
[
PARSER
]
Name
docker
Format json
Time_Key
time
Time_Format %Y-%m-%dT%H:%M:%S.%L
Time_Keep On
Time_System_Timezone
true
```

## Шаг 5. Создание файла Doсker Compose

1. Создайте файл docker-compose.yml в корне проекта:
.├── app│ ├── Dockerfile│ └── log_generator.py├── docker-compose.yml└── fluent-bit-settings ├── fluent-bit.conf ├── logaas.so ├── parsers.conf └── plugins.conf

Файл docker-compose.yml — это YAML-файл, в котором описываются сервисы, сети, тома и настройки для запуска многоконтейнерного приложения через Docker.
Он позволяет управлять всеми компонентами приложения одной командой (docker compose up), автоматизируя развертывание и связывание контейнеров.
2. Добавьте в файл docker-compose.yml данные в виде:
version: '3.8'
services: app: build: context: ./app dockerfile: Dockerfile volumes: - logs:/var/log entrypoint: sh -c "python log_generator.py > /var/log/myapp.log 2>&1"
 fluent-bit: image: fluent/fluent-bit volumes: - logs:/var/log - ./fluent-bit-settings/:/etc/fluent-bit/ command: [ "fluent-bit", "-c", "/etc/fluent-bit/fluent-bit.conf", "-e", "/etc/fluent-bit/logaas-client.so" ]
volumes: logs:

В docker-compose.yml мы используем готовый образ fluent/fluent-bit.
По желанию вы можете использовать свой образ с настроенным fluent-bit.
Установка модуля fluent-bit в систему не требуется.
3. Запустите полученный Doсker Compose.
Чтобы запустить его в фоновом режиме, добавьте к команде флаг -d:
sudo docker compose up -d

Docker загрузит недостающие образы и запустит контейнеры:
[+] Running 2/2 ✔ Container myproject-fluent-bit-1 Started 0.5s ✔ Container myproject-app-1 Start
4. Если запущенные контейнеры больше не нужны, остановите их:
sudo docker compose stop
5. Удалите неиспользованные контейнеры:
sudo docker compose down

Docker удалит неиспользованные контейнеры:
[+] Running 3/3 ✔ Container myproject-app-1 Removed 10.3s ✔ Container myproject-fluent-bit-1 Removed 0.5s ✔ Network myproject_default Removed
6. Кроме контейнеров и сетей вы можете удалить volumes:
sudo docker compose down -v

Создайте файл docker-compose.yml в корне проекта:

```bash
.
├── app
│ ├── Dockerfile
│ └── log_generator.py
├── docker-compose.yml
└── fluent-bit-settings
├── fluent-bit.conf
├── logaas.so
├── parsers.conf
└── plugins.conf
```

Файл docker-compose.yml — это YAML-файл, в котором описываются сервисы, сети, тома и настройки для запуска многоконтейнерного приложения через Docker.
Он позволяет управлять всеми компонентами приложения одной командой (docker compose up), автоматизируя развертывание и связывание контейнеров.

Добавьте в файл docker-compose.yml данные в виде:

```bash
version:
'3.8'
services:
app:
build:
context: ./app
dockerfile: Dockerfile
volumes:
- logs:/var/log
entrypoint:
sh
-c
"python log_generator.py > /var/log/myapp.log 2>&1"
fluent-bit:
image: fluent/fluent-bit
volumes:
- logs:/var/log
- ./fluent-bit-settings/:/etc/fluent-bit/
command:
[
"fluent-bit"
,
"-c"
,
"/etc/fluent-bit/fluent-bit.conf"
,
"-e"
,
"/etc/fluent-bit/logaas-client.so"
]
volumes:
logs:
```

В docker-compose.yml мы используем готовый образ fluent/fluent-bit.
По желанию вы можете использовать свой образ с настроенным fluent-bit.
Установка модуля fluent-bit в систему не требуется.

Запустите полученный Doсker Compose.
Чтобы запустить его в фоновом режиме, добавьте к команде флаг -d:

```bash
sudo
docker
compose up
-d
```

Docker загрузит недостающие образы и запустит контейнеры:

```bash
[
+
]
Running
2
/2
✔ Container myproject-fluent-bit-1 Started
0
.5s
✔ Container myproject-app-1 Start
```

Если запущенные контейнеры больше не нужны, остановите их:

```bash
sudo
docker
compose stop
```

Удалите неиспользованные контейнеры:

```bash
sudo
docker
compose down
```

Docker удалит неиспользованные контейнеры:

```bash
[
+
]
Running
3
/3
✔ Container myproject-app-1 Removed
10
.3s
✔ Container myproject-fluent-bit-1 Removed
0
.5s
✔ Network myproject_default Removed
```

Кроме контейнеров и сетей вы можете удалить volumes:

```bash
sudo
docker
compose down
-v
```

## Шаг 6. Просмотр логов

В случае успешного старта Docker-образов логи появятся в сервисе «Клиентское логирование» вскоре после старта приложения.

Вы можете [посмотреть логи в лог-группах](https://cloud.ru/docs/client-log/ug/topics/working-groups)посмотреть логи в лог-группах.
Логи можно [отфильтровать с помощью языка фильтрующих выражений](https://cloud.ru/docs/client-log/ug/topics/concepts__filter)отфильтровать с помощью языка фильтрующих выражений и выгрузить как файл.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.
Чтобы данные непрерывно поступали в сервис, выберите подходящий сценарий:

- запустите генератор логов в бесконечном цикле, чтобы поддерживать постоянное поступление данных;
- выполняйте генерацию логов пакетами — запускайте скрипт многократно с необходимым интервалом.

запустите генератор логов в бесконечном цикле, чтобы поддерживать постоянное поступление данных;

выполняйте генерацию логов пакетами — запускайте скрипт многократно с необходимым интервалом.

Это позволяет исключить дублирование записей и поддерживать актуальность передаваемых данных.

Дополнительно рекомендуется настроить ротацию логов, чтобы избежать переполнения диска при длительной работе.

## После окончания работы

Если виртуальная машина и ее логи стали неактуальными, вы можете удалить их:

- [Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу
- [Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект
- [Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину

[Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу

[Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект

[Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину
