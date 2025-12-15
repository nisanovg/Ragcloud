---
title: Подключение Foundation Models в VS Code
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode
topic: ai-factory
---
# Подключение Foundation Models в VS Code

С помощью этого руководства вы подключите Foundation Models в VS Code через плагин Roo Code.

Вы будете использовать следующие сервисы:

- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- VS Code — редактор кода, который поддерживает множество языков программирования, включая Python, Java, C++, JavaScript и многие другие.
- Roo Code — плагин для анализа, написания, рефакторинга и отладки кода.
Поддерживает различные API и локальные модели.
Позволяет создавать собственных AI-ассистентов для определенных задач и ролей, переключать режимы и настраивать промпты.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

VS Code — редактор кода, который поддерживает множество языков программирования, включая Python, Java, C++, JavaScript и многие другие.

Roo Code — плагин для анализа, написания, рефакторинга и отладки кода.
Поддерживает различные API и локальные модели.
Позволяет создавать собственных AI-ассистентов для определенных задач и ролей, переключать режимы и настраивать промпты.

Шаги:

1. [Создайте сервисный аккаунт](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Создайте сервисный аккаунт.
2. [Сгенерируйте API-ключ](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Сгенерируйте API-ключ.
3. [Установите VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Установите VS Code.
4. [Установите плагин Roo Code в VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Установите плагин Roo Code в VS Code.
5. [Подключите Foundation Models в Roo Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Подключите Foundation Models в Roo Code.
6. [Начните работу с моделями](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Начните работу с моделями.

[Создайте сервисный аккаунт](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Создайте сервисный аккаунт.

[Сгенерируйте API-ключ](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Сгенерируйте API-ключ.

[Установите VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Установите VS Code.

[Установите плагин Roo Code в VS Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Установите плагин Roo Code в VS Code.

[Подключите Foundation Models в Roo Code](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Подключите Foundation Models в Roo Code.

[Начните работу с моделями](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)Начните работу с моделями.

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

## 3. Установите VS Code

1. Перейдите на страницу загрузки [VS Code](https://code.visualstudio.com/download)VS Code.
2. Выберите версию приложения для вашей операционной системы: Windows, Linux, macOS.
3. Установите приложение.

Перейдите на страницу загрузки [VS Code](https://code.visualstudio.com/download)VS Code.

Выберите версию приложения для вашей операционной системы: Windows, Linux, macOS.

Установите приложение.

## 4. Установите плагин Roo Code в VS Code

1. Откройте VS Code.
2. Перейдите в раздел расширений Extensions.
3. Найдите плагин Roo Code.
4. Нажмите Install.

Откройте VS Code.

Перейдите в раздел расширений Extensions.

Найдите плагин Roo Code.

Нажмите Install.

![../_images/s__installation_roo_code.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__installation_roo_code.png)

## 5. Подключите Foundation Models в Roo Code

1. Откройте плагин Roo Code.
2. Перейдите в раздел Настройки.
3. В поле Провайдер API укажите OpenAI Compatible.
4. В поле Базовый URL укажите https://foundation-models.api.cloud.ru/v1.
5. В поле API-ключ укажите значение ключа, полученное [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)на шаге 2.
6. Выберите модель для работы в Roo Code.
7. Нажмите Сохранить, а затем Готово.
[](https://cloud.ru/docs/tutorials-evolution/list/_images/s__param_roo_code.png)

Откройте плагин Roo Code.

Перейдите в раздел Настройки.

![../_images/s__settings_roo_code.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__settings_roo_code.png)

В поле Провайдер API укажите OpenAI Compatible.

В поле Базовый URL укажите https://foundation-models.api.cloud.ru/v1.

В поле API-ключ укажите значение ключа, полученное [на шаге 2](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__connect-vscode)на шаге 2.

Выберите модель для работы в Roo Code.

Нажмите Сохранить, а затем Готово.

![../_images/s__param_roo_code.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__param_roo_code.png)

Все остальные параметры опциональны.
Подробная документация плагина Roo Code доступна [на официальном сайте](https://docs.roocode.com/)на официальном сайте.

## 6. Начните работу с моделями

1. На боковой панели нажмите на иконку плагина Roo Code.
Появится диалоговое окно, где вы можете описать свою задачу в чате.
Например, можно использовать такой промпт:
Создай папку проекта с именем "calculator" в текущей директории.Напиши скрипт на Python для реализации функциональности калькулятора в терминале.Напиши руководство пользователя по использованию этого приложения.
2. Если вы настроили автоматическое подтверждение действий, все действия будут выполняться автоматически.
Проверить работу созданного приложения можно сразу же в VS Code.
Пример в видео ниже:

На боковой панели нажмите на иконку плагина Roo Code.
Появится диалоговое окно, где вы можете описать свою задачу в чате.
Например, можно использовать такой промпт:

```bash
Создай папку проекта с именем
"calculator"
в текущей директории.
Напиши скрипт на Python для реализации функциональности калькулятора в терминале.
Напиши руководство пользователя по использованию этого приложения.
```

![../_images/s__prompt.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__prompt.png)

Если вы настроили автоматическое подтверждение действий, все действия будут выполняться автоматически.
Проверить работу созданного приложения можно сразу же в VS Code.
Пример в видео ниже:

## Результат

В ходе выполнения практической работы вы подключили Foundation Models в VS Code.

Cloud.ru не предоставляет техническую поддержку VS Code и Roo Code.
При возникновении вопросов обращайтесь к [документации разработчиков VS Code](https://code.visualstudio.com/docs)документации разработчиков VS Code и [документации разработчиков Roo Code](https://docs.roocode.com/)документации разработчиков Roo Code.
