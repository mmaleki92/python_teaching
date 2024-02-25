import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# Player settings
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # Player stays in the center of the screen
player_size = 50
player_color = BLUE

# Portal settings
portal_color = WHITE
portal_pos = [SCREEN_WIDTH, SCREEN_HEIGHT]  # Initial portal position relative to the player
portal_size = 60

# Clouds and greens map
level_map = [
    [0, 1, 0, 2, 0, 1, 2, 0, 1, 0],
    [2, 0, 1, 0, 2, 0, 1, 2, 0, 1],
    [0, 2, 0, 1, 0, 2, 0, 1, 2, 0],
]  # Extended the map for more area to explore

cloud_size = 60
green_size = 60

# Movement speed of the environment
move_speed = 5

def draw_environment(screen, offset_x, offset_y):
    for y, row in enumerate(level_map):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, WHITE, ((x * cloud_size) - offset_x, (y * cloud_size) - offset_y, cloud_size, cloud_size / 2))
            elif tile == 2:
                pygame.draw.rect(screen, GREEN, ((x * green_size) - offset_x, (y * green_size + SCREEN_HEIGHT - 150) - offset_y, green_size, green_size / 4))

def main():
    offset_x, offset_y = 0, 0  # Offset for simulating camera movement
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            offset_x -= move_speed
        if keys[pygame.K_RIGHT]:
            offset_x += move_speed
        if keys[pygame.K_UP]:
            offset_y -= move_speed
        if keys[pygame.K_DOWN]:
            offset_y += move_speed

        screen.fill((0, 0, 0))  # Clear screen

        # Draw the player (always in the center)
        pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

        # Draw the environment with offset
        draw_environment(screen, offset_x, offset_y)

        # Draw the portal with offset
        pygame.draw.rect(screen, portal_color, (portal_pos[0] - offset_x, portal_pos[1] - offset_y, portal_size, portal_size))

        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Maintain 60 frames per second

if __name__ == "__main__":
    main()
