import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
conn.commit()
conn.close()
