import questionary

from app.cli.menu import run_menu
from app.cli.screens import show_tasks
from app.database.sqlite import SQLiteDatabase
from app.services.todo_service import TodoService


def main():
    db_path = "./data/todo.db"
    database = SQLiteDatabase(db_path)
    database.create_table()
    service = TodoService(database)
    try:
        while True:
            show_tasks(service.get_all_tasks())
            choice = run_menu()

            if choice == "Add Task":
                questionary.print("Adding Task", style="bold italic fg:green")

                title = questionary.text("Task Title: ").ask()
                while not title:
                    if title is None:          # Ctrl+C - отмена
                        return
                    questionary.print("Task title cannot be empty", style="bold italic fg:darkred")
                    title = questionary.text("Task Title: ").ask()

                description = questionary.text("Task Description: ").ask()
                while not description:
                    if description is None:   # Ctrl+C - отмена
                        return
                    questionary.print("Description cannot be empty", style="bold italic fg:darkred")
                    description = questionary.text("Task Description: ").ask()

                service.add_task(title, description)
                questionary.print("Task was successfully created", style="bold italic fg:green")

            elif choice == "Remove Task":
                questionary.print("Removing Task", style="bold italic fg:darkred")
                try:
                    task_id = questionary.text("Enter Task ID:").ask() 
                    if task_id is None:
                        questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
                        return
                    task_exist = service.get_task(int(task_id))
                    # print(task_exist)
                    if task_exist is None:
                        questionary.print("Wrong input , enter Task ID that exist", style="bold italic fg:darkred")
                    else:
                        service.delete_task(int(task_id))
                except ValueError:
                    questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")

            elif choice == "Complete Task":
                questionary.print("Completing Task", style="bold italic fg:darkred")
                try:
                    task_id = questionary.text("Enter Task ID:").ask() 
                    if task_id is None:
                        questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
                        return
                    task_exist = service.get_task(int(task_id))
                    if task_exist is None:
                        questionary.print("Wrong input , enter Task ID that exist", style="bold italic fg:darkred")
                    else:
                        service.complete_task(int(task_id))
                except ValueError:
                    questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
            elif choice == "Change Title":
                questionary.print("Changing Task Title", style="bold italic fg:darkred")
                try:
                    task_id = questionary.text("Enter Task ID:").ask() 
                    if task_id is None:
                        questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
                        return
                    task_exist = service.get_task(int(task_id))
                    if task_exist is None:
                        questionary.print("Wrong input , enter Task ID that exist", style="bold italic fg:darkred")
                    else:
                        new_title = questionary.text("Enter New Task Title").ask()
                        while not new_title:
                            if new_title is None:          # Ctrl+C - отмена
                                return
                            questionary.print("New Task title cannot be empty", style="bold italic fg:darkred")
                            new_title = questionary.text("Enter New Task Title").ask()
                        
                        service.rename_task(task_id,new_title)

                except ValueError:
                    questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
            elif choice == "Change Description":
                questionary.print("Changing Task Description", style="bold italic fg:darkred")
                try:
                    task_id = questionary.text("Enter Task ID:").ask() 
                    if task_id is None:
                        questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
                        return
                    task_exist = service.get_task(int(task_id))
                    if task_exist is None:
                        questionary.print("Wrong input , enter Task ID that exist", style="bold italic fg:darkred")
                    else:
                        new_description = questionary.text("Enter New Description Title").ask()
                        while not new_description:
                            if new_description is None:          # Ctrl+C - отмена
                                return
                            questionary.print("New Description title cannot be empty", style="bold italic fg:darkred")
                            new_description = questionary.text("Enter New Description Title").ask()

                        service.update_description(task_id,new_description)

                except ValueError:
                    questionary.print("Wrong input , enter Task ID", style="bold italic fg:darkred")
   
            elif choice == "Exit":
                break
            elif choice is None:
                questionary.print("Action was not selected, closing the app", style="bold italic fg:darkred")

    finally:
        database.close()


if __name__ == "__main__":
    main()
