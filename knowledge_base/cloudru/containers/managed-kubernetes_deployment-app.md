---
title: Запуск контейнерного приложения в кластере Managed Kubernetes
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app
topic: containers
---
# Запуск контейнерного приложения в кластере Managed Kubernetes

С помощью этого руководства вы соберете и загрузите демонстрационный образ контейнерного приложения в Artifact Registry, создадите кластер Managed Kubernetes и развернете приложение из загруженного образа в кластере Managed Kubernetes.

Для развертывания вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry — сервис для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облачной архитектуры Cloud.ru.
- [sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальной машине и кластеру Managed Kubernetes с локального устройства.
Для выполнения сценария потребуется создать два публичных IP-адреса.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry — сервис для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облачной архитектуры Cloud.ru.

[sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к виртуальной машине и кластеру Managed Kubernetes с локального устройства.

Для выполнения сценария потребуется создать два публичных IP-адреса.

Шаги:

1. [Сгенерируйте SSH-ключ и загрузите его публичную часть в облако Cloud.ru Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Сгенерируйте SSH-ключ и загрузите его публичную часть в облако Cloud.ru Evolution
2. [Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте виртуальную машину
3. [Создайте sNAT-шлюз](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте sNAT-шлюз
4. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте кластер Managed Kubernetes
5. [Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера
6. [Подключитесь с созданной ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Подключитесь с созданной ВМ к кластеру Managed Kubernetes
7. [Разверните приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Разверните приложение в Managed Kubernetes

[Сгенерируйте SSH-ключ и загрузите его публичную часть в облако Cloud.ru Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Сгенерируйте SSH-ключ и загрузите его публичную часть в облако Cloud.ru Evolution

[Создайте виртуальную машину](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте виртуальную машину

[Создайте sNAT-шлюз](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте sNAT-шлюз

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте кластер Managed Kubernetes

[Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера

[Подключитесь с созданной ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Подключитесь с созданной ВМ к кластеру Managed Kubernetes

[Разверните приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deployment-app)Разверните приложение в Managed Kubernetes

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Сгенерируйте SSH-ключ и загрузите его публичную часть в облако Cloud.ru Evolution

1. [Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару.
2. [Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

[Сгенерируйте ключевую пару](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару.

[Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичную часть SSH-ключа в облако Cloud.ru Evolution.

## 2. Создайте виртуальную машину

1. Выполните шаги инструкции [по созданию виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/quickstart)по созданию виртуальной машины в облаке Cloud.ru Evolution до шага 4 раздела «Порядок работы».
2. Подключите виртуальную машину к подсети: в разделе Сетевые настройки нажмите Подключить к сети.
3. В открывшемся боковом меню оставьте значения по умолчанию для полей VPC, Подсети и Группы безопасности.
4. Нажмите Подключить.
По умолчанию значение группы безопасности — SSH-access_ru.AZ-<availability-zone-number>.
Такая настройка позволит подключаться к ВМ по протоколу SSH на TCP-порт 22.
5. Чтобы у виртуальной машины был доступ в интернет, оставьте активной опцию Назначить публичный IP.
6. Выберите тип публичного IP-адреса: Плавающий.
7. В разделе Авторизация пользователя выберите оба метода аутентификации пользователя — Публичный ключ и Пароль.
8. В выпадающем меню Публичный ключ выберите загруженный ранее публичный SSH-ключ.
9. Придумайте пароль и введите в поле Пароль.
10. Нажмите Создать.

Выполните шаги инструкции [по созданию виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/quickstart)по созданию виртуальной машины в облаке Cloud.ru Evolution до шага 4 раздела «Порядок работы».

Подключите виртуальную машину к подсети: в разделе Сетевые настройки нажмите Подключить к сети.

В открывшемся боковом меню оставьте значения по умолчанию для полей VPC, Подсети и Группы безопасности.

Нажмите Подключить.

По умолчанию значение группы безопасности — SSH-access_ru.AZ-<availability-zone-number>.
Такая настройка позволит подключаться к ВМ по протоколу SSH на TCP-порт 22.

Чтобы у виртуальной машины был доступ в интернет, оставьте активной опцию Назначить публичный IP.

Выберите тип публичного IP-адреса: Плавающий.

В разделе Авторизация пользователя выберите оба метода аутентификации пользователя — Публичный ключ и Пароль.

В выпадающем меню Публичный ключ выберите загруженный ранее публичный SSH-ключ.

Придумайте пароль и введите в поле Пароль.

Нажмите Создать.

На главном экране сервиса «Виртуальные машины» в списке появится новая ВМ.
Примерно через минуту ее статус должен измениться на «Запущена».

## 3. Создайте sNAT-шлюз

Рабочие узлы кластера Managed Kubernetes используют sNAT-шлюз для выхода в интернет.
Создайте его:

1. Перейдите [в личный кабинет](https://console.cloud.ru/)в личный кабинет.
2. На верхней панели слева нажмите , выберите Сеть → sNAT-шлюз и нажмите Создать шлюз.
3. Выберите зону доступности и заполните описание.
4. Нажмите Создать.

Перейдите [в личный кабинет](https://console.cloud.ru/)в личный кабинет.

На верхней панели слева нажмите , выберите Сеть → sNAT-шлюз и нажмите Создать шлюз.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Выберите зону доступности и заполните описание.

Нажмите Создать.

Для sNAT-шлюза потребуется публичный IP-адрес.
В случае необходимости вы можете [расширить квоту](https://cloud.ru/docs/virtual-machines/ug/topics/faq__quota)расширить квоту по запросу [в техническую поддержку](https://cloud.ru/docs/kubernetes-evolution/ug/contacts/technical-support)в техническую поддержку.

## 4. Создайте кластер Managed Kubernetes

1. На верхней панели слева нажмите , выберите Контейнеры → Managed Kubernetes и нажмите Подключить.
Подключение сервиса занимает примерно пять минут.
2. На странице сервиса Managed Kubernetes нажмите Создать кластер.
3. На шаге Общие параметры оставьте все значения по умолчанию и нажмите Продолжить.
4. На шаге Сеть включите опцию Публичный IP-адрес, остальные параметры оставьте по умолчанию и нажмите Продолжить.
Публичный IP — опциональный параметр для кластера Managed Kubernetes.
Он необходим, чтобы подключаться к кластеру с локального устройства, а не через виртуальную машину.
5. На шаге Группы узлов нажмите Добавить группу узлов, в появившемся меню настройки создаваемой группы узлов, оставьте значения по умолчанию и нажмите Продолжить.
6. На шаге Интеграция оставьте все значения по умолчанию и нажмите Создать.
Создание кластера занимает примерно пять минут.

На верхней панели слева нажмите , выберите Контейнеры → Managed Kubernetes и нажмите Подключить.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Подключение сервиса занимает примерно пять минут.

На странице сервиса Managed Kubernetes нажмите Создать кластер.

На шаге Общие параметры оставьте все значения по умолчанию и нажмите Продолжить.

На шаге Сеть включите опцию Публичный IP-адрес, остальные параметры оставьте по умолчанию и нажмите Продолжить.

Публичный IP — опциональный параметр для кластера Managed Kubernetes.
Он необходим, чтобы подключаться к кластеру с локального устройства, а не через виртуальную машину.

На шаге Группы узлов нажмите Добавить группу узлов, в появившемся меню настройки создаваемой группы узлов, оставьте значения по умолчанию и нажмите Продолжить.

На шаге Интеграция оставьте все значения по умолчанию и нажмите Создать.

Создание кластера занимает примерно пять минут.

## 5. Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера

1. [Создайте приватный реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте приватный реестр Artifact Registry.
2. [Пройдите аутентификацию](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию.
3. Соберите и загрузите образ в репозиторий Artifact Registry.
Используйте наше демонстрационное приложение react-hello-world.

Для сборки и тегирования образа на локальном компьютере выполните команду в Docker CLI или любом удобном терминале:
docker build --tag <registry_name>.cr.cloud.ru/react-hello-world https://gitverse.ru/cloudru/evo-containerapp-react-sample.git#master --platform linux/amd64

Для загрузки образа выполните команду:
docker push <registry_name>.cr.cloud.ru/react-hello-world:latest

Убедитесь, что в реестре появился репозиторий react-hello-world с артефактами образа.

[Создайте приватный реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте приватный реестр Artifact Registry.

[Пройдите аутентификацию](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию.

Соберите и загрузите образ в репозиторий Artifact Registry.

Используйте наше демонстрационное приложение react-hello-world.

1. Для сборки и тегирования образа на локальном компьютере выполните команду в Docker CLI или любом удобном терминале:
docker build --tag <registry_name>.cr.cloud.ru/react-hello-world https://gitverse.ru/cloudru/evo-containerapp-react-sample.git#master --platform linux/amd64
2. Для загрузки образа выполните команду:
docker push <registry_name>.cr.cloud.ru/react-hello-world:latest

Убедитесь, что в реестре появился репозиторий react-hello-world с артефактами образа.

Для сборки и тегирования образа на локальном компьютере выполните команду в Docker CLI или любом удобном терминале:

```bash
docker
build
--tag
<
registry_name
>
.cr.cloud.ru/react-hello-world https://gitverse.ru/cloudru/evo-containerapp-react-sample.git
#master --platform linux/amd64
```

Для загрузки образа выполните команду:

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/react-hello-world:latest
```

Убедитесь, что в реестре появился репозиторий react-hello-world с артефактами образа.

## 6. Подключитесь с созданной ВМ к кластеру Managed Kubernetes

1. [Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.
2. [На ВМ установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)На ВМ установите kubectl.
3. [На ВМ установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)На ВМ установите cloudlogin.
4. [Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.

[Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.

[На ВМ установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)На ВМ установите kubectl.

[На ВМ установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)На ВМ установите cloudlogin.

[Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.

## 7. Разверните приложение в Managed Kubernetes

1. Создайте containerapp-deployment.yaml и откройте его для редактирования:
nano containerapp-deployment.yaml
2. Вставьте содержимое манифеста:
apiVersion: apps/v1kind: Deploymentmetadata: name: containerappspec: replicas: 1 selector: matchLabels: app: lab-app template: metadata: labels: app: lab-app spec: containers: - name: containerapp image: <registry_name>.cr.cloud.ru/react-hello-world:latest ports: - containerPort: 80 imagePullPolicy: Always
3. Примените манифест при помощи команды:
kubectl apply -f containerapp-deployment.yaml
4. Чтобы создать внешний балансировщик нагрузки для доступа к приложению из интернета, создайте containerapp-lb.yaml и откройте его для редактирования:
nano containerapp-lb.yaml
5. Вставьте содержимое манифеста:
apiVersion: v1kind: Servicemetadata: name: containerapp-lb annotations: loadbalancer.mk8s.cloud.ru/type: "external" loadbalancer.mk8s.cloud.ru/health-check-timeout-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-interval-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-unhealthy-threshold-count: "4" loadbalancer.mk8s.cloud.ru/health-check-healthy-threshold-count: "4"spec: type: LoadBalancer selector: app: lab-app ports: - port: 80 name: cloudru-port
6. Создайте балансировщик нагрузки при помощи команды:
kubectl apply -f containerapp-lb.yaml
7. Посмотрите созданные сервисы в кластере при помощи команды:
kubectl get svc

Создайте containerapp-deployment.yaml и откройте его для редактирования:

```bash
nano
containerapp-deployment.yaml
```

Вставьте содержимое манифеста:

```bash
apiVersion
:
apps/v1
kind
:
Deployment
metadata
:
name
:
containerapp
spec
:
replicas
:
1
selector
:
matchLabels
:
app
:
lab
-
app
template
:
metadata
:
labels
:
app
:
lab
-
app
spec
:
containers
:
-
name
:
containerapp
image
:
<registry_name
>
.cr.cloud.ru/react
-
hello
-
world
:
latest
ports
:
-
containerPort
:
80
imagePullPolicy
:
Always
```

Примените манифест при помощи команды:

```bash
kubectl apply
-f
containerapp-deployment.yaml
```

Чтобы создать внешний балансировщик нагрузки для доступа к приложению из интернета, создайте containerapp-lb.yaml и откройте его для редактирования:

```bash
nano
containerapp-lb.yaml
```

Вставьте содержимое манифеста:

```bash
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
containerapp
-
lb
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
spec
:
type
:
LoadBalancer
selector
:
app
:
lab
-
app
ports
:
-
port
:
80
name
:
cloudru
-
port
```

Создайте балансировщик нагрузки при помощи команды:

```bash
kubectl apply
-f
containerapp-lb.yaml
```

Посмотрите созданные сервисы в кластере при помощи команды:

```bash
kubectl get svc
```

После создания внешнего балансировщика нагрузки платформа начнет создание объекта LoadBalancer.
После того как балансировщик будет создан и получит публичный IP, IP-адрес отобразится в поле EXTERNAL-IP.

Подождите примерно 5–10 минут и проверьте, получил ли балансировщик нагрузки публичный IP.

После получения IP-адреса проверьте доступность приложения — введите в адресную строку браузера: http://<EXTERNAL-IP>.

![../_images/app-go.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/app-go.png)

## Результат

Вы развернули кластер Managed Kubernetes и запустили в нем приложение из приватного реестра Artifact Registry.
