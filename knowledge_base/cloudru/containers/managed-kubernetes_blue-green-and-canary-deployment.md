---
title: Продвинутые методики развертывания приложений Blue-Green и Canary в управляемом кластере Managed Kubernetes
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment
topic: containers
---
# Продвинутые методики развертывания приложений Blue-Green и Canary в управляемом кластере Managed Kubernetes

С помощью этого руководства вы научитесь работать с продвинутыми стратегиями развертывания контейнерных приложений Blue-Green Deployment и Canary Deployment в управляемом кластере Managed Kubernetes на платформе [Cloud.ru](https://cloud.ru/)Cloud.ru Evolution.

Blue-Green Deployment — это метод развертывания, использующий две идентичные среды: синюю — текущую и зеленую — новую.
Пока пользователи работают с синей средой, в зеленой разворачивается и тестируется обновление.
После проверки весь трафик мгновенно переключается на зеленую среду.
Это позволяет обновлять приложение без простоев и быстро откатываться в случае проблем.

Canary Deployment — это стратегия постепенного развертывания, при котором новая версия приложения сначала выпускается для небольшой группы пользователей.
Это позволяет протестировать работу обновления в реальных условиях с минимальным риском.
Если канареечная, то есть новая, версия показывает стабильность, развертывание постепенно расширяется на всех пользователей.
Такой подход обеспечивает контроль над рисками и позволяет быстро откатить изменения при обнаружении проблем.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

Шаги:

1. [Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution.
2. [Создайте виртуальную машину и установите Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте виртуальную машину и установите Docker.
3. [Соберите образ простого веб-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Соберите образ простого веб-приложения.
4. [Создайте приватный реестр в Artifact Registry и загрузите в него образ приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте приватный реестр в Artifact Registry и загрузите в него образ приложения.
5. [Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx.
6. [Разверните Blue-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Разверните Blue-приложение.
7. [Реализуйте стратегию Blue-Green](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Реализуйте стратегию Blue-Green.
8. [Реализуйте стратегию Canary](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Реализуйте стратегию Canary.

[Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution.

[Создайте виртуальную машину и установите Docker](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте виртуальную машину и установите Docker.

[Соберите образ простого веб-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Соберите образ простого веб-приложения.

[Создайте приватный реестр в Artifact Registry и загрузите в него образ приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте приватный реестр в Artifact Registry и загрузите в него образ приложения.

[Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx.

[Разверните Blue-приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Разверните Blue-приложение.

[Реализуйте стратегию Blue-Green](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Реализуйте стратегию Blue-Green.

[Реализуйте стратегию Canary](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)Реализуйте стратегию Canary.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/use-cases__web-server)Создайте группу безопасности с правилами, разрешающими доступ по портам 8080 и 8081 для внешнего IP-адреса локальной машины.
Узнайте адрес локальной машины через сервис https://www.myip.ru.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что у вас [достаточно прав](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/security)достаточно прав для создания реестра и загрузки артефактов в сервисе Artifact Registry.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/use-cases__web-server)Создайте группу безопасности с правилами, разрешающими доступ по портам 8080 и 8081 для внешнего IP-адреса локальной машины.
Узнайте адрес локальной машины через сервис https://www.myip.ru.

## 1. Сгенерируйте ключевую пару и загрузите публичный ключ SSH в облако Cloud.ru Evolution

1. [Сгенерируйте ключевую пару SSH](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару SSH.
2. [Загрузите публичный ключ в облако Cloud.ru Evolution](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичный ключ в облако Cloud.ru Evolution.

[Сгенерируйте ключевую пару SSH](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Сгенерируйте ключевую пару SSH.

[Загрузите публичный ключ в облако Cloud.ru Evolution](https://cloud.ru/docs/public-keys/ug/topics/guides__add-key-to-service)Загрузите публичный ключ в облако Cloud.ru Evolution.

## 2. Создайте виртуальную машину и установите Docker

1. [Создайте виртуальную машину](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте виртуальную машину с параметрами:

Гарантированная доля vCPU — 10%.
vCPU, шт. — 2.
RAM, ГБ — 4.
Загрузочный диск → Размер, ГБ — 30.
Сетевой интерфейс №1 — Подсеть с публичным IP.
Группы безопасности — группа, созданная перед началом работы.
Авторизация пользователя → Метод аутентификации — Публичный ключ и Пароль.

В списке виртуальных машин появится новая ВМ.
Примерно через минуту ее статус должен измениться на «Запущена».
2. [Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.
3. Установите Docker на ВМ.
Для этого в серийной консоли выполните команды:
sudo apt update -ysudo apt upgrade -ycurl -fsSL get.docker.com -o get-docker.sh && sh get-docker.shsudo groupadd dockersudo usermod -aG docker $USERnewgrp docker
4. Чтобы проверить, что Docker установлен и работает корректно, выполните команду:
docker version

[Создайте виртуальную машину](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте виртуальную машину с параметрами:

- Гарантированная доля vCPU — 10%.
- vCPU, шт. — 2.
- RAM, ГБ — 4.
- Загрузочный диск → Размер, ГБ — 30.
- Сетевой интерфейс №1 — Подсеть с публичным IP.
- Группы безопасности — группа, созданная перед началом работы.
- Авторизация пользователя → Метод аутентификации — Публичный ключ и Пароль.

Гарантированная доля vCPU — 10%.

vCPU, шт. — 2.

RAM, ГБ — 4.

Загрузочный диск → Размер, ГБ — 30.

Сетевой интерфейс №1 — Подсеть с публичным IP.

Группы безопасности — группа, созданная перед началом работы.

Авторизация пользователя → Метод аутентификации — Публичный ключ и Пароль.

В списке виртуальных машин появится новая ВМ.
Примерно через минуту ее статус должен измениться на «Запущена».

[Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.

Установите Docker на ВМ.
Для этого в серийной консоли выполните команды:

```bash
sudo
apt
update
-y
sudo
apt
upgrade
-y
curl
-fsSL
get.docker.com
-o
get-docker.sh
&&
sh
get-docker.sh
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

Чтобы проверить, что Docker установлен и работает корректно, выполните команду:

```bash
docker
version
```

## 3. Соберите образ простого веб-приложения

1. На ВМ создайте каталог с рабочим проектом deploy-lab:
mkdir ~/deploy-lab
2. В этом каталоге создайте еще два: blue-app и green-app:
mkdir ~/deploy-lab/blue-appmkdir ~/deploy-lab/green-app
3. В каталоге blue-app создайте файл index.html:
nano ~/deploy-lab/blue-app/index.html
4. В index.html добавьте код:
<!DOCTYPE html><html lang="ru"><head> <meta http-equiv="Cache-Control" content="no-cache"> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Синий квадрат</title> <style> body { margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0f8ff; font-family: Arial, sans-serif; } .blue-square { width: 250px; height: 250px; background-color: #0066ff; border-radius: 10px; box-shadow: 0 0 20px rgba(0, 102, 255, 0.5); display: flex; justify-content: center; align-items: center; color: white; font-size: 18px; font-weight: bold; text-align: center; } </style></head><body> <div class="blue-square"> Синяя версия 1.0<br> This is the stable version of the application. </div></body></html>
5. Создайте dockerfile:
nano ~/deploy-lab/blue-app/dockerfile
6. В dockerfile добавьте код:
FROM nginx:alpineCOPY index.html /usr/share/nginx/html/index.htmlRUN rm -f /usr/share/nginx/html/*.defaultEXPOSE 80
7. В каталоге green-app создайте файл index.html:
nano ~/deploy-lab/green-app/index.html
8. В index.html добавьте код:
<!DOCTYPE html><html lang="ru"><head> <meta http-equiv="Cache-Control" content="no-cache"> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Зеленый квадрат</title> <style> body { margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f0fff0; font-family: Arial, sans-serif; } .green-square { width: 250px; height: 250px; background-color: #00cc66; border-radius: 10px; box-shadow: 0 0 20px rgba(0, 204, 102, 0.5); display: flex; justify-content: center; align-items: center; color: white; font-size: 18px; font-weight: bold; text-align: center; } </style></head><body> <div class="green-square"> Зеленая версия 2.0<br> This is the new, updated version of the application! </div></body></html>
9. Создайте dockerfile:
nano ~/deploy-lab/green-app/dockerfile
10. В dockerfile добавьте код:
FROM nginx:alpineCOPY index.html /usr/share/nginx/html/index.htmlRUN rm -f /usr/share/nginx/html/*.defaultEXPOSE 80
11. Соберите образы приложений:
docker build -t blue-app:1.0 -f /home/<user>/deploy-lab/blue-app/dockerfile $HOME/deploy-lab/blue-app/docker build -t green-app:2.0 -f /home/<user>/deploy-lab/green-app/dockerfile $HOME/deploy-lab/green-app/

Где <user> — имя пользователя, которое указали при создании ВМ.
12. Запустите контейнеры:
docker run -d -p 8080:80 --name blue-container blue-app:1.0docker run -d -p 8081:80 --name green-container green-app:2.0

В адресную строку браузера введите по очереди адреса:

http://<public-ip>:8080 — приложение «Синий квадрат»;
http://<public-ip>:8081 — приложение «Зеленый квадрат».

Где <public-ip> — публичный IP-адрес, присвоенный ВМ при ее создании [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)на шаге 2.

На ВМ создайте каталог с рабочим проектом deploy-lab:

```bash
mkdir
~/deploy-lab
```

В этом каталоге создайте еще два: blue-app и green-app:

```bash
mkdir
~/deploy-lab/blue-app
mkdir
~/deploy-lab/green-app
```

В каталоге blue-app создайте файл index.html:

```bash
nano
~/deploy-lab/blue-app/index.html
```

В index.html добавьте код:

```bash
<
!
DOCTYPE html
>
<
html
lang
=
"ru"
>
<
head
>
<
meta http-equiv
=
"Cache-Control"
content
=
"no-cache"
>
<
meta
charset
=
"UTF-8"
>
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1.0"
>
<
title
>
Синий квадрат
<
/title
>
<
style
>
body
{
margin:
0
;
padding:
0
;
display: flex
;
justify-content: center
;
align-items: center
;
height: 100vh
;
background-color:
#f0f8ff;
font-family: Arial, sans-serif
;
}
.blue-square
{
width: 250px
;
height: 250px
;
background-color:
#0066ff;
border-radius: 10px
;
box-shadow:
0
0
20px rgba
(
0
,
102
,
255
,
0.5
)
;
display: flex
;
justify-content: center
;
align-items: center
;
color: white
;
font-size: 18px
;
font-weight: bold
;
text-align: center
;
}
<
/style
>
<
/head
>
<
body
>
<
div
class
=
"blue-square"
>
Синяя версия
1
.
0
<
br
>
This is the stable version of the application.
<
/div
>
<
/body
>
<
/html
>
```

Создайте dockerfile:

```bash
nano
~/deploy-lab/blue-app/dockerfile
```

В dockerfile добавьте код:

```bash
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
RUN
rm
-f
/usr/share/nginx/html/*.default
EXPOSE
80
```

В каталоге green-app создайте файл index.html:

```bash
nano
~/deploy-lab/green-app/index.html
```

В index.html добавьте код:

```bash
<
!
DOCTYPE html
>
<
html
lang
=
"ru"
>
<
head
>
<
meta http-equiv
=
"Cache-Control"
content
=
"no-cache"
>
<
meta
charset
=
"UTF-8"
>
<
meta
name
=
"viewport"
content
=
"width=device-width, initial-scale=1.0"
>
<
title
>
Зеленый квадрат
<
/title
>
<
style
>
body
{
margin:
0
;
padding:
0
;
display: flex
;
justify-content: center
;
align-items: center
;
height: 100vh
;
background-color:
#f0fff0;
font-family: Arial, sans-serif
;
}
.green-square
{
width: 250px
;
height: 250px
;
background-color:
#00cc66;
border-radius: 10px
;
box-shadow:
0
0
20px rgba
(
0
,
204
,
102
,
0.5
)
;
display: flex
;
justify-content: center
;
align-items: center
;
color: white
;
font-size: 18px
;
font-weight: bold
;
text-align: center
;
}
<
/style
>
<
/head
>
<
body
>
<
div
class
=
"green-square"
>
Зеленая версия
2
.
0
<
br
>
This is the new, updated version of the application
!
<
/div
>
<
/body
>
<
/html
>
```

Создайте dockerfile:

```bash
nano
~/deploy-lab/green-app/dockerfile
```

В dockerfile добавьте код:

```bash
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
RUN
rm
-f
/usr/share/nginx/html/*.default
EXPOSE
80
```

Соберите образы приложений:

```bash
docker
build
-t
blue-app:1.0
-f
/home/
<
user
>
/deploy-lab/blue-app/dockerfile
$HOME
/deploy-lab/blue-app/
docker
build
-t
green-app:2.0
-f
/home/
<
user
>
/deploy-lab/green-app/dockerfile
$HOME
/deploy-lab/green-app/
```

Где <user> — имя пользователя, которое указали при создании ВМ.

Запустите контейнеры:

```bash
docker
run
-d
-p
8080
:80
--name
blue-container blue-app:1.0
docker
run
-d
-p
8081
:80
--name
green-container green-app:2.0
```

В адресную строку браузера введите по очереди адреса:

- http://<public-ip>:8080 — приложение «Синий квадрат»;
- http://<public-ip>:8081 — приложение «Зеленый квадрат».

http://<public-ip>:8080 — приложение «Синий квадрат»;

http://<public-ip>:8081 — приложение «Зеленый квадрат».

Где <public-ip> — публичный IP-адрес, присвоенный ВМ при ее создании [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__blue-green-and-canary-deployment)на шаге 2.

## 4. Создайте приватный реестр в Artifact Registry и загрузите образ приложения

1. [Создайте приватный реестр и авторизуйтесь в нем](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Создайте приватный реестр и авторизуйтесь в нем.
Присвойте реестру название blue-green-canary-registry.
Название реестра должно быть уникальным.
2. Чтобы перетегировать ранее собранные образы и залить их в blue-green-canary-registry, выполните команды:
docker tag blue-app:1.0 blue-green-canary-registry.cr.cloud.ru/blue-app:1.0docker tag green-app:2.0 blue-green-canary-registry.cr.cloud.ru/green-app:2.0docker push blue-green-canary-registry.cr.cloud.ru/blue-app:1.0docker push blue-green-canary-registry.cr.cloud.ru/green-app:2.0

В результате этой операции образы blue-app и green-app появятся в Artifact Registry.

[Создайте приватный реестр и авторизуйтесь в нем](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/guides__auth)Создайте приватный реестр и авторизуйтесь в нем.

Присвойте реестру название blue-green-canary-registry.
Название реестра должно быть уникальным.

Чтобы перетегировать ранее собранные образы и залить их в blue-green-canary-registry, выполните команды:

```bash
docker
tag blue-app:1.0 blue-green-canary-registry.cr.cloud.ru/blue-app:1.0
docker
tag green-app:2.0 blue-green-canary-registry.cr.cloud.ru/green-app:2.0
docker
push blue-green-canary-registry.cr.cloud.ru/blue-app:1.0
docker
push blue-green-canary-registry.cr.cloud.ru/green-app:2.0
```

В результате этой операции образы blue-app и green-app появятся в Artifact Registry.

![../_images/s__repo-ar.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__repo-ar.webp)

## 5. Создайте кластер Managed Kubernetes и подключите плагин Ingress Nginx

1. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.
Кластер необходимо создавать в той же VPC, что и ВМ.
Остальные параметры можно оставить по умолчанию.
При создании группы узлов укажите следующие параметры:

Гарантированная доля vCPU, % — 30.
CPU, шт. — 2.
RAM, ГБ — 4.
Объем хранилища — 30.
Количество узлов — 2.

Создание кластера занимает примерно пять минут.
2. В кластер [установите Ingress Nginx](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)установите Ingress Nginx.
3. [Подключитесь к кластеру с ВМ](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру с ВМ.

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.

Кластер необходимо создавать в той же VPC, что и ВМ.
Остальные параметры можно оставить по умолчанию.

При создании группы узлов укажите следующие параметры:

- Гарантированная доля vCPU, % — 30.
- CPU, шт. — 2.
- RAM, ГБ — 4.
- Объем хранилища — 30.
- Количество узлов — 2.

Гарантированная доля vCPU, % — 30.

CPU, шт. — 2.

RAM, ГБ — 4.

Объем хранилища — 30.

Количество узлов — 2.

Создание кластера занимает примерно пять минут.

В кластер [установите Ingress Nginx](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)установите Ingress Nginx.

[Подключитесь к кластеру с ВМ](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру с ВМ.

## 6. Разверните Blue-приложение

1. В каталоге deploy-lab создайте манифест deploy-myapp-blue-v1.yaml:
cd ~/deploy-labnano deploy-myapp-blue-v1.yaml
2. Скопируйте в deploy-myapp-blue-v1.yaml код манифеста:
apiVersion: apps/v1kind: Deploymentmetadata: name: blue-appspec: replicas: 3 selector: matchLabels: app: demo-app template: metadata: labels: app: demo-app version: v1 spec: containers: - name: web image: blue-green-canary-registry.cr.cloud.ru/blue-app:1.0 ports: - containerPort: 80

Где blue-green-canary-registry.cr.cloud.ru/blue-app:1.0 — путь до образа, который был загружен в Artifact Registry.
3. В этом же каталоге создайте файл svc-myapp-blue.yaml:
nano svc-myapp-blue.yaml
4. Скопируйте в файл svc-myapp-blue.yaml код манифеста:
# Сервис для основного приложения blue (v1)apiVersion: v1kind: Servicemetadata: name: blue-app-servicespec: selector: app: demo-app version: v1 # Добавляя этот лейбл, мы маршрутизируем трафик только на деплоймент myapp-blue ports: - protocol: TCP port: 80 targetPort: 80 type: ClusterIP # Внутренний сервис для доступа изнутри кластера
5. В этом же каталоге создайте файл ingress-myapp.yaml с содержимым:
# Этот Ingress будет направлять внешний трафик к нашему сервисуapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: demo-app-ingress annotations: nginx.ingress.kubernetes.io/rewrite-target: /spec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: blue-app-service port: number: 80
6. Чтобы создать ресурсы Kubernetes, выполните команды:
kubectl apply -f deploy-myapp-blue-v1.yamlkubectl apply -f svc-myapp-blue.yamlkubectl apply -f ingress-myapp.yaml
7. Проверьте создание ресурсов:
kubectl get svc,pods,ingress

В каталоге deploy-lab создайте манифест deploy-myapp-blue-v1.yaml:

```bash
cd
~/deploy-lab
nano
deploy-myapp-blue-v1.yaml
```

Скопируйте в deploy-myapp-blue-v1.yaml код манифеста:

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
blue
-
app
spec
:
replicas
:
3
selector
:
matchLabels
:
app
:
demo
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
demo
-
app
version
:
v1
spec
:
containers
:
-
name
:
web
image
:
blue
-
green
-
canary
-
registry.cr.cloud.ru/blue
-
app
:
1.0
ports
:
-
containerPort
:
80
```

Где blue-green-canary-registry.cr.cloud.ru/blue-app:1.0 — путь до образа, который был загружен в Artifact Registry.

В этом же каталоге создайте файл svc-myapp-blue.yaml:

```bash
nano svc
-
myapp
-
blue.yaml
```

Скопируйте в файл svc-myapp-blue.yaml код манифеста:

```bash
# Сервис для основного приложения blue (v1)
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
blue
-
app
-
service
spec
:
selector
:
app
:
demo
-
app
version
:
v1
# Добавляя этот лейбл, мы маршрутизируем трафик только на деплоймент myapp-blue
ports
:
-
protocol
:
TCP
port
:
80
targetPort
:
80
type
:
ClusterIP
# Внутренний сервис для доступа изнутри кластера
```

В этом же каталоге создайте файл ingress-myapp.yaml с содержимым:

```bash
# Этот Ingress будет направлять внешний трафик к нашему сервису
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
demo
-
app
-
ingress
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
blue
-
app
-
service
port
:
number
:
80
```

Чтобы создать ресурсы Kubernetes, выполните команды:

```bash
kubectl apply
-f
deploy-myapp-blue-v1.yaml
kubectl apply
-f
svc-myapp-blue.yaml
kubectl apply
-f
ingress-myapp.yaml
```

Проверьте создание ресурсов:

```bash
kubectl get svc,pods,ingress
```

На этом шаге мы организовали подачу трафика на стабильную версию приложения demo-app извне через Ingress-контроллер.

Чтобы проверить работоспособность приложения, определите внешний IP Ingress-контроллера.
Для этого используйте команду:

```bash
kubectl get svc
-
n=ingress
```

В результате вы увидите информацию по External IP:

```bash
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT
(
S
)
AGE
ingress-nginx-controller LoadBalancer
10.104
.209.33 XX.XXX.XXX.XX
80
:30652/TCP,443:30796/TCP 7h
```

Введите в браузере http://<EXTERNAL-IP> и увидите отображаемую версию приложения.

![../_images/s__blue-square.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__blue-square.webp)

## 7. Реализуйте стратегию Blue-Green

1. В каталоге deploy-lab создайте YAML-манифест Green-приложения:
nano deploy-myapp-green-v2.yaml
2. Скопируйте в deploy-myapp-green-v2.yaml код манифеста:
# Версия приложения на которую будем обновляться green (v2)apiVersion: apps/v1kind: Deploymentmetadata: name: green-app # Важно: другое имя!spec: replicas: 3 selector: matchLabels: app: demo-app template: metadata: labels: app: demo-app version: v2 spec: containers: - name: web image: blue-green-canary-registry.cr.cloud.ru/green-app:2.0 # лейбл новой версии v2 ports: - containerPort: 80
3. В каталоге deploy-lab создайте svc-myapp-green.yaml:
nano svc-myapp-green.yaml
4. Скопируйте в svc-myapp-green.yaml код манифеста:
# Сервис для приложения, на которое будем переключаться - green (v2)apiVersion: v1kind: Servicemetadata: name: green-app-servicespec: selector: app: demo-app version: v2 # Добавляя этот лейбл, мы маршрутизируем трафик на сборку green (v2) ports: - protocol: TCP port: 80 targetPort: 80 type: ClusterIP # Внутренний сервис для доступа изнутри кластера
5. Чтобы создать ресурсы Kubernetes, выполните команды:
kubectl apply -f deploy-myapp-green-v2.yamlkubectl apply -f svc-myapp-green.yaml
6. Проверьте создание ресурсов:
kubectl get svc,pods
7. Чтобы переключить трафик с версии приложения Blue (v1) на версию приложения Green (v2), внесите изменения в манифест ingress-myapp.yaml:
# Этот Ingress будет направлять трафик на основной сервис blue (v1) и в дальнейшем на green (v2) после обновленияapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: demo-app-ingress annotations: nginx.ingress.kubernetes.io/rewrite-target: /spec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: green-app-service # Тут мы меняем имя сервиса и теперь трафик будет идти на сборку приложения green (v2) port: number: 80
8. Примените внесенные изменения в манифесте:
kubectl apply -f ingress-myapp.yaml

Теперь трафик идет на сборку приложения Green (v2).
9. Чтобы проверить изменения, обновите окно браузера, где раньше отображалось приложение с синим квадратом.
Теперь отображается зеленый квадрат.

В каталоге deploy-lab создайте YAML-манифест Green-приложения:

```bash
nano
deploy-myapp-green-v2.yaml
```

Скопируйте в deploy-myapp-green-v2.yaml код манифеста:

```bash
# Версия приложения на которую будем обновляться green (v2)
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
green
-
app
# Важно: другое имя!
spec
:
replicas
:
3
selector
:
matchLabels
:
app
:
demo
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
demo
-
app
version
:
v2
spec
:
containers
:
-
name
:
web
image
:
blue
-
green
-
canary
-
registry.cr.cloud.ru/green
-
app
:
2.0
# лейбл новой версии v2
ports
:
-
containerPort
:
80
```

В каталоге deploy-lab создайте svc-myapp-green.yaml:

```bash
nano
svc-myapp-green.yaml
```

Скопируйте в svc-myapp-green.yaml код манифеста:

```bash
# Сервис для приложения, на которое будем переключаться - green (v2)
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
green
-
app
-
service
spec
:
selector
:
app
:
demo
-
app
version
:
v2
# Добавляя этот лейбл, мы маршрутизируем трафик на сборку green (v2)
ports
:
-
protocol
:
TCP
port
:
80
targetPort
:
80
type
:
ClusterIP
# Внутренний сервис для доступа изнутри кластера
```

Чтобы создать ресурсы Kubernetes, выполните команды:

```bash
kubectl apply
-f
deploy-myapp-green-v2.yaml
kubectl apply
-f
svc-myapp-green.yaml
```

Проверьте создание ресурсов:

```bash
kubectl get svc,pods
```

Чтобы переключить трафик с версии приложения Blue (v1) на версию приложения Green (v2), внесите изменения в манифест ingress-myapp.yaml:

```bash
# Этот Ingress будет направлять трафик на основной сервис blue (v1) и в дальнейшем на green (v2) после обновления
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
demo
-
app
-
ingress
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
green
-
app
-
service
# Тут мы меняем имя сервиса и теперь трафик будет идти на сборку приложения green (v2)
port
:
number
:
80
```

Примените внесенные изменения в манифесте:

```bash
kubectl apply
-f
ingress-myapp.yaml
```

Теперь трафик идет на сборку приложения Green (v2).

Чтобы проверить изменения, обновите окно браузера, где раньше отображалось приложение с синим квадратом.
Теперь отображается зеленый квадрат.

![../_images/s__green-square.webp](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__green-square.webp)

Таким образом, мы осуществили переключение с одной версии приложения Blue (v1) на другую Green (v2).
В этом и заключается стратегия развертывания Blue-Green.

## 8. Реализуйте стратегию Canary

1. На ВМ в каталоге deploy-lab создайте файл deploy-canary.yaml с тем же образом, что и версия Green v2 — blue-green-canary-registry.cr.cloud.ru/green-app:2.0:
cd ~/deploy-labnano deploy-canary.yaml
2. Скопируйте в deploy-canary.yaml код манифеста:
# Версия canary - сюда будет постепенно перенаправляться весь трафикapiVersion: apps/v1kind: Deploymentmetadata: name: demo-app-canaryspec: replicas: 1 # Одна реплика для canary selector: matchLabels: app: demo-app template: metadata: labels: app: demo-app version: canary-v2 # Уникальная версия для canary spec: containers: - name: web image: blue-green-canary-registry.cr.cloud.ru/green-app:2.0 # оставляем тот же образ green-app 2.0 ports: - containerPort: 80
3. В каталоге deploy-lab создайте файл svc-canary.yaml:
nano svc-canary.yaml
4. Скопируйте в svc-canary.yaml код манифеста:
apiVersion: v1kind: Servicemetadata: name: canary-servicespec: selector: app: demo-app version: canary-v2 # добавляя этот лейбл мы маршрутизируем трафик только на деплоймент canary ports: - protocol: TCP port: 80 targetPort: 80 type: ClusterIP # Внутренний сервис для доступа изнутри кластера
5. В каталоге deploy-lab создайте файл ingress-canary.yaml:
nano ingress-canary.yaml
6. Скопируйте в ingress-canary.yaml код манифеста:
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниямиapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: ingress-canary annotations: nginx.ingress.kubernetes.io/rewrite-target: / nginx.ingress.kubernetes.io/canary: "true" nginx.ingress.kubernetes.io/canary-weight: "10" # Направляем 10% трафика на canaryspec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: canary-service port: number: 80
7. Чтобы создать ресурсы Kubernetes, выполните команды:
kubectl apply -f deploy-canary.yamlkubectl apply -f svc-canary.yamlkubectl apply -f ingress-canary.yaml
8. Проверьте создание ресурсов:
kubectl get svc,pods,ingress
9. Чтобы убедиться, что трафик обеспечен на основное приложение Blue (v1), измените Service в ingress-myapp.yaml:
# Этот Ingress будет направлять внешний трафик к нашему сервисуapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: demo-app-ingress annotations: nginx.ingress.kubernetes.io/rewrite-target: /spec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: blue-app-service port: number: 80
10. Примените манифест:
kubectl apply -f ingress-myapp.yaml

Благодаря такой архитектуре большая часть трафика по-прежнему идет на синюю версию приложения, но 10% трафика теперь идет на зеленое приложение.
Чтобы проверить это, введите в адресную строку браузера IP-адрес Ingress и несколько раз обновите браузер.
Вы увидите, что примерно в 10% случаев отображается зеленая версия приложения, а в остальных случаях — синяя.
То есть через Ingress-Canary мы задали правило распределения трафика в обе версии приложения: 90% в синее и 10% в зеленое.
Меняя настройки Ingress-Canary, можно регулировать объем трафика, идущий на Canary-приложение.
11. Чтобы направить 50% трафика на версию приложения Canary, измените правило Ingress-Canary в ingress-canary.yaml:
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниямиapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: ingress-canary annotations: nginx.ingress.kubernetes.io/rewrite-target: / nginx.ingress.kubernetes.io/canary: "true" nginx.ingress.kubernetes.io/canary-weight: "50" # Направляем 50% трафика на canaryspec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: canary-service port: number: 80
12. Примените изменение:
kubectl apply -f ingress-canary.yaml
13. Чтобы проверить перенаправление трафика, введите в адресную строку браузера IP-адрес Ingress и несколько раз обновите браузер.
Вы увидите, что теперь примерно в половине случаев отображается зеленая версия приложения и половине — синяя.
14. Чтобы направить 100% трафика на версию приложения Canary, измените правило Ingress-Canary в ingress-canary.yaml:
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниямиapiVersion: networking.k8s.io/v1kind: Ingressmetadata: name: ingress-canary annotations: nginx.ingress.kubernetes.io/rewrite-target: / nginx.ingress.kubernetes.io/canary: "true" nginx.ingress.kubernetes.io/canary-weight: "100" # Направляем весь трафик на canaryspec: ingressClassName: nginx rules: - http: paths: - path: / pathType: Prefix backend: service: name: canary-service port: number: 80
15. Примените изменение:
kubectl apply -f ingress-canary.yaml

На ВМ в каталоге deploy-lab создайте файл deploy-canary.yaml с тем же образом, что и версия Green v2 — blue-green-canary-registry.cr.cloud.ru/green-app:2.0:

```bash
cd
~/deploy-lab
nano
deploy-canary.yaml
```

Скопируйте в deploy-canary.yaml код манифеста:

```bash
# Версия canary - сюда будет постепенно перенаправляться весь трафик
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
demo
-
app
-
canary
spec
:
replicas
:
1
# Одна реплика для canary
selector
:
matchLabels
:
app
:
demo
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
demo
-
app
version
:
canary
-
v2
# Уникальная версия для canary
spec
:
containers
:
-
name
:
web
image
:
blue
-
green
-
canary
-
registry.cr.cloud.ru/green
-
app
:
2.0
# оставляем тот же образ green-app 2.0
ports
:
-
containerPort
:
80
```

В каталоге deploy-lab создайте файл svc-canary.yaml:

```bash
nano
svc-canary.yaml
```

Скопируйте в svc-canary.yaml код манифеста:

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
canary
-
service
spec
:
selector
:
app
:
demo
-
app
version
:
canary
-
v2
# добавляя этот лейбл мы маршрутизируем трафик только на деплоймент canary
ports
:
-
protocol
:
TCP
port
:
80
targetPort
:
80
type
:
ClusterIP
# Внутренний сервис для доступа изнутри кластера
```

В каталоге deploy-lab создайте файл ingress-canary.yaml:

```bash
nano
ingress-canary.yaml
```

Скопируйте в ingress-canary.yaml код манифеста:

```bash
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниями
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
ingress
-
canary
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
nginx.ingress.kubernetes.io/canary
:
"true"
nginx.ingress.kubernetes.io/canary-weight
:
"10"
# Направляем 10% трафика на canary
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
canary
-
service
port
:
number
:
80
```

Чтобы создать ресурсы Kubernetes, выполните команды:

```bash
kubectl apply
-f
deploy-canary.yaml
kubectl apply
-f
svc-canary.yaml
kubectl apply
-f
ingress-canary.yaml
```

Проверьте создание ресурсов:

```bash
kubectl get svc,pods,ingress
```

Чтобы убедиться, что трафик обеспечен на основное приложение Blue (v1), измените Service в ingress-myapp.yaml:

```bash
# Этот Ingress будет направлять внешний трафик к нашему сервису
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
demo
-
app
-
ingress
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
blue
-
app
-
service
port
:
number
:
80
```

Примените манифест:

```bash
kubectl apply
-f
ingress-myapp.yaml
```

Благодаря такой архитектуре большая часть трафика по-прежнему идет на синюю версию приложения, но 10% трафика теперь идет на зеленое приложение.
Чтобы проверить это, введите в адресную строку браузера IP-адрес Ingress и несколько раз обновите браузер.
Вы увидите, что примерно в 10% случаев отображается зеленая версия приложения, а в остальных случаях — синяя.

То есть через Ingress-Canary мы задали правило распределения трафика в обе версии приложения: 90% в синее и 10% в зеленое.

Меняя настройки Ingress-Canary, можно регулировать объем трафика, идущий на Canary-приложение.

Чтобы направить 50% трафика на версию приложения Canary, измените правило Ingress-Canary в ingress-canary.yaml:

```bash
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниями
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
ingress
-
canary
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
nginx.ingress.kubernetes.io/canary
:
"true"
nginx.ingress.kubernetes.io/canary-weight
:
"50"
# Направляем 50% трафика на canary
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
canary
-
service
port
:
number
:
80
```

Примените изменение:

```bash
kubectl apply
-f
ingress-canary.yaml
```

Чтобы проверить перенаправление трафика, введите в адресную строку браузера IP-адрес Ingress и несколько раз обновите браузер.
Вы увидите, что теперь примерно в половине случаев отображается зеленая версия приложения и половине — синяя.

Чтобы направить 100% трафика на версию приложения Canary, измените правило Ingress-Canary в ingress-canary.yaml:

```bash
# Этот Ingress будет управлять распределением трафика между основным и канареечным развертываниями
apiVersion
:
networking.k8s.io/v1
kind
:
Ingress
metadata
:
name
:
ingress
-
canary
annotations
:
nginx.ingress.kubernetes.io/rewrite-target
:
/
nginx.ingress.kubernetes.io/canary
:
"true"
nginx.ingress.kubernetes.io/canary-weight
:
"100"
# Направляем весь трафик на canary
spec
:
ingressClassName
:
nginx
rules
:
-
http
:
paths
:
-
path
:
/
pathType
:
Prefix
backend
:
service
:
name
:
canary
-
service
port
:
number
:
80
```

Примените изменение:

```bash
kubectl apply
-f
ingress-canary.yaml
```

Теперь при обновлении браузера мы видим только Canary-версию приложения.

Таким образом, мы обновили наше приложение, подавая сначала трафик одновременно на текущую версию приложения Blue и новую версию Canary.
В итоге мы перенесли 100% трафика на приложение Canary, тем самым реализовав стратегию развертывания Canary.

## Результат

Вы научились работать с продвинутыми стратегиями развертывания контейнерных приложений Blue-Green Deployment и Canary Deployment в управляемом кластере Managed Kubernetes на платформе [Cloud.ru](https://cloud.ru/)Cloud.ru Evolution.
Эти методы позволяют обновлять приложения более управляемо и безопасно, сводя к минимуму простои и риски, связанные с внедрением новых версий.
