import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "John Doe"))

connection.commit()

connection.close()
