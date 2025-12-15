---
title: Разработка высоконагруженного приложения на сервере Bare Metal
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app
topic: compute
---
# Разработка высоконагруженного приложения на сервере Bare Metal

С помощью этого руководства вы развернете среду для разработки высоконагруженных приложений.
В отличие от виртуальных сред или локальных машин, Bare Metal обеспечивает:

- Предельную производительность — прямой доступ к CPU, RAM, дискам сервера без расходов на гипервизор, что критично для задач с интенсивными вычислениями, например при обработке 100 000+ RPS.
- Детерминированное поведение — идентичность версий приложения для разработки, тестирования и реализации.
Это исключает «эффект соседа» в облачной среде и гарантирует воспроизводимость результатов.
- Экономическую эффективность — централизация ресурсов сервера позволяет заменить все локальные машины разработчиков одним мощным сервером.
- Ускорение CI/CD — сборки и тесты выполняются быстрее благодаря отсутствию ограничений виртуализации.
Актуально для компиляции приложений на C++ или запуска ML-моделей.

Предельную производительность — прямой доступ к CPU, RAM, дискам сервера без расходов на гипервизор, что критично для задач с интенсивными вычислениями, например при обработке 100 000+ RPS.

Детерминированное поведение — идентичность версий приложения для разработки, тестирования и реализации.
Это исключает «эффект соседа» в облачной среде и гарантирует воспроизводимость результатов.

Экономическую эффективность — централизация ресурсов сервера позволяет заменить все локальные машины разработчиков одним мощным сервером.

Ускорение CI/CD — сборки и тесты выполняются быстрее благодаря отсутствию ограничений виртуализации.
Актуально для компиляции приложений на C++ или запуска ML-моделей.

В сценарии разберем разработку приложения командой из 10 разработчиков на сервере, у которого:

- настроена среда разработки VSCode Server;
- установлены программы для проектирования инженерных систем Ansys и HFSS;
- установлена утилита X2Go для запуска Ansys и HFSS;
- в качестве графической среды используется XFCE.

настроена среда разработки VSCode Server;

установлены программы для проектирования инженерных систем Ansys и HFSS;

установлена утилита X2Go для запуска Ansys и HFSS;

в качестве графической среды используется XFCE.

