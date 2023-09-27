import sqlite3

# Establishing a connection
conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

# Create the tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    balance FLOAT DEFAULT 0.0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    price FLOAT NOT NULL,
    inventory INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    book_id INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
)
''')
conn.commit()

# Let's add a book and a user
cursor.execute("INSERT INTO users (name, age, balance) VALUES (?, ?, ?)", ("Alice", 30, 100.0))
cursor.execute("INSERT INTO books (title, price, inventory) VALUES (?, ?, ?)", ("Fantastic Beasts", 20.0, 10))
conn.commit()

# Simulate a purchase
user_id = 1
book_id = 1
book_price_query = cursor.execute("SELECT price, inventory FROM books WHERE id=?", (book_id,)).fetchone()
book_price = book_price_query[0]
book_inventory = book_price_query[1]

user_balance_query = cursor.execute("SELECT balance FROM users WHERE id=?", (user_id,)).fetchone()
user_balance = user_balance_query[0]

# Check if the user can afford the book and if the book is in stock
if user_balance >= book_price and book_inventory > 0:
    try:
        # Reduce book inventory
        cursor.execute("UPDATE books SET inventory = inventory - 1 WHERE id=?", (book_id,))
        # Deduct book price from user's balance
        cursor.execute("UPDATE users SET balance = balance - ? WHERE id=?", (book_price, user_id))
        # Record the purchase
        cursor.execute("INSERT INTO purchases (user_id, book_id) VALUES (?, ?)", (user_id, book_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()
else:
    print("Either the book is out of stock or the user doesn't have enough balance.")
    
conn.close()
