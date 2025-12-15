---
title: Настройка site-to-site VPN с помощью strongSwan
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn
topic: compute
---
# Настройка site-to-site VPN с помощью strongSwan

С помощью этого руководства вы настроите сетевую связность между инфраструктурой в облаке Cloud.ru Evolution и некоторой удаленной стороной.
На практике в качестве удаленной стороны может выступать, например, сетевая инфраструктура в офисе или в другом облаке.

Для организации защищенного соединения вы настроите [IPsec](https://datatracker.ietf.org/doc/html/rfc6071)IPsec-туннель с помощью ПО [strongSwan](https://strongswan.org/)strongSwan, где в качестве одной из сторон выступает инфраструктура в облаке Cloud.ru Evolution.
Виртуальная машина в облаке используется как VPN-шлюз, через который другие машины из этого облака отправляют трафик в удаленную подсеть.
Такой туннель позволяет безопасно передавать трафик между приватными сетями через интернет.

В качестве удаленной вы развернете аналогичную инфраструктуру на платформе Cloud.ru Advanced.

![../_images/schm__site-to-site-vpn.svg](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/schm__site-to-site-vpn.svg)

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- strongSwan — программное решение с открытым исходным кодом для создания защищенных VPN-соединений по протоколу IPsec.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

strongSwan — программное решение с открытым исходным кодом для создания защищенных VPN-соединений по протоколу IPsec.

Шаги:

1. [Разверните инфраструктуру на стороне Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Разверните инфраструктуру на стороне Evolution.
2. [Разверните инфраструктуру на стороне Advanced](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Разверните инфраструктуру на стороне Advanced.
3. [Добавьте правила в группу безопасности облачного VPN-шлюза](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Добавьте правила в группу безопасности облачного VPN-шлюза.
4. [Настройте VPN-шлюзы](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Настройте VPN-шлюзы.
5. [Настройте маршрутизацию](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Настройте маршрутизацию.
6. [Проверьте сетевую связность](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Проверьте сетевую связность.

[Разверните инфраструктуру на стороне Evolution](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Разверните инфраструктуру на стороне Evolution.

[Разверните инфраструктуру на стороне Advanced](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Разверните инфраструктуру на стороне Advanced.

[Добавьте правила в группу безопасности облачного VPN-шлюза](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Добавьте правила в группу безопасности облачного VPN-шлюза.

[Настройте VPN-шлюзы](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Настройте VPN-шлюзы.

[Настройте маршрутизацию](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Настройте маршрутизацию.

[Проверьте сетевую связность](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__site-to-site-vpn)Проверьте сетевую связность.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что для вашей учетной записи достаточно прав на проект.
При необходимости [настройте права](https://cloud.ru/docs/administration/ug/topics/guides__employees)настройте права или запросите их у администратора.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что для вашей учетной записи достаточно прав на проект.
При необходимости [настройте права](https://cloud.ru/docs/administration/ug/topics/guides__employees)настройте права или запросите их у администратора.

## 1. Разверните инфраструктуру на стороне Evolution

На этом шаге в облаке Evolution вы создадите и подготовите виртуальную сеть, подсеть, группу безопасности и две виртуальные машины.

1. [Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием cloud-vpc.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

Название — cloud-subnet.
VPC — cloud-vpc.
Зона доступности — ru.AZ-1.
Адрес — 172.16.0.0/24.

Скопируйте и сохраните адрес подсети: он потребуется для дальнейшей настройки.
3. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием cloud-sg в зоне доступности ru.AZ-1 и добавьте в нее правило исходящего трафика:
 ПротоколПортТип адресатаАдресатЛюбойОставьте пустымIP-адрес0.0.0.0/0
После создания удаленного VPN-шлюза на платформе Advanced в эту группу необходимо добавить правила для входящего трафика.
4. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — cloud-gateway.
Зона доступности — ru.AZ-1
Образ — на вкладке Маркетплейс выберите образ «strongSwan».
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
VPC — cloud-vpc.
Подсеть — cloud-subnet.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте группу cloud-sg.
Имя пользователя — cloud-user.
Метод аутентификации — Пароль.
Пароль — задайте пароль пользователя.

Виртуальная машина будет выполнять роль облачного VPN-шлюза, который принимает трафик от клиентских ВМ и направляет его в удаленную подсеть.
5. В строке ВМ cloud-gateway скопируйте и сохраните адреса из столбцов Внутренний IP и Публичный IP: они потребуются для дальнейшей настройки.
6. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — cloud-vm.
Зона доступности — ru.AZ-1
Образ — на вкладке Публичные выберите Ubuntu 22.04.
Сетевой интерфейс — выберите тип Подсеть.
VPC — cloud-vpc.
Подсеть — cloud-subnet.
Группы безопасности — добавьте группу cloud-sg.
Логин — client.
Метод аутентификации — Пароль.
Пароль — задайте пароль пользователя.

Виртуальная машина будет выполнять роль клиента, который отправляет трафик в удаленную подсеть через облачный VPN-шлюз.
7. В строке ВМ cloud-vm скопируйте и сохраните адрес из столбца Внутренний IP: он потребуется для дальнейшей настройки.
8. На сетевом интерфейсе облачного VPN-шлюза отключите проверку адресов источника и назначения.

На странице сервиса «Виртуальные машины» выберите виртуальную машину cloud-gateway.
Перейдите на вкладку Сетевые параметры.
В правом верхнем углу блока нужного сетевого интерфейса нажмите и выберите Свойства.
Отключите опцию Проверка адреса источника/назначения.
Подтвердите отключение.

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте виртуальную сеть с названием cloud-vpc.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название — cloud-subnet.
- VPC — cloud-vpc.
- Зона доступности — ru.AZ-1.
- Адрес — 172.16.0.0/24.

Название — cloud-subnet.

VPC — cloud-vpc.

Зона доступности — ru.AZ-1.

Адрес — 172.16.0.0/24.

Скопируйте и сохраните адрес подсети: он потребуется для дальнейшей настройки.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием cloud-sg в зоне доступности ru.AZ-1 и добавьте в нее правило исходящего трафика:

Протокол

Порт

Тип адресата

Адресат

Любой

Оставьте пустым

IP-адрес

0.0.0.0/0

После создания удаленного VPN-шлюза на платформе Advanced в эту группу необходимо добавить правила для входящего трафика.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — cloud-gateway.
- Зона доступности — ru.AZ-1
- Образ — на вкладке Маркетплейс выберите образ «strongSwan».
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- VPC — cloud-vpc.
- Подсеть — cloud-subnet.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте группу cloud-sg.
- Имя пользователя — cloud-user.
- Метод аутентификации — Пароль.
- Пароль — задайте пароль пользователя.

Название — cloud-gateway.

Зона доступности — ru.AZ-1

Образ — на вкладке Маркетплейс выберите образ «strongSwan».

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

VPC — cloud-vpc.

Подсеть — cloud-subnet.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте группу cloud-sg.

Имя пользователя — cloud-user.

Метод аутентификации — Пароль.

Пароль — задайте пароль пользователя.

Виртуальная машина будет выполнять роль облачного VPN-шлюза, который принимает трафик от клиентских ВМ и направляет его в удаленную подсеть.

В строке ВМ cloud-gateway скопируйте и сохраните адреса из столбцов Внутренний IP и Публичный IP: они потребуются для дальнейшей настройки.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — cloud-vm.
- Зона доступности — ru.AZ-1
- Образ — на вкладке Публичные выберите Ubuntu 22.04.
- Сетевой интерфейс — выберите тип Подсеть.
- VPC — cloud-vpc.
- Подсеть — cloud-subnet.
- Группы безопасности — добавьте группу cloud-sg.
- Логин — client.
- Метод аутентификации — Пароль.
- Пароль — задайте пароль пользователя.

Название — cloud-vm.

Зона доступности — ru.AZ-1

Образ — на вкладке Публичные выберите Ubuntu 22.04.

Сетевой интерфейс — выберите тип Подсеть.

VPC — cloud-vpc.

Подсеть — cloud-subnet.

Группы безопасности — добавьте группу cloud-sg.

Логин — client.

Метод аутентификации — Пароль.

Пароль — задайте пароль пользователя.

Виртуальная машина будет выполнять роль клиента, который отправляет трафик в удаленную подсеть через облачный VPN-шлюз.

В строке ВМ cloud-vm скопируйте и сохраните адрес из столбца Внутренний IP: он потребуется для дальнейшей настройки.

На сетевом интерфейсе облачного VPN-шлюза отключите проверку адресов источника и назначения.

1. На странице сервиса «Виртуальные машины» выберите виртуальную машину cloud-gateway.
2. Перейдите на вкладку Сетевые параметры.
3. В правом верхнем углу блока нужного сетевого интерфейса нажмите и выберите Свойства.
4. Отключите опцию Проверка адреса источника/назначения.
5. Подтвердите отключение.

На странице сервиса «Виртуальные машины» выберите виртуальную машину cloud-gateway.

Перейдите на вкладку Сетевые параметры.

В правом верхнем углу блока нужного сетевого интерфейса нажмите и выберите Свойства.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Отключите опцию Проверка адреса источника/назначения.

Подтвердите отключение.

## 2. Разверните инфраструктуру на стороне Advanced

На этом шаге в облаке Advanced вы создадите и подготовите виртуальную сеть, подсеть, группу безопасности и две виртуальные машины.

1. [Создайте сеть VPC и подсеть](https://cloud.ru/docs/vpc/ug/topics/managing-networks__create-vpc-network)Создайте сеть VPC и подсеть со следующими параметрами:

В блоке Basic Information:

Name — remote-vpc.
IPv4 CIDR Block — 10.0.0.0/8-24.
Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.

В блоке Subnet Setting:

Subnet Name — remote-subnet.
IPv4 CIDR Block — 10.0.0.0/24.
Сохраните адрес подсети — он потребуется для дальнейшей настройки.
2. [Создайте группу безопасности](https://cloud.ru/docs/vpc/ug/topics/security-groups__managing-groups__create)Создайте группу безопасности со следующими параметрами:

Name — remote-sg.
Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.
Template — Fast-add rule.
3. [Добавьте правила в группу безопасности](https://cloud.ru/docs/vpc/ug/topics/security-groups__managing-security-group-rules__create)Добавьте правила в группу безопасности согласно таблице:
 PriorityActionTypeProtocol & PortSource1AllowIPv4UDP: 500<cloud_gateway_public_ip>1AllowIPv4UDP: 4500<cloud_gateway_public_ip>1AllowIPv4ICMP: All<cloud_subnet_ip>
Где:

<cloud_gateway_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
<cloud_subnet_ip> — адрес подсети cloud-subnet на платформе Evolution.
4. [Создайте виртуальную машину](https://cloud.ru/docs/ecs/ug/topics/guides__create-vm__new-vm)Создайте виртуальную машину со следующими параметрами:

На этапе Configure Basic Settings:

AZ — AZ1.
Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
Image — Ubuntu 22.04.

На этапе Configure Network:

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
Source/Destination Check — отключите опцию.
Security Group — remote-sg.
EIP — Auto assign.
Billed By — By Traffic.

На этапе Configure Advanced Settings:

ECS Name — remote-gateway.
Login Mode — Password.
Password — введите пароль пользователя.
Confirm Password — повторите введенный ранее пароль.

На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

Виртуальная машина будет выполнять роль удаленного VPN-шлюза, который принимает трафик от клиентских ВМ и направляет его в подсеть на стороне Evolution.
5. Сохраните IP-адреса виртуальной машины remote-gateway из столбца IP Address: публичный (EIP) и внутренний (Private IP).
Они потребуются для дальнейшей настройки.
6. [Создайте виртуальную машину](https://cloud.ru/docs/ecs/ug/topics/guides__create-vm__new-vm)Создайте виртуальную машину со следующими параметрами:

На этапе Configure Basic Settings:

AZ — AZ1.
Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
Image — Ubuntu 22.04.

На этапе Configure Network:

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
Security Group — remote-sg.
EIP — Do not use.

На этапе Configure Advanced Settings:

ECS Name — remote-vm.
Login Mode — Password.
Password — введите пароль пользователя.
Confirm Password — повторите введенный ранее пароль.

На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

Виртуальная машина будет выполнять роль клиента, который отправляет трафик в подсеть на стороне Evolution через удаленный VPN-шлюз.
7. Сохраните внутренний IP-адрес виртуальной машины remote-vm из столбца IP Address: он потребуется для дальнейшей настройки.

[Создайте сеть VPC и подсеть](https://cloud.ru/docs/vpc/ug/topics/managing-networks__create-vpc-network)Создайте сеть VPC и подсеть со следующими параметрами:

- В блоке Basic Information:

Name — remote-vpc.
IPv4 CIDR Block — 10.0.0.0/8-24.
Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.
- В блоке Subnet Setting:

Subnet Name — remote-subnet.
IPv4 CIDR Block — 10.0.0.0/24.
Сохраните адрес подсети — он потребуется для дальнейшей настройки.

В блоке Basic Information:

- Name — remote-vpc.
- IPv4 CIDR Block — 10.0.0.0/8-24.
- Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.

Name — remote-vpc.

IPv4 CIDR Block — 10.0.0.0/8-24.

Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.

В блоке Subnet Setting:

- Subnet Name — remote-subnet.
- IPv4 CIDR Block — 10.0.0.0/24.
Сохраните адрес подсети — он потребуется для дальнейшей настройки.

Subnet Name — remote-subnet.

IPv4 CIDR Block — 10.0.0.0/24.
Сохраните адрес подсети — он потребуется для дальнейшей настройки.

[Создайте группу безопасности](https://cloud.ru/docs/vpc/ug/topics/security-groups__managing-groups__create)Создайте группу безопасности со следующими параметрами:

- Name — remote-sg.
- Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.
- Template — Fast-add rule.

Name — remote-sg.

Enterprise Project — выберите существующий проект из списка или нажмите Create Enterprise Project, чтобы [создать новый](https://cloud.ru/docs/eps/ug/topics/create-eps)создать новый.

Template — Fast-add rule.

[Добавьте правила в группу безопасности](https://cloud.ru/docs/vpc/ug/topics/security-groups__managing-security-group-rules__create)Добавьте правила в группу безопасности согласно таблице:

Priority

Action

Type

Protocol & Port

Source

1

Allow

IPv4

UDP: 500

<cloud_gateway_public_ip>

1

Allow

IPv4

UDP: 4500

<cloud_gateway_public_ip>

1

Allow

IPv4

ICMP: All

<cloud_subnet_ip>

Где:

- <cloud_gateway_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
- <cloud_subnet_ip> — адрес подсети cloud-subnet на платформе Evolution.

<cloud_gateway_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.

<cloud_subnet_ip> — адрес подсети cloud-subnet на платформе Evolution.

[Создайте виртуальную машину](https://cloud.ru/docs/ecs/ug/topics/guides__create-vm__new-vm)Создайте виртуальную машину со следующими параметрами:

1. На этапе Configure Basic Settings:

AZ — AZ1.
Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
Image — Ubuntu 22.04.
2. На этапе Configure Network:

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
Source/Destination Check — отключите опцию.
Security Group — remote-sg.
EIP — Auto assign.
Billed By — By Traffic.
3. На этапе Configure Advanced Settings:

ECS Name — remote-gateway.
Login Mode — Password.
Password — введите пароль пользователя.
Confirm Password — повторите введенный ранее пароль.
4. На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

На этапе Configure Basic Settings:

- AZ — AZ1.
- Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
- Image — Ubuntu 22.04.

AZ — AZ1.

Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.

Image — Ubuntu 22.04.

На этапе Configure Network:

- Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
- Source/Destination Check — отключите опцию.
- Security Group — remote-sg.
- EIP — Auto assign.
- Billed By — By Traffic.

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.

Source/Destination Check — отключите опцию.

Security Group — remote-sg.

EIP — Auto assign.

Billed By — By Traffic.

На этапе Configure Advanced Settings:

- ECS Name — remote-gateway.
- Login Mode — Password.
- Password — введите пароль пользователя.
- Confirm Password — повторите введенный ранее пароль.

ECS Name — remote-gateway.

Login Mode — Password.

Password — введите пароль пользователя.

Confirm Password — повторите введенный ранее пароль.

На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

Виртуальная машина будет выполнять роль удаленного VPN-шлюза, который принимает трафик от клиентских ВМ и направляет его в подсеть на стороне Evolution.

Сохраните IP-адреса виртуальной машины remote-gateway из столбца IP Address: публичный (EIP) и внутренний (Private IP).
Они потребуются для дальнейшей настройки.

[Создайте виртуальную машину](https://cloud.ru/docs/ecs/ug/topics/guides__create-vm__new-vm)Создайте виртуальную машину со следующими параметрами:

1. На этапе Configure Basic Settings:

AZ — AZ1.
Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
Image — Ubuntu 22.04.
2. На этапе Configure Network:

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
Security Group — remote-sg.
EIP — Do not use.
3. На этапе Configure Advanced Settings:

ECS Name — remote-vm.
Login Mode — Password.
Password — введите пароль пользователя.
Confirm Password — повторите введенный ранее пароль.
4. На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

На этапе Configure Basic Settings:

- AZ — AZ1.
- Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.
- Image — Ubuntu 22.04.

AZ — AZ1.

Specifications — выберите спецификацию General-Purpose и флейвор s6.small.1.

Image — Ubuntu 22.04.

На этапе Configure Network:

- Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.
- Security Group — remote-sg.
- EIP — Do not use.

Network — выберите облачную сеть remote-vpc и подсеть remote-subnet.

Security Group — remote-sg.

EIP — Do not use.

На этапе Configure Advanced Settings:

- ECS Name — remote-vm.
- Login Mode — Password.
- Password — введите пароль пользователя.
- Confirm Password — повторите введенный ранее пароль.

ECS Name — remote-vm.

Login Mode — Password.

Password — введите пароль пользователя.

Confirm Password — повторите введенный ранее пароль.

На этапе Confirm проверьте настройки виртуальной машины и в поле Enterprise Project выберите проект, в котором она будет создана.

Виртуальная машина будет выполнять роль клиента, который отправляет трафик в подсеть на стороне Evolution через удаленный VPN-шлюз.

Сохраните внутренний IP-адрес виртуальной машины remote-vm из столбца IP Address: он потребуется для дальнейшей настройки.

## 3. Добавьте правила в группу безопасности облачного VPN-шлюза

Для работы strongSwan и проверки доступности виртуальных машин необходимо:

- разрешить входящий трафик со стороны удаленного VPN-шлюза через порты UDP 500 и 4500;
- разрешить входящий трафик из удаленной подсети по протоколу ICMP.

разрешить входящий трафик со стороны удаленного VPN-шлюза через порты UDP 500 и 4500;

разрешить входящий трафик из удаленной подсети по протоколу ICMP.

[Добавьте правила входящего трафика](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)Добавьте правила входящего трафика в группу безопасности cloud-sg согласно таблице:

Протокол

Порт

Тип источника

Источник

UDP

500

IP-адрес

<remote_gateway_public_ip>

UDP

4500

IP-адрес

<remote_gateway_public_ip>

ICMP

Любой

IP-адрес

<remote_subnet_ip>

Где:

- <remote_gateway_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
- <remote_subnet_ip> — адрес подсети remote-subnet на платформе Advanced.

<remote_gateway_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.

<remote_subnet_ip> — адрес подсети remote-subnet на платформе Advanced.

## 4. Настройте VPN-шлюзы

Для установления IPsec-туннеля необходимо настроить VPN-шлюзы на стороне Evolution и Advanced.

### Настройте облачный VPN-шлюз

1. Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.
2. На верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
3. Выберите виртуальную машину cloud-gateway в списке.
4. Перейдите на вкладку Серийная консоль.
5. Введите логин и пароль, указанные при создании виртуальной машины.
6. Включите маршрутизацию пакетов и отключите функциональность ICMP Redirects:

Откройте файл /etc/sysctl.conf для редактирования.
В терминале выполните команду:
sudo nano /etc/sysctl.conf

Добавьте в файл параметры:
net.ipv4.ip_forward = 1net.ipv4.conf.all.accept_redirects = 0net.ipv4.conf.all.send_redirects = 0net.ipv4.conf.enp3s0.accept_redirects = 0net.ipv4.conf.enp3s0.send_redirects = 0

Примените изменения:
sudo sysctl -p /etc/sysctl.conf
7. Заполните файл конфигурации IPsec-туннеля:

Откройте файл /etc/ipsec.conf для редактирования:
sudo nano /etc/ipsec.conf

Вставьте конфигурацию в файл:
config setup strictcrlpolicy=yes uniqueids=yes
conn evo-to-advanced type=tunnel auto=start keyexchange=ikev2 authby=secret left=<left_internal_ip> leftid=<left_public_ip> leftsubnet=<left_subnet> right=<right_public_ip> rightsubnet=<right_subnet> ike=aes256-sha2_256-modp1024! esp=aes256-sha2_256!

Где:

<left_internal_ip> — внутренний IP-адрес ВМ cloud-gateway.
<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
<left_subnet> — адрес подсети cloud-subnet.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
<right_subnet> — адрес подсети remote-subnet на платформе Advanced.

Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.
8. Заполните файл секретов:

Откройте файл /etc/ipsec.secrets для редактирования:
sudo nano /etc/ipsec.secrets

Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:
<left_public_ip> <right_public_ip> : PSK "<secret_phrase>"

Где:

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
<secret_phrase> — ключ для установки IPsec-соединения.
Значение ключа необходимо придумать самостоятельно.
9. Перезапустите strongSwan:
sudo systemctl restart strongswan-starter.service
10. Проверьте, что VPN-шлюз на стороне Evolution поднят и находится в ожидании установления IPsec-туннеля c удаленной стороной:
sudo ipsec status

Результат:
Security Associations (0 up, 1 connecting):evo-to-advanced[1]: CONNECTING, 172.31.***.***[%any]...37.18.***.***[%any]

Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.

На верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Выберите виртуальную машину cloud-gateway в списке.

Перейдите на вкладку Серийная консоль.

Введите логин и пароль, указанные при создании виртуальной машины.

Включите маршрутизацию пакетов и отключите функциональность ICMP Redirects:

1. Откройте файл /etc/sysctl.conf для редактирования.
В терминале выполните команду:
sudo nano /etc/sysctl.conf
2. Добавьте в файл параметры:
net.ipv4.ip_forward = 1net.ipv4.conf.all.accept_redirects = 0net.ipv4.conf.all.send_redirects = 0net.ipv4.conf.enp3s0.accept_redirects = 0net.ipv4.conf.enp3s0.send_redirects = 0
3. Примените изменения:
sudo sysctl -p /etc/sysctl.conf

Откройте файл /etc/sysctl.conf для редактирования.
В терминале выполните команду:

```bash
sudo
nano
/etc/sysctl.conf
```

Добавьте в файл параметры:

```bash
net.ipv4.ip_forward
=
1
net.ipv4.conf.all.accept_redirects
=
0
net.ipv4.conf.all.send_redirects
=
0
net.ipv4.conf.enp3s0.accept_redirects
=
0
net.ipv4.conf.enp3s0.send_redirects
=
0
```

Примените изменения:

```bash
sudo
sysctl
-p
/etc/sysctl.conf
```

Заполните файл конфигурации IPsec-туннеля:

1. Откройте файл /etc/ipsec.conf для редактирования:
sudo nano /etc/ipsec.conf
2. Вставьте конфигурацию в файл:
config setup strictcrlpolicy=yes uniqueids=yes
conn evo-to-advanced type=tunnel auto=start keyexchange=ikev2 authby=secret left=<left_internal_ip> leftid=<left_public_ip> leftsubnet=<left_subnet> right=<right_public_ip> rightsubnet=<right_subnet> ike=aes256-sha2_256-modp1024! esp=aes256-sha2_256!

Где:

<left_internal_ip> — внутренний IP-адрес ВМ cloud-gateway.
<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
<left_subnet> — адрес подсети cloud-subnet.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
<right_subnet> — адрес подсети remote-subnet на платформе Advanced.

Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.

Откройте файл /etc/ipsec.conf для редактирования:

```bash
sudo
nano
/etc/ipsec.conf
```

Вставьте конфигурацию в файл:

```bash
config setup
strictcrlpolicy
=
yes
uniqueids
=
yes
conn evo-to-advanced
type
=
tunnel
auto
=
start
keyexchange
=
ikev2
authby
=
secret
left
=
<
left_internal_ip
>
leftid
=
<
left_public_ip
>
leftsubnet
=
<
left_subnet
>
right
=
<
right_public_ip
>
rightsubnet
=
<
right_subnet
>
ike
=
aes256-sha2_256-modp1024
!
esp
=
aes256-sha2_256
!
```

Где:

- <left_internal_ip> — внутренний IP-адрес ВМ cloud-gateway.
- <left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
- <left_subnet> — адрес подсети cloud-subnet.
- <right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
- <right_subnet> — адрес подсети remote-subnet на платформе Advanced.

<left_internal_ip> — внутренний IP-адрес ВМ cloud-gateway.

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.

<left_subnet> — адрес подсети cloud-subnet.

<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.

<right_subnet> — адрес подсети remote-subnet на платформе Advanced.

Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.

Заполните файл секретов:

1. Откройте файл /etc/ipsec.secrets для редактирования:
sudo nano /etc/ipsec.secrets
2. Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:
<left_public_ip> <right_public_ip> : PSK "<secret_phrase>"

Где:

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
<secret_phrase> — ключ для установки IPsec-соединения.
Значение ключа необходимо придумать самостоятельно.

Откройте файл /etc/ipsec.secrets для редактирования:

```bash
sudo
nano
/etc/ipsec.secrets
```

Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:

```bash
<
left_public_ip
>
<
right_public_ip
>
:
PSK
"<secret_phrase>"
```

Где:

- <left_public_ip> — публичный IP-адрес ВМ cloud-gateway.
- <right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.
- <secret_phrase> — ключ для установки IPsec-соединения.
Значение ключа необходимо придумать самостоятельно.

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway.

<right_public_ip> — публичный IP-адрес ВМ remote-gateway на платформе Advanced.

<secret_phrase> — ключ для установки IPsec-соединения.
Значение ключа необходимо придумать самостоятельно.

Перезапустите strongSwan:

```bash
sudo
systemctl restart strongswan-starter.service
```

Проверьте, что VPN-шлюз на стороне Evolution поднят и находится в ожидании установления IPsec-туннеля c удаленной стороной:

```bash
sudo
ipsec status
```

Результат:

```bash
Security Associations
(
0
up,
1
connecting
)
:
evo-to-advanced
[
1
]
: CONNECTING,
172.31
.***.***
[
%any
]
..
.37.18.***.***
[
%any
]
```

### Настройте удаленный VPN-шлюз

1. Войдите в консоль управления Advanced:

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.
2. В списке сервисов выберите Elastic Cloud Server.
3. Напротив виртуальной машины remote-gateway нажмите Remote Login.
4. Введите логин и пароль, указанные при создании виртуальной машины.
5. Обновите версии пакетов.
В терминале выполните команду:
sudo apt update
6. Установите strongSwan:
sudo apt install -y strongswan
7. Включите маршрутизацию пакетов и отключите функциональность ICMP Redirects:

Откройте файл /etc/sysctl.conf для редактирования:
sudo nano /etc/sysctl.conf

Добавьте в файл параметры:
net.ipv4.ip_forward = 1net.ipv4.conf.all.accept_redirects = 0net.ipv4.conf.all.send_redirects = 0net.ipv4.conf.eth0.accept_redirects = 0net.ipv4.conf.eth0.send_redirects = 0

ПримечаниеНа практике имена локальных интерфейсов на удаленной стороне могут отличаться.

Примените изменения:
sudo sysctl -p /etc/sysctl.conf
8. Заполните файл конфигурации IPsec-туннеля:

Откройте файл /etc/ipsec.conf для редактирования.
sudo nano /etc/ipsec.conf

Вставьте конфигурацию в файл:
config setup strictcrlpolicy=yes uniqueids=yes
conn advanced-to-evo type=tunnel auto=start keyexchange=ikev2 authby=secret right=<right_public_ip> rightsubnet=<right_subnet> left=<left_internal_ip> leftid=<left_public_ip> leftsubnet=<left_subnet> ike=aes256-sha2_256-modp1024! esp=aes256-sha2_256!

Где:

<right_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
<right_subnet> — адрес подсети cloud-subnet на платформе Evolution.
<left_internal_ip> — внутренний IP-адрес ВМ remote-gateway.
<left_public_ip> — публичный IP-адрес ВМ remote-gateway.
<left_subnet> — адрес подсети remote-subnet.

При настройке удаленной стороны она становится левой стороной туннеля, а сторона облака Evolution становится правой стороной.
Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.
9. Заполните файл секретов:

Откройте файл /etc/ipsec.secrets для редактирования:
sudo nano /etc/ipsec.secrets

Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:
<left_public_ip> <right_public_ip> : PSK "<secret_phrase>"

Где:

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway.
<secret_phrase> — ключ для установки IPsec-соединения.
Укажите такое же значение, как и в настройках облачного VPN-шлюза.
10. Перезапустите strongSwan:
sudo systemctl restart strongswan-starter.service
11. Проверьте, что VPN-шлюз на стороне Advanced поднят, а IPsec-туннель установлен:
sudo ipsec status

Результат:
Security Associations (1 up, 0 connecting):advanced-to-evo[2]: ESTABLISHED 110 seconds ago, 10.0.***.***[37.18.***.***]...176.108.***.***[176.108.***.***]advanced-to-evo{1}: INSTALLED, TUNNEL, reqid 1, ESP in UDP SPIs: c9c35ad9_i c0c7b197_oadvanced-to-evo{1}: 10.0.***.***/24 === 172.31.***.***/24

Войдите в консоль управления Advanced:

- [через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
- [как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;

[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

В списке сервисов выберите Elastic Cloud Server.

Напротив виртуальной машины remote-gateway нажмите Remote Login.

Введите логин и пароль, указанные при создании виртуальной машины.

Обновите версии пакетов.
В терминале выполните команду:

```bash
sudo
apt
update
```

Установите strongSwan:

```bash
sudo
apt
install
-y
strongswan
```

Включите маршрутизацию пакетов и отключите функциональность ICMP Redirects:

1. Откройте файл /etc/sysctl.conf для редактирования:
sudo nano /etc/sysctl.conf
2. Добавьте в файл параметры:
net.ipv4.ip_forward = 1net.ipv4.conf.all.accept_redirects = 0net.ipv4.conf.all.send_redirects = 0net.ipv4.conf.eth0.accept_redirects = 0net.ipv4.conf.eth0.send_redirects = 0

ПримечаниеНа практике имена локальных интерфейсов на удаленной стороне могут отличаться.
3. Примените изменения:
sudo sysctl -p /etc/sysctl.conf

Откройте файл /etc/sysctl.conf для редактирования:

```bash
sudo
nano
/etc/sysctl.conf
```

Добавьте в файл параметры:

```bash
net.ipv4.ip_forward
=
1
net.ipv4.conf.all.accept_redirects
=
0
net.ipv4.conf.all.send_redirects
=
0
net.ipv4.conf.eth0.accept_redirects
=
0
net.ipv4.conf.eth0.send_redirects
=
0
```

На практике имена локальных интерфейсов на удаленной стороне могут отличаться.

Примените изменения:

```bash
sudo
sysctl
-p
/etc/sysctl.conf
```

Заполните файл конфигурации IPsec-туннеля:

1. Откройте файл /etc/ipsec.conf для редактирования.
sudo nano /etc/ipsec.conf
2. Вставьте конфигурацию в файл:
config setup strictcrlpolicy=yes uniqueids=yes
conn advanced-to-evo type=tunnel auto=start keyexchange=ikev2 authby=secret right=<right_public_ip> rightsubnet=<right_subnet> left=<left_internal_ip> leftid=<left_public_ip> leftsubnet=<left_subnet> ike=aes256-sha2_256-modp1024! esp=aes256-sha2_256!

Где:

<right_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
<right_subnet> — адрес подсети cloud-subnet на платформе Evolution.
<left_internal_ip> — внутренний IP-адрес ВМ remote-gateway.
<left_public_ip> — публичный IP-адрес ВМ remote-gateway.
<left_subnet> — адрес подсети remote-subnet.

При настройке удаленной стороны она становится левой стороной туннеля, а сторона облака Evolution становится правой стороной.
Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.

Откройте файл /etc/ipsec.conf для редактирования.

```bash
sudo
nano
/etc/ipsec.conf
```

Вставьте конфигурацию в файл:

```bash
config setup
strictcrlpolicy
=
yes
uniqueids
=
yes
conn advanced-to-evo
type
=
tunnel
auto
=
start
keyexchange
=
ikev2
authby
=
secret
right
=
<
right_public_ip
>
rightsubnet
=
<
right_subnet
>
left
=
<
left_internal_ip
>
leftid
=
<
left_public_ip
>
leftsubnet
=
<
left_subnet
>
ike
=
aes256-sha2_256-modp1024
!
esp
=
aes256-sha2_256
!
```

Где:

- <right_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
- <right_subnet> — адрес подсети cloud-subnet на платформе Evolution.
- <left_internal_ip> — внутренний IP-адрес ВМ remote-gateway.
- <left_public_ip> — публичный IP-адрес ВМ remote-gateway.
- <left_subnet> — адрес подсети remote-subnet.

<right_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.

<right_subnet> — адрес подсети cloud-subnet на платформе Evolution.

<left_internal_ip> — внутренний IP-адрес ВМ remote-gateway.

<left_public_ip> — публичный IP-адрес ВМ remote-gateway.

<left_subnet> — адрес подсети remote-subnet.

При настройке удаленной стороны она становится левой стороной туннеля, а сторона облака Evolution становится правой стороной.

Подробное описание параметров файла /etc/ipsec.conf смотрите [в документации strongSwan](https://wiki.strongswan.org/projects/strongswan/wiki/connsection)в документации strongSwan.

Заполните файл секретов:

1. Откройте файл /etc/ipsec.secrets для редактирования:
sudo nano /etc/ipsec.secrets
2. Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:
<left_public_ip> <right_public_ip> : PSK "<secret_phrase>"

Где:

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
<right_public_ip> — публичный IP-адрес ВМ remote-gateway.
<secret_phrase> — ключ для установки IPsec-соединения.
Укажите такое же значение, как и в настройках облачного VPN-шлюза.

Откройте файл /etc/ipsec.secrets для редактирования:

```bash
sudo
nano
/etc/ipsec.secrets
```

Вставьте в файл ключевую фразу (PSK, Pre-Shared Key) туннеля:

```bash
<
left_public_ip
>
<
right_public_ip
>
:
PSK
"<secret_phrase>"
```

Где:

- <left_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.
- <right_public_ip> — публичный IP-адрес ВМ remote-gateway.
- <secret_phrase> — ключ для установки IPsec-соединения.
Укажите такое же значение, как и в настройках облачного VPN-шлюза.

<left_public_ip> — публичный IP-адрес ВМ cloud-gateway на платформе Evolution.

<right_public_ip> — публичный IP-адрес ВМ remote-gateway.

<secret_phrase> — ключ для установки IPsec-соединения.
Укажите такое же значение, как и в настройках облачного VPN-шлюза.

Перезапустите strongSwan:

```bash
sudo
systemctl restart strongswan-starter.service
```

Проверьте, что VPN-шлюз на стороне Advanced поднят, а IPsec-туннель установлен:

```bash
sudo
ipsec status
```

Результат:

```bash
Security Associations
(
1
up,
0
connecting
)
:
advanced-to-evo
[
2
]
: ESTABLISHED
110
seconds ago,
10.0
.***.***
[
37.18
.***.***
]
..
.176.108.***.***
[
176.108
.***.***
]
advanced-to-evo
{
1
}
: INSTALLED, TUNNEL, reqid
1
, ESP
in
UDP SPIs: c9c35ad9_i c0c7b197_o
advanced-to-evo
{
1
}
:
10.0
.***.***/24
==
=
172.31
.***.***/24
```

### Проверьте работу шлюзов

Проверьте, что на обоих VPN-шлюзах появилась возможность пинговать внутренний IP-адрес шлюза с противоположной стороны.

1. На стороне платформы Evolution на ВМ cloud-gateway выполните команду:
ping -c4 <remote_gateway_internal_ip>

Где <remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.
2. На стороне платформы Advanced на ВМ remote-gateway выполните команду:
ping -c4 <cloud_gateway_internal_ip>

Где <cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.

На стороне платформы Evolution на ВМ cloud-gateway выполните команду:

```bash
ping
-c4
<
remote_gateway_internal_ip
>
```

Где <remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.

На стороне платформы Advanced на ВМ remote-gateway выполните команду:

```bash
ping
-c4
<
cloud_gateway_internal_ip
>
```

Где <cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.

## 5. Настройте маршрутизацию

В виртуальных сетях на обеих сторонах необходимо добавить статические маршруты.
Это позволит перенаправлять трафик с клиентских ВМ на противоположную сторону туннеля через внутренний интерфейс VPN-шлюза.

### Настройте маршрутизацию в Evolution

1. Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.
2. На верхней панели слева нажмите и выберите Сеть → VPC.
3. Выберите сеть cloud-vpc.
4. Перейдите на вкладку Маршруты.
5. Нажмите Создать маршрут.
6. Укажите параметры маршрута:

Адрес назначения — адрес подсети remote-subnet на платформе Advanced.
Next Hop Type — Виртуальная машина.
Виртуальная машина — cloud-gateway.
Интерфейс — выберите интерфейс ВМ cloud-gateway, который подключен к подсети cloud-subnet.
7. Нажмите Создать.
Дождитесь, когда статус маршрута сменится на «Активен».

Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.

На верхней панели слева нажмите и выберите Сеть → VPC.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Выберите сеть cloud-vpc.

Перейдите на вкладку Маршруты.

Нажмите Создать маршрут.

Укажите параметры маршрута:

- Адрес назначения — адрес подсети remote-subnet на платформе Advanced.
- Next Hop Type — Виртуальная машина.
- Виртуальная машина — cloud-gateway.
- Интерфейс — выберите интерфейс ВМ cloud-gateway, который подключен к подсети cloud-subnet.

Адрес назначения — адрес подсети remote-subnet на платформе Advanced.

Next Hop Type — Виртуальная машина.

Виртуальная машина — cloud-gateway.

Интерфейс — выберите интерфейс ВМ cloud-gateway, который подключен к подсети cloud-subnet.

Нажмите Создать.

Дождитесь, когда статус маршрута сменится на «Активен».

### Настройте маршрутизацию в Advanced

1. Войдите в консоль управления Advanced:

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.
2. В списке сервисов выберите Virtual Private Cloud.
3. В меню слева выберите Route Tables.
4. Нажмите Create Route Table.
5. Укажите параметры таблицы маршрутизации:

Name — rtb-remote-vpc.
VPC — remote-vpc.
6. Добавьте маршрут в таблицу:

В блоке Route Settings нажмите Add Route.
Укажите параметры маршрута:

Destination Type — IP address.
Destination — адрес подсети cloud-subnet на платформе Evolution.
Next Hop Type — Server.
Next Hop — remote-gateway.
7. Нажмите OK.
8. Во всплывающем окне нажмите Associate Subnet.
9. На вкладке Associated Subnets нажмите Associate Subnet.
10. Отметьте подсеть remote-subnet и нажмите OK.

Войдите в консоль управления Advanced:

- [через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
- [как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;

[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

В списке сервисов выберите Virtual Private Cloud.

В меню слева выберите Route Tables.

Нажмите Create Route Table.

Укажите параметры таблицы маршрутизации:

- Name — rtb-remote-vpc.
- VPC — remote-vpc.

Name — rtb-remote-vpc.

VPC — remote-vpc.

Добавьте маршрут в таблицу:

1. В блоке Route Settings нажмите Add Route.
2. Укажите параметры маршрута:

Destination Type — IP address.
Destination — адрес подсети cloud-subnet на платформе Evolution.
Next Hop Type — Server.
Next Hop — remote-gateway.

В блоке Route Settings нажмите Add Route.

Укажите параметры маршрута:

- Destination Type — IP address.
- Destination — адрес подсети cloud-subnet на платформе Evolution.
- Next Hop Type — Server.
- Next Hop — remote-gateway.

Destination Type — IP address.

Destination — адрес подсети cloud-subnet на платформе Evolution.

Next Hop Type — Server.

Next Hop — remote-gateway.

Нажмите OK.

Во всплывающем окне нажмите Associate Subnet.

На вкладке Associated Subnets нажмите Associate Subnet.

Отметьте подсеть remote-subnet и нажмите OK.

## 6. Проверьте сетевую связность

1. Проверьте, что удаленный VPN-шлюз и удаленная клиентская ВМ доступны с облачной клиентской ВМ:

Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.
На верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
Выберите виртуальную машину cloud-vm в списке.
Перейдите на вкладку Серийная консоль.
Введите логин и пароль, указанные при создании виртуальной машины.
В терминале поочередно выполните команды:
ping -c4 <remote_gateway_internal_ip>ping -c4 <remote_vm_internal_ip>

Где:

<remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.
<remote_vm_internal_ip> — внутренний IP-адрес ВМ remote-vm на платформе Advanced.
2. Проверьте, что облачный VPN-шлюз и облачная ВМ доступны с удаленной клиентской ВМ:

Войдите в консоль управления Advanced:

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

В списке сервисов выберите Elastic Cloud Server.
Напротив виртуальной машины remote-vm нажмите Remote Login.
Введите логин и пароль, указанные при создании виртуальной машины.
В терминале поочередно выполните команды:
ping -c4 <cloud_gateway_internal_ip>ping -c4 <cloud_vm_internal_ip>

Где:

<cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.
<cloud_vm_internal_ip> — внутренний IP-адрес ВМ cloud-vm на платформе Evolution.

Проверьте, что удаленный VPN-шлюз и удаленная клиентская ВМ доступны с облачной клиентской ВМ:

1. Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.
2. На верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
3. Выберите виртуальную машину cloud-vm в списке.
4. Перейдите на вкладку Серийная консоль.
5. Введите логин и пароль, указанные при создании виртуальной машины.
6. В терминале поочередно выполните команды:
ping -c4 <remote_gateway_internal_ip>ping -c4 <remote_vm_internal_ip>

Где:

<remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.
<remote_vm_internal_ip> — внутренний IP-адрес ВМ remote-vm на платформе Advanced.

Перейдите в [личный кабинет](https://console.cloud.ru/)личный кабинет платформы Evolution.

На верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Выберите виртуальную машину cloud-vm в списке.

Перейдите на вкладку Серийная консоль.

Введите логин и пароль, указанные при создании виртуальной машины.

В терминале поочередно выполните команды:

```bash
ping
-c4
<
remote_gateway_internal_ip
>
ping
-c4
<
remote_vm_internal_ip
>
```

Где:

- <remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.
- <remote_vm_internal_ip> — внутренний IP-адрес ВМ remote-vm на платформе Advanced.

<remote_gateway_internal_ip> — внутренний IP-адрес ВМ remote-gateway на платформе Advanced.

<remote_vm_internal_ip> — внутренний IP-адрес ВМ remote-vm на платформе Advanced.

Проверьте, что облачный VPN-шлюз и облачная ВМ доступны с удаленной клиентской ВМ:

1. Войдите в консоль управления Advanced:

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.
2. В списке сервисов выберите Elastic Cloud Server.
3. Напротив виртуальной машины remote-vm нажмите Remote Login.
4. Введите логин и пароль, указанные при создании виртуальной машины.
5. В терминале поочередно выполните команды:
ping -c4 <cloud_gateway_internal_ip>ping -c4 <cloud_vm_internal_ip>

Где:

<cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.
<cloud_vm_internal_ip> — внутренний IP-адрес ВМ cloud-vm на платформе Evolution.

Войдите в консоль управления Advanced:

- [через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;
- [как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

[через личный кабинет Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__auth)через личный кабинет Cloud.ru;

[как IAM-пользователь](https://cloud.ru/docs/iam/ug/topics/guides__login-to-cloud-platform)как IAM-пользователь.

В списке сервисов выберите Elastic Cloud Server.

Напротив виртуальной машины remote-vm нажмите Remote Login.

Введите логин и пароль, указанные при создании виртуальной машины.

В терминале поочередно выполните команды:

```bash
ping
-c4
<
cloud_gateway_internal_ip
>
ping
-c4
<
cloud_vm_internal_ip
>
```

Где:

- <cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.
- <cloud_vm_internal_ip> — внутренний IP-адрес ВМ cloud-vm на платформе Evolution.

<cloud_gateway_internal_ip> — внутренний IP-адрес ВМ cloud-gateway на платформе Evolution.

<cloud_vm_internal_ip> — внутренний IP-адрес ВМ cloud-vm на платформе Evolution.

Теперь клиентские ВМ могут обмениваться трафиком с помощью настроенного IPsec-туннеля.

## Результат

Вы научились настраивать защищенное соединение между инфраструктурой в облаке Cloud.ru Evolution и удаленной стороной.
