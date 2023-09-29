import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.current_version = "1.0.0"

    def init_ui(self):
        layout = QVBoxLayout()

        self.updateButton = QPushButton('Check for Updates', self)
        self.updateButton.clicked.connect(self.check_update)
        layout.addWidget(self.updateButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Update Checker with FastAPI and PyQt5')
        self.show()

    def check_update(self):
        response = requests.get("http://127.0.0.1:8000/version/")
        if response.status_code == 200:
            latest_version = response.json()['version']
            if self.current_version != latest_version:
                QMessageBox.information(self, 'Update Available', f'A new version {latest_version} is available!')
            else:
                QMessageBox.information(self, 'No Updates', 'You are on the latest version!')
        else:
            QMessageBox.warning(self, 'Error', 'Failed to check for updates.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
