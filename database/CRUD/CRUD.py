import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor method of the connection
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Name TEXT,
        Email TEXT
    )
''')

conn.commit()

def create_user(name, email):
    cursor.execute('INSERT INTO Users (Name, Email) VALUES (?, ?)', (name, email))
    conn.commit()

create_user('John Doe', 'johndoe@example.com')

def read_users():
    cursor.execute('SELECT * FROM Users')
    return cursor.fetchall()

users = read_users()
for user in users:
    print(user)

def update_user(user_id, name, email):
    cursor.execute('UPDATE Users SET Name = ?, Email = ? WHERE UserID = ?', (name, email, user_id))
    conn.commit()

update_user(1, 'Jane Doe', 'janedoe@example.com')

def delete_user(user_id):
    cursor.execute('DELETE FROM Users WHERE UserID = ?', (user_id,))
    conn.commit()

delete_user(1)


conn.close()
