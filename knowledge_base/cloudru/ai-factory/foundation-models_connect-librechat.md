---
title: Подключение корпоративной AI чат-платформы LibreChat к Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat
topic: ai-factory
---
# Подключение корпоративной AI чат-платформы LibreChat к Foundation Models

С помощью этого руководства вы развернете чат-платформу LibreChat на бесплатной виртуальной машине в облаке Cloud.ru Evolution.

Вы создадите виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите LibreChat и опубликуете сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt.

В результате вы сконфигурируете LibreChat для работы с Foundation Models и получите сервис, готовый к работе.

Вы будете использовать следующие сервисы:

- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
- [LibreChat](https://www.librechat.ai/)LibreChat — бесплатная open-source-платформа, объединяющая в одном веб-интерфейсе различные языковые модели.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[LibreChat](https://www.librechat.ai/)LibreChat — бесплатная open-source-платформа, объединяющая в одном веб-интерфейсе различные языковые модели.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Разверните необходимые ресурсы в облаке.
2. [Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Сгенерируйте API-ключ для доступа к Foundation Models.
3. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Настройте окружение на виртуальной машине.
4. [Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Настройте Nginx и HTTPS.
5. [Разверните приложение LibreChat](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Разверните приложение LibreChat.
6. [Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Отключите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Разверните необходимые ресурсы в облаке.

[Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Сгенерируйте API-ключ для доступа к Foundation Models.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Настройте окружение на виртуальной машине.

[Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Настройте Nginx и HTTPS.

[Разверните приложение LibreChat](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Разверните приложение LibreChat.

[Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)Отключите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.
3. [Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.

[Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

## 1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите группу безопасности и виртуальную машину.

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием ai-chat-service и добавьте в нее правила:

Правило входящего трафика 1:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правило входящего трафика 2:

Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правило исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности ai-chat-service со статусом «Создана».
2. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название: ai-chat-service
Образ: публичный образ Ubuntu 22.04
Подключить публичный IP: включено
Тип IP: прямой IP-адрес
Группы безопасности: SSH-access_ru.AZ-1, ai-chat-service
Логин: aichat
Метод аутентификации: Публичный ключ и Пароль
Публичный ключ: укажите ранее созданный ключ
Пароль: задайте надежный пароль
Имя хоста: ai-chat-service
3. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина ai-chat-service со статусом «Запущена».

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием ai-chat-service и добавьте в нее правила:

- Правило входящего трафика 1:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0
- Правило входящего трафика 2:

Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0
- Правило исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0

Правило входящего трафика 1:

- Протокол: TCP
- Порт: 443
- Тип источника: IP-адрес
- Источник: 0.0.0.0/0

Протокол: TCP

Порт: 443

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Правило входящего трафика 2:

- Протокол: TCP
- Порт: 80
- Тип источника: IP-адрес
- Источник: 0.0.0.0/0

Протокол: TCP

Порт: 80

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Правило исходящего трафика:

- Протокол: Любой
- Тип адресата: IP-адрес
- Адресат: 0.0.0.0/0

Протокол: Любой

Тип адресата: IP-адрес

Адресат: 0.0.0.0/0

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности ai-chat-service со статусом «Создана».

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название: ai-chat-service
- Образ: публичный образ Ubuntu 22.04
- Подключить публичный IP: включено
- Тип IP: прямой IP-адрес
- Группы безопасности: SSH-access_ru.AZ-1, ai-chat-service
- Логин: aichat
- Метод аутентификации: Публичный ключ и Пароль
- Публичный ключ: укажите ранее созданный ключ
- Пароль: задайте надежный пароль
- Имя хоста: ai-chat-service

Название: ai-chat-service

Образ: публичный образ Ubuntu 22.04

Подключить публичный IP: включено

Тип IP: прямой IP-адрес

Группы безопасности: SSH-access_ru.AZ-1, ai-chat-service

Логин: aichat

Метод аутентификации: Публичный ключ и Пароль

Публичный ключ: укажите ранее созданный ключ

Пароль: задайте надежный пароль

Имя хоста: ai-chat-service

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина ai-chat-service со статусом «Запущена».

## 2. Сгенерируйте API-ключ для доступа к Foundation Models

Следуйте инструкции по созданию API-ключа для Foundation Models.
Сохраните API-ключ, он будет использоваться для конфигурации сервиса.

1. На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
2. Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.
3. Перейдите на вкладку API-ключи.
4. Нажмите Создать API-ключ.
5. Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.
6. Заполните параметры API-ключа:

Сервисы — Foundation Models.
Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.
7. Нажмите Создать.
8. Сохраните Key Secret.
После закрытия окна получить его будет нельзя.
Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.

![../_images/s__service_account_n.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account_n.png)

Перейдите на вкладку API-ключи.

Нажмите Создать API-ключ.

![../_images/s__create_key.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__create_key.png)

Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.

Заполните параметры API-ключа:

- Сервисы — Foundation Models.
- Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
- Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Сервисы — Foundation Models.

Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.

Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Нажмите Создать.

Сохраните Key Secret.
После закрытия окна получить его будет нельзя.

Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

## 3. Настройте окружение на виртуальной машине

На этом шаге вы установите необходимые пакеты и настроите систему на виртуальной машине.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
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
7. Установите Nginx сервер:
sudo apt install nginx -ysudo systemctl start nginxsudo systemctl enable nginx
8. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.

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

Установите Nginx сервер:

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

Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

## 4. Настройте Nginx и HTTPS

На этом шаге вы настроите службу Nginx и обеспечите доступ по HTTPS.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
2. Настройте файервол:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/librechat.conf
4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины.
server { listen 80; server_name chat.<ip-address>.nip.io www.chat.<ip-address>.nip.io;
 location / { proxy_pass http://localhost:3080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; }}
5. Примените конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/librechat.conf /etc/nginx/sites-enabled/librechat.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что Nginx работает:
sudo systemctl status nginx

Cервис Nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://chat.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Запустите команду для выпуска SSL-сертификата.
sudo certbot --nginx -d chat.<ip-address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip-address> — IP-адрес вашей виртуальной машины.
<email> — email для регистрации сертификата.
9. После выпуска сертификата перейдите по адресу https://chat.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.

Настройте файервол:

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
/etc/nginx/sites-available/librechat.conf
```

Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины.

```bash
server
{
listen
80
;
server_name chat.
<
ip-address
>
.nip.io www.chat.
<
ip-address
>
.nip.io
;
location /
{
proxy_pass http://localhost:3080
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
}
}
```

Примените конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/librechat.conf /etc/nginx/sites-enabled/librechat.conf
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

Cервис Nginx должен быть в статусе «active (running)».

Перейдите по адресу http://chat.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».

Запустите команду для выпуска SSL-сертификата.

```bash
sudo
certbot
--nginx
-d
chat.
<
ip-address
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

- <ip-address> — IP-адрес вашей виртуальной машины.
- <email> — email для регистрации сертификата.

<ip-address> — IP-адрес вашей виртуальной машины.

<email> — email для регистрации сертификата.

После выпуска сертификата перейдите по адресу https://chat.<ip-address>.nip.io.

Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

## 5. Разверните приложение LibreChat

Разверните серверное приложение LibreChat с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.
2. Создайте структуру проекта:
mkdir -p $HOME/librechatcd $HOME/librechat
3. Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:
openssl rand -hex 32 # Save as JWT_SECRETopenssl rand -hex 32 # Save as JWT_REFRESH_SECRET
4. Создайте файл docker-compose.yml:
nano docker-compose.yml
5. Вставьте содержимое в файл docker-compose.yml:
services:mongo: image: mongo:6.0 restart: always volumes: - mongo-data:/data/db ports: - '27017:27017'
librechat: image: librechat/librechat:latest depends_on: - mongo ports: - '3080:3080' env_file: - ./.env volumes: - ./data:/app/data restart: always
volumes:mongo-data:
6. Создайте файл конфигурации .env:
nano docker.env
7. Вставьте содержимое в файл, заменив переменные на значения:
NODE_ENV=productionMONGO_URI=mongodb://mongo:27017/librechat
JWT_SECRET=<jwt_secret>JWT_REFRESH_SECRET=<jwt-refresh-secret>
DOMAIN_CLIENT=https://chat.<ip-address>.nip.ioDOMAIN_SERVER=https://chat.<ip-address>.nip.io
OPENAI_REVERSE_PROXY=https://foundation-models.api.cloud.ru/v1/OPENAI_API_KEY=<api-key>

Где:

<jwt-secret>, <jwt-refresh-secret> — секреты, сгенерированные ранее.
<ip-address> — публичный IP-адрес виртуальной машины.
<api-key> — ключ для доступа к сервису Foundation Models, сгенерированный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)на шаге 2.
8. Запустите сервис:
docker-compose up -d
9. Проверьте, что сервис запущен:
docker compose ps
10. Сгенерируйте пользователя с правами администратора:
sudo docker exec -it librechat_librechat_1 \ npm run create-user <email> yourname --email-verified=true

Где <email> — email-адрес пользователя.
Во время выполнения команды задайте логин и пароль для нового пользователя.
11. Перейдите по адресу https://chat.<ip-адрес>.nip.io.
Откроется страница LibreChat.
12. Авторизуйтесь в LibreChat, используя пароль пользователя с правами администратора.
13. В интерфейсе чата выберите Агенты -> OpenAI и выберите модель для работы в чате.
14. Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине ai-chat-service через серийную консоль или по SSH.

Создайте структуру проекта:

```bash
mkdir
-p
$HOME
/librechat
cd
$HOME
/librechat
```

Сгенерируйте уникальные ключи и сохраните их, они понадобятся в дальнейшем:

```bash
openssl rand
-hex
32
# Save as JWT_SECRET
openssl rand
-hex
32
# Save as JWT_REFRESH_SECRET
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте содержимое в файл docker-compose.yml:

```bash
services:
mongo:
image: mongo:6.0
restart: always
volumes:
- mongo-data:/data/db
ports:
-
'27017:27017'
librechat:
image: librechat/librechat:latest
depends_on:
- mongo
ports:
-
'3080:3080'
env_file:
- ./.env
volumes:
- ./data:/app/data
restart: always
volumes:
mongo-data:
```

Создайте файл конфигурации .env:

```bash
nano
docker.env
```

Вставьте содержимое в файл, заменив переменные на значения:

```bash
NODE_ENV
=
production
MONGO_URI
=
mongodb://mongo:27017/librechat
JWT_SECRET
=
<
jwt_secret
>
JWT_REFRESH_SECRET
=
<
jwt-refresh-secret
>
DOMAIN_CLIENT
=
https://chat.
<
ip-address
>
.nip.io
DOMAIN_SERVER
=
https://chat.
<
ip-address
>
.nip.io
OPENAI_REVERSE_PROXY
=
https://foundation-models.api.cloud.ru/v1/
OPENAI_API_KEY
=
<
api-key
>
```

Где:

- <jwt-secret>, <jwt-refresh-secret> — секреты, сгенерированные ранее.
- <ip-address> — публичный IP-адрес виртуальной машины.
- <api-key> — ключ для доступа к сервису Foundation Models, сгенерированный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)на шаге 2.

<jwt-secret>, <jwt-refresh-secret> — секреты, сгенерированные ранее.

<ip-address> — публичный IP-адрес виртуальной машины.

<api-key> — ключ для доступа к сервису Foundation Models, сгенерированный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-librechat)на шаге 2.

Запустите сервис:

```bash
docker-compose
up
-d
```

Проверьте, что сервис запущен:

```bash
docker
compose
ps
```

Сгенерируйте пользователя с правами администратора:

```bash
sudo
docker
exec
-it
librechat_librechat_1
\
npm
run create-user
<
email
>
yourname --email-verified
=
true
```

Где <email> — email-адрес пользователя.
Во время выполнения команды задайте логин и пароль для нового пользователя.

Перейдите по адресу https://chat.<ip-адрес>.nip.io.
Откроется страница LibreChat.

Авторизуйтесь в LibreChat, используя пароль пользователя с правами администратора.

В интерфейсе чата выберите Агенты -> OpenAI и выберите модель для работы в чате.

![../_images/s__model-selection.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__model-selection.png)

Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

![../_images/s__connect-librechat-chat.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__connect-librechat-chat.png)

## 6. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. [В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите ai-chat-service.
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

[В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите ai-chat-service.

Перейдите на вкладку Сетевые параметры.

В строке подсети нажмите и выберите Изменить группы безопасности.

![Кнопка с тремя горизонтальными точками](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__three-gorizontal-dots.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## Результат

В этой лабораторной работе вы развернули чат-сервис для работы в облаке Cloud.ru с сетевой изоляцией и публикацией по HTTPS.
Полученные навыки помогут вам создавать AI-сервисы с использованием сервисов Foundation Models.

Для командной работы [сконфигурируйте требуемый провайдер авторизации](https://www.librechat.ai/docs/configuration/authentication)сконфигурируйте требуемый провайдер авторизации.
