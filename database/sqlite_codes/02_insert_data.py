import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Insert a single user
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

# Insert multiple users
users = [("Bob", 25), ("Charlie", 35), ("David", 40)]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)

conn.commit()
conn.close()
