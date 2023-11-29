import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button that will trigger the menu
        self.button = QPushButton("Show Menu")
        self.button.clicked.connect(self.show_menu)

        # Set up the main layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # Create the main widget to set the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)
        self.setWindowTitle("QMenu Example")

    def show_menu(self):
        # Create a QMenu instance
        menu = QMenu(self)

        # Add actions to the menu
        action1 = menu.addAction("Action 1")
        action2 = menu.addAction("Action 2")
        action3 = menu.addAction("Action 3")

        # Connect actions to functions
        action1.triggered.connect(self.action1_triggered)
        action2.triggered.connect(self.action2_triggered)
        action3.triggered.connect(self.action3_triggered)

        # Show the context menu at the current cursor position
        menu.exec(self.mapToGlobal(self.button.pos()))

    def action1_triggered(self):
        print("Action 1 triggered!")

    def action2_triggered(self):
        print("Action 2 triggered!")

    def action3_triggered(self):
        print("Action 3 triggered!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())