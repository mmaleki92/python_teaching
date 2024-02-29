import sys
import pygame
pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
display_x, display_y = 600, 700
dis = pygame.display.set_mode((display_x, display_y))

clock = pygame.time.Clock()

size_x, size_y = 100, 100

c1 = pygame.image.load("c1.png")
c1 = pygame.transform.scale(c1, (size_x, size_y))

c2 = pygame.image.load("c2.png")
c2 = pygame.transform.scale(c2, (size_x, size_y))

x, y = 500, 500
x_circle, y_circle = 100, 100

x_change, y_change = 0, 0
x_change_circle, y_change_circle = 0, 0

step = 10
game = True
while game:
    for event in pygame.event.get(): # event loop, flask, pyqt 
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = step
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -step
            if event.key == pygame.K_RIGHT:
                x_change = step
                y_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -step
                y_change = 0
    
    x = x + x_change
    y = y + y_change

    if x >= x_circle:
        x_change_circle = 3
    else:
        x_change_circle = -3

    if y >= y_circle:
        y_change_circle = 3
    else:
        y_change_circle = -3

    x_circle = x_circle + x_change_circle
    y_circle = y_circle + y_change_circle



    dis.fill(BLACK)
    # dis, color, [x, y, size_x, size_y]
    # pygame.draw.circle(dis, RED, [x_circle, y_circle], 10)
    dis.blit(c2, [x_circle, y_circle])


    dis.blit(c1, [x, y] )
    # pygame.draw.rect(dis, RED, [x, y, size_x, size_y])

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
