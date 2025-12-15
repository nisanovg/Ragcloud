---
title: Развертывание Deployment с вертикальным масштабированием подов
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__vpa
topic: containers
---
# Развертывание Deployment с вертикальным масштабированием подов

В сценарии развернем Deployment с тремя подами, каждый из которых запускает контейнер с nginx.
В Deployment укажем:

- запросы на лимиты — 500m CPU и 1 ГиБ памяти;
- запросы на ресурсы — 150m CPU и 100 МиБ памяти.

запросы на лимиты — 500m CPU и 1 ГиБ памяти;

запросы на ресурсы — 150m CPU и 100 МиБ памяти.

Далее создадим объект VerticalPodAutoscaler с режимом Auto.

## Перед началом работы

1. [Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes и хотя бы одну [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.
2. [Установите плагины Metrics Server и Vertical Pod Autoscaler](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)Установите плагины Metrics Server и Vertical Pod Autoscaler.
3. [Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

[Создайте кластер Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер Managed Kubernetes и хотя бы одну [группу узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)группу узлов.

[Установите плагины Metrics Server и Vertical Pod Autoscaler](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__addons__add)Установите плагины Metrics Server и Vertical Pod Autoscaler.

[Подключитесь к кластеру Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__connect)Подключитесь к кластеру Managed Kubernetes.

## Шаг 1. Создайте Deployment

1. Создайте файл cloudru-nginx.yaml и скопируйте следующую спецификацию:
apiVersion: apps/v1kind: Deploymentmetadata: name: cloudru-nginxspec: replicas: 3 selector: matchLabels: app: cloudru-nginx template: metadata: labels: app: cloudru-nginx spec: containers: - name: cloudru-nginx image: mk8s.registry.smk.sbercloud.dev/nginx:latest resources: limits: cpu: 500m memory: 1Gi requests: cpu: 150m memory: 100Mi command: ["/bin/sh"] args: ["-c", "while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done"]
2. Выполните команду:
kubectl create -f cloudru-nginx.yaml

Если команда выполнена успешно, появится сообщение:
deployment.apps/cloudru-nginx created
3. Подождите несколько минут, а затем посмотрите информацию о запущенных подах:
kubectl get pods -l app=cloudru-nginx

Результат должен выглядеть примерно так:
NAME READY STATUS RESTARTS AGEcloudru-nginx-435634s132-jwr37 1/1 Running 0 6m21scloudru-nginx-435634s132-frn21 1/1 Running 0 5m09scloudru-nginx-435634s132-qsj79 1/1 Running 0 3m44s
4. Получите подробную информацию об одном из подов:
kubectl describe pod <pod_name>

Вместо <pod_name> укажите название любого пода из результата предыдущей команды.
Результат должен выглядеть примерно так:
...
 cloudru-nginx: Container ID: containerd://... Image: mk8s.registry.smk.sbercloud.dev/nginx:latest Image ID: sha256: Port: <none> Host Port: <none> Command: /bin/sh Args: -c while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done State: Running Started: Wed, 14 Aug 2024 10:19:12 -0400 Ready: True Restart Count: 0 Limits: cpu: 500m memory: 1Gi Requests: cpu: 150m memory: 100Mi Environment: <none>
...

Установлены лимиты: CPU — 500m и RAM — 1 ГиБ и запросы на ресурсы: CPU — 150m и RAM — 100 МиБ.

Создайте файл cloudru-nginx.yaml и скопируйте следующую спецификацию:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
name: cloudru-nginx
spec:
replicas:
3
selector:
matchLabels:
app: cloudru-nginx
template:
metadata:
labels:
app: cloudru-nginx
spec:
containers:
- name: cloudru-nginx
image: mk8s.registry.smk.sbercloud.dev/nginx:latest
resources:
limits:
cpu: 500m
memory: 1Gi
requests:
cpu: 150m
memory: 100Mi
command:
[
"/bin/sh"
]
args:
[
"-c"
,
"while true; do timeout 0.5s yes >/dev/null; sleep 0.5s; done"
]
```

Выполните команду:

```bash
kubectl create
-f
cloudru-nginx.yaml
```

Если команда выполнена успешно, появится сообщение:

```bash
deployment.apps/cloudru-nginx created
```

Подождите несколько минут, а затем посмотрите информацию о запущенных подах:

```bash
kubectl get pods
-l
app
=
cloudru-nginx
```

Результат должен выглядеть примерно так:

```bash
NAME READY STATUS RESTARTS AGE
cloudru-nginx-435634s132-jwr37
1
/1 Running
0
6m21s
cloudru-nginx-435634s132-frn21
1
/1 Running
0
5m09s
cloudru-nginx-435634s132-qsj79
1
/1 Running
0
3m44s
```

Получите подробную информацию об одном из подов:

```bash
kubectl describe pod
<
pod_name
>
```

Вместо <pod_name> укажите название любого пода из результата предыдущей команды.

Результат должен выглядеть примерно так:

```bash
..
.
cloudru-nginx:
Container ID: containerd://
..
.
Image: mk8s.registry.smk.sbercloud.dev/nginx:latest
Image ID: sha256:
Port:
<
none
>
Host Port:
<
none
>
Command:
/bin/sh
Args:
-c
while
true
;
do
timeout
0
.5s
yes
>
/dev/null
;
sleep
0
.5s
;
done
State: Running
Started: Wed,
14
Aug
2024
10
:19:12
-0400
Ready: True
Restart Count:
0
Limits:
cpu: 500m
memory: 1Gi
Requests:
cpu: 150m
memory: 100Mi
Environment:
<
none
>
..
.
```

Установлены лимиты: CPU — 500m и RAM — 1 ГиБ и запросы на ресурсы: CPU — 150m и RAM — 100 МиБ.

## Шаг 2. Создайте Vertical Pod Autoscaler

1. Создайте файл cloudru-vpa.yaml и сохраните следующую спецификацию:
apiVersion: autoscaling.k8s.io/v1kind: VerticalPodAutoscalermetadata: name: cloudru-vpaspec: targetRef: apiVersion: "apps/v1" kind: Deployment name: cloudru-nginx updatePolicy: updateMode: "Auto"

Где:

spec.targetRef.name — название Deployment, для которого будет выполняться вертикальное автомасштабирование.
spec.updatePolicy.updateMode — режим обновления запросов на ресурсы.
2. Выполните команду:
kubectl create -f cloudru-vpa.yaml

В результате будет создан объект Vertical Pod Autoscaler для Deployment cloudru-nginx.
3. Подождите несколько минут, пока cloudru-vpa пересоздаст поды.
Вы можете отслеживать создание новых подов.
Для этого в терминале, отличном от терминала, на котором вы выполняли предыдущий шаг, выполните команду:
kubectl get --watch Pods -l app=cloudru-nginx
4. Выполните команду:
kubectl describe pod <pod_name>

Где <pod_name> — название нового пода.
Результат должен выглядеть примерно так:
...
State: Running Started: Wed, 14 Aug 2024 10:21:22 -0400Ready: TrueRestart Count: 0Limits: cpu: 1166m memory: 2560MiRequests: cpu: 350m memory: 262144kEnvironment: <none>...

Мы видим, что VPA изменил:

лимиты: CPU — 1166m и RAM — 2560 МиБ;
запросы на ресурсы: CPU — 350m и RAM — 262144 КиБ.

Создайте файл cloudru-vpa.yaml и сохраните следующую спецификацию:

```bash
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
name: cloudru-vpa
spec:
targetRef:
apiVersion:
"apps/v1"
kind: Deployment
name: cloudru-nginx
updatePolicy:
updateMode:
"Auto"
```

Где:

- spec.targetRef.name — название Deployment, для которого будет выполняться вертикальное автомасштабирование.
- spec.updatePolicy.updateMode — режим обновления запросов на ресурсы.

spec.targetRef.name — название Deployment, для которого будет выполняться вертикальное автомасштабирование.

spec.updatePolicy.updateMode — режим обновления запросов на ресурсы.

Выполните команду:

```bash
kubectl create
-f
cloudru-vpa.yaml
```

В результате будет создан объект Vertical Pod Autoscaler для Deployment cloudru-nginx.

Подождите несколько минут, пока cloudru-vpa пересоздаст поды.

Вы можете отслеживать создание новых подов.
Для этого в терминале, отличном от терминала, на котором вы выполняли предыдущий шаг, выполните команду:

```bash
kubectl get
--watch
Pods
-l
app
=
cloudru-nginx
```

Выполните команду:

```bash
kubectl describe pod
<
pod_name
>
```

Где <pod_name> — название нового пода.

Результат должен выглядеть примерно так:

```bash
..
.
State: Running
Started: Wed,
14
Aug
2024
10
:21:22
-0400
Ready: True
Restart Count:
0
Limits:
cpu: 1166m
memory: 2560Mi
Requests:
cpu: 350m
memory: 262144k
Environment:
<
none
>
..
.
```

Мы видим, что VPA изменил:

- лимиты: CPU — 1166m и RAM — 2560 МиБ;
- запросы на ресурсы: CPU — 350m и RAM — 262144 КиБ.

лимиты: CPU — 1166m и RAM — 2560 МиБ;

запросы на ресурсы: CPU — 350m и RAM — 262144 КиБ.

## Шаг 3. Удалите ресурсы

Если вы закончили работать с VPA, удалите созданные ресурсы.

1. Удалите cloudru-vpa:
kubectl delete vpa cloudru-vpa

При удалении VPA Deployment остается c существующими запросами.
2. Удалите Deployment:
kubectl delete deployment cloudru-nginx

Результат:
deployment.apps "cloudru-nginx" deleted

Поды удалятся вместе с Deployment.
3. Если необходимо, [удалите кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)удалите кластер.

Удалите cloudru-vpa:

```bash
kubectl delete vpa cloudru-vpa
```

При удалении VPA Deployment остается c существующими запросами.

Удалите Deployment:

```bash
kubectl delete deployment cloudru-nginx
```

Результат:

```bash
deployment.apps
"cloudru-nginx"
deleted
```

Поды удалятся вместе с Deployment.

Если необходимо, [удалите кластер](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__delete)удалите кластер.

[Вертикальное масштабирование подов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__vertical-pod-autoscaler)Вертикальное масштабирование подов
