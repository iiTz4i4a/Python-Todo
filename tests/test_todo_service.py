from app.services.todo_service import TodoService


def test_add_task():
    service = TodoService()
    task = service.add_task("Test Creating The Task", "Test Creating The Description")

    assert task.id == 1
    assert task.title == "Test Creating The Task"
    assert task.description == "Test Creating The Description"
    assert task.completed is False


def test_get_task():
    service = TodoService()

    service.add_task("Test Creating The Task", "Test Creating The Description")

    task = service.get_task(1)

    assert task.id == 1
    assert task.title == "Test Creating The Task"
    assert task.description == "Test Creating The Description"
    assert task.completed is False


def test_get_all_tasks():
    service = TodoService()
    service.add_task("Creating First Task", "First Description")
    service.add_task("Creating Second Task", "Second Description")
    service.add_task("Creating Third Task", "Third Description")
    service.add_task("Creating Fourth Task", "Fourth Description")
    service.add_task("Creating Fifth Task", "Fifth Description")

    tasks = service.get_all_tasks()

    assert len(tasks) == 5
    assert tasks[0].title == "Creating First Task"
    assert tasks[0].description == "First Description"
    assert tasks[1].title == "Creating Second Task"
    assert tasks[1].description == "Second Description"
    assert tasks[2].title == "Creating Third Task"
    assert tasks[2].description == "Third Description"
    assert tasks[3].title == "Creating Fourth Task"
    assert tasks[3].description == "Fourth Description"
    assert tasks[4].title == "Creating Fifth Task"
    assert tasks[4].description == "Fifth Description"


def test_delete_task():
    service = TodoService()
    service.add_task("Creating First Task", "First Description")

    task = service.delete_task(1)
    tasks = service.get_all_tasks()

    assert len(tasks) == 0
    assert task.id == 1
    assert task.title == "Creating First Task"
    assert task.description == "First Description"


def test_rename_task():
    service = TodoService()
    service.add_task("Creating First Task", "First Description")
    service.rename_task(1, "Renamed Title")

    task = service.get_task(1)

    assert task.title == "Renamed Title"
    assert task.description == "First Description"
    assert task.id == 1


def test_update_description_task():
    service = TodoService()
    service.add_task("Creating First Task", "First Description")
    service.update_description(1, "Renamed Description")

    task = service.get_task(1)

    assert task.title == "Creating First Task"
    assert task.description == "Renamed Description"
    assert task.id == 1


def test_complete_task():
    service = TodoService()
    service.add_task("Creating First Task", "First Description")
    service.complete_task(1)

    task = service.get_task(1)

    assert task.id == 1
    assert task.title == "Creating First Task"
    assert task.description == "First Description"
    assert task.completed == True
