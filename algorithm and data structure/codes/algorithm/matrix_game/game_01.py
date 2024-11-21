import pygame
import random


RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 500, 500
n_cell = 30
dis = pygame.display.set_mode((WIDTH, HEIGHT))


grid = [[0 for i in range(n_cell)] for j in range(n_cell)]
clock = pygame.time.Clock()

def plot_grid(grid):
    for n1, col in enumerate(grid):
        for n2, cell in enumerate(col):
            if cell == 1:
                pygame.draw.rect(dis, RED, [n1 * WIDTH // n_cell, n2 * HEIGHT // n_cell, WIDTH // n_cell - 5, HEIGHT // n_cell])
            else:
                pygame.draw.rect(dis, BLACK, [n1 * WIDTH // n_cell, n2 * HEIGHT // n_cell, WIDTH // n_cell- 5, HEIGHT // n_cell])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for col in grid:
        ran = random.random()
        if ran < 0.3:
            col.insert(0, 1)
            col.pop()
        else:
            col.insert(0, 0)
            col.pop()
    plot_grid(grid)
    pygame.display.update()

    clock.tick(40)
