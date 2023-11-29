from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!"

# You can't instantiate an AbstractAnimal
# animal = AbstractAnimal()  # This will raise a TypeError

dog = Dog()
print(dog.speak())