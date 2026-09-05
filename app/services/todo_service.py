from app.models.task import Task


class TodoService:
    def __init__(self,db):
        # здесь будет храниться список задач
        self.db = db

    def add_task(self, title, description):
        task = Task(None , title, description)
        self.db.insert_task(task)
        task.id = self.db.cursor.lastrowid
        return task

    def get_task(self, task_id):
        task = self.db.get_task(task_id)
        if task is None:
            return None
        
        return Task.from_row(task)


        
    def get_all_tasks(self):
        rows = self.db.get_all_tasks()
        tasks = []
        for row in rows:
            tasks.append(Task.from_row(row))
        return tasks

    def delete_task(self, task_id):
        row = self.db.get_task(task_id)
        if row is None:
            return None
        task = Task.from_row(row)
        self.db.delete_task(task)
        return task

        
    def rename_task(self, task_id, new_title):
        row = self.db.get_task(task_id)
        if row is None:
            return None
        task = Task.from_row(row)
        task.title = new_title
        self.db.update_task(task)

        return task

    def update_description(self, task_id, new_description):
        row = self.db.get_task(task_id)
        if row is None:
            return None
        task = Task.from_row(row)
        task.description = new_description
        self.db.update_task(task)

        return task

    def complete_task(self, task_id):
        row = self.db.get_task(task_id)
        if row is None:
            return None
        task = Task.from_row(row)
        task.completed = True
        self.db.update_task(task)

        return task

