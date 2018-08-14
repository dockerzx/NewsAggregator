# Агрегатор новостных лент

Должен собирать новости из различных источников и помещать их в базу данных  
Доступ к сервису осуществляется через GET-запросы по опеределенным url  
Это поведение должно измениться в дальнейшем


## Развертывание зависимостей
```
$ server init
```

## Запуск

Перед запуском необходимо прописать url на котором будет работать сервер в config.bat
```
set apiIP=localhost
set apiPORT=8001
```

И задать локальные настройки django в файле settings_local.py
```
DEBUG = True
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

Строчка **CELERY_BROKER_URL** это url для подключения к работающему серверу redis.
Если такой отсутствует, нужно установить redis на локальной машине

После этого можно запустить сервер командой

```
$ server start
```