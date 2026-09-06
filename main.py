import questionary

from app.cli.menu import run_menu
from app.cli.screens import show_tasks
from app.database.sqlite import SQLiteDatabase
from app.services.todo_service import TodoService

DB_PATH = "./data/todo.db"

STYLE_ACTION = "bold italic fg:green"
STYLE_WARN = "bold italic fg:darkred"


def ask_task_id(service):
    """Повернуть валидный task_id (int) для существующей задачи,
    или None, если пользователь отменил ввод (Ctrl+C) или ввёл неверный id."""
    task_id = questionary.text("Enter Task ID:").ask()
    if task_id is None:
        return None
    try:
        task_id = int(task_id)
    except ValueError:
        questionary.print("Wrong input, enter Task ID", style=STYLE_WARN)
        return None
    if service.get_task(task_id) is None:
        questionary.print("Wrong input, enter Task ID that exist", style=STYLE_WARN)
        return None
    return task_id


def ask_nonempty(prompt, error_msg):
    """Запросить непустую строку.

    Возвращает введённую строку, или None, если пользователь отменил ввод (Ctrl+C).
    """
    value = questionary.text(prompt).ask()
    while not value:
        if value is None:  # Ctrl+C - отмена
            return None
        questionary.print(error_msg, style=STYLE_WARN)
        value = questionary.text(prompt).ask()
    return value


def handle_add_task(service):
    questionary.print("Adding Task", style=STYLE_ACTION)
    title = ask_nonempty("Task Title: ", "Task title cannot be empty")
    if title is None:
        return
    description = ask_nonempty("Task Description: ", "Description cannot be empty")
    if description is None:
        return
    service.add_task(title, description)
    questionary.print("Task was successfully created", style=STYLE_ACTION)


def handle_remove_task(service):
    questionary.print("Removing Task", style=STYLE_WARN)
    task_id = ask_task_id(service)
    if task_id is None:
        return
    service.delete_task(task_id)


def handle_complete_task(service):
    questionary.print("Completing Task", style=STYLE_ACTION)
    task_id = ask_task_id(service)
    if task_id is None:
        return
    service.complete_task(task_id)


def handle_rename_task(service):
    questionary.print("Changing Task Title", style=STYLE_WARN)
    task_id = ask_task_id(service)
    if task_id is None:
        return
    new_title = ask_nonempty("Enter New Task Title", "New Task title cannot be empty")
    if new_title is None:
        return
    service.rename_task(task_id, new_title)


def handle_change_description(service):
    questionary.print("Changing Task Description", style=STYLE_WARN)
    task_id = ask_task_id(service)
    if task_id is None:
        return
    new_description = ask_nonempty(
        "Enter New Description", "New Description cannot be empty"
    )
    if new_description is None:
        return
    service.update_description(task_id, new_description)


HANDLERS = {
    "Add Task": handle_add_task,
    "Remove Task": handle_remove_task,
    "Complete Task": handle_complete_task,
    "Change Title": handle_rename_task,
    "Change Description": handle_change_description,
}


def main():
    database = SQLiteDatabase(DB_PATH)
    database.create_table()
    service = TodoService(database)
    try:
        while True:
            show_tasks(service.get_all_tasks())
            choice = run_menu()

            if choice == "Exit":
                break

            if choice is None:
                questionary.print(
                    "Action was not selected, closing the app", style=STYLE_WARN
                )
                break

            handler = HANDLERS.get(choice)
            if handler is None:
                questionary.print(f"Unknown action: {choice}", style=STYLE_WARN)
                continue
            handler(service)
    finally:
        database.close()


if __name__ == "__main__":
    main()
