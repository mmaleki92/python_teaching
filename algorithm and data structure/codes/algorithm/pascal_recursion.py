def generate_pascal_triangle(row, col):
    if col == 0 or col == row:
        return 1
    else:
        return generate_pascal_triangle(row - 1, col - 1) + generate_pascal_triangle(row - 1, col)


def print_pascal_triangle(num_rows):
    for row in range(num_rows):
        row_values = [str(generate_pascal_triangle(row, col)) for col in range(row + 1)]
        row_str = ' '.join(row_values).center(50)
        print(row_str)


# Print Pascal's Triangle with 10 rows
num_rows = 10
print_pascal_triangle(num_rows)
