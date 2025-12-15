---
title: Организация CI/CD и мониторинга приложения
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus
topic: compute
---
# Организация CI/CD и мониторинга приложения

С помощью этого руководства вы научитесь настраивать полный цикл непрерывной интеграции и доставки (CI/CD) для веб-приложения на Python Flask, а также
развертывать систему мониторинга на основе Prometheus и Grafana для обеспечения наблюдаемости работы приложения.

Для этого вы выполните следующие задачи:

- Создадите автоматизированный пайплайн CI/CD в GitVerse.
- Настроите безопасную сборку Docker-образов с автоматическим тестированием и проверкой уязвимостей.
- Развернете Flask-приложение с промышленным WSGI-сервером Gunicorn.
- Настроите мониторинг с помощью стека Prometheus + Grafana.
- Реализуете сбор метрик с помощью Node Exporter и cAdvisor.
- Создадите дашборды для визуализации метрик производительности и доступности.

Создадите автоматизированный пайплайн CI/CD в GitVerse.

Настроите безопасную сборку Docker-образов с автоматическим тестированием и проверкой уязвимостей.

Развернете Flask-приложение с промышленным WSGI-сервером Gunicorn.

Настроите мониторинг с помощью стека Prometheus + Grafana.

Реализуете сбор метрик с помощью Node Exporter и cAdvisor.

