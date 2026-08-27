
import re

from app.models.task import Task

class TodoService:
    def __init__(self):
        # здесь будет храниться список задач
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = Task(self.next_id,title,description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        
        return None

    def get_all_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
            # list.remove(self.tasks,task)
                self.tasks.remove(task)
                return task
        

    def rename_task(self, task_id, new_title):
        # task_for_editing = TodoService.get_task(self,task_id)
        task_for_editing = self.get_task(task_id)
        if task_for_editing is None:
            return None

        task_for_editing.title = new_title
        return task_for_editing


    def update_description(self, task_id, new_description):
        task_for_editing = self.get_task(task_id)
        if task_for_editing is None:
            return None

        task_for_editing.description = new_description
        return task_for_editing


    def complete_task(self, task_id):
        task = self.get_task(task_id)
        if task is None:
            return None

        task.completed = True
        return task



        
service = TodoService()
service.add_task("First","Testing the description")
service.add_task("Second","Testing the description")
service.add_task("Third","Testing the description")
# Debugging
# task = service.update_description(1,"NEW DESCRIPT")
# task2 = service.get_all_tasks()
# print(task2)
task = service.complete_task(1)
print(task.completed)
