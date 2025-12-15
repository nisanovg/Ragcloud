---
title: Настройка автомасштабирования группы узлов
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-kubernetes__automatic-scaling
topic: containers
---
# Настройка автомасштабирования группы узлов

В сценарии рассмотрим, как настраивать и управлять автомасштабированием через API:

1. Создадим группу узлов [с поддержкой автомасштабирования](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__cluster-autoscaler)с поддержкой автомасштабирования.
2. Отредактируем минимальное и максимальное количество узлов.
3. Изменим политику масштабирования на фиксированную.
4. Изменим политику масштабирования с фиксированной на автоматическую.

Создадим группу узлов [с поддержкой автомасштабирования](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__cluster-autoscaler)с поддержкой автомасштабирования.

Отредактируем минимальное и максимальное количество узлов.

Изменим политику масштабирования на фиксированную.

Изменим политику масштабирования с фиксированной на автоматическую.

## Перед началом работы

1. [Создайте кластер по инструкции](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер по инструкции.
2. Пройдите [аутентификацию в API](https://cloud.ru/docs/kubernetes-evolution/ug/topics/api-ref__authentication)аутентификацию в API.

[Создайте кластер по инструкции](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__create)Создайте кластер по инструкции.

Пройдите [аутентификацию в API](https://cloud.ru/docs/kubernetes-evolution/ug/topics/api-ref__authentication)аутентификацию в API.

## Создайте группу узлов с поддержкой автомасштабирования

Выполните HTTP-запрос:

```bash
POST https://mk8s.api.cloud.ru/v2/clusters/
{
clusterId
}
/node-pools
```

Где clusterId — [идентификатор кластера](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__cluster__get-info)идентификатор кластера, для которого нужно создать группу узлов.

В теле запроса передайте параметры:

```bash
{
"displayName"
:
"cloudru-node-pool-scale"
,
"scalePolicy"
:
{
"autoScale"
:
{
"minCount"
:
2
,
"maxCount"
:
5
,
"initialCount"
:
3
}
}
,
"machineConfiguration"
:
{
"diskSize"
:
10
,
"flavorId"
:
"1f38e57c-0004-4f44-badf-1a0f3c09a128"
}
,
"networkConfiguration"
:
{
"nodesSubnetCidr"
:
"10.0.0.0/24"
}
}
```

В примере вы можете использовать указанные значения параметров displayName, diskSize, nodesSubnetCidr или заменить их на свои.

В результате выполнения запроса будет создана группа узлов с тремя рабочими узлами.
Размер группы узлов может масштабироваться в зависимости от нагрузки от двух до пяти узлов.

## Отредактируйте параметры автомасштабирования

Выполните HTTP-запрос:

```bash
PATCH https://mk8s.api.cloud.ru/v2/node-pools/
{
nodePoolId
}
```

Где nodePoolId — идентификатор созданной группы узлов.

В теле запроса передайте параметры:

```bash
{
"data"
:
{
"scalePolicy"
:
{
"autoScale"
:
{
"minCount"
:
1
,
"maxCount"
:
6
}
}
}
}
```

Параметры масштабирования изменятся.
Теперь размер группы узлов может масштабироваться в зависимости от нагрузки от одного до шести узлов.

## Измените политику масштабирования на фиксированную

Выполните HTTP-запрос:

```bash
PATCH https://mk8s.api.cloud.ru/v2/node-pools/
{
nodePoolId
}
```

Где nodePoolId — идентификатор группы узлов.

В теле запроса передайте следующие параметры:

```bash
{
"data"
:
{
"scalePolicy"
:
{
"fixedScale"
:
{
"count"
:
4
}
}
}
}
```

В результате размер группы узлов будет постоянным.

## Измените политику масштабирования на автоматическую

Выполните HTTP-запрос:

```bash
PATCH https://mk8s.api.cloud.ru/v2/node-pools/
{
nodePoolId
}
```

В теле запроса передайте параметры:

```bash
{
"data"
:
{
"scalePolicy"
:
{
"autoScale"
:
{
"minCount"
:
0
,
"maxCount"
:
6
}
}
}
}
```

После выполнения запроса группа узлов будет состоять из четырех рабочих узлов.
Размер группы может масштабироваться в зависимости от нагрузки, уменьшаясь до нуля или увеличиваясь до шести узлов.

- [Создание группы узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Создание группы узлов
- [Справочник API](https://cloud.ru/docs/kubernetes-evolution/ug/topics/api-ref)Справочник API
- [Автоматическое масштабирование группы узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__cluster-autoscaler)Автоматическое масштабирование группы узлов

[Создание группы узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/guides__node-pool__create)Создание группы узлов

[Справочник API](https://cloud.ru/docs/kubernetes-evolution/ug/topics/api-ref)Справочник API

[Автоматическое масштабирование группы узлов](https://cloud.ru/docs/kubernetes-evolution/ug/topics/concepts__cluster-autoscaler)Автоматическое масштабирование группы узлов
