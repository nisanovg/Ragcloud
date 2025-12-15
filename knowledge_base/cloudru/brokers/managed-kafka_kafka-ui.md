---
title: Kafbat UI для менеджмента и мониторинга кластера Managed Kafka®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui
topic: brokers
---
# Kafbat UI для менеджмента и мониторинга кластера Managed Kafka®

С помощью этого руководства вы развернете сервис Kafbat UI на виртуальной машине Ubuntu 22.04, создадите Managed Kafka® и свяжете Kafka с Kafbat UI.
Вы будете использовать виртуальную сеть VPC и подсети для связи виртуальной машины и сервиса Managed Kafka®.

Kafbat UI — это бесплатный и легковесный веб-интерфейс с открытым исходным кодом для мониторинга и управления кластерами Kafka, поддерживающий просмотр брокеров, топиков, групп потребителей, браузинг сообщений и работу со схемами Avro/JSON Schema/Protobuf через Schema Registry.
Инструмент упрощает наблюдаемость потоков данных и ускоряет устранение неполадок, предоставляя мультикластерное управление, создание и конфигурацию топиков, а также дополнительные функции вроде RBAC и маскирования данных.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka®.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
- [Kafbat UI](https://github.com/kafbat/kafka-ui)Kafbat UI — веб-интерфейс с открытым исходным кодом для мониторинга и управления кластерами Kafka.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/index)Managed Kafka® — сервис для развертывания и управления кластерами Kafka®.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Kafbat UI](https://github.com/kafbat/kafka-ui)Kafbat UI — веб-интерфейс с открытым исходным кодом для мониторинга и управления кластерами Kafka.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Разверните необходимые ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Настройте окружение на виртуальной машине.
3. [Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Настройте nginx и HTTPS.
4. [Разверните и настройте сервис Kafbat UI](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Разверните и настройте сервис Kafbat UI.
5. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Удалите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Разверните необходимые ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Настройте окружение на виртуальной машине.

[Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Настройте nginx и HTTPS.

[Разверните и настройте сервис Kafbat UI](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Разверните и настройте сервис Kafbat UI.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)Удалите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

## 1. Разверните необходимые ресурсы в облаке

1. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием kafka-ui-VPC.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

Название: kafka-ui-subnet.
Адрес: 10.10.1.0/24.
VPC: kafka-ui-VPC.
DNS-серверы: 8.8.8.8

Убедитесь, что в личном кабинете на странице сервиса VPC:

отображается сеть kafka-ui-VPC;
количество подсетей — 1;
подсеть kafka-ui-subnet доступна.
3. [Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

Укажите Название группы безопасности, например kafka-ui.
Добавьте правила входящего и исходящего трафика.
Правило входящего трафика:

Протокол: TCP;
Порт: 443;
Тип источника: IP-адрес;
Источник: 0.0.0.0/0.

Правило входящего трафика:

Протокол: TCP;
Порт: 80;
Тип источника: IP-адрес;
Источник: 0.0.0.0/0.

Правило исходящего трафика:

Протокол: Любой;
Тип адресата: IP-адрес;
Адресат: 0.0.0.0/0.

Убедитесь, что на странице Сети → Группы безопасности отображается группа безопасности kafka-ui со статусом «Создана».
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: kafka-ui.
Образ: Публичные → Ubuntu 22.04.
Метод аутентификации: SSH-ключ и пароль.
SSH-ключ: ваш SSH-ключ.
Пароль: ваш пароль.
Имя хоста: kafka-ui.
Подключить публичный IP: включено.
Тип IP-адреса: Прямой.
Группы безопасности: SSH-access_ru.AZ-1, kafka-ui.
Подсеть: kafka-ui-subnet.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина kafka-ui в статуса «Запущена».
5. [Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/guides__cluster-creation)Создайте кластер Managed Kafka® со следующими параметрами:

Название: kafka-ui.
Версия Kafka: 3.9.0.
Брокеры: 1.
vCPU: 4.
RAM: 16.
Подсеть: kafka-ui-subnet.

Убедитесь, что в личном кабинете на странице сервиса «Managed Kafka®» отображается кластер kafka-ui в статусе «Доступен».

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием kafka-ui-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

- Название: kafka-ui-subnet.
- Адрес: 10.10.1.0/24.
- VPC: kafka-ui-VPC.
- DNS-серверы: 8.8.8.8

Название: kafka-ui-subnet.

Адрес: 10.10.1.0/24.

VPC: kafka-ui-VPC.

DNS-серверы: 8.8.8.8

Убедитесь, что в личном кабинете на странице сервиса VPC:

- отображается сеть kafka-ui-VPC;
- количество подсетей — 1;
- подсеть kafka-ui-subnet доступна.

отображается сеть kafka-ui-VPC;

количество подсетей — 1;

подсеть kafka-ui-subnet доступна.

[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Укажите Название группы безопасности, например kafka-ui.
2. Добавьте правила входящего и исходящего трафика.
Правило входящего трафика:

Протокол: TCP;
Порт: 443;
Тип источника: IP-адрес;
Источник: 0.0.0.0/0.

Правило входящего трафика:

Протокол: TCP;
Порт: 80;
Тип источника: IP-адрес;
Источник: 0.0.0.0/0.

Правило исходящего трафика:

Протокол: Любой;
Тип адресата: IP-адрес;
Адресат: 0.0.0.0/0.

Укажите Название группы безопасности, например kafka-ui.

Добавьте правила входящего и исходящего трафика.

Правило входящего трафика:

- Протокол: TCP;
- Порт: 443;
- Тип источника: IP-адрес;
- Источник: 0.0.0.0/0.

Протокол: TCP;

Порт: 443;

Тип источника: IP-адрес;

Источник: 0.0.0.0/0.

Правило входящего трафика:

- Протокол: TCP;
- Порт: 80;
- Тип источника: IP-адрес;
- Источник: 0.0.0.0/0.

Протокол: TCP;

Порт: 80;

Тип источника: IP-адрес;

Источник: 0.0.0.0/0.

Правило исходящего трафика:

- Протокол: Любой;
- Тип адресата: IP-адрес;
- Адресат: 0.0.0.0/0.

Протокол: Любой;

Тип адресата: IP-адрес;

Адресат: 0.0.0.0/0.

Убедитесь, что на странице Сети → Группы безопасности отображается группа безопасности kafka-ui со статусом «Создана».

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: kafka-ui.
- Образ: Публичные → Ubuntu 22.04.
- Метод аутентификации: SSH-ключ и пароль.
- SSH-ключ: ваш SSH-ключ.
- Пароль: ваш пароль.
- Имя хоста: kafka-ui.
- Подключить публичный IP: включено.
- Тип IP-адреса: Прямой.
- Группы безопасности: SSH-access_ru.AZ-1, kafka-ui.
- Подсеть: kafka-ui-subnet.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.

Название: kafka-ui.

Образ: Публичные → Ubuntu 22.04.

Метод аутентификации: SSH-ключ и пароль.

SSH-ключ: ваш SSH-ключ.

Пароль: ваш пароль.

Имя хоста: kafka-ui.

Подключить публичный IP: включено.

Тип IP-адреса: Прямой.

Группы безопасности: SSH-access_ru.AZ-1, kafka-ui.

Подсеть: kafka-ui-subnet.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина kafka-ui в статуса «Запущена».

[Создайте кластер Managed Kafka®](https://cloud.ru/docs/paas-kafka/ug/topics/guides__cluster-creation)Создайте кластер Managed Kafka® со следующими параметрами:

- Название: kafka-ui.
- Версия Kafka: 3.9.0.
- Брокеры: 1.
- vCPU: 4.
- RAM: 16.
- Подсеть: kafka-ui-subnet.

Название: kafka-ui.

Версия Kafka: 3.9.0.

Брокеры: 1.

vCPU: 4.

RAM: 16.

Подсеть: kafka-ui-subnet.

Убедитесь, что в личном кабинете на странице сервиса «Managed Kafka®» отображается кластер kafka-ui в статусе «Доступен».

## 2. Настройте окружение на виртуальной машине

Настройте систему и установите необходимые пакеты на виртуальной машине.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -ysudo apt install unzip gnupg software-properties-common apt-transport-https ca-certificates nginx snapd -ysudo snap install core; sudo snap refresh coresudo snap install --classic certbotsudo ln -s /snap/bin/certbot /usr/bin/certbot
3. Установите Docker и Docker Compose:
# Add Docker's GPG keycurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Add Docker repositoryecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Install Dockersudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
# Add user to docker groupsudo usermod -aG docker $USERnewgrp docker
4. Проверьте, что Docker установлен корректно:
docker --versiondocker compose version

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине через серийную консоль или по SSH.

Обновите систему и установите необходимые зависимости:

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
unzip
gnupg software-properties-common apt-transport-https ca-certificates nginx snapd
-y
sudo
snap
install
core
;
sudo
snap refresh core
sudo
snap
install
--classic
certbot
sudo
ln
-s
/snap/bin/certbot /usr/bin/certbot
```

Установите Docker и Docker Compose:

```bash
# Add Docker's GPG key
curl
-fsSL
https://download.docker.com/linux/ubuntu/gpg
|
sudo
gpg
--dearmor
-o
/usr/share/keyrings/docker-archive-keyring.gpg
# Add Docker repository
echo
"deb [arch=
$(
dpkg --print-architecture
)
signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu
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
# Install Docker
sudo
apt
update
&&
sudo
apt
install
-y
docker-ce docker-ce-cli containerd.io docker-compose-plugin
docker-compose
# Add user to docker group
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

Проверьте, что Docker установлен корректно:

```bash
docker
--version
docker
compose version
```

## 3. Настройте nginx и HTTPS

Настройте службу nginx и обеспечьте доступ по HTTPS.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине через серийную консоль или по SSH.
2. Сконфигурируйте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/kafkaui.conf
4. Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.
server { listen 80; server_name kafkaui.<IP-адрес>.nip.io www.kafkaui.<IP-адрес>.nip.io;
 location / { proxy_pass http://localhost:8080; proxy_http_version 1.1;
 # WebSocket headers proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade";
 # Preserve original host / IP proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme;
 # Timeouts suitable for long-lived Kafbat UI streams proxy_read_timeout 600s; proxy_send_timeout 600s; }}
5. Примените конфигурацию и перезапустите nginx:
sudo ln -sf /etc/nginx/sites-available/kafkaui.conf /etc/nginx/sites-enabled/kafkaui.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что nginx работает:
sudo systemctl status nginx

Сервис nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://kafkaui.<IP-адрес>.nip.io.
Откроется страница с текстом 502 Bad Gateway.
8. Запустите команду для выпуска SSL-сертификата.
sudo certbot --nginx -d kafkaui.<IP-адрес>.nip.io --redirect --agree-tos -m <EMAIL>

Где:

<IP-адрес> — IP-адрес вашей виртуальной машины.
<EMAIL> — ваш email.
9. После успешного выпуска сертификата перейдите по адресу https://kafkaui.<IP-адрес>.nip.io.
Откроется страница с текстом 502 Bad Gateway.
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине через серийную консоль или по SSH.

Сконфигурируйте межсетевой экран:

```bash
sudo
ufw allow OpenSSH
sudo
ufw allow
'Nginx Full'
sudo
ufw
enable
```

Создайте конфигурационный файл:

```bash
sudo
nano
/etc/nginx/sites-available/kafkaui.conf
```

Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.

```bash
server
{
listen
80
;
server_name kafkaui.
<
IP-адрес
>
.nip.io www.kafkaui.
<
IP-адрес
>
.nip.io
;
location /
{
proxy_pass http://localhost:8080
;
proxy_http_version
1.1
;
# WebSocket headers
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"upgrade"
;
# Preserve original host / IP
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
proxy_set_header X-Forwarded-Proto
$scheme
;
# Timeouts suitable for long-lived Kafbat UI streams
proxy_read_timeout 600s
;
proxy_send_timeout 600s
;
}
}
```

Примените конфигурацию и перезапустите nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/kafkaui.conf /etc/nginx/sites-enabled/kafkaui.conf
sudo
rm
-f
/etc/nginx/sites-enabled/default
sudo
nginx
-t
sudo
systemctl reload nginx
```

Проверьте, что nginx работает:

```bash
sudo
systemctl status nginx
```

Сервис nginx должен быть в статусе «active (running)».

Перейдите по адресу http://kafkaui.<IP-адрес>.nip.io.

Откроется страница с текстом 502 Bad Gateway.

Запустите команду для выпуска SSL-сертификата.

```bash
sudo
certbot
--nginx
-d
kafkaui.
<
IP-адрес
>
.nip.io
--redirect
--agree-tos
-m
<
EMAIL
>
```

Где:

- <IP-адрес> — IP-адрес вашей виртуальной машины.
- <EMAIL> — ваш email.

<IP-адрес> — IP-адрес вашей виртуальной машины.

<EMAIL> — ваш email.

После успешного выпуска сертификата перейдите по адресу https://kafkaui.<IP-адрес>.nip.io.

Откроется страница с текстом 502 Bad Gateway.
В свойствах сайта браузер отметит соединение как безопасное.

## 4. Разверните и настройте сервис Kafbat UI

1. Создайте директорию для приложения и перейдите в нее:
mkdir kafkauicd kafkaui
2. Создайте файл docker-compose.yml:
nano docker-compose.yml
3. Вставьте содержимое файла:
services: kafbat-ui: image: kafbat/kafka-ui:47838bd container_name: kafbat-ui ports: - "8080:8080" restart: always
 # Load credentials from .env env_file: - .env
 environment: # ---- cluster basics ---- KAFKA_CLUSTERS_0_NAME: kafka-ui KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: ${KAFKA_BROKERS}
 # ---- SASL_PLAINTEXT + SCRAM-SHA-512 ---- KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL: SASL_PLAINTEXT KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM: SCRAM-SHA-512 KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG: > org.apache.kafka.common.security.scram.ScramLoginModule required username="${KAFKA_USERNAME}" password="${KAFKA_PASSWORD}";
 DYNAMIC_CONFIG_ENABLED: "true"
 AUTH_TYPE: LOGIN_FORM SPRING_SECURITY_USER_NAME: "${KAFKA_UI_USER}" SPRING_SECURITY_USER_PASSWORD: "${KAFKA_UI_PASSWORD}"
 healthcheck: test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/actuator/health"] interval: 30s timeout: 10s retries: 3 start_period: 40s
4. Создайте файл .env:
nano .env
5. Вставьте содержимое файла:
KAFKA_BROKERS=<KAFKA_BROKER_IP>:9094KAFKA_USERNAME=<KAFKA_USERNAME>KAFKA_PASSWORD=<KAFKA_PASSWORD>KAFKA_UI_USER=<KAFKA_UI_USER>KAFKA_UI_PASSWORD=<KAFKA_UI_PASSWORD>

Где:

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
<KAFKA_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.
<KAFKA_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.
<KAFKA_UI_USER> — логин для доступа к сервису Kafbat UI.
<KAFKA_UI_PASSWORD> — пароль для доступа к сервису Kafbat UI.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.
6. Запустите сервис:
docker compose up -d
7. Перейдите по адресу https://kafkaui.<IP-адрес>.nip.io в браузере.
Откроется страница Kafbat UI, и вы будете перенаправлены на страницу авторизации.
8. Зайдите в приложение с логином и паролем, заданными в .env (KAFKA_UI_USER/KAFKA_UI_PASSWORD).

Создайте директорию для приложения и перейдите в нее:

```bash
mkdir
kafkaui
cd
kafkaui
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте содержимое файла:

```bash
services
:
kafbat-ui
:
image
:
kafbat/kafka
-
ui
:
47838bd
container_name
:
kafbat
-
ui
ports
:
-
"8080:8080"
restart
:
always
# Load credentials from .env
env_file
:
-
.env
environment
:
# ---- cluster basics ----
KAFKA_CLUSTERS_0_NAME
:
kafka
-
ui
KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS
:
$
{
KAFKA_BROKERS
}
# ---- SASL_PLAINTEXT + SCRAM-SHA-512 ----
KAFKA_CLUSTERS_0_PROPERTIES_SECURITY_PROTOCOL
:
SASL_PLAINTEXT
KAFKA_CLUSTERS_0_PROPERTIES_SASL_MECHANISM
:
SCRAM
-
SHA
-
512
KAFKA_CLUSTERS_0_PROPERTIES_SASL_JAAS_CONFIG
:
>
org.apache.kafka.common.security.scram.ScramLoginModule required
username="${KAFKA_USERNAME}" password="${KAFKA_PASSWORD}";
DYNAMIC_CONFIG_ENABLED
:
"true"
AUTH_TYPE
:
LOGIN_FORM
SPRING_SECURITY_USER_NAME
:
"${KAFKA_UI_USER}"
SPRING_SECURITY_USER_PASSWORD
:
"${KAFKA_UI_PASSWORD}"
healthcheck
:
test
:
[
"CMD"
,
"wget"
,
"--no-verbose"
,
"--tries=1"
,
"--spider"
,
"http://localhost:8080/actuator/health"
]
interval
:
30s
timeout
:
10s
retries
:
3
start_period
:
40s
```

Создайте файл .env:

```bash
nano
.env
```

Вставьте содержимое файла:

```bash
KAFKA_BROKERS=<KAFKA_BROKER_IP
>
:
9094
KAFKA_USERNAME=<KAFKA_USERNAME
>
KAFKA_PASSWORD=<KAFKA_PASSWORD
>
KAFKA_UI_USER=<KAFKA_UI_USER
>
KAFKA_UI_PASSWORD=<KAFKA_UI_PASSWORD
>
```

Где:

- <KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.
- <KAFKA_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.
- <KAFKA_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.
- <KAFKA_UI_USER> — логин для доступа к сервису Kafbat UI.
- <KAFKA_UI_PASSWORD> — пароль для доступа к сервису Kafbat UI.

<KAFKA_BROKER_IP> — IP-адрес сервиса Managed Kafka®.

<KAFKA_USERNAME> — логин от кластера Managed Kafka® с ролью Admin.

<KAFKA_PASSWORD> — пароль от кластера Managed Kafka® с ролью Admin.

<KAFKA_UI_USER> — логин для доступа к сервису Kafbat UI.

<KAFKA_UI_PASSWORD> — пароль для доступа к сервису Kafbat UI.

IP-адрес, логины и пароли можно найти на странице информации о кластере в блоке Данные для подключения.

Запустите сервис:

```bash
docker
compose up
-d
```

Перейдите по адресу https://kafkaui.<IP-адрес>.nip.io в браузере.
Откроется страница Kafbat UI, и вы будете перенаправлены на страницу авторизации.

Зайдите в приложение с логином и паролем, заданными в .env (KAFKA_UI_USER/KAFKA_UI_PASSWORD).

## 5. Удалите доступ по SSH для виртуальной машины

Так как для настроенного сервиса больше не требуется доступ по SSH, удалите доступ для повышения безопасности.

1. В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину kafka-ui, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)на первом шаге.
2. Перейдите в раздел Сетевые параметры.
3. Нажмите на Изменить группы безопасности для публичного IP-адреса.
4. Удалите группу «SSH-access_ru».
5. Нажмите Сохранить.
6. Попробуйте подключиться к виртуальной машине по SSH по [инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)инструкции и убедитесь, что доступ отсутствует.

В личном кабинете перейдите в сервис «Виртуальные машины» и выберите машину kafka-ui, созданную [на первом шаге](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kafka__kafka-ui)на первом шаге.

Перейдите в раздел Сетевые параметры.

Нажмите на Изменить группы безопасности для публичного IP-адреса.

Удалите группу «SSH-access_ru».

Нажмите Сохранить.

Попробуйте подключиться к виртуальной машине по SSH по [инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)инструкции и убедитесь, что доступ отсутствует.

## Результат

Вы развернули Kafbat UI на виртуальной машине Ubuntu 22.04, связали его с сервисом Managed Kafka® через виртуальную сеть VPC и подсети.
Вы получили опыт управления и мониторинга Kafka-кластера через удобный веб-интерфейс, включая просмотр топиков, групп потребителей и сообщений.
