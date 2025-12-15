---
title: Генерация видео с моделью Kandinsky 5.0 Video Lite в ComfyUI на основе Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky
topic: ai-factory
---
# Генерация видео с моделью Kandinsky 5.0 Video Lite в ComfyUI на основе Notebooks

С помощью этого руководства вы настроите среду для генерации видео в ComfyUI с использованием модели Kandinsky 5.0 Video Lite в сервисе Notebooks.

В результате вы получите практический опыт работы с визуальной средой ComfyUI, управлением моделями и генерацией видео в облаке Cloud.ru Evolution.

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

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Подготовьте среду.
2. [Загрузите модели Kandinsky 5.0 Video Lite](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Загрузите модели Kandinsky 5.0 Video Lite.
3. [Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Подготовьте среду.

[Загрузите модели Kandinsky 5.0 Video Lite](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Загрузите модели Kandinsky 5.0 Video Lite.

[Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.
3. Убедитесь, что для сервиса Notebooks установлена квота на GPU.
Для расширения квоты обратитесь в техническую поддержку.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

На верхней панели слева нажмите и убедитесь в том, что сервис Notebooks в разделе AI Factory подключен.
Если сервис Notebooks не подключен, оставьте заявку на подключение.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Убедитесь, что для сервиса Notebooks установлена квота на GPU.
Для расширения квоты обратитесь в техническую поддержку.

## 1. Подготовьте среду

На этом шаге вы создадите бакет для хранения моделей и ноутбук с GPU и предустановленным ComfyUI.
Это обеспечит стабильную и производительную среду для генерации видео.

1. Для хранения модели [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage.
2. [Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

Конфигурация — GPU.
Образ — Cloud.ru Jupyter ComfyUI Kandinsky 5 Video Lite.
Хранилища — укажите бакет, созданный ранее.

Для хранения модели [создайте бакет в Object Storage](https://cloud.ru/docs/s3e/ug/topics/guides__bucket-create)создайте бакет в Object Storage.

[Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/quickstart)Создайте ноутбук со следующими параметрами:

- Конфигурация — GPU.
- Образ — Cloud.ru Jupyter ComfyUI Kandinsky 5 Video Lite.
- Хранилища — укажите бакет, созданный ранее.

Конфигурация — GPU.

Образ — Cloud.ru Jupyter ComfyUI Kandinsky 5 Video Lite.

Хранилища — укажите бакет, созданный ранее.

## 2. Загрузите модели Kandinsky 5.0 Video Lite

На этом шаге вы загрузите компоненты модели Kandinsky 5.0 Video Lite в выбранное хранилище — либо в бакет Object Storage, либо локально в ноутбук.
Использование бакета позволяет сохранять модели между перезапусками ноутбука.

1. Откройте созданный ноутбук.
2. Запустите терминал.
3. Загрузите модель в бакет S3 или напрямую в ноутбук:
Загрузка модели в бакет Object StorageЗагрузка модели в ноутбукВыполните скрипт в терминале, предварительно указав название [вашего бакета](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)вашего бакета в <bucket_name>:
# Activate the base environmentconda activate base
# Set the path to the bucket, e.g. /mnt/s3/<BUCKET_NAME>/kandinsky/weightsexport K5_WEIGHTS_DIR="/mnt/s3/<bucket_name>/kandinsky/weights" COMFY_MODELS_DIR="/comfyui/models/diffusion_models/"
# Create directory and change into itmkdir -p $K5_WEIGHTS_DIR && cd $K5_WEIGHTS_DIR
# Download modelspython3 /comfyui/custom_nodes/kandinsky/download_models.py
# Create symbolic links for text_encoder (Qwen/Qwen2.5-VL-7B-Instruct)for file in model-0000{1..5}-of-00005.safetensors; do \ ln -fs "${K5_WEIGHTS_DIR}/text_encoder/${file}" "/comfyui/models/text_encoders/text_encoder/"; \done
# Create symbolic links for text_encoder2 (openai/clip-vit-large-patch14)for file in {"tf_model.h5","pytorch_model.bin","model.safetensors","flax_model.msgpack"}; \do \ ln -fs "${K5_WEIGHTS_DIR}/text_encoder2/${file}" "/comfyui/models/text_encoders/text_encoder2/"; \done
# Create symbolic link for VAE (hunyuanvideo-community/HunyuanVideo)ln -fs "${K5_WEIGHTS_DIR}/vae/diffusion_pytorch_model.safetensors" "/comfyui/models/vae/vae/"
# Create symbolic links for Kandinsky5Lite_T2V modelsln -fs "${K5_WEIGHTS_DIR}/model/kandinsky5lite_t2v_distilled16steps_5s.safetensors" $COMFY_MODELS_DIR && \ln -fs "${K5_WEIGHTS_DIR}/model/kandinsky5lite_t2v_sft_5s.safetensors" $COMFY_MODELS_DIR

Откройте созданный ноутбук.

Запустите терминал.

Загрузите модель в бакет S3 или напрямую в ноутбук:

Выполните скрипт в терминале, предварительно указав название [вашего бакета](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__comfyui-kandinsky)вашего бакета в <bucket_name>:

```bash
# Activate the base environment
conda activate base
# Set the path to the bucket, e.g. /mnt/s3/<BUCKET_NAME>/kandinsky/weights
export
K5_WEIGHTS_DIR
=
"/mnt/s3/<bucket_name>/kandinsky/weights"
COMFY_MODELS_DIR
=
"/comfyui/models/diffusion_models/"
# Create directory and change into it
mkdir
-p
$K5_WEIGHTS_DIR
&&
cd
$K5_WEIGHTS_DIR
# Download models
python3 /comfyui/custom_nodes/kandinsky/download_models.py
# Create symbolic links for text_encoder (Qwen/Qwen2.5-VL-7B-Instruct)
for
file
in
model-0000
{
1
..
5
}
-of-00005.safetensors
;
do
\
ln
-fs
"
${K5_WEIGHTS_DIR}
/text_encoder/
${file}
"
"/comfyui/models/text_encoders/text_encoder/"
;
\
done
# Create symbolic links for text_encoder2 (openai/clip-vit-large-patch14)
for
file
in
{
"tf_model.h5"
,
"pytorch_model.bin"
,
"model.safetensors"
,
"flax_model.msgpack"
}
;
\
do
\
ln
-fs
"
${K5_WEIGHTS_DIR}
/text_encoder2/
${file}
"
"/comfyui/models/text_encoders/text_encoder2/"
;
\
done
# Create symbolic link for VAE (hunyuanvideo-community/HunyuanVideo)
ln
-fs
"
${K5_WEIGHTS_DIR}
/vae/diffusion_pytorch_model.safetensors"
"/comfyui/models/vae/vae/"
# Create symbolic links for Kandinsky5Lite_T2V models
ln
-fs
"
${K5_WEIGHTS_DIR}
/model/kandinsky5lite_t2v_distilled16steps_5s.safetensors"
$COMFY_MODELS_DIR
&&
\
ln
-fs
"
${K5_WEIGHTS_DIR}
/model/kandinsky5lite_t2v_sft_5s.safetensors"
$COMFY_MODELS_DIR
```

## 3. Сгенерируйте видео с моделью Kandinsky 5.0 Video Lite в ComfyUI

На этом шаге вы запустите рабочий процесс генерации видео в ComfyUI, используя загруженные модели.
Вы сможете настроить промпты, запустить генерацию и получить результат.

1. В интерфейсе ноутбука перейдите в модуль Comfy UI.
2. В левом верхнем углу нажмите Рабочий процесс → Посмотреть шаблоны.
3. Выберите один из доступных шаблонов:

Kandinsky 5.0 T2V Lite SFT 5s — обеспечивает лучшее качество.
Kandinsky 5.0 T2V Lite distill 5s — работает в 6 раз быстрее с минимальной потерей качества.

Интерфейс ComfyUI состоит из нод, которые соединены между собой в единый рабочий процесс.
Ноды отвечают за разные этапы генерации изображений и видео.
4. В поле ноды expand_prompt введите на русском или английском языке текстовый промпт — описание сцены, которую хотите сгенерировать.
Чем детальнее описание, тем точнее результат.
Укажите объекты, действия, стиль, освещение.
Пример промпта:
A 1980s Soviet computing lab.Green glow fills the room from massive mainframes.A scientist in a white coat watches a monochrome monitor.In bold, flickering green letters, the words written and pulse at the center of the screen surrounded by blinking status lights and scrolling hex code.Reels spin.
5. В поле ноды Kandinsky5TextEncode укажите негативный промпт — элементы, которые нужно исключить из генерации.
Пример негативного промпта:
Static2D cartooncartoon2d animationpaintingsimagesworst qualitylow qualityuglydeformedwalking backwards
6. Нажмите Запустить.
Запустится процесс генерации видео.
Если процесс не запустился, обновите страницу и повторите попытку.
7. Дождитесь завершения генерации.

В интерфейсе ноутбука перейдите в модуль Comfy UI.

В левом верхнем углу нажмите Рабочий процесс → Посмотреть шаблоны.

Выберите один из доступных шаблонов:

- Kandinsky 5.0 T2V Lite SFT 5s — обеспечивает лучшее качество.
- Kandinsky 5.0 T2V Lite distill 5s — работает в 6 раз быстрее с минимальной потерей качества.

Kandinsky 5.0 T2V Lite SFT 5s — обеспечивает лучшее качество.

Kandinsky 5.0 T2V Lite distill 5s — работает в 6 раз быстрее с минимальной потерей качества.

![../_images/s__comfyui-kandinsky1.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__comfyui-kandinsky1.png)

Интерфейс ComfyUI состоит из нод, которые соединены между собой в единый рабочий процесс.
Ноды отвечают за разные этапы генерации изображений и видео.

![../_images/s__comfyui-kandinsky2.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__comfyui-kandinsky2.png)

В поле ноды expand_prompt введите на русском или английском языке текстовый промпт — описание сцены, которую хотите сгенерировать.

Чем детальнее описание, тем точнее результат.
Укажите объекты, действия, стиль, освещение.

Пример промпта:

```bash
A 1980s Soviet computing lab.
Green glow fills the room from massive mainframes.
A scientist
in
a white coat watches a monochrome monitor.
In bold, flickering green letters, the words written and pulse at the center of the
screen
surrounded by blinking status lights and scrolling hex code.
Reels spin.
```

В поле ноды Kandinsky5TextEncode укажите негативный промпт — элементы, которые нужно исключить из генерации.

Пример негативного промпта:

```bash
Static
2D cartoon
cartoon
2d animation
paintings
images
worst quality
low quality
ugly
deformed
walking backwards
```

Нажмите Запустить.

Запустится процесс генерации видео.
Если процесс не запустился, обновите страницу и повторите попытку.

Дождитесь завершения генерации.

Первый запуск может занимать больше времени из-за инициализации GPU и загрузки модели.
Последующие запуски будут быстрее.

Чтобы отслеживать процесс, в консоли отладки нажмите Переключить нижнюю панель.

![../_images/s__comfyui-kandinsky3.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__comfyui-kandinsky3.png)

Сгенерированное видео появится в ноде Cохранить анимированный WEBP и в очереди генерации.

![../_images/s__comfyui-kandinsky4.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__comfyui-kandinsky4.png)

Оригинал файла будет сохранен в директории /comfyui/output.

ComfyUI поддерживает очередь генерации.
Вы можете добавить несколько промптов подряд для непрерывной обработки.

Пример сгенерированного видео:

## Результат

В ходе практической работы вы:

- настроили среду в сервисе Notebooks;
- загрузили модель Kandinsky 5.0 Video Lite;
- освоили работу с ComfyUI;
- использовали GPU-ускорение;
- настроили хранение моделей в облаке;
- сгенерировали видео на основе текстового описания.

настроили среду в сервисе Notebooks;

загрузили модель Kandinsky 5.0 Video Lite;

освоили работу с ComfyUI;

использовали GPU-ускорение;

настроили хранение моделей в облаке;

сгенерировали видео на основе текстового описания.

Далее вы можете экспериментировать с другими версиями модели Kandinsky 5.0 Video Lite и менять параметры генерации.
Подробную информацию о модели Kandisnky 5 можно узнать [в официальном репозитории](https://github.com/ai-forever/Kandinsky-5)в официальном репозитории.
