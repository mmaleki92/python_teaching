class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

my_rectangle = Rectangle(5, 10)
my_circle = Circle(7)

print_area(my_rectangle)
print_area(my_circle)
