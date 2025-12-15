---
title: Передача аудит-логов с виртуальной машины с помощью Fluent Bit
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__audit-logging__fluent-bit
topic: monitoring-management
---
# Передача аудит-логов с виртуальной машины с помощью Fluent Bit

Отправка аудит-логов в сервис находится на стадии

Fluent Bit — кроссплатформенный инструмент с открытым исходным кодом.
Он собирает, обрабатывает и фильтрует лог-сообщения из разных источников, а затем сохраняет их в хранилище.
После этого лог-сообщения поступают в маршрутизатор, который определяет, куда они будут отправлены.
Для работы с разными источниками и приемниками используются специализированные плагины.

## Перед началом работы

1. [Создайте необходимые типы аудит-событий](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)Создайте необходимые типы аудит-событий.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

в блоке Проект — «Пользователь сервисов»;
в блоке Сервисы — «audit.writer».
3. Для сервисного аккаунта [создайте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)создайте API-ключ.
В параметрах API-ключа укажите сервис «audit».
Срок действия API-ключа ограничен — когда он подойдет к концу, мы отправим вам уведомление.
После этого необходимо [обновить API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__update)обновить API-ключ.
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu 22.04.
5. [Подключитесь к созданной виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к созданной виртуальной машине по SSH.

[Создайте необходимые типы аудит-событий](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)Создайте необходимые типы аудит-событий.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

- в блоке Проект — «Пользователь сервисов»;
- в блоке Сервисы — «audit.writer».

в блоке Проект — «Пользователь сервисов»;

в блоке Сервисы — «audit.writer».

Для сервисного аккаунта [создайте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)создайте API-ключ.
В параметрах API-ключа укажите сервис «audit».

Срок действия API-ключа ограничен — когда он подойдет к концу, мы отправим вам уведомление.
После этого необходимо [обновить API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__update)обновить API-ключ.

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
3. После проверки сервиса fluent-bit остановите его, чтобы далее настроить на совместную работу с плагином audit:
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

После проверки сервиса fluent-bit остановите его, чтобы далее настроить на совместную работу с плагином audit:

```bash
sudo
systemctl stop fluent-bit
```

## Шаг 2. Настройка Fluent Bit

1. Откройте файл /etc/fluent-bit/fluent-bit.conf:
sudo nano /etc/fluent-bit/fluent-bit.conf
2. Добавьте в файл данные в виде:
[SERVICE] Daemon Off Flush 1 Log_Level info Plugins_File plugins.conf Parsers_File parsers.conf
[INPUT] Name tail Path <path-to-log/logfile.log> Parser docker Tag fb_tag
[FILTER] Name lua Match fb_tag Script to_audit.lua call convert_to_audit
[OUTPUT] Name http Match fb_tag Host audit.api.cloud.ru URI /bulk/<REPLACE_TO_PROJECT_ID>/send Port 443 Format json json_date_key false Header Authorization Api-Key <REPLACE_TO_AUDIT_API_KEY> tls on

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.
В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.
Подставьте в файл свои данные:

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
<REPLACE_TO_PROJECT_ID> — ID проекта, в который будут отправлены аудит-логи.
REPLACE_TO_AUDIT_API_KEY — API-ключ сервисного аккаунта с ролью «audit.writer».
Проверьте, что для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «audit.writer».

В следующем шаге инструкции настраивается тестовая отправка данных с помощью генератора логов, который записывает аудит-логи в лог-файл.
Для тестирования с помощью генератора вместо <path-to-log/logfile.log> укажите путь к лог-файлу: /usr/local/bin/log_producer/error_log.log.
Пример изменений в файле /etc/fluent-bit/fluent-bit.conf:
[SERVICE] Daemon Off Flush 1 Log_Level info Plugins_File plugins.conf Parsers_File parsers.conf
[INPUT] Name tail Path /usr/local/bin/log_producer/error_log.log Parser docker Tag fb_tag
[FILTER] Name lua Match fb_tag Script to_audit.lua call convert_to_audit
[OUTPUT] Name http Match fb_tag Host audit.api.cloud.ru URI /bulk/00000000-1111-2222-3333-444444444444/send Port 443 Format json json_date_key false Header Authorization Api-Key M2QxNjxxxxxxxxxxxxxxxxxxxxxxxxxxx.1e3c25xxxxxxxxxxxx tls on
3. Создайте скрипт-трансформер, который будет переводить исходный формат логов в формат, поддерживаемый сервисом «Аудит-логирование»:
sudo touch /etc/fluent-bit/to_audit.lua
4. Откройте файл скрипта с помощью редактора nano:
sudo nano /etc/fluent-bit/to_audit.lua
5. Измените скрипт to_audit.lua в соответствии с форматом исходного лог-файла:
function table_to_string(tbl) local result = "{" for k, v in pairs(tbl) do -- Check the key type (ignore any numerical keys - assume its an array) if type(k) == "string" then result = result.."[\""..k.."\"]".."=" end
 -- Check the value type if type(v) == "table" then result = result..table_to_string(v) elseif type(v) == "boolean" then result = result..tostring(v) else result = result.."\""..v.."\"" end result = result.."," end -- Remove leading commas from the result if result ~= "{" then result = result:sub(1, result:len()-1) end return result.."}"end
function convert_to_audit(tag, timestamp, record) new_record = {} new_record["datetime"] = os.time()*1000 new_record["service_name"] = "Customer" new_record["service_version"] = "n/a" new_record["name"] = "SyslogEvent" new_record["session_id"] = "" new_record["user_login"] = record["user_login"] new_record["user_name"] = record["user_name"] new_record["user_node"] = "n/a" new_record["tags"]={"GT2","GT3"} new_record["params"] = { { name = "details", value = table_to_string(record) } } return 1, timestamp, new_recordend

Где:

datetime — время, в которое произошло событие, в формате Unix.
service_name — имя сервиса-источника события.
В примере в инструкции мы используем предопределенный тип сервиса-источника — ["service_name"] = "Customer".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его источник.
service_version — версия сервиса.
name — тип события.
В примере в инструкции мы используем тип ["name"] = "SyslogEvent".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его название.
session_id — ID запроса.
user_login — логин пользователя.
user_name — имя пользователя.
user_node — адрес субъекта события.
tags — опциональное поле, массив строк с набором тегов.
params — детали события, массив в формате key-value pair.
Сервис-источник сам определяет состав параметров внутри объекта.

Откройте файл /etc/fluent-bit/fluent-bit.conf:

```bash
sudo
nano
/etc/fluent-bit/fluent-bit.conf
```

Добавьте в файл данные в виде:

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
Tag fb_tag
[
FILTER
]
Name lua
Match fb_tag
Script to_audit.lua
call convert_to_audit
[
OUTPUT
]
Name http
Match fb_tag
Host audit.api.cloud.ru
URI /bulk/
<
REPLACE_TO_PROJECT_ID
>
/send
Port
443
Format json
json_date_key
false
Header Authorization Api-Key
<
REPLACE_TO_AUDIT_API_KEY
>
tls on
```

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.

Подставьте в файл свои данные:

- <path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
- <REPLACE_TO_PROJECT_ID> — ID проекта, в который будут отправлены аудит-логи.
- REPLACE_TO_AUDIT_API_KEY — API-ключ сервисного аккаунта с ролью «audit.writer».
Проверьте, что для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «audit.writer».

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.

<REPLACE_TO_PROJECT_ID> — ID проекта, в который будут отправлены аудит-логи.

REPLACE_TO_AUDIT_API_KEY — API-ключ сервисного аккаунта с ролью «audit.writer».
Проверьте, что для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «audit.writer».

В следующем шаге инструкции настраивается тестовая отправка данных с помощью генератора логов, который записывает аудит-логи в лог-файл.
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
Tag fb_tag
[
FILTER
]
Name lua
Match fb_tag
Script to_audit.lua
call convert_to_audit
[
OUTPUT
]
Name http
Match fb_tag
Host audit.api.cloud.ru
URI /bulk/00000000-1111-2222-3333-444444444444/send
Port
443
Format json
json_date_key
false
Header Authorization Api-Key M2QxNjxxxxxxxxxxxxxxxxxxxxxxxxxxx.1e3c25xxxxxxxxxxxx
tls on
```

Создайте скрипт-трансформер, который будет переводить исходный формат логов в формат, поддерживаемый сервисом «Аудит-логирование»:

```bash
sudo
touch
/etc/fluent-bit/to_audit.lua
```

Откройте файл скрипта с помощью редактора nano:

```bash
sudo
nano
/etc/fluent-bit/to_audit.lua
```

Измените скрипт to_audit.lua в соответствии с форматом исходного лог-файла:

```bash
function
table_to_string
(
tbl
)
local
result
=
"{"
for
k,
v
in
pairs
(
tbl
)
do
-- Check the key
type
(
ignore any numerical keys - assume its an array
)
if
type
(
k
)
==
"string"
then
result
=
result
..
"[
\"
"
..
k
..
"
\"
]"
..
"="
end
-- Check the value
type
if
type
(
v
)
==
"table"
then
result
=
result
..
table_to_string
(
v
)
elseif type
(
v
)
==
"boolean"
then
result
=
result
..
tostring
(
v
)
else
result
=
result
..
"
\"
"
..
v
..
"
\"
"
end
result
=
result
..
","
end
-- Remove leading commas from the result
if
result ~
=
"{"
then
result
=
result:sub
(
1
, result:len
(
)
-1
)
end
return
result
..
"}"
end
function
convert_to_audit
(
tag, timestamp, record
)
new_record
=
{
}
new_record
[
"datetime"
]
=
os.time
(
)
*1000
new_record
[
"service_name"
]
=
"Customer"
new_record
[
"service_version"
]
=
"n/a"
new_record
[
"name"
]
=
"SyslogEvent"
new_record
[
"session_id"
]
=
""
new_record
[
"user_login"
]
=
record
[
"user_login"
]
new_record
[
"user_name"
]
=
record
[
"user_name"
]
new_record
[
"user_node"
]
=
"n/a"
new_record
[
"tags"
]
=
{
"GT2"
,
"GT3"
}
new_record
[
"params"
]
=
{
{
name
=
"details"
,
value
=
table_to_string
(
record
)
}
}
return
1
, timestamp, new_record
end
```

Где:

- datetime — время, в которое произошло событие, в формате Unix.
- service_name — имя сервиса-источника события.
В примере в инструкции мы используем предопределенный тип сервиса-источника — ["service_name"] = "Customer".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его источник.
- service_version — версия сервиса.
- name — тип события.
В примере в инструкции мы используем тип ["name"] = "SyslogEvent".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его название.
- session_id — ID запроса.
- user_login — логин пользователя.
- user_name — имя пользователя.
- user_node — адрес субъекта события.
- tags — опциональное поле, массив строк с набором тегов.
- params — детали события, массив в формате key-value pair.
Сервис-источник сам определяет состав параметров внутри объекта.

datetime — время, в которое произошло событие, в формате Unix.

service_name — имя сервиса-источника события.
В примере в инструкции мы используем предопределенный тип сервиса-источника — ["service_name"] = "Customer".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его источник.

service_version — версия сервиса.

name — тип события.
В примере в инструкции мы используем тип ["name"] = "SyslogEvent".
Используйте его для тестирования.
В дальнейшем вы можете [создать свой тип события](https://cloud.ru/docs/audit-logging/ug/topics/view-event-types)создать свой тип события и указать здесь его название.

session_id — ID запроса.

user_login — логин пользователя.

user_name — имя пользователя.

user_node — адрес субъекта события.

tags — опциональное поле, массив строк с набором тегов.

params — детали события, массив в формате key-value pair.
Сервис-источник сам определяет состав параметров внутри объекта.

## Шаг 3. Проверка отправки аудит-логов

На этом этапе вы сможете настроить тестовую отправку аудит-логов с помощью bash-скрипта — генератора логов.
Он будет записывать аудит-логи в лог-файл.

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
 # Construct single-line JSON printf '{"timestamp":"%s","level":"%s","message":"%s", "version":"V2_1","user_name":"Ivan Ivanov", "user_login":"ivivanov"}\n' \ "$timestamp" \ "$level" \ "$message"}
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
sudo /usr/local/bin/log_producer/log_producer.sh /usr/local/bin/log_producer/error_log.log

Генератор можно запустить в фоновом режиме, добавив к команде знак & — так вы сможете продолжать работать в этой же консоли, не открывая новую для последующих процессов:
sudo /usr/local/bin/log_producer/log_producer.sh /usr/local/bin/log_producer/error_log.log &

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
'{"timestamp":"%s","level":"%s","message":"%s", "version":"V2_1","user_name":"Ivan Ivanov", "user_login":"ivivanov"}\n'
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
/usr/local/bin/log_producer/log_producer.sh /usr/local/bin/log_producer/error_log.log
```

Генератор можно запустить в фоновом режиме, добавив к команде знак & — так вы сможете продолжать работать в этой же консоли, не открывая новую для последующих процессов:

```bash
sudo
/usr/local/bin/log_producer/log_producer.sh /usr/local/bin/log_producer/error_log.log
&
```

После запуска генератор начнет создавать лог-файл /usr/local/bin/log_producer/error_log.log.

Чтобы остановить работу log_producer.sh, нажмите CTRL + C.

## Шаг 4. Запуск Fluent Bit для сбора аудит-логов

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
[
2025
/03/20 09:40:33
]
[
info
]
[
output:http:http.0
]
worker
#1 started
[
2025
/03/20 09:40:37
]
[
info
]
[
output:http:http.0
]
audit.api.cloud.ru:443, HTTP
status
=
200
{
}
[
2025
/03/20 09:40:38
]
[
info
]
[
output:http:http.0
]
audit.api.cloud.ru:443, HTTP
status
=
200
{
}
[
2025
/03/20 09:40:39
]
[
info
]
[
output:http:http.0
]
audit.api.cloud.ru:443, HTTP
status
=
200
{
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

## Шаг 5. Просмотр аудит-логов

Через несколько секунд после отправки аудит-логи появятся в сервисе «Аудит-логирование».
Вы можете [посмотреть аудит-логи в таблице](https://cloud.ru/docs/audit-logging/ug/topics/view-logs)посмотреть аудит-логи в таблице.
Аудит-логи можно фильтровать и выгрузить как файл.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.
Чтобы данные непрерывно поступали в сервис, выберите подходящий сценарий:

- запустите генератор логов в бесконечном цикле, чтобы поддерживать постоянное поступление данных;
- выполняйте генерацию логов пакетами — запускайте скрипт многократно с необходимым интервалом.

запустите генератор логов в бесконечном цикле, чтобы поддерживать постоянное поступление данных;

выполняйте генерацию логов пакетами — запускайте скрипт многократно с необходимым интервалом.

Это позволяет исключить дублирование записей и поддерживать актуальность передаваемых данных.

## После окончания работы

Если проект и виртуальная машина стали неактуальными, вы можете удалить их:

- [Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект
- [Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину

[Удалить проект](https://cloud.ru/docs/administration/ug/topics/guides__projects)Удалить проект

[Удалить виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалить виртуальную машину
