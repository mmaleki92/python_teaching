from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMainWindow



class LibWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.title_edit = QLineEdit(parent=self)

        self.author_edit = QLineEdit(parent=self)
        self.author_edit.move(0, 50)

        self.publisher_edit = QLineEdit(parent=self)
        self.publisher_edit.move(0, 100)


        self.add_book_btn = QPushButton("افزودن", parent=self)
        self.add_book_btn.move(200, 100)



