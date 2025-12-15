---
title: Инференс на собственных изображениях с использованием модели CNN, обученной на MNIST, на основе Notebooks
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn
topic: ai-factory
---
# Инференс на собственных изображениях с использованием модели CNN, обученной на MNIST, на основе Notebooks

С помощью этого руководства вы выполните инференс на собственных изображениях с использованием простой сверточной нейронной сети (CNN), обученной на датасете MNIST.
Вы подготовите окружение, обучите модель и сохраните полученную модель для дальнейшего использования.
Это практическое руководство подходит для начинающих, интересующихся компьютерным зрением и машинным обучением.

Вы будете использовать следующие сервисы и библиотеки:

- [Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
- torch — основная библиотека для работы с нейронными сетями.
- torchvision — библиотека для работы с изображениями и наборами данных.
- matplotlib — библиотека для визуализации данных.
- SummaryWriter и torch.utils.tensorboard — инструменты для отслеживания и визуализации процесса обучения.

[Notebooks](https://cloud.ru/docs/notebooks/ug/index)Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.

torch — основная библиотека для работы с нейронными сетями.

torchvision — библиотека для работы с изображениями и наборами данных.

matplotlib — библиотека для визуализации данных.

SummaryWriter и torch.utils.tensorboard — инструменты для отслеживания и визуализации процесса обучения.

Шаги:

1. [Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Подготовьте среду.
2. [Обучите простую сверточную нейросеть (CNN) с нуля на датасете MNIST](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Обучите простую сверточную нейросеть (CNN) с нуля на датасете MNIST.
3. [Выполните инференс на собственных изображениях](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Выполните инференс на собственных изображениях.
4. [Сохраните модель для повторного использования](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Сохраните модель для повторного использования.

[Подготовьте среду](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Подготовьте среду.

[Обучите простую сверточную нейросеть (CNN) с нуля на датасете MNIST](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Обучите простую сверточную нейросеть (CNN) с нуля на датасете MNIST.

[Выполните инференс на собственных изображениях](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Выполните инференс на собственных изображениях.

[Сохраните модель для повторного использования](https://cloud.ru/docs/tutorials-evolution/list/topics/notebooks__cv-cnn)Сохраните модель для повторного использования.

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
4. Импортируйте библиотеки:
from torch import nn, optimfrom torchvision import datasetsfrom torch.utils.data import DataLoaderimport matplotlib.pyplot as pltfrom torch.utils.tensorboard import SummaryWriter

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

Импортируйте библиотеки:

```bash
from
torch
import
nn
,
optim
from
torchvision
import
datasets
from
torch
.
utils
.
data
import
DataLoader
import
matplotlib
.
pyplot
as
plt
from
torch
.
utils
.
tensorboard
import
SummaryWriter
```

## 2. Обучите простую сверточную нейросеть (CNN)

На этом шаге вы перейдете к практическому применению сверточных нейронных сетей (CNN) для решения задачи классификации изображений.
Мы будем использовать набор данных MNIST, который является классическим набором данных для задач машинного обучения и компьютерного зрения.

1. Выполните трансформацию данных для MNIST (одноканальные изображения):
transform = transforms.Compose([ transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,)),])

В результате мы выполнили трансформацию данных из набора MNIST для обучения модели.
Это нужно для того, чтобы привести данные к формату, который требуется для работы с моделью.
2. Загрузите датасеты MNIST:
train_dataset = datasets.MNIST(root='./mnist_data', train=True, download=True, transform=transform)test_dataset = datasets.MNIST(root='./mnist_data', train=False, download=True, transform=transform)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

В результате мы загрузили датасеты MNIST для обучения и тестирования модели сверточной нейронной сети (CNN).
Этот набор данных содержит изображения рукописных цифр от 0 до 9 и является одним из наиболее популярных наборов данных для задач классификации изображений.
3. Для создания эффективной модели сверточной нейронной сети (CNN) необходимо определить ее архитектуру.
В данном случае мы будем использовать архитектуру, похожую на ResNet, которая зарекомендовала себя как одна из наиболее эффективных для задач классификации изображений.
Определите архитектуру простой ResNet-like CNN:
class BasicBlock(nn.Module): def __init__(self, in_channels, out_channels, stride=1): super(BasicBlock, self).__init__() self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False) self.bn1 = nn.BatchNorm2d(out_channels) self.relu = nn.ReLU(inplace=True) self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False) self.bn2 = nn.BatchNorm2d(out_channels)
 self.downsample = None if stride != 1 or in_channels != out_channels: self.downsample = nn.Sequential( nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False), nn.BatchNorm2d(out_channels) )
 def forward(self, x): identity = x
 out = self.conv1(x) out = self.bn1(out) out = self.relu(out)
 out = self.conv2(out) out = self.bn2(out)
 if self.downsample is not None: identity = self.downsample(x)
 out += identity out = self.relu(out)
 return out
4. После определения архитектуры модели сверточной нейронной сети (CNN) необходимо выполнить ее инициализацию и настроить параметры для обучения.
Выполните инициализацию модели, настройте функцию потерь и оптимизатор:
model = MiniResNet().to(device)criterion = nn.CrossEntropyLoss()optimizer = optim.Adam(model.parameters(), lr=0.001)

В результате мы создали экземпляр модели MiniResNet, определили функцию потерь и выбрали оптимизатор, который будет использоваться для обновления весов модели в процессе обучения.
5. Для отслеживания процесса обучения модели и оценки его эффективности необходимо создать логгер, который будет записывать метрики, такие как потери и точность модели на обучающей и тестовой выборках.
Создайте логгер для записи метрик при обучении модели:
writer = SummaryWriter(log_dir='runs/mnist_experiment')
# For example, log the model graphwriter.add_graph(model, torch.randn(1, 1, 28, 28).to(device))# Number of training epochsepochs = 10
# Lists to store training and testing loss and accuracy valuestrain_losses = []test_losses = []train_accuracies = []test_accuracies = []
6. Проведите обучение модели и оцените точность:
for epoch in range(epochs): model.train() total_train_loss = 0 correct_train = 0 total_train = 0
 for images, labels in train_loader: images, labels = images.to(device), labels.to(device)
 outputs = model(images) loss = criterion(outputs, labels)
 optimizer.zero_grad() loss.backward() optimizer.step()
 total_train_loss += loss.item() _, predicted = outputs.max(1) correct_train += (predicted == labels).sum().item() total_train += labels.size(0)
 avg_train_loss = total_train_loss / len(train_loader) train_accuracy = correct_train / total_train
 train_losses.append(avg_train_loss) train_accuracies.append(train_accuracy)
 # Evaluation on the test set model.eval() # Set the model to evaluation mode total_test_loss = 0 correct_test = 0 # Number of correctly predicted samples total_test = 0 # Total number of samples
 with torch.no_grad(): for images, labels in test_loader: images, labels = images.to(device), labels.to(device)
 outputs = model(images) loss = criterion(outputs, labels)
 total_test_loss += loss.item() _, predicted = outputs.max(1) correct_test += (predicted == labels).sum().item() total_test += labels.size(0)
 avg_test_loss = total_test_loss / len(test_loader) test_accuracy = correct_test / total_test
 test_losses.append(avg_test_loss) test_accuracies.append(test_accuracy)
 # Log values to TensorBoard writer.add_scalar('Loss/Train', avg_train_loss, epoch) writer.add_scalar('Loss/Test', avg_test_loss, epoch) writer.add_scalar('Accuracy/Train', train_accuracy, epoch) writer.add_scalar('Accuracy/Test', test_accuracy, epoch)
 print(f"Эпоха [{epoch+1}/{epochs}] " f"Train Loss: {avg_train_loss:.4f}, Train Acc: {train_accuracy:.4f} " f"| Test Loss: {avg_test_loss:.4f}, Test Acc: {test_accuracy:.4f}")
# Close the SummaryWriter after training to free up resourceswriter.close()

В этом шаге мы перешли к непосредственному обучению модели на обучающей выборке и оценке ее точности.
Для корректной работы TensorBoard используйте расширение JupyterLab — tensorboard-pro.

Выполните трансформацию данных для MNIST (одноканальные изображения):

```bash
transform
=
transforms
.
Compose
(
[
transforms
.
ToTensor
(
)
,
transforms
.
Normalize
(
(
0.1307
,
)
,
(
0.3081
,
)
)
,
]
)
```

В результате мы выполнили трансформацию данных из набора MNIST для обучения модели.
Это нужно для того, чтобы привести данные к формату, который требуется для работы с моделью.

Загрузите датасеты MNIST:

```bash
train_dataset
=
datasets
.
MNIST
(
root
=
'./mnist_data'
,
train
=
True
,
download
=
True
,
transform
=
transform
)
test_dataset
=
datasets
.
MNIST
(
root
=
'./mnist_data'
,
train
=
False
,
download
=
True
,
transform
=
transform
)
train_loader
=
DataLoader
(
train_dataset
,
batch_size
=
64
,
shuffle
=
True
)
test_loader
=
DataLoader
(
test_dataset
,
batch_size
=
1000
,
shuffle
=
False
)
```

В результате мы загрузили датасеты MNIST для обучения и тестирования модели сверточной нейронной сети (CNN).
Этот набор данных содержит изображения рукописных цифр от 0 до 9 и является одним из наиболее популярных наборов данных для задач классификации изображений.

Для создания эффективной модели сверточной нейронной сети (CNN) необходимо определить ее архитектуру.
В данном случае мы будем использовать архитектуру, похожую на ResNet, которая зарекомендовала себя как одна из наиболее эффективных для задач классификации изображений.

Определите архитектуру простой ResNet-like CNN:

```bash
class
BasicBlock
(
nn
.
Module
)
:
def
__init__
(
self
,
in_channels
,
out_channels
,
stride
=
1
)
:
super
(
BasicBlock
,
self
)
.
__init__
(
)
self
.
conv1
=
nn
.
Conv2d
(
in_channels
,
out_channels
,
kernel_size
=
3
,
stride
=
stride
,
padding
=
1
,
bias
=
False
)
self
.
bn1
=
nn
.
BatchNorm2d
(
out_channels
)
self
.
relu
=
nn
.
ReLU
(
inplace
=
True
)
self
.
conv2
=
nn
.
Conv2d
(
out_channels
,
out_channels
,
kernel_size
=
3
,
stride
=
1
,
padding
=
1
,
bias
=
False
)
self
.
bn2
=
nn
.
BatchNorm2d
(
out_channels
)
self
.
downsample
=
None
if
stride
!=
1
or
in_channels
!=
out_channels
:
self
.
downsample
=
nn
.
Sequential
(
nn
.
Conv2d
(
in_channels
,
out_channels
,
kernel_size
=
1
,
stride
=
stride
,
bias
=
False
)
,
nn
.
BatchNorm2d
(
out_channels
)
)
def
forward
(
self
,
x
)
:
identity
=
x
out
=
self
.
conv1
(
x
)
out
=
self
.
bn1
(
out
)
out
=
self
.
relu
(
out
)
out
=
self
.
conv2
(
out
)
out
=
self
.
bn2
(
out
)
if
self
.
downsample
is
not
None
:
identity
=
self
.
downsample
(
x
)
out
+=
identity
out
=
self
.
relu
(
out
)
return
out
```

После определения архитектуры модели сверточной нейронной сети (CNN) необходимо выполнить ее инициализацию и настроить параметры для обучения.

Выполните инициализацию модели, настройте функцию потерь и оптимизатор:

```bash
model
=
MiniResNet
(
)
.
to
(
device
)
criterion
=
nn
.
CrossEntropyLoss
(
)
optimizer
=
optim
.
Adam
(
model
.
parameters
(
)
,
lr
=
0.001
)
```

В результате мы создали экземпляр модели MiniResNet, определили функцию потерь и выбрали оптимизатор, который будет использоваться для обновления весов модели в процессе обучения.

Для отслеживания процесса обучения модели и оценки его эффективности необходимо создать логгер, который будет записывать метрики, такие как потери и точность модели на обучающей и тестовой выборках.

Создайте логгер для записи метрик при обучении модели:

```bash
writer
=
SummaryWriter
(
log_dir
=
'runs/mnist_experiment'
)
# For example, log the model graph
writer
.
add_graph
(
model
,
torch
.
randn
(
1
,
1
,
28
,
28
)
.
to
(
device
)
)
# Number of training epochs
epochs
=
10
# Lists to store training and testing loss and accuracy values
train_losses
=
[
]
test_losses
=
[
]
train_accuracies
=
[
]
test_accuracies
=
[
]
```

Проведите обучение модели и оцените точность:

```bash
for
epoch
in
range
(
epochs
)
:
model
.
train
(
)
total_train_loss
=
0
correct_train
=
0
total_train
=
0
for
images
,
labels
in
train_loader
:
images
,
labels
=
images
.
to
(
device
)
,
labels
.
to
(
device
)
outputs
=
model
(
images
)
loss
=
criterion
(
outputs
,
labels
)
optimizer
.
zero_grad
(
)
loss
.
backward
(
)
optimizer
.
step
(
)
total_train_loss
+=
loss
.
item
(
)
_
,
predicted
=
outputs
.
max
(
1
)
correct_train
+=
(
predicted
==
labels
)
.
sum
(
)
.
item
(
)
total_train
+=
labels
.
size
(
0
)
avg_train_loss
=
total_train_loss
/
len
(
train_loader
)
train_accuracy
=
correct_train
/
total_train
train_losses
.
append
(
avg_train_loss
)
train_accuracies
.
append
(
train_accuracy
)
# Evaluation on the test set
model
.
eval
(
)
# Set the model to evaluation mode
total_test_loss
=
0
correct_test
=
0
# Number of correctly predicted samples
total_test
=
0
# Total number of samples
with
torch
.
no_grad
(
)
:
for
images
,
labels
in
test_loader
:
images
,
labels
=
images
.
to
(
device
)
,
labels
.
to
(
device
)
outputs
=
model
(
images
)
loss
=
criterion
(
outputs
,
labels
)
total_test_loss
+=
loss
.
item
(
)
_
,
predicted
=
outputs
.
max
(
1
)
correct_test
+=
(
predicted
==
labels
)
.
sum
(
)
.
item
(
)
total_test
+=
labels
.
size
(
0
)
avg_test_loss
=
total_test_loss
/
len
(
test_loader
)
test_accuracy
=
correct_test
/
total_test
test_losses
.
append
(
avg_test_loss
)
test_accuracies
.
append
(
test_accuracy
)
# Log values to TensorBoard
writer
.
add_scalar
(
'Loss/Train'
,
avg_train_loss
,
epoch
)
writer
.
add_scalar
(
'Loss/Test'
,
avg_test_loss
,
epoch
)
writer
.
add_scalar
(
'Accuracy/Train'
,
train_accuracy
,
epoch
)
writer
.
add_scalar
(
'Accuracy/Test'
,
test_accuracy
,
epoch
)
print
(
f"Эпоха [
{
epoch
+
1
}
/
{
epochs
}
] "
f"Train Loss:
{
avg_train_loss
:
.4f
}
, Train Acc:
{
train_accuracy
:
.4f
}
"
f"| Test Loss:
{
avg_test_loss
:
.4f
}
, Test Acc:
{
test_accuracy
:
.4f
}
"
)
# Close the SummaryWriter after training to free up resources
writer
.
close
(
)
```

В этом шаге мы перешли к непосредственному обучению модели на обучающей выборке и оценке ее точности.

Для корректной работы TensorBoard используйте расширение JupyterLab — tensorboard-pro.

## 3. Выполните инференс на собственных изображениях

После успешного обучения модели на наборе данных MNIST следующим шагом будет тестирование модели на новых данных.
На этом шаге мы рассмотрим процесс загрузки, преобразования и классификации собственных изображений с помощью обученной модели.

1. Загрузите изображение и преобразуйте его в нужный формат:
image_path = 'my_digit_3.jpg'
img = Image.open(image_path).convert('L').resize((28, 28))
2. После загрузки и преобразования изображения необходимо убедиться, что оно было правильно обработано и готово к классификации с помощью модели.
Посмотрите на загруженное изображение:
plt.imshow(img, cmap='gray')plt.show()
3. Перед тем как подавать загруженное изображение на вход обученной модели для классификации, необходимо выполнить его преобразование в формат, который использовался во время обучения модели.
Выполните преобразование изображения:
transform = transforms.Compose([ transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
input_tensor = transform(img).unsqueeze(0).to(device) # (1, 1, 28, 28)
4. После того как изображение было загружено, преобразовано и подготовлено к классификации, мы можем использовать обученную модель для выполнения инференса и получения предсказания.
Выполните инференс на подготовленном изображении:
model.eval()with torch.no_grad(): output = model(input_tensor) probabilities = torch.softmax(output, dim=1) predicted_class = probabilities.argmax(dim=1).item()
5. После того как модель классифицировала подготовленное изображение, необходимо получить и проанализировать результаты предсказания.
Получите результат предсказаний:
print(f"Модель предсказала цифру: {predicted_class}")
top3_prob, top3_classes = torch.topk(probabilities, 3)for i in range(3): print(f"{i+1}) Цифра {top3_classes[0][i].item()} с вероятностью {top3_prob[0][i].item():.4f}")

Загрузите изображение и преобразуйте его в нужный формат:

```bash
image_path
=
'my_digit_3.jpg'
img
=
Image
.
open
(
image_path
)
.
convert
(
'L'
)
.
resize
(
(
28
,
28
)
)
```

После загрузки и преобразования изображения необходимо убедиться, что оно было правильно обработано и готово к классификации с помощью модели.

Посмотрите на загруженное изображение:

```bash
plt
.
imshow
(
img
,
cmap
=
'gray'
)
plt
.
show
(
)
```

Перед тем как подавать загруженное изображение на вход обученной модели для классификации, необходимо выполнить его преобразование в формат, который использовался во время обучения модели.

Выполните преобразование изображения:

```bash
transform
=
transforms
.
Compose
(
[
transforms
.
ToTensor
(
)
,
transforms
.
Normalize
(
(
0.1307
,
)
,
(
0.3081
,
)
)
]
)
input_tensor
=
transform
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
# (1, 1, 28, 28)
```

После того как изображение было загружено, преобразовано и подготовлено к классификации, мы можем использовать обученную модель для выполнения инференса и получения предсказания.

Выполните инференс на подготовленном изображении:

```bash
model
.
eval
(
)
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
probabilities
=
torch
.
softmax
(
output
,
dim
=
1
)
predicted_class
=
probabilities
.
argmax
(
dim
=
1
)
.
item
(
)
```

После того как модель классифицировала подготовленное изображение, необходимо получить и проанализировать результаты предсказания.

Получите результат предсказаний:

```bash
print
(
f"Модель предсказала цифру:
{
predicted_class
}
"
)
top3_prob
,
top3_classes
=
torch
.
topk
(
probabilities
,
3
)
for
i
in
range
(
3
)
:
print
(
f"
{
i
+
1
}
) Цифра
{
top3_classes
[
0
]
[
i
]
.
item
(
)
}
с вероятностью
{
top3_prob
[
0
]
[
i
]
.
item
(
)
:
.4f
}
"
)
```

## 4. Сохраните модель для повторного использования

После сохранения, вы можете загрузить и использовать модель для классификации новых изображений без необходимости повторного обучения.

Сохраните модель для повторного использования:

```bash
model_path
=
"mini_resnet_mnist.pth"
torch
.
save
(
model
.
state_dict
(
)
,
model_path
)
print
(
f"Веса модели сохранены в
{
model_path
}
"
)
```

## Результат

В результате этой практической работы вы обучили простую сверточную нейронную сеть (CNN) на датасете MNIST с помощью PyTorch, а также научились отслеживать процесс обучения в TensorBoard.
Вы освоили процесс инференса модели на собственных изображениях, включая предобработку данных и интерпретацию результатов.
