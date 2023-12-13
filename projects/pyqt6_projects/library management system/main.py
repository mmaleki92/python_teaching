import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox
from db_model import init_db, add_book_to_db, get_all_books, delete_book_from_db

class LibrarySystem(QWidget):
    def __init__(self):
        super().__init__()
        self.book_ids = {}  # Dictionary to map list items to book IDs
        init_db()
        self.initUI()
        self.loadBooks()

    def initUI(self):
        self.setWindowTitle('Library Management System')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Book Title Input
        self.bookTitleInput = QLineEdit(self)
        self.bookTitleInput.setPlaceholderText('Enter book title')
        layout.addWidget(self.bookTitleInput)

        # Add Button
        self.addButton = QPushButton('Add Book', self)
        self.addButton.clicked.connect(self.addBook)
        layout.addWidget(self.addButton)

        # List of Books
        self.booksList = QListWidget(self)
        layout.addWidget(self.booksList)

        # Delete Button
        self.deleteButton = QPushButton('Delete Selected Book', self)
        self.deleteButton.clicked.connect(self.deleteBook)
        layout.addWidget(self.deleteButton)

        self.setLayout(layout)

    def addBook(self):
        book_title = self.bookTitleInput.text()
        if book_title:
            add_book_to_db(book_title)  # Add book to the database
            self.loadBooks()  # Reload the list of books
            self.bookTitleInput.clear()
        else:
            QMessageBox.information(self, 'Error', 'Please enter a book title')

    def loadBooks(self):
        self.booksList.clear()
        self.book_ids.clear()
        for book_id, title in get_all_books():
            self.booksList.addItem(title)
            self.book_ids[title] = book_id  # Map the title to its book ID

    def deleteBook(self):
        selected_item = self.booksList.currentItem()
        if selected_item:
            book_title = selected_item.text()
            book_id = self.book_ids[book_title]
            delete_book_from_db(book_id)
            self.loadBooks()
        else:
            QMessageBox.information(self, 'Error', 'Please select a book to delete')

def main():
    app = QApplication(sys.argv)
    ex = LibrarySystem()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
