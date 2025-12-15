---
title: Развертывание почтового сервера Exim на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__mail-server
topic: compute
---
# Развертывание почтового сервера Exim на виртуальной машине

С помощью этого руководства вы запустите собственный почтовый сервер на базе решения Exim.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к ВМ из интернета.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к ВМ из интернета.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__mail-server)Разверните инфраструктуру.
2. [Настройте почтовый сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__mail-server)Настройте почтовый сервер.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__mail-server)Разверните инфраструктуру.

[Настройте почтовый сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__mail-server)Настройте почтовый сервер.

## 1. Разверните инфраструктуру

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.
3. [Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по инструкции.
4. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

В поле Название укажите mail-vm.
В разделе Образ → Публичные выберите: Ubuntu 22.04.
В поле Название загрузочного диска укажите mail-disk.
Включите опцию Подключить публичный IP.
В поле Тип IP-адреса выберите Прямой.
Заполните поле Имя пользователя, например mail-user.
В разделе Метод аутентификации выберите Публичный ключ и Пароль.
Укажите публичный ключ и ваш пароль для создаваемого пользователя.
В поле Имя хоста укажите mail-vm.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.

[Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по инструкции.

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите mail-vm.
2. В разделе Образ → Публичные выберите: Ubuntu 22.04.
3. В поле Название загрузочного диска укажите mail-disk.
4. Включите опцию Подключить публичный IP.
5. В поле Тип IP-адреса выберите Прямой.
6. Заполните поле Имя пользователя, например mail-user.
7. В разделе Метод аутентификации выберите Публичный ключ и Пароль.
8. Укажите публичный ключ и ваш пароль для создаваемого пользователя.
9. В поле Имя хоста укажите mail-vm.

В поле Название укажите mail-vm.

В разделе Образ → Публичные выберите: Ubuntu 22.04.

В поле Название загрузочного диска укажите mail-disk.

Включите опцию Подключить публичный IP.

В поле Тип IP-адреса выберите Прямой.

Заполните поле Имя пользователя, например mail-user.

В разделе Метод аутентификации выберите Публичный ключ и Пароль.

Укажите публичный ключ и ваш пароль для создаваемого пользователя.

В поле Имя хоста укажите mail-vm.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина mail-vm;
- статус виртуальной машины — «Запущена».

отображается виртуальная машина mail-vm;

статус виртуальной машины — «Запущена».

## 2. Настройте почтовый сервер

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине mail-vm по SSH.
2. Обновите ОС и ее пакеты:
sudo apt update -y
3. Установите Exim:
sudo apt install exim4 -y
4. Перейдите к настройке Exim:
sudo dpkg-reconfigure exim4-config
5. В открывшемся окне выберите режим работы local delivery only; not on a network.
Остальные параметры оставьте без изменений.
6. Отправьте тестовое письмо:
echo "Hello world" | mail -s "First letter" <user_name>@localhost

Где <user_name> — имя пользователя ВМ.
7. Проверьте отправку письма:
mail

Результат:
Mail version 8.1.2 01/15/2001. Type ? for help."/var/mail/<user_name>": 1 message 1 new>N 1 <user_name>@<vm_name> Fri Aug 29 15:46 20/580 smekta&Message 1:From <user_name>@<vm_name> Fri Aug 29 15:46:00 2025Envelope-to: mail-user@localhostDelivery-date: Fri, 29 Aug 2025 15:46:00 +0300To: <user_name>@localhostSubject: First letterMIME-Version: 1.0Content-Type: text/plain; charset="UTF-8"Content-Transfer-Encoding: 8bitFrom: <user_name>@<vm_name>Date: Fri, 29 Aug 2025 15:46:00 +0300
Hello world

Чтобы закрыть письмо, введите exit и нажмите Enter.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине mail-vm по SSH.

Обновите ОС и ее пакеты:

```bash
sudo
apt
update
-y
```

Установите Exim:

```bash
sudo
apt
install
exim4
-y
```

Перейдите к настройке Exim:

```bash
sudo
dpkg-reconfigure exim4-config
```

В открывшемся окне выберите режим работы local delivery only; not on a network.
Остальные параметры оставьте без изменений.

Отправьте тестовое письмо:

```bash
echo
"Hello world"
|
mail
-s
"First letter"
<
user_name
>
@localhost
```

Где <user_name> — имя пользователя ВМ.

Проверьте отправку письма:

```bash
mail
```

Результат:

```bash
Mail version
8.1
.2 01/15/2001. Type ?
for
help.
"/var/mail/<user_name>"
:
1
message
1
new
>
N
1
<
user_name
>
@
<
vm_name
>
Fri Aug
29
15
:46
20
/580 smekta
&
Message
1
:
From
<
user_name
>
@
<
vm_name
>
Fri Aug
29
15
:46:00
2025
Envelope-to: mail-user@localhost
Delivery-date: Fri,
29
Aug
2025
15
:46:00 +0300
To:
<
user_name
>
@localhost
Subject: First letter
MIME-Version:
1.0
Content-Type: text/plain
;
charset
=
"UTF-8"
Content-Transfer-Encoding: 8bit
From:
<
user_name
>
@
<
vm_name
>
Date: Fri,
29
Aug
2025
15
:46:00 +0300
Hello world
```

Чтобы закрыть письмо, введите exit и нажмите Enter.

## Результат

Вы настроили и запустили собственный почтовый сервер на базе Exim.
