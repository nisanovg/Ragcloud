---
title: Связывание ресурсов в разных VPC внутри проекта
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project
topic: network
---
# Связывание ресурсов в разных VPC внутри проекта

С помощью этого руководства вы настроите сетевую связность между виртуальными машинами из разных VPC, принадлежащих одному проекту.
Вы будете использовать соединения, маршруты и правила групп безопасности для связи ресурсов.
Схема сетевой связности ресурсов представлена ниже.

![Схема связности ресурсов в разных VPC внутри проекта](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/vpcs-in-project.png)

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- [Magic Router](https://cloud.ru/docs/magic-router/ug/index)Magic Router — сервис для управления сетевыми связями между ресурсами внутри облачной инфраструктуры.
- [Группы безопасности](https://cloud.ru/docs/security-groups/ug/index)Группы безопасности — сервис для контроля трафика виртуальных машин.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Magic Router](https://cloud.ru/docs/magic-router/ug/index)Magic Router — сервис для управления сетевыми связями между ресурсами внутри облачной инфраструктуры.

[Группы безопасности](https://cloud.ru/docs/security-groups/ug/index)Группы безопасности — сервис для контроля трафика виртуальных машин.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Разверните ресурсы в облаке.
2. [Создайте соединение между VPC](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Создайте соединение между VPC.
3. [Настройте маршруты на Magic Router](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте маршруты на Magic Router.
4. [Настройте маршруты для VPC](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте маршруты для VPC.
5. [Настройте правила групп безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте правила групп безопасности.
6. [Проверьте сетевую связность](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Проверьте сетевую связность.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Разверните ресурсы в облаке.

[Создайте соединение между VPC](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Создайте соединение между VPC.

[Настройте маршруты на Magic Router](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте маршруты на Magic Router.

[Настройте маршруты для VPC](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте маршруты для VPC.

[Настройте правила групп безопасности](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Настройте правила групп безопасности.

[Проверьте сетевую связность](https://cloud.ru/docs/tutorials-evolution/list/topics/magic-router__link-vpcs-in-project)Проверьте сетевую связность.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

## 1. Разверните ресурсы в облаке

1. [Создайте две VPC-сети](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте две VPC-сети с названиями VPC-1 и VPC-2.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-1:

Название: subnet-1.
VPC: VPC-1.
Зона доступности: ru.AZ-1.
Адрес: 10.1.1.0/24.
3. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-2:

Название: subnet-2.
VPC: VPC-1.
Зона доступности: ru.AZ-2.
Адрес: 10.3.3.0/24.
4. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-3:

Название: subnet-3.
VPC: VPC-2.
Зона доступности: ru.AZ-1.
Адрес: 10.2.2.0/24.

Убедитесь, что на странице сервиса Подсети подсети subnet-1, subnet-2, subnet-3 находятся в статусе «Создана».
5. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: vm-1.
Зона доступности: ru.AZ-1.
Образ: Публичные → Ubuntu 22.04.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.
VPC: VPC-1.
Подсеть: 10.1.1.0/24 (subnet-1).
Внутренний IP: Автоматически.
Группы безопасности: SSH-access_ru.AZ-1.
Метод аутентификации: Публичный ключ и пароль.
Публичный ключ: ваш SSH-ключ.
Пароль: ваш пароль.
Имя хоста: vm-1.
6. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: vm-2.
Зона доступности: ru.AZ-2.
Образ: Публичные → Ubuntu 22.04.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.
VPC: VPC-1.
Подсеть: 10.3.3.0/24 (subnet-2).
Внутренний IP: Автоматически.
Группы безопасности: SSH-access_ru.AZ-2.
Метод аутентификации: Публичный ключ и пароль.
Публичный ключ: ваш SSH-ключ.
Пароль: ваш пароль.
Имя хоста: vm-2.
7. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: vm-3.
Зона доступности: ru.AZ-1.
Образ: Публичные → Ubuntu 22.04.
Гарантированная доля vCPU: 10%.
vCPU: 1.
RAM: 1.
VPC: VPC-2.
Подсеть: 10.2.2.0/24 (subnet-3).
Внутренний IP: Автоматически.
Группы безопасности: SSH-access_ru.AZ-1.
Метод аутентификации: Публичный ключ и пароль.
Публичный ключ: ваш SSH-ключ.
Пароль: ваш пароль.
Имя хоста: vm-3.

Убедитесь, что в личном кабинете на странице сервиса Виртуальные машины отображается виртуальные машины vm-1, vm-2, vm-3 в статусе «Запущена».

[Создайте две VPC-сети](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-vpc)Создайте две VPC-сети с названиями VPC-1 и VPC-2.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-1:

- Название: subnet-1.
- VPC: VPC-1.
- Зона доступности: ru.AZ-1.
- Адрес: 10.1.1.0/24.

Название: subnet-1.

VPC: VPC-1.

Зона доступности: ru.AZ-1.

Адрес: 10.1.1.0/24.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-2:

- Название: subnet-2.
- VPC: VPC-1.
- Зона доступности: ru.AZ-2.
- Адрес: 10.3.3.0/24.

Название: subnet-2.

VPC: VPC-1.

Зона доступности: ru.AZ-2.

Адрес: 10.3.3.0/24.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть subnet-3:

- Название: subnet-3.
- VPC: VPC-2.
- Зона доступности: ru.AZ-1.
- Адрес: 10.2.2.0/24.

Название: subnet-3.

VPC: VPC-2.

Зона доступности: ru.AZ-1.

Адрес: 10.2.2.0/24.

Убедитесь, что на странице сервиса Подсети подсети subnet-1, subnet-2, subnet-3 находятся в статусе «Создана».

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: vm-1.
- Зона доступности: ru.AZ-1.
- Образ: Публичные → Ubuntu 22.04.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.
- VPC: VPC-1.
- Подсеть: 10.1.1.0/24 (subnet-1).
- Внутренний IP: Автоматически.
- Группы безопасности: SSH-access_ru.AZ-1.
- Метод аутентификации: Публичный ключ и пароль.
- Публичный ключ: ваш SSH-ключ.
- Пароль: ваш пароль.
- Имя хоста: vm-1.

Название: vm-1.

Зона доступности: ru.AZ-1.

Образ: Публичные → Ubuntu 22.04.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

VPC: VPC-1.

Подсеть: 10.1.1.0/24 (subnet-1).

Внутренний IP: Автоматически.

Группы безопасности: SSH-access_ru.AZ-1.

Метод аутентификации: Публичный ключ и пароль.

Публичный ключ: ваш SSH-ключ.

Пароль: ваш пароль.

Имя хоста: vm-1.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: vm-2.
- Зона доступности: ru.AZ-2.
- Образ: Публичные → Ubuntu 22.04.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.
- VPC: VPC-1.
- Подсеть: 10.3.3.0/24 (subnet-2).
- Внутренний IP: Автоматически.
- Группы безопасности: SSH-access_ru.AZ-2.
- Метод аутентификации: Публичный ключ и пароль.
- Публичный ключ: ваш SSH-ключ.
- Пароль: ваш пароль.
- Имя хоста: vm-2.

Название: vm-2.

Зона доступности: ru.AZ-2.

Образ: Публичные → Ubuntu 22.04.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

VPC: VPC-1.

Подсеть: 10.3.3.0/24 (subnet-2).

Внутренний IP: Автоматически.

Группы безопасности: SSH-access_ru.AZ-2.

Метод аутентификации: Публичный ключ и пароль.

Публичный ключ: ваш SSH-ключ.

Пароль: ваш пароль.

Имя хоста: vm-2.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: vm-3.
- Зона доступности: ru.AZ-1.
- Образ: Публичные → Ubuntu 22.04.
- Гарантированная доля vCPU: 10%.
- vCPU: 1.
- RAM: 1.
- VPC: VPC-2.
- Подсеть: 10.2.2.0/24 (subnet-3).
- Внутренний IP: Автоматически.
- Группы безопасности: SSH-access_ru.AZ-1.
- Метод аутентификации: Публичный ключ и пароль.
- Публичный ключ: ваш SSH-ключ.
- Пароль: ваш пароль.
- Имя хоста: vm-3.

Название: vm-3.

Зона доступности: ru.AZ-1.

Образ: Публичные → Ubuntu 22.04.

Гарантированная доля vCPU: 10%.

vCPU: 1.

RAM: 1.

VPC: VPC-2.

Подсеть: 10.2.2.0/24 (subnet-3).

Внутренний IP: Автоматически.

Группы безопасности: SSH-access_ru.AZ-1.

Метод аутентификации: Публичный ключ и пароль.

Публичный ключ: ваш SSH-ключ.

Пароль: ваш пароль.

Имя хоста: vm-3.

Убедитесь, что в личном кабинете на странице сервиса Виртуальные машины отображается виртуальные машины vm-1, vm-2, vm-3 в статусе «Запущена».

## 2. Создайте соединение между VPC

1. Выберите сервис Magic Router.
2. Нажмите Создать Magic Router.
3. Нажмите VPC Evolution.
4. Выберите VPC-1 и VPC-2.
5. Нажмите Создать.

Выберите сервис Magic Router.

Нажмите Создать Magic Router.

Нажмите VPC Evolution.

Выберите VPC-1 и VPC-2.

Нажмите Создать.

Убедитесь, что в сервисе Magic Router на странице Соединения отображается два соединения в статусе «Активно».

## 3. Настройте маршруты на Magic Router

При создании маршрутов в Magic Router необходимо указывать зону доступности, в которой расположена целевая подсеть.

1. В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-1:

Адрес назначения: 10.1.1.0/24.
VPC: VPC-1.
Зона доступности: ru.AZ-1.
2. В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-2:

Адрес назначения: 10.3.3.0/24.
VPC: VPC-1.
Зона доступности: ru.AZ-2.
3. В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-3:

Адрес назначения: 10.2.2.0/24.
VPC: VPC-2.
Зона доступности: ru.AZ-1.

В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-1:

- Адрес назначения: 10.1.1.0/24.
- VPC: VPC-1.
- Зона доступности: ru.AZ-1.

Адрес назначения: 10.1.1.0/24.

VPC: VPC-1.

Зона доступности: ru.AZ-1.

В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-2:

- Адрес назначения: 10.3.3.0/24.
- VPC: VPC-1.
- Зона доступности: ru.AZ-2.

Адрес назначения: 10.3.3.0/24.

VPC: VPC-1.

Зона доступности: ru.AZ-2.

В сервисе Magic Router [создайте маршрут](https://cloud.ru/docs/magic-router/ug/topics/guides__routes-create)создайте маршрут к подсети subnet-3:

- Адрес назначения: 10.2.2.0/24.
- VPC: VPC-2.
- Зона доступности: ru.AZ-1.

Адрес назначения: 10.2.2.0/24.

VPC: VPC-2.

Зона доступности: ru.AZ-1.

Убедитесь, что в сервисе Magic Router на странице Маршруты отображаются три маршрута в статусе «Создан».

## 4. Настройте маршруты для VPC

При создании маршрутов в VPC необходимо указывать зону доступности, в которой расположена подсеть этой VPC.
Если в VPC созданы подсети в нескольких зонах доступности, маршруты необходимо создать в каждой зоне доступности.

1. В сервисе Evolution VPC выберите VPC-1.

[Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

Адрес назначения: 10.2.2.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.

Создайте еще один маршрут с параметрами:

Адрес назначения: 10.2.2.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-2.

Убедитесь, что для VPC-1 на странице Маршруты отображаются два маршрута в статусе «Активен».
2. В сервисе Evolution VPC выберите VPC-2.

[Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

Адрес назначения: 10.1.1.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.

Создайте еще один маршрут с параметрами:

Адрес назначения: 10.3.3.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.

Убедитесь, что для VPC-2 на странице Маршруты отображаются два маршрута в статусе «Активен».

В сервисе Evolution VPC выберите VPC-1.

1. [Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

Адрес назначения: 10.2.2.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.
2. Создайте еще один маршрут с параметрами:

Адрес назначения: 10.2.2.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-2.

[Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

- Адрес назначения: 10.2.2.0/24.
- Next Hop Type: Magic Router.
- Зона доступности: ru.AZ-1.

Адрес назначения: 10.2.2.0/24.

Next Hop Type: Magic Router.

Зона доступности: ru.AZ-1.

Создайте еще один маршрут с параметрами:

- Адрес назначения: 10.2.2.0/24.
- Next Hop Type: Magic Router.
- Зона доступности: ru.AZ-2.

Адрес назначения: 10.2.2.0/24.

Next Hop Type: Magic Router.

Зона доступности: ru.AZ-2.

Убедитесь, что для VPC-1 на странице Маршруты отображаются два маршрута в статусе «Активен».

В сервисе Evolution VPC выберите VPC-2.

1. [Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

Адрес назначения: 10.1.1.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.
2. Создайте еще один маршрут с параметрами:

Адрес назначения: 10.3.3.0/24.
Next Hop Type: Magic Router.
Зона доступности: ru.AZ-1.

[Создайте пользовательский маршрут](https://cloud.ru/docs/evolution-vpc/ug/topics/guides__add-custom-route)Создайте пользовательский маршрут с параметрами:

- Адрес назначения: 10.1.1.0/24.
- Next Hop Type: Magic Router.
- Зона доступности: ru.AZ-1.

Адрес назначения: 10.1.1.0/24.

Next Hop Type: Magic Router.

Зона доступности: ru.AZ-1.

Создайте еще один маршрут с параметрами:

- Адрес назначения: 10.3.3.0/24.
- Next Hop Type: Magic Router.
- Зона доступности: ru.AZ-1.

Адрес назначения: 10.3.3.0/24.

Next Hop Type: Magic Router.

Зона доступности: ru.AZ-1.

Убедитесь, что для VPC-2 на странице Маршруты отображаются два маршрута в статусе «Активен».

## 5. Настройте правила групп безопасности

1. Выберите сервис Группы безопасности.
2. Для группы безопасности SSH-access_ru.AZ-1 [создайте правило](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте правило для входящего трафика с параметрами:

Протокол: ICMP.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.
3. Для группы безопасности SSH-access_ru.AZ-2 [создайте правило](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте правило для входящего трафика с параметрами:

Протокол: ICMP.
Тип источника: IP-адрес.
Источник: 0.0.0.0/0.

Выберите сервис Группы безопасности.

Для группы безопасности SSH-access_ru.AZ-1 [создайте правило](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте правило для входящего трафика с параметрами:

- Протокол: ICMP.
- Тип источника: IP-адрес.
- Источник: 0.0.0.0/0.

Протокол: ICMP.

Тип источника: IP-адрес.

Источник: 0.0.0.0/0.

Для группы безопасности SSH-access_ru.AZ-2 [создайте правило](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте правило для входящего трафика с параметрами:

- Протокол: ICMP.
- Тип источника: IP-адрес.
- Источник: 0.0.0.0/0.

Протокол: ICMP.

Тип источника: IP-адрес.

Источник: 0.0.0.0/0.

## 6. Проверьте сетевую связность

1. Подключитесь к любой виртуальной машине [через виртуальную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console)через виртуальную консоль.
2. Чтобы проверить сетевую связность с оставшимися виртуальными машинами, выполните команду:
ping <IP>

Где IP — IP-адрес виртуальной машины, с которой надо проверить сетевую связность.

Подключитесь к любой виртуальной машине [через виртуальную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console)через виртуальную консоль.

Чтобы проверить сетевую связность с оставшимися виртуальными машинами, выполните команду:

```bash
ping
<
IP
>
```

Где IP — IP-адрес виртуальной машины, с которой надо проверить сетевую связность.

## Результат

Вы настроили сетевую связность между виртуальными машинами из разных VPC, принадлежащих одному проекту.
Вы получили опыт работы с соединениями, маршрутами и правилами групп безопасности.
