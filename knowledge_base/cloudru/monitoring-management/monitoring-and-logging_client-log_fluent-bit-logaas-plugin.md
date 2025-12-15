---
title: Передача логов с виртуальной машины с помощью Fluent Bit logaas plugin
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__fluent-bit-logaas-plugin
topic: monitoring-management
---
# Передача логов с виртуальной машины с помощью Fluent Bit logaas plugin

Fluent Bit — кроссплатформенный инструмент с открытым исходным кодом.
Он собирает, обрабатывает и фильтрует лог-сообщения из разных источников, а затем сохраняет их в хранилище.
После этого лог-сообщения поступают в маршрутизатор, который определяет, куда они будут отправлены.
Для работы с разными источниками и приемниками используются специализированные плагины.

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

## Шаг 1. Установка Fluent Bit

Установите Fluent Bit одним из способов:

Установите приложение Fluent Bit из сборки дистрибутива для вашей операционной системы.

Чтобы проверить, что fluent-bit установлен корректно, нужно запустить его и убедиться, что он установлен как сервис.
Для этого:

1. Запустите fluent-bit как сервис:
sudo systemctl start fluent-bit
2. Проверьте статус сервиса fluent-bit — он должен быть активным:
systemctl status fluent-bit

Если fluent-bit настроен верно, будет выведен статус в виде:
● fluent-bit.service - Fluent Bit Loaded: loaded (/lib/systemd/system/fluent-bit.service; disabled; vendor preset: enabled) Active: active (running) since Tue 2025-03-11 15:48:23 UTC; 3s ago Docs: https://docs.fluentbit.io/manual/ Main PID: 34596 (fluent-bit) Tasks: 8 (limit: 2323) Memory: 9.4M CPU: 70ms CGroup: /system.slice/fluent-bit.service └─34596 /opt/fluent-bit/bin/fluent-bit -c //etc/fluent-bit/fluent-bit.conf
3. После проверки сервиса fluent-bit остановите его, чтобы далее настроить на совместную работу с logaas:
sudo systemctl stop fluent-bit

Запустите fluent-bit как сервис:

```bash
sudo
systemctl start fluent-bit
```

Проверьте статус сервиса fluent-bit — он должен быть активным:

```bash
systemctl status fluent-bit
```

Если fluent-bit настроен верно, будет выведен статус в виде:

```bash
● fluent-bit.service - Fluent Bit
Loaded: loaded
(
/lib/systemd/system/fluent-bit.service
;
disabled
;
vendor preset: enabled
)
Active: active
(
running
)
since Tue
2025
-03-11
15
:48:23 UTC
;
3s ago
Docs: https://docs.fluentbit.io/manual/
Main PID:
34596
(
fluent-bit
)
Tasks:
8
(
limit:
2323
)
Memory:
9
.4M
CPU: 70ms
CGroup: /system.slice/fluent-bit.service
└─34596 /opt/fluent-bit/bin/fluent-bit
-c
//etc/fluent-bit/fluent-bit.conf
```

После проверки сервиса fluent-bit остановите его, чтобы далее настроить на совместную работу с logaas:

```bash
sudo
systemctl stop fluent-bit
```

## Шаг 2. Установка и настройка Fluent Bit logaas plugin

Fluent Bit logaas plugin — отдельная библиотека, которая подключается к fluent-bit и позволяет отправлять логи в сервис Клиентского логирования.

Чтобы установить плагин:

1. Скачайте скомпилированный плагин logaas.so и поместите его в папку настроек fluent-bit:
sudo wget https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaas.so -O /etc/fluent-bit/logaas.so
2. Откройте файл с настройками плагинов /etc/fluent-bit/plugins.conf с помощью редактора nano:
sudo nano /etc/fluent-bit/plugins.conf

В файл добавьте путь до плагина logaas.so:
[PLUGINS] Path /etc/fluent-bit/logaas.so
3. Откройте файл /etc/fluent-bit/fluent-bit.conf:
sudo nano /etc/fluent-bit/fluent-bit.conf

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

В следующем шаге инструкции настраивается тестовая отправка данных с помощью генератора логов, который записывает логи в лог-файл.
Для тестирования с помощью генератора вместо <path-to-log/logfile.log> укажите путь к лог-файлу: /usr/local/bin/log_producer/error_log.log.
Пример изменений в файле /etc/fluent-bit/fluent-bit.conf:
[SERVICE] Daemon Off Flush 1 Log_Level info Plugins_File plugins.conf Parsers_File parsers.conf
[INPUT] Name tail Path /usr/local/bin/log_producer/error_log.log Parser docker
[OUTPUT] Name logaas Match * address https://console.cloud.ru/ iam_address https://auth.iam.sbercloud.ru/ iam_client_id 30dce000000000000000000000f6b8e0 iam_client_secret 18a4f000000000000000000000098414 default_project_id 00000000-1111-2222-3333-444444444444 default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee default_labels {"source":"vm", "logger":"fluentbit"}

Скачайте скомпилированный плагин logaas.so и поместите его в папку настроек fluent-bit:

