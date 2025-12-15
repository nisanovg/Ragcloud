---
title: Организация хранения файлов через Nextcloud с доступом через веб-интерфейс и мобильное приложение
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud
topic: compute
---
# Организация хранения файлов через Nextcloud с доступом через веб-интерфейс и мобильное приложение

С помощью этого руководства вы развернете решение для работы с личными файлами на основе продукта [Nextcloud](https://nextcloud.com/)Nextcloud.
После развертывания продукта вы сможете работать с файлами через веб-интерфейс или с помощью приложений (Windows, MacOS X, Linux, Android и iOS).

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к веб-интерфейсу хранилища.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- (Опционально) Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к веб-интерфейсу хранилища.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

(Опционально) Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Разверните ресурсы в облаке.
2. [Установите и настройте Nextcloud](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Установите и настройте Nextcloud.
3. [Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Настройте доменное имя.
4. [Загрузите файлы в хранилище через Nextcloud](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Загрузите файлы в хранилище через Nextcloud.
5. [Проверьте отображение файлов в Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Проверьте отображение файлов в Object Storage.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Разверните ресурсы в облаке.

[Установите и настройте Nextcloud](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Установите и настройте Nextcloud.

[Настройте доменное имя](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Настройте доменное имя.

[Загрузите файлы в хранилище через Nextcloud](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Загрузите файлы в хранилище через Nextcloud.

[Проверьте отображение файлов в Object Storage](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)Проверьте отображение файлов в Object Storage.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Получите ключи доступа Key ID и Key Secret](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Получите ключи доступа Key ID и Key Secret.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Получите ключи доступа Key ID и Key Secret](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Получите ключи доступа Key ID и Key Secret.

## 1. Разверните ресурсы в облаке

На этом шаге вы создадите бесплатную виртуальную машину и бакет в хранилище Object Storage.

1. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — nextcloud-server.
Образ — на вкладке Публичные выберите образ с Ubuntu 22.04.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Логин — оставьте значение по умолчанию или укажите новый.
Метод аутентификации — Публичный ключ и Пароль.
Пароль — задайте пароль пользователя.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.
2. Уточните [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности, в которой была создана виртуальная машина.
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием nextcloud-server в той же зоне доступности и добавьте в нее правила:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбой—IP-адрес0.0.0.0/0
4. [Назначьте созданную группу безопасности виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__add-to-sg)Назначьте созданную группу безопасности виртуальной машине.
5. [Создайте бакет в сервисе Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в сервисе Object Storage со следующими параметрами:

Название — название бакета в формате <name>-nextcloud-data, например ivan-nextcloud-data.
Доменное имя — название домена в формате <name>-nextcloud-data, например ivan-nextcloud-data.
Класс хранения по умолчанию — стандартный.
(Опционально) Максимальный размер — включите опцию и укажите максимальный размер бакета.
При выключенной опции размер бакета не будет ограничен.
6. Проверьте создание ресурсов:

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности nextcloud-server со статусом «Создана».
Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина nextcloud-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.
Скопируйте и сохраните публичный IP-адрес, он понадобится далее.
Убедитесь, что в личном кабинете на странице Хранение данных → Object Storage отображается бакет <name>-nextcloud-data.
Скопируйте и сохраните ID тенанта, он понадобится далее.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — nextcloud-server.
- Образ — на вкладке Публичные выберите образ с Ubuntu 22.04.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Логин — оставьте значение по умолчанию или укажите новый.
- Метод аутентификации — Публичный ключ и Пароль.
- Пароль — задайте пароль пользователя.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Название — nextcloud-server.

Образ — на вкладке Публичные выберите образ с Ubuntu 22.04.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Логин — оставьте значение по умолчанию или укажите новый.

Метод аутентификации — Публичный ключ и Пароль.

Пароль — задайте пароль пользователя.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Уточните

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием nextcloud-server в той же зоне доступности и добавьте в нее правила:

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

[Создайте бакет в сервисе Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в сервисе Object Storage со следующими параметрами:

- Название — название бакета в формате <name>-nextcloud-data, например ivan-nextcloud-data.
- Доменное имя — название домена в формате <name>-nextcloud-data, например ivan-nextcloud-data.
- Класс хранения по умолчанию — стандартный.
- (Опционально) Максимальный размер — включите опцию и укажите максимальный размер бакета.
При выключенной опции размер бакета не будет ограничен.

Название — название бакета в формате <name>-nextcloud-data, например ivan-nextcloud-data.

Доменное имя — название домена в формате <name>-nextcloud-data, например ivan-nextcloud-data.

Класс хранения по умолчанию — стандартный.

(Опционально) Максимальный размер — включите опцию и укажите максимальный размер бакета.
При выключенной опции размер бакета не будет ограничен.

Проверьте создание ресурсов:

1. Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности nextcloud-server со статусом «Создана».
2. Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина nextcloud-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.
3. Скопируйте и сохраните публичный IP-адрес, он понадобится далее.
4. Убедитесь, что в личном кабинете на странице Хранение данных → Object Storage отображается бакет <name>-nextcloud-data.
5. Скопируйте и сохраните ID тенанта, он понадобится далее.

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности nextcloud-server со статусом «Создана».

Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина nextcloud-server со статусом «Запущена».
Виртуальной машине назначен публичный IP-адрес.

Скопируйте и сохраните публичный IP-адрес, он понадобится далее.

Убедитесь, что в личном кабинете на странице Хранение данных → Object Storage отображается бакет <name>-nextcloud-data.

Скопируйте и сохраните ID тенанта, он понадобится далее.

## 2. Установите и настройте Nextcloud

На этом шаге вы установите и настроите Nextcloud на виртуальной машине, а также настроите хранение данных в Object Storage.

1. [Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.
2. Обновите систему и установите утилиты:
sudo apt update && sudo apt upgrade -y
3. Установите пакет Nextcloud:
sudo snap install nextcloud
4. Выделите объем памяти для Nextcloud:
sudo snap set nextcloud php.memory-limit=2048M
5. Включите компрессию HTTP:
sudo snap set nextcloud http.compression=true
6. Создайте пользователя — укажите <username> и <password>:
sudo nextcloud.manual-install <username> <password>

Когда установка закончится, в консоли отобразится сообщение «Nextcloud was sucessfully installed».
7. Выполните построчно команды для настройки хранения данных в Object Storage:
sudo nextcloud.occ config:system:set objectstore class --value="\\OC\\Files\\ObjectStore\\S3"
sudo nextcloud.occ config:system:set objectstore arguments bucket --value="<bucket_name>"
sudo nextcloud.occ config:system:set objectstore arguments key --value="<tenant_id>:<key_id>"
sudo nextcloud.occ config:system:set objectstore arguments secret --value="<key_secret>"
sudo nextcloud.occ config:system:set objectstore arguments hostname --value="s3.cloud.ru"
sudo nextcloud.occ config:system:set objectstore arguments port --value="443"
sudo nextcloud.occ config:system:set objectstore arguments use_ssl --value=true
sudo nextcloud.occ config:system:set objectstore arguments region --value="ru-central-1"

Где:

<bucket_name> — название бакета, созданного на предыдущем шаге, в формате <name>-nextcloud-data.
<tenant_id> — идентификатор тенанта в Object Storage.
<key_id>, <key_secret> — ключи доступа.
8. Проверьте корректность настройки:
snap changes nextcloud

В ответе вернется информация об установке Nextcloud и изменении его конфигурации.

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

Установите пакет Nextcloud:

```bash
sudo
snap
install
nextcloud
```

Выделите объем памяти для Nextcloud:

```bash
sudo
snap
set
nextcloud php.memory-limit
=
2048M
```

Включите компрессию HTTP:

```bash
sudo
snap
set
nextcloud
http.compression
=
true
```

Создайте пользователя — укажите <username> и <password>:

```bash
sudo
nextcloud.manual-install
<
username
>
<
password
>
```

Когда установка закончится, в консоли отобразится сообщение «Nextcloud was sucessfully installed».

Выполните построчно команды для настройки хранения данных в Object Storage:

```bash
sudo
nextcloud.occ config:system:set objectstore class
--value
=
"
\\
OC
\\
Files
\\
ObjectStore
\\
S3"
sudo
nextcloud.occ config:system:set objectstore arguments bucket
--value
=
"<bucket_name>"
sudo
nextcloud.occ config:system:set objectstore arguments key
--value
=
"<tenant_id>:<key_id>"
sudo
nextcloud.occ config:system:set objectstore arguments secret
--value
=
"<key_secret>"
sudo
nextcloud.occ config:system:set objectstore arguments
hostname
--value
=
"s3.cloud.ru"
sudo
nextcloud.occ config:system:set objectstore arguments port
--value
=
"443"
sudo
nextcloud.occ config:system:set objectstore arguments use_ssl
--value
=
true
sudo
nextcloud.occ config:system:set objectstore arguments region
--value
=
"ru-central-1"
```

Где:

- <bucket_name> — название бакета, созданного на предыдущем шаге, в формате <name>-nextcloud-data.
- <tenant_id> — идентификатор тенанта в Object Storage.
- <key_id>, <key_secret> — ключи доступа.

<bucket_name> — название бакета, созданного на предыдущем шаге, в формате <name>-nextcloud-data.

<tenant_id> — идентификатор тенанта в Object Storage.

<key_id>, <key_secret> — ключи доступа.

Проверьте корректность настройки:

```bash
snap changes nextcloud
```

В ответе вернется информация об установке Nextcloud и изменении его конфигурации.

## 3. Настройте доменное имя

На этом шаге вы создадите доменное имя и поучите SSL-сертификат, используя сервис [nip.io](https://nip.io/)nip.io.

Вы также можете использовать собственный домен и SSL-сертификат.

1. Подготовьте доменное имя вида <ip_address>.nip.io, где <ip_address> — публичный IP-адрес виртуальной машины nextcloud-server.
2. Настройте доверенное доменное имя:
sudo nextcloud.occ config:system:set trusted_domains 1 --value=<ip_address>.nip.io
3. Настройте SSL-сертификат:

Выполните команду:
sudo nextcloud.enable-https lets-encrypt

Нажмите y в ответ на вопрос «Have you met these requirements?».
Укажите свой email.
Укажите домен <ip_address>.nip.io, подготовленный ранее.

Подготовьте доменное имя вида <ip_address>.nip.io, где <ip_address> — публичный IP-адрес виртуальной машины nextcloud-server.

Настройте доверенное доменное имя:

```bash
sudo
nextcloud.occ config:system:set trusted_domains
1
--value
=
<
ip_address
>
.nip.io
```

Настройте SSL-сертификат:

1. Выполните команду:
sudo nextcloud.enable-https lets-encrypt
2. Нажмите y в ответ на вопрос «Have you met these requirements?».
3. Укажите свой email.
4. Укажите домен <ip_address>.nip.io, подготовленный ранее.

Выполните команду:

```bash
sudo
nextcloud.enable-https lets-encrypt
```

Нажмите y в ответ на вопрос «Have you met these requirements?».

Укажите свой email.

Укажите домен <ip_address>.nip.io, подготовленный ранее.

## 4. Загрузите файлы в хранилище через Nextcloud

Для проверки работы системы загрузите файл через браузер:

1. Откройте браузер и перейдите по адресу <ip_address>.nip.io.
Откроется страница авторизации Nextcloud.
2. Авторизуйтесь в Nextcloud, используя username и password, которые вы задавали [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)на шаге 2.
3. Перейдите в раздел Все файлы и загрузите любой файл.
4. Убедитесь, что файл появился в Nextcloud.

Откройте браузер и перейдите по адресу <ip_address>.nip.io.

Откроется страница авторизации Nextcloud.

![../_images/img__nextcloud__auth.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__nextcloud__auth.png)

Авторизуйтесь в Nextcloud, используя username и password, которые вы задавали [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)на шаге 2.

Перейдите в раздел Все файлы и загрузите любой файл.

Убедитесь, что файл появился в Nextcloud.

Для работы с Nextcloud через мобильное устройство:

1. Скачайте приложение Nextcloud.
2. Нажмите Войти и укажите в адрес сервера <ip_address>.nip.io.
В приложении отобразится загруженный через веб-интерфейс файл.

Скачайте приложение Nextcloud.

Нажмите Войти и укажите в адрес сервера <ip_address>.nip.io.

В приложении отобразится загруженный через веб-интерфейс файл.

## 5. Проверьте отображение файлов в Object Storage

Проверьте, что в качестве хранилища для файлов используется Object Storage.

1. [В личном кабинете](https://console.cloud.ru/)В личном кабинете на верхней панели слева нажмите и выберите Хранение данных → Object Storage.
2. Выберите бакет, созданный [на шаге 1](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)на шаге 1.

[В личном кабинете](https://console.cloud.ru/)В личном кабинете на верхней панели слева нажмите и выберите Хранение данных → Object Storage.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Выберите бакет, созданный [на шаге 1](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__nextcloud)на шаге 1.

В бакете отображаются служебные и загруженные файлы.
Реальные имена файлов при этом заменены на служебные.

## Результат

Вы настроили и запустили собственный сервер для работы и обмена файлами на базе Nextcloud, а также проверили его работу в браузере и на мобильном устройстве.

Теперь вы можете загружать и работать с файлами через браузер и мобильные приложения.
