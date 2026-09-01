import sqlite3


class SQLiteDatabase:
    def __init__(self,db_path="data/todo.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with open("sql/schema.sql", "r") as file:
            schema = file.read()

        self.cursor.executescript(schema)
        self.commit()

    def insert_task(self, task):
        self.cursor.execute(
            """INSERT INTO tasks VALUES (?,?,?,?,?) """,
            (
                task.id,
                task.title,
                task.description,
                task.completed,
                task.created_at,
            ),
        )
        self.commit()

    def get_task(self, task_id):
        self.cursor.execute(
            "SELECT * FROM tasks WHERE id= ?",
            (task_id,),
        )
        return self.cursor.fetchone()

    def get_all_tasks(self):
        self.cursor.execute(
            "SELECT * FROM tasks"
        )
        return self.cursor.fetchall()

    def update_task(self, task):
        self.cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
            (task.title,task.description,task.completed, task.id)
        )
        self.commit()

    def delete_task(self, task):
        self.cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task.id,)
        )
        self.commit()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


