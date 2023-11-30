import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Obstacle classes
class Rock:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.speed = 5

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 50, 50))

class Bird:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.speed = 7

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.ellipse(screen, BLACK, (self.x, self.y, 50, 30))

# Game loop
running = True
obstacles = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Creating obstacles
    if random.randint(1, 20) == 1:
        if random.choice([True, False]):
            obstacles.append(Rock())
        else:
            obstacles.append(Bird())

    # Update the screen
    screen.fill(WHITE)
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
