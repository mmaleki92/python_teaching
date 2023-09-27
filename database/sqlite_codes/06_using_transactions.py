import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Eve", 50))
    # Some other operations...
    cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
    conn.commit()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
    conn.rollback()

conn.close()
