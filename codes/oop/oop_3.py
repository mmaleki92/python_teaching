class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog("Max")
cat = Cat("Fluffy")

make_animal_sound(dog) # Output: Woof!
make_animal_sound(cat) # Output: Meow!