Все действия в сценарии выполняются для создания пользователя dev1.
Чтобы добавить пользователей для остальных разработчиков, повторите действия.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Разверните инфраструктуру.
2. [Настройте VSCode Server и системные лимиты](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте VSCode Server и системные лимиты.
3. [Подключите локальный VSCode к VSCode Server](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Подключите локальный VSCode к VSCode Server.
4. [Настройте UFW для доступа к сервисам только по SSH](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте UFW для доступа к сервисам только по SSH.
5. [Настройте X2Go Server для удаленного рабочего стола на Linux](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте X2Go Server для удаленного рабочего стола на Linux.
6. [Настройте X2Go на устройстве разработчика](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте X2Go на устройстве разработчика.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Разверните инфраструктуру.

[Настройте VSCode Server и системные лимиты](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте VSCode Server и системные лимиты.

[Подключите локальный VSCode к VSCode Server](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Подключите локальный VSCode к VSCode Server.

[Настройте UFW для доступа к сервисам только по SSH](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте UFW для доступа к сервисам только по SSH.

[Настройте X2Go Server для удаленного рабочего стола на Linux](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте X2Go Server для удаленного рабочего стола на Linux.

[Настройте X2Go на устройстве разработчика](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__highload_app)Настройте X2Go на устройстве разработчика.

## 1. Разверните инфраструктуру

1. [Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
2. [Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.
3. [Установите Docker](https://docs.docker.com/engine/install)Установите Docker.

[Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.

[Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

[Установите Docker](https://docs.docker.com/engine/install)Установите Docker.

## 2. Настройте VSCode Server и системные лимиты

1. Создайте изолированное окружение для каждого разработчика:
sudo useradd -m -s /bin/bash dev1 # Создание пользователяsudo passwd dev1 # Установка пароляsudo usermod -aG docker dev1 # Добавление в группу docker
2. Настройте системные лимиты:

Откройте конфигурационный файл на запись:
sudo nano /etc/security/limits.conf

Добавьте в конец файла код:
dev1 soft nproc 50000dev1 hard nproc 100000dev1 soft nofile 50000dev1 hard nofile 100000
* soft core unlimited

 
 Дополнительная настройка для GUI-приложений 
 

Нажмите сочетание клавиш Ctrl + O.

Создайте изолированное окружение для каждого разработчика:

```bash
sudo
useradd
-m
-s
/bin/bash dev1
# Создание пользователя
sudo
passwd
dev1
# Установка пароля
sudo
usermod
-aG
docker
dev1
# Добавление в группу docker
```

Настройте системные лимиты:

1. Откройте конфигурационный файл на запись:
sudo nano /etc/security/limits.conf
2. Добавьте в конец файла код:
dev1 soft nproc 50000dev1 hard nproc 100000dev1 soft nofile 50000dev1 hard nofile 100000
* soft core unlimited

 
 Дополнительная настройка для GUI-приложений
3. Нажмите сочетание клавиш Ctrl + O.

Откройте конфигурационный файл на запись:

```bash
sudo
nano
/etc/security/limits.conf
```

Добавьте в конец файла код:

```bash
dev1 soft nproc
50000
dev1 hard nproc
100000
dev1 soft nofile
50000
dev1 hard nofile
100000
* soft core unlimited
```

Нажмите сочетание клавиш Ctrl + O.

## 3. Подключите локальный VSCode к VSCode Server

Чтобы обеспечить безопасность работы с приложением,

1. На устройстве разработчика создайте пару SSH-ключей:
ssh-keygen -t ed25519
2. Скопируйте публичный ключ на сервер:
ssh-copy-id dev1@<server_ip_address>
3. Установите расширение «Remote SSH» для VSCode.
4. Добавьте сервер в файл .ssh/config:
Host dev-server-dev1 HostName <server_ip_address> User dev1 IdentityFile ~/.ssh/id_ed25519
5. Подключитесь к серверу из VSCode:

Нажмите сочетание клавиш Ctrl + Shift + P.
В строке поиска введите Remote-SSH: Connect to Host.
В списке выберите dev-server-dev1.

На устройстве разработчика создайте пару SSH-ключей:

```bash
ssh-keygen
-t
ed25519
```

Скопируйте публичный ключ на сервер:

```bash
ssh-copy-id dev1@
<
server_ip_address
>
```

Установите расширение «Remote SSH» для VSCode.

Добавьте сервер в файл .ssh/config:

```bash
Host dev-server-dev1
HostName
<
server_ip_address
>
User dev1
IdentityFile ~/.ssh/id_ed25519
```

Подключитесь к серверу из VSCode:

1. Нажмите сочетание клавиш Ctrl + Shift + P.
2. В строке поиска введите Remote-SSH: Connect to Host.
3. В списке выберите dev-server-dev1.

Нажмите сочетание клавиш Ctrl + Shift + P.

В строке поиска введите Remote-SSH: Connect to Host.

В списке выберите dev-server-dev1.

## 4. Настройте UFW для доступа к сервисам только по SSH

При разработке сервисов важно обеспечить их недоступность извне.
Для этого необходимо закрыть все сервисные порты с помощью UFW.
В этом случае приложения будут доступны только по SSH.

1. Создайте новые правила UFW:
# Сброс всех правилsudo ufw --force reset# Запретить все входящие соединения по умолчаниюsudo ufw default deny incoming# Разрешить все исходящиеsudo ufw default allow outgoing# Разрешить SSH (порт 22)sudo ufw allow 22/tcp# Включить UFWsudo ufw enable
2. Проверьте статус UFW:
sudo ufw status verbose

Результат
Status: activeLogging: on (low)Default: deny (incoming), allow (outgoing), disabled (routed)New profiles: skipTo Action From-- ------ ----22/tcp ALLOW IN Anywhere

Создайте новые правила UFW:

```bash
# Сброс всех правил
sudo
ufw
--force
reset
# Запретить все входящие соединения по умолчанию
sudo
ufw default deny incoming
# Разрешить все исходящие
sudo
ufw default allow outgoing
# Разрешить SSH (порт 22)
sudo
ufw allow
22
/tcp
# Включить UFW
sudo
ufw
enable
```

Проверьте статус UFW:

```bash
sudo
ufw status verbose
```

Результат

```bash
Status: active
Logging: on
(
low
)
Default: deny
(
incoming
)
, allow
(
outgoing
)
, disabled
(
routed
)
New profiles: skip
To Action From
-- ------ ----
22
/tcp ALLOW IN Anywhere
```

## 5. Настройте X2Go Server для удаленного рабочего стола на Linux

Для работы с графическими приложениями (CAD/CAM/CAE) терминала недостаточно.
X2Go позволяет:

- запускать графические приложения через SSH;
- работать с 3D-рендерингом и тяжелыми GUI;
- использовать несколько параллельных сессий на одном сервере;
- экономить трафик.

запускать графические приложения через SSH;

работать с 3D-рендерингом и тяжелыми GUI;

использовать несколько параллельных сессий на одном сервере;

экономить трафик.

1. Установите X2Go Server и XFCE на сервер:
sudo apt updatesudo apt install -y x2goserver x2goserver-xsessionsudo apt install -y xfce4 xfce4-goodies
2. Настройте пользователей:
sudo useradd -m -s /bin/bash engineer1sudo passwd engineer1
3. Создайте конфигурационный файл x2goagent.options в каталоге /etc/x2go/ и добавьте в него код:
# Разрешить аппаратное ускорениеUSE_XVFB = noENABLE_3D = yes# Оптимизация для CAD-приложенийNX_COMPRESSION = 9NX_IMAGE_CACHE = 50NX_SHM_DISABLE = no
4. Настройте лимиты для ресурсоемких задач:

Откройте конфигурационный файл на запись:
sudo nano /etc/security/limits.conf

Добавьте в конец файла код:
engineer1 hard memlock unlimitedengineer1 soft memlock unlimitedengineer1 hard nofile 100000engineer1 soft nofile 50000engineer1 hard rtprio 99 # Для реального времени
5. Установите графические драйверы:
sudo apt install -y nvidia-driver-535-server nvidia-utils-535-server nvidia-fabricmanager-535sudo apt install linux-headers-5.15.0-94-genericsudo rebootsudo systemctl enable nvidia-fabricmanagersudo systemctl start nvidia-fabricmanagernvidia-sminvidia-smi nvlink -s

Установите X2Go Server и XFCE на сервер:

```bash
sudo
apt
update
sudo
apt
install
-y
x2goserver x2goserver-xsession
sudo
apt
install
-y
xfce4 xfce4-goodies
```

Настройте пользователей:

```bash
sudo
useradd
-m
-s
/bin/bash engineer1
sudo
passwd
engineer1
```

Создайте конфигурационный файл x2goagent.options в каталоге /etc/x2go/ и добавьте в него код:

```bash
# Разрешить аппаратное ускорение
USE_XVFB
=
no
ENABLE_3D
=
yes
# Оптимизация для CAD-приложений
NX_COMPRESSION
=
9
NX_IMAGE_CACHE
=
50
NX_SHM_DISABLE
=
no
```

Настройте лимиты для ресурсоемких задач:

1. Откройте конфигурационный файл на запись:
sudo nano /etc/security/limits.conf
2. Добавьте в конец файла код:
engineer1 hard memlock unlimitedengineer1 soft memlock unlimitedengineer1 hard nofile 100000engineer1 soft nofile 50000engineer1 hard rtprio 99 # Для реального времени

Откройте конфигурационный файл на запись:

```bash
sudo
nano
/etc/security/limits.conf
```

Добавьте в конец файла код:

```bash
engineer1 hard memlock unlimited
engineer1 soft memlock unlimited
engineer1 hard nofile
100000
engineer1 soft nofile
50000
engineer1 hard rtprio
99
# Для реального времени
```

Установите графические драйверы:

```bash
sudo
apt
install
-y
nvidia-driver-535-server nvidia-utils-535-server nvidia-fabricmanager-535
sudo
apt
install
linux-headers-5.15.0-94-generic
sudo
reboot
sudo
systemctl
enable
nvidia-fabricmanager
sudo
systemctl start nvidia-fabricmanager
nvidia-smi
nvidia-smi nvlink
-s
```

## 6. Настройте X2Go на устройстве разработчика

1. Установите клиент:
WindowsLinuxMacOS[Скачайте клиент с официального сайта](https://wiki.x2go.org/doku.php/download:start)Скачайте клиент с официального сайта.
2. Создайте подключение:

Host — публичный IP-адрес сервера.
Login — engineer1.
Session Type — XFCE.
Port — 22 (SSH).
3. Укажите дополнительные настройки:
[Connection]# Аппаратное ускорениеuse_gfx=yesglx_cooler=yes # Для OpenGL[Media]# Для 3D-приложенийsound=bothprinting=no

Установите клиент:

[Скачайте клиент с официального сайта](https://wiki.x2go.org/doku.php/download:start)Скачайте клиент с официального сайта.

Создайте подключение:

- Host — публичный IP-адрес сервера.
- Login — engineer1.
- Session Type — XFCE.
- Port — 22 (SSH).

Host — публичный IP-адрес сервера.

Login — engineer1.

Session Type — XFCE.

Port — 22 (SSH).

Укажите дополнительные настройки:

```bash
[
Connection
]
# Аппаратное ускорение
use_gfx
=
yes
glx_cooler
=
yes
# Для OpenGL
[
Media
]
# Для 3D-приложений
sound
=
both
printing
=
no
```

Сервер готов к работе над приложением.
