import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListView, QLineEdit

from PyQt5.QtCore import Qt, QStringListModel

class Model:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.setWindowTitle('MVC Example with QListView')
        self.list_view = QListView(self)
        self.list_model = QStringListModel()
        self.list_view.setModel(self.list_model)

        self.lineEdit = QLineEdit(self)
        self.pushButton_add = QPushButton('Add', self)
        self.pushButton_remove = QPushButton('Remove', self)

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton_add)
        layout.addWidget(self.pushButton_remove)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.list_model.setStringList(self.model.data)

        self.view.pushButton_add.clicked.connect(self.add_item)
        self.view.pushButton_remove.clicked.connect(self.remove_item)

    def add_item(self):
        item = self.view.lineEdit.text()
        if item:
            self.model.add_item(item)
            self.view.list_model.setStringList(self.model.data)
            self.view.lineEdit.clear()

    def remove_item(self):
        indexes = self.view.list_view.selectedIndexes()
        if indexes:
            index = indexes[0].row()
            self.model.remove_item(index)
            self.view.list_model.setStringList(self.model.data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
