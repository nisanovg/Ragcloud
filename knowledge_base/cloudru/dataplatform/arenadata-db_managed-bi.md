---
title: Подключение Managed ArenadataDB к Managed BI
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi
topic: dataplatform
---
# Подключение Managed ArenadataDB к Managed BI

С помощью этого руководства вы научитесь загружать данные в Managed ArenadataDB через JDBC-клиент DBeaver и визуализировать их в Managed BI.

Вы будете использовать следующие сервисы:

- [Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис, который позволяет разворачивать кластеры ArenadataDB и управлять ими без необходимости настраивать и обслуживать инфраструктуру.
- [Managed BI](https://cloud.ru/docs/managed-bi/ug/index)Managed BI — сервис для визуализации и анализа данных.

[Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис, который позволяет разворачивать кластеры ArenadataDB и управлять ими без необходимости настраивать и обслуживать инфраструктуру.

[Managed BI](https://cloud.ru/docs/managed-bi/ug/index)Managed BI — сервис для визуализации и анализа данных.

Шаги:

1. [Создайте инстанс Managed BI](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Создайте инстанс Managed BI.
2. [Создайте инстанс Managed ArenadataDB](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Создайте инстанс Managed ArenadataDB.
3. [Получите логин и пароль](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Получите логин и пароль.
4. [Подключите инстанс Managed ArenadataDB к DBeaver](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Подключите инстанс Managed ArenadataDB к DBeaver.
5. [Подключите Managed BI к базе данных](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Подключите Managed BI к базе данных.
6. [Переходите к визуализации данных](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Переходите к визуализации данных.

[Создайте инстанс Managed BI](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Создайте инстанс Managed BI.

[Создайте инстанс Managed ArenadataDB](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Создайте инстанс Managed ArenadataDB.

[Получите логин и пароль](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Получите логин и пароль.

[Подключите инстанс Managed ArenadataDB к DBeaver](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Подключите инстанс Managed ArenadataDB к DBeaver.

[Подключите Managed BI к базе данных](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Подключите Managed BI к базе данных.

[Переходите к визуализации данных](https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__managed-bi)Переходите к визуализации данных.

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
4. [Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.
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

[Создайте кластер Data Platform](https://cloud.ru/docs/dataplatform/ug/topics/guides__create)Создайте кластер Data Platform, в котором будет размещен инстанс.

Установите JDBC-клиент [DBeaver](https://dbeaver.io/download)DBeaver.

## 1. Создайте инстанс Managed BI

1. Перейдите в раздел Evolution и выберите сервис Managed BI.
2. Нажмите Создать инстанс.
3. В поле Кластер выберите созданный ранее кластер.
4. В поле Вычислительные ресурсы выберите «vCPU 2, RAM 4».
5. Нажмите Продолжить.
6. В блоке Сетевые настройки выберите:

Подсеть — выберите созданную подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
Группа безопасности — выберите созданную группу безопасности.
7. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed BI.

Нажмите Создать инстанс.

В поле Кластер выберите созданный ранее кластер.

В поле Вычислительные ресурсы выберите «vCPU 2, RAM 4».

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- Подсеть — выберите созданную подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.
- Группа безопасности — выберите созданную группу безопасности.

Подсеть — выберите созданную подсеть [с DNS-сервером](https://cloud.ru/docs/dataplatform/ug/topics/guides__dns)с DNS-сервером.

Группа безопасности — выберите созданную группу безопасности.

Нажмите Создать.

Создание инстанса занимает около 15 минут.

## 2. Создайте инстанс Managed ArenadataDB

1. Перейдите в раздел Evolution и выберите сервис Managed ArenadataDB.
2. В блоке Общие параметры заполните поля:

Название — adb-lab.
Тип лицензии — Test.
Версия ArenadataDB — 6.25.1.49.
Объем хранения данных, ТБ — 3 ТБ.
3. Нажмите Продолжить.
4. В блоке Сетевые настройки выберите:

VPC — [виртуальную сеть](https://cloud.ru/docs/glossary/list/index)виртуальную сеть.
Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности.
sNAT-шлюз — созданный шлюз.
Подсеть — подсеть c созданными DNS-серверами.
Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.
Подключить публичный хост — активируйте опцию.
5. Нажмите Продолжить.
6. В блоке Логирование выберите:

Лог-группа — группу логов с созданными ранее DNS-серверами.
Сервисный аккаунт — сервисный аккаунт.
7. Нажмите Создать.

Перейдите в раздел Evolution и выберите сервис Managed ArenadataDB.

В блоке Общие параметры заполните поля:

- Название — adb-lab.
- Тип лицензии — Test.
- Версия ArenadataDB — 6.25.1.49.
- Объем хранения данных, ТБ — 3 ТБ.

Название — adb-lab.

Тип лицензии — Test.

Версия ArenadataDB — 6.25.1.49.

Объем хранения данных, ТБ — 3 ТБ.

Нажмите Продолжить.

В блоке Сетевые настройки выберите:

- VPC — [виртуальную сеть](https://cloud.ru/docs/glossary/list/index)виртуальную сеть.
- Зона доступности — [зону доступности](https://cloud.ru/docs/glossary/list/index)зону доступности.
- sNAT-шлюз — созданный шлюз.
- Подсеть — подсеть c созданными DNS-серверами.
- Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.
- Подключить публичный хост — активируйте опцию.

VPC —

Зона доступности —

sNAT-шлюз — созданный шлюз.

Подсеть — подсеть c созданными DNS-серверами.

Группа безопасности — созданную группу безопасности с [разрешающими правилами](https://cloud.ru/docs/security-groups/ug/topics/guides__add-sg-rule)разрешающими правилами.

Подключить публичный хост — активируйте опцию.

Нажмите Продолжить.

В блоке Логирование выберите:

- Лог-группа — группу логов с созданными ранее DNS-серверами.
- Сервисный аккаунт — сервисный аккаунт.

Лог-группа — группу логов с созданными ранее DNS-серверами.

Сервисный аккаунт — сервисный аккаунт.

Нажмите Создать.

Инстанс Managed ArenadataDB отобразится на странице сервиса.
Создание может занять от 40 минут в зависимости от выбранной конфигурации.

## 3. Получите логин и пароль

Когда статус инстанса Managed ArenadataDB изменится на «Готов»:

1. Откройте карточку инстанса Managed ArenadataDB.
2. На вкладке Доступы в блоке Доступ к ADB нажмите Получить логин и пароль.
3. Cохраните логин и пароль.
ВниманиеЛогин и пароль отображаются один раз.В целях безопасности рекомендуем изменить пароль.
Сделать это можно [в интерфейсе ADCM](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)в интерфейсе ADCM.
4. Нажмите Принято.

Откройте карточку инстанса Managed ArenadataDB.

На вкладке Доступы в блоке Доступ к ADB нажмите Получить логин и пароль.

Cохраните логин и пароль.

Логин и пароль отображаются один раз.

В целях безопасности рекомендуем изменить пароль.
Сделать это можно [в интерфейсе ADCM](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)в интерфейсе ADCM.

Нажмите Принято.

Логин и пароль понадобятся для настройки дальнейших подключений.

## 4. Подключите инстанс Managed ArenadataDB к DBeaver

1. В списке инстансов Managed ArenadataDB откройте карточку созданного ранее инстанса.
Перейдите на вкладку Доступы.
Информация из нее понадобится для подключения к DBeaver.
2. Запустите DBeaver.
3. В панели сверху нажмите База данных → Новое соединение.
4. В списке соединений выберите PostgreSQL или Greenplum.
5. На вкладке Главное введите:

Хост — публичный хост из карточки инстанса Managed ArenadataDB;
База данных — adb;
Пользователь — сохраненный ранее логин;
Пароль — сохраненный ранее пароль.
6. Нажмите Готово. На левой панели в списке баз данных появится база adb.
7. Откройте Базы данных → adb → Схемы → public → Таблицы.
8. Нажмите на название таблицы в этой папке, чтобы убедиться, что данные из нее отображаются.

В списке инстансов Managed ArenadataDB откройте карточку созданного ранее инстанса.
Перейдите на вкладку Доступы.
Информация из нее понадобится для подключения к DBeaver.

Запустите DBeaver.

В панели сверху нажмите База данных → Новое соединение.

В списке соединений выберите PostgreSQL или Greenplum.

На вкладке Главное введите:

- Хост — публичный хост из карточки инстанса Managed ArenadataDB;
- База данных — adb;
- Пользователь — сохраненный ранее логин;
- Пароль — сохраненный ранее пароль.

Хост — публичный хост из карточки инстанса Managed ArenadataDB;

База данных — adb;

Пользователь — сохраненный ранее логин;

Пароль — сохраненный ранее пароль.

Нажмите Готово. На левой панели в списке баз данных появится база adb.

Откройте Базы данных → adb → Схемы → public → Таблицы.

Нажмите на название таблицы в этой папке, чтобы убедиться, что данные из нее отображаются.

## 5. Подключите инстанс Managed BI к базе данных

1. Откройте сервис Managed BI в новой вкладке браузера.
2. Убедитесь, что статус созданного ранее инстанса Managed BI изменился на «Готов».
3. На карточке инстанса нажмите Перейти в интерфейс BI.
4. Откройте Настройки → Подключения.
5. Нажмите База данных и выберите PostgreSQL.
6. Введите данные:

Хост — внутренний IP из карточки инстанса Managed ArenadataDB;
Порт — номер порта из карточки инстанса Managed ArenadataDB;
Имя базы данных — adb;
Имя пользователя — сохраненный ранее логин;
Пароль — сохраненный ранее пароль;
Отображаемое имя — укажите имя для базы данных.
7. Нажмите Подключить.

Откройте сервис Managed BI в новой вкладке браузера.

Убедитесь, что статус созданного ранее инстанса Managed BI изменился на «Готов».

На карточке инстанса нажмите Перейти в интерфейс BI.

Откройте Настройки → Подключения.

Нажмите База данных и выберите PostgreSQL.

Введите данные:

- Хост — внутренний IP из карточки инстанса Managed ArenadataDB;
- Порт — номер порта из карточки инстанса Managed ArenadataDB;
- Имя базы данных — adb;
- Имя пользователя — сохраненный ранее логин;
- Пароль — сохраненный ранее пароль;
- Отображаемое имя — укажите имя для базы данных.

Хост — внутренний IP из карточки инстанса Managed ArenadataDB;

Порт — номер порта из карточки инстанса Managed ArenadataDB;

Имя базы данных — adb;

Имя пользователя — сохраненный ранее логин;

Пароль — сохраненный ранее пароль;

Отображаемое имя — укажите имя для базы данных.

Нажмите Подключить.

## 6. Переходите к визуализации данных

На этом шаге вы подключите датасет и создадите график, используя инструменты сервиса Managed BI.

1. Перейдите в раздел Датасеты.
2. Cправа сверху нажмите Датасет.
3. Введите данные:

База данных — выберите подключенную базу данных;
Схема — выберите public;
Таблица — выберите таблицу из списка, например, ad_table.
4. Нажмите Создать датасет и диаграмму.
5. Выберите тип графика — Таблица.
6. Нажмите Создать новый график.
7. Перетащите в поле Измерения идентификаторы нужных столбцов, например Maker, Adv_year, Color, Bodytype, Runned_Miles, Engin_size.
8. Проверьте получившуюся таблицу в поле предпросмотра и нажмите Сохранить.
9. Укажите имя графика и нажмите Сохранить.
10. Перейдите в раздел SQL → SQL Lab.
11. Введите данные:

База данных — выберите подключенную базу данных;
Схема — выберите public;
Таблица — выберите несколько таблиц из списка, например, ad_table, price_table, sales_table.
12. Нажмите Выполнить.
13. Нажмите Сохранить, укажите имя запроса и сохраните его.
14. Нажмите Создать график.
15. Выберите тип графика, например, Столбчатая диаграмма.
16. Перетащите идентификатор столбца Fuel_type в поле Ось Х.
17. Нажмите на название идентификатора в поле Ось Х и выберите вкладку Через SQL.
18. Укажите в поле "Fuel_type" и нажмите Сохранить.
19. Перетащите идентификатор столбца Fuel_type в поле Меры и нажмите на него для редактирования параметров.
20. На вкладке Столбец в поле Агрегатная функция выберите COUNT.
21. На вкладке Через SQL проверьте правильность запроса: COUNT("Fuel_type").
При необходимости внесите исправления и нажмите Сохранить.
22. В поле X-axis sort by выберите COUNT("Fuel_type").
23. Нажмите Обновить график.
24. Чтобы сохранить график, нажмите Сохранить и задайте имя графика.

Перейдите в раздел Датасеты.

Cправа сверху нажмите Датасет.

Введите данные:

- База данных — выберите подключенную базу данных;
- Схема — выберите public;
- Таблица — выберите таблицу из списка, например, ad_table.

База данных — выберите подключенную базу данных;

Схема — выберите public;

Таблица — выберите таблицу из списка, например, ad_table.

Нажмите Создать датасет и диаграмму.

Выберите тип графика — Таблица.

Нажмите Создать новый график.

Перетащите в поле Измерения идентификаторы нужных столбцов, например Maker, Adv_year, Color, Bodytype, Runned_Miles, Engin_size.

Проверьте получившуюся таблицу в поле предпросмотра и нажмите Сохранить.

Укажите имя графика и нажмите Сохранить.

Перейдите в раздел SQL → SQL Lab.

Введите данные:

- База данных — выберите подключенную базу данных;
- Схема — выберите public;
- Таблица — выберите несколько таблиц из списка, например, ad_table, price_table, sales_table.

База данных — выберите подключенную базу данных;

Схема — выберите public;

Таблица — выберите несколько таблиц из списка, например, ad_table, price_table, sales_table.

Нажмите Выполнить.

Нажмите Сохранить, укажите имя запроса и сохраните его.

Нажмите Создать график.

Выберите тип графика, например, Столбчатая диаграмма.

Перетащите идентификатор столбца Fuel_type в поле Ось Х.

Нажмите на название идентификатора в поле Ось Х и выберите вкладку Через SQL.

Укажите в поле "Fuel_type" и нажмите Сохранить.

Перетащите идентификатор столбца Fuel_type в поле Меры и нажмите на него для редактирования параметров.

На вкладке Столбец в поле Агрегатная функция выберите COUNT.

На вкладке Через SQL проверьте правильность запроса: COUNT("Fuel_type").
При необходимости внесите исправления и нажмите Сохранить.

В поле X-axis sort by выберите COUNT("Fuel_type").

Нажмите Обновить график.

Чтобы сохранить график, нажмите Сохранить и задайте имя графика.

## Результат

Вы научились подключаться к базам данных Managed ArenadataDB для загрузки данных с помощью JDBC-клиента DBeaver, подключать Managed ArenadataDB к Managed BI и пользоваться основными инструментами для визуализации данных.
