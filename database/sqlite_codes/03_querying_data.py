import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Select all users
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()
for user in all_users:
    print(user)

# Select users with specific criteria
cursor.execute("SELECT name, age FROM users WHERE age >= 30")
older_users = cursor.fetchall()
for user in older_users:
    print(user)

conn.close()
