import models
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    username: str = None 
    email: str = None 
    phone_number: str = None 
    create_date: str = None

def register():
    user = User()
    user.username = input("username: ")
    user.phone_number = input("phone number: ")
    user.email = input("email: ")
    user.create_date = str(datetime.now())
    models.create_user(user)

register()