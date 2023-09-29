import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Press the button to get message", self)
        layout.addWidget(self.label)

        btn = QPushButton('Get Message', self)
        btn.clicked.connect(self.on_click)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setWindowTitle('FastAPI with PyQt5')
        self.show()

    def on_click(self):
        response = requests.get("http://127.0.0.1:8000/")
        if response.status_code == 200:
            self.label.setText(response.json()['message'])
        else:
            self.label.setText("Failed to fetch message")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
