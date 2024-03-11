import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 150, 255)
RED = (255, 50, 0)
YELLOW = (255, 255, 0)


# Enemy Properties
ENEMY_SIZE = 50
ENEMY_COLOR = (255, 0, 0)
ENEMY_SPEED = 7
enemies = []

# اضافه کردن دشمن
def add_enemy():
    enemy_y = random.randint(0, SCREEN_HEIGHT)
    enemies.append(pygame.Rect(SCREEN_WIDTH, enemy_y, ENEMY_SIZE, ENEMY_SIZE))

# این بخش برای حذف اونایی هست که بیرون میرن یا تغییر حرکت دشمناست
def update_enemies():
    for enemy in enemies[:]:
        enemy.x -= ENEMY_SPEED
        if enemy.x < -ENEMY_SIZE:  # اگر از صفحه خارج شد
            enemies.remove(enemy)
            add_enemy()  # اضافه کردن

# این بخش برای کشیدن لیستی از دشمنان است
def draw_enemies(screen):
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)

# این برای بررسی برخورد دو مربع است دشمن و بازیکن
def check_collision(player_rect, enemies):
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            return True
    return False

add_enemy()
player_pos = [250, 400]
player_size = 50
player_color = BLUE
player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
original_y = player_rect.y

jump = False
jump_count = 10
double_jump_allowed = False
double_jump = False

portal_color = WHITE
portal_pos = [SCREEN_WIDTH, SCREEN_HEIGHT]
portal_size = 60

level_map = [
    [0, 1, 0, 2, 0, 1, 2, 0, 1, 0],
    [2, 0, 1, 0, 2, 0, 1, 2, 0, 1],
    [0, 2, 0, 1, 0, 2, 0, 1, 2, 0],
]

cloud_size = 60
green_size = 60

move_speed = 5

def draw_environment(screen, offset_x, offset_y):
    screen_width_in_tiles = SCREEN_WIDTH // cloud_size
    for y, row in enumerate(level_map):
        for x, tile in enumerate(row):
            effective_x = (x * cloud_size - offset_x) % (screen_width_in_tiles * cloud_size)
            if tile == 1:
                pygame.draw.rect(screen, WHITE, (effective_x, (y * cloud_size), cloud_size, cloud_size / 2))
            elif tile == 2:
                pygame.draw.rect(screen, RED, (effective_x, (y * green_size + SCREEN_HEIGHT - 150), green_size, green_size / 4))

def main():
    global jump, jump_count, double_jump_allowed, double_jump
    offset_x = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not jump:
                        jump = True
                        double_jump_allowed = True
                    elif double_jump_allowed:
                        double_jump = True
                        double_jump_allowed = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            offset_x -= move_speed
        if keys[pygame.K_RIGHT]:
            offset_x += move_speed

        if jump:
            if jump_count >= -10:
                player_rect.y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 1
            else:
                player_rect.y = original_y
                jump_count = 10
                jump = False
                double_jump_allowed = False

        if double_jump:
            if jump_count >= -10:
                player_rect.y -= (jump_count * abs(jump_count)) * 0.5
                jump_count -= 1
            else:
                player_rect.y = original_y
                jump_count = 10
                double_jump = False

        screen.fill((0, 150, 255))
        pygame.draw.rect(screen, GREEN, (0, 450, 800, 150))
        pygame.draw.circle(screen, YELLOW, (750, 60), (50))

        pygame.draw.rect(screen, player_color, player_rect)

        update_enemies()

        # Check for collisions
        if check_collision(player_rect, enemies):
            print("Game Over!")  # Or any other game over handling
            break  # Exit the game loop

        # Drawing logic as before
        draw_enemies(screen)
        draw_environment(screen, offset_x, 0)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