```bash
sudo
wget
https://github.com/CLOUDdotRu/fluent-bit-plugins/raw/main/logaas.so
-O
/etc/fluent-bit/logaas.so
```

Откройте файл с настройками плагинов /etc/fluent-bit/plugins.conf с помощью редактора nano:

```bash
sudo
nano
/etc/fluent-bit/plugins.conf
```

В файл добавьте путь до плагина logaas.so:

```bash
[
PLUGINS
]
Path /etc/fluent-bit/logaas.so
```

Откройте файл /etc/fluent-bit/fluent-bit.conf:

```bash
sudo
nano
/etc/fluent-bit/fluent-bit.conf
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

В следующем шаге инструкции настраивается тестовая отправка данных с помощью генератора логов, который записывает логи в лог-файл.
Для тестирования с помощью генератора вместо <path-to-log/logfile.log> укажите путь к лог-файлу: /usr/local/bin/log_producer/error_log.log.

Пример изменений в файле /etc/fluent-bit/fluent-bit.conf:

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
Path /usr/local/bin/log_producer/error_log.log
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
"vm"
,
"logger"
:
"fluentbit"
}
```

## Шаг 3. Проверка отправки логов

На этом этапе вы сможете настроить тестовую отправку логов с помощью bash-скрипта — генератора логов.
Он будет записывать логи в лог-файл.

Чтобы создать генератор:

1. Создайте директорию, в которой будет находиться скрипт:
sudo mkdir /usr/local/bin/log_producer/
2. Создайте пустой файл log_producer.sh:
sudo touch /usr/local/bin/log_producer/log_producer.sh
3. Откройте созданный файл с помощью редактора nano:
sudo nano /usr/local/bin/log_producer/log_producer.sh

