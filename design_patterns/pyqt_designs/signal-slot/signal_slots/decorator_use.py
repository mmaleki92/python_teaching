import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Decorator Syntax for Slots')

        button = QPushButton('Click me', self)
        button.setGeometry(100, 100, 100, 30)

        button.clicked.connect(self.on_button_click)

    @pyqtSlot()
    def on_button_click(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())