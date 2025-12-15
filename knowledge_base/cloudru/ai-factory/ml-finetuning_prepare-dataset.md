---
title: Подготовка датасета Alpaca для использования в ML Finetuning
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset
topic: ai-factory
---
# Подготовка датасета Alpaca для использования в ML Finetuning

С помощью этого руководства вы подготовите датасет GitHub Issue в формате Alpaca для использования в сервисе ML Finetuning.

Датасет предназначен для дообучения моделей, которые решают задачу генерации заголовка на основе текстового описания проблемы.

В качестве исходного используется датасет mlfoundations-dev/github-issues.
В результате получится набор данных в формате Alpaca, опубликованный на HuggingFace Hub.

Вы будете использовать следующие сервисы:

- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- Huggingface — платформа для публикации и использования моделей машинного обучения.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

Huggingface — платформа для публикации и использования моделей машинного обучения.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Подготовьте среду.
2. [Загрузите и исследуйте исходный датасет](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Загрузите и исследуйте исходный датасет.
3. [Отфильтруйте датасет](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Отфильтруйте датасет.
4. [Преобразуйте датасет в формат Alpaca](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Преобразуйте датасет в формат Alpaca.
5. [Загрузите датасет на HuggingFace Hub](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Загрузите датасет на HuggingFace Hub.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Подготовьте среду.

[Загрузите и исследуйте исходный датасет](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Загрузите и исследуйте исходный датасет.

[Отфильтруйте датасет](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Отфильтруйте датасет.

[Преобразуйте датасет в формат Alpaca](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Преобразуйте датасет в формат Alpaca.

[Загрузите датасет на HuggingFace Hub](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__prepare-dataset)Загрузите датасет на HuggingFace Hub.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. Убедитесь, что в личном кабинете Cloud.ru подключен сервис Notebooks.
3. Создайте токен Huggingface.

Войдите или зарегистрируйтесь на [https://huggingface.co](https://huggingface.co/)https://huggingface.co.
Перейдите [в раздел Access Tokens](https://huggingface.co/settings/tokens)в раздел Access Tokens.

Нажмите Create new token.
Выберите тип Write.
Введите название токена.

Нажмите Create token.
Скопируйте токен и сохраните его, например в блокнот.
После закрытия страницы он будет недоступен.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

Убедитесь, что в личном кабинете Cloud.ru подключен сервис Notebooks.

Создайте токен Huggingface.

1. Войдите или зарегистрируйтесь на [https://huggingface.co](https://huggingface.co/)https://huggingface.co.
2. Перейдите [в раздел Access Tokens](https://huggingface.co/settings/tokens)в раздел Access Tokens.
3. Нажмите Create new token.
4. Выберите тип Write.
5. Введите название токена.
6. Нажмите Create token.
7. Скопируйте токен и сохраните его, например в блокнот.
После закрытия страницы он будет недоступен.

Войдите или зарегистрируйтесь на [https://huggingface.co](https://huggingface.co/)https://huggingface.co.

Перейдите [в раздел Access Tokens](https://huggingface.co/settings/tokens)в раздел Access Tokens.

![Раздел "Access Token"](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__ml-finetuning__finetune-example__hf-access-tokens.png)

Нажмите Create new token.

Выберите тип Write.

Введите название токена.

![Создание токена](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__ml-finetuning__finetune-example__hf-create-token.png)

Нажмите Create token.

Скопируйте токен и сохраните его, например в блокнот.
После закрытия страницы он будет недоступен.

## 1. Подготовьте среду

1. [Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/guides__ntb-create)Создайте ноутбук со следующими параметрами:

Конфигурация — ncpu.medium.4.
Образ — Cloud.ru Jupyter (Conda) 0.3.2.

Затем по той же инструкции настройте окружение ноутбука.
2. На главной странице сервиса Notebooks в строке нужного ноутбука нажмите JupyterLab — вы перейдете в среду разработки.
3. Установите библиотеки, выполнив код:

pip install matplotlib numpy datasets huggingface_hub langdetect
4. Импортируйте прочие библиотеки, добавив код:

import matplotlib.pyplot as pltimport numpy as npfrom datasets import load_datasetfrom huggingface_hub import loginfrom langdetect import detectfrom langdetect.lang_detect_exception import LangDetectException
# HuggingFace Authentication# Specify your HuggingFace Tokenlogin()

[Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/guides__ntb-create)Создайте ноутбук со следующими параметрами:

- Конфигурация — ncpu.medium.4.
- Образ — Cloud.ru Jupyter (Conda) 0.3.2.

Конфигурация — ncpu.medium.4.

Образ — Cloud.ru Jupyter (Conda) 0.3.2.

Затем по той же инструкции настройте окружение ноутбука.

На главной странице сервиса Notebooks в строке нужного ноутбука нажмите JupyterLab — вы перейдете в среду разработки.

Установите библиотеки, выполнив код:

```bash
pip
install
matplotlib numpy datasets huggingface_hub langdetect
```

Импортируйте прочие библиотеки, добавив код:

```bash
import
matplotlib
.
pyplot
as
plt
import
numpy
as
np
from
datasets
import
load_dataset
from
huggingface_hub
import
login
from
langdetect
import
detect
from
langdetect
.
lang_detect_exception
import
LangDetectException
# HuggingFace Authentication
# Specify your HuggingFace Token
login
(
)
```

## 2. Загрузите и исследуйте исходный датасет

1. Для загрузки датасета Github Issue добавьте следующий код:

dataset = load_dataset("mlfoundations-dev/github-issues", split="train")
2. Чтобы понять структуру данных, ознакомьтесь с примерами записей в датасете:

def show_samples(dataset, num_samples=3): """Отображение примеров записей из набора данных.""" sample = dataset.shuffle().select(range(num_samples))
 for example in sample: print(f" >> Заголовок: {example['title']}") print("-" * 50) print(f" >> Тело: \n {example['body']}") print("=" * 80) print() print()
show_samples(dataset)
3. Постройте распределение длин поля body — текстовых описаний проблем:

# Вычисление длин тел для всех проблемbody_lengths = [len(str(item['body'])) for item in dataset]body_lengths = np.array(body_lengths)
# Отображение статистикиprint("Примерная статистика длин тел:")print(f"Минимум: {body_lengths.min()}")print(f"Максимум: {body_lengths.max()}")print(f"Среднее: {body_lengths.mean():.2f}")print(f"Медиана: {np.median(body_lengths):.2f}")print(f"Стандартное отклонение: {body_lengths.std():.2f}")print(f"90-й процентиль: {np.percentile(body_lengths, 90):.2f}")print(f"95-й процентиль: {np.percentile(body_lengths, 95):.2f}")print(f"99-й процентиль: {np.percentile(body_lengths, 99):.2f}")
plt.figure(figsize=(10, 6))plt.hist(body_lengths, bins=50, log=True)plt.xlabel('Длина тела')plt.ylabel('Количество проблем')plt.title('Распределение длин тел проблем')plt.show()

Для загрузки датасета Github Issue добавьте следующий код:

```bash
dataset
=
load_dataset
(
"mlfoundations-dev/github-issues"
,
split
=
"train"
)
```

Чтобы понять структуру данных, ознакомьтесь с примерами записей в датасете:

```bash
def
show_samples
(
dataset
,
num_samples
=
3
)
:
"""Отображение примеров записей из набора данных."""
sample
=
dataset
.
shuffle
(
)
.
select
(
range
(
num_samples
)
)
for
example
in
sample
:
print
(
f" >> Заголовок:
{
example
[
'title'
]
}
"
)
print
(
"-"
*
50
)
print
(
f" >> Тело: \n
{
example
[
'body'
]
}
"
)
print
(
"="
*
80
)
print
(
)
print
(
)
show_samples
(
dataset
)
```

Постройте распределение длин поля body — текстовых описаний проблем:

```bash
# Вычисление длин тел для всех проблем
body_lengths
=
[
len
(
str
(
item
[
'body'
]
)
)
for
item
in
dataset
]
body_lengths
=
np
.
array
(
body_lengths
)
# Отображение статистики
print
(
"Примерная статистика длин тел:"
)
print
(
f"Минимум:
{
body_lengths
.
min
(
)
}
"
)
print
(
f"Максимум:
{
body_lengths
.
max
(
)
}
"
)
print
(
f"Среднее:
{
body_lengths
.
mean
(
)
:
.2f
}
"
)
print
(
f"Медиана:
{
np
.
median
(
body_lengths
)
:
.2f
}
"
)
print
(
f"Стандартное отклонение:
{
body_lengths
.
std
(
)
:
.2f
}
"
)
print
(
f"90-й процентиль:
{
np
.
percentile
(
body_lengths
,
90
)
:
.2f
}
"
)
print
(
f"95-й процентиль:
{
np
.
percentile
(
body_lengths
,
95
)
:
.2f
}
"
)
print
(
f"99-й процентиль:
{
np
.
percentile
(
body_lengths
,
99
)
:
.2f
}
"
)
plt
.
figure
(
figsize
=
(
10
,
6
)
)
plt
.
hist
(
body_lengths
,
bins
=
50
,
log
=
True
)
plt
.
xlabel
(
'Длина тела'
)
plt
.
ylabel
(
'Количество проблем'
)
plt
.
title
(
'Распределение длин тел проблем'
)
plt
.
show
(
)
```

## 3. Отфильтруйте датасет

1. Оставьте только те строки, где значение body находится в диапазоне от 100 до 5 000 символов:

def filter_by_body_length(example): """Фильтрация проблем по длине тела (100-5000 символов).""" length = len(str(example['body'])) return 100 <= length <= 5000
filtered_dataset = dataset.filter(filter_by_body_length)print(f"Общее количество проблем после фильтрации по длине: {len(filtered_dataset)}")
2. Оставьте только записи на английском языке:

def is_english(example): """Checking whether the title and body are written in English""" try: return detect(example["title"]) == "en" and detect(example["body"]) == "en" except LangDetectException: return False
# For faster processing, you can apply filtering to a subset of the dataset# english_ds = filtered_dataset.select(range(100000)).filter(is_english, num_proc=4)english_ds = filtered_dataset.filter(is_english, num_proc=4)print(f"Количество английских примеров: {len(english_ds)}")

Оставьте только те строки, где значение body находится в диапазоне от 100 до 5 000 символов:

```bash
def
filter_by_body_length
(
example
)
:
"""Фильтрация проблем по длине тела (100-5000 символов)."""
length
=
len
(
str
(
example
[
'body'
]
)
)
return
100
<=
length
<=
5000
filtered_dataset
=
dataset
.
filter
(
filter_by_body_length
)
print
(
f"Общее количество проблем после фильтрации по длине:
{
len
(
filtered_dataset
)
}
"
)
```

Оставьте только записи на английском языке:

```bash
def
is_english
(
example
)
:
"""Checking whether the title and body are written in English"""
try
:
return
detect
(
example
[
"title"
]
)
==
"en"
and
detect
(
example
[
"body"
]
)
==
"en"
except
LangDetectException
:
return
False
# For faster processing, you can apply filtering to a subset of the dataset
# english_ds = filtered_dataset.select(range(100000)).filter(is_english, num_proc=4)
english_ds
=
filtered_dataset
.
filter
(
is_english
,
num_proc
=
4
)
print
(
f"Количество английских примеров:
{
len
(
english_ds
)
}
"
)
```

## 4. Преобразуйте датасет в формат Alpaca

Преобразуйте датасет в формат Alpaca, в котором каждый пример — это словарь с тремя полями:

- instruction — текстовое задание для модели;
- input — входные данные;
- output — целевой ответ.

instruction — текстовое задание для модели;

input — входные данные;

output — целевой ответ.

```bash
def
convert_to_alpaca_format
(
example
)
:
return
{
"instruction"
:
"Write short and clear GitHib issue title that captures main problem."
,
"input"
:
example
[
"body"
]
,
"output"
:
example
[
"title"
]
,
}
alpaca_dataset
=
english_ds
.
map
(
convert_to_alpaca_format
)
alpaca_dataset
=
alpaca_dataset
.
remove_columns
(
[
col
for
col
in
alpaca_dataset
.
column_names
if
col
not
in
[
"instruction"
,
"input"
,
"output"
]
]
)
```

## 5. Загрузите датасет на HuggingFace Hub

Опубликуйте итоговый датасет в ваш репозиторий на HuggingFace Hub, подставив свои данные:

```bash
alpaca_dataset
.
push_to_hub
(
"your_login/hf-repository_name"
)
```

Вы можете [скачать готовый ноутбук](https://xbox.cloud.ru/s/MwqqcfTciwQRGta)скачать готовый ноутбук, содержащий код и инструкции для обработки датасета из этого практического руководства.

## Результат

Вы подготовили очищенный и структурированный датасет для задач генерации заголовков GitHub Issue по их описанию, преобразовали его в формат Alpaca и опубликовали на HuggingFace Hub для использования в сервисе ML Finetuning.
Теперь вы можете [дообучить модель из Huggingface](https://cloud.ru/docs/finetuning/ug/topics/tutorials__finetune-example)дообучить модель из Huggingface, используя подготовленный датасет.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, получайте навыки управления облаком, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
