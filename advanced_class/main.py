import sys
import pygame
pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
display_x, display_y = 600, 400
dis = pygame.display.set_mode((display_x, display_y))

clock = pygame.time.Clock()

x, y = 100, 100
size_x, size_y = 50, 50
x_change, y_change = 0, 0
game = True
while game:
    for event in pygame.event.get(): # event loop, flask, pyqt 
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0.5
    
    x = x + x_change
    y = y + y_change
    dis.fill(BLACK)
    # dis, color, [x, y, size_x, size_y]
    pygame.draw.rect(dis, RED, [x, y, size_x, size_y])

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()