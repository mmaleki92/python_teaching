import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()

label = QLabel("Select your favorite color:")
color_combo = QComboBox()
color_combo.addItem("Red")
color_combo.addItem("Green")
color_combo.addItem("Blue")

vbox = QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(color_combo)

window.setLayout(vbox)
window.setWindowTitle("PyQt5 Example")
window.show()

sys.exit(app.exec_())
