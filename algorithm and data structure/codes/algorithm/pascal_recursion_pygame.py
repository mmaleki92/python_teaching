import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up Pygame
pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pascal's Triangle")

# Function to generate Pascal's Triangle recursively
def generate_pascal_triangle(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return generate_pascal_triangle(row - 1, col - 1) + generate_pascal_triangle(row - 1, col)

# Function to draw Pascal's Triangle
def draw_pascal_triangle(num_rows):
    triangle = []
    for row in range(num_rows):
        row_values = []
        for col in range(row + 1):
            value = generate_pascal_triangle(row, col)
            row_values.append(value)
        triangle.append(row_values)

    max_value = max(max(row) for row in triangle)

    # Calculate cell size for drawing
    cell_width = WINDOW_SIZE[0] // (num_rows * 2)
    cell_height = WINDOW_SIZE[1] // num_rows

    for row in range(num_rows):
        for col in range(len(triangle[row])):
            x = (col * 2 + 1) * cell_width
            y = row * cell_height

            # Draw cell
            pygame.draw.rect(screen, WHITE, (x, y, cell_width, cell_height), 0)

            # Draw value in the cell
            font = pygame.font.Font(None, 24)
            text = font.render(str(triangle[row][col]), True, BLACK)
            text_rect = text.get_rect(center=(x + cell_width // 2, y + cell_height // 2))
            screen.blit(text, text_rect)

            # Draw diagonal lines connecting the cells
            if col > 0:
                pygame.draw.line(screen, RED, (x, y), (x - cell_width, y + cell_height), 1)
            if col < len(triangle[row]) - 1:
                pygame.draw.line(screen, RED, (x, y), (x + cell_width, y + cell_height), 1)

    pygame.display.update()


def main():
    num_rows = 10
    draw_pascal_triangle(num_rows)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
