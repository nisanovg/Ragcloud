---
title: Создать бэкап в Object Storage по расписанию в ADBC
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/arenadata-db__adbc-backup
topic: dataplatform
---
# Создать бэкап в Object Storage по расписанию в ADBC

С помощью этого руководства вы настроите бэкапы по расписанию и восстановите исходные данные.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис для создания инстансов распределенной аналитической СУБД ArenadataDB, основанной на решении Greenplum®.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Managed ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/index)Managed ArenadataDB — сервис для создания инстансов распределенной аналитической СУБД ArenadataDB, основанной на решении Greenplum®.

## Постановка задачи

1. Внести данные в ArenadataDB.
2. Настроить бэкап по расписанию.
3. Изменить данные и восстановить первоначальный вариант.

Внести данные в ArenadataDB.

Настроить бэкап по расписанию.

Изменить данные и восстановить первоначальный вариант.

## Перед началом работы

[Выполните шаги из практического руководства Работа с данными в ArenadataDB](https://cloud.ru/docs/arenadata-db/ug/topics/tutorials__adb-dbeaver)Выполните шаги из практического руководства Работа с данными в ArenadataDB.

## 1. Создайте бакет Object Storage

1. [Создайте бакет по инструкции](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет по инструкции.
2. [Создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)Создайте папку с названием «repo_adb».
В ней будут храниться файлы бэкапов.
3. [Сгенерируйте Key ID и Key Secret сервисного аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте Key ID и Key Secret сервисного аккаунта и сохраните их.
Они понадобятся для подключения бакета Object Storage к ADB.

[Создайте бакет по инструкции](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет по инструкции.

[Создайте папку](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_create-folder)Создайте папку с названием «repo_adb».
В ней будут храниться файлы бэкапов.

[Сгенерируйте Key ID и Key Secret сервисного аккаунта](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте Key ID и Key Secret сервисного аккаунта и сохраните их.
Они понадобятся для подключения бакета Object Storage к ADB.

## 2. Создайте расписание для бэкапа

Действия выполняются [в интерфейсе ADBC](https://cloud.ru/docs/arenadata-db/ug/topics/guides__instance-ui)в интерфейсе ADBC.

1. В интерфейсе ADBC в меню слева выберите Backup Manager.
2. В разделе Clusters нажмите на название кластера ADB.
3. Откройте вкладку Configuration.
4. Создайте конфигурацию.
5. Заполните поля:

В разделе General configuration введите:

Full Backup schedule — свое актуальное время и добавьте к нему 5 минут в формате <sec> <min> <hour> ? * <day> *, где:

<sec> — секунда начала бэкапа.
<min> — минута начала бэкапа.
<hour> — час начала бэкапа.
<day> — день недели, когда начинается бэкап.
Например, MON для понедельника.

Допустим, мы проходим лабораторную работу в среду в 17:25 по GMT+0.
Тогда введем значение 0 30 17 ? * WED * — [полное резервное копирование](https://cloud.ru/docs/glossary/list/index)полное резервное копирование будет начинаться в 17:30 каждую среду.
Запомните введенное время.

В разделе Repository:

Repository type — выберите S3.
URI type — выберите Host.
Repository Path — введите /repo_adb.
Endpoint — введите https://s3.cloud.ru.
Bucket — введите глобальное название бакета.
Key — введите ID тенанта и ключ доступа сервисного аккаунта в виде <Tenant ID>:<Key ID>.

Tennant ID — скопируйте из поля ID тенанта на карточке бакета Object Storage.
Key ID — сохраненный Key ID сервисного аккаунта.

Key secret — введите Key Secret сервисного аккаунта.
Region — введите ru-central-1, если используете бакет Object Storage, или регион внешнего бакета, если используете хранилище другого провайдера.
6. Нажмите Save.

В интерфейсе ADBC в меню слева выберите Backup Manager.

В разделе Clusters нажмите на название кластера ADB.

Откройте вкладку Configuration.

Создайте конфигурацию.

Заполните поля:

1. В разделе General configuration введите:

Full Backup schedule — свое актуальное время и добавьте к нему 5 минут в формате <sec> <min> <hour> ? * <day> *, где:

<sec> — секунда начала бэкапа.
<min> — минута начала бэкапа.
<hour> — час начала бэкапа.
<day> — день недели, когда начинается бэкап.
Например, MON для понедельника.

Допустим, мы проходим лабораторную работу в среду в 17:25 по GMT+0.
Тогда введем значение 0 30 17 ? * WED * — [полное резервное копирование](https://cloud.ru/docs/glossary/list/index)полное резервное копирование будет начинаться в 17:30 каждую среду.
Запомните введенное время.
2. В разделе Repository:

Repository type — выберите S3.
URI type — выберите Host.
Repository Path — введите /repo_adb.
Endpoint — введите https://s3.cloud.ru.
Bucket — введите глобальное название бакета.
Key — введите ID тенанта и ключ доступа сервисного аккаунта в виде <Tenant ID>:<Key ID>.

Tennant ID — скопируйте из поля ID тенанта на карточке бакета Object Storage.
Key ID — сохраненный Key ID сервисного аккаунта.

Key secret — введите Key Secret сервисного аккаунта.
Region — введите ru-central-1, если используете бакет Object Storage, или регион внешнего бакета, если используете хранилище другого провайдера.

В разделе General configuration введите:

- Full Backup schedule — свое актуальное время и добавьте к нему 5 минут в формате <sec> <min> <hour> ? * <day> *, где:

<sec> — секунда начала бэкапа.
<min> — минута начала бэкапа.
<hour> — час начала бэкапа.
<day> — день недели, когда начинается бэкап.
Например, MON для понедельника.

Допустим, мы проходим лабораторную работу в среду в 17:25 по GMT+0.
Тогда введем значение 0 30 17 ? * WED * — [полное резервное копирование](https://cloud.ru/docs/glossary/list/index)полное резервное копирование будет начинаться в 17:30 каждую среду.
Запомните введенное время.

Full Backup schedule — свое актуальное время и добавьте к нему 5 минут в формате <sec> <min> <hour> ? * <day> *, где:

- <sec> — секунда начала бэкапа.
- <min> — минута начала бэкапа.
- <hour> — час начала бэкапа.
- <day> — день недели, когда начинается бэкап.
Например, MON для понедельника.

<sec> — секунда начала бэкапа.

<min> — минута начала бэкапа.

<hour> — час начала бэкапа.

<day> — день недели, когда начинается бэкап.
Например, MON для понедельника.

Допустим, мы проходим лабораторную работу в среду в 17:25 по GMT+0.
Тогда введем значение 0 30 17 ? * WED * —

Запомните введенное время.

В разделе Repository:

- Repository type — выберите S3.
- URI type — выберите Host.
- Repository Path — введите /repo_adb.
- Endpoint — введите https://s3.cloud.ru.
- Bucket — введите глобальное название бакета.
- Key — введите ID тенанта и ключ доступа сервисного аккаунта в виде <Tenant ID>:<Key ID>.

Tennant ID — скопируйте из поля ID тенанта на карточке бакета Object Storage.
Key ID — сохраненный Key ID сервисного аккаунта.
- Key secret — введите Key Secret сервисного аккаунта.
- Region — введите ru-central-1, если используете бакет Object Storage, или регион внешнего бакета, если используете хранилище другого провайдера.

Repository type — выберите S3.

URI type — выберите Host.

Repository Path — введите /repo_adb.

Endpoint — введите https://s3.cloud.ru.

Bucket — введите глобальное название бакета.

Key — введите ID тенанта и ключ доступа сервисного аккаунта в виде <Tenant ID>:<Key ID>.

- Tennant ID — скопируйте из поля ID тенанта на карточке бакета Object Storage.
- Key ID — сохраненный Key ID сервисного аккаунта.

Tennant ID — скопируйте из поля ID тенанта на карточке бакета Object Storage.

Key ID — сохраненный Key ID сервисного аккаунта.

Key secret — введите Key Secret сервисного аккаунта.

Region — введите ru-central-1, если используете бакет Object Storage, или регион внешнего бакета, если используете хранилище другого провайдера.

Нажмите Save.

Бэкап по расписанию появится в бакете Object Storage через несколько минут после введенного в поле Full Backup schedule времени.
Перед следующим шагом убедитесь, что действие завершено и в бакете появились файлы бэкапа.

Чтобы отслеживать статус действий в ADBC:

1. В интерфейсе ADBC в меню слева выберите Backup Manager.
2. В разделе Clusters нажмите на название кластера ArenadataDB.
3. Откройте вкладку Actions.

В интерфейсе ADBC в меню слева выберите Backup Manager.

В разделе Clusters нажмите на название кластера ArenadataDB.

Откройте вкладку Actions.

## 3. Удалите данные в таблице

После того как придет время полного бэкапа по расписанию и в бакете Object Storage появятся файлы, в DBeaver выполните команду, чтобы удалить всю таблицу с данными:

```bash
DELETE FROM adb.lab.employees
;
```

## 4. Восстановите данные

1. В интерфейсе ADBC в меню слева выберите Backup Manager.
2. В разделе Clusters нажмите на название кластера ADB.
3. Откройте вкладку Restores.
4. Нажмите .
5. Выберите Restore.
6. В поле Restore point выберите первую строчку.
7. Нажмите Run.
8. Когда восстановление завершится, в DBeaver обновите базу данных.
Удаленная таблица восстановится.

В интерфейсе ADBC в меню слева выберите Backup Manager.

В разделе Clusters нажмите на название кластера ADB.

Откройте вкладку Restores.

Нажмите .

![Кнопка Опции](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/adb-ui-options.png)

Выберите Restore.

В поле Restore point выберите первую строчку.

Нажмите Run.

Когда восстановление завершится, в DBeaver обновите базу данных.
Удаленная таблица восстановится.

Чтобы отслеживать статус действий в ADBC:

1. В интерфейсе ADBC в меню слева выберите Backup Manager.
2. В разделе Clusters нажмите на название кластера ArenadataDB.
3. Откройте вкладку Actions.

В интерфейсе ADBC в меню слева выберите Backup Manager.

В разделе Clusters нажмите на название кластера ArenadataDB.

Откройте вкладку Actions.

## Результат

С этим руководством вы настроили бэкапы для инстанса Managed ArenadataDB и проверили их работу на примере создания и удаления таблицы.

## Что дальше

Вы можете [сделать бэкап вручную](https://cloud.ru/docs/arenadata-db/ug/topics/guides__ui-backup-manual)сделать бэкап вручную и узнать больше [о бэкапах в ADB](https://cloud.ru/docs/arenadata-db/ug/topics/concepts__backup)о бэкапах в ADB.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
