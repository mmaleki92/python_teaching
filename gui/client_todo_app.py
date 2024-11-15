import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QLineEdit, QMainWindow, QMessageBox
)

# Server URL
SERVER_URL = "http://127.0.0.1:5000"

class TaskItemWidget(QWidget):
    def __init__(self, task, delete_callback, update_callback):
        super().__init__()
        self.task = task
        layout = QHBoxLayout()
        
        # Task name label
        self.label = QLabel(task["task_name"])
        layout.addWidget(self.label)
        
        # "Done" checkbox
        self.checkbox = QCheckBox("Done")
        self.checkbox.setChecked(task["completed"])
        self.checkbox.stateChanged.connect(lambda: update_callback(self.task["id"], self.checkbox.isChecked()))
        layout.addWidget(self.checkbox)
        
        # Delete button
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(lambda: delete_callback(self.task["id"]))
        layout.addWidget(self.delete_button)
        
        self.setLayout(layout)
    
class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 400, 300)
        
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        main_layout.addWidget(self.task_input)
        
        add_task_button = QPushButton("Add Task")
        add_task_button.clicked.connect(self.add_task)
        main_layout.addWidget(add_task_button)
        
        self.task_list_widget = QListWidget()
        main_layout.addWidget(self.task_list_widget)
        
        self.setCentralWidget(main_widget)
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the server and display them in the list widget."""
        response = requests.get(f"{SERVER_URL}/tasks")
        if response.status_code == 200:
            tasks = response.json()
            self.task_list_widget.clear()
            for task in tasks:
                self.add_task_to_list_widget(task)
        else:
            QMessageBox.warning(self, "Error", "Failed to load tasks.")

    def add_task_to_list_widget(self, task):
        """Add a task to the QListWidget."""
        list_item = QListWidgetItem()
        task_widget = TaskItemWidget(
            task,
            delete_callback=self.delete_task,
            update_callback=self.update_task
        )
        self.task_list_widget.addItem(list_item)
        self.task_list_widget.setItemWidget(list_item, task_widget)

    def add_task(self):
        """Send a new task to the server and update the list widget."""
        task_name = self.task_input.text().strip()
        if not task_name:
            QMessageBox.warning(self, "Warning", "Please enter a task.")
            return
        
        response = requests.post(f"{SERVER_URL}/tasks", json={"task_name": task_name})
        if response.status_code == 201:
            task = response.json()
            self.add_task_to_list_widget(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Failed to add task.")

    def update_task(self, task_id, completed):
        """Update a task's completion status on the server."""
        response = requests.put(f"{SERVER_URL}/tasks/{task_id}", json={"completed": completed})
        if response.status_code != 200:
            QMessageBox.warning(self, "Error", "Failed to update task.")

    def delete_task(self, task_id):
        """Delete a task from the server and update the list widget."""
        response = requests.delete(f"{SERVER_URL}/tasks/{task_id}")
        if response.status_code == 200:
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Failed to delete task.")

# Run the PyQt5 application
app = QApplication(sys.argv)
window = ToDoListApp()
window.show()
sys.exit(app.exec_())
