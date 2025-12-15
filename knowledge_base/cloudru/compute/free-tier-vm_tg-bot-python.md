---
title: Запуск Telegram-бота на Python на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python
topic: compute
---
# Запуск Telegram-бота на Python на виртуальной машине

С помощью этого руководства вы запустите Telegram-бота на Python на виртуальной машине.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для организации работы с Telegram через webhook.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для организации работы с Telegram через webhook.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Шаги:

1. [Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Создайте виртуальную машину.
2. [Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Настройте группу безопасности.
3. [Зарегистрируйте бота в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Зарегистрируйте бота в Telegram.
4. [Подготовьте и запустите код бота](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Подготовьте и запустите код бота.
5. [Протестируйте работу бота](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Протестируйте работу бота.

[Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Создайте виртуальную машину.

[Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Настройте группу безопасности.

[Зарегистрируйте бота в Telegram](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Зарегистрируйте бота в Telegram.

[Подготовьте и запустите код бота](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Подготовьте и запустите код бота.

[Протестируйте работу бота](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__tg-bot-python)Протестируйте работу бота.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Создайте виртуальную машину

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например telegram-bot-server.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.
4. В поле Логин укажите логин пользователя виртуальной машины, например user1.
5. Выберите метод аутентификации — пароль.
6. В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например telegram-bot-server.

В поле Название укажите название виртуальной машины, например telegram-bot-server.

На вкладке Публичные выберите образ Ubuntu 22.04.

Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.

В поле Логин укажите логин пользователя виртуальной машины, например user1.

Выберите метод аутентификации — пароль.

В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например telegram-bot-server.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина telegram-bot-server;
- статус виртуальной машины — «Запущена»;
- виртуальной машине назначен публичный IP-адрес.

отображается виртуальная машина telegram-bot-server;

статус виртуальной машины — «Запущена»;

виртуальной машине назначен публичный IP-адрес.

## 2. Настройте группу безопасности

Группы безопасности в облаке Evolution позволяют контролировать входящий и исходящий трафик для создаваемых ресурсов.

Вы настроите правила фильтрации трафика — разрешите весь исходящий трафик.
[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины telegram-bot-server.
2. Укажите Название группы безопасности, например telegram-bot-server.
3. Добавьте правило исходящего трафика:

Протокол — любой
Порт — оставьте пустым
Тип адресата — IP-адрес
Адресат — 0.0.0.0/0
4. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине telegram-bot-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины telegram-bot-server.

Укажите Название группы безопасности, например telegram-bot-server.

Добавьте правило исходящего трафика:

1. Протокол — любой
2. Порт — оставьте пустым
3. Тип адресата — IP-адрес
4. Адресат — 0.0.0.0/0

Протокол — любой

Порт — оставьте пустым

Тип адресата — IP-адрес

Адресат — 0.0.0.0/0

[Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине telegram-bot-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины», в разделе Сетевые параметры отображается группа безопасности telegram-bot-server.

![../_images/img__tg-bot__security-groups.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__tg-bot__security-groups.png)

## 3. Зарегистрируйте бота в Telegram

На этом шаге вы зарегистрируете в Telegram нового бота и получите его токен.

1. В Telegram найдите бота BotFather.
2. Выполните команду /newbot.
3. Задайте имя (name) и имя пользователя (username) для бота.
Имя пользователя должно заканчиваться на Bot или _bot.
В результате регистрации BotFather сообщит токен бота.
Сохраните его, он понадобится далее.
4. Убедитесь, что созданный бот отображается в Telegram при поиске по имени.

В Telegram найдите бота BotFather.

Выполните команду /newbot.

Задайте имя (name) и имя пользователя (username) для бота.

Имя пользователя должно заканчиваться на Bot или _bot.

В результате регистрации BotFather сообщит токен бота.
Сохраните его, он понадобится далее.

Убедитесь, что созданный бот отображается в Telegram при поиске по имени.

## 4. Подготовьте и запустите код бота

Для настройки виртуальной машины вы будете использовать серийную консоль в браузере.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине telegram-bot-server через серийную консоль.
2. Обновите индекс пакетов ОС, установите обновления пакетов и необходимые зависимости:
sudo apt update -ysudo apt upgrade -ysudo apt-get install python3 python3-pip -ypip3 install python-telegram-bot
3. Создайте отдельную папку для размещения бота и перейдите в нее:
mkdir ./appcd ./app
4. Cоздайте файл bot.py:
nano bot.py
5. [Скопируйте код бота](https://docs.python-telegram-bot.org/en/stable/examples.echobot.html)Скопируйте код бота в файл.
6. В строке 57 замените TOKEN на токен бота, полученный от BotFather.
7. Измененный код вставьте в серийную консоль.
8. Нажмите Ctrl + X, затем y, чтобы сохранить изменения.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине telegram-bot-server через серийную консоль.

Обновите индекс пакетов ОС, установите обновления пакетов и необходимые зависимости:

```bash
sudo
apt
update
-y
sudo
apt
upgrade
-y
sudo
apt-get
install
python3 python3-pip
-y
pip3
install
python-telegram-bot
```

Создайте отдельную папку для размещения бота и перейдите в нее:

```bash
mkdir
./app
cd
./app
```

Cоздайте файл bot.py:

```bash
nano
bot.py
```

[Скопируйте код бота](https://docs.python-telegram-bot.org/en/stable/examples.echobot.html)Скопируйте код бота в файл.

В строке 57 замените TOKEN на токен бота, полученный от BotFather.

![../_images/img__tg-bot__token.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__tg-bot__token.png)

Измененный код вставьте в серийную консоль.

![../_images/img__tg-bot__console-vm.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__tg-bot__console-vm.png)

Нажмите Ctrl + X, затем y, чтобы сохранить изменения.

Теперь вы запустите бота в качестве службы.
Бот будет работать постоянно и запускаться автоматически при старте или перезагрузке виртуальной машины.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине telegram-bot-server через серийную консоль.
2. Создайте файл python-bot.service:
sudo nano /etc/systemd/system/python-bot.service
3. Вставьте код в файл:
[Unit]Description=My Python BotWants=network-online.targetAfter=network-online.target
[Service]Type=simpleUser=<VM_username>ExecStart=/usr/bin/python3 /home/user1/app/bot.pyWorkingDirectory=/home/user1/app
[Install]WantedBy=multi-user.target

Где User — имя пользователя виртуальной машины telegram-bot-server.
4. Нажмите Ctrl + X, затем y, чтобы сохранить изменения.
5. Перезапустите systemd:
sudo systemctl daemon-reload
6. Включите службу python-bot.service:
sudo systemctl enable python-bot
7. Запустите службу python-bot.service:
sudo systemctl start python-bot
8. Выполните команду:
sudo systemctl status python-bot

В результате должен отобразиться статус службы — «Active (running)».
 
 Вывод команды

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине telegram-bot-server через серийную консоль.

Создайте файл python-bot.service:

```bash
sudo
nano
/etc/systemd/system/python-bot.service
```

Вставьте код в файл:

```bash
[
Unit
]
Description
=
My Python Bot
Wants
=
network
-
online
.
target
After
=
network
-
online
.
target
[
Service
]
Type
=
simple
User
=
<
VM_username
>
ExecStart
=
/
usr
/
bin
/
python3
/
home
/
user1
/
app
/
bot
.
py
WorkingDirectory
=
/
home
/
user1
/
app
[
Install
]
WantedBy
=
multi
-
user
.
target
```

Где User — имя пользователя виртуальной машины telegram-bot-server.

Нажмите Ctrl + X, затем y, чтобы сохранить изменения.

Перезапустите systemd:

```bash
sudo
systemctl daemon-reload
```

Включите службу python-bot.service:

```bash
sudo
systemctl
enable
python-bot
```

Запустите службу python-bot.service:

```bash
sudo
systemctl start python-bot
```

Выполните команду:

```bash
sudo
systemctl status python-bot
```

В результате должен отобразиться статус службы — «Active (running)».

## 5. Протестируйте работу бота

1. Найдите в Telegram вашего бота и напишите ему.
Бот поздоровается с вами в начале диалога, а затем будет повторять ваши сообщения.
2. [Перезагрузите](https://cloud.ru/docs/virtual-machines/ug/topics/guides__restart)Перезагрузите виртуальную машину.
3. Напишите сообщение в бота — бот должен ответить несмотря на перезагрузку сервера.

Найдите в Telegram вашего бота и напишите ему.
Бот поздоровается с вами в начале диалога, а затем будет повторять ваши сообщения.

[Перезагрузите](https://cloud.ru/docs/virtual-machines/ug/topics/guides__restart)Перезагрузите виртуальную машину.

Напишите сообщение в бота — бот должен ответить несмотря на перезагрузку сервера.

## Результат

Вы запустили Telegram-бота на Python в качестве службы, используя виртуальную машину.
