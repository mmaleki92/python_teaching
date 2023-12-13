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
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
    ''')

    conn.commit()
    conn.close()


def add_book_to_db(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title) VALUES (?)', (title,))
    conn.commit()
    conn.close()

def get_all_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT book_id, title FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book_from_db(book_id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
    conn.commit()
    conn.close()