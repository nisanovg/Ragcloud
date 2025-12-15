---
title: Передача логов с виртуальной машины с помощью Fluent Bit и Lua-скрипта
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__client-log__fluent-bit-lua-script
topic: monitoring-management
---
# Передача логов с виртуальной машины с помощью Fluent Bit и Lua-скрипта

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
3. Для сервисного аккаунта [создайте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)создайте API-ключ.
В параметрах API-ключа укажите сервис «logging_as_a_service».
Срок действия API-ключа ограничен — когда он подойдет к концу, мы отправим вам уведомление.
После этого необходимо [обновить API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__update)обновить API-ключ.
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu 22.04.
5. [Подключитесь к созданной виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к созданной виртуальной машине по SSH.

[Создайте и настройте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте и настройте лог-группу.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
В блоке Доступы и роли выберите роли:

- в блоке Проект — «Пользователь сервисов»;
- в блоке Сервисы — «logaas.writer».

в блоке Проект — «Пользователь сервисов»;

в блоке Сервисы — «logaas.writer».

Для сервисного аккаунта [создайте API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__create)создайте API-ключ.
В параметрах API-ключа укажите сервис «logging_as_a_service».

Срок действия API-ключа ограничен — когда он подойдет к концу, мы отправим вам уведомление.
После этого необходимо [обновить API-ключ](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys__update)обновить API-ключ.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu 22.04.

[Подключитесь к созданной виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к созданной виртуальной машине по SSH.

## Шаг 1. Установка Fluent Bit

Возможно использование Fluent Bit версии 2.2 и выше.
Рекомендуемая версия — 3.2.

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

## Шаг 2. Настройка Fluent Bit

1. Создайте файл logaas_format.lua для форматирования логов в формат сервиса «Клиентское логирование»:
sudo touch /etc/fluent-bit/logaas_format.lua
2. Откройте созданный файл с помощью редактора nano:
sudo nano /etc/fluent-bit/logaas_format.lua
3. В файл добавьте:
-- Fluent Bit lua client script-- Version: 1.0.1-- Copyright 2025 Cloud.ru
-- Licensed under the Apache License, Version 2.0 (the "License");-- you may not use this file except in compliance with the License.-- You may obtain a copy of the License at
-- http://www.apache.org/licenses/LICENSE-2.0
-- Unless required by applicable law or agreed to in writing, software-- distributed under the License is distributed on an "AS IS" BASIS,-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.-- See the License for the specific language governing permissions and-- limitations under the License.

local whitelist = { "timestamp", "level", "project_id", "log_group_id", "default_labels", "labels", "message", "json_message", "trace_id", "service_name", "instance_id"}
local whitelist_hash = {}for _, key in ipairs(whitelist) do whitelist_hash[key] = trueend
local json = (function()local escape = function(str) return str:gsub('[\\"/]', function(c) return '\\' .. c end)end
local function encode_value(val) local t = type(val) if t == 'string' then return '"' .. escape(val) .. '"' elseif t == 'number' or t == 'boolean' then return tostring(val) elseif t == 'table' then local result = {} for k, v in pairs(val) do local key = type(k) == 'number' and '[' .. k .. ']' or '"' .. k .. '"' table.insert(result, key .. ':' .. encode_value(v)) end return '{' .. table.concat(result, ',') .. '}' else return 'null' endend
return { encode = function(tbl) return encode_value(tbl) end}end)()

function extra_fields(record) local message_ = {} local keys_to_remove = {} local json_message = {} local message_data = {}
 for key, value in pairs(record) do if not whitelist_hash[key] then message_data[key] = value table.insert(keys_to_remove, key) end end

 if next(message_data) ~= nil then json_message = json.encode(message_data) return json_message else return nil endend

function ensure_string(var) if type(var) == "string" then return var, true end
 if type(var) == "number" or type(var) == "boolean" then return tostring(var), true end
 return nil, falseend

function format_log(tag, timestamp, record) -- 1. Project ID & Log Group ID local default_project_id = record.default_project_id local default_group_id = record.default_group_id
 local project_id = record.project_id if not project_id or project_id == "" then project_id = default_project_id end
 local group_id = record.group_id if not group_id or group_id == "" then group_id = default_group_id end
 record.default_project_id = nil record.default_group_id = nil
 -- 2. Timestamp local system_timezone = os.date("%z") local timezone_formatted = string.sub(system_timezone, 1, 3) .. ":" .. string.sub(system_timezone, 4, 5) local sec = timestamp.sec local nsec = timestamp.nsec local iso_timestamp = os.date("%Y-%m-%dT%H:%M:%S", sec) local milliseconds = string.format("%03d", math.floor(nsec / 1000000)) local formatted_ts = iso_timestamp .. "." .. milliseconds .. timezone_formatted
 -- 3. Message local message = record.message if type(message) == "table" then message = json.encode(message) end
 -- 4. Label merging local default_labels = {} local keys_to_remove = {} local merged_labels = {}
 for key, value in pairs(record) do if key:find("^default_labels.") then local subkey = key:sub(16) default_labels[subkey] = value table.insert(keys_to_remove, key) end end
 for _, key in ipairs(keys_to_remove) do record[key] = nil end
 for k, v in pairs(default_labels) do merged_labels[k] = v end
 if record.labels then for k, v in pairs(record.labels) do val, ok = ensure_string(v) if ok then merged_labels[k] = val else print("skip unsupported type value: "..k.." => "..v) end end end

 -- 5. Build log local log_entry = { timestamp = formatted_ts, level = record.level or "INFO", project_id = project_id, log_group_id = group_id, labels = merged_labels, message = message, json_message = extra_fields(record) }
 if record.trace_id and record.trace_id ~= "" then log_entry.trace_id = record.trace_id end
 if record.service_name and record.service_name ~= "" then log_entry.service_name = record.service_name end
 if record.instance_id and record.instance_id ~= "" then log_entry.instance_id = record.instance_id end

 -- 6. Complete return 1, timestamp, log_entryend
4. Откройте файл /etc/fluent-bit/fluent-bit.conf:
sudo nano /etc/fluent-bit/fluent-bit.conf
5. Добавьте в него данные в виде:
[SERVICE] Daemon Off Flush 1 Log_Level info Parsers_File parsers.conf storage.sync full
[INPUT] Name tail Path <path-to-log/logfile.log> Parser docker
[FILTER] Name parser Match * Key_Name log Parser json Reserve_Data true
# target section[FILTER] name modify match * Set default_project_id REPLACE_TO_PROJECT_ID Set default_group_id REPLACE_TO_LOG_GROUP_ID
#default labels section[FILTER] name modify match * Set default_labels.<label_name_1> value_A Set default_labels.<label_name_2> value_B
[FILTER] Name lua Match * Script logaas_format.lua Call format_log time_as_table true
[OUTPUT] Name http Match * Host logging.api.cloud.ru Port 443 tls on URI /api/v1/logs-ingest json_date_key false Header Authorization Api-Key REPLACE_TO_SA_API_KEY

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.
В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.
Измените файл, подставив в него свои данные:

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
REPLACE_TO_LOG_GROUP_ID — необязательная строка.
Если ее не добавить, логи отправятся в группу проекта по умолчанию (default-группа).
REPLACE_TO_SA_API_KEY — API-ключ сервисного аккаунта.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «logaas.writer».

Секция default labels section — опциональная.
В ней вы можете указать метки, которые будут добавлены ко всем логам.
Это удобно для последующей фильтрации логов с помощью [языка фильтрующих выражений](https://cloud.ru/docs/client-log/ug/topics/concepts__filter)языка фильтрующих выражений.
Метки указываются в виде default_labels.<label_name>, где <label_name> — имя метки, которая добавится к логам.
В следующем шаге инструкции настраивается тестовая отправка данных с помощью генератора логов, который записывает логи в лог-файл.
Для тестирования с помощью генератора вместо <path-to-log/logfile.log> укажите путь к лог-файлу: /usr/local/bin/log_producer/error_log.log.
Пример изменений в файле /etc/fluent-bit/fluent-bit.conf:
[SERVICE] Daemon Off Flush 1 Log_Level info Parsers_File parsers.conf storage.sync full
[INPUT] Name tail Path /usr/local/bin/log_producer/error_log.log Parser docker
[FILTER] Name parser Match * Key_Name log Parser json Reserve_Data true
# target section[FILTER] name modify match * Set default_project_id 00000000-1111-2222-3333-444444444444 Set default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
#default labels section[FILTER] name modify match * Set default_labels.some_field_A value_A Set default_labels.some_field_B value_B
[FILTER] Name lua Match * Script logaas_format.lua Call format_log time_as_table true
[OUTPUT] Name http Match * Host logging.api.cloud.ru Port 443 tls on URI /api/v1/logs-ingest json_date_key false Header Authorization Api-Key ZDVkNmVlY2EtxxxxxxxxxxxxxxxxhYTJhNGJl.xxxxxxxxxxxxx

Создайте файл logaas_format.lua для форматирования логов в формат сервиса «Клиентское логирование»:

```bash
sudo
touch
/etc/fluent-bit/logaas_format.lua
```

Откройте созданный файл с помощью редактора nano:

```bash
sudo
nano
/etc/fluent-bit/logaas_format.lua
```

В файл добавьте:

```bash
-- Fluent Bit lua client script
-- Version:
1.0
.1
-- Copyright
2025
Cloud.ru
-- Licensed under the Apache License, Version
2.0
(
the
"License"
)
;
-- you may not use this
file
except
in
compliance with the License.
-- You may obtain a copy of the License at
-- http://www.apache.org/licenses/LICENSE-2.0
-- Unless required by applicable law or agreed to
in
writing, software
-- distributed under the License is distributed on an
"AS IS"
BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License
for
the specific language governing permissions and
-- limitations under the License.
local
whitelist
=
{
"timestamp"
,
"level"
,
"project_id"
,
"log_group_id"
,
"default_labels"
,
"labels"
,
"message"
,
"json_message"
,
"trace_id"
,
"service_name"
,
"instance_id"
}
local
whitelist_hash
=
{
}
for
_, key
in
ipairs
(
whitelist
)
do
whitelist_hash
[
key
]
=
true
end
local
json
=
(
function
(
)
local
escape
=
function
(
str
)
return
str:gsub
(
'[\\"/]'
, function
(
c
)
return
'\\'
..
c
end
)
end
local
function
encode_value
(
val
)
local
t
=
type
(
val
)
if
t
==
'string'
then
return
'"'
..
escape
(
val
)
..
'"'
elseif t
==
'number'
or t
==
'boolean'
then
return
tostring
(
val
)
elseif t
==
'table'
then
local
result
=
{
}
for
k,
v
in
pairs
(
val
)
do
local
key
=
type
(
k
)
==
'number'
and
'['
..
k
..
']'
or
'"'
..
k
..
'"'
table.insert
(
result, key
..
':'
..
encode_value
(
v
))
end
return
'{'
..
table.concat
(
result,
','
)
..
'}'
else
return
'null'
end
end
return
{
encode
=
function
(
tbl
)
return
encode_value
(
tbl
)
end
}
end
)
(
)
function
extra_fields
(
record
)
local
message_
=
{
}
local
keys_to_remove
=
{
}
local
json_message
=
{
}
local
message_data
=
{
}
for
key, value
in
pairs
(
record
)
do
if
not whitelist_hash
[
key
]
then
message_data
[
key
]
=
value
table.insert
(
keys_to_remove, key
)
end
end
if
next
(
message_data
)
~
=
nil
then
json_message
=
json.encode
(
message_data
)
return
json_message
else
return
nil
end
end
function
ensure_string
(
var
)
if
type
(
var
)
==
"string"
then
return
var,
true
end
if
type
(
var
)
==
"number"
or type
(
var
)
==
"boolean"
then
return
tostring
(
var
)
,
true
end
return
nil,
false
end
function
format_log
(
tag, timestamp, record
)
--
1
. Project ID
&
Log Group ID
local
default_project_id
=
record.default_project_id
local
default_group_id
=
record.default_group_id
local
project_id
=
record.project_id
if
not project_id or project_id
==
""
then
project_id
=
default_project_id
end
local
group_id
=
record.group_id
if
not group_id or group_id
==
""
then
group_id
=
default_group_id
end
record.default_project_id
=
nil
record.default_group_id
=
nil
--
2
. Timestamp
local
system_timezone
=
os.date
(
"%z"
)
local
timezone_formatted
=
string.sub
(
system_timezone,
1
,
3
)
..
":"
..
string.sub
(
system_timezone,
4
,
5
)
local
sec
=
timestamp.sec
local
nsec
=
timestamp.nsec
local
iso_timestamp
=
os.date
(
"%Y-%m-%dT%H:%M:%S"
, sec
)
local
milliseconds
=
string.format
(
"%03d"
, math.floor
(
nsec /
1000000
))
local
formatted_ts
=
iso_timestamp
..
"."
..
milliseconds
..
timezone_formatted
--
3
. Message
local
message
=
record.message
if
type
(
message
)
==
"table"
then
message
=
json.encode
(
message
)
end
--
4
. Label merging
local
default_labels
=
{
}
local
keys_to_remove
=
{
}
local
merged_labels
=
{
}
for
key, value
in
pairs
(
record
)
do
if
key:find
(
"^default_labels."
)
then
local
subkey
=
key:sub
(
16
)
default_labels
[
subkey
]
=
value
table.insert
(
keys_to_remove, key
)
end
end
for
_, key
in
ipairs
(
keys_to_remove
)
do
record
[
key
]
=
nil
end
for
k,
v
in
pairs
(
default_labels
)
do
merged_labels
[
k
]
=
v
end
if
record.labels
then
for
k,
v
in
pairs
(
record.labels
)
do
val, ok
=
ensure_string
(
v
)
if
ok
then
merged_labels
[
k
]
=
val
else
print
(
"skip unsupported type value: "
..
k
..
" => "
..
v
)
end
end
end
--
5
. Build log
local
log_entry
=
{
timestamp
=
formatted_ts,
level
=
record.level or
"INFO"
,
project_id
=
project_id,
log_group_id
=
group_id,
labels
=
merged_labels,
message
=
message,
json_message
=
extra_fields
(
record
)
}
if
record.trace_id and record.trace_id ~
=
""
then
log_entry.trace_id
=
record.trace_id
end
if
record.service_name and record.service_name ~
=
""
then
log_entry.service_name
=
record.service_name
end
if
record.instance_id and record.instance_id ~
=
""
then
log_entry.instance_id
=
record.instance_id
end
--
6
. Complete
return
1
, timestamp, log_entry
end
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
Parsers_File parsers.conf
storage.sync full
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
FILTER
]
Name parser
Match *
Key_Name log
Parser json
Reserve_Data
true
# target section
[
FILTER
]
name modify
match *
Set default_project_id REPLACE_TO_PROJECT_ID
Set default_group_id REPLACE_TO_LOG_GROUP_ID
#default labels section
[
FILTER
]
name modify
match *
Set default_labels.
<
label_name_
1
>
value_A
Set default_labels.
<
label_name_
2
>
value_B
[
FILTER
]
Name lua
Match *
Script logaas_format.lua
Call format_log
time_as_table
true
[
OUTPUT
]
Name http
Match *
Host logging.api.cloud.ru
Port
443
tls on
URI /api/v1/logs-ingest
json_date_key
false
Header Authorization Api-Key REPLACE_TO_SA_API_KEY
```

Секция [INPUT] указывает на источник логов, а [OUTPUT] — на сервис, в который отправятся логи.

В режиме tail сбор логов в fluent-bit работает по принципу отслеживания новых записей в логах.
При перезапуске сервиса данные, обработанные ранее, не отправляются в систему повторно.

Измените файл, подставив в него свои данные:

- <path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.
- REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
REPLACE_TO_LOG_GROUP_ID — необязательная строка.
Если ее не добавить, логи отправятся в группу проекта по умолчанию (default-группа).
- REPLACE_TO_SA_API_KEY — API-ключ сервисного аккаунта.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «logaas.writer».

<path-to-log/logfile.log> — путь к файлу-источнику логов: fluent-bit будет сканировать этот файл и отслеживать в нем новые строки.

REPLACE_TO_PROJECT_ID и REPLACE_TO_LOG_GROUP_ID — ID проекта и ID лог-группы, в которую будут отправлены логи.
REPLACE_TO_LOG_GROUP_ID — необязательная строка.
Если ее не добавить, логи отправятся в группу проекта по умолчанию (default-группа).

REPLACE_TO_SA_API_KEY — API-ключ сервисного аккаунта.
Проверьте, что у вас есть доступ к проекту, а для вашего сервисного аккаунта выбраны роли «Пользователь сервисов» и «logaas.writer».

Секция default labels section — опциональная.
В ней вы можете указать метки, которые будут добавлены ко всем логам.
Это удобно для последующей фильтрации логов с помощью [языка фильтрующих выражений](https://cloud.ru/docs/client-log/ug/topics/concepts__filter)языка фильтрующих выражений.
Метки указываются в виде default_labels.<label_name>, где <label_name> — имя метки, которая добавится к логам.

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
Parsers_File parsers.conf
storage.sync full
[
INPUT
]
Name
tail
Path /usr/local/bin/log_producer/error_log.log
Parser
docker
[
FILTER
]
Name parser
Match *
Key_Name log
Parser json
Reserve_Data
true
# target section
[
FILTER
]
name modify
match *
Set default_project_id 00000000-1111-2222-3333-444444444444
Set default_group_id aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
#default labels section
[
FILTER
]
name modify
match *
Set default_labels.some_field_A value_A
Set default_labels.some_field_B value_B
[
FILTER
]
Name lua
Match *
Script logaas_format.lua
Call format_log
time_as_table
true
[
OUTPUT
]
Name http
Match *
Host logging.api.cloud.ru
Port
443
tls on
URI /api/v1/logs-ingest
json_date_key
false
Header Authorization Api-Key ZDVkNmVlY2EtxxxxxxxxxxxxxxxxhYTJhNGJl.xxxxxxxxxxxxx
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
generate_log() { # Generate @timestamp in UTC with 8 fractional seconds nanoseconds=$(date +"%N") trimmed_ns=${nanoseconds:0:8} timestamp=$(date -u "+%Y-%m-%dT%H:%M:%S.${trimmed_ns}Z")
 # Random log level selection levels=("TRACE" "DEBUG" "INFO" "NOTICE" "WARN" "ERROR" "CRITICAL" "ALERT" "EMERGENCY" "FATAL") level=${levels[$RANDOM % ${#levels[@]}]}
 # Thread selection threads=("rest-query-pool-1" "rest-query-pool-2" "worker-thread-3" "io-thread-4") thread=${threads[$RANDOM % ${#threads[@]}]}
 # Logger name (fixed) logger="ru.rtlabs.einfahrt.query.server.http.request.rquery.RQueryCaExecutorImpl" request_id=$(uuidgen) message="Результат исполнения запроса $request_id получен полностью" context="default" created_time=$(TZ="Europe/Moscow" date "+%Y-%m-%dT%H:%M:%S.%3N%:z")
 # Build MDC JSON mdc_json="\"mdc\":{" mdc_json+="\"requestId\":\"$request_id\"," mdc_json+="\"created\":\"$created_time\"" mdc_json+="}"
 # Construct single-line JSON printf '{"@timestamp":"%s","level":"%s","thread":"%s","logger":"%s","message":"%s","context":"%s",%s}\n' \ "$timestamp" \ "$level" \ "$thread" \ "$logger" \ "$message" \ "$context" \ "$mdc_json"}
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
# Generate @timestamp in UTC with 8 fractional seconds
nanoseconds
=
$(
date
+
"%N"
)
trimmed_ns
=
${nanoseconds
:
0
:
8}
timestamp
=
$(
date
-u
"+%Y-%m-%dT%H:%M:%S.
${trimmed_ns}
Z"
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
# Thread selection
threads
=
(
"rest-query-pool-1"
"rest-query-pool-2"
"worker-thread-3"
"io-thread-4"
)
thread
=
${threads
[
$RANDOM
%
${
#
threads
[
@
]
}
]
}
# Logger name (fixed)
logger
=
"ru.rtlabs.einfahrt.query.server.http.request.rquery.RQueryCaExecutorImpl"
request_id
=
$(
uuidgen
)
message
=
"Результат исполнения запроса
$request_id
получен полностью"
context
=
"default"
created_time
=
$(
TZ
=
"Europe/Moscow"
date
"+%Y-%m-%dT%H:%M:%S.%3N%:z"
)
# Build MDC JSON
mdc_json
=
"
\"
mdc
\"
:{"
mdc_json
+=
"
\"
requestId
\"
:
\"
$request_id
\"
,"
mdc_json
+=
"
\"
created
\"
:
\"
$created_time
\"
"
mdc_json
+=
"}"
# Construct single-line JSON
printf
'{"@timestamp":"%s","level":"%s","thread":"%s","logger":"%s","message":"%s","context":"%s",%s}\n'
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
$thread
"
\
"
$logger
"
\
"
$message
"
\
"
$context
"
\
"
$mdc_json
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
