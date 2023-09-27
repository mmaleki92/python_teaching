from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QLineEdit, QVBoxLayout)

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()

btn = QPushButton("click!")
lbl = QLabel("Hello")
begir = QLineEdit()
layout.addWidget(btn)
layout.addWidget(lbl)
layout.addWidget(begir)

window.setLayout(layout)
window.show()

def fun():
    t = begir.text()
    lbl.setText(t)

btn.clicked.connect(fun)

app.exec()
