from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMainWindow, QFormLayout



class LibWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('سامانه')

    
        layout = QFormLayout()
        self.setLayout(layout)

        self.title_edit = QLineEdit()
        layout.addRow('Title:', self.title_edit)

        self.author_edit = QLineEdit()
        layout.addRow('Author:', self.author_edit)

        self.publisher_edit = QLineEdit()

        layout.addRow('Publisher:', self.publisher_edit)

        self.add_book_btn = QPushButton("افزودن")

        layout.addRow('', self.add_book_btn)

        self.show()

