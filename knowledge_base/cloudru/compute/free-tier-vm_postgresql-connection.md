---
title: Настройка взаимодействия приложения на виртуальных машинах с сервисом Managed PostgreSQL®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection
topic: compute
---
# Настройка взаимодействия приложения на виртуальных машинах с сервисом Managed PostgreSQL®

С помощью этого руководства вы развернете сервис сокращенных ссылок и настроите защищенную схему взаимодействия FastAPI-приложения с сервисом Managed PostgreSQL.

Вы выполните развертывание виртуальной машины Ubuntu 22.04, настройку сетей и групп безопасности, создание кластера PostgreSQL, установку и конфигурирование приложения и публикацию API за nginx с поддержкой Let’s Encrypt.

В результате вы получите надежную архитектуру: база данных доступна только по закрытому адресу, а доступ к приложению осуществляется по HTTPS.

Вы будете использовать следующие сервисы:

- [Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.
- [Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.
- Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.
- Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

[Виртуальная машина free tier](https://cloud.ru/docs/virtual-machines/ug/topics/overview__free-tier)Виртуальная машина free tier — сервис, в рамках которого предоставляется бесплатная виртуальная машина с готовой конфигурацией.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес для доступа к сервису через интернет.

[Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/index)Managed PostgreSQL — управляемая база данных PostgreSQL.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

Бесплатный сервис [nip.io](https://nip.io/)nip.io для получения публичного доменного имени и сертификата.
Вы также можете использовать собственное зарегистрированное доменное имя и SSL-сертификат для организации доступа.

Nginx — веб-сервер для проксирования запросов и организации защищeнного HTTPS-доступа к приложению.

Let’s Encrypt — сервис для автоматического получения бесплатного SSL-сертификата.

Шаги:

1. [Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Настройте окружение на виртуальной машине.
3. [Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните приложение.
4. [Настройте сервис, nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Настройте сервис, nginx и HTTPS.

[Разверните ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Настройте окружение на виртуальной машине.

[Разверните приложение](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните приложение.

[Настройте сервис, nginx и HTTPS](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Настройте сервис, nginx и HTTPS.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Разверните ресурсы в облаке

[Создайте виртуальную сеть](https://cloud.ru/docs/evolution-vpc/ug/topics/quickstart)Создайте виртуальную сеть со следующими параметрами:

1. В поле Название укажите название сети, например short-links-service-VPC.
2. [Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

В поле Название укажите short-link-service-subnet.
В поле Адрес укажите 10.10.1.0/24.
В поле VPC выберите short-links-service-VPC.
В поле DNS-серверы укажите 8.8.8.8.

В поле Название укажите название сети, например short-links-service-VPC.

[Создайте подсеть](https://cloud.ru/docs/subnets/ug/topics/guides__create-subnet)Создайте подсеть:

1. В поле Название укажите short-link-service-subnet.
2. В поле Адрес укажите 10.10.1.0/24.
3. В поле VPC выберите short-links-service-VPC.
4. В поле DNS-серверы укажите 8.8.8.8.

В поле Название укажите short-link-service-subnet.

В поле Адрес укажите 10.10.1.0/24.

В поле VPC выберите short-links-service-VPC.

В поле DNS-серверы укажите 8.8.8.8.

[Создайте новую группу безопасности](https://cloud.ru/docs/security-groups/ug/topics/guides__create-sg)Создайте новую группу безопасности со следующими параметрами:

1. Выберите Зону доступности, в которой необходимо разместить группу безопасности.
Укажите ту же зону доступности, что выбрана для сети.
2. Укажите Название группы безопасности, например short-links-service.
3. Добавьте правила входящего и исходящего трафика.
Правила входящего трафика:

Протокол: TCP
Порт: 443
Тип источника: IP-адрес
Источник: 0.0.0.0/0
Протокол: TCP
Порт: 80
Тип источника: IP-адрес
Источник: 0.0.0.0/0

Правила исходящего трафика:

Протокол: Любой
Тип адресата: IP-адрес
Адресат: 0.0.0.0/0

Выберите Зону доступности, в которой необходимо разместить группу безопасности.
Укажите ту же зону доступности, что выбрана для сети.

Укажите Название группы безопасности, например short-links-service.

Добавьте правила входящего и исходящего трафика.

Правила входящего трафика:

1. Протокол: TCP
2. Порт: 443
3. Тип источника: IP-адрес
4. Источник: 0.0.0.0/0
5. Протокол: TCP
6. Порт: 80
7. Тип источника: IP-адрес
8. Источник: 0.0.0.0/0

Протокол: TCP

Порт: 443

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Протокол: TCP

Порт: 80

Тип источника: IP-адрес

Источник: 0.0.0.0/0

Правила исходящего трафика:

1. Протокол: Любой
2. Тип адресата: IP-адрес
3. Адресат: 0.0.0.0/0

Протокол: Любой

Тип адресата: IP-адрес

Адресат: 0.0.0.0/0

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

1. В поле Название укажите название виртуальной машины, например short-links-service.
2. На вкладке Публичные выберите образ Ubuntu 22.04.
3. Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.
4. В поле Группы безопасности выберите группу безопасности short-link-service.
5. В поле Логин укажите логин пользователя виртуальной машины, например user1.
6. Выберите метод аутентификации — пароль.
7. В поле Сетевые настройки выберите подсеть short-link-service-subnet.
8. В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например short-links-service.

В поле Название укажите название виртуальной машины, например short-links-service.

На вкладке Публичные выберите образ Ubuntu 22.04.

Назначьте публичный IP-адрес виртуальной машине — оставьте включенной опцию Подключить публичный IP. Для виртуальной машины будет арендован и назначен [прямой публичный IP](https://cloud.ru/docs/public-ip/ug/topics/concepts__ip-types)прямой публичный IP.

В поле Группы безопасности выберите группу безопасности short-link-service.

В поле Логин укажите логин пользователя виртуальной машины, например user1.

Выберите метод аутентификации — пароль.

В поле Сетевые настройки выберите подсеть short-link-service-subnet.

В поле Имя хоста укажите уникальное имя устройства, по которому можно идентифицировать виртуальную машину в сети, например short-links-service.

[Создайте кластер Managed PostgreSQL](https://cloud.ru/docs/paas-postgresql/ug/topics/quickstart)Создайте кластер Managed PostgreSQL со следующими параметрами:

1. В поле Имя кластера укажите short-links-service.
2. В поле Название базы данных укажите default.
3. В поле Версия PostgreSQL выберите 16.
4. В поле Режим выберите Стандарт.
5. В поле Тип выберите Single.
6. В поле Подсеть выберите short-link-service-subnet.
7. [Создайте пользователя](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__users__creating-user)Создайте пользователя:

В поле Имя пользователя укажите short_links.
Укажите пароль.
8. [Создайте базу данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте базу данных:

В поле Владелец выберите short_links.
Название базы данных: shortener_db.

В поле Имя кластера укажите short-links-service.

В поле Название базы данных укажите default.

В поле Версия PostgreSQL выберите 16.

В поле Режим выберите Стандарт.

В поле Тип выберите Single.

В поле Подсеть выберите short-link-service-subnet.

[Создайте пользователя](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__users__creating-user)Создайте пользователя:

1. В поле Имя пользователя укажите short_links.
2. Укажите пароль.

В поле Имя пользователя укажите short_links.

Укажите пароль.

[Создайте базу данных](https://cloud.ru/docs/paas-postgresql/ug/topics/guides__databases__creating-database)Создайте базу данных:

1. В поле Владелец выберите short_links.
2. Название базы данных: shortener_db.

В поле Владелец выберите short_links.

Название базы данных: shortener_db.

Убедитесь, что в личном кабинете:

1. На странице сервиса «VPC»:

отображается сеть short-links-service-VPC;
в списке подсетей отображается short-link-service-subnet.
2. На странице сервиса «Группы безопасности»:

отображается группа безопасности short-links-service;
статус группы безопасности — «Создана».
3. На странице сервиса «Виртуальные машины»:

отображается виртуальная машина short-links-service;
статус виртуальной машины — «Запущена».
4. На странице сервиса «Managed PostgreSQL»:

отображается кластер short-links-service;
статус кластера — «Доступен».

На странице сервиса «VPC»:

- отображается сеть short-links-service-VPC;
- в списке подсетей отображается short-link-service-subnet.

отображается сеть short-links-service-VPC;

в списке подсетей отображается short-link-service-subnet.

На странице сервиса «Группы безопасности»:

- отображается группа безопасности short-links-service;
- статус группы безопасности — «Создана».

отображается группа безопасности short-links-service;

статус группы безопасности — «Создана».

На странице сервиса «Виртуальные машины»:

- отображается виртуальная машина short-links-service;
- статус виртуальной машины — «Запущена».

отображается виртуальная машина short-links-service;

статус виртуальной машины — «Запущена».

На странице сервиса «Managed PostgreSQL»:

- отображается кластер short-links-service;
- статус кластера — «Доступен».

отображается кластер short-links-service;

статус кластера — «Доступен».

## 2. Настройте окружение на виртуальной машине

На этом шаге вы настроите систему и основные сетевые параметры виртуальной машины, установите необходимые пакеты и подготовите ее к запуску FastAPI-приложения.

1. В личном кабинете перейдите к сервису «Виртуальные машины» и выберите машину short-links-service.
2. [Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.
3. Активируйте сетевой интерфейс по [инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)инструкции:
sudo cloud-init cleansudo cloud-init init
4. Обновите систему:
sudo apt update && sudo apt upgrade -y
5. Установите Python и базовые пакеты:
sudo apt install -y python3-venv build-essential nginx snapd ufw postgresql-clientsudo snap install core; sudo snap refresh coresudo snap install --classic certbotsudo ln -s /snap/bin/certbot /usr/bin/certbot
6. Настройте файрвол:
sudo ufw allow OpenSSHsudo ufw allow 'Nginx Full'sudo ufw enable
7. Проверьте установку Python, nginx, postgresql-client, ufw:
python3 --versionnginx -vsudo ufw status

В личном кабинете перейдите к сервису «Виртуальные машины» и выберите машину short-links-service.

[Подключитесь к виртуальной машине через серийную консоль](https://cloud.ru/docs/virtual-machines/ug/topics/guides__console-serial)Подключитесь к виртуальной машине через серийную консоль.

Активируйте сетевой интерфейс по [инструкции](https://cloud.ru/docs/virtual-machines/ug/topics/guides__activate-network-interface)инструкции:

```bash
sudo
cloud-init clean
sudo
cloud-init init
```

Обновите систему:

```bash
sudo
apt
update
&&
sudo
apt
upgrade
-y
```

Установите Python и базовые пакеты:

```bash
sudo
apt
install
-y
python3-venv build-essential nginx snapd ufw postgresql-client
sudo
snap
install
core
;
sudo
snap refresh core
sudo
snap
install
--classic
certbot
sudo
ln
-s
/snap/bin/certbot /usr/bin/certbot
```

Настройте файрвол:

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

Проверьте установку Python, nginx, postgresql-client, ufw:

```bash
python3
--version
nginx
-v
sudo
ufw status
```

## 3. Разверните приложение

На этом шаге вы развернете FastAPI-приложение, подготовите файлы и подключите приложение к кластеру Managed PostgreSQL.

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.
2. Создайте директорию для приложения:
cd /home/user1mkdir short-links-servicecd short-links-service
3. Создайте файл сервера:
nano server.py

Вставьте следующий код:
from fastapi import FastAPI, HTTPException, Dependsfrom fastapi.responses import RedirectResponsefrom sqlalchemy import create_engine, Column, String, DateTime, Integerfrom sqlalchemy.orm import declarative_basefrom sqlalchemy.orm import sessionmaker, Sessionfrom pydantic import BaseModel, HttpUrlfrom datetime import datetimeimport osimport secretsimport stringfrom typing import Optionalfrom dotenv import load_dotenv
load_dotenv()
# Конфигурация базы данныхDATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/shortener_db")
engine = create_engine(DATABASE_URL)SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)Base = declarative_base()
# Модель базы данныхclass URLModel(Base): __tablename__ = "urls"
 id = Column(Integer, primary_key=True, index=True) original_url = Column(String, nullable=False) short_code = Column(String, unique=True, index=True, nullable=False) created_at = Column(DateTime, default=datetime.utcnow) clicks = Column(Integer, default=0)
# Создание таблицBase.metadata.create_all(bind=engine)
# Pydantic моделиclass URLCreate(BaseModel): original_url: HttpUrl
class URLResponse(BaseModel): original_url: str short_code: str short_url: str created_at: datetime clicks: int
 class Config: from_attributes = True
# FastAPI приложениеapp = FastAPI( title="URL Shortener API", description="API для создания коротких ссылок", version="1.0.0")
# Dependency для получения сессии БДdef get_db(): db = SessionLocal() try: yield db finally: db.close()
# Функция для генерации короткого кодаdef generate_short_code(length: int = 6) -> str: """Генерирует случайный короткий код из букв и цифр""" characters = string.ascii_letters + string.digits return ''.join(secrets.choice(characters) for _ in range(length))
# Эндпоинты@app.get("/health")async def health_check(): """Проверка здоровья приложения""" return {"status": "healthy", "timestamp": datetime.utcnow()}
@app.get("/")async def root(): return { "message": "URL Shortener API", "version": "1.0.0", "endpoints": { "create": "POST /shorten", "redirect": "GET /{short_code}", "stats": "GET /stats/{short_code}" } }
@app.post("/shorten", response_model=URLResponse)async def create_short_url(url_data: URLCreate, db: Session = Depends(get_db)): """Создание короткой ссылки"""
 # Проверяем, не существует ли уже такой URL existing_url = db.query(URLModel).filter(URLModel.original_url == str(url_data.original_url)).first() if existing_url: base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=existing_url.original_url, short_code=existing_url.short_code, short_url=f"{base_url}/{existing_url.short_code}", created_at=existing_url.created_at, clicks=existing_url.clicks )
 # Генерируем уникальный короткий код while True: short_code = generate_short_code() if not db.query(URLModel).filter(URLModel.short_code == short_code).first(): break
 # Создаем запись в БД db_url = URLModel( original_url=str(url_data.original_url), short_code=short_code ) db.add(db_url) db.commit() db.refresh(db_url)
 base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=db_url.original_url, short_code=db_url.short_code, short_url=f"{base_url}/{db_url.short_code}", created_at=db_url.created_at, clicks=db_url.clicks )
@app.get("/{short_code}")async def redirect_to_url(short_code: str, db: Session = Depends(get_db)): """Перенаправление на оригинальный URL"""
 url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first() if not url_record: raise HTTPException(status_code=404, detail="Ссылка не найдена")
 # Увеличиваем счетчик кликов url_record.clicks += 1 db.commit()
 return RedirectResponse(url=url_record.original_url, status_code=302)
@app.get("/stats/{short_code}", response_model=URLResponse)async def get_url_stats(short_code: str, db: Session = Depends(get_db)): """Получение статистики по короткой ссылке"""
 url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first() if not url_record: raise HTTPException(status_code=404, detail="Ссылка не найдена")
 base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=url_record.original_url, short_code=url_record.short_code, short_url=f"{base_url}/{url_record.short_code}", created_at=url_record.created_at, clicks=url_record.clicks )
if __name__ == "__main__": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)
4. Создайте файл зависимостей:
nano requirements.txt

Содержимое файла:
fastapi==0.104.1uvicorn[standard]==0.24.0sqlalchemy==2.0.23psycopg2-binary==2.9.9python-dotenv==1.0.0pydantic==2.5.0
5. Создайте и активируйте виртуальное окружение:
python3 -m venv venvsource venv/bin/activate
6. Установите зависимости:
pip install -r requirements.txt
7. Добавьте переменные среды:
nano .env

Вставьте содержимое в файл .env:
DATABASE_URL=postgresql://short_links:<PASSWORD>@<DB_PRIVATE_IP>:5432/shortener_dbBASE_URL=<IP-адрес>.nip.io

Где:

<PASSWORD> — пароль, который вы задали при создании пользователя базы данных.
<DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL.
<IP-адрес> — публичный IP-адрес виртуальной машины.
8. Запустите сервис:
python3 server.py

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.

Создайте директорию для приложения:

```bash
cd
/home/user1
mkdir
short-links-service
cd
short-links-service
```

Создайте файл сервера:

```bash
nano
server.py
```

Вставьте следующий код:

```bash
from
fastapi
import
FastAPI
,
HTTPException
,
Depends
from
fastapi
.
responses
import
RedirectResponse
from
sqlalchemy
import
create_engine
,
Column
,
String
,
DateTime
,
Integer
from
sqlalchemy
.
orm
import
declarative_base
from
sqlalchemy
.
orm
import
sessionmaker
,
Session
from
pydantic
import
BaseModel
,
HttpUrl
from
datetime
import
datetime
import
os
import
secrets
import
string
from
typing
import
Optional
from
dotenv
import
load_dotenv
load_dotenv
(
)
# Конфигурация базы данных
DATABASE_URL
=
os
.
getenv
(
"DATABASE_URL"
,
"postgresql://user:password@localhost:5432/shortener_db"
)
engine
=
create_engine
(
DATABASE_URL
)
SessionLocal
=
sessionmaker
(
autocommit
=
False
,
autoflush
=
False
,
bind
=
engine
)
Base
=
declarative_base
(
)
# Модель базы данных
class
URLModel
(
Base
)
:
__tablename__
=
"urls"
id
=
Column
(
Integer
,
primary_key
=
True
,
index
=
True
)
original_url
=
Column
(
String
,
nullable
=
False
)
short_code
=
Column
(
String
,
unique
=
True
,
index
=
True
,
nullable
=
False
)
created_at
=
Column
(
DateTime
,
default
=
datetime
.
utcnow
)
clicks
=
Column
(
Integer
,
default
=
0
)
# Создание таблиц
Base
.
metadata
.
create_all
(
bind
=
engine
)
# Pydantic модели
class
URLCreate
(
BaseModel
)
:
original_url
:
HttpUrl
class
URLResponse
(
BaseModel
)
:
original_url
:
str
short_code
:
str
short_url
:
str
created_at
:
datetime
clicks
:
int
class
Config
:
from_attributes
=
True
# FastAPI приложение
app
=
FastAPI
(
title
=
"URL Shortener API"
,
description
=
"API для создания коротких ссылок"
,
version
=
"1.0.0"
)
# Dependency для получения сессии БД
def
get_db
(
)
:
db
=
SessionLocal
(
)
try
:
yield
db
finally
:
db
.
close
(
)
# Функция для генерации короткого кода
def
generate_short_code
(
length
:
int
=
6
)
-
>
str
:
"""Генерирует случайный короткий код из букв и цифр"""
characters
=
string
.
ascii_letters
+
string
.
digits
return
''
.
join
(
secrets
.
choice
(
characters
)
for
_
in
range
(
length
)
)
# Эндпоинты
@app
.
get
(
"/health"
)
async
def
health_check
(
)
:
"""Проверка здоровья приложения"""
return
{
"status"
:
"healthy"
,
"timestamp"
:
datetime
.
utcnow
(
)
}
@app
.
get
(
"/"
)
async
def
root
(
)
:
return
{
"message"
:
"URL Shortener API"
,
"version"
:
"1.0.0"
,
"endpoints"
:
{
"create"
:
"POST /shorten"
,
"redirect"
:
"GET /{short_code}"
,
"stats"
:
"GET /stats/{short_code}"
}
}
@app
.
post
(
"/shorten"
,
response_model
=
URLResponse
)
async
def
create_short_url
(
url_data
:
URLCreate
,
db
:
Session
=
Depends
(
get_db
)
)
:
"""Создание короткой ссылки"""
# Проверяем, не существует ли уже такой URL
existing_url
=
db
.
query
(
URLModel
)
.
filter
(
URLModel
.
original_url
==
str
(
url_data
.
original_url
)
)
.
first
(
)
if
existing_url
:
base_url
=
os
.
getenv
(
"BASE_URL"
,
"https://yourdomain.com"
)
return
URLResponse
(
original_url
=
existing_url
.
original_url
,
short_code
=
existing_url
.
short_code
,
short_url
=
f"
{
base_url
}
/
{
existing_url
.
short_code
}
"
,
created_at
=
existing_url
.
created_at
,
clicks
=
existing_url
.
clicks
)
# Генерируем уникальный короткий код
while
True
:
short_code
=
generate_short_code
(
)
if
not
db
.
query
(
URLModel
)
.
filter
(
URLModel
.
short_code
==
short_code
)
.
first
(
)
:
break
# Создаем запись в БД
db_url
=
URLModel
(
original_url
=
str
(
url_data
.
original_url
)
,
short_code
=
short_code
)
db
.
add
(
db_url
)
db
.
commit
(
)
db
.
refresh
(
db_url
)
base_url
=
os
.
getenv
(
"BASE_URL"
,
"https://yourdomain.com"
)
return
URLResponse
(
original_url
=
db_url
.
original_url
,
short_code
=
db_url
.
short_code
,
short_url
=
f"
{
base_url
}
/
{
db_url
.
short_code
}
"
,
created_at
=
db_url
.
created_at
,
clicks
=
db_url
.
clicks
)
@app
.
get
(
"/{short_code}"
)
async
def
redirect_to_url
(
short_code
:
str
,
db
:
Session
=
Depends
(
get_db
)
)
:
"""Перенаправление на оригинальный URL"""
url_record
=
db
.
query
(
URLModel
)
.
filter
(
URLModel
.
short_code
==
short_code
)
.
first
(
)
if
not
url_record
:
raise
HTTPException
(
status_code
=
404
,
detail
=
"Ссылка не найдена"
)
# Увеличиваем счетчик кликов
url_record
.
clicks
+=
1
db
.
commit
(
)
return
RedirectResponse
(
url
=
url_record
.
original_url
,
status_code
=
302
)
@app
.
get
(
"/stats/{short_code}"
,
response_model
=
URLResponse
)
async
def
get_url_stats
(
short_code
:
str
,
db
:
Session
=
Depends
(
get_db
)
)
:
"""Получение статистики по короткой ссылке"""
url_record
=
db
.
query
(
URLModel
)
.
filter
(
URLModel
.
short_code
==
short_code
)
.
first
(
)
if
not
url_record
:
raise
HTTPException
(
status_code
=
404
,
detail
=
"Ссылка не найдена"
)
base_url
=
os
.
getenv
(
"BASE_URL"
,
"https://yourdomain.com"
)
return
URLResponse
(
original_url
=
url_record
.
original_url
,
short_code
=
url_record
.
short_code
,
short_url
=
f"
{
base_url
}
/
{
url_record
.
short_code
}
"
,
created_at
=
url_record
.
created_at
,
clicks
=
url_record
.
clicks
)
if
__name__
==
"__main__"
:
import
uvicorn
uvicorn
.
run
(
app
,
host
=
"0.0.0.0"
,
port
=
8000
)
```

Создайте файл зависимостей:

```bash
nano
requirements.txt
```

Содержимое файла:

```bash
fastapi
==
0.104
.1
uvicorn
[
standard
]
==
0.24
.0
sqlalchemy
==
2.0
.23
psycopg2-binary
==
2.9
.9
python-dotenv
==
1.0
.0
pydantic
==
2.5
.0
```

Создайте и активируйте виртуальное окружение:

```bash
python3
-m
venv venv
source
venv/bin/activate
```

Установите зависимости:

```bash
pip
install
-r
requirements.txt
```

Добавьте переменные среды:

```bash
nano
.env
```

Вставьте содержимое в файл .env:

```bash
DATABASE_URL
=
postgresql://short_links:
<
PASSWORD
>
@
<
DB_PRIVATE_IP
>
:5432/shortener_db
BASE_URL
=
<
IP-адрес
>
.nip.io
```

Где:

- <PASSWORD> — пароль, который вы задали при создании пользователя базы данных.
- <DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL.
- <IP-адрес> — публичный IP-адрес виртуальной машины.

<PASSWORD> — пароль, который вы задали при создании пользователя базы данных.

<DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL.

<IP-адрес> — публичный IP-адрес виртуальной машины.

Запустите сервис:

```bash
python3 server.py
```

## 4. Настройте сервис, nginx и HTTPS

В этом шаге вы автоматически опубликуете API-приложение через системный сервис, настроите обратный прокси через nginx и выпустите бесплатный SSL-сертификат с помощью Let’s Encrypt.

### Настройте сервис

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.
2. Создайте спецификацию сервиса:
sudo nano /etc/systemd/system/short-links.service

Вставьте в спецификацию следующее содержимое:
[Unit]Description=Short Links ServiceAfter=network.target
[Service]User=user1Group=user1WorkingDirectory=/home/user1/short-links-serviceEnvironment="PATH=/home/user1/short-links-service/venv/bin"EnvironmentFile=/home/user1/short-links-service/.envExecStart=/home/user1/short-links-service/venv/bin/uvicorn server:app --host 127.0.0.1 --port 8000Restart=always
[Install]WantedBy=multi-user.target

При необходимости замените user1 на имя своего пользователя.
3. Запустите сервис:
sudo systemctl daemon-reloadsudo systemctl enable short-linkssudo systemctl start short-links
4. Проверьте статус сервиса:
sudo systemctl status short-links
5. Убедитесь, что сервис находится в статусе «active (running)».

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.

Создайте спецификацию сервиса:

```bash
sudo
nano
/etc/systemd/system/short-links.service
```

Вставьте в спецификацию следующее содержимое:

```bash
[
Unit
]
Description
=
Short Links Service
After
=
network.target
[
Service
]
User
=
user1
Group
=
user1
WorkingDirectory
=
/home/user1/short-links-service
Environment
=
"PATH=/home/user1/short-links-service/venv/bin"
EnvironmentFile
=
/home/user1/short-links-service/.env
ExecStart
=
/home/user1/short-links-service/venv/bin/uvicorn server:app
--host
127.0
.0.1
--port
8000
Restart
=
always
[
Install
]
WantedBy
=
multi-user.target
```

При необходимости замените user1 на имя своего пользователя.

Запустите сервис:

```bash
sudo
systemctl daemon-reload
sudo
systemctl
enable
short-links
sudo
systemctl start short-links
```

Проверьте статус сервиса:

```bash
sudo
systemctl status short-links
```

Убедитесь, что сервис находится в статусе «active (running)».

### Зарегистрируйте бесплатный домен

1. В сервисе виртуальных машин скопируйте публичный IP-адрес вашей виртуальной машины.
2. Сформируйте доменное имя по шаблону <IP-адрес>.nip.io (например, 1.2.3.4.nip.io).
3. Проверьте, что в браузере по адресу http://<IP-адрес>.nip.io загружается страница Welcome to nginx.

В сервисе виртуальных машин скопируйте публичный IP-адрес вашей виртуальной машины.

Сформируйте доменное имя по шаблону <IP-адрес>.nip.io (например, 1.2.3.4.nip.io).

Проверьте, что в браузере по адресу http://<IP-адрес>.nip.io загружается страница Welcome to nginx.

### Настройте nginx

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.
2. Создайте конфигурационный файл:
sudo nano /etc/nginx/sites-available/short-links-service.conf
3. Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.
server { listen 80; server_name <IP-адрес>.nip.io www.<IP-адрес>.nip.io;
 # Проксирование запросов к FastAPI location / { proxy_pass http://127.0.0.1:8000; proxy_set_header Host $host; proxy_set_header X-Real-IP $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; proxy_set_header X-Forwarded-Proto $scheme; proxy_redirect off; }
 # Логи access_log /var/log/nginx/short_links.log; error_log /var/log/nginx/short_links_error.log;}
4. Примените конфигурацию и перезапустите nginx:
sudo ln -sf /etc/nginx/sites-available/short-links-service.conf /etc/nginx/sites-enabled/short-links-service.confsudo rm -f /etc/nginx/sites-enabled/defaultsudo nginx -tsudo systemctl reload nginx
5. Проверьте, что nginx работает:
sudo systemctl status nginx

Cервис nginx должен быть в статусе «active (running)».
6. Перейдите по адресу http://<IP-адрес>.nip.io/docs.
Откроется документация API FastAPI по незащищенному протоколу HTTP.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.

Создайте конфигурационный файл:

```bash
sudo
nano
/etc/nginx/sites-available/short-links-service.conf
```

Вставьте конфигурацию, заменив <IP-адрес> на IP-адрес вашей виртуальной машины.

```bash
server
{
listen
80
;
server_name
<
IP-адрес
>
.nip.io www.
<
IP-адрес
>
.nip.io
;
# Проксирование запросов к FastAPI
location /
{
proxy_pass http://127.0.0.1:8000
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
proxy_set_header X-Forwarded-Proto
$scheme
;
proxy_redirect off
;
}
# Логи
access_log /var/log/nginx/short_links.log
;
error_log /var/log/nginx/short_links_error.log
;
}
```

Примените конфигурацию и перезапустите nginx:

```bash
sudo
ln
-sf
/etc/nginx/sites-available/short-links-service.conf /etc/nginx/sites-enabled/short-links-service.conf
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

Проверьте, что nginx работает:

```bash
sudo
systemctl status nginx
```

Cервис nginx должен быть в статусе «active (running)».

Перейдите по адресу http://<IP-адрес>.nip.io/docs.

Откроется документация API FastAPI по незащищенному протоколу HTTP.

### Выпустите SSL сертификат и настройте HTTPS

1. [Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.
2. Запустите команду для выпуска SSL-сертификата.
sudo certbot --nginx -d <DOMAIN> --redirect --agree-tos -m <EMAIL>

Где:

<DOMAIN> — ваш домен из nip.io.
<EMAIL> — ваш email.
3. После успешного выпуска сертификата, перейдите по адресу https://<IP-адрес>.nip.io/docs.
Откроется документация API FastAPI. В свойствах сайта браузер отметит соединение как безопасное.
4. Проверьте работу API:

В документации вызовите POST-запрос:
{ "original_url": "https://console.cloud.ru/"}

Вернется короткая ссылка.
Перейдите по ссылке — должен открыться сайт [https://console.cloud.ru/](https://console.cloud.ru/)https://console.cloud.ru/.

[Подключитесь к виртуальной машине](https://cloud.ru/docs/virtual-machines/ug/topics/guides__connection)Подключитесь к виртуальной машине.

Запустите команду для выпуска SSL-сертификата.

```bash
sudo
certbot
--nginx
-d
<
DOMAIN
>
--redirect
--agree-tos
-m
<
EMAIL
>
```

Где:

- <DOMAIN> — ваш домен из nip.io.
- <EMAIL> — ваш email.

<DOMAIN> — ваш домен из nip.io.

<EMAIL> — ваш email.

После успешного выпуска сертификата, перейдите по адресу https://<IP-адрес>.nip.io/docs.

Откроется документация API FastAPI. В свойствах сайта браузер отметит соединение как безопасное.

Проверьте работу API:

1. В документации вызовите POST-запрос:
{ "original_url": "https://console.cloud.ru/"}
2. Вернется короткая ссылка.
3. Перейдите по ссылке — должен открыться сайт [https://console.cloud.ru/](https://console.cloud.ru/)https://console.cloud.ru/.

В документации вызовите POST-запрос:

```bash
{
"original_url"
:
"https://console.cloud.ru/"
}
```

Вернется короткая ссылка.

Перейдите по ссылке — должен открыться сайт [https://console.cloud.ru/](https://console.cloud.ru/)https://console.cloud.ru/.

## Результат

Вы реализовали инфраструктуру и приложение для сервиса сокращения ссылок в облаке с управляемой базой данных, надежной сетевой изоляцией и публикацией API по HTTPS.
Полученные навыки помогут создавать сервисы с использованием управляемых баз данных и создавать безопасные облачные среды для приложений разного типа.
