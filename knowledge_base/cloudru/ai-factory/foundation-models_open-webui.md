---
title: Интеграция веб-интерфейса Open WebUI с Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui
topic: ai-factory
---
# Интеграция веб-интерфейса Open WebUI с Foundation Models

С помощью этого руководства вы разверните веб-интерфейс Open WebUI на бесплатной виртуальной машине в облаке Cloud.ru Evolution.
Создадите виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите Open WebUI и опубликуете сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt.
В результате вы сконфигурируете Open WebUI для работы с Foundation Models и получите сервис, готовый к работе.

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
- [Open WebUI](https://openwebui.com/)Open WebUI — веб-интерфейс с открытым исходным кодом для работы с различными моделями искусственного интеллекта.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Open WebUI](https://openwebui.com/)Open WebUI — веб-интерфейс с открытым исходным кодом для работы с различными моделями искусственного интеллекта.

## Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Разверните необходимые ресурсы в облаке.
2. [Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Сгенерируйте API-ключ для доступа к Foundation Models.
3. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Настройте окружение на виртуальной машине.
4. [Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Настройте Nginx и HTTPS.
5. [Разверните приложение Open WebUI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Разверните приложение Open WebUI.
6. [Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Отключите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Разверните необходимые ресурсы в облаке.

[Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Сгенерируйте API-ключ для доступа к Foundation Models.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Настройте окружение на виртуальной машине.

[Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Настройте Nginx и HTTPS.

[Разверните приложение Open WebUI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Разверните приложение Open WebUI.

[Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)Отключите доступ по SSH для виртуальной машины.

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

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием open-web-ui и добавьте в нее правила:

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
2. На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности open-web-ui со статусом «Создана».
3. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название: open-web-ui
Образ: публичный образ Ubuntu 22.04
Подключить публичный IP: включено
Публичный IP: Арендовать новый
Группы безопасности: SSH-access_ru.AZ-1, open-web-ui
Логин: openwebui
Метод аутентификации: Публичный ключ и Пароль
Публичный ключ: укажите ранее созданный SSH-ключ
Пароль: задайте надежный пароль
Имя хоста: open-web-ui
4. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина open-web-ui со статусом «Запущена».

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием open-web-ui и добавьте в нее правила:

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

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности open-web-ui со статусом «Создана».

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название: open-web-ui
- Образ: публичный образ Ubuntu 22.04
- Подключить публичный IP: включено
- Публичный IP: Арендовать новый
- Группы безопасности: SSH-access_ru.AZ-1, open-web-ui
- Логин: openwebui
- Метод аутентификации: Публичный ключ и Пароль
- Публичный ключ: укажите ранее созданный SSH-ключ
- Пароль: задайте надежный пароль
- Имя хоста: open-web-ui

Название: open-web-ui

Образ: публичный образ Ubuntu 22.04

Подключить публичный IP: включено

Публичный IP: Арендовать новый

Группы безопасности: SSH-access_ru.AZ-1, open-web-ui

Логин: openwebui

Метод аутентификации: Публичный ключ и Пароль

Публичный ключ: укажите ранее созданный SSH-ключ

Пароль: задайте надежный пароль

Имя хоста: open-web-ui

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина open-web-ui со статусом «Запущена».

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

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -y &&\sudo apt install -y curl apt-transport-https\ ca-certificates\ software-properties-common\ gnupg2\ lsb-release
3. После обновления желательно перезагрузить машину:
sudo reboot
4. Установите Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpgecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io -y
5. Дайте текущему пользователю права на запуск Docker:
sudo usermod -aG docker $USERnewgrp docker
6. Установите Docker Compose:
sudo apt-get install docker-compose -y
7. Проверьте, что Docker и Docker Compose установлены корректно:
docker --versiondocker compose version
8. Установите сервер Nginx:
sudo apt install nginx -ysudo systemctl start nginxsudo systemctl enable nginx
9. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

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

После обновления желательно перезагрузить машину:

```bash
sudo
reboot
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
docker-compose
-y
```

Проверьте, что Docker и Docker Compose установлены корректно:

```bash
docker
--version
docker
compose version
```

Установите сервер Nginx:

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

На этом шаге настройте службу Nginx и обеспечьте доступ по HTTPS.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.
2. Настройте файервол:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/openwebui.conf
4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:
server { listen 80; server_name webui.<ip-address>.nip.io www.webui.<ip-address>.nip.io;
 location / { proxy_pass http://localhost:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_http_version 1.1;proxy_set_header Upgrade $http_upgrade;proxy_set_header Connection "upgrade"; }}
5. Примените конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/openwebui.conf /etc/nginx/sites-enabled/openwebui.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что Nginx работает:
sudo systemctl status nginx

Сервис Nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://webui.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Запустите команду для выпуска SSL-сертификата:
sudo certbot --nginx -d webui.<ip-address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip-address> — IP-адрес вашей виртуальной машины.
<email> — email для регистрации сертификата.
9. После выпуска сертификата перейдите по адресу https://webui.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

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
/etc/nginx/sites-available/openwebui.conf
```

Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:

```bash
server
{
listen
80
;
server_name webui.
<
ip-address
>
.nip.io www.webui.
<
ip-address
>
.nip.io
;
location /
{
proxy_pass http://localhost:8080
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
proxy_http_version
1.1
;
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"upgrade"
;
}
}
```

Примените конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/openwebui.conf /etc/nginx/sites-enabled/openwebui.conf
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

Перейдите по адресу http://webui.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».

Запустите команду для выпуска SSL-сертификата:

```bash
sudo
certbot
--nginx
-d
webui.
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

После выпуска сертификата перейдите по адресу https://webui.<ip-address>.nip.io.

Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

## 5. Разверните приложение Open WebUI

Разверните серверное приложение Open WebUI с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.
2. Создайте структуру проекта:
mkdir -p $HOME/openwebuicd $HOME/openwebui
3. Создайте файл docker-compose.yml:
nano docker-compose.yml
4. Вставьте содержимое в файл docker-compose.yml:
services: open-web-ui: image: ghcr.io/open-webui/open-webui:latest ports: - '8080:8080' env_file: - ./.env volumes: - open-web-ui:/app/backend/data restart: always
volumes: open-web-ui:
5. Создайте файл конфигурации .env:
nano .env
6. Вставьте содержимое в файл, заменив переменные на значения:
OPENAI_API_BASE_URL=https://foundation-models.api.cloud.ru/v1/OPENAI_API_KEY=<api-key>

Где <api-key> — ключ для доступа к сервису Foundation Models, сгенерированный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)на шаге 2.
7. Запустите сервис:
docker-compose up -d
8. Проверьте, что сервис запущен:
docker compose ps
9. Перейдите по адресу https://webui.<ip-address>.nip.io.
Откроется страница Open WebUI, при первом входе система попросит ввести регистрационные данные Администратора.
10. В интерфейсе Open WebUI выберите модель для работы.
11. Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине open-web-ui через серийную консоль или по SSH.

Создайте структуру проекта:

```bash
mkdir
-p
$HOME
/openwebui
cd
$HOME
/openwebui
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте содержимое в файл docker-compose.yml:

```bash
services:
open-web-ui:
image: ghcr.io/open-webui/open-webui:latest
ports:
-
'8080:8080'
env_file:
- ./.env
volumes:
- open-web-ui:/app/backend/data
restart: always
volumes:
open-web-ui:
```

Создайте файл конфигурации .env:

```bash
nano
.env
```

Вставьте содержимое в файл, заменив переменные на значения:

```bash
OPENAI_API_BASE_URL
=
https://foundation-models.api.cloud.ru/v1/
OPENAI_API_KEY
=
<
api-key
>
```

Где <api-key> — ключ для доступа к сервису Foundation Models, сгенерированный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__open-webui)на шаге 2.

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

Перейдите по адресу https://webui.<ip-address>.nip.io.
Откроется страница Open WebUI, при первом входе система попросит ввести регистрационные данные Администратора.

![../_images/s__auth-open-webui.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__auth-open-webui.png)

В интерфейсе Open WebUI выберите модель для работы.

Введите ваш запрос в чат и получите ответ от LLM-модели Foundation Models.

![../_images/s__request-open-webui.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__request-open-webui.png)

## 6. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. [В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите open-web-ui.
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

[В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите open-web-ui.

Перейдите на вкладку Сетевые параметры.

В строке подсети нажмите и выберите Изменить группы безопасности.

![Кнопка с тремя горизонтальными точками](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__three-gorizontal-dots.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## Результат

В данной лабораторной работе вы развернули чат-сервис для работы в облаке Cloud.ru с сетевой изоляцией и публикацией по HTTPS.
Полученные навыки помогут вам создавать AI-сервисы с использованием сервисов Foundation Models.

Вы можете добавить [аутентификацию по SSO](https://docs.openwebui.com/features/sso)аутентификацию по SSO или [подключить внешнее S3 хранилище](https://docs.openwebui.com/tutorials/s3-storage)подключить внешнее S3 хранилище для хранения файлов, которые пользователи добавляют в Open WebUI при работе с моделями, например, [Evolution Object Storage](https://cloud.ru/products/evolution-object-storage)Evolution Object Storage.
