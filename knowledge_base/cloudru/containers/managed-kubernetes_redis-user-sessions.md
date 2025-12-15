---
title: Подключение Managed Redis® к сервисам в кластере Managed Kubernetes
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions
topic: containers
---
# Подключение Managed Redis® к сервисам в кластере Managed Kubernetes

С помощью этого руководства вы сконфигурируете Managed Redis® для хранения пользовательских сессий в сервисе, работающем в кластере Managed Kubernetes на платформе [Cloud.ru](https://cloud.ru/)Cloud.ru Evolution.

Для организации взаимодействия между Managed Kubernetes и сервисом Managed Redis® будет использована виртуальная сеть VPC и подсети.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.
- [sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.

[sNAT-шлюзы](https://cloud.ru/docs/gateways/ug/index)sNAT-шлюзы — сервис управления сетевыми шлюзами облака.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Разверните необходимые ресурсы в облаке.
2. [Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера.
3. [Подключитесь с созданной ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Подключитесь с созданной ВМ к кластеру Managed Kubernetes.
4. [Разверните приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Разверните приложение в Managed Kubernetes.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Разверните необходимые ресурсы в облаке.

[Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Создайте приватный репозиторий в Artifact Registry и загрузите в него образ контейнера.

[Подключитесь с созданной ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Подключитесь с созданной ВМ к кластеру Managed Kubernetes.

[Разверните приложение в Managed Kubernetes](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__redis-user-sessions)Разверните приложение в Managed Kubernetes.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и [загрузите](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)загрузите SSH-ключ в облако.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и [загрузите](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)загрузите SSH-ключ в облако.

## 1. Разверните необходимые ресурсы в облаке

1. [Создайте VPC](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте VPC с названием redis-kubernetes-lab-vpc.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

Название: redis-kubernetes-lab-subnet.
VPC: redis-kubernetes-lab-vpc.
Адрес: 10.10.1.0/24.

Убедитесь, что в личном кабинете на странице сервиса VPC:

отображается сеть redis-kubernetes-lab-vpc;
количество подсетей — 1;
подсеть redis-kubernetes-lab-subnet доступна.
3. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: redis-kubernetes-lab-jump-server.
Публичные → Образ: Ubuntu 22.04.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.
Подсеть с публичным IP.
VPC: redis-kubernetes-lab-vpc.
Подсеть: redis-kubernetes-lab-subnet.
Группы безопасности: SSH-access_ru.AZ-1.
Если такой группы безопасности нет, [создайте ее](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)создайте ее и [разрешите подключение по SSH](https://cloud.ru/docs/security-groups/ug/topics/use-cases__remote-access)разрешите подключение по SSH.
Метод аутентификации: публичный ключ и пароль.
Публичный ключ: публичная часть вашего SSH-ключа из сервиса «SSH-ключи».
Пароль: ваш пароль.
Имя хоста: redis-kubernetes-lab-jump-server.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина redis-kubernetes-lab-jump-server в статусе «Запущена».
4. [Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

Название кластера: redis-kubernetes-lab.
Версия Redis: v7.2.11.
vCPU: 2.
RAM: 4.
Сохранять данные на диске: включено.
Подсеть: redis-kubernetes-lab-subnet.

Убедитесь, что в личном кабинете на странице сервиса «Managed Redis» отображается кластер redis-kubernetes-lab в статусе «Доступен».
5. [Создайте sNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте sNAT-шлюз со следующими параметрами:

Название: redis-kubernetes-lab.
VPC: redis-kubernetes-lab-vpc.

Убедитесь, что в личном кабинете на странице сервиса «sNAT-шлюзы» отображается шлюз redis-kubernetes-lab в статусе «Создан».
6. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/quickstart)Создайте кластер Managed Kubernetes со следующими параметрами:

Название: redis-kubernetes-lab.
Зона доступности: совпадает с зоной доступности остальных сервисов.
Адрес подсети мастер-узлов: redis-kubernetes-lab-subnet.
Публичный IP-адрес: включено.
Группы узлов –> Адрес подсети узлов: redis-kubernetes-lab-subnet.

[Создайте VPC](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте VPC с названием redis-kubernetes-lab-vpc.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

- Название: redis-kubernetes-lab-subnet.
- VPC: redis-kubernetes-lab-vpc.
- Адрес: 10.10.1.0/24.

Название: redis-kubernetes-lab-subnet.

VPC: redis-kubernetes-lab-vpc.

Адрес: 10.10.1.0/24.

Убедитесь, что в личном кабинете на странице сервиса VPC:

- отображается сеть redis-kubernetes-lab-vpc;
- количество подсетей — 1;
- подсеть redis-kubernetes-lab-subnet доступна.

отображается сеть redis-kubernetes-lab-vpc;

количество подсетей — 1;

подсеть redis-kubernetes-lab-subnet доступна.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: redis-kubernetes-lab-jump-server.
- Публичные → Образ: Ubuntu 22.04.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.
- Подсеть с публичным IP.
- VPC: redis-kubernetes-lab-vpc.
- Подсеть: redis-kubernetes-lab-subnet.
- Группы безопасности: SSH-access_ru.AZ-1.
Если такой группы безопасности нет, [создайте ее](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)создайте ее и [разрешите подключение по SSH](https://cloud.ru/docs/security-groups/ug/topics/use-cases__remote-access)разрешите подключение по SSH.
- Метод аутентификации: публичный ключ и пароль.
- Публичный ключ: публичная часть вашего SSH-ключа из сервиса «SSH-ключи».
- Пароль: ваш пароль.
- Имя хоста: redis-kubernetes-lab-jump-server.

Название: redis-kubernetes-lab-jump-server.

Публичные → Образ: Ubuntu 22.04.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

Подсеть с публичным IP.

VPC: redis-kubernetes-lab-vpc.

Подсеть: redis-kubernetes-lab-subnet.

Группы безопасности: SSH-access_ru.AZ-1.
Если такой группы безопасности нет, [создайте ее](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)создайте ее и [разрешите подключение по SSH](https://cloud.ru/docs/security-groups/ug/topics/use-cases__remote-access)разрешите подключение по SSH.

Метод аутентификации: публичный ключ и пароль.

Публичный ключ: публичная часть вашего SSH-ключа из сервиса «SSH-ключи».

Пароль: ваш пароль.

Имя хоста: redis-kubernetes-lab-jump-server.

Убедитесь, что в личном кабинете на странице сервиса «Виртуальные машины» отображается виртуальная машина redis-kubernetes-lab-jump-server в статусе «Запущена».

[Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

- Название кластера: redis-kubernetes-lab.
- Версия Redis: v7.2.11.
- vCPU: 2.
- RAM: 4.
- Сохранять данные на диске: включено.
- Подсеть: redis-kubernetes-lab-subnet.

Название кластера: redis-kubernetes-lab.

Версия Redis: v7.2.11.

vCPU: 2.

RAM: 4.

Сохранять данные на диске: включено.

Подсеть: redis-kubernetes-lab-subnet.

Убедитесь, что в личном кабинете на странице сервиса «Managed Redis» отображается кластер redis-kubernetes-lab в статусе «Доступен».

[Создайте sNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/guides__create-gw)Создайте sNAT-шлюз со следующими параметрами:

- Название: redis-kubernetes-lab.
- VPC: redis-kubernetes-lab-vpc.

Название: redis-kubernetes-lab.

VPC: redis-kubernetes-lab-vpc.

Убедитесь, что в личном кабинете на странице сервиса «sNAT-шлюзы» отображается шлюз redis-kubernetes-lab в статусе «Создан».

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/quickstart)Создайте кластер Managed Kubernetes со следующими параметрами:

- Название: redis-kubernetes-lab.
- Зона доступности: совпадает с зоной доступности остальных сервисов.
- Адрес подсети мастер-узлов: redis-kubernetes-lab-subnet.
- Публичный IP-адрес: включено.
- Группы узлов –> Адрес подсети узлов: redis-kubernetes-lab-subnet.

Название: redis-kubernetes-lab.

Зона доступности: совпадает с зоной доступности остальных сервисов.

Адрес подсети мастер-узлов: redis-kubernetes-lab-subnet.

Публичный IP-адрес: включено.

Группы узлов –> Адрес подсети узлов: redis-kubernetes-lab-subnet.

Убедитесь, что в личном кабинете на странице сервиса «Managed Kubernetes» отображается кластер redis-kubernetes-lab в статусе «Запущено».

## 2. Создайте приватный реестр в Artifact Registry и загрузите в него образ контейнера

1. [Создайте приватный реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте приватный реестр Artifact Registry.
2. [Пройдите аутентификацию](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию.
3. Соберите и загрузите образ в реестр Artifact Registry:
Используйте наше демонстрационное приложение [evo-managed-redis-sessions-management-lab](https://github.com/cloud-ru/evo-managed-redis-sessions-management-lab)evo-managed-redis-sessions-management-lab.

Для сборки и тегирования образа на локальном компьютере в Docker CLI или любом удобном терминале выполните команду:
docker build --tag <registry_name>.cr.cloud.ru/evo-managed-redis-sessions-management-lab https://github.com/cloud-ru/evo-managed-redis-sessions-management-lab.git#main --platform linux/amd64

Для загрузки образа выполните команду:
docker push <registry_name>.cr.cloud.ru/evo-managed-redis-sessions-management-lab:latest

Убедитесь, что в реестре появился репозиторий evo-managed-redis-sessions-management-lab с артефактами образа.

[Создайте приватный реестр Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__registry-create)Создайте приватный реестр Artifact Registry.

[Пройдите аутентификацию](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Пройдите аутентификацию.

Соберите и загрузите образ в реестр Artifact Registry:

Используйте наше демонстрационное приложение [evo-managed-redis-sessions-management-lab](https://github.com/cloud-ru/evo-managed-redis-sessions-management-lab)evo-managed-redis-sessions-management-lab.

1. Для сборки и тегирования образа на локальном компьютере в Docker CLI или любом удобном терминале выполните команду:
docker build --tag <registry_name>.cr.cloud.ru/evo-managed-redis-sessions-management-lab https://github.com/cloud-ru/evo-managed-redis-sessions-management-lab.git#main --platform linux/amd64
2. Для загрузки образа выполните команду:
docker push <registry_name>.cr.cloud.ru/evo-managed-redis-sessions-management-lab:latest

Убедитесь, что в реестре появился репозиторий evo-managed-redis-sessions-management-lab с артефактами образа.

Для сборки и тегирования образа на локальном компьютере в Docker CLI или любом удобном терминале выполните команду:

```bash
docker
build
--tag
<
registry_name
>
.cr.cloud.ru/evo-managed-redis-sessions-management-lab https://github.com/cloud-ru/evo-managed-redis-sessions-management-lab.git
#main --platform linux/amd64
```

Для загрузки образа выполните команду:

```bash
docker
push
<
registry_name
>
.cr.cloud.ru/evo-managed-redis-sessions-management-lab:latest
```

Убедитесь, что в реестре появился репозиторий evo-managed-redis-sessions-management-lab с артефактами образа.

## 3. Подключитесь с созданной ВМ к кластеру Managed Kubernetes

1. [Подключитесь к ВМ через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к ВМ через серийную консоль.
2. [Активируйте сетевой интерфейс](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)Активируйте сетевой интерфейс.
3. [Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.
4. [На ВМ установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)На ВМ установите kubectl.
5. [На ВМ установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)На ВМ установите cloudlogin.
6. [Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.

[Подключитесь к ВМ через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к ВМ через серийную консоль.

[Активируйте сетевой интерфейс](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)Активируйте сетевой интерфейс.

[Подключитесь к ВМ по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к ВМ по SSH.

[На ВМ установите kubectl](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__kubectl-install)На ВМ установите kubectl.

[На ВМ установите cloudlogin](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__download-cloudlogin)На ВМ установите cloudlogin.

[Подключитесь с ВМ к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь с ВМ к кластеру Managed Kubernetes.

## 4. Разверните приложение в Managed Kubernetes

1. Создайте .env и откройте его для редактирования:
nano .env
2. Добавьте содержимое файла конфигурации:
REDIS_URL=redis://:<REDIS_PASSWORD>@<REDIS_IP>:6379

Где:

<REDIS_IP> — IP-адрес сервиса Managed Redis®.
<REDIS_PASSWORD> — пароль от кластера Managed Redis®.
3. Создайте объект из файла конфигурации:
kubectl create secret generic containerapp-secret --from-env-file=.env
4. Создайте containerapp-deployment.yaml и откройте его для редактирования:
nano containerapp-deployment.yaml
5. Добавьте содержимое манифеста:
apiVersion: apps/v1kind: Deploymentmetadata: name: containerappspec: replicas: 1 selector: matchLabels: app: lab-app template: metadata: labels: app: lab-app spec: containers: - name: containerapp image: <registry_name>.cr.cloud.ru/evo-managed-redis-sessions-management-lab:latest ports: - containerPort: 3000 imagePullPolicy: Always
 envFrom: - secretRef: name: containerapp-secret

Где <registry_name> — название реестра Artifact Registry.
6. Примените манифест при помощи команды:
kubectl apply -f containerapp-deployment.yaml
7. Чтобы создать внешний балансировщик нагрузки для доступа к приложению из интернета, создайте containerapp-lb.yaml и откройте его для редактирования:
nano containerapp-lb.yaml
8. Добавьте содержимое манифеста:
apiVersion: v1kind: Servicemetadata: name: containerapp-lb annotations: loadbalancer.mk8s.cloud.ru/type: "external" loadbalancer.mk8s.cloud.ru/health-check-timeout-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-interval-seconds: "5" loadbalancer.mk8s.cloud.ru/health-check-unhealthy-threshold-count: "4" loadbalancer.mk8s.cloud.ru/health-check-healthy-threshold-count: "4"spec: type: LoadBalancer selector: app: lab-app ports: - port: 80 name: http targetPort: 3000
9. Создайте балансировщик нагрузки при помощи команды:
kubectl apply -f containerapp-lb.yaml
10. Посмотрите созданные сервисы в кластере при помощи команды:
kubectl get svc

Создайте .env и откройте его для редактирования:

```bash
nano
.env
```

Добавьте содержимое файла конфигурации:

```bash
REDIS_URL
=
redis://:
<
REDIS_PASSWORD
>
@
<
REDIS_IP
>
:6379
```

Где:

- <REDIS_IP> — IP-адрес сервиса Managed Redis®.
- <REDIS_PASSWORD> — пароль от кластера Managed Redis®.

<REDIS_IP> — IP-адрес сервиса Managed Redis®.

<REDIS_PASSWORD> — пароль от кластера Managed Redis®.

Создайте объект из файла конфигурации:

```bash
kubectl create secret generic containerapp-secret --from-env-file
=
.env
```

Создайте containerapp-deployment.yaml и откройте его для редактирования:

```bash
nano
containerapp-deployment.yaml
```

Добавьте содержимое манифеста:

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
.cr.cloud.ru/evo
-
managed
-
redis
-
sessions
-
management
-
lab
:
latest
ports
:
-
containerPort
:
3000
imagePullPolicy
:
Always
envFrom
:
-
secretRef
:
name
:
containerapp
-
secret
```

Где <registry_name> — название реестра Artifact Registry.

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

Добавьте содержимое манифеста:

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
http
targetPort
:
3000
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
Это займет 5–10 минут.

После получения IP-адреса проверьте доступность приложения — введите в адресную строку браузера: http://<EXTERNAL-IP>.
Попробуйте зарегистрироваться в приложении и войти с вашим email и паролем.

## Результат

Вы сконфигурировали Managed Redis® как хранилище сессий и связали его с сервисом, развернутом в кластере Managed Kubernetes.
