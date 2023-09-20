def generate_pascal_triangle(num_rows):
    triangle = []

    for row in range(num_rows):
        # Create a new row with initial value of 1
        current_row = [1]

        # Fill the row with values from the previous row
        if triangle:
            previous_row = triangle[-1]
            for i in range(len(previous_row) - 1):
                current_row.append(previous_row[i] + previous_row[i+1])

            current_row.append(1)

        # Add the current row to the triangle
        triangle.append(current_row)

    return triangle


def print_pascal_triangle(triangle):
    for row in triangle:
        # Adjust spacing for formatting
        row_str = ' '.join(str(num) for num in row)
        print(row_str.center(50))


# Generate and print Pascal's Triangle with 10 rows
num_rows = 10
pascal_triangle = generate_pascal_triangle(num_rows)
print_pascal_triangle(pascal_triangle)
