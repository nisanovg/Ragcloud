---
title: Event-driven масштабирование в Managed Kubernetes с помощью KEDA
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling
topic: containers
---
# Event-driven масштабирование в Managed Kubernetes с помощью KEDA

С помощью этого руководства вы развернете инфраструктуру Managed Kubernetes и установите решение KEDA для event-driven автомасштабирования приложений.

Вы настроите масштабирование Kubernetes Job на основе сообщений из очереди RabbitMQ, что позволит реализовать обработку событий и горизонтальное масштабирование без привязки к метрикам потребления ресурсов.

В результате вы получите решение для асинхронной обработки задач в Kubernetes с использованием KEDA.

Вы будете использовать следующие сервисы:

- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис для создания виртуальных машин, используемых для управления кластерами и запуска утилит администрирования.
- [KEDA](https://keda.sh/docs/2.17)KEDA — платформа для событийного масштабирования приложений в Kubernetes на основе внешних триггеров, таких как очереди сообщений и базы данных.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис для создания виртуальных машин, используемых для управления кластерами и запуска утилит администрирования.

[KEDA](https://keda.sh/docs/2.17)KEDA — платформа для событийного масштабирования приложений в Kubernetes на основе внешних триггеров, таких как очереди сообщений и базы данных.

Шаги:

1. [Сгенерируйте ключи доступа для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Сгенерируйте ключи доступа для интеграции.
2. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Разверните ресурсы в облаке.
3. [Подготовьте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Подготовьте окружение виртуальной машины.
4. [Создайте кластер Managed Kubernetes и подключитесь к нему](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Создайте кластер Managed Kubernetes и подключитесь к нему.
5. [Создайте репозиторий Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Создайте репозиторий Artifact Registry.
6. [Установите MongoDB через Helm](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите MongoDB через Helm.
7. [Установите RabbitMQ через Helm](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите RabbitMQ через Helm.
8. [Установите KEDA](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите KEDA.
9. [Загрузите образы контейнеров в приватный реестр Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Загрузите образы контейнеров в приватный реестр Artifact Registry.
10. [Разверните приложение в Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Разверните приложение в Kubernetes.
11. [Проверьте работу автомасштабирования KEDA](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Проверьте работу автомасштабирования KEDA.

[Сгенерируйте ключи доступа для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Сгенерируйте ключи доступа для интеграции.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Разверните ресурсы в облаке.

[Подготовьте окружение виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Подготовьте окружение виртуальной машины.

[Создайте кластер Managed Kubernetes и подключитесь к нему](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Создайте кластер Managed Kubernetes и подключитесь к нему.

[Создайте репозиторий Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Создайте репозиторий Artifact Registry.

[Установите MongoDB через Helm](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите MongoDB через Helm.

[Установите RabbitMQ через Helm](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите RabbitMQ через Helm.

[Установите KEDA](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Установите KEDA.

[Загрузите образы контейнеров в приватный реестр Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Загрузите образы контейнеров в приватный реестр Artifact Registry.

[Разверните приложение в Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Разверните приложение в Kubernetes.

[Проверьте работу автомасштабирования KEDA](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__keda-scaling)Проверьте работу автомасштабирования KEDA.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Сгенерируйте ключи доступа для интеграции

На этом этапе получите ключи для программного доступа к ресурсам облачной платформы, которые потребуются для интеграции с Managed Kubernetes и приватным реестром Artifact Registry.

1. [Сгенерируйте ключи доступа Key ID и Key Secret для своего аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа Key ID и Key Secret для своего аккаунта.
2. Сохраните значения Key ID и Key Secret в надежном месте, чтобы использовать их при загрузке образов контейнеров и подключении к кластеру Managed Kubernetes.

[Сгенерируйте ключи доступа Key ID и Key Secret для своего аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа Key ID и Key Secret для своего аккаунта.

Сохраните значения Key ID и Key Secret в надежном месте, чтобы использовать их при загрузке образов контейнеров и подключении к кластеру Managed Kubernetes.

## 2. Разверните ресурсы в облаке

Этот шаг включает подготовку подсети, NAT-шлюза и виртуальной машины для последующей работы и управления кластером.

1. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть для размещения кластера Managed Kubernetes.
2. [Создайте SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте SNAT-шлюз в той же зоне доступности, что и подсеть.
3. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с подсетью с публичным IP-адресом.
Выберите ранее созданную подсеть для подключения.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть для размещения кластера Managed Kubernetes.

[Создайте SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте SNAT-шлюз в той же зоне доступности, что и подсеть.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину с подсетью с публичным IP-адресом.
Выберите ранее созданную подсеть для подключения.

## 3. Подготовьте окружение виртуальной машины

На этом этапе настройте окружение для управления облачной инфраструктурой и кластером Kubernetes.

1. [Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH, используя соответствующий SSH-клиент.
2. Установите необходимые инструменты для работы с Managed Kubernetes:

[kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl
[cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin
3. Установите Git и клонируйте репозиторий демоприложения:

Установите Git для ОС на базе Ubuntu/Debian:
sudo apt update && sudo apt install -y git

Клонируйте репозиторий демоприложения:
git clone https://gitverse.ru/sedg1l/keda-p2
4. Установите Docker:
curl -fsSL https://get.docker.com -o get-docker.shsudo sh ./get-docker.shsudo groupadd dockersudo usermod -aG docker $USERnewgrp docker
5. Установите Helm:
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3chmod 700 get_helm.sh./get_helm.sh

[Подключитесь к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине по SSH, используя соответствующий SSH-клиент.

Установите необходимые инструменты для работы с Managed Kubernetes:

1. [kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl
2. [cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin

[kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)kubectl

[cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)cloudlogin

Установите Git и клонируйте репозиторий демоприложения:

1. Установите Git для ОС на базе Ubuntu/Debian:
sudo apt update && sudo apt install -y git
2. Клонируйте репозиторий демоприложения:
git clone https://gitverse.ru/sedg1l/keda-p2

Установите Git для ОС на базе Ubuntu/Debian:

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

Клонируйте репозиторий демоприложения:

```bash
git
clone https://gitverse.ru/sedg1l/keda-p2
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

Установите Helm:

```bash
curl
-fsSL
-o
get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod
700
get_helm.sh
./get_helm.sh
```

## 4. Создайте кластер Managed Kubernetes и подключитесь к нему

На этом этапе разверните кластер Kubernetes.

1. [Создайте кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер в сервисе Managed Kubernetes:

Название: Cluster-keda.
Количество мастер-узлов: 1.
Конфигурация мастер-узла: 2 vCPU, 4 ГБ RAM.
Публичный IP: включен.
2. [Создайте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Создайте группу узлов

Гарантированная доля vCPU: 10%.
vCPU: 2.
RAM, ГБ: 4.
Количество узлов: 1.
3. Дождитесь окончания создания кластера.
4. Убедитесь, что в личном кабинете статус кластера — «Запущено».
5. [Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру с управляющей виртуальной машины.

[Создайте кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер в сервисе Managed Kubernetes:

- Название: Cluster-keda.
- Количество мастер-узлов: 1.
- Конфигурация мастер-узла: 2 vCPU, 4 ГБ RAM.
- Публичный IP: включен.

Название: Cluster-keda.

Количество мастер-узлов: 1.

Конфигурация мастер-узла: 2 vCPU, 4 ГБ RAM.

Публичный IP: включен.

[Создайте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Создайте группу узлов

- Гарантированная доля vCPU: 10%.
- vCPU: 2.
- RAM, ГБ: 4.
- Количество узлов: 1.

Гарантированная доля vCPU: 10%.

vCPU: 2.

RAM, ГБ: 4.

Количество узлов: 1.

Дождитесь окончания создания кластера.

Убедитесь, что в личном кабинете статус кластера — «Запущено».

[Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру с управляющей виртуальной машины.

## 5. Создайте репозиторий Artifact Registry

На этом шаге [создайте приватный реестр](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)создайте приватный реестр в сервисе Artifact Registry.

## 6. Установите MongoDB через Helm

На этом шаге вы установите MongoDB в кластер Managed Kubernetes.

1. Установите MongoDB с помощью Helm:
helm install mongodb oci://registry-1.docker.io/bitnamicharts/mongodb --set useStatefulSet=true --set auth.rootPassword=mongo
2. Проверьте статус развертывания MongoDB:
kubectl get pods
3. Дождитесь, пока все поды MongoDB перейдут в состояние «Running».

Установите MongoDB с помощью Helm:

```bash
helm
install
mongodb oci://registry-1.docker.io/bitnamicharts/mongodb
--set
useStatefulSet
=
true
--set
auth.rootPassword
=
mongo
```

Проверьте статус развертывания MongoDB:

```bash
kubectl get pods
```

Дождитесь, пока все поды MongoDB перейдут в состояние «Running».

## 7. Установите RabbitMQ через Helm

На этом шаге установите очередь сообщений RabbitMQ с помощью Helm в кластер Managed Kubernetes.

1. Установите RabbitMQ командой:
helm install rabbitmq oci://registry-1.docker.io/bitnamicharts/rabbitmq --set auth.username=user --set auth.password=P@ssw0rd
2. Проверьте состояние подов RabbitMQ:
kubectl get pods
3. Дождитесь, пока все поды очереди RabbitMQ перейдут в состояние «Running».

Установите RabbitMQ командой:

```bash
helm
install
rabbitmq oci://registry-1.docker.io/bitnamicharts/rabbitmq
--set
auth.username
=
user
--set
auth.password
=
P@ssw0rd
```

Проверьте состояние подов RabbitMQ:

```bash
kubectl get pods
```

Дождитесь, пока все поды очереди RabbitMQ перейдут в состояние «Running».

## 8. Установите KEDA

На этом шаге вы установите KEDA для поддержки событийного масштабирования.

1. [В личном кабинете](https://console.cloud.ru/)В личном кабинете перейдите в созданный кластер Managed Kubernetes.
2. На панели слева выберите Плагины и нажмите Добавить плагин.
3. Выберите KEDA и нажмите Установить.
4. Выберите версию плагина и нажмите Установить.
5. Чтобы проверить статус подов KEDA, в терминале выполните команду:
kubectl get pods -n keda
6. Дождитесь, пока все поды KEDA перейдут в состояние «Running».

[В личном кабинете](https://console.cloud.ru/)В личном кабинете перейдите в созданный кластер Managed Kubernetes.

На панели слева выберите Плагины и нажмите Добавить плагин.

Выберите KEDA и нажмите Установить.

Выберите версию плагина и нажмите Установить.

Чтобы проверить статус подов KEDA, в терминале выполните команду:

```bash
kubectl get pods
-n
keda
```

Дождитесь, пока все поды KEDA перейдут в состояние «Running».

## 9. Загрузите образы контейнеров в приватный реестр Artifact Registry

На этом этапе соберите и загрузите образы собственного приложения в приватный реестр.

1. Перейдите в папку репозитория приложения:
cd $HOME/keda-p2
2. Откройте файл build.sh в удобном редакторе.
3. Укажите URI вашего приватного реестра и ключи доступа к облаку в переменных в начале скрипта:

<REPO> — адрес реестра Artifact Registry.
<LOGIN> — Key ID учетной записи.
<PASSWORD> — Secret Key учетной записи.
4. Сделайте скрипт исполняемым и выполните его:
chmod +x $HOME/keda-p2/build-images.sh$HOME/keda-p2/build-images.sh

Скрипт выполнит аутентификацию с помощью ключей доступа в Artifact Registry, соберет образы контейнеров через Docker Engine и загрузит их в указанный реестр.

Перейдите в папку репозитория приложения:

```bash
cd
$HOME
/keda-p2
```

Откройте файл build.sh в удобном редакторе.

Укажите URI вашего приватного реестра и ключи доступа к облаку в переменных в начале скрипта:

- <REPO> — адрес реестра Artifact Registry.
- <LOGIN> — Key ID учетной записи.
- <PASSWORD> — Secret Key учетной записи.

<REPO> — адрес реестра Artifact Registry.

<LOGIN> — Key ID учетной записи.

<PASSWORD> — Secret Key учетной записи.

Сделайте скрипт исполняемым и выполните его:

```bash
chmod
+x
$HOME
/keda-p2/build-images.sh
$HOME
/keda-p2/build-images.sh
```

Скрипт выполнит аутентификацию с помощью ключей доступа в Artifact Registry, соберет образы контейнеров через Docker Engine и загрузит их в указанный реестр.

## 10. Разверните приложение в Managed Kubernetes

На этом этапе выполните развертывание event-driven приложения, используя подготовленные манифесты.

1. Примените манифесты:
kubectl apply -f $HOME/keda-p2/deploy/
2. Ознакомьтесь со схемой работы приложения:

При отправке POST-запроса на http://complex-app-service/send?name=<item-name>&content=<content> сервис complex-app отправляет сообщение с параметрами name и content в формате JSON в очередь RabbitMQ.
Ресурс ScaledJob периодически опрашивает очередь RabbitMQ.
Когда в очередь приходит новое сообщение, ScaledJob создает новый Kubernetes Job с именем processor-job.
Ресурс processor-job извлекает сообщение, записывает его в MongoDB в формате JSON (name и content), после чего засыпает на 20 секунд.
Функция sleep имитирует, что processor-job обрабатывает какой-то «тяжелый» файл.
Например, конвертирует видео.
Если бы вы масштабировали Deployment с помощью ресурса HPA, то реализовать описанное выше масштабирование было бы невозможно, так как нам необходимо масштабировать ресурс не на основании метрик утилизации ресурсов, а на основании событий.
3. Проверьте, что все необходимые поды созданы и работают.

Примените манифесты:

```bash
kubectl apply
-f
$HOME
/keda-p2/deploy/
```

Ознакомьтесь со схемой работы приложения:

![Схема приложения](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__keda-app.png)

- При отправке POST-запроса на http://complex-app-service/send?name=<item-name>&content=<content> сервис complex-app отправляет сообщение с параметрами name и content в формате JSON в очередь RabbitMQ.
- Ресурс ScaledJob периодически опрашивает очередь RabbitMQ.
Когда в очередь приходит новое сообщение, ScaledJob создает новый Kubernetes Job с именем processor-job.
- Ресурс processor-job извлекает сообщение, записывает его в MongoDB в формате JSON (name и content), после чего засыпает на 20 секунд.
- Функция sleep имитирует, что processor-job обрабатывает какой-то «тяжелый» файл.
Например, конвертирует видео.
- Если бы вы масштабировали Deployment с помощью ресурса HPA, то реализовать описанное выше масштабирование было бы невозможно, так как нам необходимо масштабировать ресурс не на основании метрик утилизации ресурсов, а на основании событий.

При отправке POST-запроса на http://complex-app-service/send?name=<item-name>&content=<content> сервис complex-app отправляет сообщение с параметрами name и content в формате JSON в очередь RabbitMQ.

Ресурс ScaledJob периодически опрашивает очередь RabbitMQ.
Когда в очередь приходит новое сообщение, ScaledJob создает новый Kubernetes Job с именем processor-job.

Ресурс processor-job извлекает сообщение, записывает его в MongoDB в формате JSON (name и content), после чего засыпает на 20 секунд.

Функция sleep имитирует, что processor-job обрабатывает какой-то «тяжелый» файл.
Например, конвертирует видео.

Если бы вы масштабировали Deployment с помощью ресурса HPA, то реализовать описанное выше масштабирование было бы невозможно, так как нам необходимо масштабировать ресурс не на основании метрик утилизации ресурсов, а на основании событий.

Проверьте, что все необходимые поды созданы и работают.

## 11. Проверьте работу автомасштабирования KEDA

На завершающем этапе вы протестируете работу event-driven масштабирования через отправку сообщений и анализ работы Job.

1. Создайте тестовый под curl для взаимодействия с приложением:
kubectl run -it --rm curl-pod --image=curlimages/curl -- /bin/sh
2. Внутри curl-pod отправьте несколько POST-запросов на сервис для генерации событий:
curl -X POST "http://complex-app-keda-service/send?name=record1&content=content1"curl -X POST "http://complex-app-keda-service/send?name=record2&content=content2"curl -X POST "http://complex-app-keda-service/send?name=record3&content=content3"curl -X POST "http://complex-app-keda-service/send?name=record4&content=content4"curl -X POST "http://complex-app-keda-service/send?name=record5&content=content5"
3. Проверьте, что данные были добавлены в MongoDB:
curl "http://complex-app-keda-service/data"

Job-ресурсам потребуется некоторое время на запуск и выполнение, поэтому записи могут появиться в течение минуты.
4. Выйдите из curl-пода командой:
exit
5. Проверьте количество созданных Job:
kubectl get jobs

Убедитесь, что для каждого события KEDA запустила отдельный Job, реализуя event-driven масштабирование обработки.

Создайте тестовый под curl для взаимодействия с приложением:

```bash
kubectl run
-it
--rm
curl-pod
--image
=
curlimages/curl -- /bin/sh
```

Внутри curl-pod отправьте несколько POST-запросов на сервис для генерации событий:

```bash
curl
-X
POST
"http://complex-app-keda-service/send?name=record1&content=content1"
curl
-X
POST
"http://complex-app-keda-service/send?name=record2&content=content2"
curl
-X
POST
"http://complex-app-keda-service/send?name=record3&content=content3"
curl
-X
POST
"http://complex-app-keda-service/send?name=record4&content=content4"
curl
-X
POST
"http://complex-app-keda-service/send?name=record5&content=content5"
```

Проверьте, что данные были добавлены в MongoDB:

```bash
curl
"http://complex-app-keda-service/data"
```

Job-ресурсам потребуется некоторое время на запуск и выполнение, поэтому записи могут появиться в течение минуты.

Выйдите из curl-пода командой:

```bash
exit
```

Проверьте количество созданных Job:

```bash
kubectl get
jobs
```

Убедитесь, что для каждого события KEDA запустила отдельный Job, реализуя event-driven масштабирование обработки.

## Что дальше

В практической работе вы создали кластер Managed Kubernetes, установили KEDA в этом кластере и развернули в нем приложение, в котором реализовано event-driven масштабирование с помощью KEDA.
