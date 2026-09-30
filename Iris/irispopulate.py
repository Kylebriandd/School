import sqlite3
import data_analytics

connect_to_db = sqlite3.connect("iris.db")

db_cursor = connect_to_db.cursor()


get_data_from_db = """
select sepal_length from iris_data;
"""

db_cursor.execute(get_data_from_db)
data = db_cursor.fetchall()

sepal_length_list = []
for data_point in data:
    sepal_length_list.append(data_point[0])
    
print(sepal_length_list)

average_sepal_length = data_analytics.calc_average(sepal_length_list)

print(f"The average sepal length is: {average_sepal_length}")

db_cursor.close()
connect_to_db.close()