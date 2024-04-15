from functools import partial
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, 
                             QTextEdit, QPushButton, QHBoxLayout,
                             QVBoxLayout, QGridLayout)
import os

app = QApplication([])
window = QWidget()

editor = QTextEdit(parent=window)

run_btn = QPushButton("Run", parent=window)
run_btn.move(500, 200)

def runner():
    code = editor.toPlainText()
    # m = eval(code)

    f = open("code.py", "w")
    f.write(code)
    f.close()

    os.system("python code.py")


run_btn.clicked.connect(runner)

window.show()
app.exec()
