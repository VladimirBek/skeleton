# Sceleton
### Проект-каркас для микросервисов

```
├── alembic - директория с конфиг файлом для миграций и сами миграции  
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── alembic.ini - конфиг файл для миграций
├── docker-compose.yml 
├── Dockerfile
├── env.example - перечень необходимых переменных обязательных для заполнения
├── requirements.txt - зависимости
├── src
│   ├── application - слой приложения (реализация)
│   │   ├── adapters - в адаптерах хранятся реализация репозитория и uow
│   │   │   ├── __init__.py
│   │   │   ├── repository_impl.py
│   │   │   └── unit_of_work_impl.py
│   │   ├── errors - папка для кастомных исключений
│   │   │   └── __init__.py
│   │   ├── models - здесь хранятся модели orm
│   │   ├── usecases - здесь лежат реализации юзкейсов
│   │   │   └── __init__.py
│   │   └── services - папка для реализации сервисов, а также реализация DI
│   │   │   ├── dependencies.py 
│   │             └── __init__.py
│   ├── domain - доменный слой (абстракция)
│   │   ├── entities - здесь содержатся доменные сущности
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── interfaces - в интерфейсах содержатся, например, абстракции uow и репозитория
│   │   │   └── __init__.py
│   │   ├── services - здесь лежат абстракции сервисов
│   │   │   └── __init__.py
│   │   ├── usecases - здесь лежат абстракции юзкейсов
│   │   │   └── __init__.py
│   │   └── value_objects - здесь содержатся подсущности доменных сущностей, а также enum
│   │       └── __init__.py
│   ├── __init__.py
│   ├── presentation - слой презентации (через апи или cli)
│   │   ├── api - директория для эндпоинтов
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── cli - директория для скриптов cli
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── models - модели (схемы) для api
│   │       └── __init__.py
│   └── shared - папка с общими сервисами, инфрастурктурой, базовыми классами
│       ├── application
│       │   ├── errors
│       │   │   ├── base_exception.py - базовый класс для кастомных исключений
│       │   │   └── __init__.py
│       │   ├── __init__.py
│       │   ├── models
│       │   │   ├── __init__.py
│       │   │   └── postgres
│       │   │       ├── __init__.py
│       │   │       └── models.py - базовый класс для моделей orm
│       │   ├── repositories
│       │   │   ├── base_repository.py - базовый класс для репозитория
│       │   │   └── __init__.py
│       │   ├── services
│       │   │   ├── base_query_service.py - базовый класс для query service
│       │   │   ├── aws_service.py - сервис aws
│       │   │   └── __init__.py
│       │   ├── unit_of_work 
│       │   │   ├── __init__.py
│       │   │   └── unit_of_work.py - базовый клласс для uow
│       │   └── use_cases
│       │       ├── __init__.py
│       │       └── use_case.py - базовый класс для юзкейсов
│       ├── config.py - конфиг файл
│       ├── dependencies.py
│       ├── domain 
│       │   ├── services - базовые классы для сервисов
│       │   │   ├── base_query_service.py - базовый класс для query service
│       │   ├── events - базовая реализация доменных событий 
│       │   │   ├── base_handler.py
│       │   │   ├── domain_event.py
│       │   │   ├── event_dispatcher.py
│       │   │   └── __init__.py
│       │   └── __init__.py
│       ├── entrypoints - точки входа
│       │   ├── cli.py
│       │   ├── fastapi_app.py
│       │   └── __init__.py
│       ├── infrastructure - инфраструктура проекта
│       │   ├── database
│       │   │   ├── __init__.py
│       │   │   ├── mssql
│       │   │   │   ├── database.py - движок для базы данных
│       │   │   │   └── __init__.py
│       │   │   └── postgres
│       │   │       ├── database.py - движок для базы данных
│       │   │       └── __init__.py
│       │   └── __init__.py
│       └── __init__.py
└── tests
    └── __init__.py

```