---
title: Развертывание Wiki-сервиса Outline на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline
topic: compute
---
# Развертывание Wiki-сервиса Outline на виртуальной машине

С помощью этого руководства вы развернете Wiki-сервис для командной работы на бесплатной виртуальной машине.

Вы создадите виртуальную машину Ubuntu 22.04, настроите для нее публичный IP-адрес, создадите бакет в Object Storage и настроите CORS для него.

На виртуальной машине настроите Docker и Docker Compose, развернете сервис Outline, подключите его к Object Storage и GitLab и опубликуете на сервере nginx, выпустите SSL-сертификат в сервисе Let’s Encrypt.

В итоге получится надежная схема, где файлы хранятся в Object Storage, а клиентский трафик шифруется HTTPS.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- Outline — open-source система вики.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
- GitLab — как провайдер для авторизации.
Список других доступных провайдеров можно найти в [документе по аутентификации Outline](https://docs.getoutline.com/s/hosting/doc/authentication-7ViKRmRY5o)документе по аутентификации Outline.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Outline — open-source система вики.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

GitLab — как провайдер для авторизации.
Список других доступных провайдеров можно найти в [документе по аутентификации Outline](https://docs.getoutline.com/s/hosting/doc/authentication-7ViKRmRY5o)документе по аутентификации Outline.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Разверните необходимые ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте окружение на виртуальной машине.
3. [Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте nginx и HTTPS.
4. [Настройте приложение в GitLab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте приложение в GitLab.
5. [Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Разверните приложение.
6. [Настройте CORS в Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте CORS в Object Storage.
7. [Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Удалите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Разверните необходимые ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте окружение на виртуальной машине.

[Настройте nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте nginx и HTTPS.

[Настройте приложение в GitLab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте приложение в GitLab.

[Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Разверните приложение.

[Настройте CORS в Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Настройте CORS в Object Storage.

[Удалите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__outline)Удалите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Сгенерируйте SSH-ключ по [инструкции](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)инструкции.
3. Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по [инструкции](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)инструкции.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Сгенерируйте SSH-ключ по [инструкции](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)инструкции.

Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по [инструкции](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)инструкции.

## 1. Разверните ресурсы в облаке

В этом шаге вы создадите группу безопасности, виртуальную машину и бакет в Object Storage.

[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Укажите Название группы безопасности, например outline-wiki.
2. Добавьте правила входящего и исходящего трафика.
Правила входящего трафика:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правила исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0

Укажите Название группы безопасности, например outline-wiki.

Добавьте правила входящего и исходящего трафика.

Правила входящего трафика:

1. Протокол: TCP
2. Порт: 443
3. Тип источника: IP-адрес
4. Источник: 0.0.0.0/0

Протокол: TCP

Порт: 443

Тип источника: IP-адрес

Источник: 0.0.0.0/0

1. Протокол: TCP
2. Порт: 80
3. Тип источника: IP-адрес
4. Источник: 0.0.0.0/0

Протокол: TCP

Порт: 80

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Правила исходящего трафика:

1. Протокол: Любой
2. Тип адресата: IP-адрес
3. Адресат: 0.0.0.0/0

Протокол: Любой

Тип адресата: IP-адрес

Адресат: 0.0.0.0/0

Убедитесь, что в личном кабинете на странице сервиса «Группы безопасности»:

- отображается группа безопасности outline-wiki;
- статус группы безопасности — «Создана».

отображается группа безопасности outline-wiki;

статус группы безопасности — «Создана».

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например outline-wiki.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. В поле Логин укажите логин пользователя виртуальной машины, например outline.
4. В разделе Метод аутентификации выберите публичный ключ и пароль.
5. Укажите публичный ключ и ваш пароль для создаваемого пользователя.
6. В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например outline-wiki.
7. В поле Название загрузочного диска укажите outline-wiki-disk.
8. Включите опцию Подключить публичный IP.
9. В группе Тип IP-адреса выберите Прямой.
10. Выберите группы безопасности SSH-access_ru.AZ-1, outline-wiki.

В поле Название укажите название виртуальной машины, например outline-wiki.

На вкладке Публичные выберите образ Ubuntu 22.04.

В поле Логин укажите логин пользователя виртуальной машины, например outline.

В разделе Метод аутентификации выберите публичный ключ и пароль.

Укажите публичный ключ и ваш пароль для создаваемого пользователя.

В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например outline-wiki.

В поле Название загрузочного диска укажите outline-wiki-disk.

Включите опцию Подключить публичный IP.

В группе Тип IP-адреса выберите Прямой.

Выберите группы безопасности SSH-access_ru.AZ-1, outline-wiki.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина outline-wiki;
- статус виртуальной машины — «Запущена».

отображается виртуальная машина outline-wiki;

статус виртуальной машины — «Запущена».

[Создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в Object Storage со следующими параметрами:

1. В поле Доменное имя укажите outline-wiki (должно быть уникальным, замените на своё уникальное значение).
2. В поле Название укажите outline-wiki (совпадает с доменным именем).
3. В поле Глобальное название укажите outline-wiki (совпадает с доменным именем).
4. В поле Класс хранения по умолчанию выберите стандартный.
5. В поле Максимальный размер укажите 10 ГБ.

В поле Доменное имя укажите outline-wiki (должно быть уникальным, замените на своё уникальное значение).

В поле Название укажите outline-wiki (совпадает с доменным именем).

В поле Глобальное название укажите outline-wiki (совпадает с доменным именем).

В поле Класс хранения по умолчанию выберите стандартный.

В поле Максимальный размер укажите 10 ГБ.

Перейдите в раздел Object Storage API. Сохраните значения ID тенанта и Регион.

Убедитесь, что в личном кабинете на странице сервиса «Object Storage» отображается бакет outline-wiki.

[Создайте сервисный аккаунт администратора](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт администратора со следующими параметрами:

1. В поле Название укажите outline-object-storage-admin.
2. В поле Описание укажите «Аккаунт администратора Object Storage».
3. В поле Проект выберите Пользователь сервисов.
4. Оставьте список Сервисы пустым.
5. В разделе Evolution Object Storage Роли выберите s3e.admin.

В поле Название укажите outline-object-storage-admin.

В поле Описание укажите «Аккаунт администратора Object Storage».

В поле Проект выберите Пользователь сервисов.

Оставьте список Сервисы пустым.

В разделе Evolution Object Storage Роли выберите s3e.admin.

Следуя аналогичной инструкции, создайте сервисный аккаунт пользователя со следующими параметрами:

1. В поле Название укажите outline-object-storage.
2. В поле Описание укажите «Аккаунт пользователя Object Storage».
3. В поле Проект выберите Пользователь сервисов.
4. Оставьте список Сервисы пустым.
5. В поле Evolution Object Storage Роли выберите s3e.viewer, s3e.editor.

В поле Название укажите outline-object-storage.

В поле Описание укажите «Аккаунт пользователя Object Storage».

В поле Проект выберите Пользователь сервисов.

Оставьте список Сервисы пустым.

В поле Evolution Object Storage Роли выберите s3e.viewer, s3e.editor.

[Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для обоих аккаунтов.
Сохраните Secret ID и Secret Key для обоих ключей.

## 2. Настройте окружение на виртуальной машине

Настройте систему и установите необходимые пакеты на виртуальной машине.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -ysudo apt install unzip gnupg software-properties-common apt-transport-https ca-certificates python3-pip nginx snapd -ysudo snap install core; sudo snap refresh coresudo snap install --classic certbotsudo ln -s /snap/bin/certbot /usr/bin/certbot
3. Установите Docker и Docker Compose:
# Add Docker's GPG keycurl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# Add Docker repositoryecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# Install Dockersudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
# Add user to docker groupsudo usermod -aG docker $USERnewgrp docker
4. Проверьте, что Docker установлен корректно:
docker --versiondocker compose version

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.

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
gnupg software-properties-common apt-transport-https ca-certificates python3-pip nginx snapd
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

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.
2. Сконфигурируйте файрвол:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/outline.conf
4. Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.
server { listen 80; server_name wiki.<IP-адрес>.nip.io www.wiki.<IP-адрес>.nip.io;
 location / { proxy_pass http://localhost:3000/; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection "Upgrade"; proxy_set_header Host $host; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Scheme $scheme; proxy_set_header X-Forwarded-Proto $scheme; proxy_redirect off; }}
5. Примените конфигурацию и перезапустите nginx:
sudo ln -sf /etc/nginx/sites-available/outline.conf /etc/nginx/sites-enabled/outline.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что nginx работает:
sudo systemctl status nginx

Cервис nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://wiki.<IP-адрес>.nip.io.
Откроется страница с текстом 502 Bad Gateway.
8. Запустите команду для выпуска SSL-сертификата.
sudo certbot --nginx -d wiki.<IP-адрес>.nip.io --redirect --agree-tos -m <EMAIL>

Где:

<IP-адрес> — IP-адрес вашей виртуальной машины.
<EMAIL> — ваш email.
9. После успешного выпуска сертификата, перейдите по адресу https://wiki.<IP-адрес>.nip.io.
Откроется страница с текстом 502 Bad Gateway.
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH.

Сконфигурируйте файрвол:

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
/etc/nginx/sites-available/outline.conf
```

Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.

```bash
server
{
listen
80
;
server_name wiki.
<
IP-адрес
>
.nip.io www.wiki.
<
IP-адрес
>
.nip.io
;
location /
{
proxy_pass http://localhost:3000/
;
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"Upgrade"
;
proxy_set_header Host
$host
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Scheme
$scheme
;
proxy_set_header X-Forwarded-Proto
$scheme
;
proxy_redirect off
;
}
}
```

Примените конфигурацию и перезапустите nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/outline.conf /etc/nginx/sites-enabled/outline.conf
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

Перейдите по адресу http://wiki.<IP-адрес>.nip.io.

Откроется страница с текстом 502 Bad Gateway.

Запустите команду для выпуска SSL-сертификата.

```bash
sudo
certbot
--nginx
-d
wiki.
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

После успешного выпуска сертификата, перейдите по адресу https://wiki.<IP-адрес>.nip.io.

Откроется страница с текстом 502 Bad Gateway.
В свойствах сайта браузер отметит соединение как безопасное.

## 4. Настройте приложение в GitLab

Создайте приложение в вашем GitLab-инстансе для интеграции с Outline.

1. Перейдите в Настройки → Приложения в собственном или [облачном](https://gitlab.com/)облачном GitLab-инстансе.
2. Создайте новое приложение со следующими настройками:

Имя: Outline
Redirect URI: https://wiki.<IP-адрес>.nip.io/auth/oidc.callback (замените значения IP-адрес)
Scopes: Выберите openid, profile и email
3. Сохраните приложение.
4. Сохраните значения Application ID и Secret, они понадобятся в дальнейшем.

Перейдите в Настройки → Приложения в собственном или [облачном](https://gitlab.com/)облачном GitLab-инстансе.

Создайте новое приложение со следующими настройками:

- Имя: Outline
- Redirect URI: https://wiki.<IP-адрес>.nip.io/auth/oidc.callback (замените значения IP-адрес)
- Scopes: Выберите openid, profile и email

Имя: Outline

Redirect URI: https://wiki.<IP-адрес>.nip.io/auth/oidc.callback (замените значения IP-адрес)

Scopes: Выберите openid, profile и email

Сохраните приложение.

Сохраните значения Application ID и Secret, они понадобятся в дальнейшем.

## 5. Разверните приложение

Разверните серверное приложение Outline с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH .
2. Создайте структуру проекта:
mkdir -p $HOME/outlinecd $HOME/outline
3. Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:
# Generate two random secrets for Outlineopenssl rand -hex 32 # Save this as SECRET_KEYopenssl rand -hex 32 # Save this as UTILS_SECRET
# Generate database passwordopenssl rand -base64 15 # Save this as POSTGRES_PASSWORD
4. Создайте файл docker-compose.yml:
nano docker-compose.yml
5. Вставьте содержимое в файл docker-compose.yml, заменив переменные на значения:
services: outline: image: flameshikari/outline-ru:0.86.0 env_file: ./docker.env ports: - "3000:3000" volumes: - storage-data:/var/lib/outline/data depends_on: - postgres - redis environment: PGSSLMODE: disable
 redis: image: redis:7-alpine ports: - "6379:6379" command: ["redis-server", "--bind", "0.0.0.0", "--port", "6379"] healthcheck: test: ["CMD", "redis-cli", "ping"] interval: 10s timeout: 30s retries: 3
 postgres: image: postgres:15 env_file: ./docker.env ports: - "5432:5432" volumes: - database-data:/var/lib/postgresql/data healthcheck: test: ["CMD", "pg_isready", "-d", "outline", "-U", "user"] interval: 30s timeout: 20s retries: 3 environment: POSTGRES_USER: 'user' POSTGRES_PASSWORD: <POSTGRES_PASSWORD> POSTGRES_DB: 'outline'
volumes: storage-data: database-data:

Где <POSTGRES_PASSWORD> — пароль от базы данных, сгенерированный ранее.
6. Создайте конфигурацию Redis:
nano redis.conf
7. Вставьте содержимое в файл:
bind 127.0.0.1port 6379timeout 0save 900 1save 300 10save 60 10000dbfilename dump.rdbdir ./
8. Создайте файл docker.env:
nano docker.env
9. Вставьте содержимое в файл, заменив переменные на значения:
NODE_ENV=production
# Application URLURL=https://wiki.<IP-адрес>.nip.ioPORT=3000
# Secrets (use the generated values from Step 6)SECRET_KEY=<SECRET_KEY>UTILS_SECRET=<UTILS_SECRET>
# Database configurationDATABASE_URL=postgres://user:<POSTGRES_PASSWORD>@postgres:5432/outlinePGSSLMODE=disable
# Redis configurationREDIS_URL=redis://redis:6379
# File storage (using AWS S3)FILE_STORAGE=s3AWS_ENDPOINT_URL_S3=https://s3.cloud.ruAWS_SDK_LOAD_CONFIG=1AWS_USE_GLOBAL_ENDPOINT=falseAWS_S3_ADDRESSING_STYLE=pathAWS_ACCESS_KEY_ID=<TENANT_ID>:<SECRET_KEY_ID>AWS_SECRET_ACCESS_KEY=<SECRET_KEY>AWS_REGION=<REGION>AWS_S3_CUSTOM_DOMAIN=<BUCKET_NAME>.s3.cloud.ruAWS_S3_ENDPOINT=https://<BUCKET_NAME>.s3.cloud.ruAWS_S3_UPLOAD_BUCKET_URL=https://<BUCKET_NAME>.s3.cloud.ruAWS_S3_UPLOAD_BUCKET_NAME=<BUCKET_NAME>AWS_S3_FORCE_PATH_STYLE=falseAWS_S3_ACL=privateFILE_STORAGE_UPLOAD_MAX_SIZE=26214400AWS_S3_SIGNATURE_VERSION=v4
# GitLab OIDC AuthenticationOIDC_CLIENT_ID=<GITLAB_APP_ID>OIDC_CLIENT_SECRET=<GITLAB_CLIENT_SECRET>OIDC_AUTH_URI=https://<GITLAB_DOMAIN>/oauth/authorizeOIDC_TOKEN_URI=https://<GITLAB_DOMAIN>/oauth/tokenOIDC_USERINFO_URI=https://<GITLAB_DOMAIN>/oauth/userinfoOIDC_USERNAME_CLAIM=usernameOIDC_DISPLAY_NAME=GitLabOIDC_SCOPES=openid email profile
# SSL ConfigurationFORCE_HTTPS=true
# Rate limitingRATE_LIMITER_ENABLED=trueRATE_LIMITER_REQUESTS=1000RATE_LIMITER_DURATION_WINDOW=60
# UpdatesENABLE_UPDATES=true
# LoggingDEBUG=httpLOG_LEVEL=info

Где:

<SECRET_KEY>, <UTILS_SECRET> — секреты, сгенерированные на шаге 5.
<POSTGRES_PASSWORD> — пароль от базы данных, сгенерированный ранее.
<TENANT_ID> — ID тенанта сервиса Object Storage.
<REGION> — регион Object Storage.
<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage.
<BUCKET_NAME> — название бакета Object Storage.
<GITLAB_APP_ID>, <GITLAB_CLIENT_SECRET> — ID и секретный ключ доступа к приложению GitLab.
<GITLAB_DOMAIN> — адрес сервиса GitLab.
Может быть собственный или [https://gitlab.com/](https://gitlab.com/)https://gitlab.com/.
10. Запустите сервис:
docker compose up -d
11. Проверьте, что сервисы запущены:
docker compose ps
12. Перейдите по адресу https://wiki.<IP-адрес>.nip.io.
Откроется страница Outline, и вы будете перенаправлены в GitLab для авторизации.
13. Авторизуйтесь в GitLab, и вы будете автоматически перенаправлены на страницу Outline.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH .

Создайте структуру проекта:

```bash
mkdir
-p
$HOME
/outline
cd
$HOME
/outline
```

Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:

```bash
# Generate two random secrets for Outline
openssl rand
-hex
32
# Save this as SECRET_KEY
openssl rand
-hex
32
# Save this as UTILS_SECRET
# Generate database password
openssl rand
-base64
15
# Save this as POSTGRES_PASSWORD
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте содержимое в файл docker-compose.yml, заменив переменные на значения:

```bash
services
:
outline
:
image
:
flameshikari/outline
-
ru
:
0.86.0
env_file
:
./docker.env
ports
:
-
"3000:3000"
volumes
:
-
storage
-
data
:
/var/lib/outline/data
depends_on
:
-
postgres
-
redis
environment
:
PGSSLMODE
:
disable
redis
:
image
:
redis
:
7
-
alpine
ports
:
-
"6379:6379"
command
:
[
"redis-server"
,
"--bind"
,
"0.0.0.0"
,
"--port"
,
"6379"
]
healthcheck
:
test
:
[
"CMD"
,
"redis-cli"
,
"ping"
]
interval
:
10s
timeout
:
30s
retries
:
3
postgres
:
image
:
postgres
:
15
env_file
:
./docker.env
ports
:
-
"5432:5432"
volumes
:
-
database
-
data
:
/var/lib/postgresql/data
healthcheck
:
test
:
[
"CMD"
,
"pg_isready"
,
"-d"
,
"outline"
,
"-U"
,
"user"
]
interval
:
30s
timeout
:
20s
retries
:
3
environment
:
POSTGRES_USER
:
'user'
POSTGRES_PASSWORD
:
<POSTGRES_PASSWORD
>
POSTGRES_DB
:
'outline'
volumes
:
storage-data
:
database-data
:
```

Где <POSTGRES_PASSWORD> — пароль от базы данных, сгенерированный ранее.

Создайте конфигурацию Redis:

```bash
nano
redis.conf
```

Вставьте содержимое в файл:

```bash
bind
127.0
.0.1
port
6379
timeout
0
save
900
1
save
300
10
save
60
10000
dbfilename dump.rdb
dir
./
```

Создайте файл docker.env:

```bash
nano
docker.env
```

Вставьте содержимое в файл, заменив переменные на значения:

```bash
NODE_ENV
=
production
# Application URL
URL
=
https://wiki.
<
IP-адрес
>
.nip.io
PORT
=
3000
# Secrets (use the generated values from Step 6)
SECRET_KEY
=
<
SECRET_KEY
>
UTILS_SECRET
=
<
UTILS_SECRET
>
# Database configuration
DATABASE_URL
=
postgres://user:
<
POSTGRES_PASSWORD
>
@postgres:5432/outline
PGSSLMODE
=
disable
# Redis configuration
REDIS_URL
=
redis://redis:6379
# File storage (using AWS S3)
FILE_STORAGE
=
s3
AWS_ENDPOINT_URL_S3
=
https://s3.cloud.ru
AWS_SDK_LOAD_CONFIG
=
1
AWS_USE_GLOBAL_ENDPOINT
=
false
AWS_S3_ADDRESSING_STYLE
=
path
AWS_ACCESS_KEY_ID
=
<
TENANT_ID
>
:
<
SECRET_KEY_ID
>
AWS_SECRET_ACCESS_KEY
=
<
SECRET_KEY
>
AWS_REGION
=
<
REGION
>
AWS_S3_CUSTOM_DOMAIN
=
<
BUCKET_NAME
>
.s3.cloud.ru
AWS_S3_ENDPOINT
=
https://
<
BUCKET_NAME
>
.s3.cloud.ru
AWS_S3_UPLOAD_BUCKET_URL
=
https://
<
BUCKET_NAME
>
.s3.cloud.ru
AWS_S3_UPLOAD_BUCKET_NAME
=
<
BUCKET_NAME
>
AWS_S3_FORCE_PATH_STYLE
=
false
AWS_S3_ACL
=
private
FILE_STORAGE_UPLOAD_MAX_SIZE
=
26214400
AWS_S3_SIGNATURE_VERSION
=
v4
# GitLab OIDC Authentication
OIDC_CLIENT_ID
=
<
GITLAB_APP_ID
>
OIDC_CLIENT_SECRET
=
<
GITLAB_CLIENT_SECRET
>
OIDC_AUTH_URI
=
https://
<
GITLAB_DOMAIN
>
/oauth/authorize
OIDC_TOKEN_URI
=
https://
<
GITLAB_DOMAIN
>
/oauth/token
OIDC_USERINFO_URI
=
https://
<
GITLAB_DOMAIN
>
/oauth/userinfo
OIDC_USERNAME_CLAIM
=
username
OIDC_DISPLAY_NAME
=
GitLab
OIDC_SCOPES
=
openid email profile
# SSL Configuration
FORCE_HTTPS
=
true
# Rate limiting
RATE_LIMITER_ENABLED
=
true
RATE_LIMITER_REQUESTS
=
1000
RATE_LIMITER_DURATION_WINDOW
=
60
# Updates
ENABLE_UPDATES
=
true
# Logging
DEBUG
=
http
LOG_LEVEL
=
info
```

Где:

- <SECRET_KEY>, <UTILS_SECRET> — секреты, сгенерированные на шаге 5.
- <POSTGRES_PASSWORD> — пароль от базы данных, сгенерированный ранее.
- <TENANT_ID> — ID тенанта сервиса Object Storage.
- <REGION> — регион Object Storage.
- <SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage.
- <BUCKET_NAME> — название бакета Object Storage.
- <GITLAB_APP_ID>, <GITLAB_CLIENT_SECRET> — ID и секретный ключ доступа к приложению GitLab.
- <GITLAB_DOMAIN> — адрес сервиса GitLab.
Может быть собственный или [https://gitlab.com/](https://gitlab.com/)https://gitlab.com/.

<SECRET_KEY>, <UTILS_SECRET> — секреты, сгенерированные на шаге 5.

<POSTGRES_PASSWORD> — пароль от базы данных, сгенерированный ранее.

<TENANT_ID> — ID тенанта сервиса Object Storage.

<REGION> — регион Object Storage.

<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage.

<BUCKET_NAME> — название бакета Object Storage.

<GITLAB_APP_ID>, <GITLAB_CLIENT_SECRET> — ID и секретный ключ доступа к приложению GitLab.

<GITLAB_DOMAIN> — адрес сервиса GitLab.
Может быть собственный или [https://gitlab.com/](https://gitlab.com/)https://gitlab.com/.

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

Перейдите по адресу https://wiki.<IP-адрес>.nip.io.
Откроется страница Outline, и вы будете перенаправлены в GitLab для авторизации.

Авторизуйтесь в GitLab, и вы будете автоматически перенаправлены на страницу Outline.

![../_images/img__outline_wiki.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__outline_wiki.png)

## 6. Настройте CORS в Object Storage

Настройте CORS для бакета в Object Storage, чтобы разрешить безопасное взаимодействие с вашим приложением.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH .
2. Установите зависимости командой:
pip install boto3
3. Создайте файл configure_cors.py и добавьте в него код:
nano configure_cors.py
4. Вставьте содержимое в файл конфигурации:
import sysimport boto3from botocore.client import Config
BUCKET = sys.argv[1]ENDPOINT = sys.argv[2]AK = sys.argv[3]SK = sys.argv[4]REGION = sys.argv[5]FRONTEND_URL = sys.argv[6]
s3 = boto3.client( service_name='s3', aws_access_key_id=AK, aws_secret_access_key=SK, endpoint_url=ENDPOINT, region_name=REGION, verify=False, config=Config(s3={'addressing_style': 'virtual'}))
cors_configuration = { 'CORSRules': [{ 'AllowedMethods': ['PUT', 'POST'], 'AllowedOrigins': [FRONTEND_URL], 'ExposeHeaders': ['ETag'], 'AllowedHeaders': ['*'], 'MaxAgeSeconds': 60 }]}
s3.put_bucket_cors(Bucket=BUCKET, CORSConfiguration=cors_configuration)
5. Запустите команду для обновления CORS правил:
python3 configure_cors.py <BUCKET_NAME> https://s3.cloud.ru <TENANT_ID>:<SECRET_KEY_ID> <SECRET_KEY> <REGION> https://wiki.<IP-адрес>.nip.io

Где:

<BUCKET_NAME> — название бакета Object Storage.
<TENANT_ID> — ID тенанта сервиса Object Storage.
<REGION> — регион Object Storage.
<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage-admin.
6. Перейдите по адресу http://<IP-адрес>.nip.io.
Откроется страница Outline.
7. Создайте новую заметку и загрузите в нее изображение.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине outline-wiki через серийную консоль или по SSH .

Установите зависимости командой:

```bash
pip
install
boto3
```

Создайте файл configure_cors.py и добавьте в него код:

```bash
nano
configure_cors.py
```

Вставьте содержимое в файл конфигурации:

```bash
import
sys
import
boto3
from
botocore
.
client
import
Config
BUCKET
=
sys
.
argv
[
1
]
ENDPOINT
=
sys
.
argv
[
2
]
AK
=
sys
.
argv
[
3
]
SK
=
sys
.
argv
[
4
]
REGION
=
sys
.
argv
[
5
]
FRONTEND_URL
=
sys
.
argv
[
6
]
s3
=
boto3
.
client
(
service_name
=
's3'
,
aws_access_key_id
=
AK
,
aws_secret_access_key
=
SK
,
endpoint_url
=
ENDPOINT
,
region_name
=
REGION
,
verify
=
False
,
config
=
Config
(
s3
=
{
'addressing_style'
:
'virtual'
}
)
)
cors_configuration
=
{
'CORSRules'
:
[
{
'AllowedMethods'
:
[
'PUT'
,
'POST'
]
,
'AllowedOrigins'
:
[
FRONTEND_URL
]
,
'ExposeHeaders'
:
[
'ETag'
]
,
'AllowedHeaders'
:
[
'*'
]
,
'MaxAgeSeconds'
:
60
}
]
}
s3
.
put_bucket_cors
(
Bucket
=
BUCKET
,
CORSConfiguration
=
cors_configuration
)
```

Запустите команду для обновления CORS правил:

```bash
python3 configure_cors.py
<
BUCKET_NAME
>
https://s3.cloud.ru
<
TENANT_ID
>
:
<
SECRET_KEY_ID
>
<
SECRET_KEY
>
<
REGION
>
https://wiki.
<
IP-адрес
>
.nip.io
```

Где:

- <BUCKET_NAME> — название бакета Object Storage.
- <TENANT_ID> — ID тенанта сервиса Object Storage.
- <REGION> — регион Object Storage.
- <SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage-admin.

<BUCKET_NAME> — название бакета Object Storage.

<TENANT_ID> — ID тенанта сервиса Object Storage.

<REGION> — регион Object Storage.

<SECRET_KEY_ID>, <SECRET_KEY> — ID ключа и секретный ключ доступа к Object Storage.
Используйте ключи от аккаунта outline-object-storage-admin.

Перейдите по адресу http://<IP-адрес>.nip.io.
Откроется страница Outline.

Создайте новую заметку и загрузите в нее изображение.

## 7. Удалите доступ по SSH для виртуальной машины

Обеспечьте безопасность, удалив доступ по SSH для вашей виртуальной машины, поскольку он больше не требуется.

1. Перейдите в раздел Сетевые параметры.
2. Нажмите изменить группы безопасности для публичного IP-адреса.
3. Удалите группу SSH-access_ru.
4. Нажмите Сохранить.
5. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.

Перейдите в раздел Сетевые параметры.

Нажмите изменить группы безопасности для публичного IP-адреса.

Удалите группу SSH-access_ru.

Нажмите Сохранить.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.

## Результат

Включитеы развернули Wiki-сервис для командной работы в облаке Cloud.ru с надежной сетевой изоляцией и публикацией по HTTPS.

Полученные навыки помогут вам создавать сервисы с использованием облачного хранилища и безопасной инфраструктурой.
