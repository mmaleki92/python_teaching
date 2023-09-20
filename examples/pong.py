import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5
paddle1_x = 50
paddle1_y = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2
paddle2_x = WINDOW_WIDTH - 50 - PADDLE_WIDTH
paddle2_y = WINDOW_HEIGHT / 2 - PADDLE_HEIGHT / 2

# Set up the ball
BALL_SIZE = 20
BALL_SPEED = 5
ball_x = WINDOW_WIDTH / 2 - BALL_SIZE / 2
ball_y = WINDOW_HEIGHT / 2 - BALL_SIZE / 2
ball_dx = BALL_SPEED * random.choice([-1, 1])
ball_dy = BALL_SPEED * random.choice([-1, 1])

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    elif keys[pygame.K_s] and paddle1_y + PADDLE_HEIGHT < WINDOW_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    elif keys[pygame.K_DOWN] and paddle2_y + PADDLE_HEIGHT < WINDOW_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with walls
    if ball_y <= 0 or ball_y + BALL_SIZE >= WINDOW_HEIGHT:
        ball_dy *= -1
    if ball_x <= 0:
        game_over = True
    if ball_x + BALL_SIZE >= WINDOW_WIDTH:
        game_over = True
        
    # Check for collisions with paddles
    if ball_x <= paddle1_x + PADDLE_WIDTH and ball_y >= paddle1_y and ball_y + BALL_SIZE <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    if ball_x + BALL_SIZE >= paddle2_x and ball_y >= paddle2_y and ball_y + BALL_SIZE <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Clear the screen
    window.fill(BLACK)

    # Draw the paddles
    pygame.draw.rect(window, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.rect(window, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
