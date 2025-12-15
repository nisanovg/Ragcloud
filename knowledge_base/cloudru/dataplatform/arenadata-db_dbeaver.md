---
title: Работа с данными в Managed ArenadataDB
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__dbeaver
topic: dataplatform
---
# Работа с данными в Managed ArenadataDB

С помощью этого руководства вы подключите инстанс Managed ArenadataDB по внешнему IP к JDBC-клиенту DBeaver.

## Постановка задачи

1. Развернуть инстанс с публичным IP.
2. Подключить DBeaver к инстансу.
3. Внести данные в базу данных через DBeaver.

Развернуть инстанс с публичным IP.

Подключить DBeaver к инстансу.

Внести данные в базу данных через DBeaver.

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
5. Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

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

Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

## 1. Создайте инстанс ArenadataDB

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
Подключить публичный хост — активируйте опцию.
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
- Подключить публичный хост — активируйте опцию.

VPC —

Зона доступности —

sNAT-шлюз — шлюз.

Подсеть — подсеть.

Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.

Подключить публичный хост — активируйте опцию.

Нажмите Продолжить.

В блоке Логирование выберите:

- Лог-группа — группу с созданными DNS-серверами.
- Сервисный аккаунт — сервисный аккаунт.

Лог-группа — группу с созданными DNS-серверами.

Сервисный аккаунт — сервисный аккаунт.

Нажмите Создать.

Инстанс ArenadataDB отобразится на странице сервиса.
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

Логин и пароль понадобятся для подключения в JDBC-клиенте.

## 3. Подключите ArenadataDB к JDBC-клиенту

1. В списке инстансов откройте карточку инстанса.
Информация из нее понадобится для подключения к DBeaver.
2. Запустите DBeaver.
3. В панели сверху нажмите База данных → Новое соединение.
4. В списке соединений выберите Greenplum.
5. Нажмите Далее.
6. На вкладке Главное введите данные из карточки инстанса:

Хост
Порт
Пользователь
Пароль
7. Нажмите Готово.

В списке инстансов откройте карточку инстанса.
Информация из нее понадобится для подключения к DBeaver.

Запустите DBeaver.

В панели сверху нажмите База данных → Новое соединение.

В списке соединений выберите Greenplum.

Нажмите Далее.

На вкладке Главное введите данные из карточки инстанса:

- Хост
- Порт
- Пользователь
- Пароль

Хост

Порт

Пользователь

Пароль

Нажмите Готово.

## 4. Выполните SQL-запросы

Следующие действия выполняются в DBeaver:

1. Чтобы создать структуру и таблицу, выполните запросы:
CREATE SCHEMA IF NOT EXISTS adb.lab;
CREATE TABLE IF NOT EXISTS adb.lab.employees (id_user INT, email VARCHAR(255));
INSERT INTO adb.lab.employees values (1, 'one@example.com'), (2, 'two@example.com'), (3, 'three@example.com');
2. Чтобы ввести новые данные в таблицу, выполните запрос:
INSERT INTO adb.lab.employees values (4, 'four@example.com'), (5, 'five@example.com'), (6, 'six@example.com');
3. Чтобы проверить, что данные добавлены в таблицу, выполните запрос:
SELECT * FROM adb.lab.employees;

Чтобы создать структуру и таблицу, выполните запросы:

```bash
CREATE SCHEMA IF NOT EXISTS adb.lab
;
CREATE TABLE IF NOT EXISTS adb.lab.employees
(
id_user INT, email VARCHAR
(
255
))
;
INSERT INTO adb.lab.employees values
(
1
,
'one@example.com'
)
,
(
2
,
'two@example.com'
)
,
(
3
,
'three@example.com'
)
;
```

Чтобы ввести новые данные в таблицу, выполните запрос:

```bash
INSERT INTO adb.lab.employees values
(
4
,
'four@example.com'
)
,
(
5
,
'five@example.com'
)
,
(
6
,
'six@example.com'
)
;
```

Чтобы проверить, что данные добавлены в таблицу, выполните запрос:

```bash
SELECT * FROM adb.lab.employees
;
```

## Результат

С этим руководством вы создали инстанс Managed ArenadataDB, подключили его к JDBC-клиенту DBeaver и отправили SQL-запросы.

## Что дальше

Далее вы можете настроить бэкапы по расписанию в рамках практического руководства [Создание бэкапа по расписанию в ADBC](https://cloud.ru/docs/arenadata-db/ug/topics/tutorials__adbc-backup)Создание бэкапа по расписанию в ADBC.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
