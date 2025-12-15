---
title: Подключение LLM-шлюза Litellm к Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm
topic: ai-factory
---
# Подключение LLM-шлюза Litellm к Foundation Models

С помощью этого руководства вы развернете LLM-шлюз Litellm на бесплатной виртуальной машине в облаке Cloud.ru Evolution.
Вы создадите виртуальную машину Ubuntu 22.04, назначите ей публичный IP-адрес, установите Docker и Docker Compose, запустите Litellm и опубликуете сервис через Nginx с SSL-сертификатом, выпущенным в Let’s Encrypt.
В результате вы сконфигурируете Litellm для работы с Foundation Models и получите сервис, готовый к работе.

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
- [Litellm](https://www.litellm.ai/)Litellm — комплексная платформа, предназначенная для упрощения управления несколькими большими языковыми моделями (LLM) через унифицированное API.
LiteLLM предлагает унифицированное API, балансировку нагрузки, механизмы резервирования, отслеживание расходов и обработку ошибок.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Litellm](https://www.litellm.ai/)Litellm — комплексная платформа, предназначенная для упрощения управления несколькими большими языковыми моделями (LLM) через унифицированное API.
LiteLLM предлагает унифицированное API, балансировку нагрузки, механизмы резервирования, отслеживание расходов и обработку ошибок.

## Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Разверните необходимые ресурсы в облаке.
2. [Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Сгенерируйте API-ключ для доступа к Foundation Models.
3. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Настройте окружение на виртуальной машине.
4. [Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Настройте Nginx и HTTPS.
5. [Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Разверните приложение.
6. [Добавьте модели из Foundation Models в Litellm](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Добавьте модели из Foundation Models в Litellm.
7. [Обратитесь к добавленным моделям](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Обратитесь к добавленным моделям.
8. [Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Отключите доступ по SSH для виртуальной машины.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Разверните необходимые ресурсы в облаке.

[Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Сгенерируйте API-ключ для доступа к Foundation Models.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Настройте окружение на виртуальной машине.

[Настройте Nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Настройте Nginx и HTTPS.

[Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Разверните приложение.

[Добавьте модели из Foundation Models в Litellm](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Добавьте модели из Foundation Models в Litellm.

[Обратитесь к добавленным моделям](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Обратитесь к добавленным моделям.

[Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)Отключите доступ по SSH для виртуальной машины.

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

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием litellm-service и добавьте в нее правила:

Правило входящего трафика:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правило входящего трафика:

Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правило исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0
2. На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности litellm-service со статусом «Создана».
3. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название: litellm-service
Образ: публичный образ Ubuntu 22.04
Подключить публичный IP: включено
Тип IP: прямой IP-адрес
Группы безопасности: SSH-access_ru.AZ-1, litellm-service
Логин: litellm
Метод аутентификации: Публичный ключ и Пароль
Публичный ключ: укажите ранее созданный SSH-ключ
Пароль: задайте надежный пароль
Имя хоста: litellm-service
4. На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина litellm-service со статусом «Запущена».

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием litellm-service и добавьте в нее правила:

- Правило входящего трафика:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0
- Правило входящего трафика:

Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0
- Правило исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0

Правило входящего трафика:

- Протокол: TCP
- Порт: 443
- Тип источника: IP-адрес
- Источник: 0.0.0.0/0

Протокол: TCP

Порт: 443

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Правило входящего трафика:

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

На странице Сети → Группы безопасности убедитесь, что отображается группа безопасности litellm-service со статусом «Создана».

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название: litellm-service
- Образ: публичный образ Ubuntu 22.04
- Подключить публичный IP: включено
- Тип IP: прямой IP-адрес
- Группы безопасности: SSH-access_ru.AZ-1, litellm-service
- Логин: litellm
- Метод аутентификации: Публичный ключ и Пароль
- Публичный ключ: укажите ранее созданный SSH-ключ
- Пароль: задайте надежный пароль
- Имя хоста: litellm-service

Название: litellm-service

Образ: публичный образ Ubuntu 22.04

Подключить публичный IP: включено

Тип IP: прямой IP-адрес

Группы безопасности: SSH-access_ru.AZ-1, litellm-service

Логин: litellm

Метод аутентификации: Публичный ключ и Пароль

Публичный ключ: укажите ранее созданный SSH-ключ

Пароль: задайте надежный пароль

Имя хоста: litellm-service

На странице Инфраструктура → Виртуальные машины убедитесь, что отображается виртуальная машина litellm-service со статусом «Запущена».

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

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -y &&\sudo apt install -y curl apt-transport-https\ ca-certificates\ software-properties-common\ gnupg2\ lsb-release
3. Установите Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpgecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io -y
4. Выдайте текущему пользователю права на запуск Docker:
sudo usermod -aG docker $USERnewgrp docker
5. Установите Docker Compose:
sudo apt-get install docker-compose-plugin -y
6. Проверьте, что Docker и Docker Compose установлены корректно:
docker --versiondocker compose version
7. Установите Nginx сервер:
sudo apt install nginx -ysudo systemctl start nginxsudo systemctl enable nginx
8. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.

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

Выдайте текущему пользователю права на запуск Docker:

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

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Настройте файервол:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/litellm.conf
4. Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:
server { listen 80; server_name litellm.<ip-address>.nip.io www.litellm.<ip-address>.nip.io;
 location / { proxy_pass http://localhost:4000; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; }}
5. Примените конфигурацию и перезапустите nginx:
sudo ln -sf /etc/nginx/sites-available/litellm.conf /etc/nginx/sites-enabled/litellm.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что nginx работает:
sudo systemctl status nginx

Сервис nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://litellm.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Запустите команду для выпуска SSL-сертификата:
sudo certbot --nginx -d litellm.<ip-address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip-address> — IP-адрес вашей виртуальной машины.
<email> — email-адрес для регистрации сертификата.
9. После выпуска сертификата перейдите по адресу https://litellm.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.

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
/etc/nginx/sites-available/litellm.conf
```

Вставьте конфигурацию, заменив <ip-address> на IP-адрес вашей виртуальной машины:

```bash
server
{
listen
80
;
server_name litellm.
<
ip-address
>
.nip.io www.litellm.
<
ip-address
>
.nip.io
;
location /
{
proxy_pass http://localhost:4000
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

Примените конфигурацию и перезапустите nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/litellm.conf /etc/nginx/sites-enabled/litellm.conf
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

Перейдите по адресу http://litellm.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».

Запустите команду для выпуска SSL-сертификата:

```bash
sudo
certbot
--nginx
-d
litellm.
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
- <email> — email-адрес для регистрации сертификата.

<ip-address> — IP-адрес вашей виртуальной машины.

<email> — email-адрес для регистрации сертификата.

После выпуска сертификата перейдите по адресу https://litellm.<ip-address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
В свойствах сайта браузер отметит соединение как безопасное.

## 5. Разверните приложение

На этом шаге вы развернете LiteLLM с помощью Docker Compose.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.
2. Создайте структуру проекта:
mkdir -p $HOME/litellmcd $HOME/litellm
3. Создайте файл docker-compose.yml:
nano docker-compose.yml
4. Вставьте содержимое в файл docker-compose.yml:
services: postgres: image: postgres:15 container_name: postgres-for-litellm environment: POSTGRES_USER: litellm POSTGRES_PASSWORD: ${POSTGRES_PASSWORD} POSTGRES_DB: litellm_db volumes: - postgres_data:/var/lib/postgresql/data env_file: - ./.env ports: - "5432:5432" restart: unless-stopped healthcheck: test: ["CMD-SHELL", "pg_isready -U litellm -d litellm_db"] interval: 10s timeout: 5s retries: 5
 litellm: image: ghcr.io/berriai/litellm:main-stable container_name: litellm ports: - "4000:4000" volumes: - ./config.yaml:/app/config.yaml env_file: - ./.env environment: DATABASE_URL: "postgresql://litellm:${POSTGRES_PASSWORD}@postgres:5432/litellm_db" LITELLM_MASTER_KEY: ${LITELLM_MASTER_KEY} STORE_MODEL_IN_DB: "true" depends_on: postgres: condition: service_healthy restart: unless-stopped command: ["--config", "/app/config.yaml"]volumes: postgres_data:
5. Создайте файл конфигурации litellm config.yaml:
store_model_in_db: truetelemetry: true
6. Создайте файл конфигурации .env, в котором LITELLM_MASTER_KEY — мастер-ключ и пароль для Litellm, POSTGRES_PASSWORD — пароль от Postgres:
LITELLM_MASTER_KEY=<your_litellm_key>POSTGRES_PASSWORD=<your_postgress_password>

Ключи и пароли могут быть сгенерированы с помощью команды:
openssl rand -hex 32
7. Запустите сервис:
docker-compose up -d
8. Проверьте, что сервисы запущены:
docker compose ps
9. Перейдите по адресу https://litellm.<ip-address>.nip.io/ui.
Откроется страница Litellm UI, при входе система попросит ввести данные Администратора.
Для входа нужно указать:

Username — admin
Password — LITELLM_MASTER_KEY, созданный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)на шаге 6

[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__entry_litellm.png)

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине litellm-service через серийную консоль или по SSH.

Создайте структуру проекта:

```bash
mkdir
-p
$HOME
/litellm
cd
$HOME
/litellm
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Вставьте содержимое в файл docker-compose.yml:

```bash
services
:
postgres
:
image
:
postgres
:
15
container_name
:
postgres
-
for
-
litellm
environment
:
POSTGRES_USER
:
litellm
POSTGRES_PASSWORD
:
$
{
POSTGRES_PASSWORD
}
POSTGRES_DB
:
litellm_db
volumes
:
-
postgres_data
:
/var/lib/postgresql/data
env_file
:
-
./.env
ports
:
-
"5432:5432"
restart
:
unless
-
stopped
healthcheck
:
test
:
[
"CMD-SHELL"
,
"pg_isready -U litellm -d litellm_db"
]
interval
:
10s
timeout
:
5s
retries
:
5
litellm
:
image
:
ghcr.io/berriai/litellm
:
main
-
stable
container_name
:
litellm
ports
:
-
"4000:4000"
volumes
:
-
./config.yaml
:
/app/config.yaml
env_file
:
-
./.env
environment
:
DATABASE_URL
:
"postgresql://litellm:${POSTGRES_PASSWORD}@postgres:5432/litellm_db"
LITELLM_MASTER_KEY
:
$
{
LITELLM_MASTER_KEY
}
STORE_MODEL_IN_DB
:
"true"
depends_on
:
postgres
:
condition
:
service_healthy
restart
:
unless
-
stopped
command
:
[
"--config"
,
"/app/config.yaml"
]
volumes
:
postgres_data
:
```

Создайте файл конфигурации litellm config.yaml:

```bash
store_model_in_db
:
true
telemetry
:
true
```

Создайте файл конфигурации .env, в котором LITELLM_MASTER_KEY — мастер-ключ и пароль для Litellm, POSTGRES_PASSWORD — пароль от Postgres:

```bash
LITELLM_MASTER_KEY
=
<
your_litellm_key
>
POSTGRES_PASSWORD
=
<
your_postgress_password
>
```

Ключи и пароли могут быть сгенерированы с помощью команды:

```bash
openssl rand
-hex
32
```

Запустите сервис:

```bash
docker-compose
up
-d
```

Проверьте, что сервисы запущены:

```bash
docker
compose
ps
```

Перейдите по адресу https://litellm.<ip-address>.nip.io/ui.
Откроется страница Litellm UI, при входе система попросит ввести данные Администратора.

Для входа нужно указать:

- Username — admin
- Password — LITELLM_MASTER_KEY, созданный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)на шаге 6

Username — admin

Password — LITELLM_MASTER_KEY, созданный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)на шаге 6

![../_images/s__entry_litellm.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__entry_litellm.png)

## 6. Добавьте модели из Foundation Models в Litellm

1. Перейдите во вкладку Models → Endpoints, выберите Add Model.
2. В поле Provider выберите OpenAI-compatible Endpoints.
3. В поле LiteLLM Model Name(s) выберите Custom Model Name (Enter below).
4. В поле Enter custom model name введите нужную модель из Foundation Models с дополнительным префиксом /openai, например:

openai/openai/gpt-oss-120b
openai/zai-org/GLM-4.5
openai/Qwen/Qwen3-Coder-480B-A35B-Instruct
5. В поле Public Model Name вы можете задать удобное имя модели для обращения к ней через Litellm, например GLM-4.5 вместо openai/zai-org/GLM-4.5.
6. В поле API base укажите эндпоинт для обращения к модели — https://foundation-models.api.cloud.ru/v1/.
7. В поле OpenAI API Key введите API-ключ, полученный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)на шаге 2.
8. Внизу страницы нажмите Test Connect, если все параметры указаны верно, то в ответ вы получите сообщение Connection to custom successful!.
9. Нажмите Add Model.

Перейдите во вкладку Models → Endpoints, выберите Add Model.

В поле Provider выберите OpenAI-compatible Endpoints.

В поле LiteLLM Model Name(s) выберите Custom Model Name (Enter below).

В поле Enter custom model name введите нужную модель из Foundation Models с дополнительным префиксом /openai, например:

- openai/openai/gpt-oss-120b
- openai/zai-org/GLM-4.5
- openai/Qwen/Qwen3-Coder-480B-A35B-Instruct

openai/openai/gpt-oss-120b

openai/zai-org/GLM-4.5

openai/Qwen/Qwen3-Coder-480B-A35B-Instruct

В поле Public Model Name вы можете задать удобное имя модели для обращения к ней через Litellm, например GLM-4.5 вместо openai/zai-org/GLM-4.5.

В поле API base укажите эндпоинт для обращения к модели — https://foundation-models.api.cloud.ru/v1/.

В поле OpenAI API Key введите API-ключ, полученный [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-litellm)на шаге 2.

Внизу страницы нажмите Test Connect, если все параметры указаны верно, то в ответ вы получите сообщение Connection to custom successful!.

Нажмите Add Model.

Помимо моделей из Foundation Models, вы можете добавить и модели от других провайдеров, в том числе зарубежных, чтобы в дальнейшем обращаться к ним через единый API-ключ Litellm.

1. Создайте виртуальный ключ Litellm:

Перейдите во вкладку Virtual Keys.
Нажмите Create New Key.
Вы можете дополнительно настроить модели, которые будут доступны по этому ключу, лимиты на количество запросов в минуту, срок жизни ключа и другие параметры.
Сохраните сгенерированный ключ.

Создайте виртуальный ключ Litellm:

1. Перейдите во вкладку Virtual Keys.
2. Нажмите Create New Key.
Вы можете дополнительно настроить модели, которые будут доступны по этому ключу, лимиты на количество запросов в минуту, срок жизни ключа и другие параметры.
3. Сохраните сгенерированный ключ.

Перейдите во вкладку Virtual Keys.

Нажмите Create New Key.
Вы можете дополнительно настроить модели, которые будут доступны по этому ключу, лимиты на количество запросов в минуту, срок жизни ключа и другие параметры.

Сохраните сгенерированный ключ.

## 7. Обратитесь к добавленным моделям

Теперь к добавленным моделям можно обращаться через единый эндпоинт litellm:

```bash
from
openai
import
OpenAI
api_key
=
"litellm_api_key"
#API key generated in the previous step
url
=
https
:
//
litellm
.
<
ip
-
address
>
.
nip
.
io
/
v1
#Substitute the IP address with the service
client
=
OpenAI
(
api_key
=
api_key
,
base_url
=
url
)
response
=
client
.
chat
.
completions
.
create
(
model
=
"GLM-4.5"
,
max_tokens
=
5000
,
temperature
=
0.5
,
presence_penalty
=
0
,
top_p
=
0.95
,
messages
=
[
{
"role"
:
"user"
,
"content"
:
"Как написать хороший код?"
}
]
)
print
(
response
.
choices
[
0
]
.
message
.
content
)
```

Для повышения надежности можно использовать несколько разных провайдеров моделей.

Для использования нескольких провайдеров моделей:

1. Перейдите во вкладку Settings → Router Settings → Fallbacks.
2. Нажмите Add Fallbacks.
3. Выберите основную и резервную модель.
При недоступности основной модели запросы будут переадресованы на резервную.

Перейдите во вкладку Settings → Router Settings → Fallbacks.

Нажмите Add Fallbacks.

Выберите основную и резервную модель.
При недоступности основной модели запросы будут переадресованы на резервную.

## 8. Отключите доступ по SSH для виртуальной машины

Для повышения безопасности закройте доступ по SSH, после того как вы развернули и настроили сервис.

1. [В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите litellm-service.
3. Перейдите на вкладку Сетевые параметры.
4. В строке подсети нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.

[В личном кабинете Cloud.ru](https://console.cloud.ru/registration)В личном кабинете Cloud.ru на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите litellm-service.

Перейдите на вкладку Сетевые параметры.

В строке подсети нажмите и выберите Изменить группы безопасности.

![Кнопка с тремя горизонтальными точками](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__three-gorizontal-dots.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через серийную консоль виртуальной машины.

## Результат

В этой лабораторной работе вы развернули LLM-шлюз Litellm для работы в облаке Cloud.ru с возможностью использования разных LLM-провайдеров по единому API-ключу.
Полученные навыки помогут вам создавать надежные и удобные AI-сервисы с использованием моделей Foundation Models.
