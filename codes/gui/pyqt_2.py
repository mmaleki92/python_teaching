import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()

label = QLabel("Enter your name:")
name_input = QLineEdit()
button = QPushButton("Submit")

hbox = QHBoxLayout()
hbox.addWidget(label)
hbox.addWidget(name_input)

vbox = QVBoxLayout()
vbox.addLayout(hbox)
vbox.addWidget(button)

window.setLayout(vbox)
window.setWindowTitle("PyQt5 Example")
window.show()

sys.exit(app.exec_())
