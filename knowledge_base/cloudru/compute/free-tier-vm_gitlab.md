---
title: Развертывание Gitlab на виртуальной машине
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab
topic: compute
---
# Развертывание Gitlab на виртуальной машине

С помощью этого руководства вы запустите

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к веб-интерфейсу Gitlab.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к веб-интерфейсу Gitlab.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Разверните инфраструктуру.
2. [Установите и настройте Gitlab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Установите и настройте Gitlab.
3. [Авторизуйтесь в Gitlab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Авторизуйтесь в Gitlab.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Разверните инфраструктуру.

[Установите и настройте Gitlab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Установите и настройте Gitlab.

[Авторизуйтесь в Gitlab](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__gitlab)Авторизуйтесь в Gitlab.

## 1. Разверните инфраструктуру

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.
3. [Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по инструкции.
4. [Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

В поле Название укажите gitlab-vm.
В разделе Образ выберите: Публичные → Ubuntu 24.04.
В поле Название загрузочного диска укажите gitlab-disk.
Включите опцию Подключить публичный IP.
В поле Тип IP-адреса выберите Прямой.
Заполните поле Имя пользователя, например gl-user.
В разделе Метод аутентификации выберите Публичный ключ и Пароль.
Укажите публичный ключ и ваш пароль для создаваемого пользователя.
В поле Имя хоста укажите gitlab-vm.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте SSH-ключ](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте SSH-ключ.

[Загрузите публичную часть SSH-ключа](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution по инструкции.

[Создайте бесплатную виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-free-tier-vm)Создайте бесплатную виртуальную машину со следующими параметрами:

1. В поле Название укажите gitlab-vm.
2. В разделе Образ выберите: Публичные → Ubuntu 24.04.
3. В поле Название загрузочного диска укажите gitlab-disk.
4. Включите опцию Подключить публичный IP.
5. В поле Тип IP-адреса выберите Прямой.
6. Заполните поле Имя пользователя, например gl-user.
7. В разделе Метод аутентификации выберите Публичный ключ и Пароль.
8. Укажите публичный ключ и ваш пароль для создаваемого пользователя.
9. В поле Имя хоста укажите gitlab-vm.

В поле Название укажите gitlab-vm.

В разделе Образ выберите: Публичные → Ubuntu 24.04.

В поле Название загрузочного диска укажите gitlab-disk.

Включите опцию Подключить публичный IP.

В поле Тип IP-адреса выберите Прямой.

Заполните поле Имя пользователя, например gl-user.

В разделе Метод аутентификации выберите Публичный ключ и Пароль.

Укажите публичный ключ и ваш пароль для создаваемого пользователя.

В поле Имя хоста укажите gitlab-vm.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины»:

- отображается виртуальная машина gitlab-vm;
- статус виртуальной машины — Запущена.

отображается виртуальная машина gitlab-vm;

статус виртуальной машины — Запущена.

## 2. Установите и настройте Gitlab

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине gitlab-vm через серийную консоль или по SSH.
2. Обновите ОС и ее пакеты:
sudo apt update -y
3. Установите зависимости:
sudo apt install -y ca-certificates curl openssh-server tzdata perl
4. Скачайте Gitlab из репозитория:
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
5. Установите компонент Gitlab-ce:
sudo EXTERNAL_URL="http://<vm_ip_address>" apt install gitlab-ce

Где vm_ip_address — публичный IP-адрес ВМ.
6. Настройте файрвол:
sudo ufw allow httpsudo ufw allow httpssudo ufw allow OpenSSHsudo ufw enablesudo ufw status

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине gitlab-vm через серийную консоль или по SSH.

Обновите ОС и ее пакеты:

```bash
sudo
apt
update
-y
```

Установите зависимости:

```bash
sudo
apt
install
-y
ca-certificates
curl
openssh-server tzdata perl
```

Скачайте Gitlab из репозитория:

```bash
curl
https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh
|
sudo
bash
```

Установите компонент Gitlab-ce:

```bash
sudo
EXTERNAL_URL
=
"http://<vm_ip_address>"
apt
install
gitlab-ce
```

Где vm_ip_address — публичный IP-адрес ВМ.

Настройте файрвол:

```bash
sudo
ufw allow http
sudo
ufw allow https
sudo
ufw allow OpenSSH
sudo
ufw
enable
sudo
ufw status
```

## 3. Авторизуйтесь в Gitlab

1. В браузере перейдите на страницу \http://<VM_ip-address>.
Откроется окно авторизации:

 
 Если поля для авторизации не появились

В браузере перейдите на страницу \http://<VM_ip-address>.

Откроется окно авторизации:

![../_images/img__gitlab__overview.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/img__gitlab__overview.png)

## Что дальше

В этой лабораторной работе вы настроили и запустили собственный инстанс Gitlab.
