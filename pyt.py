import mysql.connector

db = mysql.connector.connect(
    host='localhost',   # use the correct port here
    port=3307,
    user='root',
    password='root',
    database='ter'
)

cursor = db.cursor()
cursor.execute("SELECT * from users;")
result = cursor.fetchone()
print(result)
