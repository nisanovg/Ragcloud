---
title: Развертывание WireGuard VPN сервера с помощью Terraform в Cloud.ru Evolution
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn
topic: compute
---
# Развертывание WireGuard VPN сервера с помощью Terraform в Cloud.ru Evolution

С помощью этого руководства вы научитесь автоматически развертывать защищенную VPN-инфраструктуру с использованием Terraform и [WireGuard](https://www.wireguard.com/)WireGuard в облачной платформе Cloud.ru Evolution.

Вы развернете WireGuard на виртуальной машине и настроите конфигурацию сервера с помощью Terraform, а также настроите WireGuard на клиентском устройстве и подключитесь к VPN-серверу.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Terraform](https://cloud.ru/docs/terraform-evolution/ug/index)Terraform — инструмент для управления инфраструктурой как кодом (Infrastructure as Code).
- [WireGuard](https://www.wireguard.com/)WireGuard — современный VPN-протокол.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Terraform](https://cloud.ru/docs/terraform-evolution/ug/index)Terraform — инструмент для управления инфраструктурой как кодом (Infrastructure as Code).

[WireGuard](https://www.wireguard.com/)WireGuard — современный VPN-протокол.

Шаги:

1. [Установите и настройте Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Установите и настройте Terraform.
2. [Подготовьте файлы конфигурации](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Подготовьте файлы конфигурации.
3. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Разверните инфраструктуру.
4. [Установите WireGuard на клиенте](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Установите WireGuard на клиенте.
5. [Настройте сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Настройте сервер.
6. [Настройте клиент](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Настройте клиент.
7. [Проверьте соединение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Проверьте соединение.

[Установите и настройте Terraform](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Установите и настройте Terraform.

[Подготовьте файлы конфигурации](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Подготовьте файлы конфигурации.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Разверните инфраструктуру.

[Установите WireGuard на клиенте](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Установите WireGuard на клиенте.

[Настройте сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Настройте сервер.

[Настройте клиент](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Настройте клиент.

[Проверьте соединение](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__wireguard-vpn)Проверьте соединение.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт для управления облачными ресурсами.
3. [Создайте ключ доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Создайте ключ доступа для аутентификации сервисного аккаунта в API Cloud.ru.
Сохраните Key ID (логин) и Key Secret (пароль).
4. [Скопируйте идентификатор проекта](https://cloud.ru/docs/administration/ug/topics/guides__projects)Скопируйте идентификатор проекта, в котором будете разворачивать ресурсы.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте сервисный аккаунт](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт для управления облачными ресурсами.

[Создайте ключ доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Создайте ключ доступа для аутентификации сервисного аккаунта в API Cloud.ru.
Сохраните Key ID (логин) и Key Secret (пароль).

[Скопируйте идентификатор проекта](https://cloud.ru/docs/administration/ug/topics/guides__projects)Скопируйте идентификатор проекта, в котором будете разворачивать ресурсы.

## 1. Установите и настройте Terraform

1. [Установите Terraform](https://developer.hashicorp.com/terraform/install)Установите Terraform.
Если не удается скачать Terraform с сайта Hashicorp, скачайте дистрибутив Terraform из [зеркала Cloud.ru](https://cloud.ru/docs/terraform/ug/topics/overview__terraform-download)зеркала Cloud.ru.
2. Если вы загрузили дистрибутив Terraform из зеркала, добавьте в переменную PATH путь к папке с исполняемым файлом:
export PATH=$PATH:<path>

Где <path> — путь к исполняемому файлу Terraform.
3. [Установите Terraform-провайдер](https://cloud.ru/docs/terraform-evolution/ug/topics/quickstart)Установите Terraform-провайдер.

[Установите Terraform](https://developer.hashicorp.com/terraform/install)Установите Terraform.

Если не удается скачать Terraform с сайта Hashicorp, скачайте дистрибутив Terraform из [зеркала Cloud.ru](https://cloud.ru/docs/terraform/ug/topics/overview__terraform-download)зеркала Cloud.ru.

Если вы загрузили дистрибутив Terraform из зеркала, добавьте в переменную PATH путь к папке с исполняемым файлом:

```bash
export
PATH
=
$PATH
:
<
path
>
```

Где <path> — путь к исполняемому файлу Terraform.

[Установите Terraform-провайдер](https://cloud.ru/docs/terraform-evolution/ug/topics/quickstart)Установите Terraform-провайдер.

## 2. Подготовьте файлы конфигурации

В конфигурационных файлах опишите облачные ресурсы, которые создает Terraform.

1. Создайте директорию для конфигурационных файлов и перейдите в нее:
mkdir wireguard-vpn-lab && cd wireguard-vpn-lab
2. Сгенерируйте ключевую пару для подключения к серверу по SSH:
ssh-keygen -t ed25519 -f id_ed25519 -N ""
3. Выведите на экран и скопируйте публичный ключ id_ed25519.pub:
cat id_ed25519.pub
4. Создайте файл main.tf, содержащий определение всех создаваемых ресурсов и их конфигурацию.
Вместо значений <project_id> и <ssh_public_key> укажите идентификатор проекта и содержимое публичного ключа id_ed25519.pub соответственно.
 
 main.tf 
 
С помощью этой конфигурации вы создадите [новые ресурсы](https://github.com/cloud-ru/evo-terraform/tree/main/examples/compute)новые ресурсы:

виртуальную машину vpn-server с публичным IP-адресом vpn-fip;
группу безопасности vpn-security-group;
подсеть vpn-subnet.
5. Создайте файл variables.tf, содержащий все настраиваемые параметры инфраструктуры для удобства управления и повторного использования.
Вместо значений <access_key> и <secret_key> укажите логин и пароль ключа доступа, который вы создали перед началом работы.
 
 variables.tf
6. Создайте файл data.tf для получения информации о существующих ресурсах в облаке и динамической конфигурации.
 
 data.tf
7. Создайте файл wg0.conf, содержащий конфигурацию сервера.
В процессе развертывания инфраструктуры он будет автоматически скопирован на виртуальную машину vpn-server.
 
 wg0.conf

Создайте директорию для конфигурационных файлов и перейдите в нее:

```bash
mkdir
wireguard-vpn-lab
&&
cd
wireguard-vpn-lab
```

Сгенерируйте ключевую пару для подключения к серверу по SSH:

```bash
ssh-keygen
-t
ed25519
-f
id_ed25519
-N
""
```

Выведите на экран и скопируйте публичный ключ id_ed25519.pub:

```bash
cat
id_ed25519.pub
```

Создайте файл main.tf, содержащий определение всех создаваемых ресурсов и их конфигурацию.
Вместо значений <project_id> и <ssh_public_key> укажите идентификатор проекта и содержимое публичного ключа id_ed25519.pub соответственно.

С помощью этой конфигурации вы создадите [новые ресурсы](https://github.com/cloud-ru/evo-terraform/tree/main/examples/compute)новые ресурсы:

- виртуальную машину vpn-server с публичным IP-адресом vpn-fip;
- группу безопасности vpn-security-group;
- подсеть vpn-subnet.

виртуальную машину vpn-server с публичным IP-адресом vpn-fip;

группу безопасности vpn-security-group;

подсеть vpn-subnet.

Создайте файл variables.tf, содержащий все настраиваемые параметры инфраструктуры для удобства управления и повторного использования.
Вместо значений <access_key> и <secret_key> укажите логин и пароль ключа доступа, который вы создали перед началом работы.

Создайте файл data.tf для получения информации о существующих ресурсах в облаке и динамической конфигурации.

Создайте файл wg0.conf, содержащий конфигурацию сервера.
В процессе развертывания инфраструктуры он будет автоматически скопирован на виртуальную машину vpn-server.

## 3. Разверните инфраструктуру

1. Инициализируйте конфигурацию Terraform:
terraform init

Если все прошло успешно, появится сообщение:
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to seeany changes that are required for your infrastructure. All Terraform commandsshould now work.
If you ever set or change modules or backend configuration for Terraform,rerun this command to reinitialize your working directory. If you forget, othercommands will detect it and remind you to do so if necessary.
2. Проверьте корректность конфигурационных файлов с помощью команды:
terraform validate

Если файлы корректные, появится сообщение:
Success! The configuration is valid.
3. Для предварительного просмотра изменений инфраструктуры выполните команду:
terraform plan

В терминале появится список ресурсов с параметрами.
На этом этапе изменения не будут внесены.
4. Примените изменения инфраструктуры, описанные в конфигурации Terraform:
terraform apply
5. Подтвердите изменения: введите yes и нажмите Enter.
После создания всех ресурсов появится сообщение:
Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
6. Проверьте создание ресурсов:

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности vpn-security-group со статусом «Создана».
Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина vpn-server со статусом «Запущена».
Скопируйте и сохраните публичный IP-адрес виртуальной машины, он понадобится для настройки клиента.
Убедитесь, что в личном кабинете на странице Сети → Подсети отображается подсеть vpn-subnet со статусом «Создана».

Инициализируйте конфигурацию Terraform:

```bash
terraform init
```

Если все прошло успешно, появится сообщение:

```bash
Terraform has been successfully initialized
!
You may now begin working with Terraform. Try running
"terraform plan"
to see
any changes that are required
for
your infrastructure. All Terraform commands
should now work.
If you ever
set
or change modules or backend configuration
for
Terraform,
rerun this
command
to reinitialize your working directory. If you forget, other
commands will detect it and remind you to
do
so
if
necessary.
```

Проверьте корректность конфигурационных файлов с помощью команды:

```bash
terraform validate
```

Если файлы корректные, появится сообщение:

```bash
Success
!
The configuration is valid.
```

Для предварительного просмотра изменений инфраструктуры выполните команду:

```bash
terraform plan
```

В терминале появится список ресурсов с параметрами.
На этом этапе изменения не будут внесены.

Примените изменения инфраструктуры, описанные в конфигурации Terraform:

```bash
terraform apply
```

Подтвердите изменения: введите yes и нажмите Enter.

После создания всех ресурсов появится сообщение:

```bash
Apply complete
!
Resources:
4
added,
0
changed,
0
destroyed.
```

Проверьте создание ресурсов:

1. Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности vpn-security-group со статусом «Создана».
2. Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина vpn-server со статусом «Запущена».
3. Скопируйте и сохраните публичный IP-адрес виртуальной машины, он понадобится для настройки клиента.
4. Убедитесь, что в личном кабинете на странице Сети → Подсети отображается подсеть vpn-subnet со статусом «Создана».

Убедитесь, что в личном кабинете на странице Сети → Группы безопасности отображается группа безопасности vpn-security-group со статусом «Создана».

Убедитесь, что в личном кабинете на странице Инфраструктура → Виртуальные машины отображается виртуальная машина vpn-server со статусом «Запущена».

Скопируйте и сохраните публичный IP-адрес виртуальной машины, он понадобится для настройки клиента.

Убедитесь, что в личном кабинете на странице Сети → Подсети отображается подсеть vpn-subnet со статусом «Создана».

## 4. Установите WireGuard на клиенте

Для подключения к серверу установите WireGuard на своем устройстве.
В руководстве в качестве клиента используется устройство с ОС Ubuntu 22.04.

1. На клиенте в терминале выполните команду:
sudo apt install wireguard
2. Сгенерируйте ключи доступа для клиента:
wg genkey | tee client_privatekey | wg pubkey > client_publickey
3. Выведите на экран и скопируйте публичный ключ клиента:

cat client_publickey

На клиенте в терминале выполните команду:

```bash
sudo
apt
install
wireguard
```

Сгенерируйте ключи доступа для клиента:

```bash
wg genkey
|
tee
client_privatekey
|
wg pubkey
>
client_publickey
```

Выведите на экран и скопируйте публичный ключ клиента:

```bash
cat
client_publickey
```

Подробнее об установке WireGuard на других платформах читайте [на официальном сайте](https://www.wireguard.com/install)на официальном сайте.

## 5. Настройте сервер

В конфигурации сервера укажите данные для подключения клиента.

1. Подключитесь к ВМ vpn-server [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.
2. Откройте файл конфигурации сервера:
sudo nano /etc/wireguard/wg0.conf
3. Добавьте в конец файла настройки клиента:

[Peer]PublicKey = <client_public_key>AllowedIPs = 10.0.0.2/32

Где <client_public_key> — публичный ключ клиента.
4. Перезапустите WireGuard:
sudo systemctl restart wg-quick@wg0

Результат:
interface: wg0 public key: cQxq+75SZhnTetq/sXKTrPOHBGCZaArot8T0******** private key: (hidden) listening port: 51820
peer: J0SrgdesqESNTmbd858pT/x+cEKsBfOgcVO/******** allowed ips: 10.0.0.2/32
5. Скопируйте значение public key в выводе.
Оно потребуется на следующем этапе для настройки клиента.

Подключитесь к ВМ vpn-server [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.

Откройте файл конфигурации сервера:

```bash
sudo
nano
/etc/wireguard/wg0.conf
```

Добавьте в конец файла настройки клиента:

```bash
[
Peer
]
PublicKey
=
<
client_public_key
>
AllowedIPs
=
10.0
.0.2/32
```

Где <client_public_key> — публичный ключ клиента.

Перезапустите WireGuard:

```bash
sudo
systemctl restart wg-quick@wg0
```

Результат:

```bash
interface: wg0
public key: cQxq+75SZhnTetq/sXKTrPOHBGCZaArot8T0********
private key:
(
hidden
)
listening port:
51820
peer: J0SrgdesqESNTmbd858pT/x+cEKsBfOgcVO/********
allowed ips:
10.0
.0.2/32
```

Скопируйте значение public key в выводе.

Оно потребуется на следующем этапе для настройки клиента.

## 6. Настройте клиент

На клиентском устройстве создайте конфигурационный файл с настройками для подключения к серверу.

1. Выведите на экран и скопируйте приватный ключ клиента:

cat client_privatekey
2. Создайте файл конфигурации клиента:
sudo nano /etc/wireguard/wg0.conf
3. Вставьте конфигурацию для клиента:
[Interface]Address = 10.0.0.2/32PrivateKey = <client_private_key>DNS = 8.8.8.8
[Peer]PublicKey = <server_public_key>Endpoint = <server_public_ip>:51820AllowedIPs = 0.0.0.0/0PersistentKeepalive = 25

Где:

<client_private_key> — приватный ключ клиента.
<server_public_key> — публичный ключ сервера.
<server_public_ip> — публичный IP-адрес виртуальной машины vpn-server.
4. Запустите WireGuard:
sudo systemctl start wg-quick@wg0

Соединение с сервером будет установлено.

Выведите на экран и скопируйте приватный ключ клиента:

```bash
cat
client_privatekey
```

Создайте файл конфигурации клиента:

```bash
sudo
nano
/etc/wireguard/wg0.conf
```

Вставьте конфигурацию для клиента:

```bash
[
Interface
]
Address
=
10.0
.0.2/32
PrivateKey
=
<
client_private_key
>
DNS
=
8.8
.8.8
[
Peer
]
PublicKey
=
<
server_public_key
>
Endpoint
=
<
server_public_ip
>
:51820
AllowedIPs
=
0.0
.0.0/0
PersistentKeepalive
=
25
```

Где:

- <client_private_key> — приватный ключ клиента.
- <server_public_key> — публичный ключ сервера.
- <server_public_ip> — публичный IP-адрес виртуальной машины vpn-server.

<client_private_key> — приватный ключ клиента.

<server_public_key> — публичный ключ сервера.

<server_public_ip> — публичный IP-адрес виртуальной машины vpn-server.

Запустите WireGuard:

```bash
sudo
systemctl start wg-quick@wg0
```

Соединение с сервером будет установлено.

## 7. Проверьте соединение

1. Проверьте статус туннеля.
На клиентском устройстве выполните команду:
wg show

Результат:
interface: wg0 public key: J0SrgdesqESNTmbd858pT/x+cEKsBfOgcVO/******** private key: (hidden) listening port: 37904 fwmark: 0xca6c
peer: cQxq+75SZhnTetq/sXKTrPOHBGCZaArot8T0******** endpoint: 176.123.***.***:51820 allowed ips: 0.0.0.0/0 latest handshake: 46 seconds ago transfer: 92 B received, 212 B sent persistent keepalive: every 25 seconds
2. Проверьте доступность сервера:
ping 10.0.0.1

Проверьте статус туннеля.
На клиентском устройстве выполните команду:

```bash
wg show
```

Результат:

```bash
interface: wg0
public key: J0SrgdesqESNTmbd858pT/x+cEKsBfOgcVO/********
private key:
(
hidden
)
listening port:
37904
fwmark: 0xca6c
peer: cQxq+75SZhnTetq/sXKTrPOHBGCZaArot8T0********
endpoint:
176.123
.***.***:51820
allowed ips:
0.0
.0.0/0
latest handshake:
46
seconds ago
transfer:
92
B received,
212
B sent
persistent keepalive: every
25
seconds
```

Проверьте доступность сервера:

```bash
ping
10.0
.0.1
```

## Результат

Вы научились использовать Terraform для создания облачной инфраструктуры, а также настраивать серверную и клиентскую часть для WireGuard VPN.
