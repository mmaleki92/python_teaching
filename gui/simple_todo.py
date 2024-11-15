import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow, QMessageBox
)

class TaskItemWidget(QWidget):
    def __init__(self, task_name, delete_callback):
        super().__init__()
        
        # Create the main layout for the task item
        layout = QHBoxLayout()
        
        # Task name label
        self.label = QLabel(task_name)
        layout.addWidget(self.label)
        
        # "Done" checkbox
        self.checkbox = QCheckBox("Done")
        layout.addWidget(self.checkbox)
        
        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(delete_callback)  # Connect to the delete function
        layout.addWidget(self.delete_button)
        
        # Set layout for the custom widget
        self.setLayout(layout)
    
    def mark_done(self):
        """Marks the task as done by checking the checkbox and graying out the label."""
        self.checkbox.setChecked(True)
        self.label.setStyleSheet("color: gray; text-decoration: line-through;")

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)
        
        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        
        # Input field for adding new tasks
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        main_layout.addWidget(self.task_input)
        
        # Add Task button
        add_task_button = QPushButton("Add Task")
        add_task_button.clicked.connect(self.add_task)
        main_layout.addWidget(add_task_button)
        
        # List widget to hold all task items
        self.task_list_widget = QListWidget()
        main_layout.addWidget(self.task_list_widget)
        
        # Set the main widget and layout
        self.setCentralWidget(main_widget)
        
    def add_task(self):
        """Adds a new task to the list."""
        task_name = self.task_input.text().strip()
        if not task_name:
            QMessageBox.warning(self, "Warning", "Please enter a task.")
            return
        
        # Create a QListWidgetItem
        list_item = QListWidgetItem()
        
        # Define delete callback function for this item
        def delete_task():
            self.task_list_widget.takeItem(self.task_list_widget.row(list_item))
        
        # Create a TaskItemWidget with task name and delete callback
        task_widget = TaskItemWidget(task_name, delete_task)
        
        # Add the custom widget to the QListWidget
        self.task_list_widget.addItem(list_item)
        self.task_list_widget.setItemWidget(list_item, task_widget)
        
        # Clear the input field after adding the task
        self.task_input.clear()

# Run the application
app = QApplication(sys.argv)
window = ToDoListApp()
window.show()
sys.exit(app.exec_())
