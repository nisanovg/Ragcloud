---
title: Вайб-кодинг с помощью Foundation Models и подключение MCP-сервера для деплоя приложения в Container Apps
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server
topic: containers
---
# Вайб-кодинг с помощью Foundation Models и подключение MCP-сервера для деплоя приложения в Container Apps

С помощью этого руководства вы научитесь:

- вайб-кодить бэкенд-приложение на Python (фреймворк Django) с использованием VS Code и Foundation Models;
- создавать фронтенд с помощью готовых промптов к Foundation Models в VS Code;
- подключать кастомный AI-агент для работы с MCP-сервером в VS Code;
- автоматизировать деплой приложения в Container Apps, используя промпты к MCP-серверу.

вайб-кодить бэкенд-приложение на Python (фреймворк Django) с использованием VS Code и Foundation Models;

создавать фронтенд с помощью готовых промптов к Foundation Models в VS Code;

подключать кастомный AI-агент для работы с MCP-сервером в VS Code;

автоматизировать деплой приложения в Container Apps, используя промпты к MCP-серверу.

Вы будете использовать набор готовых промптов для всех шагов создания и деплоя приложения.

На примере этих промптов вы сможете не только с нуля создать работающее приложение и разместить его в [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps, но и полностью автоматизировать процесс обновления и публикации новой версии приложения.

Вы будете использовать следующие сервисы:

- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- Систему контроля версий GitVerse.
- VS Code — редактор кода, который поддерживает множество языков программирования, включая Python, Java, C++, JavaScript и многие другие.
- Roo Code или Kilo Code — плагин для анализа, написания, рефакторинга и отладки кода.
Поддерживает различные API и локальные модели.
Позволяет создавать собственных AI-ассистентов для определенных задач и ролей, переключать режимы и настраивать промпты.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

Систему контроля версий GitVerse.

VS Code — редактор кода, который поддерживает множество языков программирования, включая Python, Java, C++, JavaScript и многие другие.

Roo Code или Kilo Code — плагин для анализа, написания, рефакторинга и отладки кода.
Поддерживает различные API и локальные модели.
Позволяет создавать собственных AI-ассистентов для определенных задач и ролей, переключать режимы и настраивать промпты.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Подготовьте среду.
2. [Подготовьте окружение и создайте приложение для основных настроек Django и для работы с моделями с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Подготовьте окружение и создайте приложение для основных настроек Django и для работы с моделями с помощью промпта.
3. [Создайте модель RecordEntry и зарегистрируйте ее в Django-админке с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте модель RecordEntry и зарегистрируйте ее в Django-админке с помощью промпта.
4. [Создайте пользователя admin с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте пользователя admin с помощью промпта.
5. [Сохраните версии Python-библиотек в requirements и создайте документацию по проекту c помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Сохраните версии Python-библиотек в requirements и создайте документацию по проекту c помощью промпта.
6. [Проверьте работоспособность Django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность Django-приложения.
7. [Создайте фронтенд-приложение с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте фронтенд-приложение с помощью промпта.
8. [Проверьте работоспособность фронтенд-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность фронтенд-приложения.
9. [Заполните админку записями с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Заполните админку записями с помощью промпта.
10. [Создайте Docker-файл с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте Docker-файл с помощью промпта.
11. [Зарегистрируйте MCP-сервер в плагине для передачи промптов в Container Apps и Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Зарегистрируйте MCP-сервер в плагине для передачи промптов в Container Apps и Artifact Registry.
12. [Выполните деплой приложения с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Выполните деплой приложения с помощью промпта.
13. [Проверьте работоспособность приложения в Container Apps](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность приложения в Container Apps.
14. [Создайте бакеты в Object Storage для хранения данных](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте бакеты в Object Storage для хранения данных.
15. [(Опционально) Синхронизируйте файлы из БД с папкой, смонтированной для контейнера, с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)(Опционально) Синхронизируйте файлы из БД с папкой, смонтированной для контейнера, с помощью промпта.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Подготовьте среду.

[Подготовьте окружение и создайте приложение для основных настроек Django и для работы с моделями с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Подготовьте окружение и создайте приложение для основных настроек Django и для работы с моделями с помощью промпта.

[Создайте модель RecordEntry и зарегистрируйте ее в Django-админке с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте модель RecordEntry и зарегистрируйте ее в Django-админке с помощью промпта.

[Создайте пользователя admin с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте пользователя admin с помощью промпта.

[Сохраните версии Python-библиотек в requirements и создайте документацию по проекту c помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Сохраните версии Python-библиотек в requirements и создайте документацию по проекту c помощью промпта.

[Проверьте работоспособность Django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность Django-приложения.

[Создайте фронтенд-приложение с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте фронтенд-приложение с помощью промпта.

[Проверьте работоспособность фронтенд-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность фронтенд-приложения.

[Заполните админку записями с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Заполните админку записями с помощью промпта.

[Создайте Docker-файл с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте Docker-файл с помощью промпта.

[Зарегистрируйте MCP-сервер в плагине для передачи промптов в Container Apps и Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Зарегистрируйте MCP-сервер в плагине для передачи промптов в Container Apps и Artifact Registry.

[Выполните деплой приложения с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Выполните деплой приложения с помощью промпта.

[Проверьте работоспособность приложения в Container Apps](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Проверьте работоспособность приложения в Container Apps.

[Создайте бакеты в Object Storage для хранения данных](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)Создайте бакеты в Object Storage для хранения данных.

[(Опционально) Синхронизируйте файлы из БД с папкой, смонтированной для контейнера, с помощью промпта](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)(Опционально) Синхронизируйте файлы из БД с папкой, смонтированной для контейнера, с помощью промпта.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

1. Убедитесь, что у вас есть доступ к Foundation Models.
2. Убедитесь, что баланс в личном кабинете положительный.
Если он нулевой или отрицательный — [пополните баланс](https://cloud.ru/docs/billing/ug/topics/guides__payment_fl)пополните баланс.
Небольшое количество запросов в Foundation Models будет стоить не больше рубля, подробнее — [в тарифах](https://cloud.ru/documents/tariffs/evolution/foundation-models.html)в тарифах.
3. [Подключите Foundation Models в VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Подключите Foundation Models в VS Code.
Используйте следующие параметры:

При создании сервисного аккаунта выберите роль внутри проекта — «Администратор пользователей» для создания контейнеров Container Apps от лица этого сервисного аккаунта в дальнейшем.
При создании API-ключа укажите в поле Сервисы значение Foundation Models.
В поле Модель в плагине VS Code выберите одну из следующих моделей:

zai-org/GLM-4.6
Qwen/Qwen3-Coder-480B-A35B-Instruct
openai/gpt-oss-120b

Для решения задач этого руководства рекомендуется использовать модель zai-org/GLM-4.6.

Чтобы увидеть полное описание моделей и стоимость токенов:

Перейдите [в личный кабинет](https://cloud.ru/docs/console/ug/topics/guides__auth.html)в личный кабинет.
Перейдите в раздел AI Factory –> Foundation Models.
В разделе Модели найдите описание, параметры и стоимость токенов для нужной модели.

Вы можете использовать бесплатные модели, доступные в режиме Public Preview.

Убедитесь, что у вас есть доступ к Foundation Models.

Убедитесь, что баланс в личном кабинете положительный.
Если он нулевой или отрицательный — [пополните баланс](https://cloud.ru/docs/billing/ug/topics/guides__payment_fl)пополните баланс.
Небольшое количество запросов в Foundation Models будет стоить не больше рубля, подробнее — [в тарифах](https://cloud.ru/documents/tariffs/evolution/foundation-models.html)в тарифах.

[Подключите Foundation Models в VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Подключите Foundation Models в VS Code.

Используйте следующие параметры:

- При создании сервисного аккаунта выберите роль внутри проекта — «Администратор пользователей» для создания контейнеров Container Apps от лица этого сервисного аккаунта в дальнейшем.
- При создании API-ключа укажите в поле Сервисы значение Foundation Models.
- В поле Модель в плагине VS Code выберите одну из следующих моделей:

zai-org/GLM-4.6
Qwen/Qwen3-Coder-480B-A35B-Instruct
openai/gpt-oss-120b

Для решения задач этого руководства рекомендуется использовать модель zai-org/GLM-4.6.

При создании сервисного аккаунта выберите роль внутри проекта — «Администратор пользователей» для создания контейнеров Container Apps от лица этого сервисного аккаунта в дальнейшем.

При создании API-ключа укажите в поле Сервисы значение Foundation Models.

В поле Модель в плагине VS Code выберите одну из следующих моделей:

- zai-org/GLM-4.6
- Qwen/Qwen3-Coder-480B-A35B-Instruct
- openai/gpt-oss-120b

zai-org/GLM-4.6

Qwen/Qwen3-Coder-480B-A35B-Instruct

openai/gpt-oss-120b

Для решения задач этого руководства рекомендуется использовать модель zai-org/GLM-4.6.

Чтобы увидеть полное описание моделей и стоимость токенов:

1. Перейдите [в личный кабинет](https://cloud.ru/docs/console/ug/topics/guides__auth.html)в личный кабинет.
2. Перейдите в раздел AI Factory –> Foundation Models.
3. В разделе Модели найдите описание, параметры и стоимость токенов для нужной модели.

Перейдите [в личный кабинет](https://cloud.ru/docs/console/ug/topics/guides__auth.html)в личный кабинет.

Перейдите в раздел AI Factory –> Foundation Models.

В разделе Модели найдите описание, параметры и стоимость токенов для нужной модели.

Вы можете использовать бесплатные модели, доступные в режиме Public Preview.

## 2. Подготовьте окружение и создайте приложения с помощью промпта

Если вы хотите не писать Django-приложение с нуля, обращаясь к AI-модели с помощью промптов, а попробовать развернуть уже готовое приложение из репозитория GitVerse, [перейдите к практическому руководству по развертыванию django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-django-photo-app)перейдите к практическому руководству по развертыванию django-приложения.

В этом проекте используются:

- Django 5.2.7
- Python 3.13
- База данных SQL Lite

Django 5.2.7

Python 3.13

База данных SQL Lite

Пример с использованием SQLite предназначен исключительно для демонстрационных целей и быстрого запуска приложения.

Для production-среды настоятельно рекомендуется использовать полноценную СУБД, например PostgreSQL — она обеспечит надежность, масштабируемость и поддержку конкурентного доступа.

С помощью промптов создается приложение для добавления рекордов (как в «Книге рекордов Гиннеса»). В приложении должна быть возможность модерировать рекорды (подтверждать добавленную запись) в административной панели. В приложении должны храниться изображения с текстом описания.
Фронтенд приложения должен быть опубликован в сети с фиксированным адресом и заданным дизайном.

Чтобы создать проект и приложения с помощью выбранной модели ИИ, используйте промпт:

```bash
Создай проект под названием «Рекордасьон»
(
по-английски — Recordacion
)
с использованием следующих технологий:
- Django
5.2
.7
- Python
3.13
- База данных: SQLite
Создай новое виртуальное окружение и размести его в папке .venv
Внутри проекта создай два приложения:
- recordacion — для основных настроек Django
(
settings, urls и т.д.
)
создан через startproject
;
- records — для работы с моделями создан через startapp.
Функционал: Любой пользователь может добавить свой рекорд и просматривать рекорды других.
В приложении records создай модель RecordEntry со следующими полями:
- название
- описание
- картинка для preview
- картинки
(
картинок может быть несколько, должна быть связь ManyToMany
)
- поля
"Дата создания"
и
"Дата обновления"
(
должны заполняться автоматически
)
- модель принята администратором или нет, поле is_approved
- связь с тем, кто принял рекорд approved_by на django user
```

В процессе создания приложения AI-модель предлагает использовать стандартные команды фреймворка Django.
AI-модель периодически запрашивает подтверждение действий.

![../_images/kilo_code_working.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/kilo_code_working.png)

После завершения работы AI-модели в папке проекта появляются папки:

- ./recordacion — для хранения основных настроек Django (settings, urls).
- ../records — для хранения модели рекорда.

./recordacion — для хранения основных настроек Django (settings, urls).

../records — для хранения модели рекорда.

Чтобы ускорить работу AI-модели по созданию окружения, рекомендуется добавить все промпты из Шагов 2–5 в виде сплошного текста.

Промпт целиком для создания проекта, окружения, приложения Django, модели и базы данных (Шаги 2–5):

```bash
### Создай проект под названием «Рекордасьон»
(
по-английски — Recordacion
)
с использованием следующих технологий:
- Django
5.2
.7
- Python
3.13
- База данных: SQLite
1
. Создай новое виртуальное окружение и размести его в папке .venv
2
. Внутри проекта создай два приложения:
recordacion — для основных настроек Django
(
settings, urls и т.д.
)
создан через startproject
;
records — для работы с моделями создан через startapp.
Функционал:
Любой пользователь может добавить свой рекорд и просматривать рекорды других.
В приложении records создай модель RecordEntry со следующими полями:
- название
- описание
- картинка для preview
- картинки
(
картинок может быть несколько, должна быть связь ManyToMany
)
- поля дата создания и дата обновления
(
должны заполняться автоматически
)
- модель принята администратором или нет is_approved
- связь с тем кто принял рекорд approved_by на django user
3
. Зарегистрируй модель RecordEntry в админке Django, чтобы можно было управлять записями через интерфейс администратора.
4
. Добавь кастомную Django-команду create_admin_user, которая создаёт суперпользователя с логином admin и паролем admin. Если такой пользователь уже существует — команда должна пропустить создание.
5
. Версии Python библиотек сохрани в requirements.txt.
6
. Создай файл README.md с кратким описанием проекта и пошаговой инструкцией по его запуску
(
включая активацию виртуального окружения, миграции и запуск сервера
)
.
```

При использовании промпта целиком после того, как AI-модель закончит работу, перейдите к [проверке работоспособности Django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)проверке работоспособности Django-приложения.

## 3. Создайте модель RecordEntry и зарегистрируйте ее в Django-админке с помощью промпта

Используйте промпт:

```bash
Зарегистрируй модель RecordEntry в админке Django, чтобы можно было управлять записями через интерфейс администратора.
```

AI-модель добавила в ../records/models.py модель с заданными параметрами.

AI-модель добавила в настройки admin.py новую модель для работы с приложением.
Также AI-модель самостоятельно накатила миграции для работы с Django и создала базу данных db.sqlite3.

## 4. Создайте пользователя admin с помощью промпта

Используйте промпт:

```bash
Добавь кастомную Django-команду create_admin_user, которая создаёт суперпользователя с логином admin и паролем admin.
Если такой пользователь уже существует, команда должна пропустить создание.
```

AI-модель запускает команду create-admin-user.

## 5. Сохраните версии Python-библиотек и создайте документацию по проекту c помощью промпта

В процессе разработки AI-модель самостоятельно загружает недостающие библиотеки Python.

На этом шаге попросите модель сохранить версии скачанных библиотек в отдельном файле requirements.txt.

Используйте промпт:

```bash
Версии Python библиотек сохрани в requirements.txt
```

Попросите модель создать инструкцию по работе с проектом.

Используйте промпт:

```bash
Создай файл README.md с кратким описанием проекта и пошаговой инструкцией по его запуску
(
включая активацию виртуального окружения, миграции и запуск сервера
)
.
```

AI-модель создает файлы requirements.txt и README.md в корне проекта.

## 6. Проверьте работоспособность Django-приложения

Для запуска и проверки работоспособности приложения воспользуйтесь автоматически созданной инструкцией в файле README.md в корне проекта.

1. Запустите сервер с помощью команды:
python manage.py runserver
2. Используйте адрес 127.0.0.1:8000/admin для проверки работоспособности приложения.
Отобразится окно входа в панель администратора.

Запустите сервер с помощью команды:

```bash
python manage
.
py runserver
```

Используйте адрес 127.0.0.1:8000/admin для проверки работоспособности приложения.

Отобразится окно входа в панель администратора.

![../_images/loginpage.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/loginpage.png)

## 7. Создайте фронтенд-приложение с помощью промпта

Создайте фронтенд-приложение с заданным дизайном для просмотра добавленных рекордов, добавления рекордов и просмотра отдельного рекорда.

Используйте новое контекстное окно модели.

Используйте промпт:

```bash
### Реализуй три страницы в records.views
1
. Главная страница
Маршрут: GET /
Отображает только одобренные
(
is_approved
=
True
)
пользовательские рекорды.
Рекорды упорядочены по возрастанию даты создания — самый новый должен находиться в начале списка.
Для каждого рекорда показывай:
- Название
- Картинку из Preview
(
если есть
)
- Дату создания
Рекорды отображай по
3
на одной строчке.
Добавь фильтр:
- по названию
- выбор сортировки по дате
- добавь пагинацию по
10
рекордов
- кнопку сброса фильтрафии
2
. Страница добавления рекорда
Маршрут: GET /records и POST /records
Форма для создания нового RecordEntry с полями:
- Название
- Описание
- Картинка для preview
- Несколько картинок для поста
После успешной отправки формы отобрази сообщение:
«Ваш рекорд успешно добавлен и будет рассмотрен администратором в ближайшее время.»
Не перенаправляй пользователя — просто покажи это сообщение на той же странице.
3
. Страница отдельного рекорда
Маршрут: GET /records/
<
record_id
>
Отображает все данные конкретного рекорда:
- Название
- Описание
- Все прикрепленные изображения
(
без изображения с preview
)
- Дату создания
Требования к оформлению всех страниц:
Используй наследование шаблонов
(
base.html → дочерние шаблоны
)
.
Все стили должны находиться в одном CSS-файле
(
например, static/css/style.css
)
.
Используй формулу цветов:
60
% основной цвет,
30
% акцентный цвет,
10
% яркий цвет
Цветовая палитра:
Основной акцент - персик/терракота
#FFF9F5
Фон - очень светлый кремовый
#4B3F72
Текст - мягкий тёмно-фиолетовый
#FF6F61
Дополнительно
(
для UI-состояний
)
:
Hover на кнопке:
#FF5C4D (чуть темнее акцента)
Disabled-состояние:
#E0D9D0 (светло-бежевый, на фоне кремового)
Тени / разделители: rgba
(
75
,
63
,
114
,
0.1
)
— полупрозрачный оттенок основного текстового цвета
Кнопки должны быть одинаковыми по высоте.
Стиль должен быть чистым, современным и напоминать немного сайт Книги рекордов Гиннеса.
```

AI-модель самостоятельно находит модель данных в проекте и создает HTML-страницы.

AI-модель периодически запрашивает подтверждение действий. Модель самостоятельно тестирует полученный код и решает проблемы, например, отсутствие таблицы стилей CSS.

Записи добавлены в файл ../records/views.py.

## 8. Проверьте работоспособность фронтенд-приложения

1. Используйте адрес localhost:8000 для проверки работоспособности приложения.
Отобразится домашняя страница со строкой поиска рекордов и кнопкой Добавить рекорд.
2. Добавьте запись о рекорде через сайт.
3. Перейдите по адресу 127.0.0.1:8000/admin, войдите с логином и паролем admin/admin и подтвердите добавленную запись.
4. Проверьте по адресу localhost:8000, что запись отобразилась в списке рекордов.

Используйте адрес localhost:8000 для проверки работоспособности приложения.
Отобразится домашняя страница со строкой поиска рекордов и кнопкой Добавить рекорд.

Добавьте запись о рекорде через сайт.

Перейдите по адресу 127.0.0.1:8000/admin, войдите с логином и паролем admin/admin и подтвердите добавленную запись.

![../_images/adminpanelconfirm.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/adminpanelconfirm.png)

Проверьте по адресу localhost:8000, что запись отобразилась в списке рекордов.

## 9. Заполните админку записями с помощью промпта

1. Скопируйте в репозиторий с проектом [папку init-data](https://gitverse.ru/nicking/django-app-recordacion/content/main/prompts/init-data)папку init-data.
Используйте новое контекстное окно модели.
2. Используйте промпт:
Заполни рекорды (EntryRecords)
Создай django manage.py команду fill_records, которая добавит первые записи Используя данные из prompts/init-data/data.jsonЕсли рекорд с таким именем уже существует, его можно пропустить.
3. Запустите итоговую команду.
4. Откройте адрес localhost:8000 и проверьте, что рекорды отображаются.
5. При ошибках, например, если не отображаются изображения, в том же контекстном окне AI-модель введите промпт:
Не работает отображение картинок, поправь
6. После отработки команды повторно откройте адрес localhost:8000 и проверьте, что рекорды отображаются корректно.

Скопируйте в репозиторий с проектом [папку init-data](https://gitverse.ru/nicking/django-app-recordacion/content/main/prompts/init-data)папку init-data.
Используйте новое контекстное окно модели.

Используйте промпт:

```bash
Заполни рекорды
(
EntryRecords
)
Создай django manage.py команду fill_records, которая добавит первые записи Используя данные из prompts/init-data/data.json
Если рекорд с таким именем уже существует, его можно пропустить.
```

Запустите итоговую команду.

Откройте адрес localhost:8000 и проверьте, что рекорды отображаются.

![../_images/frontendpage.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/frontendpage.png)

При ошибках, например, если не отображаются изображения, в том же контекстном окне AI-модель введите промпт:

```bash
Не работает отображение картинок, поправь
```

После отработки команды повторно откройте адрес localhost:8000 и проверьте, что рекорды отображаются корректно.

## 10. Создайте Docker-файл с приложением с помощью промпта

В промпте предусмотрены параметры для деплоя проекта в Container Apps, в том числе:

- .dockerignore — чтобы исключить из сборки статичные папки для хранения данных.
- Переменные окружения: ALLOWED_HOSTS, CONTAINER_APP_NAME (заполняется сервисом Container Apps), CSRF_TRUSTED_ORIGINS (необходимо для отправки формы).
- FILE_UPLOAD_PERMISSIONS — настройка, необходимая для подключения в дальнейшем Object Storage.
- Непривилегированный пользователь с UID 1000 для работы в непривилегированном режиме. По умолчанию контейнеры в Container Apps запускаются от имени пользователя с идентификатором (UID) 1000.
- Точка входа, в которой указаны команды при запуске контейнера.

.dockerignore — чтобы исключить из сборки статичные папки для хранения данных.

Переменные окружения: ALLOWED_HOSTS, CONTAINER_APP_NAME (заполняется сервисом Container Apps), CSRF_TRUSTED_ORIGINS (необходимо для отправки формы).

FILE_UPLOAD_PERMISSIONS — настройка, необходимая для подключения в дальнейшем Object Storage.

Непривилегированный пользователь с UID 1000 для работы в непривилегированном режиме. По умолчанию контейнеры в Container Apps запускаются от имени пользователя с идентификатором (UID) 1000.

Точка входа, в которой указаны команды при запуске контейнера.

Используйте промпт:

```bash
### Создай Docker-образ
на основе официального образа python:3.13.9-bookworm
(
Debian Bookworm
)
со следующими требованиями:
1
. Зависимости и игнорирование файлов
Добавь файл requirements.txt с необходимыми Python-зависимостями
(
включая Django
5.2
.7
)
.
Создай файл .dockerignore и исключи из сборки:
``
`
db/
media/
staticfiles/
.venv/
`
`
`
2
. Расположение базы данных
Настрой проект так, чтобы файл SQLite
(
db.sqlite3
)
сохранялся в папке ./db
(
в корне проекта
)
.
Обнови settings.py, указав путь к базе данных:
DATABASES
=
{
'default'
:
{
'ENGINE'
:
'django.db.backends.sqlite3'
,
'NAME'
:
BASE_DIR /
'db'
/
'db.sqlite3'
,
}
}
3
. Настройки для запуска в Cloud.ru Container Apps
Добавь в settings.py следующие параметры:
`
`
`
python
import
os
CONTAINER_APP_NAME
=
os.environ.get
(
"CONTAINER_NAME"
,
"-"
)
# будет установлен средой Cloud.ru Container Apps
ALLOWED_HOSTS
=
[
f
'{CONTAINER_APP_NAME}.containerapps.ru'
,
f
'{CONTAINER_APP_NAME}.internal.containers.cloud.ru'
,
'localhost'
,
'127.0.0.1'
,
]
CSRF_TRUSTED_ORIGINS
=
[
f
'https://{CONTAINER_APP_NAME}.containerapps.ru'
,
f
'https://{CONTAINER_APP_NAME}.internal.containers.cloud.ru'
,
]
# Django пытается изменить права доступа к загруженным файлам — отключаем это поведение
FILE_UPLOAD_PERMISSIONS
=
None
`
``
4
. Пользователь и права доступа
В Dockerfile создай непривилегированного пользователя с
UID
1000
.
Предоставь этому пользователю права на запись в папки:
./db
(
для базы данных
)
./media
(
для загружаемых изображений
)
5
. В Dockerfile добавь
RUN python manage.py collectstatic
--noinput
ENTRYPOINT entrypoint.sh
в котором:
- запусти миграции
- запусти django команду для создания admin пользователя create_admin_user
- запусти django команду fill_records
CMD добавь запуск runserver
6
. Добавь в Readme.md способ запуска приложения через Docker
```

В корне проекта создан образ Dockerfile.

На следующих шагах добавьте в плагин MCP-сервер и задеплойте приложение с помощью промптов.

## 11. Зарегистрируйте в плагине MCP-сервер для передачи промптов в Container Apps и Artifact Registry

Используйте кастомный AI-агент для взаимодействия с MCP-сервером.

MCP-сервер работает совместно с VSCode-плагинами, например Kilo Code, Roo Code, Claude, и использует MCP-протокол для обращения к внешним системам (Container Apps и Artifact Registry).

1. Перед началом работы с AI-агентом для взаимодействия с MCP-сервером установите последнюю версию Golang [с официального сайта](https://go.dev/doc/install)с официального сайта.
2. Выполните команду по установке AI-агента по работе с MCP-сервером:
go install github.com/Nick1994209/cloudru-containerapps-mcp/cmd/cloudru-containerapps-mcp@latest
3. Перейдите в сервисный аккаунт, созданный на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)подготовки среды.
4. Перейдите в раздел Ключи доступа.
5. Нажмите Создать ключ.
6. Скопируйте в надежное место KeyID (логин) и Key Secret (пароль).
7. Скопируйте значения KeyID (логин) и Key Secret (пароль), а также project ID своего проекта в json-файл.
Вы можете узнать projectId своего проекта, открыв cloud.console.ru:
https://console.cloud.ru/spa/svp?customerId=&projectId=<***********>

Используйте следующий JSON-файл, дополнив своими значениями:
{ "mcpServers": { "cloudru-containerapps-mcp": { "command": "cloudru-containerapps-mcp", "args": [], "env": { "CLOUDRU_KEY_ID": "********", "CLOUDRU_KEY_SECRET": "********", "CLOUDRU_PROJECT_ID": "********", }, "alwaysAllow": [ "cloudru_containerapps_description", "cloudru_get_containerapp", "cloudru_get_list_containerapps", "cloudru_start_containerapp", "cloudru_get_list_docker_registries" ], "timeout": 900, "disabledTools": [] } }}
8. В плагине, который вы добавили в VS Code на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)подготовки среды, перейдите в раздел MCP Servers и добавьте json-файл по кнопке Edit Global MCP.

В разделе MCP Servers отобразится добавленный MCP-агент и набор команд.
9. Запустите AI-агент:
cloudru-containerapps-mcp

Перед началом работы с AI-агентом для взаимодействия с MCP-сервером установите последнюю версию Golang [с официального сайта](https://go.dev/doc/install)с официального сайта.

Выполните команду по установке AI-агента по работе с MCP-сервером:

```bash
go
install
github.com/Nick1994209/cloudru-containerapps-mcp/cmd/cloudru-containerapps-mcp@latest
```

Перейдите в сервисный аккаунт, созданный на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)подготовки среды.

Перейдите в раздел Ключи доступа.

Нажмите Создать ключ.

Скопируйте в надежное место KeyID (логин) и Key Secret (пароль).

Скопируйте значения KeyID (логин) и Key Secret (пароль), а также project ID своего проекта в json-файл.

Вы можете узнать projectId своего проекта, открыв cloud.console.ru:

```bash
https://console.cloud.ru/spa/svp?customerId
=
&
projectId
=
<
***********
>
```

Используйте следующий JSON-файл, дополнив своими значениями:

```bash
{
"mcpServers"
:
{
"cloudru-containerapps-mcp"
:
{
"command"
:
"cloudru-containerapps-mcp"
,
"args"
:
[
]
,
"env"
:
{
"CLOUDRU_KEY_ID"
:
"********"
,
"CLOUDRU_KEY_SECRET"
:
"********"
,
"CLOUDRU_PROJECT_ID"
:
"********"
,
}
,
"alwaysAllow"
:
[
"cloudru_containerapps_description"
,
"cloudru_get_containerapp"
,
"cloudru_get_list_containerapps"
,
"cloudru_start_containerapp"
,
"cloudru_get_list_docker_registries"
]
,
"timeout"
:
900
,
"disabledTools"
:
[
]
}
}
}
```

В плагине, который вы добавили в VS Code на этапе [подготовки среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__vibecode-django-photo-app-mcp-server)подготовки среды, перейдите в раздел MCP Servers и добавьте json-файл по кнопке Edit Global MCP.

![../_images/edit-kilocode-mcp-servers.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/edit-kilocode-mcp-servers.png)

В разделе MCP Servers отобразится добавленный MCP-агент и набор команд.

Запустите AI-агент:

```bash
cloudru-containerapps-mcp
```

## 12. Выполните деплой приложения с помощью промпта

На этом шаге выполняется создание реестра в Artifact Registry, сборка и отправка в созданный реестр Docker-образа приложения и создание контейнерного приложения в Container Apps на основе Docker-образа.

MCP-сервер обращается к [Public API](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/api-ref)Public API Artifact Registry и [Public API](https://cloud.ru/docs/container-apps-evolution/ug/topics/api-ref)Public API Container Apps для выполнения команд.

1. Последовательно выполните промпты, заменив название реестра на свое значение:
### Деплой приложения в Cloud.ru Evolution Container Apps
Выполни MCP команду и создай в Cloud.ru реестр, где будет храниться Docker image с приложением recordacionреестр называется = <ваше_название_реестра>

Сделай docker build and push в Cloud.ru Artifact Registry используяназвание реестра = <ваше_название_реестра>название репозитория = recordacionназвание тэга = v0.0.1

Убедитесь, что в личном кабинете в [сервисе Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/quickstart)сервисе Artifact Registry отображается реестр с указанным именем и в нем содержится репозиторий recordacion.
2. Выполните промпт для создания контейнерного приложения:
Создай ContainerApps используяназвание контейнер аппа = recordacionдокер образ возьми из предыдущего шагавключи автодеплой, тэг паттерн "*"установи время простоя в 30 минутвключи автодеплой, тэг паттерн "*"cpu = 0.5

Если название recordacion уже занято, укажите ваше название.
Убедитесь, что в личном кабинете в [сервисе Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/topics/quickstart)сервисе Container Apps отображается контейнерное приложение <ваше_название_контейнерного_приложения> и статус ревизии изменился на «Выполняется».
3. Не меняя контекстное окно, используйте промпт:
Получи публичный адрес приложения

Получи логи приложения

Если команда не вернула логи или публичный URL-адрес приложения, попробуйте ещё раз спустя 10–15 секунд.
Так как включена опция Автоматическое развертывание, при каждой загрузке в Artifact Registry новой версии образа (например, с помощью промпта) на стороне Container Apps будет автоматически создаваться новая ревизия контейнера на базе обновленной версии образа.

Последовательно выполните промпты, заменив название реестра на свое значение:

```bash
### Деплой приложения в Cloud.ru Evolution Container Apps
Выполни MCP команду и создай в Cloud.ru реестр, где будет храниться Docker image с приложением recordacion
реестр называется
=
<
ваше_название_реестра
>
```

```bash
Сделай
docker
build and push в Cloud.ru Artifact Registry используя
название реестра
=
<
ваше_название_реестра
>
название репозитория
=
recordacion
название тэга
=
v0.0.1
```

Убедитесь, что в личном кабинете в [сервисе Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/topics/quickstart)сервисе Artifact Registry отображается реестр с указанным именем и в нем содержится репозиторий recordacion.

Выполните промпт для создания контейнерного приложения:

```bash
Создай ContainerApps используя
название контейнер аппа
=
recordacion
докер образ возьми из предыдущего шага
включи автодеплой, тэг паттерн
"*"
установи время простоя в
30
минут
включи автодеплой, тэг паттерн
"*"
cpu
=
0.5
```

Если название recordacion уже занято, укажите ваше название.

Убедитесь, что в личном кабинете в [сервисе Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/topics/quickstart)сервисе Container Apps отображается контейнерное приложение <ваше_название_контейнерного_приложения> и статус ревизии изменился на «Выполняется».

Не меняя контекстное окно, используйте промпт:

```bash
Получи публичный адрес приложения
```

```bash
Получи логи приложения
```

Если команда не вернула логи или публичный URL-адрес приложения, попробуйте ещё раз спустя 10–15 секунд.

Так как включена опция Автоматическое развертывание, при каждой загрузке в Artifact Registry новой версии образа (например, с помощью промпта) на стороне Container Apps будет автоматически создаваться новая ревизия контейнера на базе обновленной версии образа.

## 13. Проверьте работоспособность приложения в Container Apps

Вставьте публичный адрес контейнерного приложения в адресную строку браузера.

Откроется страница приложения.

![../_images/frontendpage.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/frontendpage.png)

Ваше приложение запущено и работает. Но оно может потерять недавно добавленные рекорды при развертывании новой версии приложения или при масштабировании до нуля.

На следующем шаге подключите постоянное хранилище для базы данных и медиафайлов.

## 14. Создайте бакеты в Object Storage для хранения данных

1. Создайте бакеты в Object Storage, как описано в Шаге 7 [практического руководства по развертыванию django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-django-photo-app)практического руководства по развертыванию django-приложения.
Используйте следующие пути для монтирования

/app/db — для тома базы данных;
/app/media — для тома загружаемых изображений.
2. Примонтируйте созданные бакеты, как указано в Шаге 8 [практического руководства по развертыванию django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-django-photo-app)практического руководства по развертыванию django-приложения.

Теперь при каждом новом деплое Django-приложения данные не будут теряться, сохраняясь в постоянных томах Object Storage.

Создайте бакеты в Object Storage, как описано в Шаге 7 [практического руководства по развертыванию django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-django-photo-app)практического руководства по развертыванию django-приложения.

Используйте следующие пути для монтирования

- /app/db — для тома базы данных;
- /app/media — для тома загружаемых изображений.

/app/db — для тома базы данных;

/app/media — для тома загружаемых изображений.

![../_images/objectstorage_volumes.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/objectstorage_volumes.png)

Примонтируйте созданные бакеты, как указано в Шаге 8 [практического руководства по развертыванию django-приложения](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__deploy-django-photo-app)практического руководства по развертыванию django-приложения.

Теперь при каждом новом деплое Django-приложения данные не будут теряться, сохраняясь в постоянных томах Object Storage.

Монтирование папки с базой данных SQLite уместно только в демонстрационных или тестовых целях. Если вы не планируете в ближайшее время переходить на другую СУБД и ожидаете, что у вашего приложения будет много пользователей, рекомендуется выполнить следующий шаг.

## 15. (Опционально) Синхронизируйте файлы из БД с папкой, смонтированной для контейнера, с помощью промпта

Если вы планируете продолжать использовать SQL Lite, с помощью этого скрипта синхронизируйте файлы базы данных SQL Lite с папкой, примонтированной для контейнера Object Storage.

При запуске приложения этот скрипт будет скачивать БД из смонтированной папки во временную, а затем синхронизировать содержимое временной БД с постоянной примонтированной.

1. Используйте промпт:
### Добавь синхронизацию db файлов из одной папки в другую
1. добавь скрипт background-sync-folders.sh```bash#!/bin/bash
# === Проверка аргументов ===if [ "$#" -ne 2 ]; then echo "Передан только 1 или меньше аргументов, скрипт не будет синхронизировать данные" echo "Использование: $0 <SOURCE_DIR> <TARGET_DIR>" exit 0fi
SOURCE_DIR="$1"TARGET_DIR="$2"
# === Вспомогательная функция: есть ли обычные файлы в директории? ===has_files() { local dir="$1" [ -d "$dir" ] || return 1 for f in "$dir"/*; do [ -e "$f" ] && [ -f "$f" ] && return 0 done return 1}
# === Функция однократной синхронизации: SOURCE → TARGET ===sync_once() { local src="$1" local tgt="$2" for f in "$src"/*; do [ -e "$f" ] || continue if [ -f "$f" ]; then cp "$f" "$tgt/" fi done}
# === Инициализация ===mkdir -p "$SOURCE_DIR" "$TARGET_DIR"
if ! has_files "$SOURCE_DIR"; then if has_files "$TARGET_DIR"; then echo "SOURCE_DIR=$SOURCE_DIR пуста — копирую из TARGET_DIR=$TARGET_DIR..." sync_once "$TARGET_DIR" "$SOURCE_DIR" echo "Данные в SOURCE_DIR=$SOURCE_DIR восстановлены." else echo "Обе директории пусты." fielse echo "SOURCE_DIR=$SOURCE_DIR содержит данные — используем как источник."fi
# === Запуск бесконечной синхронизации в фоне ===( while true; do sync_once "$SOURCE_DIR" "$TARGET_DIR" sleep 5 done) &
echo "Скрипт завершил инициализацию. Синхронизация запущена в фоновом режиме: файлы копируются каждые 5 секунд из SOURCE_DIR=$SOURCE_DIR в TARGET_DIR=$TARGET_DIR."```Добавьте этот скрипт в ./entrypoint.sh и запустите его до выполнения миграций: `./entrypoint.sh /app/db "$MOUNTED_DB_FOLDER"`
Также включите в ./entrypoint.sh проверку: если директория /app/db/ пуста или не содержит файлов, автоматически выполните следующие Django-команды:- migrate- create_admin_user- fill_records
После создания скрипта background-sync-folders.sh и правок в ./entrypoint.shВыполни docker build and push в Cloud.ru Artifact Registry используяназвание реестра = <ваше_название_реестра>название репозитория = recordacionназвание тэга = v0.0.2

Где <ваше_название_реестра> — название реестра, заданное на Шаге 12.
2. [Создайте новую ревизию контейнера](https://cloud.ru/docs/container-apps-evolution/ug/topics/guides__revision-create)Создайте новую ревизию контейнера, изменив следующие параметры:

добавьте переменную MOUNTED_DB_FOLDER=/synced/db;

в подключенном бакете замените путь до бакета с базой данных с /app/db на /synced/db.

Используйте промпт:

```bash
### Добавь синхронизацию db файлов из одной папки в другую
1
. добавь скрипт background-sync-folders.sh
``
`
bash
#!/bin/bash
# === Проверка аргументов ===
if
[
"
$#
"
-ne
2
]
;
then
echo
"Передан только 1 или меньше аргументов, скрипт не будет синхронизировать данные"
echo
"Использование:
$0
<SOURCE_DIR> <TARGET_DIR>"
exit
0
fi
SOURCE_DIR
=
"
$1
"
TARGET_DIR
=
"
$2
"
# === Вспомогательная функция: есть ли обычные файлы в директории? ===
has_files
(
)
{
local
dir
=
"
$1
"
[
-d
"
$dir
"
]
||
return
1
for
f
in
"
$dir
"
/*
;
do
[
-e
"
$f
"
]
&&
[
-f
"
$f
"
]
&&
return
0
done
return
1
}
# === Функция однократной синхронизации: SOURCE → TARGET ===
sync_once
(
)
{
local
src
=
"
$1
"
local
tgt
=
"
$2
"
for
f
in
"
$src
"
/*
;
do
[
-e
"
$f
"
]
||
continue
if
[
-f
"
$f
"
]
;
then
cp
"
$f
"
"
$tgt
/"
fi
done
}
# === Инициализация ===
mkdir
-p
"
$SOURCE_DIR
"
"
$TARGET_DIR
"
if
!
has_files
"
$SOURCE_DIR
"
;
then
if
has_files
"
$TARGET_DIR
"
;
then
echo
"SOURCE_DIR=
$SOURCE_DIR
пуста — копирую из TARGET_DIR=
$TARGET_DIR
..."
sync_once
"
$TARGET_DIR
"
"
$SOURCE_DIR
"
echo
"Данные в SOURCE_DIR=
$SOURCE_DIR
восстановлены."
else
echo
"Обе директории пусты."
fi
else
echo
"SOURCE_DIR=
$SOURCE_DIR
содержит данные — используем как источник."
fi
# === Запуск бесконечной синхронизации в фоне ===
(
while
true
;
do
sync_once
"
$SOURCE_DIR
"
"
$TARGET_DIR
"
sleep
5
done
)
&
echo
"Скрипт завершил инициализацию. Синхронизация запущена в фоновом режиме: файлы копируются каждые 5 секунд из SOURCE_DIR=
$SOURCE_DIR
в TARGET_DIR=
$TARGET_DIR
."
`
`
`
Добавьте этот скрипт в ./entrypoint.sh и запустите его до выполнения миграций:
`
./entrypoint.sh /app/db
"
$MOUNTED_DB_FOLDER
"
`
Также включите в ./entrypoint.sh проверку: если директория /app/db/ пуста или не содержит файлов, автоматически выполните следующие Django-команды:
- migrate
- create_admin_user
- fill_records
После создания скрипта background-sync-folders.sh и правок в ./entrypoint.sh
Выполни
docker
build and push в Cloud.ru Artifact Registry используя
название реестра
=
<
ваше_название_реестра
>
название репозитория
=
recordacion
название тэга
=
v0.0.2
```

Где <ваше_название_реестра> — название реестра, заданное на Шаге 12.

[Создайте новую ревизию контейнера](https://cloud.ru/docs/container-apps-evolution/ug/topics/guides__revision-create)Создайте новую ревизию контейнера, изменив следующие параметры:

- добавьте переменную MOUNTED_DB_FOLDER=/synced/db;
- в подключенном бакете замените путь до бакета с базой данных с /app/db на /synced/db.

добавьте переменную MOUNTED_DB_FOLDER=/synced/db;

![../_images/envvariablenew.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/envvariablenew.png)

в подключенном бакете замените путь до бакета с базой данных с /app/db на /synced/db.

![../_images/newsynceddb.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/newsynceddb.png)

## Результат

Вы научились:

- подключать Foundation Models в VS Code;
- вайб-кодить Django-приложение для публикации фотографий с помощью промптов к Foundation Models;
- использовать Foundation Models для отладки и тестирования приложений в VS Code;
- подключать MCP-сервер для автоматизации сборки и публикации Docker-образа приложения в Artifact Registry
- с помощью AI-агента обращаться к MCP-серверу, чтобы деплоить контейнерное приложение в Container Apps одной командой;
- добавлять постоянный том Object Storage, который позволяет сохранить ваши данные, когда запросы к приложению не поступают;
- синхронизировать временную базу данных с томом Object Storage при работе контейнерного приложения.

подключать Foundation Models в VS Code;

вайб-кодить Django-приложение для публикации фотографий с помощью промптов к Foundation Models;

использовать Foundation Models для отладки и тестирования приложений в VS Code;

подключать MCP-сервер для автоматизации сборки и публикации Docker-образа приложения в Artifact Registry

с помощью AI-агента обращаться к MCP-серверу, чтобы деплоить контейнерное приложение в Container Apps одной командой;

добавлять постоянный том Object Storage, который позволяет сохранить ваши данные, когда запросы к приложению не поступают;

синхронизировать временную базу данных с томом Object Storage при работе контейнерного приложения.

[Смотрите обучающее видео](https://my.mts-link.ru/Cloud/4455298467/record-new/4353923738)Смотрите обучающее видео по вайб-кодингу с помощью Foundation Models и деплою приложения в Container Apps и узнайте о том, как автоматизировать деплой приложения с помощью MCP-сервера.
