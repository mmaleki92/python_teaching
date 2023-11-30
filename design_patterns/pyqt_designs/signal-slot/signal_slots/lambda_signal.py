import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Lambda Functions as Slots')

        button = QPushButton('Click me', self)
        button.setGeometry(100, 100, 100, 30)

        # Connect a lambda function as a slot
        button.clicked.connect(lambda: print('Button clicked with lambda'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
