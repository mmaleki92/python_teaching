# Text-Based Adventure Game

```python
class Room:
    def __init__(self, description):
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Example Usage
room = Room("You are in a dark room.")
torch = Item("Torch", "A small wooden torch.")
room.add_item(torch)

print(room.description)
for item in room.items:
    print(f"Item: {item.name}, Description: {item.description}")

```

# Simple Web Framework
```python
class WebFramework:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(func):
            self.routes[path] = func
            return func
        return wrapper

    def serve(self, path):
        if path in self.routes:
            return self.routes[path]()
        else:
            return '404 Not Found'

app = WebFramework()

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/about')
def about():
    return 'This is the About Page'

# Simulate a server request
print(app.serve('/'))  # Welcome to the Home Page
print(app.serve('/about'))  # This is the About Page

```

# Real-World System (e.g., Bank System)

```python

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance -= amount
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, initial_deposit):
        self.accounts[owner] = Account(owner, initial_deposit)

    def get_account_balance(self, owner):
        return self.accounts[owner].balance

# Example Usage
bank = Bank()
bank.create_account('Alice', 1000)
print(bank.get_account_balance('Alice'))  # 1000

```

# Design Pattern (e.g., Singleton Pattern)

```python

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Database Connection"

# Example Usage
db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

# Multi-threading/Multi-processing Application

```python

from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print(f"{self.name} running: {i}")

thread1 = MyThread("Thread1")
thread2 = MyThread("Thread2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

```

#  Custom Decorator Class

```python

class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function '{self.func.__name__}' with arguments {args} and {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"'{self.func.__name__}' returned {result}")
        return result

@LogDecorator
def add(a, b):
    return a + b

# Example Usage
add(5, 3)

```

# mltithreading music player

```python
import threading
import time

def play_music():
    for _ in range(10):  # Simulate playing music for 10 iterations
        print("Playing music...")
        time.sleep(1)  # Simulate the time delay of playing music

def perform_other_task():
    for _ in range(5):  # Simulate another task for 5 iterations
        print("Performing another task...")
        time.sleep(2)  # Simulate the time delay of another task

# Creating threads
music_thread = threading.Thread(target=play_music)
task_thread = threading.Thread(target=perform_other_task)

# Starting threads
music_thread.start()
task_thread.start()

# Joining threads to ensure each finishes before the script ends
music_thread.join()
task_thread.join()

print("All tasks completed.")
```

# Complex Tasks
```python
import threading
import time

def compute_heavy_task():
    # Simulate a CPU-bound task
    result = 0
    for i in range(1, 10000000):
        result += i
    print("Computation completed. Result:", result)

def io_bound_task():
    # Simulate an I/O-bound task
    for _ in range(3):
        time.sleep(2)
        print("I/O task waiting for external event...")

# Creating threads
thread1 = threading.Thread(target=compute_heavy_task)
thread2 = threading.Thread(target=io_bound_task)

# Starting threads
thread1.start()
thread2.start()

# Joining threads
thread1.join()
thread2.join()

print("All tasks completed.")

```

# Internet download manager

```python
import threading
import requests

def download_segment(url, start, end, filename):
    headers = {'Range': f'bytes={start}-{end}'}
    response = requests.get(url, headers=headers, stream=True)
    
    with open(filename, "r+b") as f:
        f.seek(start)
        f.write(response.content)

def download_file(url, num_segments):
    response = requests.head(url)
    file_size = int(response.headers.get('content-length', 0))
    segment_size = file_size // num_segments

    filename = url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(b'\0' * file_size)

    threads = []
    for segment in range(num_segments):
        start = segment * segment_size
        # Ensure the last segment goes to the end of the file
        end = start + segment_size - 1 if segment < num_segments - 1 else file_size
        thread = threading.Thread(target=download_segment, args=(url, start, end, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

download_file("http://example.com/largefile.zip", 4)

```

# Iterator class implementation

```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a

# Example Usage
fib_iter = FibonacciIterator(10)
for num in fib_iter:
    print(num)

```
# Simple Dependency Injection Container

```python
class Container:
    def __init__(self):
        self.component_registry = {}

    def register(self, name, constructor):
        self.component_registry[name] = constructor

    def resolve(self, name):
        constructor = self.component_registry.get(name)
        if not constructor:
            raise ValueError(f"No component registered under '{name}'")
        return constructor(self)

# Example Usage
class Database:
    def __init__(self, container):
        pass  # Database initialization logic

container = Container()
container.register("database", Database)
db = container.resolve("database")

```