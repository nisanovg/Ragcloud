---
title: Развертывание кластера Managed Kubernetes с помощью Terraform
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform
topic: containers
---
# Развертывание кластера Managed Kubernetes с помощью Terraform

С помощью этого руководства вы научитесь автоматически развертывать инфраструктуру в облаке [Cloud.ru](https://cloud.ru/)Cloud.ru Evolution при помощи инструмента Terraform на примере создания кластера Managed Kubernetes.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Terraform](https://developer.hashicorp.com/terraform)Terraform — инструмент для управления IaC.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Terraform](https://developer.hashicorp.com/terraform)Terraform — инструмент для управления IaC.

Шаги:

1. [Установите и настройте Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Установите и настройте Terraform.
2. [Настройте конфигурационный файл main.tf](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Настройте конфигурационный файл main.tf.
3. [Создайте кластер Managed Kubernetes с помощью Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Создайте кластер Managed Kubernetes с помощью Terraform.
4. [Проверьте создание кластера и подключитесь к нему](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Проверьте создание кластера и подключитесь к нему.

[Установите и настройте Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Установите и настройте Terraform.

[Настройте конфигурационный файл main.tf](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Настройте конфигурационный файл main.tf.

[Создайте кластер Managed Kubernetes с помощью Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Создайте кластер Managed Kubernetes с помощью Terraform.

[Проверьте создание кластера и подключитесь к нему](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__deploying-cluster-using-terraform)Проверьте создание кластера и подключитесь к нему.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте ключ доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Создайте ключ доступа и сохраните Key ID (логин) и Key Secret (пароль).
Это данные для аутентификации и подключения к сервисам [Cloud.ru](https://cloud.ru/)Cloud.ru вашего проекта.
3. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт для интеграции с другими сервисами облака Evolution вашего проекта.
4. Установите инструмент для работы с кодом, например Visual Studio Code, или используйте стандартный терминал, например bash, cmd или PowerShell.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте ключ доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Создайте ключ доступа и сохраните Key ID (логин) и Key Secret (пароль).
Это данные для аутентификации и подключения к сервисам [Cloud.ru](https://cloud.ru/)Cloud.ru вашего проекта.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт для интеграции с другими сервисами облака Evolution вашего проекта.

Установите инструмент для работы с кодом, например Visual Studio Code, или используйте стандартный терминал, например bash, cmd или PowerShell.

## 1. Установите и настройте Terraform

1. [Установите Terraform](https://developer.hashicorp.com/terraform/install)Установите Terraform.
2. [Установите Terraform-провайдер](https://cloud.ru/docs/terraform-evolution/ug/topics/quickstart)Установите Terraform-провайдер.
Шаг с командой terraform init пока пропустите.
3. Проверьте, что установка прошла корректно:
terraform --version

Должна отобразиться версия Terraform.

[Установите Terraform](https://developer.hashicorp.com/terraform/install)Установите Terraform.

[Установите Terraform-провайдер](https://cloud.ru/docs/terraform-evolution/ug/topics/quickstart)Установите Terraform-провайдер.

Шаг с командой terraform init пока пропустите.

Проверьте, что установка прошла корректно:

```bash
terraform
--version
```

Должна отобразиться версия Terraform.

## 2. Настройте конфигурационный файл main.tf

1. Создайте локальную папку для проекта.
2. В папке проекта создайте файл main.tf и добавьте в него код:
terraform { required_providers { cloudru = { source = "cloud.ru/cloudru/cloud" version = "1.5.1" } }}
provider "cloudru" { project_id = "<your-project-id>" auth_key_id = "<your-key-id>" auth_secret = "<your-key-secret>" iam_endpoint = "iam.api.cloud.ru:443" k8s_endpoint = "mk8s.api.cloud.ru:443"}

Где:

<your-project-id> — [идентификатор проекта](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__project-id)идентификатор проекта.
<your-key-id> — логин ключа доступа, который вы создали перед началом работы.
<your-key-secret> — пароль ключа доступа, который вы создали перед началом работы.
3. Сохраните файл main.tf.
С помощью него вы задали конфигурацию для провайдера Terraform и точки обращения к сервисам [Cloud.ru](https://cloud.ru/)Cloud.ru.
4. В терминале перейдите в папку проекта и выполните команду:
terraform init

Если все прошло успешно, вы увидите похожий текст:
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to seeany changes that are required for your infrastructure. All Terraform commandsshould now work.
If you ever set or change modules or backend configuration for Terraform,rerun this command to reinitialize your working directory. If you forget, othercommands will detect it and remind you to do so if necessary.

Создайте локальную папку для проекта.

В папке проекта создайте файл main.tf и добавьте в него код:

```bash
terraform
{
required_providers
{
cloudru
=
{
source
=
"cloud.ru/cloudru/cloud"
version
=
"1.5.1"
}
}
}
provider
"cloudru"
{
project_id
=
"<your-project-id>"
auth_key_id
=
"<your-key-id>"
auth_secret
=
"<your-key-secret>"
iam_endpoint
=
"iam.api.cloud.ru:443"
k8s_endpoint
=
"mk8s.api.cloud.ru:443"
}
```

Где:

- <your-project-id> — [идентификатор проекта](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__project-id)идентификатор проекта.
- <your-key-id> — логин ключа доступа, который вы создали перед началом работы.
- <your-key-secret> — пароль ключа доступа, который вы создали перед началом работы.

<your-project-id> — [идентификатор проекта](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__project-id)идентификатор проекта.

<your-key-id> — логин ключа доступа, который вы создали перед началом работы.

<your-key-secret> — пароль ключа доступа, который вы создали перед началом работы.

Сохраните файл main.tf.
С помощью него вы задали конфигурацию для провайдера Terraform и точки обращения к сервисам [Cloud.ru](https://cloud.ru/)Cloud.ru.

В терминале перейдите в папку проекта и выполните команду:

```bash
terraform init
```

Если все прошло успешно, вы увидите похожий текст:

```bash
Terraform has been successfully initialized
!
You may now begin working with Terraform. Try running
"terraform plan"
to see
any changes that are required
for
your infrastructure. All Terraform commands
should now work.
If you ever
set
or change modules or backend configuration
for
Terraform,
rerun this
command
to reinitialize your working directory. If you forget, other
commands will detect it and remind you to
do
so
if
necessary.
```

## 3. Создайте кластер Managed Kubernetes с помощью Terraform

На этом шаге вы создадите файл конфигурации и примените его.

1. В каталоге проекта создайте файл конфигурации kuber.tf и добавьте в него код:
data "cloudru_k8s_zone_flavors" "k8s_zones" {}
# Creating a K8s cluster / master nodes
resource "cloudru_k8s_cluster" "kuber" { name = "tf-cluster" control_plane = { count = 1 type = "MASTER_TYPE_SMALL" version = "v1.32.5" zones = [data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones.*.name, "ru.AZ-1")].id] }
 network_configuration = { services_subnet_cidr = "10.0.0.0/20" nodes_subnet_cidr = "192.168.20.0/24" pods_subnet_cidr = "172.16.0.0/12" kube_api_internet = true }}
# Creating a pool of workers
resource "cloudru_k8s_nodepool" "kuber_nodepool" { cluster_id = cloudru_k8s_cluster.kuber.id name = "tf-worker-pool" zone = data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones[index(data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones.*.name, "ru.AZ-1")].id scale_policy = { fixed_scale = { count = 1 } }
 hardware_compute = { disk_size = 10 disk_type = "DISK_TYPE_SSD_NVME" flavor_id = data.cloudru_k8s_zone_flavors.k8s_zones.flavors[index(data.cloudru_k8s_zone_flavors.k8s_zones.flavors.*.name, "lowcost10-2-4")].id }
 nodes_network_configuration = { nodes_subnet_cidr = "192.168.123.0/24" }
 depends_on = [ cloudru_k8s_cluster.kuber ]}

С помощью этой конфигурации вы создадите [новые ресурсы](https://github.com/cloud-ru/evo-terraform/tree/main/examples/k8s)новые ресурсы:

Кластер Managed Kubernetes на базе одного мастер-узла.
Одну группу узлов.
2. Сохраните файл kuber.tf.
3. В терминале перейдите в папку проекта и выполните команду:
terraform validate
4. Если все прошло успешно, вы увидите похожий текст:
Success! The configuration is valid.

При необходимости устраните ошибки в конфигурации.
5. Выполните команду:
terraform apply
6. Убедитесь, что Terraform планирует добавить два ресурса, введите «yes» и нажмите Enter.
Если развертывание прошло успешно, вы увидите следующее сообщение:
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

В каталоге проекта создайте файл конфигурации kuber.tf и добавьте в него код:

```bash
data
"cloudru_k8s_zone_flavors"
"k8s_zones"
{
}
# Creating a K8s cluster / master nodes
resource
"cloudru_k8s_cluster"
"kuber"
{
name
=
"tf-cluster"
control_plane
=
{
count
=
1
type
=
"MASTER_TYPE_SMALL"
version
=
"v1.32.5"
zones
=
[
data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones
[
index
(
data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones.*.name,
"ru.AZ-1"
)
]
.id
]
}
network_configuration
=
{
services_subnet_cidr
=
"10.0.0.0/20"
nodes_subnet_cidr
=
"192.168.20.0/24"
pods_subnet_cidr
=
"172.16.0.0/12"
kube_api_internet
=
true
}
}
# Creating a pool of workers
resource
"cloudru_k8s_nodepool"
"kuber_nodepool"
{
cluster_id
=
cloudru_k8s_cluster.kuber.id
name
=
"tf-worker-pool"
zone
=
data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones
[
index
(
data.cloudru_k8s_zone_flavors.k8s_zones.availability_zones.*.name,
"ru.AZ-1"
)
]
.id
scale_policy
=
{
fixed_scale
=
{
count
=
1
}
}
hardware_compute
=
{
disk_size
=
10
disk_type
=
"DISK_TYPE_SSD_NVME"
flavor_id
=
data.cloudru_k8s_zone_flavors.k8s_zones.flavors
[
index
(
data.cloudru_k8s_zone_flavors.k8s_zones.flavors.*.name,
"lowcost10-2-4"
)
]
.id
}
nodes_network_configuration
=
{
nodes_subnet_cidr
=
"192.168.123.0/24"
}
depends_on
=
[
cloudru_k8s_cluster.kuber
]
}
```

С помощью этой конфигурации вы создадите [новые ресурсы](https://github.com/cloud-ru/evo-terraform/tree/main/examples/k8s)новые ресурсы:

- Кластер Managed Kubernetes на базе одного мастер-узла.
- Одну группу узлов.

Кластер Managed Kubernetes на базе одного мастер-узла.

Одну группу узлов.

Сохраните файл kuber.tf.

В терминале перейдите в папку проекта и выполните команду:

```bash
terraform validate
```

Если все прошло успешно, вы увидите похожий текст:

```bash
Success
!
The configuration is valid.
```

При необходимости устраните ошибки в конфигурации.

Выполните команду:

```bash
terraform apply
```

Убедитесь, что Terraform планирует добавить два ресурса, введите «yes» и нажмите Enter.

Если развертывание прошло успешно, вы увидите следующее сообщение:

```bash
Apply complete
!
Resources:
2
added,
0
changed,
0
destroyed.
```

## 3. Проверьте создание кластера и подключитесь к нему

1. Перейдите [в личный кабинет](https://console.cloud.ru/)в личный кабинет Cloud.ru Evolution и проверьте, что все созданные ресурсы отображаются.
2. [Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру и выполните команду:
kubectl cluster-info

Команда выведет информацию о вашем кластере.

Перейдите [в личный кабинет](https://console.cloud.ru/)в личный кабинет Cloud.ru Evolution и проверьте, что все созданные ресурсы отображаются.

![../_images/s__cluster-terraform.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__cluster-terraform.png)

[Подключитесь к кластеру](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру и выполните команду:

```bash
kubectl cluster-info
```

Команда выведет информацию о вашем кластере.

## Результат

Вы познакомились с механизмом развертывания облачных ресурсов Terraform и научились работать с инструментами в рамках концепции Infrastructure as Code.
