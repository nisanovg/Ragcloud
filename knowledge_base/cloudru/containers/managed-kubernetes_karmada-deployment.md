---
title: Развертывание мультикластера Managed Kubernetes с помощью Karmada
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment
topic: containers
---
# Развертывание мультикластера Managed Kubernetes с помощью Karmada

С помощью этого руководства вы развернете мультикластерное окружение на базе Managed Kubernetes при помощи платформы Karmada.
Вы научитесь создавать и конфигурировать кластеры Kubernetes, управлять доступом и интегрировать несколько кластеров через централизованную платформу.
В результате вы получите рабочую мультикластерную инфраструктуру для одновременного и унифицированного управления приложениями в разных кластерах Kubernetes.

Вы будете использовать следующие сервисы:

- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для подключения и администрирования кластеров Kubernetes.
- [Karmada](https://github.com/karmada-io/karmada)Karmada — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для подключения и администрирования кластеров Kubernetes.

[Karmada](https://github.com/karmada-io/karmada)Karmada — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.

Шаги:

1. [Сгенерируйте ключи доступа для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Сгенерируйте ключи доступа для интеграции
2. [Создайте необходимые сети, NAT и виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Создайте необходимые сети, NAT и виртуальную машину
3. [Подготовьте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Подготовьте окружение виртуальной машины
4. [Создайте и настройте кластеры Evolution Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Создайте и настройте кластеры Evolution Managed Kubernetes
5. [Настройте подключение к кластерам Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Настройте подключение к кластерам Kubernetes
6. [Настройте внешний балансировщик нагрузки для Karmada](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Настройте внешний балансировщик нагрузки для Karmada
7. [Установите Karmada и интегрируйте кластеры-участники](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Установите Karmada и интегрируйте кластеры-участники

[Сгенерируйте ключи доступа для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Сгенерируйте ключи доступа для интеграции

[Создайте необходимые сети, NAT и виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Создайте необходимые сети, NAT и виртуальную машину

[Подготовьте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Подготовьте окружение виртуальной машины

[Создайте и настройте кластеры Evolution Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Создайте и настройте кластеры Evolution Managed Kubernetes

[Настройте подключение к кластерам Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Настройте подключение к кластерам Kubernetes

[Настройте внешний балансировщик нагрузки для Karmada](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Настройте внешний балансировщик нагрузки для Karmada

[Установите Karmada и интегрируйте кластеры-участники](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Установите Karmada и интегрируйте кластеры-участники

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Сгенерируйте ключи доступа для интеграции

Получите ключи для программного доступа к ресурсам облака Cloud.ru, которые понадобятся для интеграции с Managed Kubernetes.

1. Сгенерируйте ключи доступа (Key ID и Key Secret) для вашего аккаунта [по инструкции](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)по инструкции.
2. Сохраните значения Key ID и Key Secret в безопасном месте.

Сгенерируйте ключи доступа (Key ID и Key Secret) для вашего аккаунта [по инструкции](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)по инструкции.

Сохраните значения Key ID и Key Secret в безопасном месте.

## 2. Разверните ресурсы в облаке

На этом шаге вы подготовите подсети, NAT-шлюз и виртуальную машину, которая будет использоваться для управления кластерами.

1. [Создайте три отдельные подсети](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте три отдельные подсети в одной зоне доступности (например, AZ2) для размещения кластеров Managed Kubernetes.
2. [Создайте NAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте NAT-шлюз (SNAT) в этой же зоне.
3. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с подсетью и публичным IP.

[Создайте три отдельные подсети](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте три отдельные подсети в одной зоне доступности (например, AZ2) для размещения кластеров Managed Kubernetes.

[Создайте NAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте NAT-шлюз (SNAT) в этой же зоне.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с подсетью и публичным IP.

## 3. Подготовьте окружение виртуальной машины

На этом шаге вы настроите окружение для последующей работы с кластерами Kubernetes.

1. [Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH, используя соответствующий клиент.
2. Установите на виртуальной машине необходимые инструменты для работы с Managed Kubernetes:

[Установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)Установите kubectl.
[Установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)Установите cloudlogin.
3. Установите Git и клонируйте репозиторий Karmada:

Установите Git (команда приведена для ОС на базе Ubuntu/Debian):
sudo apt update && sudo apt install -y git

Клонируйте официальный репозиторий Karmada:
git clone https://github.com/karmada-io/karmada.git
4. Установите Go версии 1.24.6:
ПримечаниеПроверьте версию Go в файле go.mod репозитория karmada.

Загрузите и установите Go:
curl -fsSLo go1.24.6.linux-amd64.tar.gz https://go.dev/dl/go1.24.6.linux-amd64.tar.gzsudo tar -C /usr/local -xzf go1.24.6.linux-amd64.tar.gzecho 'export GOROOT=/usr/local/go' >> ~/.bashrcecho 'export GOPATH=$HOME/go' >> ~/.bashrcecho 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin' >> ~/.bashrcsource ~/.bashrc

Проверьте корректность установки:
go version
5. Установите Docker:
curl -fsSL https://get.docker.com -o get-docker.shsudo sh ./get-docker.shsudo groupadd dockersudo usermod -aG docker $USERnewgrp docker

[Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH, используя соответствующий клиент.

Установите на виртуальной машине необходимые инструменты для работы с Managed Kubernetes:

1. [Установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)Установите kubectl.
2. [Установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)Установите cloudlogin.

[Установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)Установите kubectl.

[Установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)Установите cloudlogin.

Установите Git и клонируйте репозиторий Karmada:

1. Установите Git (команда приведена для ОС на базе Ubuntu/Debian):
sudo apt update && sudo apt install -y git
2. Клонируйте официальный репозиторий Karmada:
git clone https://github.com/karmada-io/karmada.git

Установите Git (команда приведена для ОС на базе Ubuntu/Debian):

```bash
sudo
apt
update
&&
sudo
apt
install
-y
git
```

Клонируйте официальный репозиторий Karmada:

```bash
git
clone https://github.com/karmada-io/karmada.git
```

Установите Go версии 1.24.6:

Проверьте версию Go в файле go.mod репозитория karmada.

1. Загрузите и установите Go:
curl -fsSLo go1.24.6.linux-amd64.tar.gz https://go.dev/dl/go1.24.6.linux-amd64.tar.gzsudo tar -C /usr/local -xzf go1.24.6.linux-amd64.tar.gzecho 'export GOROOT=/usr/local/go' >> ~/.bashrcecho 'export GOPATH=$HOME/go' >> ~/.bashrcecho 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin' >> ~/.bashrcsource ~/.bashrc
2. Проверьте корректность установки:
go version

Загрузите и установите Go:

```bash
curl
-fsSLo
go1.24.6.linux-amd64.tar.gz https://go.dev/dl/go1.24.6.linux-amd64.tar.gz
sudo
tar
-C
/usr/local
-xzf
go1.24.6.linux-amd64.tar.gz
echo
'export GOROOT=/usr/local/go'
>>
~/.bashrc
echo
'export GOPATH=$HOME/go'
>>
~/.bashrc
echo
'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin'
>>
~/.bashrc
source
~/.bashrc
```

Проверьте корректность установки:

```bash
go version
```

Установите Docker:

```bash
curl
-fsSL
https://get.docker.com
-o
get-docker.sh
sudo
sh
./get-docker.sh
sudo
groupadd
docker
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

## 4. Создайте и настройте кластеры Managed Kubernetes

На этом шаге вы создадите основной кластер для control plane Karmada и два кластера-участника.

1. [Создайте три кластера](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте три кластера в сервисе Managed Kubernetes: основной (control plane) и два кластера-участника.
Для каждого выберите ранее созданные подсети и разместите их в одной VPC.

Основной кластер:

Имя: mk8s-karmada-control-plane
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.101.0.0/16
Подсеть подов: 10.102.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3

Кластер-участник 1:

Имя: mk8s-evo1
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.111.0.0/16
Подсеть подов: 10.112.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3

Кластер-участник 2:

Имя: mk8s-evo2
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.121.0.0/16
Подсеть подов: 10.122.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3
2. Дождитесь окончания создания кластеров.
Убедитесь, что в личном кабинете статус всех кластеров — «Запущено».

[Создайте три кластера](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте три кластера в сервисе Managed Kubernetes: основной (control plane) и два кластера-участника.
Для каждого выберите ранее созданные подсети и разместите их в одной VPC.

- Основной кластер:

Имя: mk8s-karmada-control-plane
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.101.0.0/16
Подсеть подов: 10.102.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3
- Кластер-участник 1:

Имя: mk8s-evo1
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.111.0.0/16
Подсеть подов: 10.112.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3
- Кластер-участник 2:

Имя: mk8s-evo2
Число мастер-узлов: 1
Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
Публичный IP: включен
Подсеть сервисов: 10.121.0.0/16
Подсеть подов: 10.122.0.0/16
Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
Количество узлов: 3

Основной кластер:

- Имя: mk8s-karmada-control-plane
- Число мастер-узлов: 1
- Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
- Публичный IP: включен
- Подсеть сервисов: 10.101.0.0/16
- Подсеть подов: 10.102.0.0/16
- Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
- Количество узлов: 3

Имя: mk8s-karmada-control-plane

Число мастер-узлов: 1

Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM

Публичный IP: включен

Подсеть сервисов: 10.101.0.0/16

Подсеть подов: 10.102.0.0/16

Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM

Количество узлов: 3

Кластер-участник 1:

- Имя: mk8s-evo1
- Число мастер-узлов: 1
- Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
- Публичный IP: включен
- Подсеть сервисов: 10.111.0.0/16
- Подсеть подов: 10.112.0.0/16
- Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
- Количество узлов: 3

Имя: mk8s-evo1

Число мастер-узлов: 1

Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM

Публичный IP: включен

Подсеть сервисов: 10.111.0.0/16

Подсеть подов: 10.112.0.0/16

Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM

Количество узлов: 3

Кластер-участник 2:

- Имя: mk8s-evo2
- Число мастер-узлов: 1
- Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM
- Публичный IP: включен
- Подсеть сервисов: 10.121.0.0/16
- Подсеть подов: 10.122.0.0/16
- Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM
- Количество узлов: 3

Имя: mk8s-evo2

Число мастер-узлов: 1

Ресурсы мастер-узла: 2 vCPU, 4 ГБ RAM

Публичный IP: включен

Подсеть сервисов: 10.121.0.0/16

Подсеть подов: 10.122.0.0/16

Конфигурация группы узлов: 2 vCPU, гарантированная доля vCPU — 30%, 4 ГБ RAM

Количество узлов: 3

Дождитесь окончания создания кластеров.
Убедитесь, что в личном кабинете статус всех кластеров — «Запущено».

## 5. Настройте подключение к кластерам Kubernetes

На этом шаге вы обеспечите конфигурирование доступа к каждому кластеру с управляющей виртуальной машины.

1. [Скачайте файлы kubeconfig](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Скачайте файлы kubeconfig для всех кластеров в личном кабинете.
2. Создайте директорию .kube, которая будет использоваться по умолчанию для основного кластера:
mkdir -p $HOME/.kube
3. Создайте директорию для конфигураций кластеров-участников:
mkdir -p $HOME/join-clusters
4. Сохраните файлы kubeconfig по следующим путям:

mk8s-karmada-control-plane: $HOME/.kube/config (по умолчанию)
mk8s-evo1: $HOME/join-clusters/evo1
mk8s-evo2: $HOME/join-clusters/evo2
5. Задайте значения <KEY_ID> и <KEY_SECRET> для параметров CLOUDRU_KEY_ID и CLOUDRU_SECRET_ID с помощью команды:
sed -i \ -e '/name: CLOUDRU_KEY_ID/ {n; s/value: ""/value: "<KEY_ID>"/}' \ -e '/name: CLOUDRU_SECRET_ID/ {n; s/value: ""/value: "<KEY_SECRET>"/}' \ $HOME/.kube/config \ $HOME/join-clusters/evo1 \ $HOME/join-clusters/evo2

Где:

<KEY_ID> — сгенерированный ранее Key ID.
<KEY_SECRET> — сгенерированный ранее Key Secret.
6. Проверьте доступ к кластерам Kubernetes:
kubectl cluster-infokubectl --kubeconfig=$HOME/join-clusters/evo1 cluster-infokubectl --kubeconfig=$HOME/join-clusters/evo2 cluster-info

Убедитесь, что каждая команда возвращает информацию о кластере без ошибок аутентификации.

[Скачайте файлы kubeconfig](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Скачайте файлы kubeconfig для всех кластеров в личном кабинете.

Создайте директорию .kube, которая будет использоваться по умолчанию для основного кластера:

```bash
mkdir
-p
$HOME
/.kube
```

Создайте директорию для конфигураций кластеров-участников:

```bash
mkdir
-p
$HOME
/join-clusters
```

Сохраните файлы kubeconfig по следующим путям:

- mk8s-karmada-control-plane: $HOME/.kube/config (по умолчанию)
- mk8s-evo1: $HOME/join-clusters/evo1
- mk8s-evo2: $HOME/join-clusters/evo2

mk8s-karmada-control-plane: $HOME/.kube/config (по умолчанию)

mk8s-evo1: $HOME/join-clusters/evo1

mk8s-evo2: $HOME/join-clusters/evo2

Задайте значения <KEY_ID> и <KEY_SECRET> для параметров CLOUDRU_KEY_ID и CLOUDRU_SECRET_ID с помощью команды:

```bash
sed
-i
\
-e
'/name: CLOUDRU_KEY_ID/ {n; s/value: ""/value: "<KEY_ID>"/}'
\
-e
'/name: CLOUDRU_SECRET_ID/ {n; s/value: ""/value: "<KEY_SECRET>"/}'
\
$HOME
/.kube/config
\
$HOME
/join-clusters/evo1
\
$HOME
/join-clusters/evo2
```

Где:

- <KEY_ID> — сгенерированный ранее Key ID.
- <KEY_SECRET> — сгенерированный ранее Key Secret.

<KEY_ID> — сгенерированный ранее Key ID.

<KEY_SECRET> — сгенерированный ранее Key Secret.

Проверьте доступ к кластерам Kubernetes:

```bash
kubectl cluster-info
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 cluster-info
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo2 cluster-info
```

Убедитесь, что каждая команда возвращает информацию о кластере без ошибок аутентификации.

## 6. Настройте внешний балансировщик нагрузки для Karmada

На этом шаге вы создадите внешний балансировщик, чтобы организовать доступ к API-серверу Karmada через сервис [Load Balancer](https://cloud.ru/docs/nlb/ug/index)Load Balancer.

Мы будем устанавливать Karmada на кластер mk8s-karmada-control-plane с помощью скрипта установки из репозитория Karmada.
При установке необходимо указать каким образом мы будем обращаться к API-серверу Karmada:

- через HostNetwork — отправка обращений на порт tcp/5443 непосредственно узла, на котором будет запущен под karmada-apiserver;
- через LoadBalancer — отправка обращений к API-серверу через балансировщик нагрузки.
Балансировщик нагрузки слушает порт tcp/5443 и переадресует наши запросы поду karmada-apiserver.

через HostNetwork — отправка обращений на порт tcp/5443 непосредственно узла, на котором будет запущен под karmada-apiserver;

через LoadBalancer — отправка обращений к API-серверу через балансировщик нагрузки.
Балансировщик нагрузки слушает порт tcp/5443 и переадресует наши запросы поду karmada-apiserver.

В этом сценарии мы будем обращаться к API-серверу через LoadBalancer.

Важно учесть, что скрипт установки сначала генерирует все необходимые сертификаты, а затем создает все необходимые ресурсы, в том числе сервис LoadBalancer.
Скрипт создает сертификаты для серверных компонентов с опцией SAN.
Поскольку скрипт в начале не может знать IP-адрес балансировщика нагрузки, т.к. он еще не создан, то он не добавляет этот IP-адрес как альтернативное имя субъекта.
Из-за этого вы не сможете подключиться к API-серверу через балансировщик нагрузки.
Чтобы выйти из ситуации, вы можете перевыпустить сертификаты после установки, но этот путь довольно ресурсозатратный.

Также вы можете, узнав IP-адрес балансировщика, переустановить Karmada.
В этом случае вы не застрахованы, что IP-адрес балансировщика будет другим.
Мы предлагаем создать заранее namespace karmada-system и сервис типа LoadBalancer.
Когда вы создадите балансировщик нагрузки в кластере Kubernetes, [платформа автоматически создаст балансировщик нагрузки](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__networks__load-balancer-external)платформа автоматически создаст балансировщик нагрузки в сервисе Evolution Load Balancer с параметрами сервиса Kubernetes.

1. Создайте папку karmada-manifests:
mkdir $HOME/karmada-manifests
2. Создайте там файл karmada.yaml и скопируйте следующий манифест:
apiVersion: v1kind: Namespacemetadata: labels: kubernetes.io/metadata.name: karmada-system name: karmada-system---apiVersion: v1kind: Servicemetadata: name: karmada-apiserver labels: app: karmada-apiserver annotations: loadbalancer.mk8s.cloud.ru/type: "external" loadbalancer.mk8s.cloud.ru/health-check-timeout-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-interval-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-unhealthy-threshold-count: "4" loadbalancer.mk8s.cloud.ru/health-check-healthy-threshold-count: "4" namespace: karmada-systemspec: type: LoadBalancer selector: app: karmada-apiserver ports: - name: karmada-apiserver-kubectl port: 5443 protocol: TCP targetPort: 5443
3. Примените манифест к основному кластеру Kubernetes:
kubectl apply -f $HOME/karmada-manifests/karmada.yaml
4. Убедитесь, что сервис создан:
kubectl -n karmada-system get svc karmada-apiserver

Проверьте, что сервис отображается, статус внешнего IP — <pending>.
Это означает, что Evolution Load Balancer создает ресурс и назначает публичный IP.
Подождите около 8-10 минут, пока балансировщик нагрузки получит внешний IP-адрес и закончит настройку.

Создайте папку karmada-manifests:

```bash
mkdir
$HOME
/karmada-manifests
```

Создайте там файл karmada.yaml и скопируйте следующий манифест:

```bash
apiVersion
:
v1
kind
:
Namespace
metadata
:
labels
:
kubernetes.io/metadata.name
:
karmada
-
system
name
:
karmada
-
system
---
apiVersion
:
v1
kind
:
Service
metadata
:
name
:
karmada
-
apiserver
labels
:
app
:
karmada
-
apiserver
annotations
:
loadbalancer.mk8s.cloud.ru/type
:
"external"
loadbalancer.mk8s.cloud.ru/health-check-timeout-seconds
:
"5"
loadbalancer.mk8s.cloud.ru/health-check-interval-seconds
:
"5"
loadbalancer.mk8s.cloud.ru/health-check-unhealthy-threshold-count
:
"4"
loadbalancer.mk8s.cloud.ru/health-check-healthy-threshold-count
:
"4"
namespace
:
karmada
-
system
spec
:
type
:
LoadBalancer
selector
:
app
:
karmada
-
apiserver
ports
:
-
name
:
karmada
-
apiserver
-
kubectl
port
:
5443
protocol
:
TCP
targetPort
:
5443
```

Примените манифест к основному кластеру Kubernetes:

```bash
kubectl apply
-f
$HOME
/karmada-manifests/karmada.yaml
```

Убедитесь, что сервис создан:

```bash
kubectl
-n
karmada-system get svc karmada-apiserver
```

Проверьте, что сервис отображается, статус внешнего IP — <pending>.
Это означает, что Evolution Load Balancer создает ресурс и назначает публичный IP.
Подождите около 8-10 минут, пока балансировщик нагрузки получит внешний IP-адрес и закончит настройку.

## 7. Установите Karmada и интегрируйте кластеры-участники

На этом шаге вы установите Karmada на основной кластер, учитывая внешний IP-адрес балансировщика, и подключите оба кластера-участника.

1. После назначения публичного IP для балансировщика получите этот IP-адрес:
kubectl -n karmada-system get svc karmada-apiserver -o jsonpath="{range .status.loadBalancer.ingress[*]}{.ip}{'\n'}{end}"
2. Скопируйте полученный IP и вставьте его в установочный скрипт deploy-karmada.sh для корректной генерации сертификатов:
sed -i "1iKARMADA_APISERVER_IP=\"<IP_BALANCER>\"" $HOME/karmada/hack/deploy-karmada.shsed -i 's#karmada_apiserver_alt_names=("karmada-apiserver.karmada-system.svc.cluster.local" "karmada-apiserver.karmada-system.svc" "localhost" "127.0.0.1" $(util::get_apiserver_ip_from_kubeconfig "${HOST_CLUSTER_NAME}"))#karmada_apiserver_alt_names=("karmada-apiserver.karmada-system.svc.cluster.local" "karmada-apiserver.karmada-system.svc" "localhost" "127.0.0.1" "${KARMADA_APISERVER_IP}" $(util::get_apiserver_ip_from_kubeconfig "${HOST_CLUSTER_NAME}"))#' $HOME/karmada/hack/deploy-karmada.shsed -i 's/HOST_CLUSTER_NAME=${HOST_CLUSTER_NAME:-"karmada-host"}/HOST_CLUSTER_NAME=${HOST_CLUSTER_NAME:-"karmada-apiserver"}/' $HOME/karmada/hack/deploy-karmada.sh

Где:

<IP_BALANCER> — публичный IP-адрес балансировщика нагрузки.
3. Установите переменную окружения, чтобы скрипт используя сервис Load Balancer:
export LOAD_BALANCER=true
4. Запустите установку Karmada на кластер mk8s-karmada-control-plane:
$HOME/karmada/hack/remote-up-karmada.sh $HOME/.kube/config <K8S_KARMADA_CONTEXT_NAME>

Где:

<K8S_KARMADA_CONTEXT_NAME> — имя контекста кластера из файла конфигурации.
5. Проверьте, что все компоненты Karmada развернуты корректно:
kubectl get pods -n karmada-systemkubectl get services -n karmada-system
6. Установите инструмент CLI karmadactl:

Скачайте и установите утилиту:
curl -s https://raw.githubusercontent.com/karmada-io/karmada/master/hack/install-cli.sh | sudo bash

Проверьте, что karmadactl успешно установлена:
karmadactl version
7. Подключите оба кластера-участника к Karmada:

Для кластера mk8s-evo1 выполните комманду:
karmadactl join evo1 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo1

Для кластера mk8s-evo2 выполните комманду:
karmadactl join evo2 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo2
8. Проверьте, что оба кластера успешно добавлены и отображаются со статусом «Ready»:
karmadactl --karmada-context karmada-apiserver get clusters

В консоли должны отобразиться оба кластера: evo1 и evo2, статус — «Ready».

После назначения публичного IP для балансировщика получите этот IP-адрес:

```bash
kubectl
-n
karmada-system get svc karmada-apiserver
-o
jsonpath
=
"{range .status.loadBalancer.ingress[*]}{.ip}{'
\n
'}{end}"
```

Скопируйте полученный IP и вставьте его в установочный скрипт deploy-karmada.sh для корректной генерации сертификатов:

```bash
sed
-i
"1iKARMADA_APISERVER_IP=
\"
<IP_BALANCER>
\"
"
$HOME
/karmada/hack/deploy-karmada.sh
sed
-i
's#karmada_apiserver_alt_names=("karmada-apiserver.karmada-system.svc.cluster.local" "karmada-apiserver.karmada-system.svc" "localhost" "127.0.0.1" $(util::get_apiserver_ip_from_kubeconfig "${HOST_CLUSTER_NAME}"))#karmada_apiserver_alt_names=("karmada-apiserver.karmada-system.svc.cluster.local" "karmada-apiserver.karmada-system.svc" "localhost" "127.0.0.1" "${KARMADA_APISERVER_IP}" $(util::get_apiserver_ip_from_kubeconfig "${HOST_CLUSTER_NAME}"))#'
$HOME
/karmada/hack/deploy-karmada.sh
sed
-i
's/HOST_CLUSTER_NAME=${HOST_CLUSTER_NAME:-"karmada-host"}/HOST_CLUSTER_NAME=${HOST_CLUSTER_NAME:-"karmada-apiserver"}/'
$HOME
/karmada/hack/deploy-karmada.sh
```

Где:

- <IP_BALANCER> — публичный IP-адрес балансировщика нагрузки.

<IP_BALANCER> — публичный IP-адрес балансировщика нагрузки.

Установите переменную окружения, чтобы скрипт используя сервис Load Balancer:

```bash
export
LOAD_BALANCER
=
true
```

Запустите установку Karmada на кластер mk8s-karmada-control-plane:

```bash
$HOME
/karmada/hack/remote-up-karmada.sh
$HOME
/.kube/config
<
K8S_KARMADA_CONTEXT_NAME
>
```

Где:

- <K8S_KARMADA_CONTEXT_NAME> — имя контекста кластера из файла конфигурации.

<K8S_KARMADA_CONTEXT_NAME> — имя контекста кластера из файла конфигурации.

Проверьте, что все компоненты Karmada развернуты корректно:

```bash
kubectl get pods
-n
karmada-system
kubectl get services
-n
karmada-system
```

Установите инструмент CLI karmadactl:

1. Скачайте и установите утилиту:
curl -s https://raw.githubusercontent.com/karmada-io/karmada/master/hack/install-cli.sh | sudo bash
2. Проверьте, что karmadactl успешно установлена:
karmadactl version

Скачайте и установите утилиту:

```bash
curl
-s
https://raw.githubusercontent.com/karmada-io/karmada/master/hack/install-cli.sh
|
sudo
bash
```

Проверьте, что karmadactl успешно установлена:

```bash
karmadactl version
```

Подключите оба кластера-участника к Karmada:

1. Для кластера mk8s-evo1 выполните комманду:
karmadactl join evo1 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo1
2. Для кластера mk8s-evo2 выполните комманду:
karmadactl join evo2 --karmada-context karmada-apiserver --cluster-kubeconfig $HOME/join-clusters/evo2

Для кластера mk8s-evo1 выполните комманду:

```bash
karmadactl
join
evo1 --karmada-context karmada-apiserver --cluster-kubeconfig
$HOME
/join-clusters/evo1
```

Для кластера mk8s-evo2 выполните комманду:

```bash
karmadactl
join
evo2 --karmada-context karmada-apiserver --cluster-kubeconfig
$HOME
/join-clusters/evo2
```

Проверьте, что оба кластера успешно добавлены и отображаются со статусом «Ready»:

```bash
karmadactl --karmada-context karmada-apiserver get clusters
```

В консоли должны отобразиться оба кластера: evo1 и evo2, статус — «Ready».

## Результат

Вы развернули мультикластерную инфраструктуру Evolution Managed Kubernetes, подготовили внешний балансировщик нагрузки и добавили кластеры-участники control plane Karmada.
Теперь вы можете централизованно управлять приложениями в распределенной среде Kubernetes, расширять масштабируемость и надежность ваших сервисов.
