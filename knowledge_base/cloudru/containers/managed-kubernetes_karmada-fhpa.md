---
title: Автоматическое масштабирование nginx с FederatedHPA и нагрузочное тестирование с k6
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa
topic: containers
---
# Автоматическое масштабирование nginx с FederatedHPA и нагрузочное тестирование с k6

С помощью этого руководства вы реализуете автоматическое горизонтальное масштабирование приложения nginx в мультикластерной среде Karmada с помощью FederatedHPA и проведете нагрузочное тестирование с использованием инструмента k6.
Вы получите практические навыки работы с Federated Horizontal Pod Autoscaler, мониторинга метрик, а также анализа масштабирования приложений в Kubernetes кластерах под управлением Karmada.

Вы будете использовать следующие сервисы:

- [Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.
- [Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для подключения и управления кластерами Kubernetes.
- [Karmada](https://github.com/karmada-io/karmada)Karmada — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.
- [k6](https://k6.io/)k6 — инструмент для проведения нагрузочного тестирования приложений на основе JavaScript-скриптов.

[Managed Kubernetes](https://cloud.ru/docs/kubernetes-evolution/ug/index)Managed Kubernetes — сервис управления кластерами Kubernetes на вычислительных ресурсах облака.

[Виртуальные машины](https://cloud.ru/docs/virtual-machines/ug/index)Виртуальные машины — сервис, в рамках которого предоставляется виртуальная машина для подключения и управления кластерами Kubernetes.

[Karmada](https://github.com/karmada-io/karmada)Karmada — Kubernetes-совместимая платформа для централизованного управления и оркестрации приложений в мультикластерной инфраструктуре.

[k6](https://k6.io/)k6 — инструмент для проведения нагрузочного тестирования приложений на основе JavaScript-скриптов.

Шаги:

1. [Убедитесь, что Metrics Server установлен в кластерах-участниках](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Убедитесь, что Metrics Server установлен в кластерах-участниках
2. [Создайте FederatedHPA для nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Создайте FederatedHPA для nginx
3. [Разверните генератор нагрузки k6 и выполните нагрузочное тестирование](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Разверните генератор нагрузки k6 и выполните нагрузочное тестирование
4. [Проведите мониторинг процессов автомасштабирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Проведите мониторинг процессов автомасштабирования
5. [Выполните анализ результатов масштабирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Выполните анализ результатов масштабирования

[Убедитесь, что Metrics Server установлен в кластерах-участниках](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Убедитесь, что Metrics Server установлен в кластерах-участниках

[Создайте FederatedHPA для nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Создайте FederatedHPA для nginx

[Разверните генератор нагрузки k6 и выполните нагрузочное тестирование](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Разверните генератор нагрузки k6 и выполните нагрузочное тестирование

[Проведите мониторинг процессов автомасштабирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Проведите мониторинг процессов автомасштабирования

[Выполните анализ результатов масштабирования](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-fhpa)Выполните анализ результатов масштабирования

## Перед началом работы

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.
2. [Разверните Karmada](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Разверните Karmada и [разверните приложение nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__app-in-karmada)разверните приложение nginx в кластерах-участниках.
3. Убедитесь, что Karmada доступна через балансировщик нагрузки, кластеры-участники evo1 и evo2 подключены к Karmada, а приложение nginx запущено в обоих кластерах-участниках.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

[Разверните Karmada](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__karmada-deployment)Разверните Karmada и [разверните приложение nginx](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__app-in-karmada)разверните приложение nginx в кластерах-участниках.

Убедитесь, что Karmada доступна через балансировщик нагрузки, кластеры-участники evo1 и evo2 подключены к Karmada, а приложение nginx запущено в обоих кластерах-участниках.

## 1. Убедитесь, что Metrics Server установлен в кластерах-участниках

На этом шаге вы проверите наличие плагина Metrics Server для сбора метрик ресурсов в кластерах-участниках Karmada.
Metrics Server необходим для работы FederatedHPA, чтобы автоматизировать масштабирование на основе метрик CPU.

1. Проверьте, что плагин Metrics Server установлен в кластерах mk8s-evo1 и mk8s-evo2.
После создания кластера через сервис Managed Kubernetes, Metrics Server устанавливается по умолчанию.
2. Выполните команду для каждого кластера:
kubectl --kubeconfig=$HOME/join-clusters/evo1 get deployment metrics-server -n kube-systemkubectl --kubeconfig=$HOME/join-clusters/evo2 get deployment metrics-server -n kube-system
3. Если статус ресурса — «AVAILABLE», значит Metrics Server активен.

Проверьте, что плагин Metrics Server установлен в кластерах mk8s-evo1 и mk8s-evo2.
После создания кластера через сервис Managed Kubernetes, Metrics Server устанавливается по умолчанию.

Выполните команду для каждого кластера:

```bash
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 get deployment metrics-server
-n
kube-system
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo2 get deployment metrics-server
-n
kube-system
```

Если статус ресурса — «AVAILABLE», значит Metrics Server активен.

## 2. Создайте FederatedHPA для nginx

На этом шаге вы опишете и примените манифест FederatedHPA, который обеспечит автоматическое масштабирование развернутого nginx в обоих кластерах на основе нагрузки по CPU.

1. В директории nginx-manifests создайте манифест nginx-fhpa.yaml, который описывает ресурс FederatedHPA со следующими параметрами:
apiVersion: autoscaling.karmada.io/v1alpha1kind: FederatedHPAmetadata: name: nginx-fhpa namespace: defaultspec: scaleTargetRef: apiVersion: apps/v1 kind: Deployment name: nginx-deployment minReplicas: 1 maxReplicas: 10 metrics: - type: Resource resource: name: cpu target: type: Utilization averageUtilization: 30

Пояснение по параметрам:

scaleTargetRef — целевой ресурс для масштабирования (nginx-deployment).
minReplicas / maxReplicas — диапазон реплик от 1 до 10.
metrics — отслеживание утилизации CPU: при превышении 50% происходит масштабирование вверх, при меньшей утилизации — вниз.
2. Примените FederatedHPA к control plane Karmada:
karmadactl --karmada-context karmada-apiserver apply -f $HOME/nginx-manifests/nginx-fhpa.yaml
3. Убедитесь, что ресурс создан и активен, выполнив команду:
karmadactl --karmada-context karmada-apiserver get fhpa nginx-fhpa

Команда выводит актуальный статус FederatedHPA, включая количество реплик и значения метрик.
4. Получите подробное описание состояния ресурса и истории масштабирования:
karmadactl --karmada-context karmada-apiserver describe fhpa nginx-fhpa

Вывод содержит историю событий и текущие метрики автомасштабирования.

В директории nginx-manifests создайте манифест nginx-fhpa.yaml, который описывает ресурс FederatedHPA со следующими параметрами:

```bash
apiVersion: autoscaling.karmada.io/v1alpha1
kind: FederatedHPA
metadata:
name: nginx-fhpa
namespace: default
spec:
scaleTargetRef:
apiVersion: apps/v1
kind: Deployment
name: nginx-deployment
minReplicas:
1
maxReplicas:
10
metrics:
- type: Resource
resource:
name: cpu
target:
type: Utilization
averageUtilization:
30
```

Пояснение по параметрам:

- scaleTargetRef — целевой ресурс для масштабирования (nginx-deployment).
- minReplicas / maxReplicas — диапазон реплик от 1 до 10.
- metrics — отслеживание утилизации CPU: при превышении 50% происходит масштабирование вверх, при меньшей утилизации — вниз.

scaleTargetRef — целевой ресурс для масштабирования (nginx-deployment).

minReplicas / maxReplicas — диапазон реплик от 1 до 10.

metrics — отслеживание утилизации CPU: при превышении 50% происходит масштабирование вверх, при меньшей утилизации — вниз.

Примените FederatedHPA к control plane Karmada:

```bash
karmadactl --karmada-context karmada-apiserver apply
-f
$HOME
/nginx-manifests/nginx-fhpa.yaml
```

Убедитесь, что ресурс создан и активен, выполнив команду:

```bash
karmadactl --karmada-context karmada-apiserver get fhpa nginx-fhpa
```

Команда выводит актуальный статус FederatedHPA, включая количество реплик и значения метрик.

Получите подробное описание состояния ресурса и истории масштабирования:

```bash
karmadactl --karmada-context karmada-apiserver describe fhpa nginx-fhpa
```

Вывод содержит историю событий и текущие метрики автомасштабирования.

## 3. Разверните генератор нагрузки k6 и выполните нагрузочное тестирование

На этом этапе вы создадите JavaScript-скрипт для k6, развернете его в кластере evo1, опишете необходимые ресурсы и запустите нагрузочный тест для проверки масштабирования nginx.

1. Создайте директорию для скриптов:
mkdir -p $HOME/k6-manifests
2. Создайте JavaScript-скрипт load-test.js для нагрузочного тестирования nginx в директории k6-manifests:
import http from 'k6/http';import { check, sleep } from 'k6';export const options = {stages: [ { duration: '1m', target: 100 }, // Наращивание до 100 пользователей за 1 минуту { duration: '10m', target: 100 },],};export default function () {const response = http.get('http://nginx-service.default.svc.cluster.local');check(response, { 'статус 200': (r) => r.status === 200, 'время ответа < 500ms': (r) => r.timings.duration < 500,});sleep(0.1); // Пауза между запросами}

Скрипт задает:

stages — плавное наращивание нагрузки до 100 виртуальных пользователей;
target URL — внутренний адрес сервиса nginx;
check — проверки успешности ответа и времени отклика;
sleep — пауза между запросами для моделирования реального сценария нагрузки.
3. Создайте ConfigMap с тестовым скриптом:
kubectl --kubeconfig=$HOME/join-clusters/evo1 create configmap k6-load-test --from-file=$HOME/k6-manifests/load-test.js

ConfigMap позволяет подам k6 получать скрипт нагрузочного теста в процессе выполнения.
4. Создайте в директории k6-manifests манифест k6-deployment.yaml для запуска Job с k6:
apiVersion: batch/v1kind: Jobmetadata: name: k6-load-test namespace: defaultspec: parallelism: 2 template: metadata: labels: app: k6-load-test spec: restartPolicy: Never containers: - name: k6 image: grafana/k6:latest command: ["k6", "run", "/scripts/load-test.js"] volumeMounts: - mountPath: /scripts name: k6-script readOnly: true resources: requests: memory: "128Mi" cpu: "100m" limits: memory: "256Mi" cpu: "200m" volumes: - name: k6-script configMap: name: k6-load-test

Описание параметров:

parallelism: 2 — запуск двух параллельных экземпляров k6 для повышения нагрузки;
grafana/k6:latest — официальный контейнер k6;
volumeMounts — монтирование скрипта из ConfigMap;
resources — ограничения на использование CPU и памяти для стабильной работы тестов.
5. Примените манифест для запуска генератора нагрузки:
kubectl --kubeconfig=$HOME/join-clusters/evo1 apply -f $HOME/k6-manifests/k6-deployment.yaml
6. Проверьте статус k6-load-test и связанных подов:
kubectl --kubeconfig=$HOME/join-clusters/evo1 get jobs k6-load-testkubectl --kubeconfig=$HOME/join-clusters/evo1 get pods -l app=k6-load-test

Создайте директорию для скриптов:

```bash
mkdir
-p
$HOME
/k6-manifests
```

Создайте JavaScript-скрипт load-test.js для нагрузочного тестирования nginx в директории k6-manifests:

```bash
import
http from
'k6/http'
;
import
{
check,
sleep
}
from
'k6'
;
export
const options
=
{
stages:
[
{
duration:
'1m'
, target:
100
}
, // Наращивание до
100
пользователей за
1
минуту
{
duration:
'10m'
, target:
100
}
,
]
,
}
;
export
default
function
(
)
{
const response
=
http.get
(
'http://nginx-service.default.svc.cluster.local'
)
;
check
(
response,
{
'статус 200'
:
(
r
)
=
>
r.status
==
=
200
,
'время ответа < 500ms'
:
(
r
)
=
>
r.timings.duration
<
500
,
}
)
;
sleep
(
0.1
)
;
// Пауза между запросами
}
```

Скрипт задает:

- stages — плавное наращивание нагрузки до 100 виртуальных пользователей;
- target URL — внутренний адрес сервиса nginx;
- check — проверки успешности ответа и времени отклика;
- sleep — пауза между запросами для моделирования реального сценария нагрузки.

stages — плавное наращивание нагрузки до 100 виртуальных пользователей;

target URL — внутренний адрес сервиса nginx;

check — проверки успешности ответа и времени отклика;

sleep — пауза между запросами для моделирования реального сценария нагрузки.

Создайте ConfigMap с тестовым скриптом:

```bash
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 create configmap k6-load-test --from-file
=
$HOME
/k6-manifests/load-test.js
```

ConfigMap позволяет подам k6 получать скрипт нагрузочного теста в процессе выполнения.

Создайте в директории k6-manifests манифест k6-deployment.yaml для запуска Job с k6:

```bash
apiVersion: batch/v1
kind: Job
metadata:
name: k6-load-test
namespace: default
spec:
parallelism:
2
template:
metadata:
labels:
app: k6-load-test
spec:
restartPolicy: Never
containers:
- name: k6
image: grafana/k6:latest
command:
[
"k6"
,
"run"
,
"/scripts/load-test.js"
]
volumeMounts:
- mountPath: /scripts
name: k6-script
readOnly:
true
resources:
requests:
memory:
"128Mi"
cpu:
"100m"
limits:
memory:
"256Mi"
cpu:
"200m"
volumes:
- name: k6-script
configMap:
name: k6-load-test
```

Описание параметров:

- parallelism: 2 — запуск двух параллельных экземпляров k6 для повышения нагрузки;
- grafana/k6:latest — официальный контейнер k6;
- volumeMounts — монтирование скрипта из ConfigMap;
- resources — ограничения на использование CPU и памяти для стабильной работы тестов.

parallelism: 2 — запуск двух параллельных экземпляров k6 для повышения нагрузки;

grafana/k6:latest — официальный контейнер k6;

volumeMounts — монтирование скрипта из ConfigMap;

resources — ограничения на использование CPU и памяти для стабильной работы тестов.

Примените манифест для запуска генератора нагрузки:

```bash
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 apply
-f
$HOME
/k6-manifests/k6-deployment.yaml
```

Проверьте статус k6-load-test и связанных подов:

```bash
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 get
jobs
k6-load-test
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 get pods
-l
app
=
k6-load-test
```

## 4. Проведите мониторинг процессов автомасштабирования

На этом шаге вы будете отслеживать метрики и состояние масштабирования nginx в кластерах с помощью инструментов мониторинга Kubernetes и командной строки.

1. Наблюдайте за утилизацией CPU подами nginx в обоих кластерах:
watch -n 10 "echo '=== CPU утилизация подов nginx в evo1 ===' && kubectl --kubeconfig=$HOME/join-clusters/evo1 top pods -l app=nginx && echo '' && echo '=== CPU утилизация подов nginx в evo2 ===' && kubectl --kubeconfig=$HOME/join-clusters/evo2 top pods -l app=nginx"

Команда watch обновляет данные по метрикам каждые 10 секунд, позволяя наблюдать динамику использования ресурсов в реальном времени.
2. Откройте еще одну сессию SSH с ВМ.
Запустите отслеживание статус FederatedHPA:
watch -n 15 "karmadactl --karmada-context karmada-apiserver get fhpa nginx-fhpa"

Вы увидите, как FederatedHPA реагирует на изменение нагрузки и корректирует количество реплик в кластерах-участниках.
3. Откройте еще одну сессию SSH с ВМ. Запустите отслеживание количествf подов nginx:
watch -n 10 "echo '=== Поды nginx в кластере evo1 ===' && kubectl --kubeconfig=$HOME/join-clusters/evo1 get pods -l app=nginx && echo '' && echo '=== Поды nginx в кластере evo2 ===' && kubectl --kubeconfig=$HOME/join-clusters/evo2 get pods -l app=nginx"

Вы увидите, как масштабирование влияет на количество запущенных подов в каждом кластере.

Наблюдайте за утилизацией CPU подами nginx в обоих кластерах:

```bash
watch
-n
10
"echo '=== CPU утилизация подов nginx в evo1 ===' && kubectl --kubeconfig=
$HOME
/join-clusters/evo1 top pods -l app=nginx && echo '' && echo '=== CPU утилизация подов nginx в evo2 ===' && kubectl --kubeconfig=
$HOME
/join-clusters/evo2 top pods -l app=nginx"
```

Команда watch обновляет данные по метрикам каждые 10 секунд, позволяя наблюдать динамику использования ресурсов в реальном времени.

Откройте еще одну сессию SSH с ВМ.
Запустите отслеживание статус FederatedHPA:

```bash
watch
-n
15
"karmadactl --karmada-context karmada-apiserver get fhpa nginx-fhpa"
```

Вы увидите, как FederatedHPA реагирует на изменение нагрузки и корректирует количество реплик в кластерах-участниках.

Откройте еще одну сессию SSH с ВМ. Запустите отслеживание количествf подов nginx:

```bash
watch
-n
10
"echo '=== Поды nginx в кластере evo1 ===' && kubectl --kubeconfig=
$HOME
/join-clusters/evo1 get pods -l app=nginx && echo '' && echo '=== Поды nginx в кластере evo2 ===' && kubectl --kubeconfig=
$HOME
/join-clusters/evo2 get pods -l app=nginx"
```

Вы увидите, как масштабирование влияет на количество запущенных подов в каждом кластере.

## 5. Выполните анализ результатов масштабирования

На завершающем шаге проанализируйте историю событий FederatedHPA, оцените распределение нагрузки между кластерами и отследите влияние масштабирования на использование ресурсов.

1. Получите подробную информацию о событиях FederatedHPA:
karmadactl --karmada-context karmada-apiserver describe fhpa nginx-fhpa

Введите команду, чтобы изучить историю событий масштабирования, включая причины и время изменения числа реплик.
2. Проверьте текущее распределение подов nginx по кластерам:
echo "Количество подов nginx в evo1:"kubectl --kubeconfig=$HOME/join-clusters/evo1 get pods -l app=nginx --no-headers | wc -l
echo "Количество подов nginx в evo2:"kubectl --kubeconfig=$HOME/join-clusters/evo2 get pods -l app=nginx --no-headers | wc -l

Получите подробную информацию о событиях FederatedHPA:

```bash
karmadactl --karmada-context karmada-apiserver describe fhpa nginx-fhpa
```

Введите команду, чтобы изучить историю событий масштабирования, включая причины и время изменения числа реплик.

Проверьте текущее распределение подов nginx по кластерам:

```bash
echo
"Количество подов nginx в evo1:"
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo1 get pods
-l
app
=
nginx --no-headers
|
wc
-l
echo
"Количество подов nginx в evo2:"
kubectl
--kubeconfig
=
$HOME
/join-clusters/evo2 get pods
-l
app
=
nginx --no-headers
|
wc
-l
```

## Результат

Вы реализовали автоматическое масштабирование nginx с помощью FederatedHPA в мультикластерной среде Karmada, научились генерировать нагрузку с помощью k6, отслеживать метрики и анализировать процессы масштабирования.
