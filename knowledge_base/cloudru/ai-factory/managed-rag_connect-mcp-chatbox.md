---
title: Подключение MCP-сервера Managed RAG к Chatbox
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox
topic: ai-factory
---
# Подключение MCP-сервера Managed RAG к Chatbox

С помощью этого руководства вы подключите MCP-сервер к базе знаний, чтобы использовать AI-агента с инструментом поиска по базе знаний в интерфейсе Chatbox AI.

Вы будете использовать следующие сервисы:

- [Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.
- [AI Agents](https://cloud.ru/docs/ai-agents/ug/index)AI Agents — сервис для создания и управления AI-агентами и агентными системами.
- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [Chatbox AI](https://mcp-chatboxai.app/ru)Chatbox AI — внешний сервис для взаимодействия с LLM через open source чат-интерфейс.

[Managed RAG](https://cloud.ru/docs/rag/ug/index)Managed RAG — сервис для создания и управления базами знаний, используемыми при генерации ответов языковыми моделями.

[AI Agents](https://cloud.ru/docs/ai-agents/ug/index)AI Agents — сервис для создания и управления AI-агентами и агентными системами.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Chatbox AI](https://mcp-chatboxai.app/ru)Chatbox AI — внешний сервис для взаимодействия с LLM через open source чат-интерфейс.

Шаги:

1. [Создайте базу знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Создайте базу знаний.
2. [Создайте и протестируйте MCP-сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Создайте и протестируйте MCP-сервер.
3. [Подключите MCP к Chatbox](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Подключите MCP к Chatbox.
4. [Сравните ответы моделей с подключенным MCP и без него](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Сравните ответы моделей с подключенным MCP и без него.

[Создайте базу знаний](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Создайте базу знаний.

[Создайте и протестируйте MCP-сервер](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Создайте и протестируйте MCP-сервер.

[Подключите MCP к Chatbox](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Подключите MCP к Chatbox.

[Сравните ответы моделей с подключенным MCP и без него](https://cloud.ru/docs/tutorials-evolution/list/topics/managed-rag__connect-mcp-chatbox)Сравните ответы моделей с подключенным MCP и без него.

## Перед началом работы

1. Скачайте [Chatbox AI](https://github.com/Bin-Huang/chatbox)Chatbox AI для вашей операционной системы.
2. Убедитесь, что сервис Foundation Models [подключен в личном кабинете Cloud.ru](https://cloud.ru/docs/foundation-models/ug/index)подключен в личном кабинете Cloud.ru, и [добавьте его в Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)добавьте его в Chatbox AI.
3. Убедитесь, что в личном кабинете Cloud.ru подключен сервис [AI Agents](https://cloud.ru/docs/ai-agents/ug/index)AI Agents.

Скачайте [Chatbox AI](https://github.com/Bin-Huang/chatbox)Chatbox AI для вашей операционной системы.

Убедитесь, что сервис Foundation Models [подключен в личном кабинете Cloud.ru](https://cloud.ru/docs/foundation-models/ug/index)подключен в личном кабинете Cloud.ru, и [добавьте его в Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)добавьте его в Chatbox AI.

Убедитесь, что в личном кабинете Cloud.ru подключен сервис [AI Agents](https://cloud.ru/docs/ai-agents/ug/index)AI Agents.

## 1. Получите данные базы знаний

1. Перейдите в AI Factory → Managed RAG.
2. [Создайте базу знаний из JSON-файлов](https://cloud.ru/docs/rag/ug/topics/tutorials__json-files)Создайте базу знаний из JSON-файлов.
3. Откройте любую версию базы знаний.
4. На вкладке Информация скопируйте и сохраните, например в блокнот, ID версии и ID базы знаний.

Перейдите в AI Factory → Managed RAG.

[Создайте базу знаний из JSON-файлов](https://cloud.ru/docs/rag/ug/topics/tutorials__json-files)Создайте базу знаний из JSON-файлов.

Откройте любую версию базы знаний.

На вкладке Информация скопируйте и сохраните, например в блокнот, ID версии и ID базы знаний.

## 2. Создайте и протестируйте MCP-сервер

1. Перейдите в AI Factory → AI Agents, на вкладку MCP-серверы.
2. Нажмите Создать MCP-сервер.
3. Задайте основные настройки:

Введите название: mcp-server-rag.
на вкладке Маркетплейс выберите сервер evolution-managed-rag-mcp.
Заполните переменные окружения сохраненными ID базы знаний и ее версии:

KNOWLEDGE_BASE_ID — ID базы знаний;
KNOWLEDGE_BASE_VERSION_ID — ID версии базы знаний.
4. Задайте масштабирование и дополнительные опции:

Выберите минимальное и максимальное количество экземпляров равным 1.
Включите опции Запускать все дочерние контейнеры при запросе и Не выключать MCP-сервер.
Выберите Тип масштабирования — RPS, задайте значение 200.
Включите дополнительную опцию Логирование запросов.
Нажмите Создать.
5. Дождитесь, пока MCP-сервер перейдет в статус «Запущен».
6. Протестируйте сервер.
Для этого на вкладке Тестирование скопируйте и отправьте запрос:
Что такое Evolution Magic Router?

Вы получите ответ, которые базируется на информации из базы знаний.
Далее в этом руководстве мы стараемся получить тот же ответ, но в интерфейсе Chatbox AI.

Перейдите в AI Factory → AI Agents, на вкладку MCP-серверы.

Нажмите Создать MCP-сервер.

Задайте основные настройки:

1. Введите название: mcp-server-rag.
2. на вкладке Маркетплейс выберите сервер evolution-managed-rag-mcp.
3. Заполните переменные окружения сохраненными ID базы знаний и ее версии:

KNOWLEDGE_BASE_ID — ID базы знаний;
KNOWLEDGE_BASE_VERSION_ID — ID версии базы знаний.

Введите название: mcp-server-rag.

на вкладке Маркетплейс выберите сервер evolution-managed-rag-mcp.

Заполните переменные окружения сохраненными ID базы знаний и ее версии:

- KNOWLEDGE_BASE_ID — ID базы знаний;
- KNOWLEDGE_BASE_VERSION_ID — ID версии базы знаний.

KNOWLEDGE_BASE_ID — ID базы знаний;

KNOWLEDGE_BASE_VERSION_ID — ID версии базы знаний.

Задайте масштабирование и дополнительные опции:

1. Выберите минимальное и максимальное количество экземпляров равным 1.
2. Включите опции Запускать все дочерние контейнеры при запросе и Не выключать MCP-сервер.
3. Выберите Тип масштабирования — RPS, задайте значение 200.
4. Включите дополнительную опцию Логирование запросов.
5. Нажмите Создать.

Выберите минимальное и максимальное количество экземпляров равным 1.

Включите опции Запускать все дочерние контейнеры при запросе и Не выключать MCP-сервер.

Выберите Тип масштабирования — RPS, задайте значение 200.

Включите дополнительную опцию Логирование запросов.

Нажмите Создать.

Дождитесь, пока MCP-сервер перейдет в статус «Запущен».

Протестируйте сервер.

Для этого на вкладке Тестирование скопируйте и отправьте запрос:

```bash
Что такое Evolution Magic Router?
```

Вы получите ответ, которые базируется на информации из базы знаний.
Далее в этом руководстве мы стараемся получить тот же ответ, но в интерфейсе Chatbox AI.

## 3. Подключите MCP к Chatbox AI

1. Скопируйте публичный URL MCP-сервера — он находится под названием сервера.
2. Откройте Chatbox AI.
3. Перейдите в Настройки → MCP и нажмите Добавить сервер.
4. Выберите Добавить пользовательский сервер.
5. Введите название, например evolution-rag.
6. Выберите Тип — Удаленный.
7. Вставьте скопированный ранее публичный URL MCP-сервера из AI Agents, добавив к нему в конце /mcp.
Например: https://e1d123b1-xxxx-xxxx-xxxx-2fdebd6da312-mcp-server.ai-agent.inference.cloud.ru/mcp.
8. Нажмите Тест.
Появится блок Инструменты со значением request_to_rag.
9. Нажмите Сохранить.

Скопируйте публичный URL MCP-сервера — он находится под названием сервера.

Откройте Chatbox AI.

Перейдите в Настройки → MCP и нажмите Добавить сервер.

Выберите Добавить пользовательский сервер.

Введите название, например evolution-rag.

Выберите Тип — Удаленный.

Вставьте скопированный ранее публичный URL MCP-сервера из AI Agents, добавив к нему в конце /mcp.

Например: https://e1d123b1-xxxx-xxxx-xxxx-2fdebd6da312-mcp-server.ai-agent.inference.cloud.ru/mcp.

Нажмите Тест.

Появится блок Инструменты со значением request_to_rag.

![Блок "Инструменты"](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__managed-rag__connect-mcp-chatbox__add-mcp.png)

Нажмите Сохранить.

## 4. Сравните ответы моделей с подключенным MCP и без него

1. В Chatbox AI создайте чат с моделью из Foundation Models без базы знаний.
Используйте «t-tech/T-lite-it-1.0».

В чате с моделью «t-tech/T-lite-it-1.0» введите запрос:
Что такое Evolution Magic Router?

В ответе, который вы получили, модель не знает об этой сущности и предлагает несколько предположений.
2. В Chatbox AI создайте чат, нажав Новый чат.

Внизу чата нажмите Настроить настройки для текущего разговора.

В поле Инструкция (Системная подсказка) введите:
Ты — ассистент для ответов на вопросы о платформе Cloud.ru Evolution.
Обращайся к базе знаний, когда пользователь спрашивает об этой платформе.Используй инструмент request_to_rag, чтобы получить достоверную информацию о платформе Cloud.ru Evolution из базы знаний.

Остальные настройки оставьте по умолчанию.
Нажмите Сохранить.
Убедитесь, что в чате включен MCP-сервер evolution_rag.

Отправьте в чате запрос:
Что такое Evolution Magic Router?

Теперь модель знает о существовании этого сервиса и может предоставить достоверную информацию.

В Chatbox AI создайте чат с моделью из Foundation Models без базы знаний.
Используйте «t-tech/T-lite-it-1.0».

1. В чате с моделью «t-tech/T-lite-it-1.0» введите запрос:
Что такое Evolution Magic Router?

В чате с моделью «t-tech/T-lite-it-1.0» введите запрос:

```bash
Что такое Evolution Magic Router?
```

В ответе, который вы получили, модель не знает об этой сущности и предлагает несколько предположений.

В Chatbox AI создайте чат, нажав Новый чат.

1. Внизу чата нажмите Настроить настройки для текущего разговора.
2. В поле Инструкция (Системная подсказка) введите:
Ты — ассистент для ответов на вопросы о платформе Cloud.ru Evolution.
Обращайся к базе знаний, когда пользователь спрашивает об этой платформе.Используй инструмент request_to_rag, чтобы получить достоверную информацию о платформе Cloud.ru Evolution из базы знаний.
3. Остальные настройки оставьте по умолчанию.
4. Нажмите Сохранить.
Убедитесь, что в чате включен MCP-сервер evolution_rag.
5. Отправьте в чате запрос:
Что такое Evolution Magic Router?

Теперь модель знает о существовании этого сервиса и может предоставить достоверную информацию.

Внизу чата нажмите Настроить настройки для текущего разговора.

![Настройки для текущего разговора](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__managed-rag__connect-mcp-chatbox__settings.png)

В поле Инструкция (Системная подсказка) введите:

```bash
Ты — ассистент для ответов на вопросы о платформе Cloud.ru Evolution.
Обращайся к базе знаний, когда пользователь спрашивает об этой платформе.
Используй инструмент request_to_rag, чтобы получить достоверную информацию о платформе Cloud.ru Evolution из базы знаний.
```

Остальные настройки оставьте по умолчанию.

Нажмите Сохранить.

Убедитесь, что в чате включен MCP-сервер evolution_rag.

![MCP-сервер включен](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__managed-rag__connect-mcp-chatbox__mcp-on.png)

Отправьте в чате запрос:

```bash
Что такое Evolution Magic Router?
```

Теперь модель знает о существовании этого сервиса и может предоставить достоверную информацию.

## Что дальше

С этим руководством вы создали MCP-сервер AI Agents для Managed RAG и подключили к Chatbox AI.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, получайте навыки управления облаком, выполняя [практические руководства](https://cloud.ru/docs/tutorials-evolution/list/index)практические руководства.
