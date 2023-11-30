import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Obstacle classes (same as before)
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

# Factory Method Pattern
class ObstacleFactory:
    @staticmethod
    def create_obstacle(type):
        if type == "rock":
            return Rock()
        elif type == "bird":
            return Bird()

# Game loop (same as before but with Factory Method)
running = True
obstacles = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    # Creating obstacles using Factory Method
    if random.randint(1, 20) == 1:
        obstacle_type = "rock" if random.choice([True, False]) else "bird"
        obstacles.append(ObstacleFactory.create_obstacle(obstacle_type))
    # Update the screen
    screen.fill(WHITE)
    for obstacle in obstacles:
        obstacle.move()
        obstacle.draw()
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
