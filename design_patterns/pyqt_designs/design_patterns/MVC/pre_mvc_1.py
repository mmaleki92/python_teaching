import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class CounterApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the counter value
        self.counter = 0

        # Create the GUI components
        self.label = QLabel(str(self.counter))
        self.increment_button = QPushButton("Increment")
        self.decrement_button = QPushButton("Decrement")

        # Connect button signals to corresponding functions
        self.increment_button.clicked.connect(self.increment_counter)
        self.decrement_button.clicked.connect(self.decrement_counter)

        # Create the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.decrement_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def increment_counter(self):
        self.counter += 1
        self.label.setText(str(self.counter))

    def decrement_counter(self):
        self.counter -= 1
        self.label.setText(str(self.counter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CounterApp()
    window.setWindowTitle("Counter App")
    window.show()
    sys.exit(app.exec_())
