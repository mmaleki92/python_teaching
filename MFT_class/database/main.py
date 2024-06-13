import models
from datetime import datetime

def user_register(user):

    user.create_date = str(datetime.now())
    models.create_user(user)

def driver_register():
    pass