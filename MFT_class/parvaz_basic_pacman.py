import pygame
from pygame.locals import Rect

pygame.init()

dis = pygame.display.set_mode((900, 400))


ghost = pygame.image.load("image.png")
ghost = pygame.transform.scale(ghost, [50, 50])

pygame.display.update()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

x  = 100
y = 100

x_green  = 200
y_green = 200

x_change = 0
y_change = 0

clock = pygame.time.Clock()
step = 5
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -step
                y_change = 0
            elif event.key == pygame.K_d:
                x_change = step
                y_change = 0
            elif event.key == pygame.K_w:
                y_change = -step
                x_change = 0
            elif event.key == pygame.K_s:
                y_change = step
                x_change = 0

    dis.fill(BLACK)
    x += x_change
    y += y_change

    if x_green < x:
        x_green += 2
    else:
        x_green -= 2

    if y_green < y:
        y_green += 2
    else:
        y_green -= 2

    # y_green -= y_change

    p1 = Rect([x % 900, y % 400, 50, 200])
    p2 = Rect([x_green % 900, y_green % 400, 50, 50])

    c = pygame.Rect.colliderect(p1, p2)
    if c:
        print("Gereftamet!") 
    # player
    pygame.draw.rect(dis, RED, [x % 900, y % 400, 50, 50])
    
    # enemy!
    # pygame.draw.rect(dis, GREEN, [x_green % 900, y_green % 400, 50, 50])
    dis.blit(ghost, [x_green % 900, y_green % 400])
    # env
    pygame.draw.rect(dis, GREEN, [0, 300, 900, 100])

    pygame.display.update()
    clock.tick(60)

pygame.quit()

