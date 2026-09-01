import pytest

from app.database.sqlite import SQLiteDatabase


@pytest.fixture
def db(tmp_path):
    db_path = tmp_path / "test.db"
    database = SQLiteDatabase(db_path)
    database.create_table()
    yield database
    database.close()
