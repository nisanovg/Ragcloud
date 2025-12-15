---
title: Инференс изображений на предобученой модели на основе Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain
topic: ai-factory
---
# Инференс изображений на предобученой модели на основе Notebooks

С помощью этого руководства вы проведете классификацию изображений с использованием предобученной модели ResNet18.
Вы создадите среду для работы с машинным обучением, загрузите и подготовите изображение, а также выполните инференс модели для получения топ-5 предсказаний.

Вы будете использовать следующие сервисы и библиотеки:

- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- torchvision — позволяет использовать предобученные модели, такие как ResNet18, и предоставляет инструменты для преобразования и обработки изображений.
- PIL — используется для работы с изображениями в формате PIL, включая их открытие, изменение размера и конвертацию.
- requests — позволяет загружать изображения и другие данные с веб-ресурсов по URL.
- BytesIO из модуля io — создает файлоподобный объект в памяти для работы с байтовыми данными, как с файлом, что удобно при обработке изображений из потока.
- json и urllib.request — библиотеки для загрузки, обработки и сериализации данных, например, при работе с веб-API или метаданными.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

torchvision — позволяет использовать предобученные модели, такие как ResNet18, и предоставляет инструменты для преобразования и обработки изображений.

PIL — используется для работы с изображениями в формате PIL, включая их открытие, изменение размера и конвертацию.

requests — позволяет загружать изображения и другие данные с веб-ресурсов по URL.

BytesIO из модуля io — создает файлоподобный объект в памяти для работы с байтовыми данными, как с файлом, что удобно при обработке изображений из потока.

