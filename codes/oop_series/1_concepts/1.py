
# Classes

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation


# Objects

person1 = Person("John", 30, "Male", "Engineer")
person2 = Person("Jane", 25, "Female", "Doctor")

# Attributes

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
person1.name = "Johnny"

# Methods

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
    def introduce(self):
        print("Hi, my name is " + self.name + " and I am a " + self.occupation)
        
person1 = Person("John", 30, "Male", "Engineer")
person1.introduce()

# Encapsulation:

class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self._age = age # underscore denotes protected attribute
        self.__gender = gender # double underscore denotes private attribute
        self.occupation = occupation
        
person1 = Person("John", 30, "Male", "Engineer")
print(person1.name)
print(person1._age)
print(person1.__gender) # this line will produce an error

# Inheritance:

class Student(Person):
    def __init__(self, name, age, gender, occupation, school):
        super().__init__(name, age, gender, occupation)
        self.school = school
        
student1 = Student("John", 20, "Male", "Student", "University of ABC")
print(student1.name)
print(student1.school)