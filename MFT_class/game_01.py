import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)

G_color = (255, 255, 0)

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
    # pressed = pygame.key.get_pressed()
    # print(pressed[pygame.K_d])
    #if x+x_change<=350 and x+x_change>-5:
  #      x = x + x_change
    
  #  if y+y_change<=250 and y+y_change>-5:
  #      y = y + y_change
    
    x = x + x_change
    y = y + y_change

    x_g = x_g - x_change
    y_g = y_g - y_change
    
    if x>400:
        x = 0
        size_x = size_x + 5
    elif x<0:
        x = 400
        size_x = size_x - 5
    if y>300:
        y = 0
        size_y = size_y + 5
    elif y<0:
        y = 300
        size_y = size_y - 5

    if x_g>400:
        x_g = 0
    elif x_g<0:
        x_g = 400

    if y_g>300:
        y_g = 0
    elif y_g<0:
        y_g = 300


    dis.fill(BLACK)

    pygame.draw.rect(dis, RED, [x, y, size_x, size_y])
    pygame.draw.rect(dis, G_color, [x_g, y_g, 50, 50])


    pygame.display.update()

    # x_change, y_change = 0, 0

    clock.tick(40)
pygame.quit()
quit()