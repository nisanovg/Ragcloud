---
title: Подготовка среды для Artifact Registry и Container Apps
source: Cloud.ru Evolution Tutorials
url: https://cloud.ru/docs/tutorials-evolution/list/topics/container-apps__before-work
topic: containers
---
# Подготовка среды для Artifact Registry и Container Apps

Перед началом работы с практическими руководствами по Artifact Registry и Container Apps:

1. [Зарегистрируйтесь в личном кабинете Cloud.ru](https://console.cloud.ru/registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
После регистрации вы получите доступ к личному кабинету.
Если вы уже зарегистрированы, [войдите в личный кабинет](https://console.cloud.ru/)войдите в личный кабинет.
2. Установите [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop.
3. Установите [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli)Docker CLI или используйте привычный терминал на вашем компьютере.
4. Создайте приватный реестр в Artifact Registry.

В [личном кабинете](https://console.cloud.ru/)личном кабинете перейдите на карточку сервиса Artifact Registry.

Нажмите Создать реестр.
Укажите название реестра — оно станет частью URI, который вы будете использовать при работе в Docker CLI.
Нажмите Создать.

Скопируйте полученный URI реестра, он будет нужен для выполнения дальнейших шагов.
5. Получите ключи доступа для аутентификации.

В личном кабинете перейдите в раздел Управление профилем.

Выберите раздел Ключи доступа и нажмите Создать ключ.

Введите краткое описание ключа, которое поможет в будущем идентифировать его среди других ключей.
Задайте время жизни ключа: от 1 до 365 дней.
Нажмите Создать.
После этого будут сгенерированы Key ID (логин) и Key Secret (пароль).
Сохраните Key Secret.
После того как вы закроете окно, повторно посмотреть его будет нельзя.
6. Пройдите аутентификацию в реестре Artifact Registry.
Откройте терминал и введите команду для аутентификации.
Вы можете использовать любой привычный для вас терминал.
docker login <registry_name>.cr.cloud.ru -u <key_id> -p <key_secret>

Где:

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
<key_id> — логин персонального ключа (Key ID).
<key_secret> — пароль персонального ключа (Key Secret).
7. (Опционально) Создайте учетную запись в [GitVerse](https://gitverse.ru/)GitVerse.
Вы можете зарегистрироваться в GitVerse, если у вас еще нет аккаунта, и познакомиться с новой системой контроля версий.
Примеры кода из практических руководств размещаются в GitVerse.

[Зарегистрируйтесь в личном кабинете Cloud.ru](https://console.cloud.ru/registration)Зарегистрируйтесь в личном кабинете Cloud.ru.
После регистрации вы получите доступ к личному кабинету.

Если вы уже зарегистрированы, [войдите в личный кабинет](https://console.cloud.ru/)войдите в личный кабинет.

Установите [Docker Desktop](https://www.docker.com/products/docker-desktop)Docker Desktop.

Установите [Docker CLI](https://docs.docker.com/engine/reference/commandline/cli)Docker CLI или используйте привычный терминал на вашем компьютере.

Создайте приватный реестр в Artifact Registry.

1. В [личном кабинете](https://console.cloud.ru/)личном кабинете перейдите на карточку сервиса Artifact Registry.
2. Нажмите Создать реестр.
3. Укажите название реестра — оно станет частью URI, который вы будете использовать при работе в Docker CLI.
4. Нажмите Создать.
5. Скопируйте полученный URI реестра, он будет нужен для выполнения дальнейших шагов.

В [личном кабинете](https://console.cloud.ru/)личном кабинете перейдите на карточку сервиса Artifact Registry.

![../_images/ar-go-console.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-go-console.png)

Нажмите Создать реестр.

Укажите название реестра — оно станет частью URI, который вы будете использовать при работе в Docker CLI.

Нажмите Создать.

![../_images/ar-registry-create.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-registry-create.png)

Скопируйте полученный URI реестра, он будет нужен для выполнения дальнейших шагов.

![../_images/ar-registry-copy-uri.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-registry-copy-uri.png)

Получите ключи доступа для аутентификации.

1. В личном кабинете перейдите в раздел Управление профилем.
2. Выберите раздел Ключи доступа и нажмите Создать ключ.
3. Введите краткое описание ключа, которое поможет в будущем идентифировать его среди других ключей.
4. Задайте время жизни ключа: от 1 до 365 дней.
5. Нажмите Создать.
После этого будут сгенерированы Key ID (логин) и Key Secret (пароль).
Сохраните Key Secret.
После того как вы закроете окно, повторно посмотреть его будет нельзя.

В личном кабинете перейдите в раздел Управление профилем.

![../_images/profile-settings.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/profile-settings.png)

Выберите раздел Ключи доступа и нажмите Создать ключ.

![../_images/ar-secrets.png](https://cloud.ru/docs/api/cdn/tutorials-evolution/list/_images/ar-secrets.png)

Введите краткое описание ключа, которое поможет в будущем идентифировать его среди других ключей.

Задайте время жизни ключа: от 1 до 365 дней.

Нажмите Создать.

После этого будут сгенерированы Key ID (логин) и Key Secret (пароль).
Сохраните Key Secret.
После того как вы закроете окно, повторно посмотреть его будет нельзя.

Пройдите аутентификацию в реестре Artifact Registry.

Откройте терминал и введите команду для аутентификации.
Вы можете использовать любой привычный для вас терминал.

```bash
docker
login
<
registry_name
>
.cr.cloud.ru
-u
<
key_id
>
-p
<
key_secret
>
```

Где:

- <registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.
- <key_id> — логин персонального ключа (Key ID).
- <key_secret> — пароль персонального ключа (Key Secret).

<registry_name> — название реестра, которое вы указывали при его создании в Artifact Registry.

<key_id> — логин персонального ключа (Key ID).

<key_secret> — пароль персонального ключа (Key Secret).

(Опционально) Создайте учетную запись в [GitVerse](https://gitverse.ru/)GitVerse.

Вы можете зарегистрироваться в GitVerse, если у вас еще нет аккаунта, и познакомиться с новой системой контроля версий.
Примеры кода из практических руководств размещаются в GitVerse.
