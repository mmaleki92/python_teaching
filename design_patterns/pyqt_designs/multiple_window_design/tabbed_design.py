import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QTabWidget

class TabbedInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tabbed Interface Design')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.addTab(self.create_tab('Tab 1'), 'Tab 1')
        self.tab_widget.addTab(self.create_tab('Tab 2'), 'Tab 2')
        self.tab_widget.addTab(self.create_tab('Tab 3'), 'Tab 3')

        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)

        self.central_widget.setLayout(layout)

    def create_tab(self, text):
        tab = QWidget()
        button = QPushButton(f'Button in {text}', tab)
        layout = QVBoxLayout(tab)
        layout.addWidget(button)
        return tab

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TabbedInterface()
    window.show()
    sys.exit(app.exec_())
