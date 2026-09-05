from datetime import datetime

from app.models.task import Task

def test_create_table(db):
    db.create_table()
    result = db.cursor.execute(
        "SELECT * FROM sqlite_master WHERE type = 'table' AND name = ?",
    ("tasks",)
    ).fetchone()

    assert result is not None 
    
    

def test_insert_task(db):
   
    task = Task(
        100,
        "Task Title",
        "Task Description"
    )

    db.insert_task(task)

    result = db.cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (100,)
    ).fetchone()   

    assert result is not None
    assert result[0] == 100
    assert result[1] == "Task Title"
    assert result[2] == "Task Description"

def test_get_task(db):
    db.create_table()

    task = Task(
        100,
        "Test",
        "Test"
    )

    db.insert_task(task)

    result = db.get_task(100)

    assert result[0] == task.id
    assert result[1] == task.title
    assert result[2] == task.description
    assert result[3] == task.completed

def test_get_task_not_found(db):
    db.create_table()

    result = db.get_task(999)

    assert result is None

def test_get_all_tasks(db):
    db.create_table()

    task = Task(
        1,
        "First",
        "Comment"
    )
    task1 = Task(
        2,
        "Second",
        "Comment2"
    )

    db.insert_task(task)
    db.insert_task(task1)

    result = db.get_all_tasks()

    assert len(result) == 2
    assert result[0][0] == 1
    assert result[0][1] == "First"
    assert result[0][2] == "Comment"
    assert result[1][0] == 2
    assert result[1][1] == "Second"
    assert result[1][2] == "Comment2"

def test_get_all_tasks_empty(db):
    db.create_table()
    result = db.get_all_tasks()

    assert result == []
    
def test_delete_task(db):
    db.create_table()
    task = Task(
        1,
        "First",
        "Comment"
    )
    task1 = Task(
        2,
        "Second",
        "Comment2"
    )

    db.insert_task(task)
    db.insert_task(task1)
    db.delete_task(task)
    result = db.get_all_tasks()

    assert len(result) == 1
    assert result[0][0] == 2
    assert result[0][1] == "Second"
    assert result[0][2] == "Comment2"

def test_delete_task_empty(db):
    db.create_table()
    task = Task(
        1,
        "First",
        "Comment"
    )
    db.delete_task(task)
    result = db.get_all_tasks()

    assert result == []

def test_update_task(db):
    db.create_table()
    task = Task(
        1,
        "OLD Title",
        "OLD Description",
        False
    )
    task2 = Task(
        1,
        "NEW Title",
        "NEW Description",
        True
    )
    db.insert_task(task)
    db.update_task(task2)
    result = db.get_task(1)

    assert result[0] == 1
    assert result[1] == "NEW Title"
    assert result[2] == "NEW Description"
    assert result[3] == True

def test_update_task_not_found(db):
    db.create_table()
    task = Task(
        1,
        "OLD Title",
        "OLD Description",
        False
    )
    task2 = Task(
        999,
        "NEW Title",
        "NEW Description",
        True
    )
    db.insert_task(task)
    db.update_task(task2)
    result = db.get_all_tasks()

    assert len(result) == 1
    assert result[0][0] == 1
    assert result[0][1] == "OLD Title"
    assert result[0][2] == "OLD Description"
    assert result[0][3] == False
 
def test_task_from_row():
    row = (1, "First", "Comment", 0, "2026-09-03T12:34:56.789012")
    result = Task.from_row(row)

    assert result.id == 1
    assert result.title == "First"
    assert result.description == "Comment"
    assert result.completed is False
    assert result.created_at == datetime.fromisoformat("2026-09-03T12:34:56.789012")
    assert isinstance(datetime(2026, 9, 3, 12, 34, 56, 789012),datetime)

