import sqlite3

connect_to_db = sqlite3.connect("iris.db")

db_cursor = connect_to_db.cursor()

add_data_to_db = """insert into iris_data (sepal_length,sepal_width,
petal_length,petal_width,class) values (?,?,?,?,?);
"""

f = open("Iris - all-numbers.csv","r")
header_line = f.readline()
for line in f:#\n
    line = line.strip()#removes \n
    line = line.split(",")#creates a list - splits on comma
    line = tuple(line)
    
    db_cursor.execute(add_data_to_db,line)
    connect_to_db.commit()
#close connections
db_cursor.close()