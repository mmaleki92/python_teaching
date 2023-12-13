import sqlite3

def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            author_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            isbn TEXT,
            quantity INTEGER DEFAULT 1,
            FOREIGN KEY (author_id) REFERENCES authors (author_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INTEGER PRIMARY KEY,
            book_id INTEGER,
            member_id INTEGER,
            due_date DATE,
            returned_date DATE,
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inside_outside (
            book_id INTEGER PRIMARY KEY,
            status TEXT CHECK( status IN ('inside','outside') ) NOT NULL DEFAULT 'inside',
            FOREIGN KEY (book_id) REFERENCES books (book_id)
        )
    ''')

    conn.commit()
    conn.close()


def add_book_to_db(title, author, isbn, quantity):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Assuming you have a way to handle or add authors in your authors table, get the author_id
    # Here's a simple way to get or add an author (requires modification based on your schema)
    cursor.execute('SELECT author_id FROM authors WHERE name = ?', (author,))
    author_id = cursor.fetchone()
    if not author_id:
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (author,))
        author_id = cursor.lastrowid
    else:
        author_id = author_id[0]

    # Now insert the book details
    cursor.execute('INSERT INTO books (title, author_id, isbn, quantity) VALUES (?, ?, ?, ?)', 
                   (title, author_id, isbn, quantity))

    # Add an entry to inside_outside table
    book_id = cursor.lastrowid
    cursor.execute('INSERT INTO inside_outside (book_id, status) VALUES (?, "inside")', (book_id,))

    conn.commit()
    conn.close()




def get_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT books.book_id, books.title, authors.name, books.isbn, books.quantity 
        FROM books 
        LEFT JOIN authors ON books.author_id = authors.author_id
    ''')
    books = cursor.fetchall()
    conn.close()
    return books


def delete_book_from_db(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
    conn.commit()
    conn.close()

def borrow_book(book_id, member_id, due_date):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # First, check if the book is already borrowed
    cursor.execute('SELECT status FROM inside_outside WHERE book_id = ?', (book_id,))
    status_result = cursor.fetchone()
    if status_result and status_result[0] == 'outside':
        conn.close()
        return "Book is already borrowed"

    # Proceed to borrow the book
    cursor.execute('UPDATE inside_outside SET status = "outside" WHERE book_id = ?', (book_id,))
    cursor.execute('INSERT INTO loans (book_id, member_id, due_date) VALUES (?, ?, ?)', (book_id, member_id, due_date))
    conn.commit()
    conn.close()
    return "Book borrowed successfully"

def return_book(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Update the loans table to set the returned_date to today
    cursor.execute('UPDATE loans SET returned_date = CURRENT_DATE WHERE book_id = ? AND returned_date IS NULL', (book_id,))

    # Update the inside_outside table to set the status back to 'inside'
    cursor.execute('UPDATE inside_outside SET status = "inside" WHERE book_id = ?', (book_id,))

    conn.commit()
    conn.close()
