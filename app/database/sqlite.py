import sqlite3


class SQLiteDatabase:
    def __init__(self):
        self.connection = sqlite3.connect("../../data/todo.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        with open("../../sql/schema.sql", "r") as file:
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
            """SELECT * FROM tasks WHERE id=(?)""",
            (task_id,)
        return self.cursor.fetchone()

    def get_all_tasks(self):
        pass

    def update_task(self, task):
        pass

    def delete_task(self, task):
        pass

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()
