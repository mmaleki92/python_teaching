import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant

class Model:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def update_item(self, index, item):
        if 0 <= index < len(self.data):
            self.data[index] = item

    def remove_item(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

class TableViewTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self.data = data
        self.headers = headers

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()
            item = self.data[row]
            return QVariant(item[self.headers[col]])
        return QVariant()

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return QVariant(self.headers[section])
        return QVariant()

class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.setWindowTitle('MVC Example with QTableView')
        self.table_view = QTableView(self)
        self.table_model = TableViewTableModel(self.model.data, headers=["Name", "Age"])
        self.table_view.setModel(self.table_model)

        self.lineEdit_name = QLineEdit(self)
        self.lineEdit_age = QLineEdit(self)
        self.pushButton_add = QPushButton('Add', self)
        self.pushButton_update = QPushButton('Update', self)
        self.pushButton_remove = QPushButton('Remove', self)

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.lineEdit_name)
        layout.addWidget(self.lineEdit_age)
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

        self.view.pushButton_add.clicked.connect(self.add_item)
        self.view.pushButton_update.clicked.connect(self.update_item)
        self.view.pushButton_remove.clicked.connect(self.remove_item)

    def add_item(self):
        name = self.view.lineEdit_name.text()
        age = self.view.lineEdit_age.text()
        if name and age:
            item = {"Name": name, "Age": age}
            self.model.add_item(item)
            self.view.table_model.layoutChanged.emit()

    def update_item(self):
        indexes = self.view.table_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            name = self.view.lineEdit_name.text()
            age = self.view.lineEdit_age.text()
            if name and age:
                item = {"Name": name, "Age": age}
                self.model.update_item(row, item)
                self.view.table_model.layoutChanged.emit()

    def remove_item(self):
        indexes = self.view.table_view.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            self.model.remove_item(row)
            self.view.table_model.layoutChanged.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
