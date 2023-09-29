import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.studentList = QListWidget(self)
        layout.addWidget(self.studentList)
        
        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText('Enter Student Name')
        layout.addWidget(self.nameInput)
        
        self.ageInput = QLineEdit(self)
        self.ageInput.setPlaceholderText('Enter Student Age')
        layout.addWidget(self.ageInput)
        
        self.addButton = QPushButton('Add Student', self)
        self.addButton.clicked.connect(self.add_student)
        layout.addWidget(self.addButton)
        
        self.deleteButton = QPushButton('Delete Selected Student', self)
        self.deleteButton.clicked.connect(self.delete_student)
        layout.addWidget(self.deleteButton)
        
        self.refreshButton = QPushButton('Refresh List', self)
        self.refreshButton.clicked.connect(self.load_students)
        layout.addWidget(self.refreshButton)
        
        self.setLayout(layout)
        self.setWindowTitle('Student Management with FastAPI and PyQt5')
        self.show()

    def load_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            self.studentList.clear()
            for student in response.json():
                self.studentList.addItem(f"{student['name']} (Age: {student['age']})")

    def add_student(self):
        student = {"name": self.nameInput.text(), "age": int(self.ageInput.text())}
        response = requests.post("http://127.0.0.1:8000/students/", json=student)
        if response.status_code == 200:
            self.load_students()

    def delete_student(self):
        student_id = self.studentList.currentRow()
        response = requests.delete(f"http://127.0.0.1:8000/students/{student_id}")
        if response.status_code == 200:
            self.load_students()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
