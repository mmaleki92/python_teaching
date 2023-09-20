import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Polymorphism Example")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define Shape base class
class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pass

# Define Rectangle subclass
class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

# Define Circle subclass
class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Create instances of Shape subclasses
rectangle = Rectangle(100, 100, 200, 100, RED)
circle = Circle(400, 300, 50, GREEN)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill(BLACK)

    # Draw shapes
    rectangle.draw()
    circle.draw()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
