import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Variable to keep track of the connection state
        self.connected = False

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Disconnecting Signals')

        self.button = QPushButton('Connect/Disconnect', self)
        self.button.setGeometry(100, 100, 150, 30)

        # Connect the button's clicked signal to the custom slot
        self.button.clicked.connect(self.toggle_connection)

    def toggle_connection(self):
        if self.connected:
            # Disconnect the signal from the slot
            self.button.clicked.disconnect(self.on_button_click)
            print('Signal disconnected')
        else:
            # Connect the signal to the slot
            self.button.clicked.connect(self.on_button_click)
            print('Signal connected')

        # Toggle the connection state
        self.connected = not self.connected

    def on_button_click(self):
        print('Button clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
