import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class StudentMarksForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Marks Form")
        self.setGeometry(100, 100, 400, 200)

        self.name_label = QLabel("Student Name:")
        self.name_edit = QLineEdit()

        self.marks_label = QLabel("Marks:")
        self.marks_edit = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_form)
        menu = QMenu()
        menu.setFont(QFont("Times", 14,
        QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:green')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.marks_label)
        layout.addWidget(self.marks_edit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_form(self):
        student_name = self.name_edit.text()
        marks = self.marks_edit.text()

        if student_name and marks:
            print(f"Submitted: Student Name: {student_name}, Marks: {marks}")
            self.clear_form()
        else:
            print("Please fill in all fields.")

    def clear_form(self):
        self.name_edit.clear()
        self.marks_edit.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = StudentMarksForm()
    form.show()
    sys.exit(app.exec())
