---
title: Развертывание сервиса статического мониторинга кода и безопасности SonarQube
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube
topic: compute
---
# Развертывание сервиса статического мониторинга кода и безопасности SonarQube

С помощью этого руководства вы развернете платформу статического анализа кода SonarQube в облаке Cloud.ru для автоматической проверки качества и безопасности кода.

Вы создадите инфраструктуру, подключите SonarQube к управляемой базе данных Managed PostgreSQL®, опубликуете сервис через Nginx с автоматическим выпуском сертификатов Let’s Encrypt и обеспечите безопасный доступ по HTTPS.
Также вы подключите репозиторий из GitVerse и настроите пайплайн CI/CD, запускающий анализ кода в SonarQube при каждом commit и pull request.
Дополнительно вы интегрируете SonarQube с IDE VS Code для локального статического анализа кода во время разработки.

В результате вы получите готовый сервис анализа качества кода, изолированный в собственной VPC, доступный из интернета и встроенный в рабочий процесс разработки.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- [Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
- [GitVerse](https://gitverse.ru/home)GitVerse — платформа для совместной работы с исходным кодом.
- (Опционально) [SonarQube for IDE](https://marketplace.visualstudio.com/items)SonarQube for IDE — расширение для подключения SonarQube к редактору Visual Studio Code.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для размещения приложения.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

[Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[GitVerse](https://gitverse.ru/home)GitVerse — платформа для совместной работы с исходным кодом.

(Опционально) [SonarQube for IDE](https://marketplace.visualstudio.com/items)SonarQube for IDE — расширение для подключения SonarQube к редактору Visual Studio Code.

Шаги:

1. [Определите необходимую инфраструктуру для вашего проекта](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Определите необходимую инфраструктуру для вашего проекта.
2. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Разверните ресурсы в облаке.
3. [Настройте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Настройте окружение виртуальной машины.
4. [Настройте защищенный доступ через Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Настройте защищенный доступ через Nginx.
5. [Разверните и запустите SonarQube](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Разверните и запустите SonarQube.
6. [Отключите SSH-доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Отключите SSH-доступ.
7. [Подключите SonarQube к репозиторию в GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Подключите SonarQube к репозиторию в GitVerse.
8. (Опционально) [Подключите SonarQube к Visual Studio Code](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Подключите SonarQube к Visual Studio Code.

[Определите необходимую инфраструктуру для вашего проекта](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Определите необходимую инфраструктуру для вашего проекта.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Разверните ресурсы в облаке.

[Настройте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Настройте окружение виртуальной машины.

[Настройте защищенный доступ через Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Настройте защищенный доступ через Nginx.

[Разверните и запустите SonarQube](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Разверните и запустите SonarQube.

[Отключите SSH-доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Отключите SSH-доступ.

[Подключите SonarQube к репозиторию в GitVerse](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Подключите SonarQube к репозиторию в GitVerse.

(Опционально) [Подключите SonarQube к Visual Studio Code](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__postgresql-sonarqube)Подключите SonarQube к Visual Studio Code.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.
3. Создайте учетную запись в [GitVerse](https://gitverse.ru/)GitVerse, если не сделали этого ранее.
Примеры кода в практическом руководстве размещаются в GitVerse.
4. (Опционально) Скачайте и установите [Visual Studio Code](https://code.visualstudio.com/download)Visual Studio Code для выполнения шага 8.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

Создайте учетную запись в [GitVerse](https://gitverse.ru/)GitVerse, если не сделали этого ранее.
Примеры кода в практическом руководстве размещаются в GitVerse.

(Опционально) Скачайте и установите [Visual Studio Code](https://code.visualstudio.com/download)Visual Studio Code для выполнения шага 8.

## 1. Определите необходимую инфраструктуру для вашего проекта

Определите необходимые конфигурации виртуальной машины и кластера Managed PostgreSQL®, исходя из минимально рекомендованных значений.

Размер команды

Виртуальная машина

Кластер Managed PostgreSQL®

Небольшая команда разработки или тестовая среда:

- 1–10 разработчиков;
- 1–20 проектов;
- кодовая база до 1 млн строк.

1–10 разработчиков;

1–20 проектов;

кодовая база до 1 млн строк.

- CPU: 2 vCPU
- RAM: 4 ГБ
- SSD: 30–50 ГБ

CPU: 2 vCPU

RAM: 4 ГБ

SSD: 30–50 ГБ

- Режим: Стандарт
- Тип: Single
- CPU: 2 vCPU
- RAM: 4 ГБ
- SSD: 50–100 ГБ

Режим: Стандарт

Тип: Single

CPU: 2 vCPU

RAM: 4 ГБ

SSD: 50–100 ГБ

Средняя команда или промышленная среда:

- 10–50 разработчиков;
- 20–100 проектов;
- кодовая база — 1–10 млн строк.

10–50 разработчиков;

20–100 проектов;

кодовая база — 1–10 млн строк.

- CPU: 4 vCPU
- RAM: 8 ГБ
- SSD: 100–200 ГБ

CPU: 4 vCPU

RAM: 8 ГБ

SSD: 100–200 ГБ

- Режим: Бизнес
- Тип: Single
- CPU: 4 vCPU
- RAM: 8 ГБ
- SSD: 100–500 ГБ

Режим: Бизнес

Тип: Single

CPU: 4 vCPU

RAM: 8 ГБ

SSD: 100–500 ГБ

Большая команда — корпоративное решение:

- 50–200 разработчиков;
- 100–500 проектов;
- кодовая база — 10–50 млн строк.

50–200 разработчиков;

100–500 проектов;

кодовая база — 10–50 млн строк.

- CPU: 8 vCPU
- RAM: 16 ГБ
- SSD: 200–500 ГБ

CPU: 8 vCPU

RAM: 16 ГБ

SSD: 200–500 ГБ

- Режим: Бизнес
- Тип: Master/Replica
- CPU: 8 vCPU
- RAM: 16 ГБ
- SSD: 500–1 000 ГБ

Режим: Бизнес

Тип: Master/Replica

CPU: 8 vCPU

RAM: 16 ГБ

SSD: 500–1 000 ГБ

## 2. Разверните ресурсы в облаке

На этом шаге вы подготовите сеть, группу безопасности, виртуальную машину и кластер Managed PostgreSQL®.
Все ресурсы будут расположены в одной VPC, что обеспечит сетевую изоляцию.

1. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием sonarqube-VPC.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

Название — sonarqube-subnet.
VPC — sonarqube-VPC.
Адрес — 10.10.1.0/24.
DNS-серверы — 8.8.8.8.
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием sonarqube и добавьте в нее правила:
 ТрафикПротоколПортТип источника/адресатаИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — sonarqube.
Образ — публичный образ Ubuntu 22.04.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
VPC — sonarqube-VPC.
Подсеть — sonarqube-subnet.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте sonarqube.
Логин — sonarqube.
Метод аутентификации — Публичный ключ и Пароль.
Публичный ключ — укажите ключ, созданный ранее.
Пароль — задайте пароль пользователя.
Имя хоста — sonarqube.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.
5. [Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL со следующими параметрами:

Имя кластера — sonarqube.
Название базы данных — sonarqube_db.
Версия PostgreSQL — 16.
Подсеть — sonarqube-subnet.
Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием sonarqube-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название — sonarqube-subnet.
- VPC — sonarqube-VPC.
- Адрес — 10.10.1.0/24.
- DNS-серверы — 8.8.8.8.

Название — sonarqube-subnet.

VPC — sonarqube-VPC.

Адрес — 10.10.1.0/24.

DNS-серверы — 8.8.8.8.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием sonarqube и добавьте в нее правила:

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

Оставьте пустым

IP-адрес

0.0.0.0/0

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — sonarqube.
- Образ — публичный образ Ubuntu 22.04.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- VPC — sonarqube-VPC.
- Подсеть — sonarqube-subnet.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте sonarqube.
- Логин — sonarqube.
- Метод аутентификации — Публичный ключ и Пароль.
- Публичный ключ — укажите ключ, созданный ранее.
- Пароль — задайте пароль пользователя.
- Имя хоста — sonarqube.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Название — sonarqube.

Образ — публичный образ Ubuntu 22.04.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

VPC — sonarqube-VPC.

Подсеть — sonarqube-subnet.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте sonarqube.

Логин — sonarqube.

Метод аутентификации — Публичный ключ и Пароль.

Публичный ключ — укажите ключ, созданный ранее.

Пароль — задайте пароль пользователя.

Имя хоста — sonarqube.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

[Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__cluster-creation)Создайте кластер Managed PostgreSQL со следующими параметрами:

- Имя кластера — sonarqube.
- Название базы данных — sonarqube_db.
- Версия PostgreSQL — 16.
- Подсеть — sonarqube-subnet.
- Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Имя кластера — sonarqube.

Название базы данных — sonarqube_db.

Версия PostgreSQL — 16.

Подсеть — sonarqube-subnet.

Остальные параметры оставьте по умолчанию или выберите на свое усмотрение.

Убедитесь, что ресурсы созданы и отображаются в личном кабинете:

1. На странице Сети → VPC отображается сеть sonarqube-VPC, а в списке ее подсетей — sonarqube-subnet.
2. На странице Сети → Группы безопасности отображается группа безопасности sonarqube со статусом «Создана».
3. На странице Инфраструктура → Виртуальные машины отображается виртуальная машина sonarqube со статусом «Запущена».
4. На странице Базы данных → Managed PostgreSQL® отображается кластер sonarqube со статусом «Доступен».

На странице Сети → VPC отображается сеть sonarqube-VPC, а в списке ее подсетей — sonarqube-subnet.

На странице Сети → Группы безопасности отображается группа безопасности sonarqube со статусом «Создана».

На странице Инфраструктура → Виртуальные машины отображается виртуальная машина sonarqube со статусом «Запущена».

На странице Базы данных → Managed PostgreSQL® отображается кластер sonarqube со статусом «Доступен».

## 3. Настройте окружение виртуальной машины

На этом шаге вы установите необходимые пакеты и подготовите среду для SonarQube.

1. [Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.
2. Обновите систему и установите утилиты:
sudo apt update && sudo apt upgrade -y
3. Установите и запустите Nginx:
sudo apt install nginx -ysudo systemctl enable nginxsudo systemctl start nginx
4. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y
5. Установите Docker и Docker Compose:
curl -fsSL https://get.docker.com -o get-docker.shsudo sh get-docker.shsudo apt install docker compose -y
6. Добавьте текущего пользователя виртуальной машины в группу Docker:

Выполните команду:
sudo usermod -aG docker $USERnewgrp docker

Перезагрузите систему.
Проверьте работоспособность Docker:
docker run hello-world

Появится сообщение, подтверждающее успешность установки и настройки.

ПримечаниеВ некоторых случаях права на использование Docker без префикса sudo не сохраняются и командная строка возвращает ошибку permission denied.
В этом случае вы можете продолжить работу с Docker, добавляя в начало каждой команды префикс sudo.
7. Настройте системные параметры для SonarQube.
Для стабильной работы SonarQube требуются повышенные значения параметров ядра vm.max_map_count, fs.file-max и пользовательских лимитов на количество открытых файлов (open files) и потоков (threads).
В противном случае компонент Elasticsearch, используемый в SonarQube, не сможет создать необходимое количество отображений памяти (memory mappings) и файловых дескрипторов, что приведет к ошибкам при запуске и аварийному завершению анализа.
Настройка этих параметров с помощью sysctl и limits.conf обеспечивает их сохранение на уровне ядра и пользовательских лимитов.
Это гарантирует, что при каждой загрузке операционной системы SonarQube будет автоматически получать требуемые ресурсы.

Настройте параметры ядра:
sudo sysctl -w vm.max_map_count=262144sudo sysctl -w fs.file-max=65536

Задайте постоянное применение этих параметров:
echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.confecho 'fs.file-max=65536' | sudo tee -a /etc/sysctl.conf

Укажите лимиты:
echo 'sonarqube - nofile 65536' | sudo tee -a /etc/security/limits.confecho 'sonarqube - nproc 4096' | sudo tee -a /etc/security/limits.conf
ulimit -n 65536ulimit -u 4096

[Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH.

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

Установите и запустите Nginx:

```bash
sudo
apt
install
nginx
-y
sudo
systemctl
enable
nginx
sudo
systemctl start nginx
```

Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

Установите Docker и Docker Compose:

```bash
curl
-fsSL
https://get.docker.com
-o
get-docker.sh
sudo
sh
get-docker.sh
sudo
apt
install
docker
compose
-y
```

Добавьте текущего пользователя виртуальной машины в группу Docker:

1. Выполните команду:
sudo usermod -aG docker $USERnewgrp docker
2. Перезагрузите систему.
3. Проверьте работоспособность Docker:
docker run hello-world

Появится сообщение, подтверждающее успешность установки и настройки.

Выполните команду:

```bash
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

Перезагрузите систему.

Проверьте работоспособность Docker:

```bash
docker
run hello-world
```

Появится сообщение, подтверждающее успешность установки и настройки.

В некоторых случаях права на использование Docker без префикса sudo не сохраняются и командная строка возвращает ошибку permission denied.
В этом случае вы можете продолжить работу с Docker, добавляя в начало каждой команды префикс sudo.

Настройте системные параметры для SonarQube.

Для стабильной работы SonarQube требуются повышенные значения параметров ядра vm.max_map_count, fs.file-max и пользовательских лимитов на количество открытых файлов (open files) и потоков (threads).
В противном случае компонент Elasticsearch, используемый в SonarQube, не сможет создать необходимое количество отображений памяти (memory mappings) и файловых дескрипторов, что приведет к ошибкам при запуске и аварийному завершению анализа.

Настройка этих параметров с помощью sysctl и limits.conf обеспечивает их сохранение на уровне ядра и пользовательских лимитов.
Это гарантирует, что при каждой загрузке операционной системы SonarQube будет автоматически получать требуемые ресурсы.

1. Настройте параметры ядра:
sudo sysctl -w vm.max_map_count=262144sudo sysctl -w fs.file-max=65536
2. Задайте постоянное применение этих параметров:
echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.confecho 'fs.file-max=65536' | sudo tee -a /etc/sysctl.conf
3. Укажите лимиты:
echo 'sonarqube - nofile 65536' | sudo tee -a /etc/security/limits.confecho 'sonarqube - nproc 4096' | sudo tee -a /etc/security/limits.conf
ulimit -n 65536ulimit -u 4096

Настройте параметры ядра:

```bash
sudo
sysctl
-w
vm.max_map_count
=
262144
sudo
sysctl
-w
fs.file-max
=
65536
```

Задайте постоянное применение этих параметров:

```bash
echo
'vm.max_map_count=262144'
|
sudo
tee
-a
/etc/sysctl.conf
echo
'fs.file-max=65536'
|
sudo
tee
-a
/etc/sysctl.conf
```

Укажите лимиты:

```bash
echo
'sonarqube - nofile 65536'
|
sudo
tee
-a
/etc/security/limits.conf
echo
'sonarqube - nproc 4096'
|
sudo
tee
-a
/etc/security/limits.conf
ulimit
-n
65536
ulimit
-u
4096
```

## 4. Настройте защищенный доступ через Nginx

На этом шаге вы зарегистрируете доменное имя, настроите Nginx в качестве защищенного прокси, получите SSL-сертификат и ограничите доступ через межсетевой экран.

1. Создайте конфигурационный файл Nginx:
sudo nano /etc/nginx/sites-available/sonarqube.conf
2. Вставьте код, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:
server { listen 80; server_name sonar.<ip_address>.nip.io www.sonar.<ip_address>.nip.io;
location / { proxy_pass http://127.0.0.1:9000; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-Proto $scheme;}}
3. Сконфигурируйте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
4. Активируйте конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/sonarqube.conf /etc/nginx/sites-enabled/sonarqube.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
5. Выпустите SSL-сертификат:
sudo certbot --nginx -d sonar.<ip_address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip_address> — публичный IP-адрес виртуальной машины.
<email> — email для регистрации сертификата.
6. Перейдите по адресу https://sonar.<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

Создайте конфигурационный файл Nginx:

```bash
sudo
nano
/etc/nginx/sites-available/sonarqube.conf
```

Вставьте код, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:

```bash
server
{
listen
80
;
server_name sonar.
<
ip_address
>
.nip.io www.sonar.
<
ip_address
>
.nip.io
;
location /
{
proxy_pass http://127.0.0.1:9000
;
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-Proto
$scheme
;
}
}
```

Сконфигурируйте межсетевой экран:

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

Активируйте конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/sonarqube.conf /etc/nginx/sites-enabled/sonarqube.conf
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

Выпустите SSL-сертификат:

```bash
sudo
certbot
--nginx
-d
sonar.
<
ip_address
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

- <ip_address> — публичный IP-адрес виртуальной машины.
- <email> — email для регистрации сертификата.

<ip_address> — публичный IP-адрес виртуальной машины.

<email> — email для регистрации сертификата.

Перейдите по адресу https://sonar.<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

## 5. Установите и запустите SonarQube

На этом шаге вы установите SonarQube, настроите подключение к базе данных и запустите сервис через Docker Compose.

1. Создайте директорию проекта и перейдите в нее:
mkdir sonarqube-deploymentcd sonarqube-deployment
2. Создайте файл docker-compose.yml:
nano docker-compose.yml
3. Добавьте следующую конфигурацию:
services: sonarqube: image: sonarqube:25.8.0.112029-community container_name: sonarqube restart: unless-stopped ports: - "9000:9000" environment: - SONAR_JDBC_URL=jdbc:postgresql://<postgres_ip>:5432/sonarqube_db - SONAR_JDBC_USERNAME=<postgres_admin_user> - SONAR_JDBC_PASSWORD=<postgres_admin_password> - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true volumes: - sonarqube_data:/opt/sonarqube/data - sonarqube_extensions:/opt/sonarqube/extensions - sonarqube_logs:/opt/sonarqube/logs ulimits: nproc: 131072 nofile: soft: 8192 hard: 131072
volumes: sonarqube_data: sonarqube_extensions: sonarqube_logs:

Где:

<postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.
<postgres_admin_password> — пароль указанного пользователя.
<postgres_ip> — приватный IP-адрес кластера.
4. Запустите контейнеры:
docker compose up -d
5. Проверьте статус контейнеров:
docker compose psdocker compose logs -f sonarqube
6. Перейдите по адресу https://sonar.<ip_address>.nip.io и войдите в панель администратора, используя временные логин и пароль admin.
7. Смените пароль администратора.

Создайте директорию проекта и перейдите в нее:

```bash
mkdir
sonarqube-deployment
cd
sonarqube-deployment
```

Создайте файл docker-compose.yml:

```bash
nano
docker-compose.yml
```

Добавьте следующую конфигурацию:

```bash
services
:
sonarqube
:
image
:
sonarqube
:
25.8.0.112029
-
community
container_name
:
sonarqube
restart
:
unless
-
stopped
ports
:
-
"9000:9000"
environment
:
-
SONAR_JDBC_URL=jdbc
:
postgresql
:
//<postgres_ip
>
:
5432/sonarqube_db
-
SONAR_JDBC_USERNAME=<postgres_admin_user
>
-
SONAR_JDBC_PASSWORD=<postgres_admin_password
>
-
SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true
volumes
:
-
sonarqube_data
:
/opt/sonarqube/data
-
sonarqube_extensions
:
/opt/sonarqube/extensions
-
sonarqube_logs
:
/opt/sonarqube/logs
ulimits
:
nproc
:
131072
nofile
:
soft
:
8192
hard
:
131072
volumes
:
sonarqube_data
:
sonarqube_extensions
:
sonarqube_logs
:
```

Где:

- <postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.
- <postgres_admin_password> — пароль указанного пользователя.
- <postgres_ip> — приватный IP-адрес кластера.

<postgres_admin_user> — имя пользователя кластера Managed PostgreSQL®.

<postgres_admin_password> — пароль указанного пользователя.

<postgres_ip> — приватный IP-адрес кластера.

Запустите контейнеры:

```bash
docker
compose up
-d
```

Проверьте статус контейнеров:

```bash
docker
compose
ps
docker
compose logs
-f
sonarqube
```

Перейдите по адресу https://sonar.<ip_address>.nip.io и войдите в панель администратора, используя временные логин и пароль admin.

Смените пароль администратора.

## 6. Отключите SSH-доступ

Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.

1. В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите sonarqube.
3. Перейдите на вкладку Сетевые параметры.
4. В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите sonarqube.

Перейдите на вкладку Сетевые параметры.

В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## 7. Подключите SonarQube к репозиторию в GitVerse

На этом шаге вы подключите SonarQube к проекту, размещенному в GitVerse, через CI/CD процесс.

1. Склонируйте [репозиторий с приложением](https://gitverse.ru/cloudru/evo-virtual-machine-sonarqube-lab)репозиторий с приложением в GitVerse.
2. Перейдите в SonarQube по адресу https://sonar.<ip_address>.nip.io/projects.
3. Нажмите Create Project → Local.
4. Создайте проект со следующими значениями:

Project display name — evo-virtual-machine-sonarqube-lab.
Project key — evo-virtual-machine-sonarqube-lab.
Main branch name — master.
5. Нажмите Next.
6. Выберите значение Use the global setting.
7. Нажмите Create project.
8. В параметре Analysis Method выберите With GitHub Actions.
9. Нажмите Generate a token и скопируйте сгенерированный токен.
10. Добавьте [секреты в GitVerse репозиторий](https://gitverse.ru/docs/knowledge-base/actions/secrets)секреты в GitVerse репозиторий:

SONAR_TOKEN;
SONAR_HOST_URL.
11. Убедитесь, что сборка CI/CD прошла успешно.
Если сборка неуспешная, нажмите Перезапустить все джобы.
12. Перейдите в SonarQube по адресу https://sonar.<ip_address>.nip.io/projects и откройте проект evo-virtual-machine-sonar-qube-lab.
13. Посмотрите на отчет, проанализируйте найденные проблемы.

Склонируйте [репозиторий с приложением](https://gitverse.ru/cloudru/evo-virtual-machine-sonarqube-lab)репозиторий с приложением в GitVerse.

Перейдите в SonarQube по адресу https://sonar.<ip_address>.nip.io/projects.

Нажмите Create Project → Local.

Создайте проект со следующими значениями:

- Project display name — evo-virtual-machine-sonarqube-lab.
- Project key — evo-virtual-machine-sonarqube-lab.
- Main branch name — master.

Project display name — evo-virtual-machine-sonarqube-lab.

Project key — evo-virtual-machine-sonarqube-lab.

Main branch name — master.

Нажмите Next.

Выберите значение Use the global setting.

Нажмите Create project.

В параметре Analysis Method выберите With GitHub Actions.

Нажмите Generate a token и скопируйте сгенерированный токен.

Добавьте [секреты в GitVerse репозиторий](https://gitverse.ru/docs/knowledge-base/actions/secrets)секреты в GitVerse репозиторий:

- SONAR_TOKEN;
- SONAR_HOST_URL.

SONAR_TOKEN;

SONAR_HOST_URL.

Убедитесь, что сборка CI/CD прошла успешно.
Если сборка неуспешная, нажмите Перезапустить все джобы.

![../_images/sonarqube_gitverse_cicd.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/sonarqube_gitverse_cicd.png)

Перейдите в SonarQube по адресу https://sonar.<ip_address>.nip.io/projects и откройте проект evo-virtual-machine-sonar-qube-lab.

Посмотрите на отчет, проанализируйте найденные проблемы.

![../_images/sonarqube_analysis_report.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/sonarqube_analysis_report.png)

## 8. Подключите SonarQube к Visual Studio Code

На этом шаге вы подключите сервер SonarQube к проекту в IDE Visual Studio Code для получения подсказок в коде.

1. Откройте Visual Studio Code.
2. Склонируйте [репозиторий с примером](https://gitverse.ru/cloudru/evo-virtual-machine-sonarqube-lab)репозиторий с примером в GitVerse.
3. Откройте репозиторий с кодом примера evo-virtual-machine-sonarqube-lab в Visual Studio Code.
4. Установите расширение [SonarQube for IDE](https://marketplace.visualstudio.com/items)SonarQube for IDE для подключения SonarQube к редактору Visual Studio Code.
5. В левом меню Visual Studio Code нажмите на расширение SonarQube Setup.
6. Нажмите Connect to SonarQube Server.
7. В параметре Server URL введите значение https://sonar.<ip_address>.nip.io.
8. Нажмите Generate Token.
9. В открывшемся окне браузера подтвердите соединение и скопируйте токен.
10. Вставьте скопированное значение в User Token.
11. Нажмите Save connection.
12. Нажмите кнопку + в меню SonarQube Setup.
13. Выберите проект evo-virtual-machine-sonarqube-lab в выпадающем меню.
14. Откройте файл health-check.service.ts в Visual Studio Code и проверьте, что в строке 23 подсвечена ошибка.
Такая же ошибка отображается в результатах анализа проекта в SonarQube.

Откройте Visual Studio Code.

Склонируйте [репозиторий с примером](https://gitverse.ru/cloudru/evo-virtual-machine-sonarqube-lab)репозиторий с примером в GitVerse.

Откройте репозиторий с кодом примера evo-virtual-machine-sonarqube-lab в Visual Studio Code.

Установите расширение [SonarQube for IDE](https://marketplace.visualstudio.com/items)SonarQube for IDE для подключения SonarQube к редактору Visual Studio Code.

В левом меню Visual Studio Code нажмите на расширение SonarQube Setup.

Нажмите Connect to SonarQube Server.

В параметре Server URL введите значение https://sonar.<ip_address>.nip.io.

Нажмите Generate Token.

В открывшемся окне браузера подтвердите соединение и скопируйте токен.

Вставьте скопированное значение в User Token.

Нажмите Save connection.

Нажмите кнопку + в меню SonarQube Setup.

Выберите проект evo-virtual-machine-sonarqube-lab в выпадающем меню.

![../_images/sonarqube_project_binding.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/sonarqube_project_binding.png)

Откройте файл health-check.service.ts в Visual Studio Code и проверьте, что в строке 23 подсвечена ошибка.
Такая же ошибка отображается в результатах анализа проекта в SonarQube.

![../_images/sonarqube_warning.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/sonarqube_warning.png)

## Результат

Вы развернули изолированную облачную инфраструктуру с SonarQube, подключенной к управляемой базе Managed PostgreSQL®, опубликовали сервис через Nginx с автоматическим выпуском TLS-сертификатов Let’s Encrypt и обеспечили доступ по HTTPS.
Вы подключили репозиторий из Git, настроили CI/CD-пайплайн для автоматического анализа кода при каждом commit и интегрировали SonarQube с VS Code для локального статического анализа.

Таким образом, вы освоили ключевые практики DevSecOps и получили защищенный, полностью автоматизированный сервис контроля качества и безопасности кода.
