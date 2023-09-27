class MyClass:
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value += value

class MyApp:
    def __init__(self):
        self.is_logged_in = False

    def login(self, username, password):
        if username == 'username' and password == 'password':
            self.is_logged_in = True
        else:
            raise Exception('Invalid username or password')

    def is_logged_in(self):
        return self.is_logged_in

my_class = MyClass()
my_class.add(1)
my_class.add(2)

print(my_class.value)
my_app = MyApp()

if my_app.login('username', 'password'):
    print('Login successful!')
else:
    print('Login failed!')
