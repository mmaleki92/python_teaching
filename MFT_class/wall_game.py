import pygame
from pygame.locals import Rect

dis = pygame.display.set_mode((500, 500))

#RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
gameover = False
clock = pygame.time.Clock()
x, y = 0, 0
x_change, y_change = 0, 0

while not gameover:
    for event in pygame.event.get(): # event loop!
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                x_change = 0
                y_change = -10
            if event.key == pygame.K_s:
                    x_change = 0
                    y_change = 10
            if event.key == pygame.K_a:
                    x_change = -10
                    y_change = 0
            if event.key == pygame.K_d:
                    x_change = 10
                    y_change = 0

    dis.fill(BLACK)


    p1 = Rect([x + x_change, y + y_change, 50, 50])
    p2 = Rect([0, 400, 500, 50])
    wall = Rect([0, 400, 500, 50])
    
    col1 =  pygame.Rect.colliderect(p1, p2)
    
    if not col1:
        x = x + x_change
        y = y + y_change
    if col1:
        y_change = -y_change
        x_change = -x_change
    pygame.draw.rect(dis, RED, [x, y, 50, 50])
    pygame.draw.rect(dis, YELLOW, [0, 400, 500, 50])

    pygame.display.update()

    clock.tick(30)
