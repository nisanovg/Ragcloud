---
title: Развертывание CRM-сервиса Twenty на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm
topic: compute
---
# Развертывание CRM-сервиса Twenty на виртуальной машине

В этой лабораторной работе вы развернете CRM‑сервис Twenty на бесплатной виртуальной машине в облаке Cloud.ru Evolution.
Вы создадите инфраструктуру, развернете сервис CRM и опубликуете его на сервере nginx, обеспечив безопасный доступ по HTTPS.
Вы создадите резервную копию виртуальной машины в сервисе «Резервное копирование» для сохранности данных.
В результате вы получите работающее окружение Twenty, развернутое из фиксированного тега образа и готовое к использованию.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к приложению через интернет.
- [Резервное копирование](https://cloud.ru/docs/backup-evolution/ug/index)Резервное копирование — для создания резервных копий.
- [Docker](https://www.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- [Twenty CRM](https://twenty.com/)Twenty CRM — CRM-сервис с открытым исходным кодом.
- [nip.io](https://nip.io/)nip.io — бесплатный сервис динамического DNS для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- [nginx](https://nginx.org/)nginx — для проксирования запросов и организации защищенного HTTPS-доступа к приложению.
- [Let’s Encrypt](https://letsencrypt.org/)Let’s Encrypt — для автоматического получения бесплатного SSL-сертификата.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к приложению через интернет.

[Резервное копирование](https://cloud.ru/docs/backup-evolution/ug/index)Резервное копирование — для создания резервных копий.

[Docker](https://www.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

[Twenty CRM](https://twenty.com/)Twenty CRM — CRM-сервис с открытым исходным кодом.

[nip.io](https://nip.io/)nip.io — бесплатный сервис динамического DNS для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

[nginx](https://nginx.org/)nginx — для проксирования запросов и организации защищенного HTTPS-доступа к приложению.

[Let’s Encrypt](https://letsencrypt.org/)Let’s Encrypt — для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Разверните ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Настройте окружение на виртуальной машине.
3. [Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Настройте nginx и HTTPS.
4. [Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Разверните приложение.
5. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Удалите доступ по SSH для виртуальной машины.
6. [Обеспечьте сохранность данных приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Обеспечьте сохранность данных приложения.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Разверните ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Настройте окружение на виртуальной машине.

[Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Настройте nginx и HTTPS.

[Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Разверните приложение.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Удалите доступ по SSH для виртуальной машины.

[Обеспечьте сохранность данных приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__twenty-crm)Обеспечьте сохранность данных приложения.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару и [загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)загрузите публичный ключ в Cloud.ru Evolution.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару и [загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)загрузите публичный ключ в Cloud.ru Evolution.

## 1. Разверните ресурсы в облаке

В этом шаге вы создадите группу безопасности и виртуальную машину.

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием crm-service и добавьте в нее правила:

Правило входящего трафика:

Протокол: TCP.
Порт: 443.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.

Правило входящего трафика:

Протокол: TCP.
Порт: 80.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.

Правило исходящего трафика:

Протокол: Любой.
Тип адресата: IP-адрес.
Адресат: 0.0.0.0/0.

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности crm-service со статусом «Создана».
2. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название: crm-service.
Образ: публичный образ Ubuntu 22.04.
Подключить публичный IP: оставьте опцию включенной.
Тип IP: оставьте прямой IP-адрес.
Группы безопасности: SSH-access_ru.AZ-1 и crm-service.
Логин: crm.
Метод аутентификации: Публичный ключ и Пароль.
Публичный ключ: укажите ключ, созданный ранее.
Пароль: задайте пароль.
Имя хоста: crm-service.

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина crm-service со статусом «Запущена».
3. [Создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в Object Storage со следующими параметрами:

Название: crm-service.
Максимальный размер: 15 ГБ.
Класс хранения по умолчанию: Стандартный.

Перейдите в раздел Object Storage API.
Сохраните значения ID тенанта и Регион.
4. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт со следующими параметрами:

Название: crm-service.
Описание: Аккаунт Object Storage.
Проект: Пользователь сервисов.
Evolution Object Storage Роли: s3e.viewer, s3e.editor.
5. [Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.
Сохраните Secret ID и Secret Key.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием crm-service и добавьте в нее правила:

- Правило входящего трафика:

Протокол: TCP.
Порт: 443.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.
- Правило входящего трафика:

Протокол: TCP.
Порт: 80.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.
- Правило исходящего трафика:

Протокол: Любой.
Тип адресата: IP-адрес.
Адресат: 0.0.0.0/0.

Правило входящего трафика:

- Протокол: TCP.
- Порт: 443.
- Тип источника: IP-адрес.
- Источник: 0.0.0.0/0.

Протокол: TCP.

Порт: 443.

Тип источника: IP-адрес.

Источник: 0.0.0.0/0.

Правило входящего трафика:

- Протокол: TCP.
- Порт: 80.
- Тип источника: IP-адрес.
- Источник: 0.0.0.0/0.

Протокол: TCP.

Порт: 80.

Тип источника: IP-адрес.

Источник: 0.0.0.0/0.

Правило исходящего трафика:

- Протокол: Любой.
- Тип адресата: IP-адрес.
- Адресат: 0.0.0.0/0.

Протокол: Любой.

Тип адресата: IP-адрес.

Адресат: 0.0.0.0/0.

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности crm-service со статусом «Создана».

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название: crm-service.
- Образ: публичный образ Ubuntu 22.04.
- Подключить публичный IP: оставьте опцию включенной.
- Тип IP: оставьте прямой IP-адрес.
- Группы безопасности: SSH-access_ru.AZ-1 и crm-service.
- Логин: crm.
- Метод аутентификации: Публичный ключ и Пароль.
- Публичный ключ: укажите ключ, созданный ранее.
- Пароль: задайте пароль.
- Имя хоста: crm-service.

Название: crm-service.

Образ: публичный образ Ubuntu 22.04.

Подключить публичный IP: оставьте опцию включенной.

Тип IP: оставьте прямой IP-адрес.

Группы безопасности: SSH-access_ru.AZ-1 и crm-service.

Логин: crm.

Метод аутентификации: Публичный ключ и Пароль.

Публичный ключ: укажите ключ, созданный ранее.

Пароль: задайте пароль.

Имя хоста: crm-service.

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина crm-service со статусом «Запущена».

[Создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в Object Storage со следующими параметрами:

- Название: crm-service.
- Максимальный размер: 15 ГБ.
- Класс хранения по умолчанию: Стандартный.

Название: crm-service.

Максимальный размер: 15 ГБ.

Класс хранения по умолчанию: Стандартный.

Перейдите в раздел Object Storage API.
Сохраните значения ID тенанта и Регион.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт со следующими параметрами:

- Название: crm-service.
- Описание: Аккаунт Object Storage.
- Проект: Пользователь сервисов.
- Evolution Object Storage Роли: s3e.viewer, s3e.editor.

Название: crm-service.

Описание: Аккаунт Object Storage.

Проект: Пользователь сервисов.

Evolution Object Storage Роли: s3e.viewer, s3e.editor.

[Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.
Сохраните Secret ID и Secret Key.

## 2. Настройте окружение на виртуальной машине

На этом шаге вы установите необходимые пакеты и настроите систему на виртуальной машине.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -y &&\sudo apt install -y curl apt-transport-https\ ca-certificates\ software-properties-common\ gnupg2\ lsb-release
3. Установите Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpgecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io -y
4. Дайте текущему пользователю права на запуск Docker:
sudo usermod -aG docker $USERnewgrp docker
5. Установите Docker Compose:
sudo apt-get install docker-compose-plugin -y
6. Проверьте, что Docker и Docker Compose установлены корректно:
docker --versiondocker compose version
7. Установите сервер nginx:
sudo apt install nginx -ysudo systemctl start nginxsudo systemctl enable nginx
8. Установите Let’s Encrypt и плагин для nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .

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
&&
\
sudo
apt
install
-y
curl
apt-transport-https
\
ca-certificates
\
software-properties-common
\
gnupg2
\
lsb-release
```

Установите Docker:

```bash
curl
-fsSL
https://download.docker.com/linux/ubuntu/gpg
|
sudo
gpg
--dearmor
-o
/usr/share/keyrings/docker-archive-keyring.gpg
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
sudo
apt
update
sudo
apt
install
docker-ce docker-ce-cli containerd.io
-y
```

Дайте текущему пользователю права на запуск Docker:

```bash
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

Установите Docker Compose:

```bash
sudo
apt-get
install
docker-compose-plugin
-y
```

Проверьте, что Docker и Docker Compose установлены корректно:

```bash
docker
--version
docker
compose version
```

Установите сервер nginx:

```bash
sudo
apt
install
nginx
-y
sudo
systemctl start nginx
sudo
systemctl
enable
nginx
```

Установите Let’s Encrypt и плагин для nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

## 3. Настройте nginx и HTTPS

На этом шаге вы настроите службу nginx и обеспечите доступ по HTTPS.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .
2. Настройте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/crm.conf
4. Вставьте конфигурацию, заменив <IP-ADDRESS> на IP-адрес вашей виртуальной машины.
server { listen 80; server_name crm.<IP-ADDRESS>.nip.io www.crm.<IP-ADDRESS>.nip.io;
 # Proxy all other requests to Twenty CRM location / { proxy_pass http://localhost:3000; proxy_http_version 1.1; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection 'upgrade'; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; proxy_cache_bypass $http_upgrade; proxy_read_timeout 300; proxy_connect_timeout 300; proxy_send_timeout 300; }}
5. Примените конфигурацию и перезапустите nginx:
sudo ln -sf /etc/nginx/sites-available/crm.conf /etc/nginx/sites-enabled/crm.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что nginx работает:
sudo systemctl status nginx

Cервис nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://crm.<IP-ADDRESS>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Запустите команду для выпуска SSL-сертификата.
sudo certbot --nginx -d crm.<IP-ADDRESS>.nip.io --redirect --agree-tos -m <EMAIL>

Где:

<IP-ADDRESS> — IP-адрес вашей виртуальной машины.
<EMAIL> — email для регистрации сертификата.
9. После выпуска сертификата перейдите по адресу https://crm.<IP-ADDRESS>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .

Настройте межсетевой экран:

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
/etc/nginx/sites-available/crm.conf
```

Вставьте конфигурацию, заменив <IP-ADDRESS> на IP-адрес вашей виртуальной машины.

```bash
server
{
listen
80
;
server_name crm.
<
IP-ADDRESS
>
.nip.io www.crm.
<
IP-ADDRESS
>
.nip.io
;
# Proxy all other requests to Twenty CRM
location /
{
proxy_pass http://localhost:3000
;
proxy_http_version
1.1
;
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
'upgrade'
;
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
proxy_cache_bypass
$http_upgrade
;
proxy_read_timeout
300
;
proxy_connect_timeout
300
;
proxy_send_timeout
300
;
}
}
```

Примените конфигурацию и перезапустите nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/crm.conf /etc/nginx/sites-enabled/crm.conf
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

Cервис nginx должен быть в статусе «active (running)».

Перейдите по адресу http://crm.<IP-ADDRESS>.nip.io.

Откроется страница с текстом «502 Bad Gateway».

Запустите команду для выпуска SSL-сертификата.

```bash
sudo
certbot
--nginx
-d
crm.
<
IP-ADDRESS
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

- <IP-ADDRESS> — IP-адрес вашей виртуальной машины.
- <EMAIL> — email для регистрации сертификата.

<IP-ADDRESS> — IP-адрес вашей виртуальной машины.

<EMAIL> — email для регистрации сертификата.

После выпуска сертификата перейдите по адресу https://crm.<IP-ADDRESS>.nip.io.

Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

## 4. Разверните приложение

Разверните серверное приложение Twenty CRM с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .
2. Создайте структуру проекта:
mkdir ~/twenty-crmcd ~/twenty-crm
3. Сгенерируйте уникальный ключ и сохраните его, он понадобится в дальнейшем:
openssl rand -base64 32
4. Сгенерируйте пароль для базы данных и сохраните его, он понадобится в дальнейшем:
openssl rand -base64 15
5. Создайте файл docker-compose.yml:
nano docker-compose.yml
6. Вставьте код:
name: twenty
services: server: image: twentycrm/twenty:${TAG:-latest} volumes: - server-local-data:/app/packages/twenty-server/.local-storage ports: - "3000:3000" environment: NODE_PORT: 3000 PG_DATABASE_URL: postgres://${PG_DATABASE_USER:-postgres}:${PG_DATABASE_PASSWORD:-postgres}@${PG_DATABASE_HOST:-db}:${PG_DATABASE_PORT:-5432}/default SERVER_URL: ${SERVER_URL} REDIS_URL: ${REDIS_URL:-redis://redis:6379} DISABLE_DB_MIGRATIONS: ${DISABLE_DB_MIGRATIONS} DISABLE_CRON_JOBS_REGISTRATION: ${DISABLE_CRON_JOBS_REGISTRATION} STORAGE_TYPE: ${STORAGE_TYPE} STORAGE_S3_REGION: ${STORAGE_S3_REGION} STORAGE_S3_NAME: ${STORAGE_S3_NAME} STORAGE_S3_ENDPOINT: ${STORAGE_S3_ENDPOINT} STORAGE_S3_ACCESS_KEY_ID: ${STORAGE_S3_ACCESS_KEY_ID} STORAGE_S3_SECRET_ACCESS_KEY: ${STORAGE_S3_SECRET_ACCESS_KEY} APP_SECRET: ${APP_SECRET:-replace_me_with_a_random_string} # MESSAGING_PROVIDER_GMAIL_ENABLED: ${MESSAGING_PROVIDER_GMAIL_ENABLED} # CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED} # AUTH_GOOGLE_CLIENT_ID: ${AUTH_GOOGLE_CLIENT_ID} # AUTH_GOOGLE_CLIENT_SECRET: ${AUTH_GOOGLE_CLIENT_SECRET} # AUTH_GOOGLE_CALLBACK_URL: ${AUTH_GOOGLE_CALLBACK_URL} # AUTH_GOOGLE_APIS_CALLBACK_URL: ${AUTH_GOOGLE_APIS_CALLBACK_URL}
 # CALENDAR_PROVIDER_MICROSOFT_ENABLED: ${CALENDAR_PROVIDER_MICROSOFT_ENABLED} # MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED} # AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED} # AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID} # AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET} # AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL} # AUTH_MICROSOFT_APIS_CALLBACK_URL: ${AUTH_MICROSOFT_APIS_CALLBACK_URL}
 # EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:-contact@yourdomain.com} # EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:-"John from YourDomain"} # EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:-system@yourdomain.com} # EMAIL_DRIVER: ${EMAIL_DRIVER:-smtp} # EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:-smtp.gmail.com} # EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:-465} # EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-} # EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}
 depends_on: db: condition: service_healthy healthcheck: test: curl --fail http://localhost:3000/healthz interval: 5s timeout: 5s retries: 20 restart: always
 worker: image: twentycrm/twenty:${TAG:-latest} volumes: - server-local-data:/app/packages/twenty-server/.local-storage command: ["yarn", "worker:prod"] environment: PG_DATABASE_URL: postgres://${PG_DATABASE_USER:-postgres}:${PG_DATABASE_PASSWORD:-postgres}@${PG_DATABASE_HOST:-db}:${PG_DATABASE_PORT:-5432}/default SERVER_URL: ${SERVER_URL} REDIS_URL: ${REDIS_URL:-redis://redis:6379} DISABLE_DB_MIGRATIONS: "true" DISABLE_CRON_JOBS_REGISTRATION: "true" STORAGE_TYPE: ${STORAGE_TYPE} STORAGE_S3_REGION: ${STORAGE_S3_REGION} STORAGE_S3_NAME: ${STORAGE_S3_NAME} STORAGE_S3_ENDPOINT: ${STORAGE_S3_ENDPOINT} STORAGE_S3_ACCESS_KEY_ID: ${STORAGE_S3_ACCESS_KEY_ID} STORAGE_S3_SECRET_ACCESS_KEY: ${STORAGE_S3_SECRET_ACCESS_KEY} APP_SECRET: ${APP_SECRET:-replace_me_with_a_random_string} # MESSAGING_PROVIDER_GMAIL_ENABLED: ${MESSAGING_PROVIDER_GMAIL_ENABLED} # CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED} # AUTH_GOOGLE_CLIENT_ID: ${AUTH_GOOGLE_CLIENT_ID} # AUTH_GOOGLE_CLIENT_SECRET: ${AUTH_GOOGLE_CLIENT_SECRET} # AUTH_GOOGLE_CALLBACK_URL: ${AUTH_GOOGLE_CALLBACK_URL} # AUTH_GOOGLE_APIS_CALLBACK_URL: ${AUTH_GOOGLE_APIS_CALLBACK_URL}
 # CALENDAR_PROVIDER_MICROSOFT_ENABLED: ${CALENDAR_PROVIDER_MICROSOFT_ENABLED} # MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED} # AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED} # AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID} # AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET} # AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL} # AUTH_MICROSOFT_APIS_CALLBACK_URL: ${AUTH_MICROSOFT_APIS_CALLBACK_URL}
 # EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:-contact@yourdomain.com} # EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:-"John from YourDomain"} # EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:-system@yourdomain.com} # EMAIL_DRIVER: ${EMAIL_DRIVER:-smtp} # EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:-smtp.gmail.com} # EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:-465} # EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-} # EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}
 depends_on: db: condition: service_healthy server: condition: service_healthy restart: always
 db: image: postgres:16 volumes: - db-data:/var/lib/postgresql/data environment: POSTGRES_USER: ${PG_DATABASE_USER:-postgres} POSTGRES_PASSWORD: ${PG_DATABASE_PASSWORD:-postgres} healthcheck: test: pg_isready -U ${PG_DATABASE_USER:-postgres} -h localhost -d postgres interval: 5s timeout: 5s retries: 10 restart: always
 redis: image: redis restart: always command: [ "redis-server", "--maxmemory-policy", "noeviction" ]
volumes: db-data: server-local-data:

Файл docker-compose.yml содержит закоментированные секции для включения интеграций с Google, Microsoft и email.
Для настройки этих интеграций, раскомментируйте необходимые параметры и добавьте значения в файл .env.
Подробнее — в документации [Twenty CRM](https://twenty.com/developers/section/self-hosting/setup)Twenty CRM.
7. Создайте файл .env:
nano .env
8. Вставьте код в файл:
TAG=<TAG>
PG_DATABASE_USER=postgresPG_DATABASE_PASSWORD=<PG_DATABASE_PASSWORD>PG_DATABASE_HOST=dbPG_DATABASE_PORT=5432REDIS_URL=redis://redis:6379
SERVER_URL=https://crm.<IP-ADDRESS>.nip.io
# Use openssl rand -base64 32 for each secretAPP_SECRET=<APP_SECRET>
STORAGE_TYPE=s3STORAGE_S3_NAME=<OBJECT-STORAGE-NAME>STORAGE_S3_REGION=<REGION>STORAGE_S3_ENDPOINT=https://s3.cloud.ruSTORAGE_S3_ACCESS_KEY_ID=<TENANT_ID>:<SECRET_KEY_ID>STORAGE_S3_SECRET_ACCESS_KEY=<SECRET_KEY>STORAGE_S3_FORCE_PATH_STYLE=true

Где:

<TAG> — тeг docker-образа Twenty CRM. Для этой лабораторной работы используйте значение v1.3.0.
Другие теги могут требовать иной конфигурации.
Актуальный список тегов доступен на [странице docker-образа Twenty CRM](https://hub.docker.com/r/twentycrm/twenty)странице docker-образа Twenty CRM.
<APP_SECRET> — уникальный ключ, сгенерированный ранее.
<PG_DATABASE_PASSWORD> — пароль от базы данных, сгенерированный ранее.
<IP-ADDRESS> — IP-адрес вашей виртуальной машины.
<OBJECT-STORAGE-NAME> — название бакета Object Storage.
<TENANT_ID> — ID тенанта сервиса Object Storage.
<REGION> — регион Object Storage.
<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
<BUCKET_NAME> — название бакета Object Storage.
9. Запустите сервис:
docker compose up -d
10. Проверьте, что сервисы запущены:
docker compose ps
11. На компьютере в браузере откройте страницу https://crm.<IP-ADDRESS>.nip.io.
Отобразится страница настройки Twenty CRM.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине crm-service через серийную консоль или по SSH .

Создайте структуру проекта:

```bash
mkdir
~/twenty-crm
cd
~/twenty-crm
```

Сгенерируйте уникальный ключ и сохраните его, он понадобится в дальнейшем:

```bash
openssl rand
-base64
32
```

Сгенерируйте пароль для базы данных и сохраните его, он понадобится в дальнейшем:

```bash
openssl rand
-base64
15
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте код:

```bash
name
:
twenty
services
:
server
:
image
:
twentycrm/twenty
:
$
{
TAG
:
-
latest
}
volumes
:
-
server
-
local
-
data
:
/app/packages/twenty
-
server/.local
-
storage
ports
:
-
"3000:3000"
environment
:
NODE_PORT
:
3000
PG_DATABASE_URL
:
postgres
:
//$
{
PG_DATABASE_USER
:
-
postgres
}
:
$
{
PG_DATABASE_PASSWORD
:
-
postgres
}
@$
{
PG_DATABASE_HOST
:
-
db
}
:
$
{
PG_DATABASE_PORT
:
-5432
}
/default
SERVER_URL
:
$
{
SERVER_URL
}
REDIS_URL
:
$
{
REDIS_URL
:
-
redis
:
//redis
:
6379
}
DISABLE_DB_MIGRATIONS
:
$
{
DISABLE_DB_MIGRATIONS
}
DISABLE_CRON_JOBS_REGISTRATION
:
$
{
DISABLE_CRON_JOBS_REGISTRATION
}
STORAGE_TYPE
:
$
{
STORAGE_TYPE
}
STORAGE_S3_REGION
:
$
{
STORAGE_S3_REGION
}
STORAGE_S3_NAME
:
$
{
STORAGE_S3_NAME
}
STORAGE_S3_ENDPOINT
:
$
{
STORAGE_S3_ENDPOINT
}
STORAGE_S3_ACCESS_KEY_ID
:
$
{
STORAGE_S3_ACCESS_KEY_ID
}
STORAGE_S3_SECRET_ACCESS_KEY
:
$
{
STORAGE_S3_SECRET_ACCESS_KEY
}
APP_SECRET
:
$
{
APP_SECRET
:
-
replace_me_with_a_random_string
}
# MESSAGING_PROVIDER_GMAIL_ENABLED: ${MESSAGING_PROVIDER_GMAIL_ENABLED}
# CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED}
# AUTH_GOOGLE_CLIENT_ID: ${AUTH_GOOGLE_CLIENT_ID}
# AUTH_GOOGLE_CLIENT_SECRET: ${AUTH_GOOGLE_CLIENT_SECRET}
# AUTH_GOOGLE_CALLBACK_URL: ${AUTH_GOOGLE_CALLBACK_URL}
# AUTH_GOOGLE_APIS_CALLBACK_URL: ${AUTH_GOOGLE_APIS_CALLBACK_URL}
# CALENDAR_PROVIDER_MICROSOFT_ENABLED: ${CALENDAR_PROVIDER_MICROSOFT_ENABLED}
# MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED}
# AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED}
# AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID}
# AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET}
# AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL}
# AUTH_MICROSOFT_APIS_CALLBACK_URL: ${AUTH_MICROSOFT_APIS_CALLBACK_URL}
# EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:-contact@yourdomain.com}
# EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:-"John from YourDomain"}
# EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:-system@yourdomain.com}
# EMAIL_DRIVER: ${EMAIL_DRIVER:-smtp}
# EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:-smtp.gmail.com}
# EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:-465}
# EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-}
# EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}
depends_on
:
db
:
condition
:
service_healthy
healthcheck
:
test
:
curl
-
-
fail http
:
//localhost
:
3000/healthz
interval
:
5s
timeout
:
5s
retries
:
20
restart
:
always
worker
:
image
:
twentycrm/twenty
:
$
{
TAG
:
-
latest
}
volumes
:
-
server
-
local
-
data
:
/app/packages/twenty
-
server/.local
-
storage
command
:
[
"yarn"
,
"worker:prod"
]
environment
:
PG_DATABASE_URL
:
postgres
:
//$
{
PG_DATABASE_USER
:
-
postgres
}
:
$
{
PG_DATABASE_PASSWORD
:
-
postgres
}
@$
{
PG_DATABASE_HOST
:
-
db
}
:
$
{
PG_DATABASE_PORT
:
-5432
}
/default
SERVER_URL
:
$
{
SERVER_URL
}
REDIS_URL
:
$
{
REDIS_URL
:
-
redis
:
//redis
:
6379
}
DISABLE_DB_MIGRATIONS
:
"true"
DISABLE_CRON_JOBS_REGISTRATION
:
"true"
STORAGE_TYPE
:
$
{
STORAGE_TYPE
}
STORAGE_S3_REGION
:
$
{
STORAGE_S3_REGION
}
STORAGE_S3_NAME
:
$
{
STORAGE_S3_NAME
}
STORAGE_S3_ENDPOINT
:
$
{
STORAGE_S3_ENDPOINT
}
STORAGE_S3_ACCESS_KEY_ID
:
$
{
STORAGE_S3_ACCESS_KEY_ID
}
STORAGE_S3_SECRET_ACCESS_KEY
:
$
{
STORAGE_S3_SECRET_ACCESS_KEY
}
APP_SECRET
:
$
{
APP_SECRET
:
-
replace_me_with_a_random_string
}
# MESSAGING_PROVIDER_GMAIL_ENABLED: ${MESSAGING_PROVIDER_GMAIL_ENABLED}
# CALENDAR_PROVIDER_GOOGLE_ENABLED: ${CALENDAR_PROVIDER_GOOGLE_ENABLED}
# AUTH_GOOGLE_CLIENT_ID: ${AUTH_GOOGLE_CLIENT_ID}
# AUTH_GOOGLE_CLIENT_SECRET: ${AUTH_GOOGLE_CLIENT_SECRET}
# AUTH_GOOGLE_CALLBACK_URL: ${AUTH_GOOGLE_CALLBACK_URL}
# AUTH_GOOGLE_APIS_CALLBACK_URL: ${AUTH_GOOGLE_APIS_CALLBACK_URL}
# CALENDAR_PROVIDER_MICROSOFT_ENABLED: ${CALENDAR_PROVIDER_MICROSOFT_ENABLED}
# MESSAGING_PROVIDER_MICROSOFT_ENABLED: ${MESSAGING_PROVIDER_MICROSOFT_ENABLED}
# AUTH_MICROSOFT_ENABLED: ${AUTH_MICROSOFT_ENABLED}
# AUTH_MICROSOFT_CLIENT_ID: ${AUTH_MICROSOFT_CLIENT_ID}
# AUTH_MICROSOFT_CLIENT_SECRET: ${AUTH_MICROSOFT_CLIENT_SECRET}
# AUTH_MICROSOFT_CALLBACK_URL: ${AUTH_MICROSOFT_CALLBACK_URL}
# AUTH_MICROSOFT_APIS_CALLBACK_URL: ${AUTH_MICROSOFT_APIS_CALLBACK_URL}
# EMAIL_FROM_ADDRESS: ${EMAIL_FROM_ADDRESS:-contact@yourdomain.com}
# EMAIL_FROM_NAME: ${EMAIL_FROM_NAME:-"John from YourDomain"}
# EMAIL_SYSTEM_ADDRESS: ${EMAIL_SYSTEM_ADDRESS:-system@yourdomain.com}
# EMAIL_DRIVER: ${EMAIL_DRIVER:-smtp}
# EMAIL_SMTP_HOST: ${EMAIL_SMTP_HOST:-smtp.gmail.com}
# EMAIL_SMTP_PORT: ${EMAIL_SMTP_PORT:-465}
# EMAIL_SMTP_USER: ${EMAIL_SMTP_USER:-}
# EMAIL_SMTP_PASSWORD: ${EMAIL_SMTP_PASSWORD:-}
depends_on
:
db
:
condition
:
service_healthy
server
:
condition
:
service_healthy
restart
:
always
db
:
image
:
postgres
:
16
volumes
:
-
db
-
data
:
/var/lib/postgresql/data
environment
:
POSTGRES_USER
:
$
{
PG_DATABASE_USER
:
-
postgres
}
POSTGRES_PASSWORD
:
$
{
PG_DATABASE_PASSWORD
:
-
postgres
}
healthcheck
:
test
:
pg_isready
-
U $
{
PG_DATABASE_USER
:
-
postgres
}
-
h localhost
-
d postgres
interval
:
5s
timeout
:
5s
retries
:
10
restart
:
always
redis
:
image
:
redis
restart
:
always
command
:
[
"redis-server"
,
"--maxmemory-policy"
,
"noeviction"
]
volumes
:
db-data
:
server-local-data
:
```

Файл docker-compose.yml содержит закоментированные секции для включения интеграций с Google, Microsoft и email.
Для настройки этих интеграций, раскомментируйте необходимые параметры и добавьте значения в файл .env.
Подробнее — в документации [Twenty CRM](https://twenty.com/developers/section/self-hosting/setup)Twenty CRM.

Создайте файл .env:

```bash
nano
.env
```

Вставьте код в файл:

```bash
TAG=<TAG
>
PG_DATABASE_USER=postgres
PG_DATABASE_PASSWORD=<PG_DATABASE_PASSWORD
>
PG_DATABASE_HOST=db
PG_DATABASE_PORT=5432
REDIS_URL=redis
:
//redis
:
6379
SERVER_URL=https
:
//crm.<IP
-
ADDRESS
>
.nip.io
# Use openssl rand -base64 32 for each secret
APP_SECRET=<APP_SECRET
>
STORAGE_TYPE=s3
STORAGE_S3_NAME=<OBJECT
-
STORAGE
-
NAME
>
STORAGE_S3_REGION=<REGION
>
STORAGE_S3_ENDPOINT=https
:
//s3.cloud.ru
STORAGE_S3_ACCESS_KEY_ID=<TENANT_ID
>
:
<SECRET_KEY_ID
>
STORAGE_S3_SECRET_ACCESS_KEY=<SECRET_KEY
>
STORAGE_S3_FORCE_PATH_STYLE=true
```

Где:

- <TAG> — тeг docker-образа Twenty CRM. Для этой лабораторной работы используйте значение v1.3.0.
Другие теги могут требовать иной конфигурации.
Актуальный список тегов доступен на [странице docker-образа Twenty CRM](https://hub.docker.com/r/twentycrm/twenty)странице docker-образа Twenty CRM.
- <APP_SECRET> — уникальный ключ, сгенерированный ранее.
- <PG_DATABASE_PASSWORD> — пароль от базы данных, сгенерированный ранее.
- <IP-ADDRESS> — IP-адрес вашей виртуальной машины.
- <OBJECT-STORAGE-NAME> — название бакета Object Storage.
- <TENANT_ID> — ID тенанта сервиса Object Storage.
- <REGION> — регион Object Storage.
- <SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
- <BUCKET_NAME> — название бакета Object Storage.

<TAG> — тeг docker-образа Twenty CRM. Для этой лабораторной работы используйте значение v1.3.0.
Другие теги могут требовать иной конфигурации.
Актуальный список тегов доступен на [странице docker-образа Twenty CRM](https://hub.docker.com/r/twentycrm/twenty)странице docker-образа Twenty CRM.

<APP_SECRET> — уникальный ключ, сгенерированный ранее.

<PG_DATABASE_PASSWORD> — пароль от базы данных, сгенерированный ранее.

<IP-ADDRESS> — IP-адрес вашей виртуальной машины.

<OBJECT-STORAGE-NAME> — название бакета Object Storage.

<TENANT_ID> — ID тенанта сервиса Object Storage.

<REGION> — регион Object Storage.

<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.

<BUCKET_NAME> — название бакета Object Storage.

Запустите сервис:

```bash
docker
compose up
-d
```

Проверьте, что сервисы запущены:

```bash
docker
compose
ps
```

На компьютере в браузере откройте страницу https://crm.<IP-ADDRESS>.nip.io.

Отобразится страница настройки Twenty CRM.

![../_images/img__twenty_crm.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__twenty_crm.png)

## 5. Отключите SSH-доступ

Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.

1. В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите crm-service.
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите crm-service.

Перейдите на вкладку Сетевые параметры.

В строке подсети нажмите и выберите Изменить группы безопасности.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## 6. Обеспечьте сохранность данных приложения

[Создайте резервную копию виртуальной машины](https://cloud.ru/docs/backup-evolution/ug/topics/guides__create-copy)Создайте резервную копию виртуальной машины со следующими параметрами:

- Тип ресурса: Виртуальная машина.
- Ресурс: crm-service.
- Название: crm-service-backup.
- Описание: Резервная копия CRM.

Тип ресурса: Виртуальная машина.

Ресурс: crm-service.

Название: crm-service-backup.

Описание: Резервная копия CRM.

Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается резервная копия crm-service-backup со статусом «Создана».

Периодически создавайте резервные копии для сохранности данных.

## Результат

Вы развернули CRM-сервис для командной работы на бесплатной виртуальной машине в облаке Cloud.ru с надежной сетевой изоляцией и публикацией по HTTPS.
Полученные навыки помогут вам создавать сервисы с использованием облачного хранилища и безопасной инфраструктурой.

Для создания отказоустойчивого и масштабируемого решения с надежным хранением данных вы можете воспользоваться сервисами Managed PostgreSQL®, Managed Redis® и Object Storage.

При необходимости активируйте интеграции с Google, Microsoft и email.
