---
title: Развертывание Deployment с горизонтальным масштабированием подов
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__hpa
topic: containers
---
# Развертывание Deployment с горизонтальным масштабированием подов

В сценарии развернем Deployment с Apache и PHP, а затем зададим условия изменения количества подов в зависимости от нагрузки на виртуальный процессор:

- Пороговая нагрузка на виртуальный процессор — 60% от запрошенного на запуск контейнера.
- Минимальное количество реплик — 2.
- Максимальное количество реплик — 7.

Пороговая нагрузка на виртуальный процессор — 60% от запрошенного на запуск контейнера.

Минимальное количество реплик — 2.

Максимальное количество реплик — 7.

## Перед началом работы

1. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes и хотя бы одну [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.
2. [Установите плагин Metrics Server](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)Установите плагин Metrics Server.
3. [Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes и хотя бы одну [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.

[Установите плагин Metrics Server](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)Установите плагин Metrics Server.

[Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

## Шаг 1. Создайте Deployment

Сохраните следующую спецификацию в файл cloudru-php-apache.yaml:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
name: cloudru-php-apache
namespace: default
spec:
replicas:
3
selector:
matchLabels:
run: cloudru-php-apache
template:
metadata:
labels:
run: cloudru-php-apache
spec:
containers:
- name: hpa-example
image: mk8s.registry.smk.sbercloud.dev/hpa-example
ports:
- containerPort:
80
resources:
requests:
cpu:
"250m"
---
apiVersion: v1
kind: Service
metadata:
name: cloudru-php-apache
labels:
run: cloudru-php-apache
spec:
ports:
- port:
80
selector:
run: cloudru-php-apache
```

Обязательно укажите параметр resources.requests.cpu — запрос CPU для запуска контейнера, чтобы выполнять автоматическое масштабирование на основе использования ресурса в процентах.

Выполните команду:

```bash
kubectl create
-f
cloudru-php-apache.yaml
```

Если команда выполнена успешно, появится сообщение:

```bash
deployment.apps/cloudru-php-apache created
```

## Шаг 2. Создайте Horizontal Pod Autoscaler одним из способов

Сохраните следующую спецификацию в файл cloudru-hpa.yaml:

```bash
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
name: cloudru-hpa
spec:
scaleTargetRef:
apiVersion: apps/v1
kind: Deployment
name: cloudru-php-apache
minReplicas:
2
maxReplicas:
7
targetCPUUtilizationPercentage:
60
```

Затем выполните команду:

```bash
kubectl create
-f
cloudru-hpa.yaml
```

Выполните команду:

```bash
kubectl autoscale deployment cloudru-php-apache --cpu-percent
=
60
--min
=
2
--max
=
7
```

В результате будет создан Horizontal Pod Autoscaler для Deployment cloudru-php-apache.

При нагрузке на виртуальный процессор:

- выше 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно увеличиваться, пока не достигнет семи;
- ниже 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно уменьшаться, пока не достигнет двух.

выше 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно увеличиваться, пока не достигнет семи;

ниже 60% от запрошенной нагрузки на каждый контейнер — количество подов будет постепенно уменьшаться, пока не достигнет двух.

Для горизонтального масштабирования подов можно использовать не только метрики CPU, но и RAM.
В этом случае для создания HPA используйте следующую спецификацию:

```bash
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
name: cloudru-php-apache
spec:
scaleTargetRef:
apiVersion: apps/v1
kind: Deployment
name: cloudru-php-apache
minReplicas:
2
maxReplicas:
7
metrics:
- type: Resource
resource:
name: cpu
target:
type: Utilization
averageUtilization:
60
- type: Resource
resource:
name: memory
target:
type: AverageValue
averageValue: 500Mi
```

При увеличении нагрузки на виртуальный процессор выше 60% от запрошенной нагрузки на каждый контейнер и занятой оперативной памяти более 500 МиБ, количество подов будет увеличиваться, пока не достигнет семи подов.

При уменьшении нагрузки на виртуальный процессор ниже 60% от запрошенной нагрузки на каждый контейнер и занятой оперативной памяти менее 500 МиБ, количество подов будет уменьшаться, пока не достигнет двух подов.

## Шаг 3. Получите список HPA в кластере

Выполните команду:

```bash
kubectl get hpa
```

Ответ будет содержать следующее:

```bash
NAME REFERENCE TARGETS MINPODS MAXPODS REPLICAS AGE
cloudru-php-apache Deployment/cloudru-php-apache
0
%/60%
2
7
3
121s
```

## Шаг 4. Создайте нагрузку для веб-сервера

Выполните команду:

```bash
kubectl run
-i
--tty
load-generator
--rm
--image
=
busybox
--restart
=
Never -- /bin/sh
-c
"while sleep 0.01; do wget -q -O- http://cloudru-php-apache; done"
```

Чтобы наблюдать за масштабированием, периодически запускайте следующую команду в терминале, отличном от терминала, на котором вы выполняли предыдущий шаг:

```bash
kubectl get hpa cloudru-php-apache
--watch
```

Ответ будет содержать следующее:

```bash
NAME REFERENCE TARGETS MINPODS MAXPODS REPLICAS AGE
cloudru-php-apache Deployment/cloudru-php-apache
200
%/60%
2
7
3
5m34s
```

Так как потребление процессора возросло до 200% от запрошенного, количество реплик было увеличено до 5:

```bash
NAME REFERENCE TARGETS MINPODS MAXPODS REPLICAS AGE
cloudru-php-apache Deployment/cloudru-php-apache
200
%/60%
2
7
5
7m
```

Увеличение количества подов может занять несколько минут.

## Шаг 5. Остановите нагрузку для веб-сервера

Чтобы завершить генерацию нагрузки, в терминале, где вы создали под, запускающий образ busybox, нажмите Ctrl + C.

Затем через несколько минут выполните команду:

```bash
kubectl get hpa cloudru-php-apache
--watch
```

Результат:

```bash
NAME REFERENCE TARGETS MINPODS MAXPODS REPLICAS AGE
cloudru-php-apache Deployment/cloudru-php-apache
0
%/60%
2
7
1
10m
```

## Шаг 6. Удалите ресурсы

Если вы закончили работать с HPA, удалите созданные ресурсы.

1. Удалите cloudru-hpa:
kubectl delete cloudru-hpa cloudru-php-apache

При удалении HPA Deployment остается в существующем масштабе и не возвращается к количеству реплик, указанному в исходной спецификации Deployment.
Если необходимо, измените количество реплик, например, до трех:
kubectl scale deployment cloudru-php-apache --replicas=3
2. Удалите Deployment:
kubectl delete deployment cloudru-php-apache

Результат:
deployment.apps "cloudru-php-apache" deleted

Поды удалятся вместе с Deployment.
3. Если необходимо, [удалите кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)удалите кластер.

Удалите cloudru-hpa:

```bash
kubectl delete cloudru-hpa cloudru-php-apache
```

При удалении HPA Deployment остается в существующем масштабе и не возвращается к количеству реплик, указанному в исходной спецификации Deployment.

Если необходимо, измените количество реплик, например, до трех:

```bash
kubectl scale deployment cloudru-php-apache
--replicas
=
3
```

Удалите Deployment:

```bash
kubectl delete deployment cloudru-php-apache
```

Результат:

```bash
deployment.apps
"cloudru-php-apache"
deleted
```

Поды удалятся вместе с Deployment.

Если необходимо, [удалите кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)удалите кластер.

[Горизонтальное масштабирование подов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__horizontal-pod-autoscaler)Горизонтальное масштабирование подов
