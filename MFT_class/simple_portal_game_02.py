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
BLACK = (0, 150,255)
RED = (255,50,0)
YELLOW = (255,255,0)
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
    screen_width_in_tiles = SCREEN_WIDTH // cloud_size  # Calculate how many tiles fit on the screen
    for y, row in enumerate(level_map):
        for x, tile in enumerate(row):
            effective_x = (x * cloud_size - offset_x) % (screen_width_in_tiles * cloud_size)
            if tile == 1:
                pygame.draw.rect(screen, WHITE, (effective_x, (y * cloud_size), cloud_size, cloud_size / 2))
            elif tile == 2:
                # For greens, if you want them to wrap around too, uncomment the next line and adjust as needed
                # effective_x = (x * green_size - offset_x) % (screen_width_in_tiles * green_size)
                pygame.draw.rect(screen, RED, (effective_x, (y * green_size + SCREEN_HEIGHT - 150), green_size, green_size / 4))

def main():
    offset_x = 0  # Horizontal offset for simulating camera movement
    player_y = SCREEN_HEIGHT // 2  # Player's vertical position
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
            player_y -= move_speed
            if player_y < 0:  # Prevent the player from moving off-screen upwards
                player_y = 0
        if keys[pygame.K_DOWN]:
            player_y += move_speed
            if player_y > SCREEN_HEIGHT - player_size:  # Prevent the player from moving off-screen downwards
                player_y = SCREEN_HEIGHT - player_size

        screen.fill((0, 150, 255))  # Clear screen with the sky color
        pygame.draw.rect(screen, GREEN, (0, 450, 800, 150))  # Draw the ground
        pygame.draw.circle(screen, YELLOW, (750, 60), (50))  # Draw the sun
        
        # Draw the player based on the updated vertical position and fixed horizontal center position
        pygame.draw.rect(screen, player_color, (player_pos[0], player_y, player_size, player_size))

        # Draw the environment and the portal with the horizontal offset and fixed vertical position
        draw_environment(screen, offset_x, 0)  # `offset_y` is not used anymore, so it's set to 0

        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Maintain 60 frames per second

if __name__ == "__main__":
    main()