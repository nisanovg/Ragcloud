---
title: Развертывание Identity Provider Keycloak на виртуальной машине и Managed PostgreSQL®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak
topic: database
---
# Развертывание Identity Provider Keycloak на виртуальной машине и Managed PostgreSQL®

С помощью этого руководства вы развернете Identity Provider Keycloak в облаке для централизованной аутентификации пользователей.
Вы создадите инфраструктуру, настроите подключение к управляемой базе данных Managed PostgreSQL®, опубликуете сервис через Nginx и обеспечите безопасный доступ по HTTPS.
В результате вы получите готовый сервис аутентификации, полностью изолированный в собственной VPC и доступный из интернета.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- [Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

[Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Разверните ресурсы в облаке.
2. [Настройте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Настройте окружение виртуальной машины.
3. [Настройте защищенный доступ через Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Настройте защищенный доступ через Nginx.
4. [Разверните и запустите Keycloak](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Разверните и запустите Keycloak.
5. [Отключите SSH-доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Отключите SSH-доступ.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Разверните ресурсы в облаке.

[Настройте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Настройте окружение виртуальной машины.

[Настройте защищенный доступ через Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Настройте защищенный доступ через Nginx.

[Разверните и запустите Keycloak](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Разверните и запустите Keycloak.

[Отключите SSH-доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-keycloak)Отключите SSH-доступ.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

## 1. Разверните ресурсы в облаке

На этом шаге вы подготовите сеть, группу безопасности, виртуальную машину и кластер Managed PostgreSQL®.
Все ресурсы будут расположены в одной VPC, что обеспечит сетевую изоляцию.

1. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием identity-provider-VPC.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

Название — identity-provider-subnet.
VPC — identity-provider-VPC.
Адрес — 10.10.1.0/24.
DNS-серверы — 8.8.8.8.
3. [Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

Укажите Название группы безопасности, например identity-provider-sg.
Добавьте правила входящего и исходящего трафика.
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — identity-provider.
Образ — публичный образ Ubuntu 22.04.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
VPC — identity-provider-VPC.
Подсеть — identity-provider-subnet.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте группу identity-provider-sg.
Логин — keycloak.
Метод аутентификации — Публичный ключ и Пароль.
Публичный ключ — укажите ключ, созданный ранее.
Пароль — задайте пароль пользователя.
5. [Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL со следующими параметрами:

В поле Имя кластера укажите identity-provider.
В поле Название базы данных укажите identity_provider_database.
В поле Версия PostgreSQL выберите 16.
Выберите Режим — Стандарт.
Выберите Тип — Single.
Выберите Подсеть — identity-provider-subnet.

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием identity-provider-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название — identity-provider-subnet.
- VPC — identity-provider-VPC.
- Адрес — 10.10.1.0/24.
- DNS-серверы — 8.8.8.8.

Название — identity-provider-subnet.

VPC — identity-provider-VPC.

Адрес — 10.10.1.0/24.

DNS-серверы — 8.8.8.8.

[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Укажите Название группы безопасности, например identity-provider-sg.
2. Добавьте правила входящего и исходящего трафика.
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0

Укажите Название группы безопасности, например identity-provider-sg.

Добавьте правила входящего и исходящего трафика.

Трафик

Протокол

Порт

Тип источника/адресата

Источник/Адресат

Входящий

TCP

443

IP-адрес

0.0.0.0/0

Входящий

TCP

80

IP-адрес

0.0.0.0/0

Исходящий

Любой

Оставьте пустым

IP-адрес

0.0.0.0/0

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — identity-provider.
- Образ — публичный образ Ubuntu 22.04.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- VPC — identity-provider-VPC.
- Подсеть — identity-provider-subnet.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте группу identity-provider-sg.
- Логин — keycloak.
- Метод аутентификации — Публичный ключ и Пароль.
- Публичный ключ — укажите ключ, созданный ранее.
- Пароль — задайте пароль пользователя.

Название — identity-provider.

Образ — публичный образ Ubuntu 22.04.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

VPC — identity-provider-VPC.

Подсеть — identity-provider-subnet.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте группу identity-provider-sg.

Логин — keycloak.

Метод аутентификации — Публичный ключ и Пароль.

Публичный ключ — укажите ключ, созданный ранее.

Пароль — задайте пароль пользователя.

[Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL со следующими параметрами:

- В поле Имя кластера укажите identity-provider.
- В поле Название базы данных укажите identity_provider_database.
- В поле Версия PostgreSQL выберите 16.
- Выберите Режим — Стандарт.
- Выберите Тип — Single.
- Выберите Подсеть — identity-provider-subnet.

В поле Имя кластера укажите identity-provider.

В поле Название базы данных укажите identity_provider_database.

В поле Версия PostgreSQL выберите 16.

Выберите Режим — Стандарт.

Выберите Тип — Single.

Выберите Подсеть — identity-provider-subnet.

Убедитесь, что ресурсы созданы и отображаются в личном кабинете:

1. На странице Сети → VPC отображается сеть identity-provider-VPC, а в списке ее подсетей — identity-provider-subnet.
2. На странице Сети → Группы безопасности отображается группа безопасности identity-provider-sg со статусом «Создана».
3. На странице Инфраструктура → Виртуальные машины отображается виртуальная машина identity-provider со статусом «Запущена».
4. На странице Базы данных → Managed PostgreSQL® отображается кластер identity-provider со статусом «Доступен».

На странице Сети → VPC отображается сеть identity-provider-VPC, а в списке ее подсетей — identity-provider-subnet.

На странице Сети → Группы безопасности отображается группа безопасности identity-provider-sg со статусом «Создана».

На странице Инфраструктура → Виртуальные машины отображается виртуальная машина identity-provider со статусом «Запущена».

На странице Базы данных → Managed PostgreSQL® отображается кластер identity-provider со статусом «Доступен».

## 2. Настройте окружение виртуальной машины

На этом шаге вы установите необходимые пакеты и подготовите среду для Keycloak.

1. [Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.
2. Обновите систему и установите утилиты:
sudo apt update && sudo apt upgrade -y
3. Установите и запустите Nginx:
sudo apt install nginx -ysudo systemctl enable nginxsudo systemctl start nginx
4. Установите Java 17:
sudo apt install openjdk-17-jdk -yexport JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
5. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.

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

Установите и запустите Nginx:

```bash
sudo
apt
install
nginx
-y
sudo
systemctl
enable
nginx
sudo
systemctl start nginx
```

Установите Java 17:

```bash
sudo
apt
install
openjdk-17-jdk
-y
export
JAVA_HOME
=
/usr/lib/jvm/java-17-openjdk-amd64
echo
'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64'
>>
~/.bashrc
```

Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

## 3. Настройте защищенный доступ через Nginx

На этом шаге вы зарегистрируете доменное имя, настроите Nginx в качестве защищенного прокси, получите SSL-сертификат и ограничите доступ через межсетевой экран.

1. Создайте конфигурационный файл Nginx:
sudo nano /etc/nginx/sites-available/identity-provider.conf
2. Вставьте код, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:
server { listen 80; server_name <ip_address>.nip.io www.<ip_address>.nip.io;
 location / { proxy_pass http://127.0.0.1:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto https; proxy_set_header X-Forwarded-Host $host; proxy_set_header X-Forwarded-Port 443;
 proxy_http_version 1.1; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade";
 proxy_buffer_size 128k; proxy_buffers 4 256k; proxy_busy_buffers_size 256k;
 proxy_connect_timeout 60s; proxy_send_timeout 60s; proxy_read_timeout 60s; }}
3. Сконфигурируйте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
4. Активируйте конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/identity-provider.conf /etc/nginx/sites-enabled/identity-provider.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
5. Выпустите SSL-сертификат:
sudo certbot --nginx -d <ip_address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip_address> — публичный IP-адрес виртуальной машины.
<email> — email для регистрации сертификата.
6. Перейдите по адресу https://<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

Создайте конфигурационный файл Nginx:

```bash
sudo
nano
/etc/nginx/sites-available/identity-provider.conf
```

Вставьте код, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:

```bash
server
{
listen
80
;
server_name
<
ip_address
>
.nip.io www.
<
ip_address
>
.nip.io
;
location /
{
proxy_pass http://127.0.0.1:8080
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
proxy_set_header X-Forwarded-Proto https
;
proxy_set_header X-Forwarded-Host
$host
;
proxy_set_header X-Forwarded-Port
443
;
proxy_http_version
1.1
;
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"upgrade"
;
proxy_buffer_size 128k
;
proxy_buffers
4
256k
;
proxy_busy_buffers_size 256k
;
proxy_connect_timeout 60s
;
proxy_send_timeout 60s
;
proxy_read_timeout 60s
;
}
}
```

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

Активируйте конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/identity-provider.conf /etc/nginx/sites-enabled/identity-provider.conf
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

Выпустите SSL-сертификат:

```bash
sudo
certbot
--nginx
-d
<
ip_address
>
.nip.io
--redirect
--agree-tos
-m
<
email
>
```

Где:

- <ip_address> — публичный IP-адрес виртуальной машины.
- <email> — email для регистрации сертификата.

<ip_address> — публичный IP-адрес виртуальной машины.

<email> — email для регистрации сертификата.

Перейдите по адресу https://<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

## 4. Установите и запустите Keycloak

На этом шаге вы установите Keycloak, настроите подключение к базе данных и запустите сервис как systemd-службу.

1. Загрузите и распакуйте Keycloak:
cd /optsudo wget https://github.com/keycloak/keycloak/releases/download/26.0.2/keycloak-26.0.2.tar.gzsudo tar -xzf keycloak-26.0.2.tar.gzsudo mv keycloak-26.0.2 keycloaksudo chown -R keycloak:keycloak /opt/keycloaksudo chmod o+x /opt/keycloak/bin/
2. Создайте файл конфигурации Keycloak:
sudo nano /opt/keycloak/conf/keycloak.conf
3. Вставьте код, заменив значения параметров ниже на свои:
db=postgresdb-username=<postgres_admin_user>db-password=<postgres_admin_password>db-url=jdbc:postgresql://<postgres_ip>:5432/identity_provider_database
proxy=edgehostname=https://<ip_address>.nip.iohttp-enabled=trueproxy-headers=xforwardedhostname-strict=falsehostname-admin=https://<ip_address>.nip.io
health-enabled=truemetrics-enabled=true

Где:

<postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.
<postgres_admin_password> — пароль указанного пользователя.
<postgres_ip> — приватный IP-адрес кластера.
<ip_address> — публичный IP-адрес виртуальной машины.
4. Соберите приложение:
sudo -u keycloak /opt/keycloak/bin/kc.sh build
5. Создайте файл службы systemd:
sudo nano /etc/systemd/system/keycloak.service
6. Содержимое файла:
[Unit]Description=Keycloak Identity ProviderAfter=network.targetWants=network.target
[Service]Type=simpleUser=keycloakGroup=keycloakEnvironment=JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64Environment=KC_LOG_LEVEL=INFOWorkingDirectory=/opt/keycloakExecStart=/opt/keycloak/bin/kc.sh startExecReload=/bin/kill -s HUP $MAINPIDKillMode=mixedKillSignal=SIGINTTimeoutStopSec=30Restart=alwaysRestartSec=10
[Install]WantedBy=multi-user.target
7. Создайте временного администратора:
sudo -u keycloak /opt/keycloak/bin/kc.sh bootstrap-admin user
8. Запустите сервис:
sudo systemctl daemon-reloadsudo systemctl enable keycloaksudo systemctl start keycloak
9. Перейдите по адресу https://<ip_address>.nip.io и войдите в администраторскую консоль Keycloak, используя созданные учетные данные.

Загрузите и распакуйте Keycloak:

```bash
cd
/opt
sudo
wget
https://github.com/keycloak/keycloak/releases/download/26.0.2/keycloak-26.0.2.tar.gz
sudo
tar
-xzf
keycloak-26.0.2.tar.gz
sudo
mv
keycloak-26.0.2 keycloak
sudo
chown
-R
keycloak:keycloak /opt/keycloak
sudo
chmod
o+x /opt/keycloak/bin/
```

Создайте файл конфигурации Keycloak:

```bash
sudo
nano
/opt/keycloak/conf/keycloak.conf
```

Вставьте код, заменив значения параметров ниже на свои:

```bash
db
=
postgres
db-username
=
<
postgres_admin_user
>
db-password
=
<
postgres_admin_password
>
db-url
=
jdbc:postgresql://
<
postgres_ip
>
:5432/identity_provider_database
proxy
=
edge
hostname
=
https://
<
ip_address
>
.nip.io
http-enabled
=
true
proxy-headers
=
xforwarded
hostname-strict
=
false
hostname-admin
=
https://
<
ip_address
>
.nip.io
health-enabled
=
true
metrics-enabled
=
true
```

Где:

- <postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.
- <postgres_admin_password> — пароль указанного пользователя.
- <postgres_ip> — приватный IP-адрес кластера.
- <ip_address> — публичный IP-адрес виртуальной машины.

<postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.

<postgres_admin_password> — пароль указанного пользователя.

<postgres_ip> — приватный IP-адрес кластера.

<ip_address> — публичный IP-адрес виртуальной машины.

Соберите приложение:

```bash
sudo
-u
keycloak /opt/keycloak/bin/kc.sh build
```

Создайте файл службы systemd:

```bash
sudo
nano
/etc/systemd/system/keycloak.service
```

Содержимое файла:

```bash
[
Unit
]
Description
=
Keycloak Identity Provider
After
=
network.target
Wants
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
keycloak
Group
=
keycloak
Environment
=
JAVA_HOME
=
/usr/lib/jvm/java-17-openjdk-amd64
Environment
=
KC_LOG_LEVEL
=
INFO
WorkingDirectory
=
/opt/keycloak
ExecStart
=
/opt/keycloak/bin/kc.sh start
ExecReload
=
/bin/kill
-s
HUP
$MAINPID
KillMode
=
mixed
KillSignal
=
SIGINT
TimeoutStopSec
=
30
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

Создайте временного администратора:

```bash
sudo
-u
keycloak /opt/keycloak/bin/kc.sh bootstrap-admin user
```

Запустите сервис:

```bash
sudo
systemctl daemon-reload
sudo
systemctl
enable
keycloak
sudo
systemctl start keycloak
```

Перейдите по адресу https://<ip_address>.nip.io и войдите в администраторскую консоль Keycloak, используя созданные учетные данные.

## 5. Отключите SSH-доступ

Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.

1. В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите identity-provider.
3. Перейдите на вкладку Сетевые параметры.
4. В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите identity-provider.

Перейдите на вкладку Сетевые параметры.

В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## Результат

Вы развернули Keycloak, настроили его взаимодействие с Managed PostgreSQL®, обеспечили безопасный доступ через Nginx и отключили неиспользуемый SSH-доступ.
