import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        self.label = QLabel(text)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        widget1 = MyWidget("Hello")
        widget2 = MyWidget("PyQt6")

        layout = QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