Создадите дашборды для визуализации метрик производительности и доступности.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальным машинам через интернет.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- [GitVerse](https://gitverse.ru/home)GitVerse — платформа для совместной работы с исходным кодом.
- [Prometheus](https://prometheus.io/)Prometheus — система мониторинга, сбора и хранения метрик.
- [Grafana](https://grafana.com/)Grafana — платформа для визуализации, мониторинга и анализа данных.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальным машинам через интернет.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

[GitVerse](https://gitverse.ru/home)GitVerse — платформа для совместной работы с исходным кодом.

[Prometheus](https://prometheus.io/)Prometheus — система мониторинга, сбора и хранения метрик.

[Grafana](https://grafana.com/)Grafana — платформа для визуализации, мониторинга и анализа данных.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Разверните ресурсы в облаке.
2. [Настройте окружение виртуальных машин и установите Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте окружение виртуальных машин и установите Docker.
3. [Настройте агенты сбора метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте агенты сбора метрик.
4. [Настройте Prometheus и Grafana](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте Prometheus и Grafana.
5. [Настройте пайплайн CI/CD в GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте пайплайн CI/CD в GitVerse.
6. [Разверните Flask-приложение на ВМ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Разверните Flask-приложение на ВМ.
7. [Настройте дашборды мониторинга](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте дашборды мониторинга.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Разверните ресурсы в облаке.

[Настройте окружение виртуальных машин и установите Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте окружение виртуальных машин и установите Docker.

[Настройте агенты сбора метрик](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте агенты сбора метрик.

[Настройте Prometheus и Grafana](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте Prometheus и Grafana.

[Настройте пайплайн CI/CD в GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте пайплайн CI/CD в GitVerse.

[Разверните Flask-приложение на ВМ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Разверните Flask-приложение на ВМ.

[Настройте дашборды мониторинга](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__gitverse-grafana-prometheus)Настройте дашборды мониторинга.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Разверните ресурсы в облаке

На этом шаге вы подготовите инфраструктуру проекта: создадите две виртуальные машины с публичными IP-адресами и настроите для них правила фильтрации трафика.

- app-vm — целевая виртуальная машина для приложения, на которой будет располагаться контейнер с Flask-API и экспортеры метрик.
- monitoring-vm — инфраструктурная виртуальная машина, на которой будут располагаться GitVerse Runner, Prometheus, Grafana.

app-vm — целевая виртуальная машина для приложения, на которой будет располагаться контейнер с Flask-API и экспортеры метрик.

monitoring-vm — инфраструктурная виртуальная машина, на которой будут располагаться GitVerse Runner, Prometheus, Grafana.

Все создаваемые ресурсы должны располагаться в одной

1. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.
2. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием app-vm-sg и добавьте в нее правила со следующими параметрами:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP5000IP-адрес0.0.0.0/0ВходящийTCP9100IP-адрес0.0.0.0/0ВходящийTCP8080IP-адрес0.0.0.0/0ИсходящийЛюбой—IP-адрес0.0.0.0/0
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием monitoring-vm-sg и добавьте в нее правила со следующими параметрами:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP9090IP-адрес0.0.0.0/0ВходящийTCP3000IP-адрес0.0.0.0/0ИсходящийЛюбой—IP-адрес0.0.0.0/0
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — app-vm.
Зона доступности — та же, что у группы безопасности.
Образ — на вкладке Публичные выберите образ Ubuntu 22.04.
Гарантированная доля vCPU — 10%.
Сетевой интерфейс — выберите тип Публичный IP.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — app-vm-sg и группа безопасности по умолчанию.
Логин — оставьте значение по умолчанию или укажите новый.
Метод аутентификации — Публичный ключ и Пароль.
Пароль — задайте пароль пользователя.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.
5. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — monitoring-vm.
Зона доступности — та же, что у группы безопасности.
Образ — на вкладке Публичные выберите образ Ubuntu 22.04.
Гарантированная доля vCPU — 10%.
vCPU, шт — 4.
RAM, ГБ — 8.
Диски — SSD-диск 40 ГБ.
Сетевой интерфейс — выберите тип Публичный IP.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — monitoring-vm-sg и группа безопасности по умолчанию.
Логин — оставьте значение по умолчанию или укажите новый.
Метод аутентификации — Публичный ключ и Пароль.
Пароль — задайте пароль пользователя.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.
6. Убедитесь, что ресурсы созданы и отображаются в личном кабинете:

На странице Сети → Группы безопасности отображаются группы безопасности app-vm-sg и monitoring-vm-sg со статусом «Создана».
На странице Инфраструктура → Виртуальные машины отображаются виртуальные машины app-vm и monitoring-vm со статусом «Запущена».
7. Запишите публичные IP-адреса каждой виртуальной машины.
В этом руководстве используются следующие IP-адреса:

app-vm — 176.109.105.170;
monitoring-vm — 176.123.164.242.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием app-vm-sg и добавьте в нее правила со следующими параметрами:

Трафик

Протокол

Порт

Тип источника/адресата

Источник/Адресат

Входящий

TCP

5000

IP-адрес

0.0.0.0/0

Входящий

TCP

9100

IP-адрес

0.0.0.0/0

Входящий

TCP

8080

IP-адрес

0.0.0.0/0

Исходящий

Любой

—

IP-адрес

0.0.0.0/0

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием monitoring-vm-sg и добавьте в нее правила со следующими параметрами:

Трафик

Протокол

Порт

Тип источника/адресата

Источник/Адресат

Входящий

TCP

9090

IP-адрес

0.0.0.0/0

Входящий

TCP

3000

IP-адрес

0.0.0.0/0

Исходящий

Любой

—

IP-адрес

0.0.0.0/0

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — app-vm.
- Зона доступности — та же, что у группы безопасности.
- Образ — на вкладке Публичные выберите образ Ubuntu 22.04.
- Гарантированная доля vCPU — 10%.
- Сетевой интерфейс — выберите тип Публичный IP.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — app-vm-sg и группа безопасности по умолчанию.
- Логин — оставьте значение по умолчанию или укажите новый.
- Метод аутентификации — Публичный ключ и Пароль.
- Пароль — задайте пароль пользователя.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Название — app-vm.

Зона доступности — та же, что у группы безопасности.

Образ — на вкладке Публичные выберите образ Ubuntu 22.04.

Гарантированная доля vCPU — 10%.

Сетевой интерфейс — выберите тип Публичный IP.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — app-vm-sg и группа безопасности по умолчанию.

Логин — оставьте значение по умолчанию или укажите новый.

Метод аутентификации — Публичный ключ и Пароль.

Пароль — задайте пароль пользователя.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — monitoring-vm.
- Зона доступности — та же, что у группы безопасности.
- Образ — на вкладке Публичные выберите образ Ubuntu 22.04.
- Гарантированная доля vCPU — 10%.
- vCPU, шт — 4.
- RAM, ГБ — 8.
- Диски — SSD-диск 40 ГБ.
- Сетевой интерфейс — выберите тип Публичный IP.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — monitoring-vm-sg и группа безопасности по умолчанию.
- Логин — оставьте значение по умолчанию или укажите новый.
- Метод аутентификации — Публичный ключ и Пароль.
- Пароль — задайте пароль пользователя.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Название — monitoring-vm.

Зона доступности — та же, что у группы безопасности.

Образ — на вкладке Публичные выберите образ Ubuntu 22.04.

Гарантированная доля vCPU — 10%.

vCPU, шт — 4.

RAM, ГБ — 8.

Диски — SSD-диск 40 ГБ.

Сетевой интерфейс — выберите тип Публичный IP.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — monitoring-vm-sg и группа безопасности по умолчанию.

Логин — оставьте значение по умолчанию или укажите новый.

Метод аутентификации — Публичный ключ и Пароль.

Пароль — задайте пароль пользователя.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Убедитесь, что ресурсы созданы и отображаются в личном кабинете:

1. На странице Сети → Группы безопасности отображаются группы безопасности app-vm-sg и monitoring-vm-sg со статусом «Создана».
2. На странице Инфраструктура → Виртуальные машины отображаются виртуальные машины app-vm и monitoring-vm со статусом «Запущена».

На странице Сети → Группы безопасности отображаются группы безопасности app-vm-sg и monitoring-vm-sg со статусом «Создана».

На странице Инфраструктура → Виртуальные машины отображаются виртуальные машины app-vm и monitoring-vm со статусом «Запущена».

Запишите публичные IP-адреса каждой виртуальной машины.
В этом руководстве используются следующие IP-адреса:

- app-vm — 176.109.105.170;
- monitoring-vm — 176.123.164.242.

app-vm — 176.109.105.170;

monitoring-vm — 176.123.164.242.

## 2. Настройте окружение виртуальных машин и установите Docker

На этом шаге вы настроите окружение виртуальных машин и установите Docker.

В терминале для каждой из созданных машин выполните действия:

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH с использованием публичного IP-адреса.
2. Обновите систему и установите утилиты:
sudo apt update && sudo apt upgrade -y
3. Добавьте настройки DNS для разрешения доменных имен:

Откройте файл /etc/resolv.conf для редактирования:
sudo nano /etc/resolv.conf

Добавьте следующие настройки и сохраните файл:
nameserver 8.8.8.8nameserver 8.8.4.4

[Перезагрузите виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__restart)Перезагрузите виртуальную машину и подключитесь к ней по SSH.
4. Подготовьте систему к безопасной установке Docker, добавив официальный репозиторий и настроив механизмы проверки подлинности пакетов:
sudo apt-get install ca-certificates curl -ysudo install -m 0755 -d /etc/apt/keyringssudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.ascsudo chmod a+r /etc/apt/keyrings/docker.asc
5. Добавьте ключ репозитория:
echo \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \$(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt-get update
6. Установите Docker, Docker Compose и сопутствующее ПО:

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
7. Добавьте текущего пользователя виртуальной машины в группу Docker:

Выполните команду:
sudo usermod -aG docker $USERnewgrp docker

Перезагрузите систему.
Проверьте работоспособность Docker:
docker run hello-world

Появится сообщение, подтверждающее успешность установки и настройки.

ПримечаниеВ некоторых случаях права на использование Docker без префикса sudo не сохраняются и командная строка возвращает ошибку permission denied.
В этом случае вы можете продолжить работу с Docker, добавляя в начало каждой команды префикс sudo.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH с использованием публичного IP-адреса.

Обновите систему и установите утилиты:

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

Добавьте настройки DNS для разрешения доменных имен:

1. Откройте файл /etc/resolv.conf для редактирования:
sudo nano /etc/resolv.conf
2. Добавьте следующие настройки и сохраните файл:
nameserver 8.8.8.8nameserver 8.8.4.4
3. [Перезагрузите виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__restart)Перезагрузите виртуальную машину и подключитесь к ней по SSH.

Откройте файл /etc/resolv.conf для редактирования:

```bash
sudo
nano
/etc/resolv.conf
```

Добавьте следующие настройки и сохраните файл:

```bash
nameserver 8.8.8.8
nameserver 8.8.4.4
```

[Перезагрузите виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__restart)Перезагрузите виртуальную машину и подключитесь к ней по SSH.

Подготовьте систему к безопасной установке Docker, добавив официальный репозиторий и настроив механизмы проверки подлинности пакетов:

```bash
sudo
apt-get
install
ca-certificates
curl
-y
sudo
install
-m
0755
-d
/etc/apt/keyrings
sudo
curl
-fsSL
https://download.docker.com/linux/ubuntu/gpg
-o
/etc/apt/keyrings/docker.asc
sudo
chmod
a+r /etc/apt/keyrings/docker.asc
```

Добавьте ключ репозитория:

```bash
echo
\
"deb [arch=
$(
dpkg --print-architecture
)
signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(
.
/etc/os-release
&&
echo
"
${UBUNTU_CODENAME
:-
$VERSION_CODENAME}
"
)
stable"
|
\
sudo
tee
/etc/apt/sources.list.d/docker.list
>
/dev/null
sudo
apt-get
update
```

Установите Docker, Docker Compose и сопутствующее ПО:

```bash
sudo
apt-get
install
docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
-y
```

Добавьте текущего пользователя виртуальной машины в группу Docker:

1. Выполните команду:
sudo usermod -aG docker $USERnewgrp docker
2. Перезагрузите систему.
3. Проверьте работоспособность Docker:
docker run hello-world

Появится сообщение, подтверждающее успешность установки и настройки.

Выполните команду:

```bash
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

Перезагрузите систему.

Проверьте работоспособность Docker:

```bash
docker
run hello-world
```

Появится сообщение, подтверждающее успешность установки и настройки.

В некоторых случаях права на использование Docker без префикса sudo не сохраняются и командная строка возвращает ошибку permission denied.
В этом случае вы можете продолжить работу с Docker, добавляя в начало каждой команды префикс sudo.

## 3. Настройте агенты сбора метрик

На этом шаге вы настроите агенты для сбора метрик приложения.

1. Откройте сессию терминала с подключением к виртуальной машине app-vm.
2. Создайте директорию для файлов мониторинга и установите права пользователя:
sudo mkdir -p /opt/monitoringsudo chown $USER:$USER /opt/monitoringcd /opt/monitoring
3. Скопируйте файлы конфигурации из Git-репозитория:
git clone https://gitverse.ru/cloud.ru/lab2_cicd_monitoring.git .
4. Запустите контейнеры с агентами мониторинга в фоновом режиме:
docker compose -f config/docker-compose.monitoring-agents.yml up -d
5. Убедитесь, что все сервисы запущены корректно:
docker compose -f config/docker-compose.monitoring-agents.yml ps

В ответе вернется список запущенных контейнеров:
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTSmonitoring-cadvisor gcr.io/cadvisor/cadvisor:v0.47.2 "/usr/bin/cadvisor -…" cadvisor 15 seconds ago Up 15 seconds (health: starting) 0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcpmonitoring-node-exporter prom/node-exporter:v1.6.1 "/bin/node_exporter …" node-exporter 15 seconds ago Up 15 seconds 0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp

Где:

node_exporter — отвечает за сбор метрик операционной системы;
cadvisor — отвечает за сбор метрик контейнеров.

Откройте сессию терминала с подключением к виртуальной машине app-vm.

Создайте директорию для файлов мониторинга и установите права пользователя:

```bash
sudo
mkdir
-p
/opt/monitoring
sudo
chown
$USER
:
$USER
/opt/monitoring
cd
/opt/monitoring
```

Скопируйте файлы конфигурации из Git-репозитория:

```bash
git
clone https://gitverse.ru/cloud.ru/lab2_cicd_monitoring.git
.
```

Запустите контейнеры с агентами мониторинга в фоновом режиме:

```bash
docker
compose
-f
config/docker-compose.monitoring-agents.yml up
-d
```

Убедитесь, что все сервисы запущены корректно:

```bash
docker
compose
-f
config/docker-compose.monitoring-agents.yml
ps
```

В ответе вернется список запущенных контейнеров:

```bash
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
monitoring-cadvisor gcr.io/cadvisor/cadvisor:v0.47.2
"/usr/bin/cadvisor -…"
cadvisor
15
seconds ago Up
15
seconds
(
health: starting
)
0.0
.0.0:8080-
>
8080
/tcp,
[
::
]
:8080-
>
8080
/tcp
monitoring-node-exporter prom/node-exporter:v1.6.1
"/bin/node_exporter …"
node-exporter
15
seconds ago Up
15
seconds
0.0
.0.0:9100-
>
9100
/tcp,
[
::
]
:9100-
>
9100
/tcp
```

Где:

- node_exporter — отвечает за сбор метрик операционной системы;
- cadvisor — отвечает за сбор метрик контейнеров.

node_exporter — отвечает за сбор метрик операционной системы;

cadvisor — отвечает за сбор метрик контейнеров.

## 4. Настройте Prometheus и Grafana

На этом шаге вы настроите Prometheus и Grafana на виртуальной машине мониторинга.

1. Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.
2. Создайте директорию для файлов мониторинга и установите права пользователя:
sudo mkdir -p /opt/monitoringsudo chown $USER:$USER /opt/monitoringcd /opt/monitoring
3. Скопируйте файлы конфигурации из Git-репозитория:
git clone https://gitverse.ru/cloud.ru/lab2_cicd_monitoring.git .
4. Откройте конфигурационный файл мониторинга:
nano monitoring/prometheus.yml
5. Замените в нем IP-адрес на публичный IP-адрес app-vm.
В этом практическом — 176.109.105.170.
6. Запустите контейнеры с агентами мониторинга в фоновом режиме:
docker compose -f config/docker-compose.monitoring.yml up -d
7. Убедитесь, что все сервисы запущены корректно:
docker compose -f config/docker-compose.monitoring.yml ps

В ответе вернется список запущенных контейнеров:
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTSmonitoring-grafana grafana/grafana:latest "/run.sh" grafana 16 minutes ago Up 9 seconds 0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcpmonitoring-prometheus prom/prometheus:latest "/bin/prometheus --c…" prometheus 17 minutes ago Up 9 seconds 0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp
8. Проверьте доступность сервисов:

Отправьте API-запрос к сервису Prometheus:
curl http://localhost:9090/-/healthy

Отправьте API-запрос к сервису Grafana:
curl http://localhost:3000/api/health
9. Проверьте, что Prometheus получает метрики с сервера приложения:

В браузере откройте страницу http://<monitoring_public_ip>:9090/targets, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.
Проверьте, что Node Exporter и cAdvisor имеют статус «UP» и передают метрики.
10. Проверьте, что Grafana работает:

В браузере откройте страницу http://<monitoring_public_ip>:3000, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.
Авторизуйтесь в приложении.
В учебных целях используйте логин и пароль, который задан в файле Docker Compose:
- GF_SECURITY_ADMIN_USER=admin- GF_SECURITY_ADMIN_PASSWORD=admin123

Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.

Создайте директорию для файлов мониторинга и установите права пользователя:

```bash
sudo
mkdir
-p
/opt/monitoring
sudo
chown
$USER
:
$USER
/opt/monitoring
cd
/opt/monitoring
```

Скопируйте файлы конфигурации из Git-репозитория:

```bash
git
clone https://gitverse.ru/cloud.ru/lab2_cicd_monitoring.git
.
```

Откройте конфигурационный файл мониторинга:

```bash
nano
monitoring/prometheus.yml
```

Замените в нем IP-адрес на публичный IP-адрес app-vm.
В этом практическом — 176.109.105.170.

Запустите контейнеры с агентами мониторинга в фоновом режиме:

```bash
docker
compose
-f
config/docker-compose.monitoring.yml up
-d
```

Убедитесь, что все сервисы запущены корректно:

```bash
docker
compose
-f
config/docker-compose.monitoring.yml
ps
```

В ответе вернется список запущенных контейнеров:

```bash
NAME IMAGE COMMAND SERVICE CREATED STATUS PORTS
monitoring-grafana grafana/grafana:latest
"/run.sh"
grafana
16
minutes ago Up
9
seconds
0.0
.0.0:3000-
>
3000
/tcp,
[
::
]
:3000-
>
3000
/tcp
monitoring-prometheus prom/prometheus:latest
"/bin/prometheus --c…"
prometheus
17
minutes ago Up
9
seconds
0.0
.0.0:9090-
>
9090
/tcp,
[
::
]
:9090-
>
9090
/tcp
```

Проверьте доступность сервисов:

1. Отправьте API-запрос к сервису Prometheus:
curl http://localhost:9090/-/healthy
2. Отправьте API-запрос к сервису Grafana:
curl http://localhost:3000/api/health

Отправьте API-запрос к сервису Prometheus:

```bash
curl
http://localhost:9090/-/healthy
```

Отправьте API-запрос к сервису Grafana:

```bash
curl
http://localhost:3000/api/health
```

Проверьте, что Prometheus получает метрики с сервера приложения:

1. В браузере откройте страницу http://<monitoring_public_ip>:9090/targets, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.
2. Проверьте, что Node Exporter и cAdvisor имеют статус «UP» и передают метрики.

В браузере откройте страницу http://<monitoring_public_ip>:9090/targets, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.

Проверьте, что Node Exporter и cAdvisor имеют статус «UP» и передают метрики.

![../_images/prometheus_check.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/prometheus_check.png)

Проверьте, что Grafana работает:

1. В браузере откройте страницу http://<monitoring_public_ip>:3000, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.
2. Авторизуйтесь в приложении.
В учебных целях используйте логин и пароль, который задан в файле Docker Compose:
- GF_SECURITY_ADMIN_USER=admin- GF_SECURITY_ADMIN_PASSWORD=admin123

В браузере откройте страницу http://<monitoring_public_ip>:3000, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.

Авторизуйтесь в приложении.
В учебных целях используйте логин и пароль, который задан в файле Docker Compose:

```bash
-
GF_SECURITY_ADMIN_USER=admin
-
GF_SECURITY_ADMIN_PASSWORD=admin123
```

![../_images/grafana_check.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/grafana_check.png)

## 5. Настройте пайплайн CI/CD в GitVerse

На этом шаге вы настроите CI/CD для развертывания Flask-приложения из репозитория GitVerse на виртуальной машине.

1. Авторизуйтесь в [GitVerse](https://gitverse.ru/)GitVerse.
2. [Создайте форк](https://gitverse.ru/docs/repositories/fork-repo)Создайте форк учебного [репозитория GitVerse](https://gitverse.ru/cloud.ru/lab2_cicd_monitoring)репозитория GitVerse.
3. Подключите CI/CD:

Перейдите в раздел Настройки.
Активируйте опцию CI/CD и нажмите Обновить.
4. Добавьте переменные окружения в проект:

Перейдите в раздел Секреты и переменные.
Добавьте следующие секреты в проект:

CI_REGISTRY — registry.gitverse.ru.
CI_REGISTRY_IMAGE — registry.gitverse.ru/<gitverse_login>/lab2-cicd-monitoring, где <gitverse_login> — ваш логин в GitVerse.
CI_REGISTRY_USER — ваш логин в GitVerse.
CI_REGISTRY_PASSWORD — ваш пароль в GitVerse.
DEPLOY_HOST — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.
DEPLOY_USER — логин пользователя виртуальной машины app-vm.
В этом практическом — user1.
DEPLOY_SSH_PRIVATE_KEY — приватная часть SSH-ключа для подключения к app-vm.

ВниманиеВ учебных целях DEPLOY_USER и DEPLOY_SSH_PRIVATE_KEY используют учетные данные подключения к виртуальной машине, которые вы добавили при ее создании.
В реальных задачах используйте для этого отдельный логин и публичный ключ.
5. Добавьте раннер в CI.

Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.
Установите менеджер пакетов и библиотеки Python:
sudo apt install -y python3-pip python3-venv python3-dev build-essential

Установите Node.js:
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -sudo apt-get install -y nodejs

Создайте рабочую директорию для раннера и перейдите в нее:
mkdir -p ~/gitverse-runnercd ~/gitverse-runner

Установите актуальную версию раннера и добавьте права на выполнение:
wget https://gitverse.ru/api/packages/gitverse/generic/act_runner_linux_amd64/4.1.0/act_runner_linux_amd64mv act_runner_linux_amd64 act_runnerchmod +x act_runner

Проверьте, что раннер установлен:
./act_runner --version
6. Получите токен регистрации в GitVerse:

В верхней части страницы нажмите Настройки и перейдите на вкладку Раннеры.
Нажмите Добавить раннер.
В открывшемся окне скопируйте сгенерированный токен.
7. Зарегистрируйте раннер.
В терминале monitoring-vm выполните команду:
sudo ./act_runner register \ --no-interactive \ --instance https://gitverse.ru/sc \ --token <registration_token> \ --name "lab2-runner" \ --labels "docker,monitoring,self-hosted"

Где <registration_token> — токен, полученный в GitVerse.
8. Вернитесь на страницу настройки раннеров в GitVerse.
Проверьте, что локальный раннер появился в настройках и его статус — «Недоступен».
Вы зарегистрировали раннер, но еще не запускали.
9. Настройте автозапуск раннера:

Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.
Выполните команду, которая создаст файл службы systemd:
sudo tee /etc/systemd/system/gitverse-runner.service << EOF[Unit]Description=GitVerse RunnerAfter=network.target docker.service
[Service]Type=simpleUser=rootWorkingDirectory=/home/<vm_login>/gitverse-runnerExecStart=/home/<vm_login>/gitverse-runner/act_runner daemonRestart=alwaysRestartSec=10
[Install]WantedBy=multi-user.targetEOF

Где <vm_login> — имя пользователя виртуальной машины (логин).
В этом практическом — user1.

Включите автозапуск:
sudo systemctl enable gitverse-runnersudo systemctl start gitverse-runner

Проверьте статус раннера в терминале виртуальной машины:
sudo systemctl status gitverse-runner

Пример ожидаемого ответа:
● gitverse-runner.service - GitVerse Runner Loaded: loaded (/etc/systemd/system/gitverse-runner.service; enabled; vendor preset: enabled) Active: active (running) since Tue 2025-11-11 14:42:45 MSK; 16s ago Main PID: 18335 (act_runner) Tasks: 9 (limit: 9388) Memory: 7.3M CPU: 49ms CGroup: /system.slice/gitverse-runner.service └─18335 /home/user1/gitverse-runner/act_runner daemon

Проверьте статус раннера в GitVerse.
Вернитесь на страницу настройки раннеров в GitVerse и проверьте, что статус локального раннера в настройках изменился на «Простаивает».

Авторизуйтесь в [GitVerse](https://gitverse.ru/)GitVerse.

[Создайте форк](https://gitverse.ru/docs/repositories/fork-repo)Создайте форк учебного [репозитория GitVerse](https://gitverse.ru/cloud.ru/lab2_cicd_monitoring)репозитория GitVerse.

Подключите CI/CD:

1. Перейдите в раздел Настройки.
2. Активируйте опцию CI/CD и нажмите Обновить.

Перейдите в раздел Настройки.

Активируйте опцию CI/CD и нажмите Обновить.

Добавьте переменные окружения в проект:

1. Перейдите в раздел Секреты и переменные.
2. Добавьте следующие секреты в проект:

CI_REGISTRY — registry.gitverse.ru.
CI_REGISTRY_IMAGE — registry.gitverse.ru/<gitverse_login>/lab2-cicd-monitoring, где <gitverse_login> — ваш логин в GitVerse.
CI_REGISTRY_USER — ваш логин в GitVerse.
CI_REGISTRY_PASSWORD — ваш пароль в GitVerse.
DEPLOY_HOST — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.
DEPLOY_USER — логин пользователя виртуальной машины app-vm.
В этом практическом — user1.
DEPLOY_SSH_PRIVATE_KEY — приватная часть SSH-ключа для подключения к app-vm.

Перейдите в раздел Секреты и переменные.

Добавьте следующие секреты в проект:

- CI_REGISTRY — registry.gitverse.ru.
- CI_REGISTRY_IMAGE — registry.gitverse.ru/<gitverse_login>/lab2-cicd-monitoring, где <gitverse_login> — ваш логин в GitVerse.
- CI_REGISTRY_USER — ваш логин в GitVerse.
- CI_REGISTRY_PASSWORD — ваш пароль в GitVerse.
- DEPLOY_HOST — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.
- DEPLOY_USER — логин пользователя виртуальной машины app-vm.
В этом практическом — user1.
- DEPLOY_SSH_PRIVATE_KEY — приватная часть SSH-ключа для подключения к app-vm.

CI_REGISTRY — registry.gitverse.ru.

CI_REGISTRY_IMAGE — registry.gitverse.ru/<gitverse_login>/lab2-cicd-monitoring, где <gitverse_login> — ваш логин в GitVerse.

CI_REGISTRY_USER — ваш логин в GitVerse.

CI_REGISTRY_PASSWORD — ваш пароль в GitVerse.

DEPLOY_HOST — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.

DEPLOY_USER — логин пользователя виртуальной машины app-vm.
В этом практическом — user1.

DEPLOY_SSH_PRIVATE_KEY — приватная часть SSH-ключа для подключения к app-vm.

В учебных целях DEPLOY_USER и DEPLOY_SSH_PRIVATE_KEY используют учетные данные подключения к виртуальной машине, которые вы добавили при ее создании.
В реальных задачах используйте для этого отдельный логин и публичный ключ.

Добавьте раннер в CI.

1. Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.
2. Установите менеджер пакетов и библиотеки Python:
sudo apt install -y python3-pip python3-venv python3-dev build-essential
3. Установите Node.js:
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -sudo apt-get install -y nodejs
4. Создайте рабочую директорию для раннера и перейдите в нее:
mkdir -p ~/gitverse-runnercd ~/gitverse-runner
5. Установите актуальную версию раннера и добавьте права на выполнение:
wget https://gitverse.ru/api/packages/gitverse/generic/act_runner_linux_amd64/4.1.0/act_runner_linux_amd64mv act_runner_linux_amd64 act_runnerchmod +x act_runner
6. Проверьте, что раннер установлен:
./act_runner --version

Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.

Установите менеджер пакетов и библиотеки Python:

```bash
sudo
apt
install
-y
python3-pip python3-venv python3-dev build-essential
```

Установите Node.js:

```bash
curl
-fsSL
https://deb.nodesource.com/setup_20.x
|
sudo
-E
bash
-
sudo
apt-get
install
-y
nodejs
```

Создайте рабочую директорию для раннера и перейдите в нее:

```bash
mkdir
-p
~/gitverse-runner
cd
~/gitverse-runner
```

Установите актуальную версию раннера и добавьте права на выполнение:

```bash
wget
https://gitverse.ru/api/packages/gitverse/generic/act_runner_linux_amd64/4.1.0/act_runner_linux_amd64
mv
act_runner_linux_amd64 act_runner
chmod
+x act_runner
```

Проверьте, что раннер установлен:

```bash
./act_runner
--version
```

Получите токен регистрации в GitVerse:

1. В верхней части страницы нажмите Настройки и перейдите на вкладку Раннеры.
2. Нажмите Добавить раннер.
3. В открывшемся окне скопируйте сгенерированный токен.

В верхней части страницы нажмите Настройки и перейдите на вкладку Раннеры.

Нажмите Добавить раннер.

В открывшемся окне скопируйте сгенерированный токен.

Зарегистрируйте раннер.
В терминале monitoring-vm выполните команду:

```bash
sudo
./act_runner register
\
--no-interactive
\
--instance
https://gitverse.ru/sc
\
--token
<
registration_token
>
\
--name
"lab2-runner"
\
--labels
"docker,monitoring,self-hosted"
```

Где <registration_token> — токен, полученный в GitVerse.

Вернитесь на страницу настройки раннеров в GitVerse.

Проверьте, что локальный раннер появился в настройках и его статус — «Недоступен».
Вы зарегистрировали раннер, но еще не запускали.

Настройте автозапуск раннера:

1. Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.
2. Выполните команду, которая создаст файл службы systemd:
sudo tee /etc/systemd/system/gitverse-runner.service << EOF[Unit]Description=GitVerse RunnerAfter=network.target docker.service
[Service]Type=simpleUser=rootWorkingDirectory=/home/<vm_login>/gitverse-runnerExecStart=/home/<vm_login>/gitverse-runner/act_runner daemonRestart=alwaysRestartSec=10
[Install]WantedBy=multi-user.targetEOF

Где <vm_login> — имя пользователя виртуальной машины (логин).
В этом практическом — user1.
3. Включите автозапуск:
sudo systemctl enable gitverse-runnersudo systemctl start gitverse-runner
4. Проверьте статус раннера в терминале виртуальной машины:
sudo systemctl status gitverse-runner

Пример ожидаемого ответа:
● gitverse-runner.service - GitVerse Runner Loaded: loaded (/etc/systemd/system/gitverse-runner.service; enabled; vendor preset: enabled) Active: active (running) since Tue 2025-11-11 14:42:45 MSK; 16s ago Main PID: 18335 (act_runner) Tasks: 9 (limit: 9388) Memory: 7.3M CPU: 49ms CGroup: /system.slice/gitverse-runner.service └─18335 /home/user1/gitverse-runner/act_runner daemon
5. Проверьте статус раннера в GitVerse.
Вернитесь на страницу настройки раннеров в GitVerse и проверьте, что статус локального раннера в настройках изменился на «Простаивает».

Откройте сессию терминала с подключением к виртуальной машине monitoring-vm.

Выполните команду, которая создаст файл службы systemd:

```bash
sudo
tee
/etc/systemd/system/gitverse-runner.service
<<
EOF
[Unit]
Description=GitVerse Runner
After=network.target docker.service
[Service]
Type=simple
User=root
WorkingDirectory=/home/<vm_login>/gitverse-runner
ExecStart=/home/<vm_login>/gitverse-runner/act_runner daemon
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
EOF
```

Где <vm_login> — имя пользователя виртуальной машины (логин).
В этом практическом — user1.

Включите автозапуск:

```bash
sudo
systemctl
enable
gitverse-runner
sudo
systemctl start gitverse-runner
```

Проверьте статус раннера в терминале виртуальной машины:

```bash
sudo
systemctl status gitverse-runner
```

Пример ожидаемого ответа:

```bash
● gitverse-runner.service - GitVerse Runner
Loaded: loaded
(
/etc/systemd/system/gitverse-runner.service
;
enabled
;
vendor preset: enabled
)
Active: active
(
running
)
since Tue
2025
-11-11
14
:42:45 MSK
;
16s ago
Main PID:
18335
(
act_runner
)
Tasks:
9
(
limit:
9388
)
Memory:
7
.3M
CPU: 49ms
CGroup: /system.slice/gitverse-runner.service
└─18335 /home/user1/gitverse-runner/act_runner daemon
```

Проверьте статус раннера в GitVerse.

Вернитесь на страницу настройки раннеров в GitVerse и проверьте, что статус локального раннера в настройках изменился на «Простаивает».

## 6. Разверните Flask-приложение на ВМ

В учебном репозитории GitVerse содержится исходный код Flask-приложения.
На этом шаге вы настроите автоматическое развертывание Flask-приложения из репозитория на виртуальную машину.

1. Откройте GitVerse и перейдите на вкладку CI/CD вашего репозитория.
2. На вкладке может отображаться пайплайн, который автоматически запускается после создания репозитория.
Если этого не произошло:

В меню слева нажмите CI/CD Pipeline для Lab2 (Self-hosted GitVerse).
Нажмите Запустить.
В открывшемся окне оставьте ветку по умолчанию и подтвердите запуск пайплайна.

Пайплайн отобразится на странице.
ПримечаниеКонфигурация пайплайна содержится в файле lab2_cicd_monitoring/.gitverse/workflows/ci-cd-pipeline.yaml.
3. Чтобы посмотреть процесс выполнения заданий, нажмите на название пайплайна.
4. Дождитесь выполнения всех заданий.
5. Проверьте работу приложения на виртуальной машине:

Откройте сессию терминала с подключением к виртуальной машине app-vm.
Выполните команду для проверки работы контейнера:
docker ps

Пример ожидаемого ответа:
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMESe52a3a8b0a44 gitverse.ru/dsdimbrilova/lab2_cicd_monitoring:86162a407c6e92a22b5ec52ddcf4a9d851e2ff26 "gunicorn --bind 0.0…" 22 minutes ago Up 22 minutes 0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp lab2-app4acb8e7bb178 prom/node-exporter:v1.6.1 "/bin/node_exporter …" 7 hours ago Up 7 hours 0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp monitoring-node-exporter3520e6b03e4a gcr.io/cadvisor/cadvisor:v0.47.2 "/usr/bin/cadvisor -…" 7 hours ago Up 7 hours (healthy) 0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp monitoring-cadvisor

Выполните команду для просмотра логов контейнера:
docker logs lab2-app

Пример ожидаемого ответа:
[2025-11-11 12:48:28 +0000] [1] [INFO] Starting gunicorn 21.2.0[2025-11-11 12:48:28 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)[2025-11-11 12:48:28 +0000] [1] [INFO] Using worker: sync[2025-11-11 12:48:28 +0000] [6] [INFO] Booting worker with pid: 6[2025-11-11 12:48:28 +0000] [7] [INFO] Booting worker with pid: 7[2025-11-11 12:48:28 +0000] [8] [INFO] Booting worker with pid: 8[2025-11-11 12:48:28 +0000] [9] [INFO] Booting worker with pid: 9

Обратитесь к API приложения:
curl http://<ip-address>:5000/healthcurl http://<ip-address>:5000/api/time

Где <ip-address> — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.

Откройте GitVerse и перейдите на вкладку CI/CD вашего репозитория.

На вкладке может отображаться пайплайн, который автоматически запускается после создания репозитория.

Если этого не произошло:

1. В меню слева нажмите CI/CD Pipeline для Lab2 (Self-hosted GitVerse).
2. Нажмите Запустить.
3. В открывшемся окне оставьте ветку по умолчанию и подтвердите запуск пайплайна.

В меню слева нажмите CI/CD Pipeline для Lab2 (Self-hosted GitVerse).

Нажмите Запустить.

В открывшемся окне оставьте ветку по умолчанию и подтвердите запуск пайплайна.

Пайплайн отобразится на странице.

Конфигурация пайплайна содержится в файле lab2_cicd_monitoring/.gitverse/workflows/ci-cd-pipeline.yaml.

Чтобы посмотреть процесс выполнения заданий, нажмите на название пайплайна.

![../_images/cicd_jobs.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/cicd_jobs.png)

Дождитесь выполнения всех заданий.

![../_images/cicd_jobs_done.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/cicd_jobs_done.png)

Проверьте работу приложения на виртуальной машине:

1. Откройте сессию терминала с подключением к виртуальной машине app-vm.
2. Выполните команду для проверки работы контейнера:
docker ps

Пример ожидаемого ответа:
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMESe52a3a8b0a44 gitverse.ru/dsdimbrilova/lab2_cicd_monitoring:86162a407c6e92a22b5ec52ddcf4a9d851e2ff26 "gunicorn --bind 0.0…" 22 minutes ago Up 22 minutes 0.0.0.0:5000->5000/tcp, [::]:5000->5000/tcp lab2-app4acb8e7bb178 prom/node-exporter:v1.6.1 "/bin/node_exporter …" 7 hours ago Up 7 hours 0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp monitoring-node-exporter3520e6b03e4a gcr.io/cadvisor/cadvisor:v0.47.2 "/usr/bin/cadvisor -…" 7 hours ago Up 7 hours (healthy) 0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp monitoring-cadvisor
3. Выполните команду для просмотра логов контейнера:
docker logs lab2-app

Пример ожидаемого ответа:
[2025-11-11 12:48:28 +0000] [1] [INFO] Starting gunicorn 21.2.0[2025-11-11 12:48:28 +0000] [1] [INFO] Listening at: http://0.0.0.0:5000 (1)[2025-11-11 12:48:28 +0000] [1] [INFO] Using worker: sync[2025-11-11 12:48:28 +0000] [6] [INFO] Booting worker with pid: 6[2025-11-11 12:48:28 +0000] [7] [INFO] Booting worker with pid: 7[2025-11-11 12:48:28 +0000] [8] [INFO] Booting worker with pid: 8[2025-11-11 12:48:28 +0000] [9] [INFO] Booting worker with pid: 9
4. Обратитесь к API приложения:
curl http://<ip-address>:5000/healthcurl http://<ip-address>:5000/api/time

Где <ip-address> — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.

Откройте сессию терминала с подключением к виртуальной машине app-vm.

Выполните команду для проверки работы контейнера:

```bash
docker
ps
```

Пример ожидаемого ответа:

```bash
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
e52a3a8b0a44 gitverse.ru/dsdimbrilova/lab2_cicd_monitoring:86162a407c6e92a22b5ec52ddcf4a9d851e2ff26
"gunicorn --bind 0.0…"
22
minutes ago Up
22
minutes
0.0
.0.0:5000-
>
5000
/tcp,
[
::
]
:5000-
>
5000
/tcp lab2-app
4acb8e7bb178 prom/node-exporter:v1.6.1
"/bin/node_exporter …"
7
hours ago Up
7
hours
0.0
.0.0:9100-
>
9100
/tcp,
[
::
]
:9100-
>
9100
/tcp monitoring-node-exporter
3520e6b03e4a gcr.io/cadvisor/cadvisor:v0.47.2
"/usr/bin/cadvisor -…"
7
hours ago Up
7
hours
(
healthy
)
0.0
.0.0:8080-
>
8080
/tcp,
[
::
]
:8080-
>
8080
/tcp monitoring-cadvisor
```

Выполните команду для просмотра логов контейнера:

```bash
docker
logs lab2-app
```

Пример ожидаемого ответа:

```bash
[
2025
-11-11
12
:48:28 +0000
]
[
1
]
[
INFO
]
Starting gunicorn
21.2
.0
[
2025
-11-11
12
:48:28 +0000
]
[
1
]
[
INFO
]
Listening at: http://0.0.0.0:5000
(
1
)
[
2025
-11-11
12
:48:28 +0000
]
[
1
]
[
INFO
]
Using worker:
sync
[
2025
-11-11
12
:48:28 +0000
]
[
6
]
[
INFO
]
Booting worker with pid:
6
[
2025
-11-11
12
:48:28 +0000
]
[
7
]
[
INFO
]
Booting worker with pid:
7
[
2025
-11-11
12
:48:28 +0000
]
[
8
]
[
INFO
]
Booting worker with pid:
8
[
2025
-11-11
12
:48:28 +0000
]
[
9
]
[
INFO
]
Booting worker with pid:
9
```

Обратитесь к API приложения:

```bash
curl
http://
<
ip-address
>
:5000/health
curl
http://
<
ip-address
>
:5000/api/time
```

Где <ip-address> — публичный IP-адрес виртуальной машины app-vm.
В этом практическом — 176.109.105.170.

## 7. Настройте дашборды мониторинга

На этом шаге вы настроите дашборды мониторинга Grafana для визуализации метрик производительности и доступности приложения.
В этом практическом используются стандартные экспортеры метрик, поэтому вы будете использовать готовые дашборды Grafana.

1. Скачайте готовые дашборды [Node Exporter](https://grafana.com/grafana/dashboards/1860-node-exporter-full)Node Exporter и [cAdvisor](https://grafana.com/grafana/dashboards/19792-cadvisor-dashboard)cAdvisor с сайта Grafana.
2. В браузере откройте страницу http://<monitoring_public_ip>:3000, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.
3. Авторизуйтесь в Grafana:

логин — admin;
пароль — admin123.
4. Добавьте дашборды в сервис.
Для каждого скачанного JSON-файла выполните действия:

Перейдите на вкладку Dashboards и нажмите New → Import.
Откройте скачанный JSON-файл и нажмите Import.
Node Exporter потребует указать источник данных.
Выберите Prometheus.

На вкладке Dashboards появится список добавленных дашбордов.
5. Выберите любой из дашбордов.
В сервисе отобразятся виджеты с метриками работы приложения на виртуальной машине app-vm.
Вы можете выбрать нужный временной интервал или виджет.

Скачайте готовые дашборды [Node Exporter](https://grafana.com/grafana/dashboards/1860-node-exporter-full)Node Exporter и [cAdvisor](https://grafana.com/grafana/dashboards/19792-cadvisor-dashboard)cAdvisor с сайта Grafana.

В браузере откройте страницу http://<monitoring_public_ip>:3000, где <monitoring_public_ip> — публичный IP-адрес виртуальной машины monitoring-vm.
В этом практическом — 176.123.164.242.

Авторизуйтесь в Grafana:

- логин — admin;
- пароль — admin123.

логин — admin;

пароль — admin123.

Добавьте дашборды в сервис.
Для каждого скачанного JSON-файла выполните действия:

1. Перейдите на вкладку Dashboards и нажмите New → Import.
2. Откройте скачанный JSON-файл и нажмите Import.
Node Exporter потребует указать источник данных.
Выберите Prometheus.

Перейдите на вкладку Dashboards и нажмите New → Import.

Откройте скачанный JSON-файл и нажмите Import.

Node Exporter потребует указать источник данных.
Выберите Prometheus.

На вкладке Dashboards появится список добавленных дашбордов.

Выберите любой из дашбордов.

В сервисе отобразятся виджеты с метриками работы приложения на виртуальной машине app-vm.

Вы можете выбрать нужный временной интервал или виджет.

![../_images/grafana.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/grafana.png)

## Результат

Вы научились:

- Создавать автоматизированный пайплайн CI/CD в GitVerse.
- Настраивать безопасную сборку Docker-образов с автоматическим тестированием и проверкой уязвимостей.
- Автоматически разворачивать Flask-приложение из репозитория.
- Настраивать мониторинг с помощью Prometheus и Grafana.
- Создавать дашборды для визуализации метрик производительности и доступности.

Создавать автоматизированный пайплайн CI/CD в GitVerse.

Настраивать безопасную сборку Docker-образов с автоматическим тестированием и проверкой уязвимостей.

Автоматически разворачивать Flask-приложение из репозитория.

Настраивать мониторинг с помощью Prometheus и Grafana.

Создавать дашборды для визуализации метрик производительности и доступности.
