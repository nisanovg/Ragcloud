---
title: Создание ассистентов и работа с документами в Chatbox на основе Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox
topic: ai-factory
---
# Создание ассистентов и работа с документами в Chatbox на основе Foundation Models

С помощью этого руководства вы получите практический опыт по созданию ассистента и работе с документами в приложении Chatbox AI на основе сервиса Foundation Models.

Вы будете использовать следующие сервисы:

- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [Chatbox AI](https://chatboxai.app/ru)Chatbox AI — сервис для взаимодействия с LLM через open-source чат-интерфейс.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Chatbox AI](https://chatboxai.app/ru)Chatbox AI — сервис для взаимодействия с LLM через open-source чат-интерфейс.

Шаги:

1. [Создайте сервисный аккаунт](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте сервисный аккаунт.
2. [Сгенерируйте API-ключ](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Сгенерируйте API-ключ.
3. [Установите Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Установите Chatbox AI.
4. [Подключите Foundation Models в Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Подключите Foundation Models в Chatbox AI.
5. [Создайте ассистента для генерации кода](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте ассистента для генерации кода.
6. [Создайте чат с документами](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте чат с документами.

[Создайте сервисный аккаунт](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте сервисный аккаунт.

[Сгенерируйте API-ключ](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Сгенерируйте API-ключ.

[Установите Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Установите Chatbox AI.

[Подключите Foundation Models в Chatbox AI](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Подключите Foundation Models в Chatbox AI.

[Создайте ассистента для генерации кода](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте ассистента для генерации кода.

[Создайте чат с документами](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)Создайте чат с документами.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Создайте сервисный аккаунт

1. На верхней панели слева нажмите и перейдите в раздел Пользователи → Сервисные аккаунты.
2. В правом верхнем углу нажмите Создать сервисный аккаунт.
3. Задайте для сервисного аккаунта название и описание.
4. Назначьте доступы и роль.
Роль определяет права доступа сервисного аккаунта.
Чтобы аккаунт мог совершать какие-либо действия с ресурсами, выберите роль «Пользователь проекта».
5. Нажмите Создать.

На верхней панели слева нажмите и перейдите в раздел Пользователи → Сервисные аккаунты.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

![../_images/s__service_account.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account.png)

В правом верхнем углу нажмите Создать сервисный аккаунт.

![../_images/s__service_account_create.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account_create.png)

Задайте для сервисного аккаунта название и описание.

Назначьте доступы и роль.
Роль определяет права доступа сервисного аккаунта.
Чтобы аккаунт мог совершать какие-либо действия с ресурсами, выберите роль «Пользователь проекта».

![../_images/s__service_account_roles.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account_roles.png)

Нажмите Создать.

## 2. Сгенерируйте API-ключ

1. На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.
2. Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.
3. Перейдите на вкладку API-ключи.
4. Нажмите Создать API-ключ.
5. Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.
6. Заполните параметры API-ключа:

Сервисы — Foundation Models.
Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.
7. Нажмите Создать.
8. Сохраните Key Secret.
После закрытия окна получить его будет нельзя.
Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

На верхней панели слева нажмите и перейдите в раздел Пользователи, на вкладку Сервисные аккаунты.

![Кнопка с изображением девяти точек](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__platform-menu.svg)

Нажмите на название сервисного аккаунта, который будете использовать для отправки запроса к модели.

![../_images/s__service_account_n.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__service_account_n.png)

Перейдите на вкладку API-ключи.

Нажмите Создать API-ключ.

![../_images/s__create_key.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__create_key.png)

Введите название и описание API-ключа, которое поможет в будущем идентифицировать его среди других ключей.

Заполните параметры API-ключа:

- Сервисы — Foundation Models.
- Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.
- Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Сервисы — Foundation Models.

Время действия — срок действия API-ключа и часовой пояс.
Вы можете установить значение от одного дня до одного года с текущей даты.
Если параметр не задан, срок действия ключа устанавливается на максимальное значение — один год.
С целью повышения уровня безопасности рекомендуется выставлять средние значения, например 90 дней.

Интервал работы ключа — один или несколько интервалов времени, в которые можно использовать API-ключ.

Нажмите Создать.

Сохраните Key Secret.
После закрытия окна получить его будет нельзя.

Созданный API-ключ появится в списке ключей в статусе «Активен».
[Подробнее о работе с API-ключом](https://cloud.ru/docs/console_api/ug/topics/guides__static-api-keys)Подробнее о работе с API-ключом.

## 3. Установите Chatbox AI

1. Перейдите на страницу загрузки [Chatbox AI](https://github.com/Bin-Huang/chatbox)Chatbox AI.
2. Выберите версию приложения для вашей операционной системы: Windows, Linux, macOS, Android, iOS или используйте веб-версию.
3. Установите приложение или откройте веб-интерфейс.

Перейдите на страницу загрузки [Chatbox AI](https://github.com/Bin-Huang/chatbox)Chatbox AI.

Выберите версию приложения для вашей операционной системы: Windows, Linux, macOS, Android, iOS или используйте веб-версию.

Установите приложение или откройте веб-интерфейс.

## 4. Подключите Foundation Models в Chatbox AI

1. Откройте Chatbox AI.
2. Перейдите в раздел Настройки.
3. Нажмите Добавить.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__settings_ch_b_add.png)
4. В поле Название укажите Foundation Models.
5. В поле Режим API выберите значение Совместимо с API OpenAI.
6. Нажмите Добавить.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__add_provider_ch_b.png)
7. В списке поставщиков моделей выберите Foundation Models.
8. В поле API‑ключ введите значение, полученное [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)на шаге 2.
9. В поле Хост API укажите https://foundation-models.api.cloud.ru.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__settings_param.png)
10. Нажмите Получить.
Откроется список доступных моделей.
11. Нажмите для добавления модели.
Вы можете добавить любое количество доступных моделей.
12. Нажмите в строке модели, чтобы включить поддержку дополнительных возможностей:

Видение — распознавание документов и изображений.
Логика — режим размышления для модели в чате.
Использование инструмента — возможность работы с дополнительными инструментами.
13. Нажмите Сохранить.

Откройте Chatbox AI.

Перейдите в раздел Настройки.

![../_images/s__settings_ch_b.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__settings_ch_b.png)

Нажмите Добавить.

![../_images/s__settings_ch_b_add.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__settings_ch_b_add.png)

В поле Название укажите Foundation Models.

В поле Режим API выберите значение Совместимо с API OpenAI.

Нажмите Добавить.

![../_images/s__add_provider_ch_b.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__add_provider_ch_b.png)

В списке поставщиков моделей выберите Foundation Models.

В поле API‑ключ введите значение, полученное [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-chatbox)на шаге 2.

В поле Хост API укажите https://foundation-models.api.cloud.ru.

![../_images/s__settings_param.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__settings_param.png)

Нажмите Получить.
Откроется список доступных моделей.

Нажмите для добавления модели.
Вы можете добавить любое количество доступных моделей.

![Кнопка с изображением плюса](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__add_model.svg)

![../_images/s__add_model_ch_b.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__add_model_ch_b.png)

Нажмите в строке модели, чтобы включить поддержку дополнительных возможностей:

![Кнопка с изображением шестеренки](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/b__settings_model.svg)

- Видение — распознавание документов и изображений.
- Логика — режим размышления для модели в чате.
- Использование инструмента — возможность работы с дополнительными инструментами.

Видение — распознавание документов и изображений.

Логика — режим размышления для модели в чате.

Использование инструмента — возможность работы с дополнительными инструментами.

![../_images/s__settings_edit_model.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__settings_edit_model.png)

Нажмите Сохранить.

## 5. Создайте ассистента для генерации кода

В Chatbox AI доступно создание собственных ассистентов для различных задач.

Для создания ассистента:

1. Перейдите во вкладку Мои Copilots.
2. Выберите ассистента, например Fullstack Software Developer.
Будет создан новый чат с ассистентом по генерации кода.
3. Введите запрос, например:
Сгенерируй красивый лендинг для сервиса Foundation Models с использованием HTML, CSS и JS
4. Дождитесь ответа ассистента.
5. Нажмите Предпросмотр, чтобы просмотреть сгенерированную страницу.
6. При необходимости попросите ассистента внести правки в код.

Перейдите во вкладку Мои Copilots.

Выберите ассистента, например Fullstack Software Developer.
Будет создан новый чат с ассистентом по генерации кода.

Введите запрос, например:

```bash
Сгенерируй красивый лендинг для сервиса Foundation Models с использованием HTML, CSS и JS
```

![../_images/s__request_chat.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__request_chat.png)

Дождитесь ответа ассистента.

Нажмите Предпросмотр, чтобы просмотреть сгенерированную страницу.

![../_images/s__preview_chat.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__preview_chat.png)

При необходимости попросите ассистента внести правки в код.

## 6. Создайте чат с документами

Chatbox AI поддерживает работу с изображениями и файлами.

Для загрузки файла:

1. В интерфейсе чата нажмите кнопку Выбрать файл.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__file_selection.png)
2. Выберите текстовый файл.
В качестве примера мы загрузили страницу Foundation Models, сохраненную в DOCX.
3. Задайте вопрос по содержанию документа, например:
Какие модели доступны в сервисе Foundation Models?
4. Убедитесь, что ответ модели содержит информацию из загруженного файла.

В интерфейсе чата нажмите кнопку Выбрать файл.

![../_images/s__file_selection.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__file_selection.png)

Выберите текстовый файл.
В качестве примера мы загрузили страницу Foundation Models, сохраненную в DOCX.

Задайте вопрос по содержанию документа, например:

```bash
Какие модели доступны в сервисе Foundation Models?
```

![../_images/s__ch_model_response.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__ch_model_response.png)

Убедитесь, что ответ модели содержит информацию из загруженного файла.

## Результат

В ходе практической работы вы подключили приложение Chatbox AI к сервису Foundation Models, создали API-ключ, настроили модель и воспользовались ассистентом для генерации кода и анализа документов.
Теперь вы можете использовать Chatbox AI для эффективной работы с LLM и файлами, обеспечивая приватность и контроль над данными.

Cloud.ru не предоставляет техническую поддержку приложения Chatbox AI.
При возникновении вопросов обращайтесь [в центр помощи Chatbox AI](https://chatboxai.app/ru/help-center)в центр помощи Chatbox AI.
