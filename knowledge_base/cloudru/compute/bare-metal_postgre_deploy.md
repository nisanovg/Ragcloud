---
title: Развертывание PostgreSQL на сервере Bare Metal
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy
topic: compute
---
# Развертывание PostgreSQL на сервере Bare Metal

С помощью этого руководства вы развернете СУБД PostgreSQL 15 на сервере Bare Metal с ОС Ubuntu 22.04.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Разверните инфраструктуру.
2. [Установите и настройте PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Установите и настройте PostgreSQL.
3. [Оптимизируйте настройки PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Оптимизируйте настройки PostgreSQL.
4. [Оптимизируйте настройки файловой системы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Оптимизируйте настройки файловой системы.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Разверните инфраструктуру.

[Установите и настройте PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Установите и настройте PostgreSQL.

[Оптимизируйте настройки PostgreSQL](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Оптимизируйте настройки PostgreSQL.

[Оптимизируйте настройки файловой системы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__postgre_deploy)Оптимизируйте настройки файловой системы.

## 1. Разверните инфраструктуру

1. [Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
Для корректной работы модели выбирайте конфигурации с объемом оперативной памяти более 32 ГБ.
2. [Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

[Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
Для корректной работы модели выбирайте конфигурации с объемом оперативной памяти более 32 ГБ.

[Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

## 2. Установите и настройте PostgreSQL

1. Установите PostgreSQL:
sudo apt updatesudo apt install postgresql
2. Переключитесь на профиль администратора PostgreSQL:
sudo su - postgres
3. Создайте базу данных и пользователя для нее:
createdb test_database \createuser -P test_user \psql -c "GRANT ALL PRIVILEGES ON DATABASE test_database TO test_user;"
4. Переключитесь на основного пользователя:
exit

Установите PostgreSQL:

```bash
sudo
apt
update
sudo
apt
install
postgresql
```

Переключитесь на профиль администратора PostgreSQL:

```bash
sudo
su
- postgres
```

Создайте базу данных и пользователя для нее:

```bash
createdb test_database
\
createuser
-P
test_user
\
psql
-c
"GRANT ALL PRIVILEGES ON DATABASE test_database TO test_user;"
```

Переключитесь на основного пользователя:

```bash
exit
```

## 3. Оптимизируйте настройки PostgreSQL

PostgreSQL по умолчанию содержит набор параметров для более тонкой настройки ее работы.
Например, вы можете увеличить производительность СУБД.

1. Откройте файл с конфигурацией СУБД:
sudo nano /etc/postgresql/<postrgesql_version>/main/postgresql.conf
2. Отредактируйте параметры в файле:
# 25% ОЗУshared_buffers = 16GB# 50-75% ОЗУeffective_cache_size = 48GB# 128MB–256 MBwork_mem = 256MB# 1-2 GBmaintenance_work_mem = 2GB# обычно достаточно 100–200max_connections = 150# для возможности репликацииwal_level = replica# для максимальной производительности# synchronous_commit = off# checkpoint_timeout = 30minmax_wal_size = 4GB

Где:

shared_buffers — определяет производительность СУБД. Увеличьте его до 25% от доступной оперативной памяти. Например, если у вас 64 ГБ ОЗУ, установите значение около 16 ГБ.
effective_cache_size — объем памяти, который резервируется под PostgreSQL в кэше ОС. Установите его на 50-75% от общей оперативной памяти.
work_mem — объем памяти, выделяемый для сортировки и хеширования операций. Увеличьте его до 128–256 МБ.
maintenance_work_mem — объем памяти для фоновых задач обслуживания, таких как «VACUUM» и «CREATE INDEX». Увеличьте его до 1-2 ГБ.
max_connections — лимит на соединения с СУБД. Устанавливайте исходя из предполагаемой нагрузки. Обычно достаточно 100–200 соединений.
wal_level — режим работы журнала предзаписи (WAL). Установите режим «replica», чтобы обеспечить возможность репликации БД в случае сбоя.
synchronous_commit — определяет, в какой момент транзакции считаются выполненными. Если вам важна максимальная производительность, установите значение «off». Однако это снизит надежность транзакций.
checkpoint_timeout — настраивает интервал между созданием контрольных точек восстановления. Для повышения производительности увеличьте этот интервал до 30 минут. Однако при сбое БД ее восстановление займет больше времени.
max_wal_size — управляет размером WAL-файлов. Увеличьте значение для больших рабочих нагрузок.

Откройте файл с конфигурацией СУБД:

```bash
sudo
nano
/etc/postgresql/
<
postrgesql_version
>
/main/postgresql.conf
```

Отредактируйте параметры в файле:

```bash
# 25% ОЗУ
shared_buffers
=
16GB
# 50-75% ОЗУ
effective_cache_size
=
48GB
# 128MB–256 MB
work_mem
=
256MB
# 1-2 GB
maintenance_work_mem
=
2GB
# обычно достаточно 100–200
max_connections
=
150
# для возможности репликации
wal_level
=
replica
# для максимальной производительности
# synchronous_commit = off
# checkpoint_timeout = 30min
max_wal_size
=
4GB
```

Где:

- shared_buffers — определяет производительность СУБД. Увеличьте его до 25% от доступной оперативной памяти. Например, если у вас 64 ГБ ОЗУ, установите значение около 16 ГБ.
- effective_cache_size — объем памяти, который резервируется под PostgreSQL в кэше ОС. Установите его на 50-75% от общей оперативной памяти.
- work_mem — объем памяти, выделяемый для сортировки и хеширования операций. Увеличьте его до 128–256 МБ.
- maintenance_work_mem — объем памяти для фоновых задач обслуживания, таких как «VACUUM» и «CREATE INDEX». Увеличьте его до 1-2 ГБ.
- max_connections — лимит на соединения с СУБД. Устанавливайте исходя из предполагаемой нагрузки. Обычно достаточно 100–200 соединений.
- wal_level — режим работы журнала предзаписи (WAL). Установите режим «replica», чтобы обеспечить возможность репликации БД в случае сбоя.
- synchronous_commit — определяет, в какой момент транзакции считаются выполненными. Если вам важна максимальная производительность, установите значение «off». Однако это снизит надежность транзакций.
- checkpoint_timeout — настраивает интервал между созданием контрольных точек восстановления. Для повышения производительности увеличьте этот интервал до 30 минут. Однако при сбое БД ее восстановление займет больше времени.
- max_wal_size — управляет размером WAL-файлов. Увеличьте значение для больших рабочих нагрузок.

shared_buffers — определяет производительность СУБД. Увеличьте его до 25% от доступной оперативной памяти. Например, если у вас 64 ГБ ОЗУ, установите значение около 16 ГБ.

effective_cache_size — объем памяти, который резервируется под PostgreSQL в кэше ОС. Установите его на 50-75% от общей оперативной памяти.

work_mem — объем памяти, выделяемый для сортировки и хеширования операций. Увеличьте его до 128–256 МБ.

maintenance_work_mem — объем памяти для фоновых задач обслуживания, таких как «VACUUM» и «CREATE INDEX». Увеличьте его до 1-2 ГБ.

max_connections — лимит на соединения с СУБД. Устанавливайте исходя из предполагаемой нагрузки. Обычно достаточно 100–200 соединений.

wal_level — режим работы журнала предзаписи (WAL). Установите режим «replica», чтобы обеспечить возможность репликации БД в случае сбоя.

synchronous_commit — определяет, в какой момент транзакции считаются выполненными. Если вам важна максимальная производительность, установите значение «off». Однако это снизит надежность транзакций.

checkpoint_timeout — настраивает интервал между созданием контрольных точек восстановления. Для повышения производительности увеличьте этот интервал до 30 минут. Однако при сбое БД ее восстановление займет больше времени.

max_wal_size — управляет размером WAL-файлов. Увеличьте значение для больших рабочих нагрузок.

## 4. Оптимизируйте настройки файловой системы

Вы также можете повысить производительность СУБД за счет оптимизации настроек файловой системы.
Для этого добавьте дополнительные параметры в конфигурационный файл диска:

- noatime — отключает запись времени доступа к файлу.
- nodiratime — отключает обновление времени доступа для каталогов.

noatime — отключает запись времени доступа к файлу.

nodiratime — отключает обновление времени доступа для каталогов.

Настройки снижают нагрузку на оперативную память.
Чтобы их добавить:

1. Откройте файл с конфигурацией диска:
sudo nano /etc/fstab
2. В строке с диском, на котором установлена СУБД, добавьте параметры «noatime» и «nodiratime»:
...# <device> <dir> <type> <options> <dump> <fsck>UUID=0a3407de-014b-458b-b5c1-848e******** / ext4 defaults,noatime,nodiratime 0 1

Откройте файл с конфигурацией диска:

```bash
sudo
nano
/etc/fstab
```

В строке с диском, на котором установлена СУБД, добавьте параметры «noatime» и «nodiratime»:

```bash
..
.
# <device> <dir> <type> <options> <dump> <fsck>
UUID
=
0a3407de-014b-458b-b5c1-848e******** / ext4 defaults,noatime,nodiratime
0
1
```