В файл добавьте:
#!/bin/bash
LOG_FILE=${1:-./error_log.log}
generate_log() { # Generate timestamp with timezone timestamp=$(date "+%Y-%m-%dT%H:%M:%S.%3N%:z")
 # Random log level selection levels=("TRACE" "DEBUG" "INFO" "NOTICE" "WARN" "ERROR" "CRITICAL" "ALERT" "EMERGENCY" "FATAL") level=${levels[$RANDOM % ${#levels[@]}]}
 # Create labels JSON object labels_json="\"labels\":{" labels_json+="\"app\":\"logger\"," labels_json+="\"host\":\"$(hostname)\"," labels_json+="\"pid\":$$," labels_json+="\"random\":$((RANDOM % 1000))" labels_json+="}"
 # Generate random message messages=( "Processing request" "Task completed" "Operation failed" "Initializing system" "Checking permissions" "Resource allocated" "Connection timeout" "Data received" "Invalid input" "Queue processed" ) message="${messages[$RANDOM % ${#messages[@]}]} [ID: $((RANDOM % 10000))]"
 # Construct single-line JSON printf '{"timestamp":"%s","level":"%s",%s,"message":"%s"}\n' \ "$timestamp" \ "$level" \ "$labels_json" \ "$message"}
# Handle Ctrl+Ctrap 'echo -e "\nLogging stopped. Output: $LOG_FILE"; exit' SIGINT
echo "Logging to $LOG_FILE - Press CTRL+C to stop"while true; do generate_log >> "$LOG_FILE" sleep 1done

Последние строки кода запускают генератор логов в бесконечном цикле — чтобы остановить генератор, нажмите CTRL + C.
Вы можете изменить это поведение генератора — например, чтобы задать генерацию логов в течение 1 минуты, замените строки:
while true; do generate_log >> "$LOG_FILE" sleep 1done

на строки:
count=0while [ $count -lt 60 ]; do generate_log >> "$LOG_FILE" ((count++)) sleep 1done
4. Назначьте файл log_producer.sh исполняемым:
sudo chmod +x /usr/local/bin/log_producer/log_producer.sh
5. Запустите генератор логов:
sudo /usr/local/bin/log_producer/log_producer.sh

Генератор можно запустить в фоновом режиме, добавив к команде знак & — так вы сможете продолжать работать в этой же консоли, не открывая новую для последующих процессов.
sudo /usr/local/bin/log_producer/log_producer.sh &

Создайте директорию, в которой будет находиться скрипт:

```bash
sudo
mkdir
/usr/local/bin/log_producer/
```

Создайте пустой файл log_producer.sh:

```bash
sudo
touch
/usr/local/bin/log_producer/log_producer.sh
```

Откройте созданный файл с помощью редактора nano:

```bash
sudo
nano
/usr/local/bin/log_producer/log_producer.sh
```

В файл добавьте:

```bash
#!/bin/bash
LOG_FILE
=
${1
:-
.
/
error_log.log}
generate_log
(
)
{
# Generate timestamp with timezone
timestamp
=
$(
date
"+%Y-%m-%dT%H:%M:%S.%3N%:z"
)
# Random log level selection
levels
=
(
"TRACE"
"DEBUG"
"INFO"
"NOTICE"
"WARN"
"ERROR"
"CRITICAL"
"ALERT"
"EMERGENCY"
"FATAL"
)
level
=
${levels
[
$RANDOM
%
${
#
levels
[
@
]
}
]
}
# Create labels JSON object
labels_json
=
"
\"
labels
\"
:{"
labels_json
+=
"
\"
app
\"
:
\"
logger
\"
,"
labels_json
+=
"
\"
host
\"
:
\"
$(
hostname
)
\"
,"
labels_json
+=
"
\"
pid
\"
:
$$
,"
labels_json
+=
"
\"
random
\"
:
$((
RANDOM
%
1000
))
"
labels_json
+=
"}"
# Generate random message
messages
=
(
"Processing request"
"Task completed"
"Operation failed"
"Initializing system"
"Checking permissions"
"Resource allocated"
"Connection timeout"
"Data received"
"Invalid input"
"Queue processed"
)
message
=
"
${messages
[
$RANDOM
%
${
#
messages
[
@
]
}
]} [ID:
$((
RANDOM
%
10000
))
]"
# Construct single-line JSON
printf
'{"timestamp":"%s","level":"%s",%s,"message":"%s"}\n'
\
"
$timestamp
"
\
"
$level
"
\
"
$labels_json
"
\
"
$message
"
}
# Handle Ctrl+C
trap
'echo -e "\nLogging stopped. Output: $LOG_FILE"; exit'
SIGINT
echo
"Logging to
$LOG_FILE
- Press CTRL+C to stop"
while
true
;
do
generate_log
>>
"
$LOG_FILE
"
sleep
1
done
```

Последние строки кода запускают генератор логов в бесконечном цикле — чтобы остановить генератор, нажмите CTRL + C.
Вы можете изменить это поведение генератора — например, чтобы задать генерацию логов в течение 1 минуты, замените строки:

```bash
while
true
;
do
generate_log
>>
"
$LOG_FILE
"
sleep
1
done
```

на строки:

```bash
count
=
0
while
[
$count
-lt
60
]
;
do
generate_log
>>
"
$LOG_FILE
"
((
count
++
))
sleep
1
done
```

Назначьте файл log_producer.sh исполняемым:

```bash
sudo
chmod
+x /usr/local/bin/log_producer/log_producer.sh
```

Запустите генератор логов:

```bash
sudo
/usr/local/bin/log_producer/log_producer.sh
```

Генератор можно запустить в фоновом режиме, добавив к команде знак & — так вы сможете продолжать работать в этой же консоли, не открывая новую для последующих процессов.

```bash
sudo
/usr/local/bin/log_producer/log_producer.sh
&
```

После запуска генератор начнет создавать лог-файл /usr/local/bin/log_producer/error_log.log.

Чтобы остановить работу log_producer.sh, нажмите CTRL + C.

## Шаг 4. Запуск Fluent Bit для сбора логов

Перед первым запуском fluent-bit в режиме сервиса нужно проверить, нет ли ошибок доступа и корректно ли заполнены файлы настроек.
Для этого проверьте работу fluent-bit в следующем порядке:

1. Запустите fluent-bit в консольном режиме.
2. Запустите fluent-bit в режиме сервиса.

Запустите fluent-bit в консольном режиме.

Запустите fluent-bit в режиме сервиса.

В дальнейшем вы сможете использовать любой из этих способов.

### Запуск в консольном режиме

Запустите fluent-bit в консоли:

```bash
sudo
/opt/fluent-bit/bin/fluent-bit
-c
/etc/fluent-bit/fluent-bit.conf
```

Сообщения такого типа показывают, что данные отправляются успешно:

```bash
2025
/03/11
15
:56:22 send
2025
/03/11
15
:56:22 0xc00017a010
2025
/03/11
15
:56:22 logaas send data:
{
"logs"
:
[
{
"timestamp"
:
"2025-03-12T15:56:21.975165893Z"
,
"level"
:
"EMERGENCY"
,
"project_id"
:
"21df218c-931b-4707-8e02-f0498a57e2c9"
,
"log_group_id"
:
"80746b7e-efb3-11ef-990d-525356cf44f3"
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
"myvm"
,
"logger"
:
"client_plugin"
,
"pid"
:
"61467"
,
"random"
:
"646"
,
"source"
:
"docker_compose"
,
"transport"
:
"log_file"
}
,
"message"
:
"Invalid input [ID: 5930]"
}
]
}
2025
/03/11
15
:56:22 received response body:
{
"errors"
:
{
}
}
```

Чтобы завершить работу fluent-bit, нажмите CTRL + C.

### Запуск в режиме сервиса

Запустите fluent-bit для сбора логов как сервис:

```bash
sudo
systemctl start fluent-bit
```

Если сервис был запущен ранее, его можно перезапустить, чтобы применились изменения конфигурации:

```bash
sudo
systemctl restart fluent-bit
```

## Шаг 5. Просмотр логов

Через несколько секунд после отправки логи появятся в сервисе Клиентского логирования.

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

## После окончания работы

Если виртуальная машина и ее логи стали неактуальными, вы можете удалить их:

- [Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу
- [Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект
- [Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину

[Удалить лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Удалить лог-группу

[Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект

[Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину
