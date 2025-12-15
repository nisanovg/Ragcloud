---
title: Подготовка и создание пользовательского образа с ОС Windows
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image
topic: compute
---
# Подготовка и создание пользовательского образа с ОС Windows

С помощью этого руководства вы подготовите файл образа виртуальной машины с операционной системой Windows, создадите пользовательский образ из этого файла и развернете виртуальную машину.

Вы развернете и настроите виртуальную машину с ОС Windows на локальном компьютере, а затем импортируете ее загрузочный диск в сервис «Образы».
Для виртуализации на локальном компьютере с установленной ОС Ubuntu используется гипервизор KVM.

Вы будете использовать следующие сервисы:

- [Образы](https://cloud.ru/docs/images/ug/index)Образы — сервис для управления образами, из которых развертываются виртуальные машины.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, которая будет развернута из созданного образа.

[Образы](https://cloud.ru/docs/images/ug/index)Образы — сервис для управления образами, из которых развертываются виртуальные машины.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина, которая будет развернута из созданного образа.

Шаги:

1. [Разверните виртуальную машину на локальном компьютере](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Разверните виртуальную машину на локальном компьютере.
2. [Установите Windows](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Установите Windows.
3. [Загрузите образ в облако](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Загрузите образ в облако.
4. [Разверните в облаке ВМ из созданного образа](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Разверните в облаке ВМ из созданного образа.

[Разверните виртуальную машину на локальном компьютере](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Разверните виртуальную машину на локальном компьютере.

[Установите Windows](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Установите Windows.

[Загрузите образ в облако](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Загрузите образ в облако.

[Разверните в облаке ВМ из созданного образа](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__windows-custom-image)Разверните в облаке ВМ из созданного образа.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Скачайте ISO-образ с операционной системой Windows.
В руководстве используется ОС Windows Server 2019.
3. [Скачайте подписанный ISO-образ с драйверами VirtIO](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso)Скачайте подписанный ISO-образ с драйверами VirtIO.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Скачайте ISO-образ с операционной системой Windows.
В руководстве используется ОС Windows Server 2019.

[Скачайте подписанный ISO-образ с драйверами VirtIO](https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/stable-virtio/virtio-win.iso)Скачайте подписанный ISO-образ с драйверами VirtIO.

## 1. Разверните виртуальную машину на локальном компьютере

На этом шаге вы развернете ВМ, которая будет использоваться для установки и настройки Windows.
Виртуальная машина разворачивается на локальном компьютере с установленной ОС Ubuntu 22.04 и графическим интерфейсом.

1. Обновите пакеты.
В терминале выполните команду:
sudo apt update
2. Установите утилиты для виртуализации и использования графического интерфейса:
sudo apt install virtinst virt-manager virt-viewer qemu-system-x86 qemu-utils
3. Создайте загрузочный диск для виртуальной машины размером 25 ГБ:
qemu-img create -f raw windows-cloud.raw 25G
4. Назначьте системному пользователю libvirt-qemu права на каталог, в котором находится загрузочный диск и необходимые ISO-образы.
libvirt-qemu — это системный пользователь, от имени которого работают процессы виртуализации.
sudo setfacl -m u:libvirt-qemu:x <path_to_iso>

Где <path_to_iso> — каталог, в котором находится загрузочный диск и необходимые ISO-образы.
5. Создайте виртуальную машину с помощью команды:
virt-install \ --connect qemu:///system \ --name ws2019 \ --ram 2048 \ --vcpus 2 \ --network network=default,model=virtio \ --disk path=windows-cloud.raw,format=raw,device=disk,bus=virtio \ --cdrom <path_to_win_iso> \ --disk path=<path_to_virtio_iso>,device=cdrom \ --vnc \ --noautoconsole \ --noreboot

Где:

<path_to_win_iso> — путь к ISO-образу с операционной системой Windows.
<path_to_virtio_iso> — путь к ISO-образу с драйверами VirtIO.

Обновите пакеты.
В терминале выполните команду:

```bash
sudo
apt
update
```

Установите утилиты для виртуализации и использования графического интерфейса:

```bash
sudo
apt
install
virtinst virt-manager virt-viewer qemu-system-x86 qemu-utils
```

Создайте загрузочный диск для виртуальной машины размером 25 ГБ:

```bash
qemu-img create
-f
raw windows-cloud.raw 25G
```

Назначьте системному пользователю libvirt-qemu права на каталог, в котором находится загрузочный диск и необходимые ISO-образы.
libvirt-qemu — это системный пользователь, от имени которого работают процессы виртуализации.

```bash
sudo
setfacl
-m
u:libvirt-qemu:x
<
path_to_iso
>
```

Где <path_to_iso> — каталог, в котором находится загрузочный диск и необходимые ISO-образы.

Создайте виртуальную машину с помощью команды:

```bash
virt-install
\
--connect
qemu:///system
\
--name
ws2019
\
--ram
2048
\
--vcpus
2
\
--network
network
=
default,model
=
virtio
\
--disk
path
=
windows-cloud.raw,format
=
raw,device
=
disk,bus
=
virtio
\
--cdrom
<
path_to_win_iso
>
\
--disk
path
=
<
path_to_virtio_iso
>
,device
=
cdrom
\
--vnc
\
--noautoconsole
\
--noreboot
```

Где:

- <path_to_win_iso> — путь к ISO-образу с операционной системой Windows.
- <path_to_virtio_iso> — путь к ISO-образу с драйверами VirtIO.

<path_to_win_iso> — путь к ISO-образу с операционной системой Windows.

<path_to_virtio_iso> — путь к ISO-образу с драйверами VirtIO.

## 2. Установите Windows

На этом шаге вы установите и настроите ОС Windows на развернутой ранее виртуальной машине.
Далее образ загрузочного диска этой машины будет использоваться для развертывания виртуальных машин в облаке.

1. Подключитесь к созданной ВМ.
virt-viewer ws2019

Откроется программа установки Windows.
2. На стартовом экране в поле Time and currency format выберите Russian (Russia) и нажмите Next.
3. Нажмите Install Now.
4. Выберите тип инсталляции Custom.
5. По умолчанию программа установки не обнаружит локальные диски без загрузки драйверов.
Загрузите нужные драйверы вручную.

Нажмите Load driver и выберите драйверы VirtIO SCSI в директории E:\virtio-win-0.1.xxx\viostor\2k19\amd64.
После установки драйверов в списке появится загрузочный диск.
Нажмите Load driver и выберите сетевые драйверы в директории E:\virtio-win-0.1.xxx\NetKVM\2k19\amd64.
6. Выберите появившийся диск на 25 ГБ и нажмите Next.
Начнется процесс установки Windows, после завершения которого ВМ перезагрузится.
7. Запустите ВМ ws2019:
virsh start ws2019
8. Снова подключитесь к ВМ ws2019 через virt-viewer и установите пароль администратора.
9. Завершите установку драйверов:

Перейдите в каталог E:\virtio-win-0.1.xxx.
Запустите установочный файл virtio-win-gt-x64.msi и пройдите все шаги мастера установки.
Перейдите в каталог E:\virtio-win-0.1.xxx\viostor\2k19\amd64.
Нажмите на файл viostor.inf правой кнопкой мыши и выберите Install.
10. Настройте Cloudbase-Init.

Откройте PowerShell.
Разрешите Cloudbase-Init запускать скрипты во время загрузки ВМ.
Выполните команду:

Set-ExecutionPolicy Unrestricted

Загрузите Cloudbase-Init:
Invoke-WebRequest -UseBasicParsing https://cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi -OutFile cloudbaseinit.msi

Запустите установку Cloudbase-Init:
.\cloudbaseinit.msi

На шаге Configuration options:

Укажите параметры:

Username: Administrator.
Serial port for logging: COM1.

Включите опцию Run Cloudbase-Init service as LocalSystem.
Нажмите Finish.

Откройте файл C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf\cloudbase-init.conf.
Добавьте строки и сохраните файл:
metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService,cloudbaseinit.metadata.services.httpservice.HttpServiceplugins=cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.windows.createuser.CreateUserPlugin,cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin,cloudbaseinit.plugins.common.sshpublickeys.SetUserSSHPublicKeysPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin,cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPluginstop_service_on_exit=falsefirst_logon_behavior=no
11. Выполните генерализацию образа.
В Powershell введите команду:
C:\Windows\System32\Sysprep\sysprep.exe /oobe /generalize /shutdown

Подключитесь к созданной ВМ.

```bash
virt-viewer ws2019
```

Откроется программа установки Windows.

На стартовом экране в поле Time and currency format выберите Russian (Russia) и нажмите Next.

Нажмите Install Now.

Выберите тип инсталляции Custom.

По умолчанию программа установки не обнаружит локальные диски без загрузки драйверов.
Загрузите нужные драйверы вручную.

1. Нажмите Load driver и выберите драйверы VirtIO SCSI в директории E:\virtio-win-0.1.xxx\viostor\2k19\amd64.
После установки драйверов в списке появится загрузочный диск.
2. Нажмите Load driver и выберите сетевые драйверы в директории E:\virtio-win-0.1.xxx\NetKVM\2k19\amd64.

Нажмите Load driver и выберите драйверы VirtIO SCSI в директории E:\virtio-win-0.1.xxx\viostor\2k19\amd64.
После установки драйверов в списке появится загрузочный диск.

Нажмите Load driver и выберите сетевые драйверы в директории E:\virtio-win-0.1.xxx\NetKVM\2k19\amd64.

Выберите появившийся диск на 25 ГБ и нажмите Next.
Начнется процесс установки Windows, после завершения которого ВМ перезагрузится.

Запустите ВМ ws2019:

```bash
virsh
start ws2019
```

Снова подключитесь к ВМ ws2019 через virt-viewer и установите пароль администратора.

Завершите установку драйверов:

1. Перейдите в каталог E:\virtio-win-0.1.xxx.
2. Запустите установочный файл virtio-win-gt-x64.msi и пройдите все шаги мастера установки.
3. Перейдите в каталог E:\virtio-win-0.1.xxx\viostor\2k19\amd64.
4. Нажмите на файл viostor.inf правой кнопкой мыши и выберите Install.

Перейдите в каталог E:\virtio-win-0.1.xxx.

Запустите установочный файл virtio-win-gt-x64.msi и пройдите все шаги мастера установки.

Перейдите в каталог E:\virtio-win-0.1.xxx\viostor\2k19\amd64.

Нажмите на файл viostor.inf правой кнопкой мыши и выберите Install.

Настройте Cloudbase-Init.

1. Откройте PowerShell.
2. Разрешите Cloudbase-Init запускать скрипты во время загрузки ВМ.
Выполните команду:

Set-ExecutionPolicy Unrestricted
3. Загрузите Cloudbase-Init:
Invoke-WebRequest -UseBasicParsing https://cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi -OutFile cloudbaseinit.msi
4. Запустите установку Cloudbase-Init:
.\cloudbaseinit.msi
5. На шаге Configuration options:

Укажите параметры:

Username: Administrator.
Serial port for logging: COM1.

Включите опцию Run Cloudbase-Init service as LocalSystem.
Нажмите Finish.
6. Откройте файл C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf\cloudbase-init.conf.
7. Добавьте строки и сохраните файл:
metadata_services=cloudbaseinit.metadata.services.configdrive.ConfigDriveService,cloudbaseinit.metadata.services.httpservice.HttpServiceplugins=cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.windows.createuser.CreateUserPlugin,cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin,cloudbaseinit.plugins.common.sshpublickeys.SetUserSSHPublicKeysPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin,cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPluginstop_service_on_exit=falsefirst_logon_behavior=no

Откройте PowerShell.

Разрешите Cloudbase-Init запускать скрипты во время загрузки ВМ.
Выполните команду:

```bash
Set-ExecutionPolicy Unrestricted
```

Загрузите Cloudbase-Init:

```bash
Invoke-WebRequest
-UseBasicParsing
https://cloudbase.it/downloads/CloudbaseInitSetup_Stable_x64.msi
-OutFile
cloudbaseinit.msi
```

Запустите установку Cloudbase-Init:

```bash
.
\
cloudbaseinit.msi
```

На шаге Configuration options:

1. Укажите параметры:

Username: Administrator.
Serial port for logging: COM1.
2. Включите опцию Run Cloudbase-Init service as LocalSystem.
3. Нажмите Finish.

Укажите параметры:

- Username: Administrator.
- Serial port for logging: COM1.

Username: Administrator.

Serial port for logging: COM1.

Включите опцию Run Cloudbase-Init service as LocalSystem.

Нажмите Finish.

Откройте файл C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf\cloudbase-init.conf.

Добавьте строки и сохраните файл:

```bash
metadata_services
=
cloudbaseinit.metadata.services.configdrive.ConfigDriveService,cloudbaseinit.metadata.services.httpservice.HttpService
plugins
=
cloudbaseinit.plugins.common.sethostname.SetHostNamePlugin,cloudbaseinit.plugins.windows.createuser.CreateUserPlugin,cloudbaseinit.plugins.common.networkconfig.NetworkConfigPlugin,cloudbaseinit.plugins.common.sshpublickeys.SetUserSSHPublicKeysPlugin,cloudbaseinit.plugins.common.userdata.UserDataPlugin,cloudbaseinit.plugins.windows.extendvolumes.ExtendVolumesPlugin,cloudbaseinit.plugins.common.setuserpassword.SetUserPasswordPlugin
stop_service_on_exit
=
false
first_logon_behavior
=
no
```

Выполните генерализацию образа.
В Powershell введите команду:

```bash
C:
\
Windows
\
System32
\
Sysprep
\
sysprep.exe /oobe /generalize /shutdown
```

## 3. Загрузите образ в облако

[Создайте пользовательский образ в облаке Evolution](https://cloud.ru/docs/images/ug/topics/guides__create-image)Создайте пользовательский образ в облаке Evolution, используя образ загрузочного диска виртуальной машины с установленной ОС Windows:

- Зона доступности — ru.AZ-1.
- vCPU, шт — 2.
- RAM, ГБ — 2.
- Диск, ГБ — 30.
- Название — windows-server-2019.
- Источник — выберите файл образа windows-cloud.raw.

Зона доступности — ru.AZ-1.

vCPU, шт — 2.

RAM, ГБ — 2.

Диск, ГБ — 30.

Название — windows-server-2019.

Источник — выберите файл образа windows-cloud.raw.

## 4. Разверните в облаке ВМ из созданного образа

На этом шаге вы развернете в облаке Cloud.ru виртуальную машину с ОС Windows из пользовательского образа и подключитесь к ней.

1. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — win-server.
Зона доступности — ru.AZ-1.
Образ — на вкладке Пользовательские выберите образ windows-server-2019.
Гарантированная доля vCPU — 10%.
vCPU, шт — 2.
RAM, ГБ: — 4.
Загрузочный диск — укажите размер 30 ГБ.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
2. Подключитесь к созданной ВМ.

Выберите ВМ win-server в списке.
Перейдите на вкладку Виртуальная консоль.
Дождитесь загрузки системы.

Выполните первоначальную настройку системы: укажите настройки языка и примите лицензионное соглашение.
Установите пароль для пользователя Administrator и войдите в систему.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — win-server.
- Зона доступности — ru.AZ-1.
- Образ — на вкладке Пользовательские выберите образ windows-server-2019.
- Гарантированная доля vCPU — 10%.
- vCPU, шт — 2.
- RAM, ГБ: — 4.
- Загрузочный диск — укажите размер 30 ГБ.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.

Название — win-server.

Зона доступности — ru.AZ-1.

Образ — на вкладке Пользовательские выберите образ windows-server-2019.

Гарантированная доля vCPU — 10%.

vCPU, шт — 2.

RAM, ГБ: — 4.

Загрузочный диск — укажите размер 30 ГБ.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

Подключитесь к созданной ВМ.

1. Выберите ВМ win-server в списке.
2. Перейдите на вкладку Виртуальная консоль.
Дождитесь загрузки системы.
3. Выполните первоначальную настройку системы: укажите настройки языка и примите лицензионное соглашение.
4. Установите пароль для пользователя Administrator и войдите в систему.

Выберите ВМ win-server в списке.

Перейдите на вкладку Виртуальная консоль.

Дождитесь загрузки системы.

Выполните первоначальную настройку системы: укажите настройки языка и примите лицензионное соглашение.

Установите пароль для пользователя Administrator и войдите в систему.

## Результат

Вы научились подготавливать образы с ОС Windows, загружать их в облако Cloud.ru и разворачивать из них виртуальные машины.
