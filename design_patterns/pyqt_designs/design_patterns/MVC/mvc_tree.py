import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTreeWidget, QTreeWidgetItem, QLineEdit

class Model:
    def __init__(self):
        self.root = QTreeWidgetItem(["Root"])

    def add_item(self, parent, item):
        parent.addChild(item)

    def update_item(self, item, text):
        item.setText(0, text)

    def remove_item(self, item):
        parent = item.parent()
        if parent is not None:
            parent.removeChild(item)

class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.setWindowTitle('MVC Example with QTreeWidget')
        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Item"])

        self.lineEdit = QLineEdit(self)
        self.pushButton_add = QPushButton('Add', self)
        self.pushButton_update = QPushButton('Update', self)
        self.pushButton_remove = QPushButton('Remove', self)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton_add)
        layout.addWidget(self.pushButton_update)
        layout.addWidget(self.pushButton_remove)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.tree_widget.addTopLevelItem(self.model.root)

        self.view.pushButton_add.clicked.connect(self.add_item)
        self.view.pushButton_update.clicked.connect(self.update_item)
        self.view.pushButton_remove.clicked.connect(self.remove_item)

    def add_item(self):
        text = self.view.lineEdit.text()
        if text:
            item = QTreeWidgetItem([text])
            self.model.add_item(self.view.tree_widget.currentItem(), item)
            self.view.lineEdit.clear()

    def update_item(self):
        item = self.view.tree_widget.currentItem()
        text = self.view.lineEdit.text()
        if item and text:
            self.model.update_item(item, text)
            self.view.lineEdit.clear()

    def remove_item(self):
        item = self.view.tree_widget.currentItem()
        if item:
            self.model.remove_item(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
