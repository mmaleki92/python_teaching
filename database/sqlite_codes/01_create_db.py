import sqlite3

# Connect to a new or existing database
conn = sqlite3.connect('example.db')

# Create a new table
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')
conn.commit()
conn.close()
