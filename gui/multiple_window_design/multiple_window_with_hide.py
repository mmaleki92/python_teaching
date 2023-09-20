import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window 1')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.button = QPushButton('Open Window 2', self.central_widget)
        self.button.clicked.connect(self.open_window2)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.central_widget.setLayout(layout)

    def open_window2(self):
        if hasattr(self, 'window2'):
            self.window2.show()
        else:
            self.window2 = Window2()
            self.window2.show()

        self.hide()

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window 2')
        self.setGeometry(200, 200, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.button = QPushButton('Open Window 1', self.central_widget)
        self.button.clicked.connect(self.open_window1)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.central_widget.setLayout(layout)

    def open_window1(self):
        if hasattr(self, 'window1'):
            self.window1.show()
        else:
            self.window1 = Window1()
            self.window1.show()

        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = Window1()
    window1.show()
    sys.exit(app.exec_())
