## QtWidgets
- QApplication
- QMainWindow
- QVBoxLayout
- QWidget
- QListView
- QPushButton
- QLineEdit
- QLabel
- QHBoxLayout
- QFormLayout
- QAbstractItemView
- QSizePolicy
- QGroupBox
## Qt

- QStandardItemModel
- QStandardItem

---

```python
class Model:
    def __init__(self):
        self.data = [0, 1, 2, 3, 4]

    def increment(self, index):
        self.data[index] += 1

    def decrement(self, index):
        self.data[index] -= 1
```
```python
class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.setWindowTitle('MVC Example with QListView')
        self.listView = QListView(self)
        self.listView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.pushButton_increment = QPushButton('Increment', self)
        self.pushButton_decrement = QPushButton('Decrement', self)

        self.label_selected_value = QLabel('Selected Value:', self)
        self.lineEdit_selected_value = QLineEdit(self)
        self.lineEdit_selected_value.setReadOnly(True)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.pushButton_increment)
        layout_buttons.addWidget(self.pushButton_decrement)

        layout_selection_info = QFormLayout()
        layout_selection_info.addRow(self.label_selected_value, self.lineEdit_selected_value)

        group_box_buttons = QGroupBox('Actions')
        group_box_buttons.setLayout(layout_buttons)

        group_box_selection_info = QGroupBox('Selected Item')
        group_box_selection_info.setLayout(layout_selection_info)

        layout = QVBoxLayout()
        layout.addWidget(self.listView)
        layout.addWidget(group_box_buttons)
        layout.addWidget(group_box_selection_info)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
```

```python
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.list_model = QStandardItemModel(self.view)
        self.view.listView.setModel(self.list_model)

        for item in self.model.data:
            self.list_model.appendRow(QStandardItem(str(item)))

        self.view.listView.clicked.connect(self.update_selection_info)
        self.view.pushButton_increment.clicked.connect(self.increment)
        self.view.pushButton_decrement.clicked.connect(self.decrement)

    def update_selection_info(self, index):
        if index.isValid():
            selected_value = self.model.data[index.row()]
            self.view.lineEdit_selected_value.setText(str(selected_value))

    def increment(self):
        selected_index = self.view.listView.currentIndex()
        if selected_index.isValid():
            index = selected_index.row()
            self.model.increment(index)
            item = QStandardItem(str(self.model.data[index]))
            self.list_model.setItem(index, item)
            self.view.lineEdit_selected_value.setText(str(self.model.data[index]))

    def decrement(self):
        selected_index = self.view.listView.currentIndex()
        if selected_index.isValid():
            index = selected_index.row()
            self.model.decrement(index)
            item = QStandardItem(str(self.model.data[index]))
            self.list_model.setItem(index, item)
            self.view.lineEdit_selected_value.setText(str(self.model.data[index]))
```
```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
```