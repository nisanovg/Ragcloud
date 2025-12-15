---
title: Развертывание сервиса видеоконференций Jitsi на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences
topic: compute
---
# Развертывание сервиса видеоконференций Jitsi на виртуальной машине

С помощью этого руководства вы развернете сервис видеоконференций Jitsi на бесплатной виртуальной машине в облаке Cloud.ru Evolution.
Вы создадите инфраструктуру, развернете сервис видеоконференций и опубликуете его на сервере Nginx, обеспечив безопасный доступ по HTTPS.

В результате вы получите работающее окружение Jitsi, полностью готовое к использованию.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к приложению через интернет.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- [Jitsi](https://jitsi.org/)Jitsi — сервис видеоконференций с открытым исходным кодом.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к приложению через интернет.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

[Jitsi](https://jitsi.org/)Jitsi — сервис видеоконференций с открытым исходным кодом.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Разверните ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Настройте окружение на виртуальной машине.
3. [Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Настройте Nginx и HTTPS.
4. [Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Разверните приложение.
5. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Удалите доступ по SSH для виртуальной машины.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Разверните ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Настройте окружение на виртуальной машине.

[Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Настройте Nginx и HTTPS.

[Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Разверните приложение.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__jitsi-video-conferences)Удалите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

## 1. Разверните ресурсы в облаке

На этом шаге вы создадите группу безопасности и виртуальную машину.

1. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название: meet-service.
Образ: публичный образ Ubuntu 22.04.
Подключить публичный IP: оставьте опцию включенной.
Метод аутентификации: публичный ключ.
Публичный ключ: укажите ключ, созданный ранее.
Имя хоста: meet-service.

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина meet-service со статусом «Запущена».
2. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием meet-service-sg и добавьте в нее правила:
 ТрафикПротоколПортТип источникаИсточникВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ВходящийTCP4443IP-адрес0.0.0.0/0ВходящийUDP10000IP-адрес0.0.0.0/0ВходящийUDP3478IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0
На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности meet-service-sg со статусом «Создана».
3. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине meet-service.
Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины», в разделе Сетевые параметры отображается группа безопасности meet-service-sg.

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название: meet-service.
- Образ: публичный образ Ubuntu 22.04.
- Подключить публичный IP: оставьте опцию включенной.
- Метод аутентификации: публичный ключ.
- Публичный ключ: укажите ключ, созданный ранее.
- Имя хоста: meet-service.

Название: meet-service.

Образ: публичный образ Ubuntu 22.04.

Подключить публичный IP: оставьте опцию включенной.

Метод аутентификации: публичный ключ.

Публичный ключ: укажите ключ, созданный ранее.

Имя хоста: meet-service.

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина meet-service со статусом «Запущена».

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием meet-service-sg и добавьте в нее правила:

Трафик

Протокол

Порт

Тип источника

Источник

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

Входящий

TCP

4443

IP-адрес

0.0.0.0/0

Входящий

UDP

10000

IP-адрес

0.0.0.0/0

Входящий

UDP

3478

IP-адрес

0.0.0.0/0

Исходящий

Любой

Оставьте пустым

IP-адрес

0.0.0.0/0

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности meet-service-sg со статусом «Создана».

[Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине meet-service.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины», в разделе Сетевые параметры отображается группа безопасности meet-service-sg.

## 2. Настройте окружение на виртуальной машине

На этом шаге вы установите необходимые пакеты и настроите систему на виртуальной машине.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -y &&\sudo apt install -y curl apt-transport-https\ ca-certificates\ software-properties-common\ gnupg2\ lsb-release\ unzip
3. Установите Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpgecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io -y
4. Дайте текущему пользователю права на запуск Docker:
sudo usermod -aG docker $USERnewgrp docker
5. Установите Docker Compose:
sudo apt-get install docker-compose-plugin -y
6. Проверьте, что Docker и Docker Compose установлены корректно:
docker --versiondocker compose version
7. Установите и запустите Nginx:
sudo apt install nginx -ysudo systemctl enable nginxsudo systemctl start nginx
8. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.

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
\
unzip
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

Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

## 3. Настройте Nginx и HTTPS

На этом шаге вы настроите службу Nginx и обеспечите доступ по HTTPS.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.
2. Настройте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw allow 10000/udp comment 'JVB media traffic'sudo ufw allow 4443/tcp comment 'JVB TCP fallback'
sudo ufw enable
3. Создайте конфигурационный файл Nginx:
sudo nano /etc/nginx/sites-available/meet.conf
4. Вставьте конфигурацию, заменив <ip_address> на публичный IP-адрес виртуальной машины meet-service.
server { listen 80; server_name meet.<ip_address>.nip.io www.meet.<ip_address>.nip.io;
 # Основной прокси к Jitsi Web location / { proxy_pass http://localhost:8000; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; }
 # WebSocket прокси для XMPP location /xmpp-websocket { proxy_pass http://127.0.0.1:5280/xmpp-websocket; proxy_http_version 1.1; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "upgrade"; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; tcp_nodelay on; }
 # BOSH прокси для XMPP location /http-bind { proxy_pass http://localhost:5280/http-bind; proxy_set_header X-Forwarded-For $remote_addr; proxy_set_header Host $http_host; }}
5. Активируйте конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/meet.conf /etc/nginx/sites-enabled/meet.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что Nginx работает:
sudo systemctl status nginx

Сервис Nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://meet.<ip_address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Выпустите SSL-сертификат:
sudo certbot --nginx -d meet.<ip_address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip_address> — публичный IP-адрес виртуальной машины meet-service.
<email> — email для регистрации сертификата.
9. После выпуска сертификата перейдите по адресу https://meet.<ip_address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.

Настройте межсетевой экран:

```bash
sudo
ufw allow OpenSSH
sudo
ufw allow
'Nginx Full'
sudo
ufw allow
10000
/udp comment
'JVB media traffic'
sudo
ufw allow
4443
/tcp comment
'JVB TCP fallback'
sudo
ufw
enable
```

Создайте конфигурационный файл Nginx:

```bash
sudo
nano
/etc/nginx/sites-available/meet.conf
```

Вставьте конфигурацию, заменив <ip_address> на публичный IP-адрес виртуальной машины meet-service.

```bash
server
{
listen
80
;
server_name meet.
<
ip_address
>
.nip.io www.meet.
<
ip_address
>
.nip.io
;
# Основной прокси к Jitsi Web
location /
{
proxy_pass http://localhost:8000
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
}
# WebSocket прокси для XMPP
location /xmpp-websocket
{
proxy_pass http://127.0.0.1:5280/xmpp-websocket
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
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
tcp_nodelay on
;
}
# BOSH прокси для XMPP
location /http-bind
{
proxy_pass http://localhost:5280/http-bind
;
proxy_set_header X-Forwarded-For
$remote_addr
;
proxy_set_header Host
$http_host
;
}
}
```

Активируйте конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/meet.conf /etc/nginx/sites-enabled/meet.conf
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

Проверьте, что Nginx работает:

```bash
sudo
systemctl status nginx
```

Сервис Nginx должен быть в статусе «active (running)».

Перейдите по адресу http://meet.<ip_address>.nip.io.

Откроется страница с текстом «502 Bad Gateway».

Выпустите SSL-сертификат:

```bash
sudo
certbot
--nginx
-d
meet.
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

- <ip_address> — публичный IP-адрес виртуальной машины meet-service.
- <email> — email для регистрации сертификата.

<ip_address> — публичный IP-адрес виртуальной машины meet-service.

<email> — email для регистрации сертификата.

После выпуска сертификата перейдите по адресу https://meet.<ip_address>.nip.io.

Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

## 4. Разверните приложение

Разверните серверное приложение Jitsi с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.
2. Скачайте [стабильную версию Jitsi](https://github.com/jitsi/docker-jitsi-meet/releases/tag/stable-10431)стабильную версию Jitsi:
wget $(wget -q -O - https://api.github.com/repos/jitsi/docker-jitsi-meet/releases/234931998 | grep zip | cut -d\" -f4)
3. Распакуйте архив Jitsi:
unzip stable-10431
4. Перейдите в директорию приложения:
cd jitsi-docker-jitsi-meet-*
5. Создайте файл .env:
cp env.example .env
6. Сгенерируйте пароли:
./gen-passwords.sh
7. Создайте директории для конфигурации:
mkdir -p ~/.jitsi-meet-cfg/{web,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri}
8. Откройте файл .env на редактирование:
nano .env
9. Замените или вставьте следующие значения, оставив остальные по умолчанию:
CONFIG=~/.jitsi-meet-cfgHTTP_PORT=8000HTTPS_PORT=8443TZ=Europe/MoscowPUBLIC_URL=https://meet.<ip_address>.nip.ioJVB_ADVERTISE_IPS=<ip_address>DISABLE_HTTPS=1ENABLE_HTTP_REDIRECT=0ENABLE_LETSENCRYPT=0JVB_PORT=10000

Где <ip_address> — публичный IP-адрес виртуальной машины meet-service.
10. Откройте файл docker-compose.yml на редактирование:
nano docker-compose.yml
11. Добавьте следующий код на строку 200 в конфигурацию сервиса prosody:
ports: - "127.0.0.1:5280:5280"
12. Запустите сервис:
docker compose up -d
13. Проверьте, что сервис запущен:
docker compose ps
14. Перейдите по адресу https://meet.<ip_address>.nip.io.
Отобразится страница сервера видеоконференций Jitsi.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине meet-service по SSH.

Скачайте [стабильную версию Jitsi](https://github.com/jitsi/docker-jitsi-meet/releases/tag/stable-10431)стабильную версию Jitsi:

```bash
wget
$(
wget
-q
-O
- https://api.github.com/repos/jitsi/docker-jitsi-meet/releases/234931998
|
grep
zip
|
cut
-d
\
"
-f4
)
```

Распакуйте архив Jitsi:

```bash
unzip
stable-10431
```

Перейдите в директорию приложения:

```bash
cd
jitsi-docker-jitsi-meet-*
```

Создайте файл .env:

```bash
cp
env.example .env
```

Сгенерируйте пароли:

```bash
./gen-passwords.sh
```

Создайте директории для конфигурации:

```bash
mkdir
-p
~/.jitsi-meet-cfg/
{
web,transcripts,prosody/config,prosody/prosody-plugins-custom,jicofo,jvb,jigasi,jibri
}
```

Откройте файл .env на редактирование:

```bash
nano
.env
```

Замените или вставьте следующие значения, оставив остальные по умолчанию:

```bash
CONFIG
=~
/.jitsi-meet-cfg
HTTP_PORT
=
8000
HTTPS_PORT
=
8443
TZ
=
Europe/Moscow
PUBLIC_URL
=
https://meet.
<
ip_address
>
.nip.io
JVB_ADVERTISE_IPS
=
<
ip_address
>
DISABLE_HTTPS
=
1
ENABLE_HTTP_REDIRECT
=
0
ENABLE_LETSENCRYPT
=
0
JVB_PORT
=
10000
```

Где <ip_address> — публичный IP-адрес виртуальной машины meet-service.

Откройте файл docker-compose.yml на редактирование:

```bash
nano
docker-compose.yml
```

Добавьте следующий код на строку 200 в конфигурацию сервиса prosody:

```bash
ports
:
-
"127.0.0.1:5280:5280"
```

Запустите сервис:

```bash
docker
compose up
-d
```

Проверьте, что сервис запущен:

```bash
docker
compose
ps
```

Перейдите по адресу https://meet.<ip_address>.nip.io.

Отобразится страница сервера видеоконференций Jitsi.

![../_images/img__jitsi-meet.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__jitsi-meet.png)

## 5. Отключите SSH-доступ

Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.

1. В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите meet-service.
3. Перейдите на вкладку Сетевые параметры.
4. В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите meet-service.

Перейдите на вкладку Сетевые параметры.

В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## Результат

Вы развернули сервис видеоконференций Jitsi на бесплатной виртуальной машине в облаке Cloud.ru с публикацией по HTTPS.
Полученные навыки помогут вам создавать сервисы с использованием облачной инфраструктуры.
