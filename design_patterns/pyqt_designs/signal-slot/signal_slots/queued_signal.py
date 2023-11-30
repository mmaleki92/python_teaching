import sys
import time
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Worker(QObject):
    finished = pyqtSignal()

    def do_work(self):
        # Simulate time-consuming work
        time.sleep(2)
        self.finished.emit()

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Queued Connections')

        self.button = QPushButton('Start Work', self)
        self.button.setGeometry(100, 100, 150, 30)

        self.worker = Worker()

        # Connect the button's clicked signal to the worker's slot
        self.button.clicked.connect(self.worker.do_work)

        # Connect the worker's finished signal to a slot in the main thread
        self.worker.finished.connect(self.on_work_finished)

    def on_work_finished(self):
        print('Work finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
