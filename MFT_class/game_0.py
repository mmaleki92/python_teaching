import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

dis = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()
game = True
x, y = 10, 10

x_g, y_g = 400 - 10, 300 - 10

x_change, y_change = 0, 0
size_x, size_y = 50, 50

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_change = -5
                x_change = 0
            elif event.key == pygame.K_d:
                y_change = 0
                x_change = 5
            elif event.key == pygame.K_s:
                y_change = 5
                x_change = 0
            elif event.key == pygame.K_a:
                y_change = 0
                x_change = -5

    x = x + x_change
    y = y + y_change

    x_g = x_g - x_change
    y_g = y_g - y_change
    
    dis.fill(BLACK)

    pygame.draw.rect(dis, RED, [x, y, size_x, size_y])


    pygame.display.update()

    clock.tick(40)
pygame.quit()
quit()