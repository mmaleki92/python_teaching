import sys
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyEmitter(QObject):
    my_signal = pyqtSignal(str)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Custom Signals and Slots')

        button = QPushButton('Emit Custom Signal', self)
        button.setGeometry(100, 100, 150, 30)

        self.emitter = MyEmitter()

        # Connect the custom signal to a custom slot
        self.emitter.my_signal.connect(self.on_custom_signal)

        button.clicked.connect(self.emit_custom_signal)

    def emit_custom_signal(self):
        self.emitter.my_signal.emit("Hello from custom signal!")

    def on_custom_signal(self, message):
        print(f'Custom Signal Received: {message}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
