import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
dis = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()
game = True
x, y = 10, 10
x_change, y_change = 0, 0

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
    if x>400:
        x = 0
    
    if y>300:
        y = 0
    dis.fill(BLACK)


    pygame.draw.rect(dis, RED, [x, y, 50, 50])
    pygame.display.update()
    
   # x_change, y_change = 0, 0

    clock.tick(30)
pygame.quit()
quit()