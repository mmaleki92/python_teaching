import sqlite3

class LibraryCatalog:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.create_table()

    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS Books (
                BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Genre TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def add_book(self, title, author, genre):
        self.conn.execute('INSERT INTO Books (Title, Author, Genre) VALUES (?, ?, ?)', (title, author, genre))
        self.conn.commit()

    def view_books(self):
        cursor = self.conn.execute('SELECT * FROM Books WHRER brand= ?')
        return cursor.fetchall()



    def update_book(self, book_id, title, author, genre):
        self.conn.execute('UPDATE Books SET Title = ?, Author = ?, Genre = ? WHERE BookID = ?', (title, author, genre, book_id))
        self.conn.commit()

    def delete_book(self, book_id):
        self.conn.execute('DELETE FROM Books WHERE BookID = ?', (book_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# Usage
library = LibraryCatalog()
library.add_book('1984', 'George Orwell', 'Dystopian')
library.add_book('To Kill a Mockingbird', 'Harper Lee', 'Classic')
print(library.view_books())
library.update_book(1, '1984', 'George Orwell', 'Political Fiction')
library.delete_book(2)
