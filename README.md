# Manager Task 10 - ORM Operations

Проект для выполнения CRUD операций с использованием Django ORM.

## Установка и запуск

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте окружение: `.\venv\Scripts\activate` (Windows) или `source venv/bin/activate` (macOS/Linux)
4. Установите зависимости: `pip install django`
5. Примените миграции: `python manage.py migrate`
6. Запустите ORM операции: `python manage.py run_orm_operations`

## Структура проекта

- `tasks/models.py` - Модели Task, SubTask, Status
- `tasks/orm_operations.py` - Основные ORM операции
- `tasks/management/commands/run_orm_operations.py` - Команда для запуска операций
- `tasks/tests/test_orm_operations.py` - Тесты для ORM операций

## Выполненные операции

1. **Создание записей** - задачи и подзадачи
2. **Чтение записей** - фильтрация по статусу и дедлайну
3. **Изменение записей** - обновление статуса, дедлайна, описания
4. **Удаление записей** - удаление задачи с каскадным удалением подзадач 


Manager_task_10/
├── Manager_task_10/          # Настройки проекта
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tasks/                    # Приложение tasks
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── orm_operations.py    # Основные ORM операции
│   ├── management/
│   │   └── commands/
│   │       └── run_orm_operations.py
│   └── migrations/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md# Manager_task_10
# Manager_task_10
# Manager_task_10
# Manager_task_10
