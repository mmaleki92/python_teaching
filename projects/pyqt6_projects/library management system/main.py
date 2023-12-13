import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox
from db_model import init_db, add_book_to_db, get_all_books, delete_book_from_db, borrow_book, return_book
from PyQt5.QtWidgets import QLabel, QDateEdit, QDateTimeEdit
from PyQt5.QtWidgets import QGroupBox, QGridLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from datetime import datetime

from PyQt5.QtWidgets import QDialog, QFormLayout, QDialogButtonBox

class AddBookDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Book")
        self.layout = QFormLayout(self)

        # Book details fields
        self.titleInput = QLineEdit(self)
        self.layout.addRow("Title:", self.titleInput)
        
        self.authorInput = QLineEdit(self)
        self.layout.addRow("Author:", self.authorInput)

        self.isbnInput = QLineEdit(self)
        self.layout.addRow("ISBN:", self.isbnInput)

        self.quantityInput = QLineEdit(self)
        self.layout.addRow("Quantity:", self.quantityInput)

        # Dialog buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def getBookDetails(self):
        return (self.titleInput.text(), self.authorInput.text(), self.isbnInput.text(), self.quantityInput.text())

class BorrowBookDialog(QDialog):
    def __init__(self, selected_book_title, book_ids, parent=None):
        super().__init__(parent)
        self.selected_book_title = selected_book_title
        self.book_ids = book_ids  # This should be a dictionary
        self.setWindowTitle("Borrow Book")
        self.layout = QFormLayout(self)

        # Borrower ID and Due Date
        self.memberIdInput = QLineEdit(self)
        self.dueDateInput = QDateEdit(self)
        self.dueDateInput.setCalendarPopup(True)
        self.dueDateInput.setDateTime(datetime.now())

        self.layout.addRow("Member ID:", self.memberIdInput)
        self.layout.addRow("Due Date:", self.dueDateInput)

        self.book_ids = book_ids  # Dictionary of book titles to IDs

        # Dialog buttons
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        self.layout.addWidget(self.buttons)

    def getBorrowDetails(self):
        book_id = self.book_ids.get(self.selected_book_title)  # Safely get the book ID
        member_id = self.memberIdInput.text()
        due_date = self.dueDateInput.date().toString("yyyy-MM-dd")
        return (book_id, member_id, due_date)


class LibrarySystem(QWidget):
    def __init__(self):
        super().__init__()
        self.book_ids = {}  # Dictionary to map list items to book IDs
        init_db()
        self.initUI()
        self.loadBooks()

    def initUI(self):
        self.setWindowTitle('Library Management System')
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        # Group Box for Book Details
        bookDetailsGroup = QGroupBox("Book Details")
        bookDetailsLayout = QGridLayout()

        # Add Book Dialog Button
        self.addBookDialogButton = QPushButton('Add New Book', self)
        self.addBookDialogButton.clicked.connect(self.openAddBookDialog)
        layout.addWidget(self.addBookDialogButton)

        # Borrow Book Dialog Button
        self.borrowBookDialogButton = QPushButton('Borrow Book', self)
        self.borrowBookDialogButton.clicked.connect(self.openBorrowBookDialog)
        layout.addWidget(self.borrowBookDialogButton)

        self.deleteButton = QPushButton('Delete Selected Book', self)
        self.deleteButton.clicked.connect(self.deleteBook)
        layout.addWidget(self.deleteButton)


        self.setLayout(layout)
        # Return Book Button
        self.returnBookButton = QPushButton('Return Selected Book', self)
        self.returnBookButton.clicked.connect(self.returnBook)
        layout.addWidget(self.returnBookButton)

        # Initialize the table
        self.booksTable = QTableWidget(self)
        self.booksTable.setColumnCount(4)  # For title, author, ISBN, quantity
        self.booksTable.setHorizontalHeaderLabels(["Title", "Author", "ISBN", "Quantity"])
        self.booksTable.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.booksTable)

    def returnBook(self):
        selected_row = self.booksTable.currentRow()
        if selected_row != -1:
            book_title = self.booksTable.item(selected_row, 0).text()
            book_id = self.book_ids[book_title]

            return_book(book_id)
            QMessageBox.information(self, 'Return Book', 'Book returned successfully')
            self.loadBooks()
        else:
            QMessageBox.information(self, 'Error', 'Please select a book to return')

    def addBook(self):
        book_title = self.bookTitleInput.text()
        if book_title:
            add_book_to_db(book_title)  # Add book to the database
            self.loadBooks()  # Reload the list of books
            self.bookTitleInput.clear()
        else:
            QMessageBox.information(self, 'Error', 'Please enter a book title')

    def loadBooks(self):
        self.booksTable.setRowCount(0)  # Clear the table
        for book_id, title, author, isbn, quantity in get_all_books():
            row_position = self.booksTable.rowCount()
            self.booksTable.insertRow(row_position)

            self.booksTable.setItem(row_position, 0, QTableWidgetItem(title))
            self.booksTable.setItem(row_position, 1, QTableWidgetItem(author))
            self.booksTable.setItem(row_position, 2, QTableWidgetItem(isbn))
            self.booksTable.setItem(row_position, 3, QTableWidgetItem(str(quantity)))

            self.book_ids[title] = book_id  # Use title as key; consider using book_id for uniqueness

    def deleteBook(self):
        selected_item = self.booksList.currentItem()
        if selected_item:
            book_title = selected_item.text()
            book_id = self.book_ids[book_title]
            delete_book_from_db(book_id)
            self.loadBooks()
        else:
            QMessageBox.information(self, 'Error', 'Please select a book to delete')

    def borrowBook(self):
        selected_row = self.booksTable.currentRow()
        if selected_row != -1:
            book_title = self.booksTable.item(selected_row, 0).text()  # Assuming the first column is the title
            book_id = self.book_ids[book_title]
            member_id = self.memberIdInput.text()
            due_date = self.dueDateInput.date().toString("yyyy-MM-dd")

            book_id = int(book_id)

            response = borrow_book(book_id, member_id, due_date)
            QMessageBox.information(self, 'Borrow Book', response)
            self.loadBooks()
        else:
            QMessageBox.information(self, 'Error', 'Please select a book to borrow')


    def openAddBookDialog(self):
        dialog = AddBookDialog(self)
        if dialog.exec_():
            title, author, isbn, quantity = dialog.getBookDetails()
            add_book_to_db(title, author, isbn, quantity)  # Pass all details to the function
            self.loadBooks()

    def openBorrowBookDialog(self):
        selected_row = self.booksTable.currentRow()
        if selected_row != -1:
            selected_book_title = self.booksTable.item(selected_row, 0).text()
            dialog = BorrowBookDialog(selected_book_title, self.book_ids, self)

            if dialog.exec_():
                book_id, member_id, due_date = dialog.getBorrowDetails()
                book_id = int(book_id)
                response = borrow_book(book_id, member_id, due_date)
                QMessageBox.information(self, 'Borrow Book', response)
                self.loadBooks()
            else:
                QMessageBox.information(self, 'Error', 'Please select a book to borrow')

def main():
    app = QApplication(sys.argv)
    ex = LibrarySystem()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
