---
title: Дообучение готовой модели из Huggingface
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__finetune-example
topic: ai-factory
---
# Дообучение готовой модели из Huggingface

С помощью этого руководства вы запустите процесс дообучения модели mistralai/Ministral-8B-Instruct-2410.

Вы будете использовать следующие сервисы:

- [Secret Management](https://cloud.ru/docs/scsm/ug/index)Secret Management — безопасное хранилище секретов.
- [ML Finetuning](https://cloud.ru/docs/finetuning/ug/index)ML Finetuning — сервис для дообучения моделей.
- [Huggingface](https://huggingface.co/)Huggingface — платформа для публикации и использования моделей машинного обучения.

[Secret Management](https://cloud.ru/docs/scsm/ug/index)Secret Management — безопасное хранилище секретов.

[ML Finetuning](https://cloud.ru/docs/finetuning/ug/index)ML Finetuning — сервис для дообучения моделей.

[Huggingface](https://huggingface.co/)Huggingface — платформа для публикации и использования моделей машинного обучения.

Шаги:

1. [Создайте секрет с токеном Huggingface](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__finetune-example)Создайте секрет с токеном Huggingface.
2. [Запустите дообучение модели и проверьте результат](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__finetune-example)Запустите дообучение модели и проверьте результат.

[Создайте секрет с токеном Huggingface](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__finetune-example)Создайте секрет с токеном Huggingface.

[Запустите дообучение модели и проверьте результат](https://cloud.ru/docs/tutorials-evolution/list/topics/ml-finetuning__finetune-example)Запустите дообучение модели и проверьте результат.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Создайте секрет с токеном Huggingface

1. Создайте токен Huggingface.

Войдите или зарегистрируйтесь на [https://huggingface.co](https://huggingface.co/)https://huggingface.co.
Перейдите [в раздел Access Tokens](https://huggingface.co/settings/tokens)в раздел Access Tokens.

Нажмите Create new token.
Выберите тип Write.
Введите название токена.

Нажмите Create token.
Скопируйте токен и сохраните его, например в блокнот.
После закрытия страницы он будет недоступен.
2. [Создайте секрет в Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секрет в Secret Management со следующими параметрами:

В поле Название укажите название секрета, например hf-token.
В поле Значение вставьте токен, полученный в личном кабинете Huggingface.

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

[Создайте секрет в Secret Management](https://cloud.ru/docs/scsm/ug/topics/guides__add-secret)Создайте секрет в Secret Management со следующими параметрами:

1. В поле Название укажите название секрета, например hf-token.
2. В поле Значение вставьте токен, полученный в личном кабинете Huggingface.

В поле Название укажите название секрета, например hf-token.

В поле Значение вставьте токен, полученный в личном кабинете Huggingface.

## 2. Запустите дообучение модели

1. Перейдите в AI Factory → ML Finetuning.
2. Нажмите Дообучить модель.

В поле Репозиторий с моделью укажите название модели mistralai/Ministral-8B-Instruct-2410.
ПримечаниеПеред началом дообучения убедитесь, что у вас есть доступ к модели, проверив ее карточку на Huggingface.
Для модели mistralai/Ministral-8B-Instruct-2410 запрашивать специальный доступ не нужно.

В поле Токен доступа выберите секрет hf-token.
В поле Репозиторий модели укажите репозиторий для загрузки дообученной модели my-org/ministral-finetuned.
В поле Датасет укажите репозиторий датасета tatsu-lab/alpaca.
В поле Метод обучения выберите LoRA.
Укажите гиперпараметры обучения:

Learning rate — 0.0001.
Epoch — 3.
Gradient accumulation — 4.
Batch size per device — 16.
Training precision — bf16.
Logging steps — 50.
Save steps — 500.
Max samples — 100000.

Нажмите Запустить дообучение.
3. Проверьте результат дообучения в логах:

Перейдите в AI Factory → ML Finetuning.
Нажмите на название модели.
Перейдите на вкладку Логи.

Перейдите в AI Factory → ML Finetuning.

Нажмите Дообучить модель.

1. В поле Репозиторий с моделью укажите название модели mistralai/Ministral-8B-Instruct-2410.
ПримечаниеПеред началом дообучения убедитесь, что у вас есть доступ к модели, проверив ее карточку на Huggingface.
Для модели mistralai/Ministral-8B-Instruct-2410 запрашивать специальный доступ не нужно.
2. В поле Токен доступа выберите секрет hf-token.
3. В поле Репозиторий модели укажите репозиторий для загрузки дообученной модели my-org/ministral-finetuned.
4. В поле Датасет укажите репозиторий датасета tatsu-lab/alpaca.
5. В поле Метод обучения выберите LoRA.
6. Укажите гиперпараметры обучения:

Learning rate — 0.0001.
Epoch — 3.
Gradient accumulation — 4.
Batch size per device — 16.
Training precision — bf16.
Logging steps — 50.
Save steps — 500.
Max samples — 100000.
7. Нажмите Запустить дообучение.

В поле Репозиторий с моделью укажите название модели mistralai/Ministral-8B-Instruct-2410.

Перед началом дообучения убедитесь, что у вас есть доступ к модели, проверив ее карточку на Huggingface.

Для модели mistralai/Ministral-8B-Instruct-2410 запрашивать специальный доступ не нужно.

В поле Токен доступа выберите секрет hf-token.

В поле Репозиторий модели укажите репозиторий для загрузки дообученной модели my-org/ministral-finetuned.

В поле Датасет укажите репозиторий датасета tatsu-lab/alpaca.

В поле Метод обучения выберите LoRA.

Укажите гиперпараметры обучения:

- Learning rate — 0.0001.
- Epoch — 3.
- Gradient accumulation — 4.
- Batch size per device — 16.
- Training precision — bf16.
- Logging steps — 50.
- Save steps — 500.
- Max samples — 100000.

Learning rate — 0.0001.

Epoch — 3.

Gradient accumulation — 4.

Batch size per device — 16.

Training precision — bf16.

Logging steps — 50.

Save steps — 500.

Max samples — 100000.

Нажмите Запустить дообучение.

Проверьте результат дообучения в логах:

1. Перейдите в AI Factory → ML Finetuning.
2. Нажмите на название модели.
3. Перейдите на вкладку Логи.

Перейдите в AI Factory → ML Finetuning.

Нажмите на название модели.

Перейдите на вкладку Логи.

## Что дальше

Вы создали секрет с токеном Huggingface, запустили процесс дообучения модели в сервисе ML Finetuning и проверили модель в Huggingface.
Полученные навыки помогут интегрировать внешние модели и данные в облачную инфраструктуру Cloud.ru, а также автоматизировать процесс дообучения.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, получайте навыки управления облаком, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
