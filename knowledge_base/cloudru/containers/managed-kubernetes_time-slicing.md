---
title: Настройка Time-Slicing GPU
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__time-slicing
topic: containers
---
# Настройка Time-Slicing GPU

NVIDIA GPU Operator поддерживает возможность настройки Time-Slicing — механизма виртуального разделения одной физической GPU между несколькими подами на уровне рабочего узла.

Например, если на узле установлена одна GPU V100, а в кластере есть пять подов, каждый из которых запрашивает всю GPU, то без использования Time-Slicing на узел будет назначен только один под.
Остальные останутся в статусе «Pending» из-за нехватки ресурсов.
При включении Time-Slicing ресурсы одной физической GPU делятся между пятью подами.

Таким образом, все пять подов смогут быть запущены на одном узле одновременно, несмотря на то, что физически доступна только одна GPU.

В сценарии настроим Time-Slicing, развернем пять реплик приложения, которое требует для своей работы GPU-ресурсов, проверим состояние подов и логи.

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.
3. В кластере [создайте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)создайте группу узлов с параметрами для GPU:

Графический процессор (GPU) — активно.
Модель GPU — GPU NVIDIA Tesla V100.
GPU — 1.
По умолчанию в Managed Kubernetes установлена нулевая квота на создание узлов с GPU. Чтобы запросить увеличение квоты, [обратитесь в техническую поддержку](https://cloud.ru/docs/overview/support/index)обратитесь в техническую поддержку.
4. [Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes.

В кластере [создайте группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)создайте группу узлов с параметрами для GPU:

1. Графический процессор (GPU) — активно.
2. Модель GPU — GPU NVIDIA Tesla V100.
3. GPU — 1.
По умолчанию в Managed Kubernetes установлена нулевая квота на создание узлов с GPU. Чтобы запросить увеличение квоты, [обратитесь в техническую поддержку](https://cloud.ru/docs/overview/support/index)обратитесь в техническую поддержку.

Графический процессор (GPU) — активно.

Модель GPU — GPU NVIDIA Tesla V100.

GPU — 1.

По умолчанию в Managed Kubernetes установлена нулевая квота на создание узлов с GPU. Чтобы запросить увеличение квоты, [обратитесь в техническую поддержку](https://cloud.ru/docs/overview/support/index)обратитесь в техническую поддержку.

[Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

## Шаг 1. Настройте Time-Slicing

1. Создайте пространство имен gpu-operator:
kubectl create ns gpu-operator
2. Перезапишите метку:
kubectl label --overwrite ns gpu-operator pod-security.kubernetes.io/enforce=privileged
3. Создайте файл cloudru-time-slicing.yaml со следующим содержимым:
apiVersion: v1kind: ConfigMapmetadata: name: time-slicing-config namespace: gpu-operatordata: tesla-v100: |- version: v1 sharing: timeSlicing: resources: - name: nvidia.com/gpu replicas: 5
4. Выполните команду:
kubectl apply -f cloudru-time-slicing.yaml

Результат:
configmap/time-slicing-config created
5. Проверьте статус:
kubectl get cm time-slicing-config -n gpu-operator

Результат:
NAME DATA AGEtime-slicing-config 1 114s

Создайте пространство имен gpu-operator:

```bash
kubectl create ns gpu
-
operator
```

Перезапишите метку:

```bash
kubectl label
-
-
overwrite ns gpu
-
operator pod
-
security.kubernetes.io/enforce=privileged
```

Создайте файл cloudru-time-slicing.yaml со следующим содержимым:

```bash
apiVersion
:
v1
kind
:
ConfigMap
metadata
:
name
:
time
-
slicing
-
config
namespace
:
gpu
-
operator
data
:
tesla-v100
:
|
-
version
:
v1
sharing
:
timeSlicing
:
resources
:
-
name
:
nvidia.com/gpu
replicas
:
5
```

Выполните команду:

```bash
kubectl apply
-
f cloudru
-
time
-
slicing.yaml
```

Результат:

```bash
configmap/time-slicing-config created
```

Проверьте статус:

```bash
kubectl get cm time
-
slicing
-
config
-
n gpu
-
operator
```

Результат:

```bash
NAME DATA AGE
time-slicing-config
1
114s
```

В дополнение к стандартным меткам, которые применяются к узлам после настройки Time-Slicing, для узла применяется метка:

```bash
nvidia.com/gpu.replicas
=
<
replicas-count
>
```

Здесь <replicas-count> указывает, сколько раз выделенный ресурс gpu может быть переподписан на узле.

Также по умолчанию модифицируется метка nvidia.com/gpu.product:

```bash
nvidia.com/gpu.product
=
<
product-name
>
-SHARED
```

Суффикс -SHARED помогает отличать узлы с поддержкой Time-Slicing.

## Шаг 2. Установите NVIDIA GPU Operator

1. [В личном кабинете](https://console.cloud.ru/)В личном кабинете перейдите в кластер, для которого создали группу узлов с GPU.
2. Перейдите в раздел Плагины и справа над списком установленных плагинов нажмите Добавить плагин.
3. Выберите NVIDIA GPU Operator.
4. Нажмите Установить.
5. В разделе Расширенная конфигурация → YAML укажите параметры:
devicePlugin: config: name: time-slicing-config default: tesla-v100
6. Нажмите Установить.

[В личном кабинете](https://console.cloud.ru/)В личном кабинете перейдите в кластер, для которого создали группу узлов с GPU.

Перейдите в раздел Плагины и справа над списком установленных плагинов нажмите Добавить плагин.

Выберите NVIDIA GPU Operator.

Нажмите Установить.

В разделе Расширенная конфигурация → YAML укажите параметры:

```bash
devicePlugin
:
config
:
name
:
time
-
slicing
-
config
default
:
tesla
-
v100
```

Нажмите Установить.

Дождитесь, когда состояние плагина изменится на «Установлен».

## Шаг 3. Протестируйте настройку Time-Slicing

1. Создайте файл cloudru-time-slicing-check.yaml со следующим содержимым:
apiVersion: apps/v1kind: Deploymentmetadata: name: cloudru-time-slicing-check labels: app: cloudru-time-slicing-checkspec: replicas: 5 selector: matchLabels: app: cloudru-time-slicing-check template: metadata: labels: app: cloudru-time-slicing-check spec: tolerations: - key: nvidia.com/gpu operator: Exists effect: NoSchedule hostPID: true containers: - name: cuda-sample-vector-add image: "nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04" command: ["/bin/bash", "-c", "--"] args: - while true; do /cuda-samples/vectorAdd; done resources: limits: nvidia.com/gpu: 1
2. Выполните команду:
kubectl apply -f cloudru-time-slicing-check.yaml

Результат:
deployment.apps/cloudru-time-slicing-check created
3. Проверьте, что все пять реплик в статусе «Running»:
kubectl get pods

Примерный результат:
NAME READY STATUS RESTARTS AGEcloudru-time-slicing-check-6dcc7495bc-6dt4k 1/1 Running 0 6m25scloudru-time-slicing-check-6dcc7495bc-7vdvw 1/1 Running 0 6m25scloudru-time-slicing-check-6dcc7495bc-g5xdr 1/1 Running 0 6m25scloudru-time-slicing-check-6dcc7495bc-txbd9 1/1 Running 0 6m25scloudru-time-slicing-check-6dcc7495bc-zxdx8 1/1 Running 0 6m25s
4. Посмотрите логи одного из подов:
kubectl logs deploy/cloudru-time-slicing-check

Примерный результат:
Found 5 pods, using pod/cloudru-time-slicing-check-6dcc7495bc-7vdvw[Vector addition of 50000 elements]Copy input data from the host memory to the CUDA deviceCUDA kernel launch with 196 blocks of 256 threadsCopy output data from the CUDA device to the host memoryTest PASSED...

Создайте файл cloudru-time-slicing-check.yaml со следующим содержимым:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
name: cloudru-time-slicing-check
labels:
app: cloudru-time-slicing-check
spec:
replicas:
5
selector:
matchLabels:
app: cloudru-time-slicing-check
template:
metadata:
labels:
app: cloudru-time-slicing-check
spec:
tolerations:
- key: nvidia.com/gpu
operator: Exists
effect: NoSchedule
hostPID:
true
containers:
- name: cuda-sample-vector-add
image:
"nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda11.7.1-ubuntu20.04"
command:
[
"/bin/bash"
,
"-c"
,
"--"
]
args:
-
while
true
;
do
/cuda-samples/vectorAdd
;
done
resources:
limits:
nvidia.com/gpu:
1
```

Выполните команду:

```bash
kubectl apply
-f
cloudru-time-slicing-check.yaml
```

Результат:

```bash
deployment.apps/cloudru-time-slicing-check created
```

Проверьте, что все пять реплик в статусе «Running»:

```bash
kubectl get pods
```

Примерный результат:

```bash
NAME READY STATUS RESTARTS AGE
cloudru-time-slicing-check-6dcc7495bc-6dt4k
1
/1 Running
0
6m25s
cloudru-time-slicing-check-6dcc7495bc-7vdvw
1
/1 Running
0
6m25s
cloudru-time-slicing-check-6dcc7495bc-g5xdr
1
/1 Running
0
6m25s
cloudru-time-slicing-check-6dcc7495bc-txbd9
1
/1 Running
0
6m25s
cloudru-time-slicing-check-6dcc7495bc-zxdx8
1
/1 Running
0
6m25s
```

Посмотрите логи одного из подов:

```bash
kubectl logs deploy/cloudru-time-slicing-check
```

Примерный результат:

```bash
Found
5
pods, using pod/cloudru-time-slicing-check-6dcc7495bc-7vdvw
[
Vector addition of
50000
elements
]
Copy input data from the
host
memory to the CUDA device
CUDA kernel launch with
196
blocks of
256
threads
Copy output data from the CUDA device to the
host
memory
Test PASSED
..
.
```

[Time-Slicing GPUs in Kubernetes](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html)Time-Slicing GPUs in Kubernetes
