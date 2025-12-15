---
title: Запуск личного блога на WordPress на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress
topic: compute
---
# Запуск личного блога на WordPress на виртуальной машине

С помощью этого руководства вы научитесь разворачивать личный блог на WordPress на виртуальной машине в облаке Cloud.ru.
В результате вы получите работающий сайт с защищенным HTTPS-соединением, используя бесплатный домен от сервиса nip.io или собственное доменное имя.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к блогу через интернет.
- (Опционально) Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к блогу через интернет.

(Опционально) Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Разверните ресурсы в облаке.
2. [Установите и настройте WordPress](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Установите и настройте WordPress.
3. [Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Настройте доменное имя.
4. [Авторизуйтесь в WordPress](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Авторизуйтесь в WordPress.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Разверните ресурсы в облаке.

[Установите и настройте WordPress](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Установите и настройте WordPress.

[Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Настройте доменное имя.

[Авторизуйтесь в WordPress](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__blog-wordpress)Авторизуйтесь в WordPress.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Разверните ресурсы в облаке

На этом шаге вы создадите бесплатную виртуальную машину, назначите ей публичный IP-адрес и настроите правила фильтрации трафика через него.

1. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

Название — wordpress-server.
Образ — на вкладке Маркетплейс выберите образ LAMP.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Логин — оставьте значение по умолчанию или укажите новый.
Метод аутентификации — Публичный ключ и Пароль.
Пароль — задайте пароль пользователя.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

ВниманиеОбраз LAMP содержит предустановленные дистрибутивы Apache, СУБД MySQL и PHP. Если вы используете другой образ, установите дистрибутивы самостоятельно.
2. Уточните [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, в которой была создана виртуальная машина.
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием wordpress-server в той же зоне доступности и добавьте в нее правила:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбой—IP-адрес0.0.0.0/0
4. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине.
5. Проверьте создание ресурсов:

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности wordpress-server со статусом «Создана».
Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина wordpress-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.
Скопируйте и сохраните публичный IP-адрес, он понадобится далее.

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

- Название — wordpress-server.
- Образ — на вкладке Маркетплейс выберите образ LAMP.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Логин — оставьте значение по умолчанию или укажите новый.
- Метод аутентификации — Публичный ключ и Пароль.
- Пароль — задайте пароль пользователя.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Название — wordpress-server.

Образ — на вкладке Маркетплейс выберите образ LAMP.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Логин — оставьте значение по умолчанию или укажите новый.

Метод аутентификации — Публичный ключ и Пароль.

Пароль — задайте пароль пользователя.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Образ LAMP содержит предустановленные дистрибутивы Apache, СУБД MySQL и PHP. Если вы используете другой образ, установите дистрибутивы самостоятельно.

Уточните

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием wordpress-server в той же зоне доступности и добавьте в нее правила:

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

—

IP-адрес

0.0.0.0/0

[Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине.

Проверьте создание ресурсов:

1. Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности wordpress-server со статусом «Создана».
2. Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина wordpress-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.
3. Скопируйте и сохраните публичный IP-адрес, он понадобится далее.

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности wordpress-server со статусом «Создана».

Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина wordpress-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.

Скопируйте и сохраните публичный IP-адрес, он понадобится далее.

## 2. Установите и настройте WordPress

На этом шаге вы установите и настроите WordPress на виртуальной машине.

1. [Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.
2. Обновите систему и установите утилиты:
sudo apt update && sudo apt upgrade -y
3. Чтобы WordPress работал корректно, включите модуль Apache mod_rewrite и перезапустите его:
sudo a2enmod rewritesudo systemctl restart apache2
4. Скачайте последнюю версию Wordpress и распакуйте файлы:
wget -c http://wordpress.org/latest.tar.gzsudo tar -xzvf latest.tar.gz
5. Перенесите распакованные файлы в папку веб-сервера и удалите файл index.html:
sudo mv wordpress/* /var/www/html/sudo rm /var/www/html/index.html
6. Для корректной работы веб-сервера с файлами установите для них нужные права — пользователь и группа www-data:
sudo chown -R www-data:www-data /var/www/html/sudo chmod -R 755 /var/www/html/
7. Задайте пароль для подключения к базе данных — тот, который вы задавали при создании виртуальной машины.
sudo mysql -u root -p
8. Выполните построчно следующие команды.
В <password> укажите пароль для пользователя wp_user.
CREATE DATABASE wp_database;CREATE USER 'wp_user'@'localhost' IDENTIFIED BY '<password>';GRANT ALL PRIVILEGES ON wp_database.* TO 'wp_user'@'localhost';FLUSH PRIVILEGES;EXIT;
9. Настройте WordPress с помощью шаблона wp-config-sample.php.
Выполните команды копирования и заполнения шаблонного файла.
В <password> укажите пароль для пользователя wp_user, заданный при настройке базы данных.
sudo cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.phpsudo sed -i -e "s/database_name_here/wp_database/" /var/www/html/wp-config.phpsudo sed -i -e "s/username_here/wp_user/g" /var/www/html/wp-config.phpsudo sed -i -e "s/password_here/password/g" /var/www/html/wp-config.php

[Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.

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

Чтобы WordPress работал корректно, включите модуль Apache mod_rewrite и перезапустите его:

```bash
sudo
a2enmod rewrite
sudo
systemctl restart apache2
```

Скачайте последнюю версию Wordpress и распакуйте файлы:

```bash
wget
-c
http://wordpress.org/latest.tar.gz
sudo
tar
-xzvf
latest.tar.gz
```

Перенесите распакованные файлы в папку веб-сервера и удалите файл index.html:

```bash
sudo
mv
wordpress/* /var/www/html/
sudo
rm
/var/www/html/index.html
```

Для корректной работы веб-сервера с файлами установите для них нужные права — пользователь и группа www-data:

```bash
sudo
chown
-R
www-data:www-data /var/www/html/
sudo
chmod
-R
755
/var/www/html/
```

Задайте пароль для подключения к базе данных — тот, который вы задавали при создании виртуальной машины.

```bash
sudo
mysql
-u
root
-p
```

Выполните построчно следующие команды.
В <password> укажите пароль для пользователя wp_user.

```bash
CREATE DATABASE wp_database
;
CREATE
USER
'wp_user'
@
'localhost'
IDENTIFIED BY
'<password>'
;
GRANT ALL PRIVILEGES ON wp_database.* TO
'wp_user'
@
'localhost'
;
FLUSH PRIVILEGES
;
EXIT
;
```

Настройте WordPress с помощью шаблона wp-config-sample.php.
Выполните команды копирования и заполнения шаблонного файла.
В <password> укажите пароль для пользователя wp_user, заданный при настройке базы данных.

```bash
sudo
cp
/var/www/html/wp-config-sample.php /var/www/html/wp-config.php
sudo
sed
-i
-e
"s/database_name_here/wp_database/"
/var/www/html/wp-config.php
sudo
sed
-i
-e
"s/username_here/wp_user/g"
/var/www/html/wp-config.php
sudo
sed
-i
-e
"s/password_here/password/g"
/var/www/html/wp-config.php
```

## 3. Настройте доменное имя

На этом шаге вы создадите доменное имя и поучите SSL-сертификат, используя сервис [nip.io](https://nip.io/)nip.io.

Вы также можете использовать собственный домен и SSL-сертификат.

1. Подготовьте доменное имя вида <ip_address>.nip.io, где <ip_address> — публичный IP-адрес виртуальной машины wordpress-server.
2. Установите утилиту для формирования SSL-сертификата и запустите ее:
sudo apt install python3-certbot-apache -ysudo certbot --apache

Во время работы мастера укажите подготовленное доменное имя <ip_address>.nip.io.

Подготовьте доменное имя вида <ip_address>.nip.io, где <ip_address> — публичный IP-адрес виртуальной машины wordpress-server.

Установите утилиту для формирования SSL-сертификата и запустите ее:

```bash
sudo
apt
install
python3-certbot-apache
-y
sudo
certbot
--apache
```

Во время работы мастера укажите подготовленное доменное имя <ip_address>.nip.io.

## 4. Авторизуйтесь в WordPress

1. Откройте браузер и перейдите по адресу <ip_address>.nip.io.
Отобразится страница настройки WordPress.
2. Выберите язык вашего сайта.
3. Введите название сайта, логин администратора wp_user и пароль.
4. Пройдите авторизацию.
Откроется главная страница WordPress.
Последующая настройка производится в веб-интерфейсе WordPress.

Откройте браузер и перейдите по адресу <ip_address>.nip.io.

Отобразится страница настройки WordPress.

Выберите язык вашего сайта.

Введите название сайта, логин администратора wp_user и пароль.

![../_images/img__wordpress__welcome-page.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__wordpress__welcome-page.png)

Пройдите авторизацию.

Откроется главная страница WordPress.
Последующая настройка производится в веб-интерфейсе WordPress.

![../_images/img__wordpress__main-page.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__wordpress__main-page.png)

## Результат

Вы настроили и запустили собственный личный сайт на базе WordPress, а также проверили его работу в браузере.
