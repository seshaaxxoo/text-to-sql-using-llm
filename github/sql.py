import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Seshathri3@",
    database="student"
)
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS stduents ("
               "id VARCHAR(10) PRIMARY KEY,"
               "name VARCHAR(255) NOT NULL,"
               "age INT NOT NULL,"
               "marks INT NOT NULL)")

data = [
    ('42111191', 'Seshathri', 21, 87),
    ('42110497', 'Karthick',  21, 66),
    ('42111229', 'Sheryas',   21, 85),
    ('42111274', 'Shailesh',  22, 90),
    ('42111295', 'Subha',     21, 80),
    ('42111300', 'Arun',      20, 75),
    ('42111301', 'Priya',     22, 92),
    ('42111302', 'Ravi',      21, 55),
    ('42111303', 'Meena',     23, 88),
    ('42111304', 'Deepak',    20, 70),
]

cursor.executemany(
    "INSERT IGNORE INTO students (id, name, age, marks) VALUES (%s, %s, %s, %s)",
    data
)

connection.commit()

cursor.execute("SELECT * FROM students ORDER BY id DESC")

connection.close()
