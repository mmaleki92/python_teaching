import pygame
import random
import string

chars = string.ascii_uppercase
pygame.init()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 500, 500
n_cell = 20
dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix")
font = pygame.font.SysFont(None, 30)

grid = [[0 for i in range(n_cell)] for j in range(n_cell)]
clock = pygame.time.Clock()

def plot_grid(grid):
    for n1, col in enumerate(grid):
        for n2, cell in enumerate(col):
            if cell != 0:
                dis.blit(cell, (n1 * WIDTH // n_cell, n2 * HEIGHT // n_cell))
            else:
                pygame.draw.rect(dis, BLACK, [n1 * WIDTH // n_cell, 
                                              n2 * HEIGHT // n_cell, 
                                              WIDTH // n_cell - 5, 
                                              HEIGHT // n_cell])

def update_grid(grid):
    for col in grid:
        ran = random.random()
        if ran < 0.70:
            word = font.render(random.choice(chars), False, GREEN, (9, 48, 24))
            
            col.insert(0, word)
            col.pop()
        else:
            col.insert(0, 0)
            col.pop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    update_grid(grid)
    plot_grid(grid)
    pygame.display.update()

    clock.tick(10)
