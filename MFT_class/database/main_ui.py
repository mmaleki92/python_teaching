from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from dataclasses import dataclass
import main

app = QApplication([])

window = QWidget()

@dataclass
class User:
    username: str = None 
    email: str = None 
    phone_number: str = None 
    create_date: str = None

def get_form():
    user = User()
    user.email = email_ledit.text()
    user.username = username_ledit.text()
    user.phone_number = phonenumber_ledit.text()
    main.user_register(user)


register_btn = QPushButton("ثبت نام", parent=window)
register_btn.clicked.connect(get_form)

email_ledit = QLineEdit(parent=window)
email_ledit.move(100, 100)
username_ledit = QLineEdit(parent=window)
username_ledit.move(100, 200)
phonenumber_ledit = QLineEdit(parent=window)
phonenumber_ledit.move(100, 300)


window.show()

app.exec()