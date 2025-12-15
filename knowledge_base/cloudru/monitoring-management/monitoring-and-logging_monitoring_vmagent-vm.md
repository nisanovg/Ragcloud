---
title: Мониторинг виртуальной машины с помощью vmagent
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm
topic: monitoring-management
---
# Мониторинг виртуальной машины с помощью vmagent

С помощью этого руководства вы настроите мониторинг виртуальной машины в сервисе «Мониторинг» с помощью плагина vmagent.
Плагин представляет собой легковесный агент для сбора метрик, который поддерживает протокол remote_write для отправки данных в системы мониторинга.

Вы будете использовать следующие сервисы:

- [Мониторинг](https://cloud.ru/docs/service-monitoring/ug/index)Мониторинг — сервис сбора и хранения метрик облачных ресурсов.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, для которой будет настроен мониторинг.
- vmagent — агент, автоматизирующий сбор метрик приложений, развернутых на виртуальной машине.
- Node Exporter — агент, собирающий мертики ОС на базе ядра Linux и передающий их в систему мониторинга Prometheus.

[Мониторинг](https://cloud.ru/docs/service-monitoring/ug/index)Мониторинг — сервис сбора и хранения метрик облачных ресурсов.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, для которой будет настроен мониторинг.

vmagent — агент, автоматизирующий сбор метрик приложений, развернутых на виртуальной машине.

Node Exporter — агент, собирающий мертики ОС на базе ядра Linux и передающий их в систему мониторинга Prometheus.

Шаги:

1. [Подготовьте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Подготовьте виртуальную машину.
2. [Установите vmagent](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Установите vmagent.
3. [Установите Node Exporter](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Установите Node Exporter.
4. [Настройте конфигурацию vmagent](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте конфигурацию vmagent.
5. [Запустите vmagent и настройте отправку метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Запустите vmagent и настройте отправку метрик.
6. [Cоздайте дашборд в сервисе «Мониторинг»](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Cоздайте дашборд в сервисе «Мониторинг».
7. [Настройте алерты](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте алерты.
8. [Проверьте доступность метрик в сервисе](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Проверьте доступность метрик в сервисе.
9. [Проверьте уведомления об алертах](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Проверьте уведомления об алертах.
10. [Оптимизируйте сбор метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Оптимизируйте сбор метрик.
11. [Настройте дополнительные экспортеры](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте дополнительные экспортеры.

[Подготовьте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Подготовьте виртуальную машину.

[Установите vmagent](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Установите vmagent.

[Установите Node Exporter](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Установите Node Exporter.

[Настройте конфигурацию vmagent](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте конфигурацию vmagent.

[Запустите vmagent и настройте отправку метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Запустите vmagent и настройте отправку метрик.

[Cоздайте дашборд в сервисе «Мониторинг»](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Cоздайте дашборд в сервисе «Мониторинг».

[Настройте алерты](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте алерты.

[Проверьте доступность метрик в сервисе](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Проверьте доступность метрик в сервисе.

[Проверьте уведомления об алертах](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Проверьте уведомления об алертах.

[Оптимизируйте сбор метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Оптимизируйте сбор метрик.

[Настройте дополнительные экспортеры](https://cloud.ru/docs/tutorials-evolution/list/topics/monitoring-and-logging__monitoring__vmagent-vm)Настройте дополнительные экспортеры.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
При создании в поле Сервисы выберите роль «monaas.write».
3. Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.
4. [Получите авторизационный токен](https://cloud.ru/docs/console_api/ug/topics/guides__auth_api)Получите авторизационный токен.
5. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu.
6. Убедитесь, что в сервисе «Виртуальные машины» у вас есть [права администратора](https://cloud.ru/docs/virtual-machines/ug/topics/security)права администратора для установки программного обеспечения.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт.
При создании в поле Сервисы выберите роль «monaas.write».

Для сервисного аккаунта [создайте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)создайте ключи доступа.

[Получите авторизационный токен](https://cloud.ru/docs/console_api/ug/topics/guides__auth_api)Получите авторизационный токен.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину Ubuntu.

Убедитесь, что в сервисе «Виртуальные машины» у вас есть [права администратора](https://cloud.ru/docs/virtual-machines/ug/topics/security)права администратора для установки программного обеспечения.

## 1. Подготовьте виртуальную машину

1. После создания виртуальной машины подключитесь к ней по SSH:
ssh username@your-vm-ip-address
2. Обновите системные пакеты.
sudo apt update && sudo apt upgrade -y

После создания виртуальной машины подключитесь к ней по SSH:

```bash
ssh
username@your-vm-ip-address
```

Обновите системные пакеты.

```bash
sudo
apt
update
&&
sudo
apt
upgrade
-y
```

## 2. Установите vmagent

1. Создайте директорию для vmagent:
sudo mkdir -p /opt/vmagentcd /opt/vmagent
2. Загрузите последний релиз vmagent. Пример для amd64:
sudo wget https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.126.0/vmutils-linux-amd64-v1.126.0.tar.gz
3. Распакуйте архив:
sudo tar -xvzf vmutils-linux-amd64-v1.126.0.tar.gz

Создайте директорию для vmagent:

```bash
sudo
mkdir
-p
/opt/vmagent
cd
/opt/vmagent
```

Загрузите последний релиз vmagent. Пример для amd64:

```bash
sudo
wget
https://github.com/VictoriaMetrics/VictoriaMetrics/releases/download/v1.126.0/vmutils-linux-amd64-v1.126.0.tar.gz
```

Распакуйте архив:

```bash
sudo
tar
-xvzf
vmutils-linux-amd64-v1.126.0.tar.gz
```

## 3. Установите Node Exporter

1. Создайте директорию для Node Exporter:
sudo mkdir -p /opt/node_exportercd /opt/node_exporter
2. Скачайте дистрибутив Node Exporter:
sudo wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
3. Распакуйте архив:
sudo tar -xvzf node_exporter-1.9.1.linux-amd64.tar.gz
4. Скопируйте бинарный файл в директорию /opt/node_exporter:
sudo cp node_exporter-1.9.1.linux-amd64/node_exporter ./
5. Создайте службу systemd для Node Exporter с помощью текстового редактора, например vi:
sudo vi /etc/systemd/system/node_exporter.service
6. В файл добавьте данные в виде:
[Unit]Description=Node ExporterAfter=network.target
[Service]User=node_exporterGroup=node_exporterType=simpleExecStart=/opt/node_exporter/node_exporter
[Install]WantedBy=multi-user.target
7. Создайте пользователя для Node Exporter:
sudo useradd -rs /bin/false node_exporter
8. Запустите службу и проверьте ее состояние:
sudo systemctl daemon-reloadsudo systemctl enable --now node_exportersudo systemctl status node_exporter

Создайте директорию для Node Exporter:

```bash
sudo
mkdir
-p
/opt/node_exporter
cd
/opt/node_exporter
```

Скачайте дистрибутив Node Exporter:

```bash
sudo
wget
https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
```

Распакуйте архив:

```bash
sudo
tar
-xvzf
node_exporter-1.9.1.linux-amd64.tar.gz
```

Скопируйте бинарный файл в директорию /opt/node_exporter:

```bash
sudo
cp
node_exporter-1.9.1.linux-amd64/node_exporter ./
```

Создайте службу systemd для Node Exporter с помощью текстового редактора, например vi:

```bash
sudo
vi
/etc/systemd/system/node_exporter.service
```

В файл добавьте данные в виде:

```bash
[
Unit
]
Description
=
Node Exporter
After
=
network.target
[
Service
]
User
=
node_exporter
Group
=
node_exporter
Type
=
simple
ExecStart
=
/opt/node_exporter/node_exporter
[
Install
]
WantedBy
=
multi-user.target
```

Создайте пользователя для Node Exporter:

```bash
sudo
useradd
-rs
/bin/false node_exporter
```

Запустите службу и проверьте ее состояние:

```bash
sudo
systemctl daemon-reload
sudo
systemctl
enable
--now
node_exporter
sudo
systemctl status node_exporter
```

## 4. Настройте конфигурацию vmagent

1. Создайте файл конфигурации для vmagent:
sudo vi /opt/vmagent/vmagent-config.yml
2. В файл добавьте данные в виде:
global: scrape_interval: 15s external_labels: monitor: 'vm-agent'
scrape_configs: - job_name: 'node-exporter' static_configs: - targets: ['localhost:9100'] metrics_path: /metrics
 - job_name: 'vmagent' static_configs: - targets: ['localhost:8429'] metrics_path: /metrics

Создайте файл конфигурации для vmagent:

```bash
sudo
vi
/opt/vmagent/vmagent-config.yml
```

В файл добавьте данные в виде:

```bash
global
:
scrape_interval
:
15s
external_labels
:
monitor
:
'vm-agent'
scrape_configs
:
-
job_name
:
'node-exporter'
static_configs
:
-
targets
:
[
'localhost:9100'
]
metrics_path
:
/metrics
-
job_name
:
'vmagent'
static_configs
:
-
targets
:
[
'localhost:8429'
]
metrics_path
:
/metrics
```

## 5. Запустите vmagent и настройте отправку метрик

На этом этапе вы создадите службу vmagent с конфигурацией для отправки метрик в сервис «Мониторинг».

1. Создайте файл службы vmagent:
sudo vi /etc/systemd/system/vmagent.service
2. В файл добавьте данные в виде:
[Unit]Description=vmagentAfter=network.target
[Service]Type=simpleUser=vmagentGroup=vmagentExecStart=/opt/vmagent/vmagent-prod --promscrape.config=/opt/vmagent/vmagent-config.yml --remoteWrite.tmpDataPath=/opt/vmagent/data --remoteWrite.maxDiskUsagePerURL=10737418240 --remoteWrite.url="https://monitoring.api.cloud.ru/v2/project/{project_ID}/prometheus/api/v1/write" --remoteWrite.oauth2.clientID="{clientID}" --remoteWrite.oauth2.clientSecret="{clientSecret}" --remoteWrite.oauth2.tokenUrl=https://auth.iam.sbercloud.ru/auth/system/openid/token --remoteWrite.oauth2.endpointParams='{"grant_type": "access_key"}'Restart=alwaysRestartSec=10
[Install]WantedBy=multi-user.target

Где:

{project_ID} — идентификатор проекта, куда будут отправляться метрики.
Вы можете скопировать его из URL личного кабинета.
{clientID} — Key ID (логин) сервисного аккаунта с ролью «monaas.write».
{clientSecret} — Key Secret (пароль) сервисного аккаунта.
3. Создайте пользователя для vmagent:
sudo useradd -rs /bin/false vmagent
4. Назначьте права на директорию:
sudo chown -R vmagent:vmagent /opt/vmagent
5. Запустите службу vmagent и проверьте ее состояние:
sudo systemctl daemon-reloadsudo systemctl enable --now vmagentsudo systemctl status vmagent

Создайте файл службы vmagent:

```bash
sudo
vi
/etc/systemd/system/vmagent.service
```

В файл добавьте данные в виде:

```bash
[
Unit
]
Description
=
vmagent
After
=
network.target
[
Service
]
Type
=
simple
User
=
vmagent
Group
=
vmagent
ExecStart
=
/opt/vmagent/vmagent-prod
--promscrape.config
=
/opt/vmagent/vmagent-config.yml
--remoteWrite.tmpDataPath
=
/opt/vmagent/data
--remoteWrite.maxDiskUsagePerURL
=
10737418240
--remoteWrite.url
=
"https://monitoring.api.cloud.ru/v2/project/{project_ID}/prometheus/api/v1/write"
--remoteWrite.oauth2.clientID
=
"{clientID}"
--remoteWrite.oauth2.clientSecret
=
"{clientSecret}"
--remoteWrite.oauth2.tokenUrl
=
https://auth.iam.sbercloud.ru/auth/system/openid/token
--remoteWrite.oauth2.endpointParams
=
'{"grant_type": "access_key"}'
Restart
=
always
RestartSec
=
10
[
Install
]
WantedBy
=
multi-user.target
```

Где:

- {project_ID} — идентификатор проекта, куда будут отправляться метрики.
Вы можете скопировать его из URL личного кабинета.
- {clientID} — Key ID (логин) сервисного аккаунта с ролью «monaas.write».
- {clientSecret} — Key Secret (пароль) сервисного аккаунта.

{project_ID} — идентификатор проекта, куда будут отправляться метрики.
Вы можете скопировать его из URL личного кабинета.

{clientID} — Key ID (логин) сервисного аккаунта с ролью «monaas.write».

{clientSecret} — Key Secret (пароль) сервисного аккаунта.

Создайте пользователя для vmagent:

```bash
sudo
useradd
-rs
/bin/false vmagent
```

Назначьте права на директорию:

```bash
sudo
chown
-R
vmagent:vmagent /opt/vmagent
```

Запустите службу vmagent и проверьте ее состояние:

```bash
sudo
systemctl daemon-reload
sudo
systemctl
enable
--now
vmagent
sudo
systemctl status vmagent
```

## 6. Cоздайте дашборд в сервисе «Мониторинг»

1. В сервисе «Мониторинг» перейдите в раздел Мониторинг → Дашборды → Пользовательские.
2. Нажмите Создать дашборд.
Укажите его название: «Мониторинг ВМ».
3. Перейдите на страницу дашборда и [добавьте виджеты](https://cloud.ru/docs/service-monitoring/ug/topics/custom-dashboard__widget)добавьте виджеты:

Виджет для отслеживания использования CPU:

Тип виджета: Временной ряд.
Название: «Использование CPU».
Описание: «Средняя загрузка CPU в процентах за 5 минут (100% минус время idle)».
Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100

Настройка левой оси: категория Проценты (0-100).

Виджет для отслеживания объема доступной оперативной памяти:

Тип виджета: Временной ряд.
Название: «Использование памяти».
Описание: «Объем доступной оперативной памяти».
Запрос:
node_memory_MemAvailable_bytes{monitor="vm-agent"}

Настройка левой оси: категория Объем данных.

Виджет для отслеживания свободного места на корневом разделе диска:

Тип виджета: Временной ряд.
Название: «Дисковое пространство».
Описание: «Свободное место на корневом разделе диска (в байтах)».
Запрос:
node_filesystem_avail_bytes {monitor="vm-agent"}

Легенда:
device: {{device}}; mountpoint: {{mountpoint}}

Настройка левой оси: категория Объем данных.

Виджет для отслеживания сетевого трафика:

Тип виджета: Временной ряд.
Название: «Сетевая активность».
Описание: «Входящий и исходящий сетевой трафик (в байтах)».
Запрос для входящего трафика:
rate(node_network_receive_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (входящий) (б/с)

Запрос для исходящего трафика:
rate(node_network_transmit_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (исходящий) (б/с)

Настройка левой оси: категория Передача данных.

В сервисе «Мониторинг» перейдите в раздел Мониторинг → Дашборды → Пользовательские.

Нажмите Создать дашборд.
Укажите его название: «Мониторинг ВМ».

Перейдите на страницу дашборда и [добавьте виджеты](https://cloud.ru/docs/service-monitoring/ug/topics/custom-dashboard__widget)добавьте виджеты:

1. Виджет для отслеживания использования CPU:

Тип виджета: Временной ряд.
Название: «Использование CPU».
Описание: «Средняя загрузка CPU в процентах за 5 минут (100% минус время idle)».
Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100

Настройка левой оси: категория Проценты (0-100).
2. Виджет для отслеживания объема доступной оперативной памяти:

Тип виджета: Временной ряд.
Название: «Использование памяти».
Описание: «Объем доступной оперативной памяти».
Запрос:
node_memory_MemAvailable_bytes{monitor="vm-agent"}

Настройка левой оси: категория Объем данных.
3. Виджет для отслеживания свободного места на корневом разделе диска:

Тип виджета: Временной ряд.
Название: «Дисковое пространство».
Описание: «Свободное место на корневом разделе диска (в байтах)».
Запрос:
node_filesystem_avail_bytes {monitor="vm-agent"}

Легенда:
device: {{device}}; mountpoint: {{mountpoint}}

Настройка левой оси: категория Объем данных.
4. Виджет для отслеживания сетевого трафика:

Тип виджета: Временной ряд.
Название: «Сетевая активность».
Описание: «Входящий и исходящий сетевой трафик (в байтах)».
Запрос для входящего трафика:
rate(node_network_receive_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (входящий) (б/с)

Запрос для исходящего трафика:
rate(node_network_transmit_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (исходящий) (б/с)

Настройка левой оси: категория Передача данных.

Виджет для отслеживания использования CPU:

1. Тип виджета: Временной ряд.
2. Название: «Использование CPU».
3. Описание: «Средняя загрузка CPU в процентах за 5 минут (100% минус время idle)».
4. Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100
5. Настройка левой оси: категория Проценты (0-100).

Тип виджета: Временной ряд.

Название: «Использование CPU».

Описание: «Средняя загрузка CPU в процентах за 5 минут (100% минус время idle)».

Запрос:

```bash
100
-
(
avg by
(
instance
)
(
rate
(
node_cpu_seconds_total
{
mode
=
"idle"
,
monitor
=
"vm-agent"
}
[
5m
]
))
)
*
100
```

Настройка левой оси: категория Проценты (0-100).

Виджет для отслеживания объема доступной оперативной памяти:

1. Тип виджета: Временной ряд.
2. Название: «Использование памяти».
3. Описание: «Объем доступной оперативной памяти».
4. Запрос:
node_memory_MemAvailable_bytes{monitor="vm-agent"}
5. Настройка левой оси: категория Объем данных.

Тип виджета: Временной ряд.

Название: «Использование памяти».

Описание: «Объем доступной оперативной памяти».

Запрос:

```bash
node_memory_MemAvailable_bytes
{
monitor
=
"vm-agent"
}
```

Настройка левой оси: категория Объем данных.

Виджет для отслеживания свободного места на корневом разделе диска:

1. Тип виджета: Временной ряд.
2. Название: «Дисковое пространство».
3. Описание: «Свободное место на корневом разделе диска (в байтах)».
4. Запрос:
node_filesystem_avail_bytes {monitor="vm-agent"}

Легенда:
device: {{device}}; mountpoint: {{mountpoint}}
5. Настройка левой оси: категория Объем данных.

Тип виджета: Временной ряд.

Название: «Дисковое пространство».

Описание: «Свободное место на корневом разделе диска (в байтах)».

Запрос:

```bash
node_filesystem_avail_bytes
{
monitor
=
"vm-agent"
}
```

Легенда:

```bash
device:
{
{
device
}
}
;
mountpoint:
{
{
mountpoint
}
}
```

Настройка левой оси: категория Объем данных.

Виджет для отслеживания сетевого трафика:

1. Тип виджета: Временной ряд.
2. Название: «Сетевая активность».
3. Описание: «Входящий и исходящий сетевой трафик (в байтах)».
4. Запрос для входящего трафика:
rate(node_network_receive_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (входящий) (б/с)
5. Запрос для исходящего трафика:
rate(node_network_transmit_bytes_total{device!~"lo|veth.*"}[5m])

Легенда:
Сетевой трафик (исходящий) (б/с)
6. Настройка левой оси: категория Передача данных.

Тип виджета: Временной ряд.

Название: «Сетевая активность».

Описание: «Входящий и исходящий сетевой трафик (в байтах)».

Запрос для входящего трафика:

```bash
rate
(
node_network_receive_bytes_total
{
device
!
~
"lo|veth.*"
}
[
5m
]
)
```

Легенда:

```bash
Сетевой трафик
(
входящий
)
(
б/с
)
```

Запрос для исходящего трафика:

```bash
rate
(
node_network_transmit_bytes_total
{
device
!
~
"lo|veth.*"
}
[
5m
]
)
```

Легенда:

```bash
Сетевой трафик
(
исходящий
)
(
б/с
)
```

Настройка левой оси: категория Передача данных.

## 7. Настройте алерты

1. В сервисе «Мониторинг» перейдите в раздел Мониторинг → Алерты мониторинга → Правила алертов.
2. [Создайте правила алертов](https://cloud.ru/docs/service-monitoring/ug/topics/alerts)Создайте правила алертов для ключевых метрик:

Правило, срабатывающее при загрузке CPU выше 90% в течение 5 минут:

Название: «Высокая загрузка CPU на vm».
Описание: «Утилизация CPU на VM более 90% за 5 минут».
Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100 > 0.90

Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «CPU».

Правило, срабатывающее при использование памяти более чем на 90%:

Название: «Высокая утилизация RAM на vm».
Описание: «Утилизация RAM на VM более 90% за 5 минут».
Запрос:
(node_memory_MemTotal_bytes{monitor="vm-agent"}-node_memory_MemAvailable_bytes{monitor="vm-agent"})/node_memory_MemTotal_bytes{monitor="vm-agent"} > 0.90

Частота проверки: 5 минут.
Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «RAM».

Правило, срабатывающее при заполненности дискового пространства более чем на 85%:

Название: «Диск заполнен более чем на 85%».
Описание: «Дисковое пространство заполнено более чем на 85%».
Запрос:
(node_filesystem_size_bytes {monitor="vm-agent"}-node_filesystem_avail_bytes {monitor="vm-agent"})/node_filesystem_size_bytes {monitor="vm-agent"} > 0.85

Частота проверки: 5 минут.
Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «DISK».

В сервисе «Мониторинг» перейдите в раздел Мониторинг → Алерты мониторинга → Правила алертов.

[Создайте правила алертов](https://cloud.ru/docs/service-monitoring/ug/topics/alerts)Создайте правила алертов для ключевых метрик:

1. Правило, срабатывающее при загрузке CPU выше 90% в течение 5 минут:

Название: «Высокая загрузка CPU на vm».
Описание: «Утилизация CPU на VM более 90% за 5 минут».
Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100 > 0.90

Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «CPU».
2. Правило, срабатывающее при использование памяти более чем на 90%:

Название: «Высокая утилизация RAM на vm».
Описание: «Утилизация RAM на VM более 90% за 5 минут».
Запрос:
(node_memory_MemTotal_bytes{monitor="vm-agent"}-node_memory_MemAvailable_bytes{monitor="vm-agent"})/node_memory_MemTotal_bytes{monitor="vm-agent"} > 0.90

Частота проверки: 5 минут.
Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «RAM».
3. Правило, срабатывающее при заполненности дискового пространства более чем на 85%:

Название: «Диск заполнен более чем на 85%».
Описание: «Дисковое пространство заполнено более чем на 85%».
Запрос:
(node_filesystem_size_bytes {monitor="vm-agent"}-node_filesystem_avail_bytes {monitor="vm-agent"})/node_filesystem_size_bytes {monitor="vm-agent"} > 0.85

Частота проверки: 5 минут.
Важность: Высокая.
Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «DISK».

Правило, срабатывающее при загрузке CPU выше 90% в течение 5 минут:

1. Название: «Высокая загрузка CPU на vm».
2. Описание: «Утилизация CPU на VM более 90% за 5 минут».
3. Запрос:
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle", monitor="vm-agent"}[5m]))) * 100 > 0.90
4. Важность: Высокая.
5. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.
6. Ресурс: «CPU».

Название: «Высокая загрузка CPU на vm».

Описание: «Утилизация CPU на VM более 90% за 5 минут».

Запрос:

```bash
100
-
(
avg by
(
instance
)
(
rate
(
node_cpu_seconds_total
{
mode
=
"idle"
,
monitor
=
"vm-agent"
}
[
5m
]
))
)
*
100
>
0.90
```

Важность: Высокая.

Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

- название;
- ID;
- название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

название;

ID;

название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «CPU».

Правило, срабатывающее при использование памяти более чем на 90%:

1. Название: «Высокая утилизация RAM на vm».
2. Описание: «Утилизация RAM на VM более 90% за 5 минут».
3. Запрос:
(node_memory_MemTotal_bytes{monitor="vm-agent"}-node_memory_MemAvailable_bytes{monitor="vm-agent"})/node_memory_MemTotal_bytes{monitor="vm-agent"} > 0.90
4. Частота проверки: 5 минут.
5. Важность: Высокая.
6. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.
7. Ресурс: «RAM».

Название: «Высокая утилизация RAM на vm».

Описание: «Утилизация RAM на VM более 90% за 5 минут».

Запрос:

```bash
(
node_memory_MemTotal_bytes
{
monitor
=
"vm-agent"
}
-node_memory_MemAvailable_bytes
{
monitor
=
"vm-agent"
}
)
/node_memory_MemTotal_bytes
{
monitor
=
"vm-agent"
}
>
0.90
```

Частота проверки: 5 минут.

Важность: Высокая.

Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

- название;
- ID;
- название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

название;

ID;

название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «RAM».

Правило, срабатывающее при заполненности дискового пространства более чем на 85%:

1. Название: «Диск заполнен более чем на 85%».
2. Описание: «Дисковое пространство заполнено более чем на 85%».
3. Запрос:
(node_filesystem_size_bytes {monitor="vm-agent"}-node_filesystem_avail_bytes {monitor="vm-agent"})/node_filesystem_size_bytes {monitor="vm-agent"} > 0.85
4. Частота проверки: 5 минут.
5. Важность: Высокая.
6. Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

название;
ID;
название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.
7. Ресурс: «DISK».

Название: «Диск заполнен более чем на 85%».

Описание: «Дисковое пространство заполнено более чем на 85%».

Запрос:

```bash
(
node_filesystem_size_bytes
{
monitor
=
"vm-agent"
}
-node_filesystem_avail_bytes
{
monitor
=
"vm-agent"
}
)
/node_filesystem_size_bytes
{
monitor
=
"vm-agent"
}
>
0.85
```

Частота проверки: 5 минут.

Важность: Высокая.

Объект: выберите, для какой виртуальной машины создается правило алерта, указав любой из ее параметров:

- название;
- ID;
- название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

название;

ID;

название лейбла метрики, в котором содержится название виртуальной машины, в формате {{.label}}.

Ресурс: «DISK».

## 8. Проверьте доступность метрик в сервисе

1. Проверьте состояние служб на виртуальной машине:
sudo systemctl status node_exportersudo systemctl status vmagent
2. Проверьте логи vmagent на наличие ошибок:
sudo journalctl -u vmagent.service -f
3. Убедитесь, что метрики поступают в сервис «Мониторинг».
4. Проверьте, что на виджетах дашборда «Мониторинг ВМ» отображаются показатели.

Проверьте состояние служб на виртуальной машине:

```bash
sudo
systemctl status node_exporter
sudo
systemctl status vmagent
```

Проверьте логи vmagent на наличие ошибок:

```bash
sudo
journalctl
-u
vmagent.service
-f
```

Убедитесь, что метрики поступают в сервис «Мониторинг».

Проверьте, что на виджетах дашборда «Мониторинг ВМ» отображаются показатели.

## 9. Проверьте уведомления об алертах

1. Чтобы провести нагрузочное тестирование и проверить, что алерты работают, установите утилиту stress-ng на виртуальную машину:
sudo apt-get install stress-ng
2. Создайте нагрузку на CPU для тестирования оповещений:
stress-ng --cpu 4 --timeout 300s
3. Проверьте, что на созданном дашборде отображается высокая утилизация CPU.
4. Проверьте, что срабатывает алерт о высокой загрузке CPU.

Чтобы провести нагрузочное тестирование и проверить, что алерты работают, установите утилиту stress-ng на виртуальную машину:

```bash
sudo
apt-get
install
stress-ng
```

Создайте нагрузку на CPU для тестирования оповещений:

```bash
stress-ng
--cpu
4
--timeout
300s
```

Проверьте, что на созданном дашборде отображается высокая утилизация CPU.

Проверьте, что срабатывает алерт о высокой загрузке CPU.

## 10. Оптимизируйте сбор метрик

Для оптимизации производительности vmagent:

1. Настройте фильтрацию метрик: используйте relabel_configs, чтобы отфильтровать ненужные метрики.
2. Настройте часоту сбора метрик: задайте подходящее значение scrape_interval.
3. Оптимизируйте параметры буферизации для нестабильных сетей.
Пример оптимизированной конфигурации vmagent, расположенной в файле /opt/vmagent/vmagent-config.yml:
global: scrape_interval: 30s scrape_timeout: 25s
scrape_configs: - job_name: 'node-exporter' static_configs: - targets: ['localhost:9100'] metrics_path: /metrics relabel_configs: - source_labels: [__name__] regex: '(node_cpu_seconds_total|node_memory_MemAvailable_bytes| node_memory_MemTotal_bytes|node_disk_io_time_seconds_total| node_network_transmit_bytes_total|node_network_receive_bytes_total| node_filesystem_size_bytes| node_filesystem_avail_bytes|)' action: keep

В сервис «Мониторинг» будут отправляться только метрики, указанные в regex.

Настройте фильтрацию метрик: используйте relabel_configs, чтобы отфильтровать ненужные метрики.

Настройте часоту сбора метрик: задайте подходящее значение scrape_interval.

Оптимизируйте параметры буферизации для нестабильных сетей.
Пример оптимизированной конфигурации vmagent, расположенной в файле /opt/vmagent/vmagent-config.yml:

```bash
global
:
scrape_interval
:
30s
scrape_timeout
:
25s
scrape_configs
:
-
job_name
:
'node-exporter'
static_configs
:
-
targets
:
[
'localhost:9100'
]
metrics_path
:
/metrics
relabel_configs
:
-
source_labels
:
[
__name__
]
regex
:
'(node_cpu_seconds_total|node_memory_MemAvailable_bytes| node_memory_MemTotal_bytes|node_disk_io_time_seconds_total| node_network_transmit_bytes_total|node_network_receive_bytes_total| node_filesystem_size_bytes| node_filesystem_avail_bytes|)'
action
:
keep
```

В сервис «Мониторинг» будут отправляться только метрики, указанные в regex.

## 11. Настройте дополнительные экспортеры

Для расширенного мониторинга установите дополнительные экспортеры:

- для мониторинга Docker — cadvisor;
- для мониторинга веб-сервера — nginx-exporter или apache-exporter;
- для мониторинга баз данных — mysqld-exporter.

для мониторинга Docker — cadvisor;

для мониторинга веб-сервера — nginx-exporter или apache-exporter;

для мониторинга баз данных — mysqld-exporter.

## Результат

Вы запустили vmagent для мониторинга виртуальной машины на базе Ubuntu, настроили сбор и отправку метрик в сервис «Мониторинг», создали дашборд для отслеживания показателей и настроили оповещения по основным метрикам.
