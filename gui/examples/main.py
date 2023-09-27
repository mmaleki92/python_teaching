from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

Form, Window = uic.loadUiType("user.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

def fun():
    t = form.user_lineEdit.text()
    if t == "mammad":
        p = form.pass_lineEdit.text()
        if p == "1234":
            print("Horraaa!")
form.btn.clicked.connect(fun)
window.show()
app.exec()

