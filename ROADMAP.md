# 📝 TODO CLI — Roadmap

> Пет-проект на Python: Todo List с красивым интерактивным CLI-интерфейсом.

---

## 🎯 1. Цель проекта

Создать консольное приложение Todo List, которое позволяет:

* [ ] Добавлять задачи
* [ ] Удалять задачи
* [ ] Переименовывать задачи
* [ ] Добавлять и изменять описание
* [ ] Отмечать задачу как выполненную
* [ ] Просматривать список задач
* [ ] Хранить задачи после перезапуска программы
* [ ] Иметь красивый интерактивный CLI

### Технологии

Основной стек:

* **Python 3**
* **Rich** — красивый вывод в терминале
* **Questionary** — интерактивные меню
* **SQLite** — хранение данных
* **pytest** — тестирование

---

# 🏗️ 2. Архитектура проекта

Проект будет разделён на несколько уровней:

```text
                    ┌──────────────┐
                    │    main.py   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │     CLI      │
                    │ Rich +       │
                    │ Questionary  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Service    │
                    │ Business     │
                    │ Logic        │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ Repository   │
                    │ SQLite       │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   todo.db    │
                    └──────────────┘
```

### Главное правило

Каждый слой отвечает только за свою работу.

**CLI** не должен напрямую работать с SQLite.

**Repository** не должен заниматься меню.

**Service** не должен знать, как именно пользователь видит информацию.

---

# 📁 3. Файловая структура

Финальная структура проекта:

```text
todo-cli/
│
├── app/
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── task_repository.py
│   │
│   └── cli/
│       ├── __init__.py
│       ├── menu.py
│       ├── screens.py
│       └── styles.py
│
├── data/
│   └── todo.db
│
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_todo_service.py
│   └── test_task_repository.py
│
├── main.py
├── requirements.txt
├── README.md
├── ROADMAP.md
└── .gitignore
```

---

# 📚 4. Что отвечает за каждый файл

## `main.py`

Точка входа приложения.

Здесь не должно быть бизнес-логики.

Задача:

```text
Запустить приложение
       ↓
Создать необходимые объекты
       ↓
Запустить CLI
```

---

## `app/models/task.py`

Модель задачи.

Примерная структура:

```text
Task
│
├── id
├── title
├── description
├── completed
└── created_at
```

Изучить:

* `class`
* `dataclass`
* type hints
* `datetime`

---

## `app/services/todo_service.py`

Главная бизнес-логика приложения.

Здесь будут операции:

```text
add_task()
delete_task()
rename_task()
update_description()
complete_task()
get_task()
get_all_tasks()
```

Service не должен заниматься отображением информации.

---

## `app/repositories/task_repository.py`

Работа с базой данных.

Основные операции:

```text
create()
get()
get_all()
update()
delete()
```

Repository отвечает только за сохранение и получение данных.

---

## `app/cli/menu.py`

Интерактивные меню.

Например:

```text
? What do you want to do?

❯ Add task
  Edit task
  Delete task
  Complete task
  Show tasks
  Exit
```

Для этого используется `Questionary`.

---

## `app/cli/screens.py`

Отображение информации пользователю.

Например:

```text
╭──────────────────────────────────────╮
│              TODO LIST               │
╰──────────────────────────────────────╯

  3 tasks
  1 completed
  2 active
```

Здесь используется `Rich`.

---

## `app/cli/styles.py`

Все настройки визуального оформления:

* цвета;
* стили;
* emoji;
* темы;
* форматирование.

---
<!-- TODO: Начало -->
# 🚀 5. Этап 0 — Подготовка проекта
Создать директорию:

