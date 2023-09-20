class PrintableMixin:
    def __str__(self):
        return f"{type(self).__name__} ({self.__dict__})"

class Shape:
    pass

class Rectangle(Shape, PrintableMixin):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape, PrintableMixin):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

my_rectangle = Rectangle(5, 10)
print(my_rectangle)

my_circle = Circle(7)
print(my_circle)
