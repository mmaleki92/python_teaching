import pygame

display = pygame.display.set_mode((500, 500))

# R G B
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
x, y = 0, 0
snake =  [[50, 100], [50, 150], [50, 200]]

clock = pygame.time.Clock()
x_change = 0
y_change = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                x_change = 50
                y_change = 0        
            if event.key == pygame.K_LEFT: 
                x_change = -50
                y_change = 0
            if event.key == pygame.K_UP: 
                y_change = -50
                x_change = 0
            if event.key == pygame.K_DOWN: 
                y_change = 50
                x_change = 0

    display.fill(BLACK)
    x = x + x_change
    y = y + y_change

    snake.append([x, y])
    snake.pop(0)
    
    for x_map, y_map in snake:
        pygame.draw.rect(display, GREEN, [x_map, y_map, 40, 40])
    # for x_map, y_map in MAP:
    #     pygame.draw.circle(display, GREEN, [x_map, y_map], 5)

    pygame.display.update()

    clock.tick(10)

