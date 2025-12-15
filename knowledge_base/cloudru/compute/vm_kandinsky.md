---
title: Запуск Kandinsky 5.0 Video Lite на GPU NVIDIA A100
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky
topic: compute
---
# Запуск Kandinsky 5.0 Video Lite на GPU NVIDIA A100

С помощью этого руководства вы развернете ComfyUI с поддержкой модели Kandinsky 5.0 Video Lite на виртуальной машине с GPU NVIDIA A100 в облаке Cloud.ru Evolution.

Модель Kandinsky 5.0 Video Lite — это компактная, но мощная модель для генерации видео с открытым исходным кодом.
Она позволяет генерировать видео длиной до 10 секунд в разрешении 768×512.
Также у модели есть оптимизированные версии (distilled), позволяющие ускорить инференс в 6 раз.

Вы научитесь:

- развертывать виртуальную машину с графическим процессором NVIDIA A100;
- устанавливать CUDA, Docker и ComfyUI;
- загружать и настраивать Kandinsky 5.0 Video Lite в ComfyUI;
- генерировать видео с помощью визуального интерфейса;
- обеспечивать безопасный доступ к сервису через HTTPS.

развертывать виртуальную машину с графическим процессором NVIDIA A100;

устанавливать CUDA, Docker и ComfyUI;

загружать и настраивать Kandinsky 5.0 Video Lite в ComfyUI;

генерировать видео с помощью визуального интерфейса;

