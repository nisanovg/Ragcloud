---
title: Развертывание личного менеджера паролей на базе PassBolt на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt
topic: compute
---
# Развертывание личного менеджера паролей на базе PassBolt на виртуальной машине

С помощью этого руководства вы развернете менеджер паролей на базе Passbolt на виртуальной машине.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к менеджеру паролей через интернет.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к менеджеру паролей через интернет.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Шаги:

1. [Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Создайте виртуальную машину.
2. [Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Настройте группу безопасности.
3. [Установите Passbolt](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Установите Passbolt.
4. [Настройте Passbolt](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Настройте Passbolt.

[Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Создайте виртуальную машину.

[Настройте группу безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Настройте группу безопасности.

[Установите Passbolt](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Установите Passbolt.

[Настройте Passbolt](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)Настройте Passbolt.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Создайте домен с помощью сервиса [nip.io](https://nip.io/)nip.io, если не планируете использовать собственное зарегистрированное доменное имя.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Создайте домен с помощью сервиса [nip.io](https://nip.io/)nip.io, если не планируете использовать собственное зарегистрированное доменное имя.

## 1. Создайте виртуальную машину

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например passbolt-server.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.
4. В поле Логин укажите логин пользователя виртуальной машины, например user1.
5. Выберите метод аутентификации — пароль.
6. В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например passbolt-server.

В поле Название укажите название виртуальной машины, например passbolt-server.

На вкладке Публичные выберите образ Ubuntu 22.04.

Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.

В поле Логин укажите логин пользователя виртуальной машины, например user1.

Выберите метод аутентификации — пароль.

В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например passbolt-server.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина passbolt-server;
- статус виртуальной машины — «Запущена»;
- виртуальной машине назначен публичный IP-адрес.

отображается виртуальная машина passbolt-server;

статус виртуальной машины — «Запущена»;

виртуальной машине назначен публичный IP-адрес.

## 2. Настройте группу безопасности

Группы безопасности в облаке Evolution позволяют контролировать входящий и исходящий трафик для создаваемых ресурсов.

Вы настроите правила фильтрации трафика — разрешите весь входящий трафик по порту 443 (HTTPS) и весь исходящий трафик.
[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины passbolt-server.
2. Укажите Название группы безопасности, например passbolt-server.
3. Добавьте правила входящего и исходящего трафика.
Правила входящего трафика:

Правило 1:

Протокол — TCP
Порт — 443
Тип источника — IP-адрес
Источник — 0.0.0.0/0

Правило 2

Протокол — TCP
Порт — 80
Тип источника — IP-адрес
Источник — 0.0.0.0/0

Правила исходящего трафика:

Протокол — любой
Порт — оставьте пустым
Тип адресата — IP-адрес
Адресат — 0.0.0.0/0
4. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине passbolt-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Выберите Зону доступности, в которой необходимо разместить группу безопасности. Укажите ту же зону доступности, что выбрана для виртуальной машины passbolt-server.

Укажите Название группы безопасности, например passbolt-server.

Добавьте правила входящего и исходящего трафика.

Правила входящего трафика:

1. Правило 1:

Протокол — TCP
Порт — 443
Тип источника — IP-адрес
Источник — 0.0.0.0/0
2. Правило 2

Протокол — TCP
Порт — 80
Тип источника — IP-адрес
Источник — 0.0.0.0/0

Правило 1:

1. Протокол — TCP
2. Порт — 443
3. Тип источника — IP-адрес
4. Источник — 0.0.0.0/0

Протокол — TCP

Порт — 443

Тип источника — IP-адрес

Источник — 0.0.0.0/0

Правило 2

1. Протокол — TCP
2. Порт — 80
3. Тип источника — IP-адрес
4. Источник — 0.0.0.0/0

Протокол — TCP

Порт — 80

Тип источника — IP-адрес

Источник — 0.0.0.0/0

Правила исходящего трафика:

1. Протокол — любой
2. Порт — оставьте пустым
3. Тип адресата — IP-адрес
4. Адресат — 0.0.0.0/0

Протокол — любой

Порт — оставьте пустым

Тип адресата — IP-адрес

Адресат — 0.0.0.0/0

[Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине passbolt-server.
Если в группе безопасности присутствуют другие виртуальные машины, [исключите их из группы](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-from-sg)исключите их из группы.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины», в разделе Сетевые параметры отображается группа безопасности passbolt-server.

![../_images/img__passbolt__security-groups.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__passbolt__security-groups.png)

## 3. Установите Passbolt

Для настройки виртуальной машины вы будете использовать серийную консоль в браузере.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине passbolt-server через серийную консоль.
2. Обновите индекс пакетов ОС и установите обновления пакетов:
sudo apt update -ysudo apt upgrade -y
3. Скачайте и запустите скрипт настройки репозиториев Passbolt:
wget "https://download.passbolt.com/ce/installer/passbolt-repo-setup.ce.sh"wget https://github.com/passbolt/passbolt-dep-scripts/releases/latest/download/passbolt-ce-SHA512SUM.txtsha512sum -c passbolt-ce-SHA512SUM.txt && sudo bash ./passbolt-repo-setup.ce.sh || echo \"Bad checksum. Aborting\" && rm -f passbolt-repo-setup.ce.sh

В результате выполнения скриптов вы увидите сообщение, что настройка репозиториев завершена успешно.
 
 Вывод команды

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине passbolt-server через серийную консоль.

Обновите индекс пакетов ОС и установите обновления пакетов:

```bash
sudo
apt
update
-y
sudo
apt
upgrade
-y
```

Скачайте и запустите скрипт настройки репозиториев Passbolt:

```bash
wget
"https://download.passbolt.com/ce/installer/passbolt-repo-setup.ce.sh"
wget
https://github.com/passbolt/passbolt-dep-scripts/releases/latest/download/passbolt-ce-SHA512SUM.txt
sha512sum
-c
passbolt-ce-SHA512SUM.txt
&&
sudo
bash
./passbolt-repo-setup.ce.sh
||
echo
\
"Bad checksum. Aborting
\
"
&&
rm
-f
passbolt-repo-setup.ce.sh
```

В результате выполнения скриптов вы увидите сообщение, что настройка репозиториев завершена успешно.

Подготовьте параметры для установки Passbolt и выполните установку:

1. Подготовьте доменное имя вида {Публичный_IP-адрес_виртуальной_машины_passbolt-server}.nip.io, например 1.1.1.1.nip.io.
Или используйте собственный зарегистрированный домен.
2. Сконфигурируйте параметры установки:
 echo passbolt-ce-server passbolt/mysql-configuration boolean true | sudo debconf-set-selections echo passbolt-ce-server passbolt/mysql-passbolt-username string pb_user | sudo debconf-set-selections echo passbolt-ce-server passbolt/mysql-passbolt-password password P@ssw0rd | sudo debconf-set-selections echo passbolt-ce-server passbolt/mysql-passbolt-password-repeat password P@ssw0rd | sudo debconf-set-selections echo passbolt-ce-server passbolt/mysql-passbolt-dbname string passbolt | sudo debconf-set-selections echo passbolt-ce-server passbolt/nginx-configuration boolean true | sudo debconf-set-selections echo passbolt-ce-server passbolt/nginx-configuration-three-choices select auto | sudo debconf-set-selections echo passbolt-ce-server passbolt/nginx-domain string 176.109.108.146.nip.io | sudo debconf-set-selections
В ``P@ssw0rd`` задайте пароль.
3. Выполните установку Passbolt:
sudo DEBIAN_FRONTEND=noninteractive apt-get install passbolt-ce-server -y

Подготовьте доменное имя вида {Публичный_IP-адрес_виртуальной_машины_passbolt-server}.nip.io, например 1.1.1.1.nip.io.
Или используйте собственный зарегистрированный домен.

Сконфигурируйте параметры установки:

```bash
echo
passbolt-ce-server passbolt/mysql-configuration boolean
true
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/mysql-passbolt-username string pb_user
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/mysql-passbolt-password password P@ssw0rd
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/mysql-passbolt-password-repeat password P@ssw0rd
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/mysql-passbolt-dbname string passbolt
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/nginx-configuration boolean
true
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/nginx-configuration-three-choices
select
auto
|
sudo
debconf-set-selections
echo
passbolt-ce-server passbolt/nginx-domain string
176.109
.108.146.nip.io
|
sudo
debconf-set-selections
В `
`
P@ssw0rd
`
` задайте пароль.
```

Выполните установку Passbolt:

```bash
sudo
DEBIAN_FRONTEND
=
noninteractive
apt-get
install
passbolt-ce-server
-y
```

Убедитесь, что при переходе по домену в браузере ображается мастер настройки Passbolt.

![../_images/img__passbolt__config.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__passbolt__config.png)

## 4. Настройте Passbolt

1. Откройте в браузере {Публичный_IP-адрес_виртуальной_машины_passbolt-server}.nip.io, например 1.1.1.1.nip.io.
2. Нажмите Get Started.
3. В открывшемся окне проверьте, что все обязательные поля заполнены и нажмите Start cofiguration.
4. Заполните параметры базы данных:

Database connection url — localhost.
Username — pb_user.
Password — пароль, который вы указали [на шаге 3](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)на шаге 3.
Database name — passbolt.
5. Нажмите Next.
6. На странице «Create a new OpenPGP key for your server» заполните поля:

Server Name — укажите произвольное имя сервера.
Server Email—укажите вашу электронную почту.
7. Перейдите на вкладку Emails и укажите параметры почтового сервера.
Вы можете использовать вашу личную почту, а параметры конфигурации (SMTP Host, Port и т.д.) получить в документации вашего почтового провайдера.
8. Нажмите Next.
9. Заполните обязательные поля на странице «Admin user details» — First name, Last name, Username.
10. Нажмите Next.
Дождитесь завершения настройки Passbolt.

Откройте в браузере {Публичный_IP-адрес_виртуальной_машины_passbolt-server}.nip.io, например 1.1.1.1.nip.io.

Нажмите Get Started.

В открывшемся окне проверьте, что все обязательные поля заполнены и нажмите Start cofiguration.

![../_images/img__passbolt__start-config.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__passbolt__start-config.png)

Заполните параметры базы данных:

- Database connection url — localhost.
- Username — pb_user.
- Password — пароль, который вы указали [на шаге 3](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)на шаге 3.
- Database name — passbolt.

Database connection url — localhost.

Username — pb_user.

Password — пароль, который вы указали [на шаге 3](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__passbolt)на шаге 3.

Database name — passbolt.

Нажмите Next.

На странице «Create a new OpenPGP key for your server» заполните поля:

- Server Name — укажите произвольное имя сервера.
- Server Email—укажите вашу электронную почту.

Server Name — укажите произвольное имя сервера.

Server Email—укажите вашу электронную почту.

Перейдите на вкладку Emails и укажите параметры почтового сервера.

Вы можете использовать вашу личную почту, а параметры конфигурации (SMTP Host, Port и т.д.) получить в документации вашего почтового провайдера.

Нажмите Next.

Заполните обязательные поля на странице «Admin user details» — First name, Last name, Username.

Нажмите Next.

Дождитесь завершения настройки Passbolt.

Настройте административный аккаунт:

1. После окончания настройки, появится окно с предложением установить расширение для браузера.
Скачайте и установите расширение.
2. Создайте новый ключ.
Passbolt попросит вас создать или импортировать ключ, который будет позже использоваться для вашей идентификации и шифрования ваших паролей.
Ваш ключ должен быть защищен паролем.
3. Загрузите комплект восстановления.
Это необходимый шаг.
Ваш ключ — единственный способ получить доступ к вашей учетной записи и паролям.
Если вы потеряете ключ, ваши зашифрованные данные будут утеряны, даже если вы помните свою парольную фразу.
4. Определите токен безопасности.
Выбор цвета и трех символов — вторичный механизм безопасности, который поможет вам митигировать фишинговые атаки.
Каждый раз, когда вы выполняете критичные операции, вы должны видеть этот токен.
5. Ваша учетная запись администратора настроена.
Вы будете перенаправлены на страницу входа в Passbolt.

После окончания настройки, появится окно с предложением установить расширение для браузера.
Скачайте и установите расширение.

Создайте новый ключ.
Passbolt попросит вас создать или импортировать ключ, который будет позже использоваться для вашей идентификации и шифрования ваших паролей.
Ваш ключ должен быть защищен паролем.

Загрузите комплект восстановления.

Это необходимый шаг.
Ваш ключ — единственный способ получить доступ к вашей учетной записи и паролям.
Если вы потеряете ключ, ваши зашифрованные данные будут утеряны, даже если вы помните свою парольную фразу.

Определите токен безопасности.
Выбор цвета и трех символов — вторичный механизм безопасности, который поможет вам митигировать фишинговые атаки.
Каждый раз, когда вы выполняете критичные операции, вы должны видеть этот токен.

Ваша учетная запись администратора настроена.

Вы будете перенаправлены на страницу входа в Passbolt.

Проверьте, что вы можете:

- создать пароль в браузере;
- при переходе на сайты заполнить внесенные пароли через расширение браузера;
- [подключить приложение на мобильном телефоне](https://www.passbolt.com/blog/passbolt-mobile-app-is-here)подключить приложение на мобильном телефоне к вашему серверу Passbolt.

создать пароль в браузере;

при переходе на сайты заполнить внесенные пароли через расширение браузера;

[подключить приложение на мобильном телефоне](https://www.passbolt.com/blog/passbolt-mobile-app-is-here)подключить приложение на мобильном телефоне к вашему серверу Passbolt.

## Результат

Вы установили и настроили собственный безопасный менеджер паролей на базе Passbolt.
