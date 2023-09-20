import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

def on_button_click():
    label.setText("Hello, World!")

app = QApplication(sys.argv)
window = QMainWindow()

label = QLabel(window)
label.setText("Welcome to my PyQt5 GUI!")
label.setGeometry(100, 50, 200, 50)

button = QPushButton(window)
button.setText("Click me")
button.setGeometry(100, 120, 100, 50)
button.clicked.connect(on_button_click)

window.setGeometry(200, 200, 400, 300)
window.setWindowTitle("PyQt5 Example")
window.show()

sys.exit(app.exec_())
