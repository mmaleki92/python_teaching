import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Single Main Window Design')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.label = QLabel('Welcome to Single Main Window Design', self.central_widget)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = QPushButton('Click Me', self.central_widget)
        self.button.clicked.connect(self.on_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.central_widget.setLayout(layout)

    def on_button_clicked(self):
        self.label.setText('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
