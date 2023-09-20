class Shape:
    def __init__(self, color):
        self.color = color
        
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

my_rectangle = Rectangle(5, 10, "blue")
print(f"Area of rectangle: {my_rectangle.area()}")
print(f"Perimeter of rectangle: {my_rectangle.perimeter()}")

my_circle = Circle(7, "red")
print(f"Area of circle: {my_circle.area()}")
print(f"Circumference of circle: {my_circle.perimeter():.2f}")