обеспечивать безопасный доступ к сервису через HTTPS.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина с GPU.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.
- [ComfyUI](https://docs.comfy.org/)ComfyUI — визуальный интерфейс с открытым исходным кодом для запуска и управления диффузионными моделями генерации изображений и видео.
Позволяет строить сложные рабочие процессы (workflows) в виде узлов и соединений, обеспечивая гибкость и контроль над генерацией.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина с GPU.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Docker Compose](https://docs.docker.com/compose)Docker Compose — инструмент для запуска и управления Docker-контейнерами.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[ComfyUI](https://docs.comfy.org/)ComfyUI — визуальный интерфейс с открытым исходным кодом для запуска и управления диффузионными моделями генерации изображений и видео.
Позволяет строить сложные рабочие процессы (workflows) в виде узлов и соединений, обеспечивая гибкость и контроль над генерацией.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Разверните ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Настройте окружение на виртуальной машине.
3. [Настройте Nginx и HTTPS для ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Настройте Nginx и HTTPS для ComfyUI.
4. [Разверните ComfyUI с моделью Kandinsky 5](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Разверните ComfyUI с моделью Kandinsky 5.
5. [Сгенерируйте видео в ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Сгенерируйте видео в ComfyUI.
6. [Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Отключите доступ по SSH для виртуальной машины.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Разверните ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Настройте окружение на виртуальной машине.

[Настройте Nginx и HTTPS для ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Настройте Nginx и HTTPS для ComfyUI.

[Разверните ComfyUI с моделью Kandinsky 5](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Разверните ComfyUI с моделью Kandinsky 5.

[Сгенерируйте видео в ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Сгенерируйте видео в ComfyUI.

[Отключите доступ по SSH для виртуальной машины](https://cloud.ru/docs/tutorials-evolution/list/topics/vm__kandinsky)Отключите доступ по SSH для виртуальной машины.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Сгенерируйте ключевую пару и загрузите публичный ключ](https://cloud.ru/docs/public-keys/ug/topics/quickstart)Сгенерируйте ключевую пару и загрузите публичный ключ в Cloud.ru Evolution.

## 1. Разверните ресурсы в облаке

На этом шаге вы создадите группу безопасности, подсеть и виртуальную машину.

1. [Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием vm-gpu-sg в зоне доступности ru.AZ-2 и добавьте в нее правила:
 ТрафикПротоколПортТип источника/адресатИсточник/АдресатВходящийTCP443IP-адрес0.0.0.0/0ВходящийTCP80IP-адрес0.0.0.0/0ИсходящийЛюбойОставьте пустымIP-адрес0.0.0.0/0
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

Название — vm-gpu-subnet.
VPC — Default.
Адрес — 10.10.1.0/24.
DNS-серверы — 8.8.8.8.
3. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название — vm-gpu.
Зона доступности — ru.AZ-2.
Графический процессор (GPU) — включите опцию.
Образ — публичный образ Ubuntu 22.04 with GPU.
Модель GPU — NVIDIA A100.
Загрузочный диск — укажите размер 350 ГБ.
Сетевой интерфейс — выберите тип Подсеть с публичным IP.
Подсеть — vm-gpu-subnet.
Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
Группы безопасности — добавьте vm-gpu-sg.
Метод аутентификации — Публичный ключ и Пароль.
Публичный ключ — укажите ключ, созданный ранее.
Пароль — задайте пароль пользователя.

[Создайте группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте группу безопасности с названием vm-gpu-sg в зоне доступности ru.AZ-2 и добавьте в нее правила:

Трафик

Протокол

Порт

Тип источника/адресат

Источник/Адресат

Входящий

TCP

443

IP-адрес

0.0.0.0/0

Входящий

TCP

80

IP-адрес

0.0.0.0/0

Исходящий

Любой

Оставьте пустым

IP-адрес

0.0.0.0/0

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть со следующими параметрами:

- Название — vm-gpu-subnet.
- VPC — Default.
- Адрес — 10.10.1.0/24.
- DNS-серверы — 8.8.8.8.

Название — vm-gpu-subnet.

VPC — Default.

Адрес — 10.10.1.0/24.

DNS-серверы — 8.8.8.8.

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название — vm-gpu.
- Зона доступности — ru.AZ-2.
- Графический процессор (GPU) — включите опцию.
- Образ — публичный образ Ubuntu 22.04 with GPU.
- Модель GPU — NVIDIA A100.
- Загрузочный диск — укажите размер 350 ГБ.
- Сетевой интерфейс — выберите тип Подсеть с публичным IP.
- Подсеть — vm-gpu-subnet.
- Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.
- Группы безопасности — добавьте vm-gpu-sg.
- Метод аутентификации — Публичный ключ и Пароль.
- Публичный ключ — укажите ключ, созданный ранее.
- Пароль — задайте пароль пользователя.

Название — vm-gpu.

Зона доступности — ru.AZ-2.

Графический процессор (GPU) — включите опцию.

Образ — публичный образ Ubuntu 22.04 with GPU.

Модель GPU — NVIDIA A100.

Загрузочный диск — укажите размер 350 ГБ.

Сетевой интерфейс — выберите тип Подсеть с публичным IP.

Подсеть — vm-gpu-subnet.

Публичный IP — оставьте Арендовать новый или выберите IP-адрес из списка арендованных.

Группы безопасности — добавьте vm-gpu-sg.

Метод аутентификации — Публичный ключ и Пароль.

Публичный ключ — укажите ключ, созданный ранее.

Пароль — задайте пароль пользователя.

Убедитесь, что ресурсы созданы и отображаются в личном кабинете:

1. На странице Инфраструктура → Виртуальные машины отображается виртуальная машина vm-gpu со статусом «Запущена».
2. На странице Сети → Группы безопасности отображается группа безопасности vm-gpu-sg со статусом «Создана».

На странице Инфраструктура → Виртуальные машины отображается виртуальная машина vm-gpu со статусом «Запущена».

На странице Сети → Группы безопасности отображается группа безопасности vm-gpu-sg со статусом «Создана».

## 2. Настройте окружение на виртуальной машине

На этом шаге вы установите необходимые пакеты и настроите систему на ВМ.

1. Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.
2. Обновите систему и установите необходимые зависимости:
sudo apt update && sudo apt upgrade -y &&\sudo apt install -y curl apt-transport-https\ ca-certificates\ software-properties-common\ gnupg2\ lsb-release
3. Перезагрузите ВМ:
sudo reboot
4. Установите Docker:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpgecho "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt updatesudo apt install docker-ce docker-ce-cli containerd.io -y
5. Дайте текущему пользователю права на запуск Docker:
sudo usermod -aG docker $USERnewgrp docker
6. Установите Docker Compose:
sudo apt-get install docker-compose -y
7. Проверьте, что Docker и Docker Compose установлены корректно:
docker --versiondocker-compose version
8. Установите и запустите Nginx:
sudo apt install nginx -ysudo systemctl enable nginxsudo systemctl start nginx
9. Установите Let’s Encrypt и плагин для Nginx:
sudo apt install certbot python3-certbot-nginx -y
10. Установите NVIDIA Container Toolkit:
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.listsudo apt-get updatesudo apt-get install -y nvidia-docker2sudo systemctl restart docker

Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.

Обновите систему и установите необходимые зависимости:

```bash
sudo
apt
update
&&
sudo
apt
upgrade
-y
&&
\
sudo
apt
install
-y
curl
apt-transport-https
\
ca-certificates
\
software-properties-common
\
gnupg2
\
lsb-release
```

Перезагрузите ВМ:

```bash
sudo
reboot
```

Установите Docker:

```bash
curl
-fsSL
https://download.docker.com/linux/ubuntu/gpg
|
sudo
gpg
--dearmor
-o
/usr/share/keyrings/docker-archive-keyring.gpg
echo
"deb [arch=
$(
dpkg --print-architecture
)
signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu
$(
lsb_release
-cs
)
stable"
|
sudo
tee
/etc/apt/sources.list.d/docker.list
>
/dev/null
sudo
apt
update
sudo
apt
install
docker-ce docker-ce-cli containerd.io
-y
```

Дайте текущему пользователю права на запуск Docker:

```bash
sudo
usermod
-aG
docker
$USER
newgrp
docker
```

Установите Docker Compose:

```bash
sudo
apt-get
install
docker-compose
-y
```

Проверьте, что Docker и Docker Compose установлены корректно:

```bash
docker
--version
docker-compose
version
```

Установите и запустите Nginx:

```bash
sudo
apt
install
nginx
-y
sudo
systemctl
enable
nginx
sudo
systemctl start nginx
```

Установите Let’s Encrypt и плагин для Nginx:

```bash
sudo
apt
install
certbot python3-certbot-nginx
-y
```

Установите NVIDIA Container Toolkit:

```bash
distribution
=
$(
.
/etc/os-release
;
echo
$ID$VERSION_ID
)
curl
-s
-L
https://nvidia.github.io/nvidia-docker/gpgkey
|
sudo
apt-key
add
-
curl
-s
-L
https://nvidia.github.io/nvidia-docker/
$distribution
/nvidia-docker.list
|
sudo
tee
/etc/apt/sources.list.d/nvidia-docker.list
sudo
apt-get
update
sudo
apt-get
install
-y
nvidia-docker2
sudo
systemctl restart
docker
```

## 3. Настройте Nginx и HTTPS для ComfyUI

На этом шаге вы настроите службу Nginx и обеспечите доступ по HTTPS.

1. Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.
2. Сконфигурируйте межсетевой экран:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
3. Создайте конфигурационный файл Nginx:
sudo nano /etc/nginx/sites-available/comfyui.conf
4. Вставьте конфигурацию, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:
server { listen 80; server_name comfyui.<ip_address>.nip.io www.comfyui.<ip_address>.nip.io;
 location / { proxy_pass http://localhost:8080; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_http_version 1.1;proxy_set_header Upgrade $http_upgrade;proxy_set_header Connection "upgrade";}}
5. Активируйте конфигурацию и перезапустите Nginx:
sudo ln -sf /etc/nginx/sites-available/comfyui.conf /etc/nginx/sites-enabled/comfyui.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
6. Проверьте, что Nginx работает:
sudo systemctl status nginx

Сервис Nginx должен быть в статусе «active (running)».
7. Перейдите по адресу http://comfyui.<ip_address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».
8. Выпустите SSL-сертификат:
sudo certbot --nginx -d comfyui.<ip_address>.nip.io --redirect --agree-tos -m <email>

Где:

<ip_address> — публичный IP-адрес виртуальной машины.
<email> — email для регистрации сертификата.
9. Перейдите по адресу https://comfyui.<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.

Сконфигурируйте межсетевой экран:

```bash
sudo
ufw allow OpenSSH
sudo
ufw allow
'Nginx Full'
sudo
ufw
enable
```

Создайте конфигурационный файл Nginx:

```bash
sudo
nano
/etc/nginx/sites-available/comfyui.conf
```

Вставьте конфигурацию, заменив <ip_address> на значение публичного IP-адреса виртуальной машины:

```bash
server
{
listen
80
;
server_name comfyui.
<
ip_address
>
.nip.io www.comfyui.
<
ip_address
>
.nip.io
;
location /
{
proxy_pass http://localhost:8080
;
proxy_set_header Host
$host
;
proxy_set_header X-Real-IP
$remote_addr
;
proxy_set_header X-Forwarded-For
$proxy_add_x_forwarded_for
;
proxy_http_version
1.1
;
proxy_set_header Upgrade
$http_upgrade
;
proxy_set_header Connection
"upgrade"
;
}
}
```

Активируйте конфигурацию и перезапустите Nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/comfyui.conf /etc/nginx/sites-enabled/comfyui.conf
sudo
rm
-f
/etc/nginx/sites-enabled/default
sudo
nginx
-t
sudo
systemctl reload nginx
```

Проверьте, что Nginx работает:

```bash
sudo
systemctl status nginx
```

Сервис Nginx должен быть в статусе «active (running)».

Перейдите по адресу http://comfyui.<ip_address>.nip.io.
Откроется страница с текстом «502 Bad Gateway».

Выпустите SSL-сертификат:

```bash
sudo
certbot
--nginx
-d
comfyui.
<
ip_address
>
.nip.io
--redirect
--agree-tos
-m
<
email
>
```

Где:

- <ip_address> — публичный IP-адрес виртуальной машины.
- <email> — email для регистрации сертификата.

<ip_address> — публичный IP-адрес виртуальной машины.

<email> — email для регистрации сертификата.

Перейдите по адресу https://comfyui.<ip_address>.nip.io и убедитесь, что браузер отмечает соединение как безопасное.

## 4. Разверните ComfyUI с моделью Kandinsky 5

На этом шаге вы развернете ComfyUI с помощью Docker Compose.

1. Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.
2. Создайте структуру проекта:
mkdir -p $HOME/comfyuicd $HOME/comfyui
3. Клонируйте репозиторий Kandinsky 5 и перейдите в него:
git clone https://github.com/ai-forever/Kandinsky-5.gitcd Kandinsky-5
4. Загрузите модели Kandinsky 5 с помощью скрипта download_models.py:
pip install huggingface_hubpython download_models.py

Чтобы не скачивать все модели, вы можете удалить ненужные внутри скрипта.
5. Перенесите скачанные модели в директорию comfyui/models:
mkdir -p ~/comfyui/models/diffusion_modelsmkdir -p ~/comfyui/models/vaemkdir -p ~/comfyui/models/text_encodersmv weights/model ~/comfyui/models/diffusion_models/mv weights/vae ~/comfyui/models/vae/mv weights/text_encoder ~/comfyui/models/text_encoders/mv weights/text_encoder2 ~/comfyui/models/text_encoders/
6. Вернитесь в директорию comfyui:
cd ~/comfyui
7. Создайте папку output, в которую будут сохраняться сгенерированные видео:
mkdir ~/comfyui/output
8. Создайте файл docker-compose.yml:
sudo nano docker-compose.yml
9. Вставьте в созданный файл описание контейнера:
version: '3.8'
services: comfyui: build: context: . dockerfile: Dockerfile ports: - "8080:8188" volumes: - ./models:/comfyui/models - ./output:/comfyui/output shm_size: '16gb' deploy: resources: reservations: devices: - driver: nvidia count: 1 capabilities: [gpu] restart: unless-stopped
10. Создайте Dockerfile:
sudo nano Dockerfile
11. Вставьте содержимое:
# Используем CUDA-образ для A100FROM nvidia/cuda:12.4.1-devel-ubuntu22.04
# Устанавливаем системные зависимостиRUN apt-get update && apt-get install -y \ python3.10 \ python3-pip \ git \ wget \ ffmpeg \ build-essential \ --no-install-recommends && \ rm -rf /var/lib/apt/lists/*
# Добавляем символическую ссылку python → python3.10RUN ln -s /usr/bin/python3.10 /usr/bin/python
# Устанавливаем pipRUN curl -sS https://bootstrap.pypa.io/get-pip.py | python
WORKDIR /comfyui
# =============== 1. Устанавливаем ComfyUI ===============RUN git clone https://github.com/comfyanonymous/ComfyUI.git .RUN pip install -r requirements.txt
# =============== 2. Устанавливаем PyTorch с CUDA ===============RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# =============== 3. Устанавливаем flash-attn ===============RUN pip install packaging && \ pip install "flash-attn>=2.0" --no-build-isolation --no-use-pep517 --no-cache-dir
# =============== 4. Клонируем kandinsky-5-inference в custom_nodes ===============RUN mkdir -p custom_nodesWORKDIR /comfyui/custom_nodes
RUN git clone https://github.com/gen-ai-team/kandinsky-5-inference.git kandinsky
# =============== 5. Устанавливаем зависимости плагина + omegaconf ===============WORKDIR /comfyui/custom_nodes/kandinskyRUN pip install -r requirements.txtRUN pip install omegaconf # Требуется для nodes_kandinsky.py
# =============== 6. Копируем workflow в ComfyUI ===============WORKDIR /comfyuiRUN mkdir -p workflowsRUN cp /comfyui/custom_nodes/kandinsky/comfyui/kandisnky5_lite_T2V.json workflows/kandisnky5_lite_T2V.json
# =============== 7. Запускаем ComfyUI ===============EXPOSE 8188
CMD ["python", "main.py", "--listen", "0.0.0.0", "--port", "8188", "--gpu-only", "--use-flash-attention"]
12. Создайте файл .dockerignore:
sudo nano .dockerignore
13. Вставьте содержимое:
models/output/.git__pycache__*.logtemp/logs/*.safetensors*.bin*.pt*.pth
14. Запустите сервис:
docker-compose up -d
15. Проверьте, что сервис запущен:
docker compose ps

Подключитесь к виртуальной машине vm-gpu [через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)через серийную консоль или [по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)по SSH.

Создайте структуру проекта:

```bash
mkdir
-p
$HOME
/comfyui
cd
$HOME
/comfyui
```

Клонируйте репозиторий Kandinsky 5 и перейдите в него:

```bash
git
clone https://github.com/ai-forever/Kandinsky-5.git
cd
Kandinsky-5
```

Загрузите модели Kandinsky 5 с помощью скрипта download_models.py:

```bash
pip
install
huggingface_hub
python download_models.py
```

Чтобы не скачивать все модели, вы можете удалить ненужные внутри скрипта.

Перенесите скачанные модели в директорию comfyui/models:

```bash
mkdir
-p
~/comfyui/models/diffusion_models
mkdir
-p
~/comfyui/models/vae
mkdir
-p
~/comfyui/models/text_encoders
mv
weights/model ~/comfyui/models/diffusion_models/
mv
weights/vae ~/comfyui/models/vae/
mv
weights/text_encoder ~/comfyui/models/text_encoders/
mv
weights/text_encoder2 ~/comfyui/models/text_encoders/
```

Вернитесь в директорию comfyui:

```bash
cd
~/comfyui
```

Создайте папку output, в которую будут сохраняться сгенерированные видео:

```bash
mkdir
~/comfyui/output
```

Создайте файл docker-compose.yml:

```bash
sudo
nano
docker-compose.yml
```

Вставьте в созданный файл описание контейнера:

```bash
version
:
'3.8'
services
:
comfyui
:
build
:
context
:
.
dockerfile
:
Dockerfile
ports
:
-
"8080:8188"
volumes
:
-
./models
:
/comfyui/models
-
./output
:
/comfyui/output
shm_size
:
'16gb'
deploy
:
resources
:
reservations
:
devices
:
-
driver
:
nvidia
count
:
1
capabilities
:
[
gpu
]
restart
:
unless
-
stopped
```

Создайте Dockerfile:

```bash
sudo
nano
Dockerfile
```

Вставьте содержимое:

```bash
# Используем CUDA-образ для A100
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04
# Устанавливаем системные зависимости
RUN
apt-get
update
&&
apt-get
install
-y
\
python3.10
\
python3-pip
\
git
\
wget
\
ffmpeg
\
build-essential
\
--no-install-recommends
&&
\
rm
-rf
/var/lib/apt/lists/*
# Добавляем символическую ссылку python → python3.10
RUN
ln
-s
/usr/bin/python3.10 /usr/bin/python
# Устанавливаем pip
RUN
curl
-sS
https://bootstrap.pypa.io/get-pip.py
|
python
WORKDIR /comfyui
# =============== 1. Устанавливаем ComfyUI ===============
RUN
git
clone https://github.com/comfyanonymous/ComfyUI.git
.
RUN pip
install
-r
requirements.txt
# =============== 2. Устанавливаем PyTorch с CUDA ===============
RUN pip
install
torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# =============== 3. Устанавливаем flash-attn ===============
RUN pip
install
packaging
&&
\
pip
install
"flash-attn>=2.0"
--no-build-isolation --no-use-pep517 --no-cache-dir
# =============== 4. Клонируем kandinsky-5-inference в custom_nodes ===============
RUN
mkdir
-p
custom_nodes
WORKDIR /comfyui/custom_nodes
RUN
git
clone https://github.com/gen-ai-team/kandinsky-5-inference.git kandinsky
# =============== 5. Устанавливаем зависимости плагина + omegaconf ===============
WORKDIR /comfyui/custom_nodes/kandinsky
RUN pip
install
-r
requirements.txt
RUN pip
install
omegaconf
# Требуется для nodes_kandinsky.py
# =============== 6. Копируем workflow в ComfyUI ===============
WORKDIR /comfyui
RUN
mkdir
-p
workflows
RUN
cp
/comfyui/custom_nodes/kandinsky/comfyui/kandisnky5_lite_T2V.json workflows/kandisnky5_lite_T2V.json
# =============== 7. Запускаем ComfyUI ===============
EXPOSE
8188
CMD
[
"python"
,
"main.py"
,
"--listen"
,
"0.0.0.0"
,
"--port"
,
"8188"
,
"--gpu-only"
,
"--use-flash-attention"
]
```

Создайте файл .dockerignore:

```bash
sudo
nano
.dockerignore
```

Вставьте содержимое:

```bash
models/
output/
.git
__pycache__
*.log
temp/
logs/
*.safetensors
*.bin
*.pt
*.pth
```

Запустите сервис:

```bash
docker-compose
up
-d
```

Проверьте, что сервис запущен:

```bash
docker
compose
ps
```

## 5. Сгенерируйте видео в ComfyUI

1. Перейдите по адресу https://comfyui.<ip_address>.nip.io.
Откроется интерфейс ComfyUI.
2. Скачайте [файл конфигурации для моделей Kandinsky 5](https://raw.githubusercontent.com/ai-forever/Kandinsky-5/refs/heads/main/comfyui/kandisnky5_lite_T2V.json)файл конфигурации для моделей Kandinsky 5.
3. Загрузите файл конфигурации: в меню ComfyUI нажмите File → Открыть.

После этого у вас появится рабочий процесс для модели Kandinsky 5.
4. Выберите необходимую модель для генерации из тех, что вы скачали ранее.
Например:

kandinsky5lite_t2v_sft_5s.safetensors — для лучшего качества.
kandinsky5lite_t2v_distilled16steps_5s.safetensors — в 6 раз быстрее, но без серьезной потери качества.

[Подробнее о моделях Kandinsky 5](https://github.com/ai-forever/Kandinsky-5)Подробнее о моделях Kandinsky 5.
5. Настройте ключевые параметры:

prompt — описание сцены, которую хотите увидеть.
Чем детальнее, тем лучше: указывайте объекты, движение, стиль, освещение.
Пример:
A cat running through a sunlit forest, cinematic, 4K

negative prompt — то, что нужно исключить: артефакты, деформации, нежелательные объекты.
Пример:
blurry, low quality, extra limbs, text

width × height × length — размер кадра и количество кадров.
Укажите:

Для 5-секундного видео: 768×512×121.
Для 10-секундного видео: 768×512×241.

ПримечаниеДля 10-секундного видео ширина и высота должны делиться на 128.

steps — число итераций генерации.
Укажите 50 для SFT и Pretrain моделей, 16 — для distilled-версий.

cfg — параметр определяет, насколько строго модель следует промпту.
Рекомендуемое значение — 5.0.
Более высокие значения могут снизить качество.

scheduler_scale — управляет шумом и динамикой.
Для 5-секундного видео укажите 5.0, для 10-секундного — 10.0.
6. После введения промпта и выбора параметров нажмите кнопку Запустить.

Когда генерация завершится, в ComfyUI отобразится превью, а оригинальное видео сохранится в директории /comfyui/output.

[Пример сгенерированного видео](https://drive.google.com/file/d/15wTWujdwGVW7bWf03qPFgIpyRQfeHTXB/view)Пример сгенерированного видео.

Перейдите по адресу https://comfyui.<ip_address>.nip.io.

Откроется интерфейс ComfyUI.

Скачайте [файл конфигурации для моделей Kandinsky 5](https://raw.githubusercontent.com/ai-forever/Kandinsky-5/refs/heads/main/comfyui/kandisnky5_lite_T2V.json)файл конфигурации для моделей Kandinsky 5.

Загрузите файл конфигурации: в меню ComfyUI нажмите File → Открыть.

![../_images/s__kandinsky-open-conf.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__kandinsky-open-conf.png)

После этого у вас появится рабочий процесс для модели Kandinsky 5.

![../_images/s__kandinsky-workflow.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__kandinsky-workflow.png)

Выберите необходимую модель для генерации из тех, что вы скачали ранее.

Например:

- kandinsky5lite_t2v_sft_5s.safetensors — для лучшего качества.
- kandinsky5lite_t2v_distilled16steps_5s.safetensors — в 6 раз быстрее, но без серьезной потери качества.

kandinsky5lite_t2v_sft_5s.safetensors — для лучшего качества.

kandinsky5lite_t2v_distilled16steps_5s.safetensors — в 6 раз быстрее, но без серьезной потери качества.

![../_images/s__kandinsky-select-model.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__kandinsky-select-model.png)

[Подробнее о моделях Kandinsky 5](https://github.com/ai-forever/Kandinsky-5)Подробнее о моделях Kandinsky 5.

Настройте ключевые параметры:

- prompt — описание сцены, которую хотите увидеть.
Чем детальнее, тем лучше: указывайте объекты, движение, стиль, освещение.
Пример:
A cat running through a sunlit forest, cinematic, 4K
- negative prompt — то, что нужно исключить: артефакты, деформации, нежелательные объекты.
Пример:
blurry, low quality, extra limbs, text
- width × height × length — размер кадра и количество кадров.
Укажите:

Для 5-секундного видео: 768×512×121.
Для 10-секундного видео: 768×512×241.

ПримечаниеДля 10-секундного видео ширина и высота должны делиться на 128.
- steps — число итераций генерации.
Укажите 50 для SFT и Pretrain моделей, 16 — для distilled-версий.
- cfg — параметр определяет, насколько строго модель следует промпту.
Рекомендуемое значение — 5.0.
Более высокие значения могут снизить качество.
- scheduler_scale — управляет шумом и динамикой.
Для 5-секундного видео укажите 5.0, для 10-секундного — 10.0.

prompt — описание сцены, которую хотите увидеть.

Чем детальнее, тем лучше: указывайте объекты, движение, стиль, освещение.

Пример:

```bash
A
cat
running through a sunlit forest, cinematic, 4K
```

negative prompt — то, что нужно исключить: артефакты, деформации, нежелательные объекты.

Пример:

```bash
blurry, low quality, extra limbs, text
```

width × height × length — размер кадра и количество кадров.

Укажите:

- Для 5-секундного видео: 768×512×121.
- Для 10-секундного видео: 768×512×241.

Для 5-секундного видео: 768×512×121.

Для 10-секундного видео: 768×512×241.

Для 10-секундного видео ширина и высота должны делиться на 128.

steps — число итераций генерации.

Укажите 50 для SFT и Pretrain моделей, 16 — для distilled-версий.

cfg — параметр определяет, насколько строго модель следует промпту.

Рекомендуемое значение — 5.0.
Более высокие значения могут снизить качество.

scheduler_scale — управляет шумом и динамикой.

Для 5-секундного видео укажите 5.0, для 10-секундного — 10.0.

После введения промпта и выбора параметров нажмите кнопку Запустить.

![../_images/s__kandinsky-gen-start.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__kandinsky-gen-start.png)

Когда генерация завершится, в ComfyUI отобразится превью, а оригинальное видео сохранится в директории /comfyui/output.

![../_images/s__kandinsky-result-video.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__kandinsky-result-video.png)

[Пример сгенерированного видео](https://drive.google.com/file/d/15wTWujdwGVW7bWf03qPFgIpyRQfeHTXB/view)Пример сгенерированного видео.

## 6. Отключите доступ по SSH для виртуальной машины

Когда вы развернули и настроили сервис, закройте доступ по SSH для повышения безопасности.

1. В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.
2. В списке виртуальных машин выберите vm-gpu.
3. Перейдите на вкладку Сетевые параметры.
4. В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.
5. Удалите группу SSH-access_ru и сохраните изменения.
6. Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

В личном кабинете на верхней панели слева нажмите и выберите Инфраструктура → Виртуальные машины.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

В списке виртуальных машин выберите vm-gpu.

Перейдите на вкладку Сетевые параметры.

В блоке сетевого интерфейса нажмите и выберите Изменить группы безопасности.

![Горизонтальное меню](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__more.svg)

Удалите группу SSH-access_ru и сохраните изменения.

Убедитесь, что доступа нет — попробуйте [подключиться к виртуальной машине по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)подключиться к виртуальной машине по SSH.
После отключения доступа по SSH, администрирование сервиса будет доступно через [серийную консоль виртуальной машины](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)серийную консоль виртуальной машины.

## Результат

Вы развернули ComfyUI с поддержкой Kandinsky 5.0 Video Lite на GPU NVIDIA A100 с доступом через HTTPS.

В нем вы можете:

- Загружать workflow одним кликом.
- Генерировать видео до 10 секунд по текстовому промпту.
- Настраивать параметры: длину, шаги, CFG, разрешение.
- Сохранять результаты в папку output на хосте.

Загружать workflow одним кликом.

Генерировать видео до 10 секунд по текстовому промпту.

Настраивать параметры: длину, шаги, CFG, разрешение.

Сохранять результаты в папку output на хосте.

Теперь вы можете генерировать качественные короткие видео с помощью одной из самых передовых открытых видеомоделей в удобном интерфейсе ComfyUI.
