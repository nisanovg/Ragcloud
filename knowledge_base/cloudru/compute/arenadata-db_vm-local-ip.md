---
title: Подключение к Managed ArenadataDB через ВМ по локальной сети
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__vm-local-ip
topic: compute
---
# Подключение к Managed ArenadataDB через ВМ по локальной сети

С помощью этого руководства вы развернете инстанс Managed ArenadataDB, создадите виртуальную машину (ВМ), подключите ВМ к Managed ArenadataDB.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина
- [Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис для создания инстансов распределенной аналитической СУБД ArenadataDB, основанной на решении Greenplum®.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина

[Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис для создания инстансов распределенной аналитической СУБД ArenadataDB, основанной на решении Greenplum®.

## Постановка задачи

Необходимо подключиться к инстансу Managed ArenadataDB, не публикуя инстанс в интернет, используя [Виртуальную машину Evolution](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальную машину Evolution и внутреннюю сеть.

## Перед началом работы

1. [Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/quickstart)Создайте публичный SNAT-шлюз в той зоне доступности, в которой собираетесь создавать кластер.
2. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности для инстанса ArenadataDB.
В этой группе безопасности [создайте разрешающие правила](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте разрешающие правила для:

входящего трафика в подсети инстанса ArenadataDB;
исходящего трафика в подсети инстанса ArenadataDB;
[ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB порт 5432;
[ArenadataDB Control](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB Control порт 81;
[Arenadata Cluster Manager](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)Arenadata Cluster Manager порт 8080.
3. [Создайте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте лог-группу.
В этой лог-группе [создайте два DNS-сервера](https://cloud.ru/docs/evolution-dns/ug/topics/guides__add-server)создайте два DNS-сервера:

8.8.8.8
8.8.4.4
4. Установите клиент для подключения к базам данных по протоколу JDBC, например DBeaver.

[Создайте публичный SNAT-шлюз](https://cloud.ru/docs/gateways/ug/topics/quickstart)Создайте публичный SNAT-шлюз в той зоне доступности, в которой собираетесь создавать кластер.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности для инстанса ArenadataDB.

В этой группе безопасности [создайте разрешающие правила](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)создайте разрешающие правила для:

- входящего трафика в подсети инстанса ArenadataDB;
- исходящего трафика в подсети инстанса ArenadataDB;
- [ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB порт 5432;
- [ArenadataDB Control](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB Control порт 81;
- [Arenadata Cluster Manager](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)Arenadata Cluster Manager порт 8080.

входящего трафика в подсети инстанса ArenadataDB;

исходящего трафика в подсети инстанса ArenadataDB;

[ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB порт 5432;

[ArenadataDB Control](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)ArenadataDB Control порт 81;

[Arenadata Cluster Manager](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)Arenadata Cluster Manager порт 8080.

[Создайте лог-группу](https://cloud.ru/docs/client-log/ug/topics/working-groups)Создайте лог-группу.

В этой лог-группе [создайте два DNS-сервера](https://cloud.ru/docs/evolution-dns/ug/topics/guides__add-server)создайте два DNS-сервера:

- 8.8.8.8
- 8.8.4.4

8.8.8.8

8.8.4.4

Установите клиент для подключения к базам данных по протоколу JDBC, например DBeaver.

## 1. Создайте инстанс Managed ArenadataDB

1. Перейдите в раздел Evolution и выберите сервис Managed ArenadataDB.
2. В блоке Общие параметры заполните поля:

Название — adb-lab.
Тип лицензии — Test.
Объем хранения данных, ТБ — 3 ТБ.
3. Нажмите Продолжить.
4. В блоке Сетевые настройки выберите:

VPC — [виртуальную сеть](https://cloud.ru/docs/glossary/list/index)виртуальную сеть.
Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности.
sNAT-шлюз — шлюз.
Подсеть — подсеть.
Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.
5. Нажмите Продолжить.
6. В блоке Логирование выберите:

Лог-группа — группу с созданными DNS-серверами.
Сервисный аккаунт — сервисный аккаунт.
7. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed ArenadataDB.

В блоке Общие параметры заполните поля:

- Название — adb-lab.
- Тип лицензии — Test.
- Объем хранения данных, ТБ — 3 ТБ.

Название — adb-lab.

Тип лицензии — Test.

Объем хранения данных, ТБ — 3 ТБ.

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- VPC — [виртуальную сеть](https://cloud.ru/docs/glossary/list/index)виртуальную сеть.
- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности.
- sNAT-шлюз — шлюз.
- Подсеть — подсеть.
- Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.

VPC —

Зона доступности —

sNAT-шлюз — шлюз.

Подсеть — подсеть.

Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.

Нажмите Продолжить.

В блоке Логирование выберите:

- Лог-группа — группу с созданными DNS-серверами.
- Сервисный аккаунт — сервисный аккаунт.

Лог-группа — группу с созданными DNS-серверами.

Сервисный аккаунт — сервисный аккаунт.

Нажмите Создать.

Инстанс Managed ArenadataDB отобразится на странице сервиса.
Создание может занять от 40 минут в зависимости от выбранной конфигурации.

## 2. Получите логин и пароль

Когда статус инстанса изменится на «Готов»:

1. Откройте карточку инстанса.
2. На вкладке Доступы в блоке Доступ к ADB нажмите Получить логин и пароль.
3. Cохраните логин и пароль.
ВниманиеЛогин и пароль отображаются один раз.В целях безопасности рекомендуем изменить пароль.
Сделать это можно [в интерфейсе ADCM](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)в интерфейсе ADCM.
4. Нажмите Принято.

Откройте карточку инстанса.

На вкладке Доступы в блоке Доступ к ADB нажмите Получить логин и пароль.

Cохраните логин и пароль.

Логин и пароль отображаются один раз.

В целях безопасности рекомендуем изменить пароль.
Сделать это можно [в интерфейсе ADCM](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)в интерфейсе ADCM.

Нажмите Принято.

Логин и пароль понадобятся для подключения к JDBC-клиенту.

## 3. Разверните виртуальную машину

1. [Создайте виртуальную машину по инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину по инструкции.

В поле Зона доступности выберите зону доступности, в которой располагается инстанс Managed ArenadataDB.
В сетевых настройках выберите опцию Подсеть.
В этом примере понадобится только внутренний IP.
В поле Подсеть выберите подсеть, в которой располагается инстанс Managed ArenadataDB.
2. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине.
3. [Обновите пакеты на виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__update-packages)Обновите пакеты на виртуальной машине.
4. Установите JDBC-клиент DBeaver на виртуальную машину:
sudo apt install dbeaver-ce

[Создайте виртуальную машину по инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину по инструкции.

- В поле Зона доступности выберите зону доступности, в которой располагается инстанс Managed ArenadataDB.
- В сетевых настройках выберите опцию Подсеть.
В этом примере понадобится только внутренний IP.
- В поле Подсеть выберите подсеть, в которой располагается инстанс Managed ArenadataDB.

В поле Зона доступности выберите зону доступности, в которой располагается инстанс Managed ArenadataDB.

В сетевых настройках выберите опцию Подсеть.
В этом примере понадобится только внутренний IP.

В поле Подсеть выберите подсеть, в которой располагается инстанс Managed ArenadataDB.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине.

[Обновите пакеты на виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__update-packages)Обновите пакеты на виртуальной машине.

Установите JDBC-клиент DBeaver на виртуальную машину:

```bash
sudo
apt
install
dbeaver-ce
```

## 4. Подключите Managed ArenadataDB к JDBC-клиенту

В следующих шагах используется графический интерфейс виртуальной машины.
Установите удаленный рабочий стол и подключитесь к ВМ.

1. В списке инстансов Managed ArenadataDB откройте карточку инстанса.
Информация из нее понадобится для подключения к DBeaver.
2. Запустите удаленный рабочий стол для доступа к графическому интерфейсу виртуальной машины.
3. На виртуальной машине запустите DBeaver.
4. В панели сверху нажмите База данных → Новое соединение.
5. В списке соединений выберите Greenplum.
6. Нажмите Далее.
7. На вкладке Главное введите данные из карточки инстанса:

Хост — внутренний IP
Порт
Пользователь
Пароль
8. Нажмите Готово.

В списке инстансов Managed ArenadataDB откройте карточку инстанса.
Информация из нее понадобится для подключения к DBeaver.

Запустите удаленный рабочий стол для доступа к графическому интерфейсу виртуальной машины.

На виртуальной машине запустите DBeaver.

В панели сверху нажмите База данных → Новое соединение.

В списке соединений выберите Greenplum.

Нажмите Далее.

На вкладке Главное введите данные из карточки инстанса:

- Хост — внутренний IP
- Порт
- Пользователь
- Пароль

Хост — внутренний IP

Порт

Пользователь

Пароль

Нажмите Готово.

## Результат

С этим руководством вы создали инстанс Managed ArenadataDB и виртуальную машину, настроили соединение в JDBC-клиенте DBeaver.

## Что дальше

Далее вы можете настроить бэкапы по расписанию в рамках практического руководства [Создание бэкапа по расписанию в ADBC](https://cloud.ru/docs/arenadata-db/ug/topics/tutorials__adbc-backup)Создание бэкапа по расписанию в ADBC.