json и urllib.request — библиотеки для загрузки, обработки и сериализации данных, например, при работе с веб-API или метаданными.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Подготовьте среду.
2. [Используйте предобученную модель для инференса](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Используйте предобученную модель для инференса.
3. [Подготовьте изображение и выведете топ-5 предсказаний](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Подготовьте изображение и выведете топ-5 предсказаний.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Подготовьте среду.

[Используйте предобученную модель для инференса](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Используйте предобученную модель для инференса.

[Подготовьте изображение и выведете топ-5 предсказаний](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-pretrain)Подготовьте изображение и выведете топ-5 предсказаний.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Подготовьте среду

1. [Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/guides__ntb-create)Создайте ноутбук на основе [образа](https://cloud.ru/docs/notebooks/ug/topics/concepts__ntb-libs-in-images)образа с поддержкой CUDA.
2. Установите PyTorch и torchvision:
pip install torchpip install torchvision

Подробнее об установке PyTorch [на официальном сайте](https://pytorch.org/get-started/locally)на официальном сайте.
3. Проверьте доступность GPU:
import torch
# Check GPU availabilitycuda_available = torch.cuda.is_available()print(f"CUDA доступен: {cuda_available}")
# If GPU is available, display the number of GPUs and the GPU nameif cuda_available: print(f"Количество доступных GPU: {torch.cuda.device_count()}") print(f"Название GPU: {torch.cuda.get_device_name(0)}") device = torch.device("cuda")else: print("Используется CPU") device = torch.device("cpu")
4. Импортируйте библиотеки для работы:
from torchvision import models, transformsfrom PIL import Imageimport requestsfrom io import BytesIOimport jsonimport urllib.request

[Создайте ноутбук](https://cloud.ru/docs/notebooks/ug/topics/guides__ntb-create)Создайте ноутбук на основе [образа](https://cloud.ru/docs/notebooks/ug/topics/concepts__ntb-libs-in-images)образа с поддержкой CUDA.

Установите PyTorch и torchvision:

```bash
pip install torch
pip install torchvision
```

Подробнее об установке PyTorch [на официальном сайте](https://pytorch.org/get-started/locally)на официальном сайте.

Проверьте доступность GPU:

```bash
import
torch
# Check GPU availability
cuda_available
=
torch
.
cuda
.
is_available
(
)
print
(
f"CUDA доступен:
{
cuda_available
}
"
)
# If GPU is available, display the number of GPUs and the GPU name
if
cuda_available
:
print
(
f"Количество доступных GPU:
{
torch
.
cuda
.
device_count
(
)
}
"
)
print
(
f"Название GPU:
{
torch
.
cuda
.
get_device_name
(
0
)
}
"
)
device
=
torch
.
device
(
"cuda"
)
else
:
print
(
"Используется CPU"
)
device
=
torch
.
device
(
"cpu"
)
```

Импортируйте библиотеки для работы:

```bash
from
torchvision
import
models
,
transforms
from
PIL
import
Image
import
requests
from
io
import
BytesIO
import
json
import
urllib
.
request
```

## 2. Используйте предобученную модель для инференса

На этом шаге вы будете использовать предобученную модель для инференса, то есть для классификации изображений.
Мы загрузим изображение из интернета и обработаем его с помощью модели ResNet18, которая уже обучена на большом наборе данных.

1. Загрузите изображение из интернета:
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlSaRKDvkuC2_Qyfnt8jMDmZzphQbIrz-TSg&s"response = requests.get(url)img = Image.open(BytesIO(response.content)).convert('RGB')

В результате мы получим объект изображения в формате RGB, готовый для дальнейшей обработки и анализа моделью.
2. Загрузите модель ResNet18 и переведите ее в режим инференса:
model = models.resnet18(pretrained=True)model = model.to(device)model.eval()

В результате мы загрузили модель, перевели ее в режим инференса и переместили на выбранное устройство GPU, если оно доступно, или CPU.
Это необходимо для того, чтобы модель была готова к обработке изображений и выдавала предсказания.

Загрузите изображение из интернета:

```bash
url
=
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlSaRKDvkuC2_Qyfnt8jMDmZzphQbIrz-TSg&s"
response
=
requests
.
get
(
url
)
img
=
Image
.
open
(
BytesIO
(
response
.
content
)
)
.
convert
(
'RGB'
)
```

В результате мы получим объект изображения в формате RGB, готовый для дальнейшей обработки и анализа моделью.

Загрузите модель ResNet18 и переведите ее в режим инференса:

```bash
model
=
models
.
resnet18
(
pretrained
=
True
)
model
=
model
.
to
(
device
)
model
.
eval
(
)
```

В результате мы загрузили модель, перевели ее в режим инференса и переместили на выбранное устройство GPU, если оно доступно, или CPU.
Это необходимо для того, чтобы модель была готова к обработке изображений и выдавала предсказания.

## 3. Подготовьте изображение и получите топ-5 предсказаний

1. Выполните преобразование изображения для инференса:
preprocess = transforms.Compose([ transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor()])

Перед тем как подавать изображение на вход модели, необходимо преобразовать его в нужный формат.
В данном случае мы применили три преобразования: изменение размера изображения до 256 пикселей, центрированный обрез до размера 224x224 пикселей и преобразование в tensor.
Это необходимо для того, чтобы изображение соответствовало требованиям модели и могло быть обработано корректно.
2. Загрузите имена классов:
url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"urllib.request.urlretrieve(url, "imagenet_classes.txt")
with open("imagenet_classes.txt") as f: class_names = [line.strip() for line in f.readlines()]

В результате мы загрузили файл с именами классов ImageNet, которые используются в предобученной модели ResNet18.
Это нужно для интерпретации результатов работы модели и понимания какие классы она может предсказывать.
3. Подготовьте изображение и выведите топ-5 предсказаний:
# Preprocess the imageinput_tensor = preprocess(img).unsqueeze(0).to(device)
# Perform inferencewith torch.no_grad(): output = model(input_tensor)
# Apply softmax to get probabilitiesprobabilities = torch.nn.functional.softmax(output[0], dim=0)
# Get the top-5 predictionstop5_prob, top5_idx = torch.topk(probabilities, 5)
# Print the top-5 predictionsprint("Топ-5 предсказаний:")for i in range(top5_prob.size(0)): class_name = class_names[top5_idx[i]] prob = top5_prob[i].item() print(f"{i+1}: {class_name} ({prob:.4f})")

В результате мы получили Топ-5 предсказаний:
Топ-5 предсказаний:1: tabby (0.5923)2: tiger cat (0.2160)3: Egyptian cat (0.1611)4: paper towel (0.0057)5: plastic bag (0.0037)

Выполните преобразование изображения для инференса:

```bash
preprocess
=
transforms
.
Compose
(
[
transforms
.
Resize
(
256
)
,
transforms
.
CenterCrop
(
224
)
,
transforms
.
ToTensor
(
)
]
)
```

Перед тем как подавать изображение на вход модели, необходимо преобразовать его в нужный формат.
В данном случае мы применили три преобразования: изменение размера изображения до 256 пикселей, центрированный обрез до размера 224x224 пикселей и преобразование в tensor.
Это необходимо для того, чтобы изображение соответствовало требованиям модели и могло быть обработано корректно.

Загрузите имена классов:

```bash
url
=
"https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
urllib
.
request
.
urlretrieve
(
url
,
"imagenet_classes.txt"
)
with
open
(
"imagenet_classes.txt"
)
as
f
:
class_names
=
[
line
.
strip
(
)
for
line
in
f
.
readlines
(
)
]
```

В результате мы загрузили файл с именами классов ImageNet, которые используются в предобученной модели ResNet18.
Это нужно для интерпретации результатов работы модели и понимания какие классы она может предсказывать.

Подготовьте изображение и выведите топ-5 предсказаний:

```bash
# Preprocess the image
input_tensor
=
preprocess
(
img
)
.
unsqueeze
(
0
)
.
to
(
device
)
# Perform inference
with
torch
.
no_grad
(
)
:
output
=
model
(
input_tensor
)
# Apply softmax to get probabilities
probabilities
=
torch
.
nn
.
functional
.
softmax
(
output
[
0
]
,
dim
=
0
)
# Get the top-5 predictions
top5_prob
,
top5_idx
=
torch
.
topk
(
probabilities
,
5
)
# Print the top-5 predictions
print
(
"Топ-5 предсказаний:"
)
for
i
in
range
(
top5_prob
.
size
(
0
)
)
:
class_name
=
class_names
[
top5_idx
[
i
]
]
prob
=
top5_prob
[
i
]
.
item
(
)
print
(
f"
{
i
+
1
}
:
{
class_name
}
(
{
prob
:
.4f
}
)"
)
```

В результате мы получили Топ-5 предсказаний:

```bash
Топ-5 предсказаний:
1
: tabby
(
0.5923
)
2
: tiger
cat
(
0.2160
)
3
: Egyptian
cat
(
0.1611
)
4
: paper towel
(
0.0057
)
5
: plastic bag
(
0.0037
)
```

## Результат

В ходе практической работы вы подготовили среду для работы с предобученной моделью ResNet18, загрузили и подготовили изображение, а также выполнили инференс модели для получения топ-5 предсказаний.
Этот подход позволяет быстро и эффективно классифицировать изображения без необходимости обучения модели с нуля.

Вы можете экспериментировать с разными изображениями и настройками, чтобы лучше понять, как работает модель, и улучшить ее производительность для ваших задач.
