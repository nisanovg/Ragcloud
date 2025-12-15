---
title: Развертывание K3s на сервере Bare Metal
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s
topic: compute
---
# Развертывание K3s на сервере Bare Metal

С помощью этого руководства вы развернете сервер Bare Metal с K3s — упрощенной версией Kubernetes для сред с ограниченными ресурсами.
Решение сохраняет все возможности Kubernetes и подходит для тестирования и разработки небольших приложений.

Шаги:

1. [Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Разверните инфраструктуру.
2. [Установите K3s](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Установите K3s.
3. [Настройте удаленный доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Настройте удаленный доступ.
4. [Добавьте дополнительные узлы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Добавьте дополнительные узлы.

[Разверните инфраструктуру](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Разверните инфраструктуру.

[Установите K3s](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Установите K3s.

[Настройте удаленный доступ](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Настройте удаленный доступ.

[Добавьте дополнительные узлы](https://cloud.ru/docs/tutorials-evolution/list/topics/bare-metal__k3s)Добавьте дополнительные узлы.

## 1. Разверните инфраструктуру

1. [Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.
2. [Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.
3. Обновите систему и установите утилиту Curl:
sudo apt update && sudo apt upgrade -ysudo apt install -y curl
4. Откройте порт 6443:
sudo ufw allow 6443

[Арендуйте сервер](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__server-rent)Арендуйте сервер Bare Metal с публичным IP-адресом.

[Подключитесь к серверу по SSH](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__ssh-connection)Подключитесь к серверу по SSH или [через виртуальную консоль](https://cloud.ru/docs/bare-metal-evolution/ug/topics/guides__console)через виртуальную консоль.

Обновите систему и установите утилиту Curl:

```bash
sudo
apt
update
&&
sudo
apt
upgrade
-y
sudo
apt
install
-y
curl
```

Откройте порт 6443:

```bash
sudo
ufw allow
6443
```

## 2. Установите K3s

1. Выполните команду:
curl -sfL https://get.k3s.io | sh -
2. Проверьте установку:
systemctl status k3s

Результат:
● k3s.service - Lightweight Kubernetes Loaded: loaded (/etc/systemd/system/k3s.service; enabled; preset: enabled) Active: active (running) since Thu 2025-07-17 13:26:31 MSK; 1s ago ...

Выполните команду:

```bash
curl
-sfL
https://get.k3s.io
|
sh
-
```

Проверьте установку:

```bash
systemctl status k3s
```

Результат:

```bash
● k3s.service - Lightweight Kubernetes
Loaded: loaded
(
/etc/systemd/system/k3s.service
;
enabled
;
preset: enabled
)
Active: active
(
running
)
since Thu
2025
-07-17
13
:26:31 MSK
;
1s ago
..
.
```

## 3. Настройте удаленный доступ

1. Получите содержимое конфигурационного файла:
cat /etc/rancher/k3s/config.yaml

Скопируйте содержимое.
2. Вставьте содержимое в файл /.kube/config на вашем устройстве.
Замените IP-адрес 127.0.0.1 на IP-адрес сервера или DNS-имя вашего хоста.

Получите содержимое конфигурационного файла:

```bash
cat
/etc/rancher/k3s/config.yaml
```

Скопируйте содержимое.

Вставьте содержимое в файл /.kube/config на вашем устройстве.

Замените IP-адрес 127.0.0.1 на IP-адрес сервера или DNS-имя вашего хоста.

## 4. Добавьте дополнительные узлы

Дополнительным узлом может стать виртуальная машина, другой сервер или пользовательское устройство.

1. Сгенерируйте токен на сервере:
sudo k3s token create --ttl 1h
2. Установите K3s на новый узел:
curl -sfL https://get.k3s.io | K3S_URL=https://<server_ip>:6443 K3S_TOKEN=<token> sh -

Где:

<server_ip> — IP-адрес сервера.
<token> — токен, полученный на предыдущем шаге.
3. Проверьте подключение узла:
k3s kubectl get nodes

Результат:
k3s kubectl get nodesNAME STATUS ROLES AGE VERSIONserver.local Ready control-plane,master 3d v1.31.5+k3s1

Сгенерируйте токен на сервере:

```bash
sudo
k3s token create
--ttl
1h
```

Установите K3s на новый узел:

```bash
curl
-sfL
https://get.k3s.io
|
K3S_URL
=
https://
<
server_ip
>
:6443
K3S_TOKEN
=
<
token
>
sh
-
```

Где:

- <server_ip> — IP-адрес сервера.
- <token> — токен, полученный на предыдущем шаге.

<server_ip> — IP-адрес сервера.

<token> — токен, полученный на предыдущем шаге.

Проверьте подключение узла:

```bash
k3s kubectl get nodes
```

Результат:

```bash
k3s kubectl get nodes
NAME STATUS ROLES AGE VERSION
server.local Ready control-plane,master 3d v1.31.5+k3s1
```

Вы установили K3s, настроили к нему удаленный доступ и добавили дополнительные узлы для
расширения кластера.
Такую конфигурацию можно использовать как среду для небольших приложений.
