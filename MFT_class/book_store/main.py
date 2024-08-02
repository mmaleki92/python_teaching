from models import LibraryCatalog
from lib_gui import LibWindow
from PyQt6.QtWidgets import QApplication

def fun():
    library.add_book(window.title_edit.text(), window.author_edit.text(), window.publisher_edit.text())

library = LibraryCatalog()

app = QApplication([])
window = LibWindow()


window.add_book_btn.clicked.connect(fun)


window.show()
app.exec()

