---
title: Генерация изображений с ComfyUI на основе Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui
topic: ai-factory
---
# Генерация изображений с ComfyUI на основе Notebooks

С помощью этого руководства вы научитесь настраивать среду для генерации изображений с помощью ComfyUI, загружать модели с платформы Hugging Face и создавать изображения на основе текстовых промптов.

Вы будете использовать следующие сервисы:

- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- [Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.
- [Hugging Face](https://huggingface.co/)Hugging Face — платформа с открытым исходным кодом и сообщество разработчиков, ориентированное на машинное обучение, обработку естественного языка (NLP) и другие области искусственного интеллекта.
- [ComfyUI](https://docs.comfy.org/)ComfyUI — визуальная среда для создания и запуска процессов генерации контента на основе моделей диффузии.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

[Object Storage](https://cloud.ru/docs/s3e/ug/index)Object Storage — объектное S3-хранилище [с бесплатным хранением файлов](https://cloud.ru/docs/s3e/ug/topics/overview__free-tier)с бесплатным хранением файлов, объемом до 15 ГБ.

[Hugging Face](https://huggingface.co/)Hugging Face — платформа с открытым исходным кодом и сообщество разработчиков, ориентированное на машинное обучение, обработку естественного языка (NLP) и другие области искусственного интеллекта.

[ComfyUI](https://docs.comfy.org/)ComfyUI — визуальная среда для создания и запуска процессов генерации контента на основе моделей диффузии.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Подготовьте среду.
2. [Загрузите модель из Hugging Face](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Загрузите модель из Hugging Face.
3. [Сгенерируйте изображение](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Сгенерируйте изображение.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Подготовьте среду.

[Загрузите модель из Hugging Face](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Загрузите модель из Hugging Face.

[Сгенерируйте изображение](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__images-comfyui)Сгенерируйте изображение.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

## 1. Подготовьте среду

1. Для хранения модели [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage, если не сделали этого ранее.
2. [Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

Конфигурация — GPU.
Образ — Cloud.ru Jupyter ComfyUI.
Том — укажите бакет для хранения модели.

Для хранения модели [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage, если не сделали этого ранее.

[Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

- Конфигурация — GPU.
- Образ — Cloud.ru Jupyter ComfyUI.
- Том — укажите бакет для хранения модели.

Конфигурация — GPU.

Образ — Cloud.ru Jupyter ComfyUI.

Том — укажите бакет для хранения модели.

## 2. Загрузите модель из Hugging Face

1. Откройте созданный ноутбук.
2. Выберите тип ноутбука Python 3.
3. Загрузите модель в бакет S3 или напрямую в ноутбук:
Загрузка модели в бакет Object StorageЗагрузка модели в ноутбук
Загрузите модель в бакет S3:
!wget <model-address>-O <buсket-address>

Где:

<model-address> — адрес модели в репозитории Hugging Face.
<buсket-address> — адрес бакета в Object Storage.

Пример:
!wget https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/resolve/main/v1-5-pruned-emaonly-fp16.safetensors \-O /mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors

Создайте символическую ссылку для доступа к модели из ComfyUI:
!ln -s /mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors \/comfyui/models/checkpoints/v1-5-pruned-emaonly-fp16.safetensors

Откройте созданный ноутбук.

Выберите тип ноутбука Python 3.

Загрузите модель в бакет S3 или напрямую в ноутбук:

1. Загрузите модель в бакет S3:
!wget <model-address>-O <buсket-address>

Где:

<model-address> — адрес модели в репозитории Hugging Face.
<buсket-address> — адрес бакета в Object Storage.

Пример:
!wget https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/resolve/main/v1-5-pruned-emaonly-fp16.safetensors \-O /mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors
2. Создайте символическую ссылку для доступа к модели из ComfyUI:
!ln -s /mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors \/comfyui/models/checkpoints/v1-5-pruned-emaonly-fp16.safetensors

Загрузите модель в бакет S3:

```bash
!
wget
<
model-address
>
-O
<
buсket-address
>
```

Где:

- <model-address> — адрес модели в репозитории Hugging Face.
- <buсket-address> — адрес бакета в Object Storage.

<model-address> — адрес модели в репозитории Hugging Face.

<buсket-address> — адрес бакета в Object Storage.

Пример:

```bash
!
wget https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/resolve/main/v1-5-pruned-emaonly-fp16.safetensors
\
-O
/mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors
```

Создайте символическую ссылку для доступа к модели из ComfyUI:

```bash
!
ln
-s
/mnt/s3/ntbbckt/comfy_models/v1-5-pruned-emaonly-fp16.safetensors
\
/comfyui/models/checkpoints/v1-5-pruned-emaonly-fp16.safetensors
```

## 3. Сгенерируйте изображение в ComfyUI

1. Перейдите в модуль Comfy UI.
2. В правом верхнем углу откройте шаблоны Рабочий процесс → Посмотреть шаблоны.
3. Выберите шаблон Генерация изображений.

Интерфейс ComfyUI состоит из нод, которые соединены между собой в единый рабочий процесс.
Ноды отвечают за разные этапы генерации изображения.
Например, промпт для генерации необходимо ввести в поле ноды Кодирование текста CLIP (Запрос).
4. В поле ноды Кодирование текста CLIP (Запрос) укажите текстовый промпт для генерации изображения.
Пример позитивного промпта:
a highly detailed futuristic humanoid robot3/4 viewstanding in a thoughtful pose while solving a complex problemintricate mechanical partsglowing blue circuitry and transparent alloy panelsexpressive LED eyes reflecting data streamsultra realistic skin like polymer texturesubtle steam and dust particles around the jointssoft cinematic rim lightingdepth of field focusing on the robot’s facebackground: a sprawling megacity of the future with towering neon lit skyscrapersfloating traffic lanesholographic billboardsmisty evening atmosphereneon pink and cyan color palettehyper realisticphotorealisticultra detailed8kaward winning concept arttrending on ArtStation

Пример негативного промпта:
low resblurryjpeg artifactswatermarktextlogocroppingdeformed handsextra limbsuglypoorly drawnunrealistic anatomyover exposedunderexposedflat lighting
5. При необходимости скорректируйте параметры в других нодах.
6. Нажмите Запустить.
Запустится процесс генерации изображения.
Если процесс не запустился, обновите страницу и повторите попытку.
Сгенерированное изображение появится в блоке Save Image и будет сохранено в директории /comfyui/output.

Перейдите в модуль Comfy UI.

В правом верхнем углу откройте шаблоны Рабочий процесс → Посмотреть шаблоны.

Выберите шаблон Генерация изображений.

![../_images/s__gen-image-comfui.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__gen-image-comfui.png)

Интерфейс ComfyUI состоит из нод, которые соединены между собой в единый рабочий процесс.
Ноды отвечают за разные этапы генерации изображения.
Например, промпт для генерации необходимо ввести в поле ноды Кодирование текста CLIP (Запрос).

![../_images/s__nodes-comfui.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__nodes-comfui.png)

В поле ноды Кодирование текста CLIP (Запрос) укажите текстовый промпт для генерации изображения.

Пример позитивного промпта:

```bash
a highly detailed futuristic humanoid robot
3
/4 view
standing
in
a thoughtful pose
while
solving a complex problem
intricate mechanical parts
glowing blue circuitry and transparent alloy panels
expressive LED eyes reflecting data streams
ultra realistic skin like polymer texture
subtle steam and dust particles around the joints
soft cinematic rim lighting
depth of field focusing on the robot’s face
background: a sprawling megacity of the future with towering neon lit skyscrapers
floating traffic lanes
holographic billboards
misty evening atmosphere
neon pink and cyan color palette
hyper realistic
photorealistic
ultra detailed
8k
award winning concept art
trending on ArtStation
```

Пример негативного промпта:

```bash
low res
blurry
jpeg artifacts
watermark
text
logo
cropping
deformed hands
extra limbs
ugly
poorly drawn
unrealistic anatomy
over exposed
underexposed
flat lighting
```

При необходимости скорректируйте параметры в других нодах.

Нажмите Запустить.

Запустится процесс генерации изображения.
Если процесс не запустился, обновите страницу и повторите попытку.

Сгенерированное изображение появится в блоке Save Image и будет сохранено в директории /comfyui/output.

## Результат

В результате выполнения практической работы вы запустили Notebooks с визуальной средой для запуска генеративных нейронных сетей ComfyUI, подключили объектное хранилище для хранения моделей и сгенерировали первое изображение.

Далее вы можете эксперементировать с другими моделями, добавлять ноды и усложнять рабочий процесс.
Подробную информацию о работе с ComfyUI можно узнать [в официальной документации](https://docs.comfy.org/)в официальной документации.
