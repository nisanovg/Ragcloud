---
title: Оптимизация производительности Web-приложения с Managed Redis®
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance
topic: database
---
# Оптимизация производительности Web-приложения с Managed Redis®

С помощью этого руководства вы оптимизируете производительность Web-приложения с использованием сервиса Managed Redis®.
Вы создадите и настроите сервис Managed Redis®, соедините его с Web-сервисом на виртуальной машине и Managed PostgreSQL®, а затем оптимизируете Web-приложение на Fast API с использованием технологии кеширования данных.
Также создадите виртуальную машину Ubuntu 22.04 и запустите нагрузочный тест с использованием технологии Grafana k6.
В конце сравните результаты нагрузочного тестирования Web-приложения с кешированием и без.

Вы будете использовать следующие сервисы:

- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.
- [Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.
- [Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.
- [VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.
- [Grafana k6](https://k6.io/)Grafana k6 — фреймворк для нагрузочного тестирования веб-приложений.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина.

[Managed Redis](https://cloud.ru/docs/redis/ug/index)Managed Redis — хранилище данных в оперативной памяти.

[Публичный IP-адрес](https://cloud.ru/docs/public-ip/ug/topics/guides__allocate-ip)Публичный IP-адрес — для доступа к сервису через интернет.

[VPC](https://cloud.ru/docs/evolution-vpc/ug/index)VPC — изолированная виртуальная сеть для создания безопасной инфраструктуры.

[Grafana k6](https://k6.io/)Grafana k6 — фреймворк для нагрузочного тестирования веб-приложений.

Шаги:

1. [Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Разверните необходимые ресурсы в облаке.
2. [Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Настройте окружение на виртуальной машине.
3. [Запустите нагрузочный тест без кеширования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Запустите нагрузочный тест без кеширования.
4. [Настройте кеширование для Web-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Настройте кеширование для Web-приложения.
5. [Запустите нагрузочный тест с кешированием](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Запустите нагрузочный тест с кешированием.
6. [Удалите виртуальную машину после тестирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Удалите виртуальную машину после тестирования.

[Разверните необходимые ресурсы в облаке](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Разверните необходимые ресурсы в облаке.

[Настройте окружение на виртуальной машине](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Настройте окружение на виртуальной машине.

[Запустите нагрузочный тест без кеширования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Запустите нагрузочный тест без кеширования.

[Настройте кеширование для Web-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Настройте кеширование для Web-приложения.

[Запустите нагрузочный тест с кешированием](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Запустите нагрузочный тест с кешированием.

[Удалите виртуальную машину после тестирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-redis__web-performance)Удалите виртуальную машину после тестирования.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.
3. [Разверните Web-сервис, выполнив сценарий из руководства](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните Web-сервис, выполнив сценарий из руководства.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте и загрузите SSH-ключ в облако](https://cloud.ru/docs/public-keys/ug/topics/guides__generate-key)Создайте и загрузите SSH-ключ в облако.

[Разверните Web-сервис, выполнив сценарий из руководства](https://cloud.ru/docs/tutorials-evolution/list/topics/free-tier-vm__postgresql-connection)Разверните Web-сервис, выполнив сценарий из руководства.

## 1. Разверните необходимые ресурсы в облаке

На этом шаге вы создадите виртуальную машину и кластер Managed Redis® для проведения тестирования.

1. [Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

Название: k6-load-test.
Образ: Публичные → Ubuntu 22.04.
Метод аутентификации: SSH-ключ.
SSH-ключ: ваш SSH-ключ.
Имя хоста: k6-load-test.
Подключить публичный IP: включено.
Тип IP-адреса: Прямой.
Группы безопасности: SSH-access_ru.AZ-1.
Подсеть: short-link-service-subnet.
Гарантированная доля vCPU: 30%.
vCPU: 1.
RAM: 1.

Убедитесь, что в личном кабинете в сервисе «Виртуальные машины» отображается виртуальная машина k6-load-test в статусе «Запущена».
2. [Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

Название: short-links-cache.
Версия Redis: v7.2.11.
vCPU: 2.
RAM: 4.
Подсеть: short-link-service-subnet.

Убедитесь, что в личном кабинете в сервисе Managed Redis® отображается кластер short-links-cache в статусе «Доступен».

[Создайте виртуальную машину](https://cloud.ru/docs/virtual-machines/ug/topics/guides__create-vm)Создайте виртуальную машину со следующими параметрами:

- Название: k6-load-test.
- Образ: Публичные → Ubuntu 22.04.
- Метод аутентификации: SSH-ключ.
- SSH-ключ: ваш SSH-ключ.
- Имя хоста: k6-load-test.
- Подключить публичный IP: включено.
- Тип IP-адреса: Прямой.
- Группы безопасности: SSH-access_ru.AZ-1.
- Подсеть: short-link-service-subnet.
- Гарантированная доля vCPU: 30%.
- vCPU: 1.
- RAM: 1.

Название: k6-load-test.

Образ: Публичные → Ubuntu 22.04.

Метод аутентификации: SSH-ключ.

SSH-ключ: ваш SSH-ключ.

Имя хоста: k6-load-test.

Подключить публичный IP: включено.

Тип IP-адреса: Прямой.

Группы безопасности: SSH-access_ru.AZ-1.

Подсеть: short-link-service-subnet.

Гарантированная доля vCPU: 30%.

vCPU: 1.

RAM: 1.

Убедитесь, что в личном кабинете в сервисе «Виртуальные машины» отображается виртуальная машина k6-load-test в статусе «Запущена».

[Создайте кластер Managed Redis](https://cloud.ru/docs/redis/ug/topics/guides__cluster-creation)Создайте кластер Managed Redis со следующими параметрами:

- Название: short-links-cache.
- Версия Redis: v7.2.11.
- vCPU: 2.
- RAM: 4.
- Подсеть: short-link-service-subnet.

Название: short-links-cache.

Версия Redis: v7.2.11.

vCPU: 2.

RAM: 4.

Подсеть: short-link-service-subnet.

Убедитесь, что в личном кабинете в сервисе Managed Redis® отображается кластер short-links-cache в статусе «Доступен».

## 2. Настройте окружение на виртуальной машине

Подготовьте виртуальную машину для проведения нагрузочного теста.

1. [Подключитесь к виртуальной машине k6-load-test по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине k6-load-test по SSH.
2. Обновите систему и установите необходимые пакеты:
sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential git curl unzip
3. Установите NodeJS:
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -sudo apt install -y nodejs
4. Установите k6:
sudo apt install -y gnupg ca-certificatescurl -fsSL https://dl.k6.io/key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/k6-archive-keyring.gpgecho "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" \ | sudo tee /etc/apt/sources.list.d/k6.listsudo apt updatesudo apt install -y k6
5. Проверьте установку:
node -vk6 version

[Подключитесь к виртуальной машине k6-load-test по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине k6-load-test по SSH.

Обновите систему и установите необходимые пакеты:

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
build-essential
git
curl
unzip
```

Установите NodeJS:

```bash
curl
-fsSL
https://deb.nodesource.com/setup_18.x
|
sudo
-E
bash
-
sudo
apt
install
-y
nodejs
```

Установите k6:

```bash
sudo
apt
install
-y
gnupg ca-certificates
curl
-fsSL
https://dl.k6.io/key.gpg
|
sudo
gpg
--dearmor
-o
/usr/share/keyrings/k6-archive-keyring.gpg
echo
"deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main"
\
|
sudo
tee
/etc/apt/sources.list.d/k6.list
sudo
apt
update
sudo
apt
install
-y
k6
```

Проверьте установку:

```bash
node
-v
k6 version
```

## 3. Запустите нагрузочный тест без кеширования

На этом шаге вы проведете нагрузочный тест без использования кеширования для оценки производительности системы.

1. Создайте директорию и файл теста:
mkdir loadtestcd loadtestnano short-links.test.js
2. Вставьте содержимое теста, заменив <IP-ADDRESS> на публичный IP-адрес вашей виртуальной машины short-links-service.
import http from 'k6/http';import { check, sleep } from 'k6';
export const options = { scenarios: { shortener_flow: { executor: 'constant-vus', vus: 10, duration: '1m' }, },};
const BASE = 'https://<IP-ADDRESS>.nip.io';
export default function () { const createPayload = JSON.stringify({ original_url: 'https://cloud.ru' }); const params = { headers: { 'Content-Type': 'application/json' } };
 const createRes = http.post(`${BASE}/shorten`, createPayload, params);
 check(createRes, { 'create - status 201/200': r => r.status === 201 || r.status === 200, 'create - has short_code': r => !!r.json('short_code'), });
 const shortCode = createRes.json('short_code'); const targetURL = `${BASE}/${shortCode}`;
 for (let i = 0; i < 20; i++) { const res = http.get(targetURL, { redirects: 0 }); check(res, { 'redirect status 302/301': r => r.status === 302 || r.status === 301, }); }
 sleep(1);}

Данный нагрузочный тест моделирует работу 10 виртуальных пользователей, которые в течение одной минуты создают короткие ссылки через POST-запрос и затем по 20 раз запрашивают каждую полученную короткую ссылку, проверяя корректность редиректа.
3. Запустите нагрузочный тест командой:
k6 run short-links.test.js
4. Дождитесь выполнения теста и проанализируйте результаты.
Пример результата:
█ TOTAL RESULTS
 checks_total.......................: 1584 24.456932/s checks_succeeded...................: 100.00% 1584 out of 1584 checks_failed......................: 0.00% 0 out of 1584
 ✓ create - status 201/200 ✓ create - has short_code ✓ redirect status 302/301
 HTTP http_req_duration.......................................................: avg=370.01ms min=19.25ms med=387.07ms max=622.41ms p(90)=453.49ms p(95)=483.84ms { expected_response:true }............................................: avg=370.01ms min=19.25ms med=387.07ms max=622.41ms p(90)=453.49ms p(95)=483.84ms http_req_failed.........................................................: 0.00% 0 out of 1512 http_reqs...............................................................: 1512 23.345253/s
 EXECUTION iteration_duration......................................................: avg=8.78s min=5.8s med=8.86s max=10.19s p(90)=9.85s p(95)=10.01s iterations..............................................................: 72 1.111679/s vus.....................................................................: 4 min=4 max=10 vus_max.................................................................: 10 min=10 max=10
 NETWORK data_received...........................................................: 341 kB 5.3 kB/s data_sent...............................................................: 172 kB 2.7 kB/s
running (1m04.8s), 00/10 VUs, 72 complete and 0 interrupted iterationsshortener_flow ✓ [======================================] 10 VUs 1m0s

Результаты теста k6 показывают, что система полностью справилась с заявленной нагрузкой: все 1584 проверки («checks») прошли успешно без ошибок, доля неуспешных HTTP-запросов — 0%, а среднее время отклика сервера составило 370 мс при медиане 387 мс, и даже для 95% самых «медленных» запросов время не превышало 484 мс — это свидетельствует о стабильной и быстрой работе приложения на тестовой нагрузке из 10 виртуальных пользователей.

Создайте директорию и файл теста:

```bash
mkdir
loadtest
cd
loadtest
nano
short-links.test.js
```

Вставьте содержимое теста, заменив <IP-ADDRESS> на публичный IP-адрес вашей виртуальной машины short-links-service.

```bash
import
http
from
'k6/http'
;
import
{
check
,
sleep
}
from
'k6'
;
export
const
options
=
{
scenarios
:
{
shortener_flow
:
{
executor
:
'constant-vus'
,
vus
:
10
,
duration
:
'1m'
}
,
}
,
}
;
const
BASE
=
'https://<IP-ADDRESS>.nip.io'
;
export
default
function
(
)
{
const
createPayload
=
JSON
.
stringify
(
{
original_url
:
'https://cloud.ru'
}
)
;
const
params
=
{
headers
:
{
'Content-Type'
:
'application/json'
}
}
;
const
createRes
=
http
.
post
(
`
${
BASE
}
/shorten
`
,
createPayload
,
params
)
;
check
(
createRes
,
{
'create - status 201/200'
:
r
=>
r
.
status
===
201
||
r
.
status
===
200
,
'create - has short_code'
:
r
=>
!
!
r
.
json
(
'short_code'
)
,
}
)
;
const
shortCode
=
createRes
.
json
(
'short_code'
)
;
const
targetURL
=
`
${
BASE
}
/
${
shortCode
}
`
;
for
(
let
i
=
0
;
i
<
20
;
i
++
)
{
const
res
=
http
.
get
(
targetURL
,
{
redirects
:
0
}
)
;
check
(
res
,
{
'redirect status 302/301'
:
r
=>
r
.
status
===
302
||
r
.
status
===
301
,
}
)
;
}
sleep
(
1
)
;
}
```

Данный нагрузочный тест моделирует работу 10 виртуальных пользователей, которые в течение одной минуты создают короткие ссылки через POST-запрос и затем по 20 раз запрашивают каждую полученную короткую ссылку, проверяя корректность редиректа.

Запустите нагрузочный тест командой:

```bash
k6 run short-links.test.js
```

Дождитесь выполнения теста и проанализируйте результаты.
Пример результата:

```bash
█ TOTAL RESULTS
checks_total
..
..
..
..
..
..
..
..
..
..
..
.:
1584
24.456932
/s
checks_succeeded
..
..
..
..
..
..
..
..
..
.:
100.00
%
1584
out of
1584
checks_failed
..
..
..
..
..
..
..
..
..
..
..
:
0.00
%
0
out of
1584
✓ create - status
201
/200
✓ create - has short_code
✓ redirect status
302
/301
HTTP
http_req_duration
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
avg
=
370
.01ms
min
=
19
.25ms
med
=
387
.07ms
max
=
622
.41ms p
(
90
)
=
453
.49ms p
(
95
)
=
483
.84ms
{
expected_response:true
}
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
avg
=
370
.01ms
min
=
19
.25ms
med
=
387
.07ms
max
=
622
.41ms p
(
90
)
=
453
.49ms p
(
95
)
=
483
.84ms
http_req_failed
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
0.00
%
0
out of
1512
http_reqs
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
1512
23.345253
/s
EXECUTION
iteration_duration
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
avg
=
8
.78s
min
=
5
.8s
med
=
8
.86s
max
=
10
.19s p
(
90
)
=
9
.85s p
(
95
)
=
10
.01s
iterations
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
72
1.111679
/s
vus
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
4
min
=
4
max
=
10
vus_max
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
10
min
=
10
max
=
10
NETWORK
data_received
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
341
kB
5.3
kB/s
data_sent
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
172
kB
2.7
kB/s
running
(
1m04.8s
)
, 00/10 VUs,
72
complete and
0
interrupted iterations
shortener_flow ✓
[
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
]
10
VUs 1m0s
```

Результаты теста k6 показывают, что система полностью справилась с заявленной нагрузкой: все 1584 проверки («checks») прошли успешно без ошибок, доля неуспешных HTTP-запросов — 0%, а среднее время отклика сервера составило 370 мс при медиане 387 мс, и даже для 95% самых «медленных» запросов время не превышало 484 мс — это свидетельствует о стабильной и быстрой работе приложения на тестовой нагрузке из 10 виртуальных пользователей.

## 4. Настройте кеширование для Web-приложения

На этом шаге вы добавите кеширование с использованием Redis в ваше Web-приложение для повышения эффективности.

1. [Подключитесь к виртуальной машине short-links-service по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине short-links-service по SSH.
2. Перейдите в директорию приложения:
cd short-links-service
3. Активируйте виртуальное окружение:
source venv/bin/activate
4. Замените содержимое файла сервера server.py на обновленное с поддержкой Redis.
nano server.py

Содержимое файла:
import asyncioimport jsonimport osimport secretsimport stringimport threadingimport timefrom datetime import datetime
from dotenv import load_dotenvfrom fastapi import Depends, FastAPI, HTTPExceptionfrom fastapi.responses import RedirectResponsefrom pydantic import BaseModel, HttpUrlfrom sqlalchemy import Column, DateTime, Integer, String, create_enginefrom sqlalchemy.orm import Session, declarative_base, sessionmaker
# 🔴 redis (async, pooled)import redis.asyncio as redis # redis-py ≥5 provides asyncio & pooling
load_dotenv()
# -------------------------------------------------# Environment & external services# -------------------------------------------------DATABASE_URL = os.getenv( "DATABASE_URL", "postgresql://user:password@localhost:5432/shortener_db")REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0") # 🔴 redisCACHE_TTL = int(os.getenv("CACHE_TTL", "3600")) # 🔴 redisSYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", "300")) # 🔴 redisMAX_REDIS_CONNECTIONS = int(os.getenv("REDIS_POOL_SIZE", "20")) # 🔴 redis
# DB -------------------------------------------------------------------------engine = create_engine(DATABASE_URL)SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)Base = declarative_base()

class URLModel(Base): __tablename__ = "urls" id = Column(Integer, primary_key=True, index=True) original_url = Column(String, nullable=False) short_code = Column(String, unique=True, index=True, nullable=False) created_at = Column(DateTime, default=datetime.utcnow) clicks = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)
# -------------------------------------------------# Redis: build a reusable async connection-pool client# -------------------------------------------------redis_pool: redis.ConnectionPool | None = None # set on startupredis_client: redis.Redis | None = None # set on startup

# -------------------------------------------------# Pydantic# -------------------------------------------------class URLCreate(BaseModel): original_url: HttpUrl

class URLResponse(BaseModel): original_url: str short_code: str short_url: str created_at: datetime clicks: int
 class Config: from_attributes = True

# -------------------------------------------------# FastAPI# -------------------------------------------------app = FastAPI( title="URL Shortener API", description="API для создания коротких ссылок", version="1.0.0",)

# -------------------------------------------------# Helpers# -------------------------------------------------def get_db(): db = SessionLocal() try: yield db finally: db.close()

def generate_short_code(length: int = 6) -> str: return "".join( secrets.choice(string.ascii_letters + string.digits) for _ in range(length) )

# 🔴 redis – cache keys helpersdef _clicks_key(code: str) -> str: return f"url:{code}:clicks"

def _url_key(code: str) -> str: return f"url:{code}:data"

# -------------------------------------------------# Background sync: flush cached click counts# -------------------------------------------------async def _sync_clicks_async(): assert redis_client # mypy/IDE hint while True: print("Running background sync task") await asyncio.sleep(SYNC_INTERVAL) keys = await redis_client.keys("url:*:clicks") if not keys: continue with SessionLocal() as db: for k in keys: # k format: url:<code>:clicks code = k.split(":")[1] cached_clicks_raw = await redis_client.get(k) cached_clicks = int(cached_clicks_raw or 0) if cached_clicks: row = db.query(URLModel).filter(URLModel.short_code == code).first() if row: row.clicks += cached_clicks db.add(row) db.commit() await redis_client.delete(k)

# -------------------------------------------------# Application lifespan: create & close pool# -------------------------------------------------@app.on_event("startup")async def startup_event() -> None: global redis_pool, redis_client
 # 1. Build a pool with a max connection limit redis_pool = redis.ConnectionPool.from_url( REDIS_URL, max_connections=MAX_REDIS_CONNECTIONS, decode_responses=True, )
 # 2. Build a client bound to that pool redis_client = redis.Redis(connection_pool=redis_pool) # type: ignore[arg-type]
 # 3. Launch background syncing coroutine asyncio.create_task(_sync_clicks_async())

@app.on_event("shutdown")async def shutdown_event() -> None: # Close client and pool gracefully if redis_client: await redis_client.aclose() if redis_pool: await redis_pool.aclose()

# -------------------------------------------------# End-points# -------------------------------------------------@app.get("/health")async def health_check(): return {"status": "healthy", "timestamp": datetime.utcnow()}

@app.get("/")async def root(): return { "message": "URL Shortener API", "version": "1.0.0", "endpoints": { "create": "POST /shorten", "redirect": "GET /{short_code}", "stats": "GET /stats/{short_code}", }, }

@app.post("/shorten", response_model=URLResponse)async def create_short_url(url_data: URLCreate, db: Session = Depends(get_db)): existing_url = ( db.query(URLModel) .filter(URLModel.original_url == str(url_data.original_url)) .first() ) if existing_url: base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=existing_url.original_url, short_code=existing_url.short_code, short_url=f"{base_url}/{existing_url.short_code}", created_at=existing_url.created_at, clicks=existing_url.clicks, )
 while True: short_code = generate_short_code() if not db.query(URLModel).filter(URLModel.short_code == short_code).first(): break
 db_url = URLModel(original_url=str(url_data.original_url), short_code=short_code) db.add(db_url) db.commit() db.refresh(db_url)
 # 🔴 caching a key in redis await redis_client.setex( # type: ignore[func-returns-value] _url_key(short_code), CACHE_TTL, json.dumps( { "original_url": db_url.original_url, "created_at": db_url.created_at.isoformat(), } ), )
 base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=db_url.original_url, short_code=db_url.short_code, short_url=f"{base_url}/{db_url.short_code}", created_at=db_url.created_at, clicks=db_url.clicks, )

@app.get("/{short_code}")async def redirect_to_url(short_code: str, db: Session = Depends(get_db)): # 🔴 attempting to retrieve data from redis cache_key = _url_key(short_code) cached = await redis_client.get(cache_key) # type: ignore[attr-defined] if cached: data = json.loads(cached) await redis_client.incr(_clicks_key(short_code)) # type: ignore[attr-defined] return RedirectResponse(url=data["original_url"], status_code=302)
 url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first() if not url_record: raise HTTPException(status_code=404, detail="Ссылка не найдена")
 # 🔴 caching a data in redis await redis_client.setex( # type: ignore[func-returns-value] cache_key, CACHE_TTL, json.dumps( { "original_url": url_record.original_url, "created_at": url_record.created_at.isoformat(), } ), ) await redis_client.incr(_clicks_key(short_code)) # type: ignore[attr-defined]
 return RedirectResponse(url=url_record.original_url, status_code=302)

@app.get("/stats/{short_code}", response_model=URLResponse)async def get_url_stats(short_code: str, db: Session = Depends(get_db)): url_record = db.query(URLModel).filter(URLModel.short_code == short_code).first() if not url_record: raise HTTPException(status_code=404, detail="Ссылка не найдена")
 # 🔴 retrieving data from redis pending_raw = await redis_client.get(_clicks_key(short_code)) # type: ignore[attr-defined] pending = int(pending_raw or 0) total_clicks = url_record.clicks + pending
 base_url = os.getenv("BASE_URL", "https://yourdomain.com") return URLResponse( original_url=url_record.original_url, short_code=url_record.short_code, short_url=f"{base_url}/{url_record.short_code}", created_at=url_record.created_at, clicks=total_clicks, )

if __name__ == "__main__": import uvicorn
 uvicorn.run(app, host="0.0.0.0", port=8000)

Приложение теперь использует гибридную схему с Managed PostgreSQL® и Managed Redis® для кэширования и буферизации, что снижает нагрузку на базу данных и ускоряет работу сервиса.
Новый код, использующий Redis, отмечен комментариями с 🔴.
5. Откройте файл requirements.txt на редактирование и замените содержимое, добавив модули для работы с Managed Redis®.
nano requirements.txt

Содержимое файла:
uvicorn[standard]==0.24.0sqlalchemy==2.0.23psycopg2-binary==2.9.9python-dotenv==1.0.0pydantic==2.5.0redis==6.2.0aioredis==2.0.1

Добавлены новые библиотеки redis и aioredis.
6. Установите новые зависимости:
pip install -r requirements.txt
7. Откройте файл .env и обновите содержимое для подключения к Managed Redis® и Managed PostgreSQL®.
nano .env

Содержимое файла:
DATABASE_URL=postgresql://short_links:<PASSWORD>@<DB_PRIVATE_IP>:5432/short_linksBASE_URL=<IP-адрес>.nip.ioREDIS_URL=redis://:<REDIS_PASSWORD>@<REDIS_IP>:6379CACHE_TTL=3600SYNC_INTERVAL=60

Где:

<PASSWORD> — пароль, который вы задали при создании пользователя базы данных Managed PostgreSQL®.
<DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL®.
<IP-адрес> — публичный IP-адрес виртуальной машины.
<REDIS_IP> — IP-адрес сервиса Managed Redis®.
<REDIS_PASSWORD> — пароль от кластера Managed Redis®.
8. Перезапустите сервис short-links:
sudo systemctl daemon-reloadsudo systemctl restart short-links

[Подключитесь к виртуальной машине short-links-service по SSH](https://cloud.ru/docs/virtual-machines/ug/topics/guides__ssh-connection)Подключитесь к виртуальной машине short-links-service по SSH.

Перейдите в директорию приложения:

```bash
cd
short-links-service
```

Активируйте виртуальное окружение:

```bash
source
venv/bin/activate
```

Замените содержимое файла сервера server.py на обновленное с поддержкой Redis.

```bash
nano
server.py
```

Содержимое файла:

```bash
import
asyncio
import
json
import
os
import
secrets
import
string
import
threading
import
time
from
datetime
import
datetime
from
dotenv
import
load_dotenv
from
fastapi
import
Depends
,
FastAPI
,
HTTPException
from
fastapi
.
responses
import
RedirectResponse
from
pydantic
import
BaseModel
,
HttpUrl
from
sqlalchemy
import
Column
,
DateTime
,
Integer
,
String
,
create_engine
from
sqlalchemy
.
orm
import
Session
,
declarative_base
,
sessionmaker
# 🔴 redis (async, pooled)
import
redis
.
asyncio
as
redis
# redis-py ≥5 provides asyncio & pooling
load_dotenv
(
)
# -------------------------------------------------
# Environment & external services
# -------------------------------------------------
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
REDIS_URL
=
os
.
getenv
(
"REDIS_URL"
,
"redis://localhost:6379/0"
)
# 🔴 redis
CACHE_TTL
=
int
(
os
.
getenv
(
"CACHE_TTL"
,
"3600"
)
)
# 🔴 redis
SYNC_INTERVAL
=
int
(
os
.
getenv
(
"SYNC_INTERVAL"
,
"300"
)
)
# 🔴 redis
MAX_REDIS_CONNECTIONS
=
int
(
os
.
getenv
(
"REDIS_POOL_SIZE"
,
"20"
)
)
# 🔴 redis
# DB -------------------------------------------------------------------------
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
# -------------------------------------------------
# Redis: build a reusable async connection-pool client
# -------------------------------------------------
redis_pool
:
redis
.
ConnectionPool
|
None
=
None
# set on startup
redis_client
:
redis
.
Redis
|
None
=
None
# set on startup
# -------------------------------------------------
# Pydantic
# -------------------------------------------------
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
# -------------------------------------------------
# FastAPI
# -------------------------------------------------
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
,
)
# -------------------------------------------------
# Helpers
# -------------------------------------------------
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
return
""
.
join
(
secrets
.
choice
(
string
.
ascii_letters
+
string
.
digits
)
for
_
in
range
(
length
)
)
# 🔴 redis – cache keys helpers
def
_clicks_key
(
code
:
str
)
-
>
str
:
return
f"url:
{
code
}
:clicks"
def
_url_key
(
code
:
str
)
-
>
str
:
return
f"url:
{
code
}
:data"
# -------------------------------------------------
# Background sync: flush cached click counts
# -------------------------------------------------
async
def
_sync_clicks_async
(
)
:
assert
redis_client
# mypy/IDE hint
while
True
:
print
(
"Running background sync task"
)
await
asyncio
.
sleep
(
SYNC_INTERVAL
)
keys
=
await
redis_client
.
keys
(
"url:*:clicks"
)
if
not
keys
:
continue
with
SessionLocal
(
)
as
db
:
for
k
in
keys
:
# k format: url:<code>:clicks
code
=
k
.
split
(
":"
)
[
1
]
cached_clicks_raw
=
await
redis_client
.
get
(
k
)
cached_clicks
=
int
(
cached_clicks_raw
or
0
)
if
cached_clicks
:
row
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
code
)
.
first
(
)
if
row
:
row
.
clicks
+=
cached_clicks
db
.
add
(
row
)
db
.
commit
(
)
await
redis_client
.
delete
(
k
)
# -------------------------------------------------
# Application lifespan: create & close pool
# -------------------------------------------------
@app
.
on_event
(
"startup"
)
async
def
startup_event
(
)
-
>
None
:
global
redis_pool
,
redis_client
# 1. Build a pool with a max connection limit
redis_pool
=
redis
.
ConnectionPool
.
from_url
(
REDIS_URL
,
max_connections
=
MAX_REDIS_CONNECTIONS
,
decode_responses
=
True
,
)
# 2. Build a client bound to that pool
redis_client
=
redis
.
Redis
(
connection_pool
=
redis_pool
)
# type: ignore[arg-type]
# 3. Launch background syncing coroutine
asyncio
.
create_task
(
_sync_clicks_async
(
)
)
@app
.
on_event
(
"shutdown"
)
async
def
shutdown_event
(
)
-
>
None
:
# Close client and pool gracefully
if
redis_client
:
await
redis_client
.
aclose
(
)
if
redis_pool
:
await
redis_pool
.
aclose
(
)
# -------------------------------------------------
# End-points
# -------------------------------------------------
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
,
}
,
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
existing_url
=
(
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
,
)
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
# 🔴 caching a key in redis
await
redis_client
.
setex
(
# type: ignore[func-returns-value]
_url_key
(
short_code
)
,
CACHE_TTL
,
json
.
dumps
(
{
"original_url"
:
db_url
.
original_url
,
"created_at"
:
db_url
.
created_at
.
isoformat
(
)
,
}
)
,
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
,
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
# 🔴 attempting to retrieve data from redis
cache_key
=
_url_key
(
short_code
)
cached
=
await
redis_client
.
get
(
cache_key
)
# type: ignore[attr-defined]
if
cached
:
data
=
json
.
loads
(
cached
)
await
redis_client
.
incr
(
_clicks_key
(
short_code
)
)
# type: ignore[attr-defined]
return
RedirectResponse
(
url
=
data
[
"original_url"
]
,
status_code
=
302
)
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
# 🔴 caching a data in redis
await
redis_client
.
setex
(
# type: ignore[func-returns-value]
cache_key
,
CACHE_TTL
,
json
.
dumps
(
{
"original_url"
:
url_record
.
original_url
,
"created_at"
:
url_record
.
created_at
.
isoformat
(
)
,
}
)
,
)
await
redis_client
.
incr
(
_clicks_key
(
short_code
)
)
# type: ignore[attr-defined]
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
# 🔴 retrieving data from redis
pending_raw
=
await
redis_client
.
get
(
_clicks_key
(
short_code
)
)
# type: ignore[attr-defined]
pending
=
int
(
pending_raw
or
0
)
total_clicks
=
url_record
.
clicks
+
pending
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
total_clicks
,
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

Приложение теперь использует гибридную схему с Managed PostgreSQL® и Managed Redis® для кэширования и буферизации, что снижает нагрузку на базу данных и ускоряет работу сервиса.
Новый код, использующий Redis, отмечен комментариями с 🔴.

Откройте файл requirements.txt на редактирование и замените содержимое, добавив модули для работы с Managed Redis®.

```bash
nano
requirements.txt
```

Содержимое файла:

```bash
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
redis
==
6.2
.0
aioredis
==
2.0
.1
```

Добавлены новые библиотеки redis и aioredis.

Установите новые зависимости:

```bash
pip
install
-r
requirements.txt
```

Откройте файл .env и обновите содержимое для подключения к Managed Redis® и Managed PostgreSQL®.

```bash
nano
.env
```

Содержимое файла:

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
:5432/short_links
BASE_URL
=
<
IP-адрес
>
.nip.io
REDIS_URL
=
redis://:
<
REDIS_PASSWORD
>
@
<
REDIS_IP
>
:6379
CACHE_TTL
=
3600
SYNC_INTERVAL
=
60
```

Где:

- <PASSWORD> — пароль, который вы задали при создании пользователя базы данных Managed PostgreSQL®.
- <DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL®.
- <IP-адрес> — публичный IP-адрес виртуальной машины.
- <REDIS_IP> — IP-адрес сервиса Managed Redis®.
- <REDIS_PASSWORD> — пароль от кластера Managed Redis®.

<PASSWORD> — пароль, который вы задали при создании пользователя базы данных Managed PostgreSQL®.

<DB_PRIVATE_IP> — IP-адрес сервиса Managed PostgreSQL®.

<IP-адрес> — публичный IP-адрес виртуальной машины.

<REDIS_IP> — IP-адрес сервиса Managed Redis®.

<REDIS_PASSWORD> — пароль от кластера Managed Redis®.

Перезапустите сервис short-links:

```bash
sudo
systemctl daemon-reload
sudo
systemctl restart short-links
```

## 5. Запустите нагрузочный тест с кешированием

Теперь, когда настройка кеширования завершена, проведите повторный тест для сравнения производительности.

1. Запустите нагрузочный тест командой:
k6 run short-links.test.js
2. Дождитесь выполнения теста и проанализируйте результаты.
Пример результата:
█ TOTAL RESULTS
 checks_total.......................: 8690 141.794978/s checks_succeeded...................: 100.00% 8690 out of 8690 checks_failed......................: 0.00% 0 out of 8690
 ✓ create - status 201/200 ✓ create - has short_code ✓ redirect status 302/301
 HTTP http_req_duration.......................................................: avg=24.59ms min=10.53ms med=17.39ms max=3.04s p(90)=23.72ms p(95)=61.7ms { expected_response:true }............................................: avg=24.59ms min=10.53ms med=17.39ms max=3.04s p(90)=23.72ms p(95)=61.7ms http_req_failed.........................................................: 0.00% 0 out of 8295 http_reqs...............................................................: 8295 135.349752/s
 EXECUTION iteration_duration......................................................: avg=1.52s min=1.25s med=1.48s max=5.44s p(90)=1.52s p(95)=1.55s iterations..............................................................: 395 6.445226/s vus.....................................................................: 1 min=1 max=10 vus_max.................................................................: 10 min=10 max=10
 NETWORK data_received...........................................................: 1.8 MB 30 kB/s data_sent...............................................................: 946 kB 15 kB/s
running (1m01.3s), 00/10 VUs, 395 complete and 0 interrupted iterationsshortener_flow ✓ [======================================] 10 VUs 1m0s

Запустите нагрузочный тест командой:

```bash
k6 run short-links.test.js
```

Дождитесь выполнения теста и проанализируйте результаты.
Пример результата:

```bash
█ TOTAL RESULTS
checks_total
..
..
..
..
..
..
..
..
..
..
..
.:
8690
141.794978
/s
checks_succeeded
..
..
..
..
..
..
..
..
..
.:
100.00
%
8690
out of
8690
checks_failed
..
..
..
..
..
..
..
..
..
..
..
:
0.00
%
0
out of
8690
✓ create - status
201
/200
✓ create - has short_code
✓ redirect status
302
/301
HTTP
http_req_duration
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
avg
=
24
.59ms
min
=
10
.53ms
med
=
17
.39ms
max
=
3
.04s p
(
90
)
=
23
.72ms p
(
95
)
=
61
.7ms
{
expected_response:true
}
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
avg
=
24
.59ms
min
=
10
.53ms
med
=
17
.39ms
max
=
3
.04s p
(
90
)
=
23
.72ms p
(
95
)
=
61
.7ms
http_req_failed
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
0.00
%
0
out of
8295
http_reqs
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
8295
135.349752
/s
EXECUTION
iteration_duration
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
avg
=
1
.52s
min
=
1
.25s
med
=
1
.48s
max
=
5
.44s p
(
90
)
=
1
.52s p
(
95
)
=
1
.55s
iterations
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
:
395
6.445226
/s
vus
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
1
min
=
1
max
=
10
vus_max
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
10
min
=
10
max
=
10
NETWORK
data_received
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
1.8
MB
30
kB/s
data_sent
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
..
.:
946
kB
15
kB/s
running
(
1m01.3s
)
, 00/10 VUs,
395
complete and
0
interrupted iterations
shortener_flow ✓
[
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
==
]
10
VUs 1m0s
```

Сравнение с тестом без кеширования показывает значительное улучшение производительности: среднее время отклика сократилось с 370.01 мс до 24.59 мс, а среднее время итерации — с 8.78 с до 1.52 с.

## 6. Удалите виртуальную машину после тестирования

Виртуальная машина k6-load-test использовалась для тестирования и больше не нужна.

[Удалите виртуальную машину k6-load-test](https://cloud.ru/docs/virtual-machines/ug/topics/guides__delete-vm)Удалите виртуальную машину k6-load-test убедившись, что отмечены:

1. Диски.
2. Публичный IP.

Диски.

Публичный IP.

Убедитесь, что в личном кабинете в сервисе «Виртуальные машины» больше не отображается виртуальная машина k6-load-test.

## Результат

Вы настроили кеширование для Web-приложения, выполнили нагрузочные тесты и оценили их результаты.
