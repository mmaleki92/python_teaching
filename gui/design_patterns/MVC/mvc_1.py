import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt

class Model:
    def __init__(self):
        self.data = 0

    def increment(self):
        self.data += 1

    def decrement(self):
        self.data -= 1

class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        self.setWindowTitle('MVC Example')
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.pushButton_increment = QPushButton('Increment', self)
        self.pushButton_decrement = QPushButton('Decrement', self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton_increment)
        layout.addWidget(self.pushButton_decrement)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.label.setText(str(self.model.data))

        self.view.pushButton_increment.clicked.connect(self.increment)
        self.view.pushButton_decrement.clicked.connect(self.decrement)

    def increment(self):
        self.model.increment()
        self.view.label.setText(str(self.model.data))

    def decrement(self):
        self.model.decrement()
        self.view.label.setText(str(self.model.data))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
