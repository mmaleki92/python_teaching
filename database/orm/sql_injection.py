# This is a hypothetical, vulnerable piece of code for illustrative purposes only.
import sqlite3
import sqlite3

def setup_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create the 'users' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)
    
    # Insert some sample data
    users = [
        ('alice', 'password123'),
        ('bob', 'securepass'),
        ('eve', 'password456')
    ]

    cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)
    conn.commit()
    conn.close()

setup_db()

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return "Login successful!"
    else:
        return "Login failed!"

f = login("' OR '1' = '1' -- ", "23")
print(f)
# the -- is a comment so it would ignore the code
# SELECT * FROM users WHERE username='' OR '1' = '1' -- ' AND password='whatever'

# prevention:
def secure_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Secure SQL query using parameterized statements
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    if user:
        return "Login successful!"
    else:
        return "Login failed!"
