from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QGridLayout


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.mohasebat = []
        self.layout = QGridLayout()
        self.num_1 = QPushButton("1")
        self.num_2 = QPushButton("2")
        self.num_1.setObjectName("1")
        self.num_2.setObjectName("2")
        self.plus = QPushButton("+")
        self.plus.setObjectName("+")
        self.lbl = QLabel("lskahfdykjsad")
        self.layout.addWidget(self.num_1, 1, 1)
        self.layout.addWidget(self.num_2, 2, 1)
        self.layout.addWidget(self.plus, 2, 2)
        self.layout.addWidget(self.lbl, 3, 3)

        self.layout.setColumnStretch(1, 60)
        self.layout.setRowStretch(1, 1)

        self.setLayout(self.layout)
        self.num_1.clicked.connect(self.fun)
        self.num_2.clicked.connect(self.fun)
        self.mosavi = QPushButton("=")
        self.mosavi.setObjectName("=")
        self.layout.addWidget(self.mosavi, 3, 4)
        self.mosavi.clicked.connect(self.calc)

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        print(a0)
        return super().keyPressEvent(a0)
    def calc(self):
        n = "".join(self.mohasebat)

        m = eval(n)
        self.lbl.setText(str(n) + " = " + str(m))

    def fun(self):
        key = self.sender()
        self.mohasebat.append(key.objectName())

app = QApplication([])
window = Calculator()
window.show()
app.exec()
