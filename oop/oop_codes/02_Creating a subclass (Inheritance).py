class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

dog = Dog("Charlie")
print(dog.speak())