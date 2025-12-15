---
title: Развертывание сайта с использованием LEMP
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp
topic: compute
---
# Развертывание сайта с использованием LEMP

С помощью этого руководства вы создадите простой сайт с использованием стека LEMP.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, на которой будет развернут веб-сервер Nginx и СУБД MySQL.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, на которой будет развернут веб-сервер Nginx и СУБД MySQL.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Разверните ресурсы в облаке.
2. [Настройте Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте Nginx.
3. [Настройте базу данных MySQL](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте базу данных MySQL.
4. [Настройте сайт](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте сайт.
5. [Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте доменное имя.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Разверните ресурсы в облаке.

[Настройте Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте Nginx.

[Настройте базу данных MySQL](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте базу данных MySQL.

[Настройте сайт](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте сайт.

[Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-on-lemp)Настройте доменное имя.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что вам назначена [сервисная роль](https://cloud.ru/docs/virtual-machines/ug/topics/security)сервисная роль eiv.admin или роль администратора проекта.
При необходимости [настройте права](https://cloud.ru/docs/administration/ug/topics/guides__employees)настройте права или запросите их у администратора.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что вам назначена [сервисная роль](https://cloud.ru/docs/virtual-machines/ug/topics/security)сервисная роль eiv.admin или роль администратора проекта.
При необходимости [настройте права](https://cloud.ru/docs/administration/ug/topics/guides__employees)настройте права или запросите их у администратора.

## 1. Разверните ресурсы в облаке

На этом шаге вы подготовите группу безопасности и виртуальную машину.

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием sg-lemp в зоне доступности ru.AZ-1 и добавьте в нее правила:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0
2. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — lemp-server.
Зона доступности — ru.AZ-1.
Образ — на вкладке Маркетплейс выберите образ LEMP.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте sg-lemp.
Имя пользователя — cloud-user.
Метод аутентификации — Пароль
Пароль — задайте пароль пользователя.
3. В строке созданной ВМ скопируйте и сохраните адрес из столбца Публичный IP: он потребуется для дальнейшей настройки.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием sg-lemp в зоне доступности ru.AZ-1 и добавьте в нее правила:

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

Исходящий

Любой

Оставьте пустым

IP-адрес

0.0.0.0/0

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — lemp-server.
- Зона доступности — ru.AZ-1.
- Образ — на вкладке Маркетплейс выберите образ LEMP.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте sg-lemp.
- Имя пользователя — cloud-user.
- Метод аутентификации — Пароль
- Пароль — задайте пароль пользователя.

Название — lemp-server.

Зона доступности — ru.AZ-1.

Образ — на вкладке Маркетплейс выберите образ LEMP.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте sg-lemp.

Имя пользователя — cloud-user.

Метод аутентификации — Пароль

Пароль — задайте пароль пользователя.

В строке созданной ВМ скопируйте и сохраните адрес из столбца Публичный IP: он потребуется для дальнейшей настройки.

## 2. Настройте Nginx

Сервер Nginx обрабатывает запросы пользователей к сайту.

1. Выберите виртуальную машину lemp-server в списке.
2. Перейдите на вкладку Серийная консоль.
3. Введите логин и пароль, указанные при создании виртуальной машины.
4. Обновите пакеты ОС.
В серийной консоли выполните команды:
sudo apt updatesudo apt upgrade
5. Для обработки скриптов установите менеджер процессов PHP-FPM:
sudo apt install php8.1-fpm
6. Создайте новый конфигурационный файл:
sudo nano /etc/nginx/sites-available/mysite
7. Добавьте в файл конфигурацию виртуального сервера, заменив <public_ip> на публичный IP-адрес виртуальной машины lemp-server:
 server { listen 80; server_name <public_ip>.nip.io;
 root /var/www/html/mysite; index index.php index.html index.htm;
 location / { try_files $uri $uri/ =404; }
 location ~ \.php$ { include snippets/fastcgi-php.conf; fastcgi_pass unix:/var/run/php/php8.1-fpm.sock; }
 location ~ /\.ht { deny all; }}
8. Добавьте ссылку на конфигурационный файл в каталоге sites-enabled:
sudo ln -s /etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/
9. Проверьте, что в конфигурации Nginx нет ошибок:
sudo nginx -t
10. Чтобы применить настройки, перезапустите Nginx:
sudo systemctl restart nginx

Выберите виртуальную машину lemp-server в списке.

Перейдите на вкладку Серийная консоль.

Введите логин и пароль, указанные при создании виртуальной машины.

Обновите пакеты ОС.
В серийной консоли выполните команды:

```bash
sudo
apt
update
sudo
apt
upgrade
```

Для обработки скриптов установите менеджер процессов PHP-FPM:

```bash
sudo
apt
install
php8.1-fpm
```

Создайте новый конфигурационный файл:

```bash
sudo
nano
/etc/nginx/sites-available/mysite
```

Добавьте в файл конфигурацию виртуального сервера, заменив <public_ip> на публичный IP-адрес виртуальной машины lemp-server:

```bash
server
{
listen
80
;
server_name
<
public_ip
>
.nip.io
;
root /var/www/html/mysite
;
index index.php index.html index.htm
;
location /
{
try_files
$uri
$uri
/
=
404
;
}
location ~
\
.php$
{
include snippets/fastcgi-php.conf
;
fastcgi_pass unix:/var/run/php/php8.1-fpm.sock
;
}
location ~ /
\
.ht
{
deny all
;
}
}
```

Добавьте ссылку на конфигурационный файл в каталоге sites-enabled:

```bash
sudo
ln
-s
/etc/nginx/sites-available/mysite /etc/nginx/sites-enabled/
```

Проверьте, что в конфигурации Nginx нет ошибок:

```bash
sudo
nginx
-t
```

Чтобы применить настройки, перезапустите Nginx:

```bash
sudo
systemctl restart nginx
```

## 3. Настройте базу данных MySQL

В базе данных будут храниться записи, которые добавляются через форму на сайте.

1. Подключитесь к MySQL:
sudo mysql -u root -p
2. Создайте новую базу данных.
Выполните построчно следующие команды:
CREATE DATABASE mydatabase;USE mydatabase;CREATE TABLE entries ( id INT AUTO_INCREMENT PRIMARY KEY, content TEXT NOT NULL);
3. Создайте пользователя db_user:
CREATE USER 'db_user'@'localhost' IDENTIFIED BY '<user_password>';GRANT ALL PRIVILEGES ON mydatabase.* TO 'db_user'@'localhost';FLUSH PRIVILEGES;EXIT;

Где <user_password> — пароль пользователя.

Подключитесь к MySQL:

```bash
sudo
mysql
-u
root
-p
```

Создайте новую базу данных.
Выполните построчно следующие команды:

```bash
CREATE DATABASE mydatabase
;
USE mydatabase
;
CREATE TABLE entries
(
id
INT AUTO_INCREMENT PRIMARY KEY,
content TEXT NOT NULL
)
;
```

Создайте пользователя db_user:

```bash
CREATE
USER
'db_user'
@
'localhost'
IDENTIFIED BY
'<user_password>'
;
GRANT ALL PRIVILEGES ON mydatabase.* TO
'db_user'
@
'localhost'
;
FLUSH PRIVILEGES
;
EXIT
;
```

Где <user_password> — пароль пользователя.

## 4. Настройте сайт

Сайт состоит из одной страницы с простой формой для добавления записей.

1. Создайте корневой каталог сайта:
sudo mkdir -p /var/www/html/mysite
2. Установите права доступа:
sudo chown -R $USER:$USER /var/www/html/mysitesudo chmod -R 755 /var/www/html/mysite
3. Создайте стартовую страницу сайта:
sudo nano /var/www/html/mysite/index.php
4. Вставьте на страницу код, заменив <user_password> на пароль пользователя базы данных, созданного на предыдущем шаге:
<?php$conn = new mysqli("localhost", "db_user", "<user_password>", "mydatabase");
if ($conn->connect_error) { die("Connection failed: " . $conn->connect_error);}
if ($_SERVER["REQUEST_METHOD"] == "POST") { $content = $_POST["content"]; $stmt = $conn->prepare("INSERT INTO entries (content) VALUES (?)"); $stmt->bind_param("s", $content); $stmt->execute(); $stmt->close();}
$result = $conn->query("SELECT * FROM entries");?>
<!DOCTYPE html><html><head> <title>Simple LEMP Site</title></head><body> <h1>Add a New Record</h1> <form method="post"> <textarea name="content" rows="4" cols="50"></textarea><br> <input type="submit" value="Submit"> </form>
 <h2>Entries</h2> <ul> <?php while ($row = $result->fetch_assoc()): ?> <li><?php echo htmlspecialchars($row['content']); ?></li> <?php endwhile; ?> </ul></body></html>
<?php$conn->close();?>

Создайте корневой каталог сайта:

```bash
sudo
mkdir
-p
/var/www/html/mysite
```

Установите права доступа:

```bash
sudo
chown
-R
$USER
:
$USER
/var/www/html/mysite
sudo
chmod
-R
755
/var/www/html/mysite
```

Создайте стартовую страницу сайта:

```bash
sudo
nano
/var/www/html/mysite/index.php
```

Вставьте на страницу код, заменив <user_password> на пароль пользователя базы данных, созданного на предыдущем шаге:

```bash
<
?php
$conn
=
new mysqli
(
"localhost"
,
"db_user"
,
"<user_password>"
,
"mydatabase"
)
;
if
(
$conn
-
>
connect_error
)
{
die
(
"Connection failed: "
.
$conn
-
>
connect_error
)
;
}
if
(
$_SERVER
[
"REQUEST_METHOD"
]
==
"POST"
)
{
$content
=
$_POST
[
"content"
]
;
$stmt
=
$conn
-
>
prepare
(
"INSERT INTO entries (content) VALUES (?)"
)
;
$stmt
-
>
bind_param
(
"s"
,
$content
)
;
$stmt
-
>
execute
(
)
;
$stmt
-
>
close
(
)
;
}
$result
=
$conn
-
>
query
(
"SELECT * FROM entries"
)
;
?
>
<
!
DOCTYPE html
>
<
html
>
<
head
>
<
title
>
Simple LEMP Site
<
/title
>
<
/head
>
<
body
>
<
h
1
>
Add a New Record
<
/h
1
>
<
form
method
=
"post"
>
<
textarea
name
=
"content"
rows
=
"4"
cols
=
"50"
>
<
/textarea
>
<
br
>
<
input
type
=
"submit"
value
=
"Submit"
>
<
/form
>
<
h
2
>
Entries
<
/h
2
>
<
ul
>
<
?php
while
(
$row
=
$result
-
>
fetch_assoc
(
))
: ?
>
<
li
>
<
?php
echo
htmlspecialchars
(
$row
[
'content'
]
)
;
?
>
<
/li
>
<
?php endwhile
;
?
>
<
/ul
>
<
/body
>
<
/html
>
<
?php
$conn
-
>
close
(
)
;
?
>
```

## 5. Настройте доменное имя

Для создания доменного имени и SSL-сертификата используется сервис [nip.io](https://nip.io/)nip.io.
Также вы можете использовать собственный домен и SSL-сертификат.

1. Подготовьте доменное имя вида <public_ip>.nip.io, где <public_ip> — публичный IP-адрес виртуальной машины lemp-server.
2. Установите утилиту для формирования SSL-сертификата и запустите ее:
sudo apt install certbot python3-certbot-nginxsudo certbot --nginx -d <public_ip>.nip.io --register-unsafely-without-email
3. Откройте браузер и перейдите по адресу <public_ip>.nip.io.

Подготовьте доменное имя вида <public_ip>.nip.io, где <public_ip> — публичный IP-адрес виртуальной машины lemp-server.

Установите утилиту для формирования SSL-сертификата и запустите ее:

```bash
sudo
apt
install
certbot python3-certbot-nginx
sudo
certbot
--nginx
-d
<
public_ip
>
.nip.io --register-unsafely-without-email
```

Откройте браузер и перейдите по адресу <public_ip>.nip.io.

При переходе по адресу вашего сайта откроется форма для добавления записей.
Добавленные записи отображаются в списке под формой.

## Результат

Вы развернули сайт с использованием стека LEMP и обеспечили безопасный доступ к нему через Nginx.
