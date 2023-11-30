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

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Item class
class Item:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(100, 700), random.randint(100, 500), 30, 30)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Game loop
running = True
player = Player()
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
            player.score += 10  # Increase score
            items.remove(item)  # Remove collected item

    # Update the screen
    screen.fill(WHITE)
    player.draw()
    for item in items:
        item.draw()
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
