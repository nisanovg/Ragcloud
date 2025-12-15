---
title: Создание бота для суммаризации чатов и каналов в Telegram на LangChain и Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot
topic: ai-factory
---
# Создание бота для суммаризации чатов и каналов в Telegram на LangChain и Foundation Models

С помощью этого руководства вы познакомитесь с проектом evo-foundation-models-tg-bot-lab — Telegram-ботом, который демонстрирует, как интегрировать языковую модель при помощи фреймворка LangChain и сервиса Foundation Models.
Бот автоматически логирует сообщения чатов и выполняет интеллектуальный анализ: составляет краткие изложения диалогов и извлекает из них задачи.

Вы будете использовать следующие сервисы:

- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.
- [Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Docker](https://docs.docker.com/)Docker — система контейнеризации.
- [Telegram](https://web.telegram.org/)Telegram — чат-платформа.
- [LangChain](https://www.langchain.com/)LangChain — фреймворк для создания AI-ориентированных приложений.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Artifact Registry](https://cloud.ru/docs/artifact-registry-evolution/ug/index)Artifact Registry для хранения, совместного использования и управления Docker-образами и Helm-чартами.

[Container Apps](https://cloud.ru/docs/container-apps-evolution/ug/index)Container Apps — сервис для запуска контейнерных приложений в облаке. Не требует знания Kubernetes и создания виртуальных машин.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Docker](https://docs.docker.com/)Docker — система контейнеризации.

[Telegram](https://web.telegram.org/)Telegram — чат-платформа.

[LangChain](https://www.langchain.com/)LangChain — фреймворк для создания AI-ориентированных приложений.

Шаги:

1. [Клонируйте или скачайте репозиторий кода с GitHub](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Клонируйте или скачайте репозиторий кода с GitHub.
2. [Ознакомьтесь с архитектурой кода и интеграции с AI-моделями](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Ознакомьтесь с архитектурой кода и интеграции с AI-моделями.
3. [Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Соберите образ и присвойте тег.
4. [Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Загрузите Docker-образ в реестр.
5. [Зарегистрируйте Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Зарегистрируйте Telegram-бота.
6. [Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Сгенерируйте API-ключ для доступа к Foundation Models.
7. [Создайте и запустите контейнер с чат-ботом](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Создайте и запустите контейнер с чат-ботом.
8. [Создайте Object Storage и ключи доступа](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Создайте Object Storage и ключи доступа.
9. [Проверьте работоспособность развернутого чат-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Проверьте работоспособность развернутого чат-бота.

[Клонируйте или скачайте репозиторий кода с GitHub](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Клонируйте или скачайте репозиторий кода с GitHub.

[Ознакомьтесь с архитектурой кода и интеграции с AI-моделями](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Ознакомьтесь с архитектурой кода и интеграции с AI-моделями.

[Соберите образ и присвойте тег](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Соберите образ и присвойте тег.

[Загрузите Docker-образ в реестр](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Загрузите Docker-образ в реестр.

[Зарегистрируйте Telegram-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Зарегистрируйте Telegram-бота.

[Сгенерируйте API-ключ для доступа к Foundation Models](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Сгенерируйте API-ключ для доступа к Foundation Models.

[Создайте и запустите контейнер с чат-ботом](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Создайте и запустите контейнер с чат-ботом.

[Создайте Object Storage и ключи доступа](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Создайте Object Storage и ключи доступа.

[Проверьте работоспособность развернутого чат-бота](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)Проверьте работоспособность развернутого чат-бота.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Подготовьте среду Container Apps и Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду Container Apps и Artifact Registry, если не сделали этого ранее.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Подготовьте среду Container Apps и Artifact Registry](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)Подготовьте среду Container Apps и Artifact Registry, если не сделали этого ранее.

## 1. Клонируйте или скачайте репозиторий кода с GitHub

Клонируйте или скачайте код [из репозитория](https://github.com/cloud-ru/evo-foundation-models-tg-bot-lab)из репозитория.

```bash
git
clone https://github.com/cloud-ru/evo-foundation-models-tg-bot-lab.git
```

## 2. Ознакомьтесь с архитектурой кода и интеграции с AI-моделями

### Архитектура интеграции

Проект использует модульную архитектуру с четким разделением ответственности:

```bash
chat_bot/
├── assistant.py
# Main class for working with AI
├── models/
# Pydantic models for type hinting
│ ├── ai_config.py
# AI configuration
│ ├── summary_response.py
│ ├── task_extraction_response.py
│ └── task.py
├── prompts/
# Prompt templates
│ ├── summary.txt
│ └── task_extraction.txt
└── formatter.py
# Message formatting
```

```bash
# chat_bot/models/ai_config.py
from
pydantic
import
BaseModel
,
Field
,
validator
class
AIConfig
(
BaseModel
)
:
"""Model for AI configuration."""
api_key
:
str
=
Field
(
.
.
.
,
description
=
"AI API key"
)
model
:
str
=
Field
(
"t-tech/T-pro-it-2.0"
,
description
=
"AI model name"
)
base_url
:
Optional
[
str
]
=
Field
(
None
,
description
=
"Custom AI base URL"
)
temperature
:
float
=
Field
(
0.3
,
ge
=
0.0
,
le
=
2.0
,
description
=
"Generation temperature"
)
max_tokens
:
int
=
Field
(
500
,
gt
=
0
,
description
=
"Maximum tokens for generation"
)
@classmethod
@validator
(
"api_key"
)
def
validate_api_key
(
cls
,
v
:
str
)
-
>
str
:
"""Validate that API key is not empty."""
if
not
v
or
not
v
.
strip
(
)
:
raise
ValueError
(
"api_key cannot be empty"
)
return
v
.
strip
(
)
```

```bash
# chat_bot/assistant.py
from
langchain_openai
import
ChatOpenAI
from
pydantic
import
SecretStr
def
_init_llm
(
self
)
-
>
None
:
"""Initialize the language model."""
try
:
# Initialize with required parameters
self
.
llm
=
ChatOpenAI
(
api_key
=
SecretStr
(
self
.
config
.
api_key
)
,
model
=
self
.
config
.
model
,
temperature
=
self
.
config
.
temperature
,
base_url
=
self
.
config
.
base_url
,
)
logger
.
info
(
f"Initialized AI model:
{
self
.
config
.
model
}
"
f"(temp:
{
self
.
config
.
temperature
}
, max_tokens:
{
self
.
config
.
max_tokens
}
)"
)
except
Exception
as
e
:
logger
.
error
(
f"Failed to initialize AI model:
{
e
}
"
)
raise
```

Ключевые особенности:

- Использование SecretStr для безопасного хранения API-ключа.
- Валидация конфигурации через Pydantic.
- Поддержка кастомных базовых URL для различных AI-провайдеров.
- Настраиваемые параметры генерации (temperature, max_tokens).

Использование SecretStr для безопасного хранения API-ключа.

Валидация конфигурации через Pydantic.

Поддержка кастомных базовых URL для различных AI-провайдеров.

Настраиваемые параметры генерации (temperature, max_tokens).

```bash
def
_load_prompts
(
self
)
-
>
None
:
"""Load prompt templates from files."""
try
:
prompts_dir
=
Path
(
__file__
)
.
parent
/
"prompts"
summary_prompt_file
=
prompts_dir
/
"summary.txt"
task_extraction_prompt_file
=
prompts_dir
/
"task_extraction.txt"
# Load summary prompt
if
summary_prompt_file
.
exists
(
)
:
with
open
(
summary_prompt_file
,
"r"
,
encoding
=
"utf-8"
)
as
f
:
summary_template
=
f
.
read
(
)
self
.
summary_prompt
=
ChatPromptTemplate
.
from_template
(
summary_template
)
logger
.
info
(
"Loaded summary prompt from file"
)
else
:
# Fallback to default prompt
self
.
summary_prompt
=
ChatPromptTemplate
.
from_template
(
"You are an assistant for creating brief chat summaries. "
"Please provide your response in Russian.\n\n{messages}\n\n"
"Create a brief summary in Russian."
)
except
Exception
as
e
:
logger
.
error
(
f"Failed to load prompts:
{
e
}
"
)
# Fallback to default prompts
```

```bash
# chat_bot/prompts/summary.txt
You are an assistant
for
creating brief chat summaries.
Your task is to analyze messages from a chat and create a brief but informative summary
in
Russian.
The summary should include:
- Main discussion topics
- Key points
- Number of participants
- Overall tone of the conversation
Be concise but informative.
Use telegram emojis
for
better readability. You can
add
max one emoji.
Don
't change or translate names, use exact name provided.
A name consists of the First Name and Last Name. Don'
t show patronymic
in
the assignee name.
Use bullets
for
main discussion topics formatting.
Use line breaks
for
identation formatting.
Format message
for
easy reading
in
telegram.
You will provide your response
in
a structured
format
with two fields:
1
.
"thoughts"
- Your reasoning process and analysis of the messages
(
in Russian
)
2
.
"summary"
- The final Russian summary, formatted
for
Telegram
Here are the chat messages:
{
messages
}
Analyze the messages and provide your thoughts and summary
in
Russian.
```

Преимущества такого подхода:

- Промпты хранятся отдельно от кода.
- Легко редактировать и версионировать.
- Поддержка fallback промптов.
- Четкие инструкции для AI модели.

Промпты хранятся отдельно от кода.

Легко редактировать и версионировать.

Поддержка fallback промптов.

Четкие инструкции для AI модели.

```bash
# chat_bot/models/summary_response.py
class
SummaryOutput
(
BaseModel
)
:
"""
Structured output schema for summary generation from chat messages.
This model is used with LangChain's structured output feature to ensure
the AI model returns properly formatted summary data.
"""
thoughts
:
str
=
Field
(
.
.
.
,
description
=
"The AI's reasoning process and thoughts about the messages before creating the summary. This should be in Russian."
,
)
summary
:
str
=
Field
(
.
.
.
,
description
=
"The actual summary of the chat messages. This should be concise and in Russian."
,
)
# chat_bot/models/task_extraction_response.py
class
TaskExtractionOutput
(
BaseModel
)
:
"""
Structured output schema for task extraction from chat messages.
"""
tasks
:
List
[
Task
]
=
Field
(
default_factory
=
list
,
description
=
"List of tasks extracted from the chat messages. If no tasks are found, return an empty list."
,
)
class
Task
(
BaseModel
)
:
"""Represents a task extracted from chat messages."""
assignee
:
str
=
Field
(
.
.
.
,
description
=
"The person assigned to the task"
)
title
:
str
=
Field
(
.
.
.
,
description
=
"The title/description of the task"
)
deadline
:
Optional
[
datetime
]
=
Field
(
None
,
description
=
"Optional deadline date/time for the task"
)
```

```bash
async
def
summarize
(
self
,
messages_input
:
Union
[
str
,
Dict
[
str
,
Any
]
,
MessagesData
]
)
-
>
SummaryResponse
:
"""Summarize messages using LangChain's structured output."""
import
time
start_time
=
time
.
time
(
)
try
:
# Handle different input types
if
isinstance
(
messages_input
,
str
)
:
data
=
json
.
loads
(
messages_input
)
messages_data
=
MessagesData
(
**
data
)
elif
isinstance
(
messages_input
,
dict
)
:
messages_data
=
MessagesData
(
**
messages_input
)
elif
isinstance
(
messages_input
,
MessagesData
)
:
messages_data
=
messages_input
else
:
raise
ValueError
(
"Input must be either a JSON string, dictionary, or MessagesData object"
)
# Format messages for summarization
formatted_messages
=
MessageFormatter
.
format_messages_for_summary
(
messages_data
)
# Create the prompt
prompt
=
self
.
summary_prompt
.
format
(
messages
=
formatted_messages
)
# Create model with structured output
model_with_structure
=
self
.
llm
.
with_structured_output
(
SummaryOutput
)
# Generate summary response using structured output
structured_output
:
SummaryOutput
=
await
model_with_structure
.
ainvoke
(
prompt
)
processing_time
=
time
.
time
(
)
-
start_time
logger
.
info
(
"Successfully generated summary"
)
return
SummaryResponse
(
summary
=
structured_output
.
summary
,
success
=
True
,
error_message
=
None
,
processing_time
=
processing_time
,
)
except
Exception
as
e
:
logger
.
error
(
f"Failed to generate summary:
{
e
}
"
)
return
SummaryResponse
(
summary
=
""
,
success
=
False
,
error_message
=
f"Ошибка при создании сводки:
{
str
(
e
)
}
"
,
processing_time
=
time
.
time
(
)
-
start_time
,
)
```

Ключевые преимущества структурированного вывода:

- Гарантированная типизация ответов.
- Валидация данных через Pydantic.
- Предсказуемый формат ответов.
- Упрощенная обработка результатов.

Гарантированная типизация ответов.

Валидация данных через Pydantic.

Предсказуемый формат ответов.

Упрощенная обработка результатов.

## 3. Соберите образ и присвойте тег

Перед сборкой образа, убедитесь, что Docker Desktop запущен и пользователь авторизован в приложении.

Соберите образ и присвойте тег, используя команду:

```bash
docker
build
-t
evo-foundation-models-tg-bot-lab
.
docker
tag evo-foundation-models-tg-bot-lab
<
registry-name
>
.cr.cloud.ru/evo-foundation-models-tg-bot-lab:latest
```

Где <registry-name> — имя реестра, созданного при [подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)подготовке среды.

## 4. Загрузите Docker-образ в реестр

1. Загрузите образ в реестр Artifact Registry, выполнив команду:
docker push <registry-name>.cr.cloud.ru/evo-foundation-models-tg-bot-lab:latest

Где <registry-name> — имя реестра, созданного при [подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)подготовке среды.
2. В личном кабинете перейдите в сервис Artifact Registry и убедитесь, что образ загружен.

Загрузите образ в реестр Artifact Registry, выполнив команду:

```bash
docker
push
<
registry-name
>
.cr.cloud.ru/evo-foundation-models-tg-bot-lab:latest
```

Где <registry-name> — имя реестра, созданного при [подготовке среды](https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work)подготовке среды.

В личном кабинете перейдите в сервис Artifact Registry и убедитесь, что образ загружен.

## 5. Зарегистрируйте Telegram-бота

1. В Telegram найдите [BotFather](https://t.me/BotFather)BotFather.
2. Выполните команду /newbot.
3. Задайте название (name) и имя пользователя (username) для бота.
Имя пользователя должно оканчиваться на ...Bot или ..._bot.
Например:

name — new-bot
username — botforlabbot

В результате вы получите токен.
Сохраните его — он потребуется на следующих этапах.
4. С помощью команды /setuserpic установите иконку для вашего бота.

В Telegram найдите [BotFather](https://t.me/BotFather)BotFather.

![../_images/s__search-botfather.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__search-botfather.png)

Выполните команду /newbot.

Задайте название (name) и имя пользователя (username) для бота.

Имя пользователя должно оканчиваться на ...Bot или ..._bot.

Например:

- name — new-bot
- username — botforlabbot

name — new-bot

username — botforlabbot

В результате вы получите токен.
Сохраните его — он потребуется на следующих этапах.

![../_images/s__create-bot.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__create-bot.png)

С помощью команды /setuserpic установите иконку для вашего бота.

![../_images/s__set-userpick.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__set-userpick.png)

## 6. Сгенерируйте API-ключ для доступа к Foundation Models

1. На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
2. Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.
3. Перейдите на вкладку API-ключи.
4. Нажмите Создать API-ключ.
5. Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.
6. Заполните параметры API-ключа:

Сервисы — Foundation Models.
Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.
7. Нажмите Создать.
8. Сохраните Key Secret.
После закрытия окна получить его будет нельзя.
Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.

![../_images/s__service_account_n.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account_n.png)

Перейдите на вкладку API-ключи.

Нажмите Создать API-ключ.

![../_images/s__create_key.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__create_key.png)

Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.

Заполните параметры API-ключа:

- Сервисы — Foundation Models.
- Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
- Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Сервисы — Foundation Models.

Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.

Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Нажмите Создать.

Сохраните Key Secret.
После закрытия окна получить его будет нельзя.

Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

## 7. Создайте Object Storage и ключи доступа

1. [Создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в Object Storage со следующими параметрами:

Название: tg-bot-lab
Глобальное название: tg-bot-lab
Класс хранения по умолчанию: Стандартный
Максимальный размер: 10 ГБ
2. Перейдите в раздел Object Storage API.
Сохраните значения ID тенанта и Регион.
3. Убедитесь, что в личном кабинете на странице сервиса Object Storage отображается бакет tg-bot-lab.
4. [Создайте сервисный аккаунт пользователя](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт пользователя со следующими параметрами:

Название: tg-bot-lab-object-storage
Описание: Аккаунт пользователя Object Storage
Проект: Пользователь сервисов
Сервисы: оставьте список пустым
Evolution Object Storage Роли: s3e.viewer, s3e.editor
5. [Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.
6. Сохраните Secret ID и Secret Key для обоих ключей.

[Создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет в Object Storage со следующими параметрами:

- Название: tg-bot-lab
- Глобальное название: tg-bot-lab
- Класс хранения по умолчанию: Стандартный
- Максимальный размер: 10 ГБ

Название: tg-bot-lab

Глобальное название: tg-bot-lab

Класс хранения по умолчанию: Стандартный

Максимальный размер: 10 ГБ

Перейдите в раздел Object Storage API.
Сохраните значения ID тенанта и Регион.

Убедитесь, что в личном кабинете на странице сервиса Object Storage отображается бакет tg-bot-lab.

[Создайте сервисный аккаунт пользователя](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_create)Создайте сервисный аккаунт пользователя со следующими параметрами:

- Название: tg-bot-lab-object-storage
- Описание: Аккаунт пользователя Object Storage
- Проект: Пользователь сервисов
- Сервисы: оставьте список пустым
- Evolution Object Storage Роли: s3e.viewer, s3e.editor

Название: tg-bot-lab-object-storage

Описание: Аккаунт пользователя Object Storage

Проект: Пользователь сервисов

Сервисы: оставьте список пустым

Evolution Object Storage Роли: s3e.viewer, s3e.editor

[Сгенерируйте ключи доступа](https://cloud.ru/docs/console_api/ug/topics/guides__service_accounts_key)Сгенерируйте ключи доступа для сервисного аккаунта.

Сохраните Secret ID и Secret Key для обоих ключей.

## 8. Создайте и запустите контейнер

1. Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.
2. Нажмите Создать.
3. Заполните поля и активируйте опции:

Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене \*.containers.cloud.ru.
URI образа — выберите образ, загруженный в Artifact Registry [на шаге 4](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 4.
Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этой лабораторной работе мы используем порт 8080.
vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.
Минимальное и Максимальное количество экземпляров при масштабировании сервиса.
Установите минимальное и максимальное количество экземпляров в значении 1, чтобы приложение всегда оставалось активным.
Переменные — добавьте следующие переменные:

TELEGRAM_BOT_TOKEN — токен Telegram-бота, полученный [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 5
AI_API_KEY — токен сервиса Foundation Models, полученный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 6
AI_MODEL — название AI-модели для нашего сервиса.
Используйте значение RefalMachine/RuadaptQwen2.5-32B-Pro-Beta
AI_BASE_URL — https://foundation-models.api.cloud.ru/v1/
AI_TEMPERATURE — 0.5
AI_MAX_TOKENS — 1000
OBJECT_STORAGE_BUCKET_NAME — tg-bot-lab.
Название бакета, созданного [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7.
OBJECT_STORAGE_ACCESS_KEY_ID — ключ для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
OBJECT_STORAGE_SECRET_ACCESS_KEY — секрет для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
OBJECT_STORAGE_REGION — ru-central-1
OBJECT_STORAGE_ROOT_DIR — chat_logs
OBJECT_STORAGE_ENDPOINT_URL — https://s3.cloud.ru

Активируйте опцию Автоматическое развертывание, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.
4. Нажмите Создать.
Контейнер будет запущен в течение нескольких секунд.
5. Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

Перейдите в сервис Container Apps через меню в левом верхнем углу экрана.

Нажмите Создать.

Заполните поля и активируйте опции:

1. Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене \*.containers.cloud.ru.
2. URI образа — выберите образ, загруженный в Artifact Registry [на шаге 4](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 4.
3. Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этой лабораторной работе мы используем порт 8080.
4. vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.
5. Минимальное и Максимальное количество экземпляров при масштабировании сервиса.
Установите минимальное и максимальное количество экземпляров в значении 1, чтобы приложение всегда оставалось активным.
6. Переменные — добавьте следующие переменные:

TELEGRAM_BOT_TOKEN — токен Telegram-бота, полученный [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 5
AI_API_KEY — токен сервиса Foundation Models, полученный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 6
AI_MODEL — название AI-модели для нашего сервиса.
Используйте значение RefalMachine/RuadaptQwen2.5-32B-Pro-Beta
AI_BASE_URL — https://foundation-models.api.cloud.ru/v1/
AI_TEMPERATURE — 0.5
AI_MAX_TOKENS — 1000
OBJECT_STORAGE_BUCKET_NAME — tg-bot-lab.
Название бакета, созданного [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7.
OBJECT_STORAGE_ACCESS_KEY_ID — ключ для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
OBJECT_STORAGE_SECRET_ACCESS_KEY — секрет для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
OBJECT_STORAGE_REGION — ru-central-1
OBJECT_STORAGE_ROOT_DIR — chat_logs
OBJECT_STORAGE_ENDPOINT_URL — https://s3.cloud.ru
7. Активируйте опцию Автоматическое развертывание, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.

Название контейнера — глобально уникальное имя, на базе которого формируется адрес вашего приложения в домене \*.containers.cloud.ru.

URI образа — выберите образ, загруженный в Artifact Registry [на шаге 4](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 4.

Порт контейнера — порт контейнера, который должен совпадать с портом вашего приложения.
В этой лабораторной работе мы используем порт 8080.

vCPU/RAM — количество vCPU и RAM, которые выделяются для каждого экземпляра контейнера при обработке вызова.
Выберите минимальную конфигурацию.

Минимальное и Максимальное количество экземпляров при масштабировании сервиса.
Установите минимальное и максимальное количество экземпляров в значении 1, чтобы приложение всегда оставалось активным.

Переменные — добавьте следующие переменные:

- TELEGRAM_BOT_TOKEN — токен Telegram-бота, полученный [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 5
- AI_API_KEY — токен сервиса Foundation Models, полученный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 6
- AI_MODEL — название AI-модели для нашего сервиса.
Используйте значение RefalMachine/RuadaptQwen2.5-32B-Pro-Beta
- AI_BASE_URL — https://foundation-models.api.cloud.ru/v1/
- AI_TEMPERATURE — 0.5
- AI_MAX_TOKENS — 1000
- OBJECT_STORAGE_BUCKET_NAME — tg-bot-lab.
Название бакета, созданного [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7.
- OBJECT_STORAGE_ACCESS_KEY_ID — ключ для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
- OBJECT_STORAGE_SECRET_ACCESS_KEY — секрет для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7
- OBJECT_STORAGE_REGION — ru-central-1
- OBJECT_STORAGE_ROOT_DIR — chat_logs
- OBJECT_STORAGE_ENDPOINT_URL — https://s3.cloud.ru

TELEGRAM_BOT_TOKEN — токен Telegram-бота, полученный [на шаге 5](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 5

AI_API_KEY — токен сервиса Foundation Models, полученный [на шаге 6](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 6

AI_MODEL — название AI-модели для нашего сервиса.
Используйте значение RefalMachine/RuadaptQwen2.5-32B-Pro-Beta

AI_BASE_URL — https://foundation-models.api.cloud.ru/v1/

AI_TEMPERATURE — 0.5

AI_MAX_TOKENS — 1000

OBJECT_STORAGE_BUCKET_NAME — tg-bot-lab.
Название бакета, созданного [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7.

OBJECT_STORAGE_ACCESS_KEY_ID — ключ для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7

OBJECT_STORAGE_SECRET_ACCESS_KEY — секрет для доступа к бакету Object Storage, полученный [на шаге 7](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__langchain-tg-bot)на шаге 7

OBJECT_STORAGE_REGION — ru-central-1

OBJECT_STORAGE_ROOT_DIR — chat_logs

OBJECT_STORAGE_ENDPOINT_URL — https://s3.cloud.ru

Активируйте опцию Автоматическое развертывание, чтобы каждый раз после загрузки в Artifact Registry новой версии образа на стороне Container Apps автоматически создавалась новая ревизия контейнера.

Нажмите Создать.

Контейнер будет запущен в течение нескольких секунд.

Дождитесь, когда контейнер и ревизия перейдут в статус «Выполняется».

## 9. Проверьте работоспособность развернутого чат-бота

1. Добавьте чат-бота в закрытый канал или чат в Telegram с ролью администратор.
2. Напишите несколько сообщений в канал или чат.
3. Выполните команду /summary.
Дождитесь ответа от чат-бота с суммаризацией вашей переписки.
4. Выполните команду /tasks.
Дождитесь ответа от чат-бота со списком задач.

Добавьте чат-бота в закрытый канал или чат в Telegram с ролью администратор.

Напишите несколько сообщений в канал или чат.

Выполните команду /summary.
Дождитесь ответа от чат-бота с суммаризацией вашей переписки.

Выполните команду /tasks.
Дождитесь ответа от чат-бота со списком задач.

![../_images/s__chat_bot_summary_tasks.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__chat_bot_summary_tasks.png)

## Результат

В ходе выполнения практической работы вы получили практический опыт интеграции LLM-моделей из сервиса Foundation Models в Telegram-экосистему, освоили приемы безопасной работы с ключами и конфигурацией, а также убедились, что сервис Foundation Models существенно упрощает создание production-ready AI-сервисов.
