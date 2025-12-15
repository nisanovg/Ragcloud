---
title: Создание базы знаний из JSON-файла
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__json-files
topic: ai-factory
---
# Создание базы знаний из JSON-файла

В руководстве описан сценарий создания базы знаний с ручной настройкой экстрактора для конкретного JSON-файла.

Общий алгоритм описан в [инструкции по созданию базы знаний](https://cloud.ru/docs/rag/ug/topics/guides__create-kb)инструкции по созданию базы знаний.

Вы будете использовать следующие сервисы:

- [Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

Шаги:

1. [Подготовьте контент для базы знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__json-files)Подготовьте контент для базы знаний.
2. [Создайте базу знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__json-files)Создайте базу знаний.

[Подготовьте контент для базы знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__json-files)Подготовьте контент для базы знаний.

[Создайте базу знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__json-files)Создайте базу знаний.

## Перед началом работы

1. Убедитесь, что у вас есть доступ к [Foundation Models](https://cloud.ru/docs/foundation-models/ug/topics/quickstart)Foundation Models и [Object Storage](https://cloud.ru/docs/s3e/ug/topics/quickstart)Object Storage.
2. [Скачайте файл faq_products.json](https://xbox.cloud.ru/index.php/s/BrZc3SC4X7ae7oT)Скачайте файл faq_products.json.

Убедитесь, что у вас есть доступ к [Foundation Models](https://cloud.ru/docs/foundation-models/ug/topics/quickstart)Foundation Models и [Object Storage](https://cloud.ru/docs/s3e/ug/topics/quickstart)Object Storage.

[Скачайте файл faq_products.json](https://xbox.cloud.ru/index.php/s/BrZc3SC4X7ae7oT)Скачайте файл faq_products.json.

## Шаг 1. Подготовьте контент для базы знаний

Необходим документ для базы знаний в [Evolution Object Storage](https://cloud.ru/docs/s3e/ug/topics/quickstart)Evolution Object Storage.
Для этого:

1. [Создайте бакет](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет.
2. Создайте папку rag-json-kb в бакете и [загрузите в нее](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)загрузите в нее файл faq_products.json, скачанный ранее.
[Список поддерживаемых типов файлов](https://cloud.ru/docs/rag/ug/topics/concepts__extensions)Список поддерживаемых типов файлов

[Создайте бакет](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)Создайте бакет.

Создайте папку rag-json-kb в бакете и [загрузите в нее](https://cloud.ru/docs/s3e/ug/topics/guides__file-manager_upload-file)загрузите в нее файл faq_products.json, скачанный ранее.

[Список поддерживаемых типов файлов](https://cloud.ru/docs/rag/ug/topics/concepts__extensions)Список поддерживаемых типов файлов

## Шаг 2. Создайте базу знаний

1. Перейдите в AI Factory → Managed RAG.
2. Нажмите Создать базу знаний.
3. Введите название и, если необходимо, описание базы знаний.
4. В поле Путь к папке с документами на S3 выберите папку rag-json-kb в бакете Object Storage, куда вы загрузили файл faq_products.json.
5. В поле Расширения документов введите json — расширение файла, который будет обработан и сохранен в базе знаний.
6. Активируйте опцию Вручную настроить обработку данных и модель.
Теперь необходимо настроить экстратор так, чтобы получились чанки вида:
Продукт: Evolution Foundation ModelsВопрос: Какой SLA у сервиса Foundation Models?Ответ: SLA на сервис Foundation Models составляет 99.9%.

Скопируйте jq-схему и проверьте ее корректность с помощью сайта [https://play.jqlang.org](https://play.jqlang.org/)https://play.jqlang.org:
.content[]|"Продукт: \(.product); Вопрос: \(.question); Ответ: \(.answer)"

Активируйте опцию Парсер по jq-cхеме вернет массив строк, так как в результате парсинга по jq-схеме возвращаются строки.
В поле Splitter выберите RecursiveCharacterTextSplitter — способ разбиения текста на чанки.
Остальные поля оставьте без изменений.
Нажмите Продолжить.
Выберите модель-эмбеддер или оставьте по умолчанию.
Нажмите Создать.

Перейдите в AI Factory → Managed RAG.

Нажмите Создать базу знаний.

Введите название и, если необходимо, описание базы знаний.

В поле Путь к папке с документами на S3 выберите папку rag-json-kb в бакете Object Storage, куда вы загрузили файл faq_products.json.

В поле Расширения документов введите json — расширение файла, который будет обработан и сохранен в базе знаний.

Активируйте опцию Вручную настроить обработку данных и модель.

Теперь необходимо настроить экстратор так, чтобы получились чанки вида:

```bash
Продукт: Evolution Foundation Models
Вопрос: Какой SLA у сервиса Foundation Models?
Ответ: SLA на сервис Foundation Models составляет 99.9%.
```

1. Скопируйте jq-схему и проверьте ее корректность с помощью сайта [https://play.jqlang.org](https://play.jqlang.org/)https://play.jqlang.org:
.content[]|"Продукт: \(.product); Вопрос: \(.question); Ответ: \(.answer)"
2. Активируйте опцию Парсер по jq-cхеме вернет массив строк, так как в результате парсинга по jq-схеме возвращаются строки.
3. В поле Splitter выберите RecursiveCharacterTextSplitter — способ разбиения текста на чанки.
Остальные поля оставьте без изменений.
4. Нажмите Продолжить.
5. Выберите модель-эмбеддер или оставьте по умолчанию.
6. Нажмите Создать.

Скопируйте jq-схему и проверьте ее корректность с помощью сайта [https://play.jqlang.org](https://play.jqlang.org/)https://play.jqlang.org:

```bash
.content
[
]
|
"Продукт: \(.product); Вопрос: \(.question); Ответ: \(.answer)"
```

Активируйте опцию Парсер по jq-cхеме вернет массив строк, так как в результате парсинга по jq-схеме возвращаются строки.

В поле Splitter выберите RecursiveCharacterTextSplitter — способ разбиения текста на чанки.
Остальные поля оставьте без изменений.

Нажмите Продолжить.

Выберите модель-эмбеддер или оставьте по умолчанию.

Нажмите Создать.

Дождитесь, пока база знаний и ее версия перейдет в статус «Активная».

## Что дальше

С этим руководством вы создали базу знаний с помощью Managed RAG, загрузили в неё JSON-файлы и настроили.

Теперь можно [отправлять API-запросы к версии базы знаний](https://cloud.ru/docs/rag/ug/topics/guides__send-request-kb-version)отправлять API-запросы к версии базы знаний.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, получайте навыки управления облаком, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
