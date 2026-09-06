# Python-Todo

Терминальное приложение для ведения списка задач (todo). CRUD по SQLite,
CLI с меню (questionary) и табличным выводом (rich), тесты pytest.

## Структура

```
main.py                      # точка входа: цикл меню + обработчики
app/cli/menu.py              # run_menu() — селектор действий
app/cli/screens.py           # show_tasks() — таблица задач
app/models/task.py           # Task (dataclass)
app/services/todo_service.py # TodoService — бизнес-логика (CRUD)
app/database/sqlite.py       # SQLiteDatabase — доступ к SQLite
sql/schema.sql               # схема таблицы
tests/                       # pytest (18 тестов)
data/todo.db                 # база данных (создаётся автоматически)
```

## Требования

- Python 3.14 (работает на 3.10+)
- Зависимости: `rich`, `questionary`, `pytest` (в `requirements.txt`)

## Установка и запуск

```bash
# 1. Виртуальное окружение
python3 -m venv .venv
source .venv/bin/activate

# 2. Зависимости
python -m pip install -r requirements.txt

# 3. Запуск
python main.py
```

База данных `data/todo.db` создаётся автоматически при первом запуске
(`create_table()`), каталог `data/` должен существовать.

## Команды меню

- `Add Task` — добавить задачу (название + описание)
- `Remove Task` — удалить по ID
- `Complete Task` — пометить выполненной
- `Change Title` — переименовать
- `Change Description` — изменить описание
- `Exit` — выход

## Тесты

```bash
python -m pytest -v
```
