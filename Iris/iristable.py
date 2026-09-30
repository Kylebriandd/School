import sqlite3

connect_to_db = sqlite3.connect("iris.db")

db_cursor = connect_to_db.cursor()

create_table = """create table if not exists iris_data(
sepal_id INTEGER PRIMARY KEY AUTOINCREMENT,
sepal_length REAL NOT NULL,
sepal_width REAL NOT NULL,
petal_length REAL NOT NULL,
petal_width REAL NOT NULL,
class INTEGER NOT NULL
) STRICT
"""

db_cursor.execute(create_table)

connect_to_db.commit()