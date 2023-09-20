import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = 5  # x-axis velocity
        self.dy = 5  # y-axis velocity

    def update(self):
        # Update ball position
        self.x += self.dx
        self.y += self.dy

        # Check for collision with window edges
        if self.x + self.radius > WIDTH or self.x - self.radius < 0:
            self.dx *= -1
        if self.y + self.radius > HEIGHT or self.y - self.radius < 0:
            self.dy *= -1

    def draw(self):
        # Draw the ball on the window
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

# Create Ball object
ball = Ball(WIDTH // 2, HEIGHT // 2, 20, WHITE)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball.update()

    # Clear the window
    window.fill(BLACK)

    # Draw the ball
    ball.draw()

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
