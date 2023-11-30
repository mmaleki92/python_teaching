import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 50, 50)

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Item class
class Item:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(100, 700), random.randint(100, 500), 30, 30)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Observer Pattern Implementation
class Observer:
    def update(self, subject):
        pass

class ScoreBoard(Observer):
    def __init__(self):
        self.score = 0

    def update(self, subject):
        self.score += 10  # Update score
        print(f"Score: {self.score}")  # For demonstration, print score

class GameEnvironment(Observer):
    def update(self, subject):
        # Change the game environment in response to item collection
        pass

# Subject
class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

# Player as a Subject
class PlayerSubject(Player, Subject):
    def __init__(self):
        Player.__init__(self)
        Subject.__init__(self)

    def collect_item(self, item):
        self.notify_observers()  # Notify all observers

# Game loop
running = True
player = PlayerSubject()
scoreboard = ScoreBoard()
environment = GameEnvironment()
player.register_observer(scoreboard)
player.register_observer(environment)
items = [Item() for _ in range(5)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (simplified)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Check for item collection
    for item in items[:]:
        if player.rect.colliderect(item.rect):
            player.collect_item(item)  # Player collects the item
            items.remove(item)  # Remove collected item

    # Update the screen
    screen.fill(WHITE)
    player.draw()
    for item in items:
        item.draw()
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
