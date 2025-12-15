---
title: Создание приложения с Aider и Foundation Models
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider
topic: ai-factory
---
# Создание приложения с Aider и Foundation Models

С помощью этого руководства вы интегрируете сервис Foundation Models с приложением Aider, чтобы превратить Терминал в ИИ-ассистента.
Вы создадите полноценную игру на Python с помощью искусственного интеллекта, используя API-ключ и настройки окружения.
В результате вы получите практические навыки работы с языковыми моделями, автоматизацией разработки и настройкой сторонних инструментов.

Вы будете использовать следующие сервисы:

- [Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.
- [Aider](https://aider.chat/)Aider — консольное приложение с ИИ-ассистентом для помощи в написании кода.
- Терминал macOS — среда выполнения команд и запуска приложений.

[Foundation Models](https://cloud.ru/docs/foundation-models/ug/index)Foundation Models — сервис для доступа к API популярных фундаментальных моделей машинного обучения с открытым исходным кодом.

[Aider](https://aider.chat/)Aider — консольное приложение с ИИ-ассистентом для помощи в написании кода.

Терминал macOS — среда выполнения команд и запуска приложений.

Шаги:

1. [Сгенерируйте API-ключ для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Сгенерируйте API-ключ для интеграции.
2. [Установите и настройте Aider](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Установите и настройте Aider.
3. [Создайте игру с помощью Aider](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Создайте игру с помощью Aider.

[Сгенерируйте API-ключ для интеграции](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Сгенерируйте API-ключ для интеграции.

[Установите и настройте Aider](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Установите и настройте Aider.

[Создайте игру с помощью Aider](https://cloud.ru/docs/tutorials-evolution/list/topics/foundation-models__assistent-aider)Создайте игру с помощью Aider.

## Перед началом работы

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://cloud.ru/docs/console/ug/topics/guides__registration)Зарегистрируйтесь в личном кабинете Cloud.ru.

Если вы уже зарегистрированы, [войдите под своей учетной записью](https://cloud.ru/docs/console/ug/topics/guides__auth)войдите под своей учетной записью.

## 1. Сгенерируйте API-ключ для интеграции

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

## 2. Установите и настройте Aider

Установите приложение Aider на вашу операционную систему, [следуя официальной документации](https://aider.chat/docs/install.html)следуя официальной документации.

Ниже пример установки для macOS:

1. Откройте Терминал на macOS.
2. Выполните команду для установки Aider:
curl -LsSf https://aider.chat/install.sh | sh
3. Создайте директорию для проекта и перейдите в нее:
mkdir test_project && cd test_project
4. Создайте файл .env с настройками подключения к Foundation Models:
cat <<'EOF' > .env## Foundation Models connection settings for Aider# Default modelAIDER_MODEL=openai/t-tech/T-pro-it-2.0# API settingsOPENAI_API_KEY=<your-api-key>OPENAI_API_BASE=https://foundation-models.api.cloud.ru/v1# Additional convenience settingsAIDER_PRETTY=trueAIDER_STREAM=trueAIDER_AUTO_COMMITS=trueAIDER_SHOW_MODEL_WARNINGS=falseAIDER_SKIP_SANITY_CHECK_REPO=trueAIDER_GIT=falseEOF

Где <your-api-key> — API-ключ, полученный на предыдущем шаге.

Откройте Терминал на macOS.

Выполните команду для установки Aider:

```bash
curl
-LsSf
https://aider.chat/install.sh
|
sh
```

![../_images/s__install-aider.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__install-aider.png)

Создайте директорию для проекта и перейдите в нее:

```bash
mkdir
test_project
&&
cd
test_project
```

Создайте файл .env с настройками подключения к Foundation Models:

```bash
cat
<<
'EOF'
>
.env
## Foundation Models connection settings for Aider
# Default model
AIDER_MODEL=openai/t-tech/T-pro-it-2.0
# API settings
OPENAI_API_KEY=<your-api-key>
OPENAI_API_BASE=https://foundation-models.api.cloud.ru/v1
# Additional convenience settings
AIDER_PRETTY=true
AIDER_STREAM=true
AIDER_AUTO_COMMITS=true
AIDER_SHOW_MODEL_WARNINGS=false
AIDER_SKIP_SANITY_CHECK_REPO=true
AIDER_GIT=false
EOF
```

Где <your-api-key> — API-ключ, полученный на предыдущем шаге.

В примере модель по умолчанию указана T-pro-it-2.0, но вы можете выбрать [любую доступную модель в Foundation Models](https://cloud.ru/products/evolution-foundation-models)любую доступную модель в Foundation Models.

Корректный синтаксис для указания модели — AIDER_MODEL=openai/вендор/название_llm.
Все доступные настройки для Aider описаны [в официальной документации](https://aider.chat/docs/config/dotenv.html)в официальной документации.

1. Убедитесь, что все настройки корректны, и запустите Aider:
aider
2. Дождитесь ответа от ассистента.
Если подключение установлено, вы увидите приветственное сообщение и приглашение к диалогу.

Убедитесь, что все настройки корректны, и запустите Aider:

```bash
aider
```

Дождитесь ответа от ассистента.
Если подключение установлено, вы увидите приветственное сообщение и приглашение к диалогу.

![../_images/s__start-aider.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/s__start-aider.png)

## 3. Создайте игру с помощью Aider

1. В той же директории запустите Aider с указанием имени файла:
aider snake_game.py
2. Введите запрос ИИ-ассистенту:
Создай игру змейка на python с красивым дизайном
3. Дождитесь, пока Aider сгенерирует код.
4. Когда ассистент предложит записать изменения в файл, нажмите Y и подтвердите ввод.
5. Запустите игру:
python3 snake_game.py
6. Управляйте змейкой с помощью стрелок на клавиатуре и наслаждайтесь игрой:

В той же директории запустите Aider с указанием имени файла:

```bash
aider snake_game.py
```

Введите запрос ИИ-ассистенту:

```bash
Создай игру змейка на python с красивым дизайном
```

Дождитесь, пока Aider сгенерирует код.

Когда ассистент предложит записать изменения в файл, нажмите Y и подтвердите ввод.

Запустите игру:

```bash
python3 snake_game.py
```

Управляйте змейкой с помощью стрелок на клавиатуре и наслаждайтесь игрой:

## Результат

В ходе лабораторной работы вы создали API-ключ для доступа к Foundation Models, настроили приложение Aider и сгенерировали игру с помощью ИИ.
Теперь вы можете использовать Aider для автоматизации разработки, написания кода и тестирования идей с помощью языковых моделей.