```bash
mkdir todo-cli
cd todo-cli
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Активировать его.

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Проверить Python:

```bash
python --version
```

---

### Установить зависимости

```bash
pip install rich questionary pytest
```

После этого создать:

```bash
pip freeze > requirements.txt
```

---

### Создать `.gitignore`

Добавить:

```text
.venv/
__pycache__/
.pytest_cache/
*.pyc
data/*.db
.idea/
.vscode/
```

---

### Проверка этапа

* [ ] Создан проект
* [ ] Создан `.venv`
* [ ] Установлен Rich
* [ ] Установлен Questionary
* [ ] Установлен pytest
* [ ] Создан `requirements.txt`
* [ ] Создан `.gitignore`

---

# 🧱 6. Этап 1 — Task Model

## Цель

Создать модель задачи.

---

## Что изучить

* Python classes
* `dataclass`
* type hints
* `datetime`
* `Optional`

---

## Задачи

* [ ] Создать `app/models/task.py`
* [ ] Создать `Task`
* [ ] Добавить `id`
* [ ] Добавить `title`
* [ ] Добавить `description`
* [ ] Добавить `completed`
* [ ] Добавить `created_at`

---

## Проверка

Создать несколько задач вручную:

```text
Task #1
Title: Learn Python
Description: Study classes
Completed: False
```

Убедиться, что объект корректно создаётся.

---

## ✅ Этап завершён, если

Ты можешь создать объект `Task` и получить из него все необходимые данные.

---

# ⚙️ 7. Этап 2 — Todo Service

## Цель

Создать слой бизнес-логики.

---

## Создать

```text
app/services/todo_service.py
```

---

## Реализовать

### Добавление

```text
add_task()
```

### Получение

```text
get_task()
get_all_tasks()
```

### Удаление

```text
delete_task()
```

### Переименование

```text
rename_task()
```

### Описание

```text
update_description()
```

### Выполнение

```text
complete_task()
```

---

## Проверить

* [ ] Можно создать задачу
* [ ] Можно получить задачу
* [ ] Можно получить все задачи
* [ ] Можно удалить задачу
* [ ] Можно изменить название
* [ ] Можно изменить описание
* [ ] Можно изменить статус

---

# 💾 8. Этап 3 — SQLite

## Цель

Сделать так, чтобы задачи не исчезали после закрытия программы.

---

## Изучить

* SQLite
* SQL
* `CREATE TABLE`
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* Python `sqlite3`

---

## Создать

```text
data/
└── todo.db
```

---

## Таблица

```text
tasks
--------------------------------
id
title
description
completed
created_at
```

---

## SQL операции

### Create

```text
INSERT
```

### Read

```text
SELECT
```

### Update

```text
UPDATE
```

### Delete

```text
DELETE
```

---

## Проверка

Сценарий:

```text
Запустить приложение
        ↓
Создать задачу
        ↓
Закрыть приложение
        ↓
Запустить снова
        ↓
Задача существует
```

---

# 🗄️ 9. Этап 4 — Repository

## Цель

Убрать работу с SQLite из Service.

Создать:

```text
app/repositories/task_repository.py
```

---

## Repository должен уметь

```text
create(task)
get(task_id)
get_all()
update(task)
delete(task_id)
```

---

## Архитектура

```text
CLI
 ↓
TodoService
 ↓
TaskRepository
 ↓
SQLite
```

---

## Важно

`TodoService` не должен выполнять SQL-запросы.

Плохо:

```text
TodoService
    ↓
sqlite3.execute(...)
```

Хорошо:

```text
TodoService
    ↓
repository.update(...)
    ↓
SQLite
```

---

# 🖥️ 10. Этап 5 — Первый CLI

## Цель

Создать рабочий консольный интерфейс.

Пока можно без красивого оформления.

---

## Главное меню

```text
TODO LIST

1. Add task
2. Show tasks
3. Edit task
4. Delete task
5. Complete task
6. Exit
```

---

## Задачи

* [ ] Создать `main.py`
* [ ] Сделать главное меню
* [ ] Добавить задачу
* [ ] Показать задачи
* [ ] Изменить задачу
* [ ] Удалить задачу
* [ ] Завершить задачу
* [ ] Добавить выход

---

# 🎨 11. Этап 6 — Rich

## Цель

Превратить обычный CLI в красивый интерфейс.

---

## Изучить Rich

Основные компоненты:

* `Console`
* `Table`
* `Panel`
* `Text`
* `Columns`
* `Prompt`
* `Confirm`
* `Status`
* `Progress`

---

# 📋 Таблица задач

Сделать примерно:

```text
╭────┬────────────────────────────┬────────────╮
│ ID │ TASK                       │ STATUS     │
├────┼────────────────────────────┼────────────┤
│ 1  │ Изучить Python             │ ○ Active   │
│ 2  │ Сделать Todo               │ ✓ Done     │
│ 3  │ Изучить Rich               │ ○ Active   │
╰────┴────────────────────────────┴────────────╯
```

---

# 🏠 Dashboard

Главный экран должен содержать:

```text
╭─────────────────────────────────────────────────────╮
│                  ✦ TODO LIST ✦                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│       TOTAL          ACTIVE          COMPLETED      │
│        12              8                 4          │
│                                                     │
│       Progress: ████████░░░░░░░░ 33%              │
│                                                     │
╰─────────────────────────────────────────────────────╯
```

---

# 🎨 12. Этап 7 — Цветовая схема

Предлагаемая тема:

```text
Background  → dark
Primary     → cyan / blue
Success     → green
Warning     → yellow
Error       → red
Secondary   → grey
```

Например:

```text
✓ Completed
● Active
⚠ Warning
✗ Error
```

---

# 🎛️ 13. Этап 8 — Questionary

Теперь сделать меню интерактивным.

Вместо:

```text
1
2
3
4
```

получить:

```text
? What do you want to do?

❯ Add task
  Edit task
  Delete task
  Complete task
  Show tasks
  Exit
```

Пользователь перемещается стрелками.

---

# ➕ 14. Добавление задачи

Интерфейс:

```text
╭──────────────────────────────╮
│          NEW TASK            │
╰──────────────────────────────╯

? Task title: Learn Python

? Description:
  Study OOP and dataclasses

✓ Task created successfully!
```

---

# ✏️ 15. Редактирование задачи

После выбора задачи:

```text
╭──────────────────────────────╮
│          EDIT TASK            │
╰──────────────────────────────╯

Task: Learn Python

? What do you want to change?

❯ Rename
  Change description
  Mark as completed
  Back
```

---

# 🗑️ 16. Удаление

Перед удалением спросить подтверждение:

```text
? Delete "Learn Python"?

❯ Yes
  No
```

После удаления:

```text
✓ Task deleted successfully.
```

---

# 🧪 17. Этап 9 — Тестирование

## Цель

Научиться проверять код автоматически.

Использовать:

```text
pytest
```

---

## Создать

```text
tests/
├── test_task.py
├── test_todo_service.py
└── test_task_repository.py
```

---

## Проверить

### Task

* [ ] Task создаётся
* [ ] Поля имеют правильные значения
* [ ] Статус корректный

### Service

* [ ] Добавление работает
* [ ] Удаление работает
* [ ] Переименование работает
* [ ] Описание изменяется
* [ ] Completion работает

### Repository

* [ ] Create работает
* [ ] Get работает
* [ ] Get all работает
* [ ] Update работает
* [ ] Delete работает

---

## Запуск

```bash
pytest
```

---

# 🧹 18. Этап 10 — Полировка

Когда весь функционал готов, пройтись по проекту.

---

## Код

* [ ] Удалить дублирование
* [ ] Переименовать непонятные переменные
* [ ] Добавить type hints
* [ ] Проверить обработку ошибок
* [ ] Проверить структуру файлов
* [ ] Проверить импорты

---

## CLI

* [ ] Все сообщения выглядят одинаково
* [ ] Ошибки выделяются красным
* [ ] Успешные операции зелёным
* [ ] Есть понятная навигация
* [ ] Нет лишнего текста
* [ ] Интерфейс выглядит аккуратно

---

# 🚀 19. Дополнительные функции

После завершения основной версии можно выбрать несколько дополнительных функций.

## Приоритет

```text
🔴 High
🟡 Medium
🟢 Low
```

---

## Категории

```text
Study
Work
Personal
Other
```

---

## Поиск

```text
🔍 Search: python

1. Learn Python
2. Python project
3. Read Python book
```

---

## Фильтры

```text
All
Active
Completed
High priority
Today
```

---

## Дедлайн

Добавить:

```text
due_date
```

И отображать:

```text
⚠ Due today
```

---

## Сортировка

Добавить возможность:

```text
Sort by:

❯ Created
  Name
  Priority
  Deadline
  Status
```

---

# 🧠 20. Дополнительная задача — Command Pattern

Если после основной версии захочется усложнить проект, можно попробовать команды:

```text
/add
/delete
/edit
/list
/complete
```

Например:

```bash
todo add "Learn Python"
todo list
todo complete 3
todo delete 2
```

Тогда приложение сможет работать не только как интерактивный TUI, но и как настоящий CLI-инструмент.

---

# 📦 21. Финальная структура

После всех этапов проект должен выглядеть примерно так:

```text
todo-cli/
│
├── app/
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── todo_service.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── task_repository.py
│   │
│   └── cli/
│       ├── __init__.py
│       ├── menu.py
│       ├── screens.py
│       └── styles.py
│
├── data/
│   └── todo.db
│
├── tests/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_todo_service.py
│   └── test_task_repository.py
│
├── main.py
├── requirements.txt
├── README.md
├── ROADMAP.md
└── .gitignore
```

---

# 🏁 22. Definition of Done

Проект можно считать завершённым, когда:

* [ ] Можно создать задачу
* [ ] Можно посмотреть задачи
* [ ] Можно удалить задачу
* [ ] Можно переименовать задачу
* [ ] Можно изменить описание
* [ ] Можно завершить задачу
* [ ] Данные сохраняются в SQLite
* [ ] После перезапуска данные остаются
* [ ] CLI интерактивный
* [ ] CLI красиво оформлен через Rich
* [ ] Меню работает через Questionary
* [ ] Есть обработка ошибок
* [ ] Есть тесты
* [ ] Код разделён по модулям
* [ ] Есть README
* [ ] Проект можно запустить по инструкции

---

# 📈 23. Чему я научусь после проекта

После завершения проекта ты потрогаешь сразу несколько важных вещей:

```text
Python
 │
 ├── OOP
 ├── dataclasses
 ├── type hints
 ├── modules
 ├── packages
 ├── exceptions
 │
 ├── SQLite
 │   ├── SQL
 │   ├── CRUD
 │   └── persistence
 │
 ├── Architecture
 │   ├── Model
 │   ├── Service
 │   ├── Repository
 │   └── Separation of concerns
 │
 ├── CLI
 │   ├── Rich
 │   └── Questionary
 │
 └── Testing
     └── pytest
```

---

# 💡 24. Главное правило разработки

Не пытаться написать весь проект сразу.

Работать маленькими итерациями:

```text
1. Написал
      ↓
2. Запустил
      ↓
3. Проверил
      ↓
4. Исправил
      ↓
5. Закоммитил
      ↓
6. Следующая функция
```

Не переходить к следующему этапу, пока предыдущий нормально не работает.

---

# 🌱 25. Возможные версии проекта

## v0.1

Простой Python CLI.

```text
Add
Delete
Rename
Description
Complete
```

## v0.2

SQLite.

```text
Tasks survive restart
```

## v0.3

Rich.

```text
Beautiful terminal
```

## v0.4

Questionary.

```text
Interactive menus
```

## v0.5

Tests.

```text
pytest
```

## v1.0

Полноценный Todo CLI.

```text
Rich
+
Questionary
+
SQLite
+
Tests
+
Clean Architecture
```

---

# 🚀 26. После v1.0

Не обязательно останавливаться.

Следующий эксперимент:

**Сделать v2 на Textual.**

Тогда архитектура останется примерно той же:

```text
              TodoService
                   │
             ┌─────┴─────┐
             │           │
          CLI v1       TUI v2
          Rich        Textual
             │           │
             └─────┬─────┘
                   │
             TaskRepository
                   │
                SQLite
```

Таким образом ты увидишь очень важный принцип разработки:

> **Бизнес-логика приложения не должна зависеть от интерфейса.**

Сегодня у тебя CLI.

Завтра TUI.

А потом, если захочешь, даже Web UI.

А `Task`, `TodoService` и `TaskRepository` при этом можно оставить практически теми же.

---

# ✅ Финальный чек-лист

Перед публикацией проекта:

* [ ] Код работает
* [ ] SQLite работает
* [ ] Все CRUD операции работают
* [ ] CLI красивый
* [ ] Меню интерактивное
* [ ] Есть обработка ошибок
* [ ] Есть тесты
* [ ] Нет огромного `main.py`
* [ ] Код разделён по ответственности
* [ ] Есть `README.md`
* [ ] Есть `requirements.txt`
* [ ] Есть `.gitignore`
* [ ] Есть несколько Git commits
* [ ] Проект загружен на GitHub

---

## 🎓 Главная цель

Не просто сделать Todo List.

Главная цель проекта — пройти путь:

```text
"Я знаю Python"
        ↓
"Я умею писать программу"
        ↓
"Я умею разделять код"
        ↓
"Я умею работать с БД"
        ↓
"Я умею строить CLI"
        ↓
"Я умею тестировать код"
        ↓
"Я понимаю базовую архитектуру приложения"
```

Todo List — маленький проект, но если сделать его именно таким способом, он становится отличным учебным проектом.

