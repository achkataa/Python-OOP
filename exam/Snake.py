size = int(input())

snake_row_index = None
snake_col_index = None

matrix = []

for i in range(size):
    line = list(input())
    if "S" in line:
        snake_row_index = i
        snake_col_index = line.index("S")
    matrix.append(line)


def are_coordinates_valid(snake_row_index, snake_col_index, matrix):
    if snake_row_index < len(matrix)and snake_row_index > -1 and snake_col_index < len(matrix) and snake_col_index > -1:
        return True
    return False


food = 0
while food < 10:
    command = input()

    if command == "left":
        if are_coordinates_valid(snake_row_index, snake_col_index - 1, matrix):
            matrix[snake_row_index][snake_col_index] = "."
            if matrix[snake_row_index][snake_col_index - 1] == "B":
                matrix[snake_row_index][snake_col_index - 1] = "."
                for row in range(snake_row_index, len(matrix)):
                    for col in range(snake_col_index + 1, len(matrix)):
                        if matrix[row][col] == "B":
                            snake_row_index = row
                            snake_col_index = col
            elif matrix[snake_row_index][snake_col_index - 1] == "*":
                food += 1
                snake_col_index -= 1
            else:
                snake_col_index -= 1

            matrix[snake_row_index][snake_col_index] = "S"
        else:
            matrix[snake_row_index][snake_col_index] = "."
            break





    elif command == "right":
        if are_coordinates_valid(snake_row_index, snake_col_index + 1, matrix):
            matrix[snake_row_index][snake_col_index] = "."
            if matrix[snake_row_index][snake_col_index + 1] == "B":
                matrix[snake_row_index][snake_col_index + 1] = "."
                for row in range(snake_row_index, len(matrix)):
                    for col in range(snake_col_index + 1, len(matrix)):
                        if matrix[row][col] == "B":
                            snake_row_index = row
                            snake_col_index = col
            elif matrix[snake_row_index][snake_col_index + 1] == "*":
                food += 1
                snake_col_index += 1
            else:
                snake_col_index += 1

            matrix[snake_row_index][snake_col_index] = "S"
        else:
            matrix[snake_row_index][snake_col_index] = "."
            break
    elif command == "up":
        if are_coordinates_valid(snake_row_index - 1, snake_col_index, matrix):
            matrix[snake_row_index][snake_col_index] = "."
            if matrix[snake_row_index - 1][snake_col_index] == "B":
                matrix[snake_row_index - 1][snake_col_index] = "."
                for row in range(snake_row_index, len(matrix)):
                    for col in range(snake_col_index + 1, len(matrix)):
                        if matrix[row][col] == "B":
                            snake_row_index = row
                            snake_col_index = col
            elif matrix[snake_row_index - 1][snake_col_index] == "*":
                food += 1
                snake_row_index -= 1
            else:
                snake_row_index -= 1

            matrix[snake_row_index][snake_col_index] = "S"
        else:
            matrix[snake_row_index][snake_col_index] = "."
            break
    elif command == "down":
        if are_coordinates_valid(snake_row_index + 1, snake_col_index, matrix):
            matrix[snake_row_index][snake_col_index] = "."
            if matrix[snake_row_index + 1][snake_col_index] == "B":
                matrix[snake_row_index + 1][snake_col_index] = "."
                for row in range(len(matrix)):
                    for col in range(len(matrix)):
                        if matrix[row][col] == "B":
                            snake_row_index = row
                            snake_col_index = col
            elif matrix[snake_row_index + 1][snake_col_index] == "*":
                food += 1
                snake_row_index += 1
            else:
                snake_row_index += 1

            matrix[snake_row_index][snake_col_index] = "S"
        else:
            matrix[snake_row_index][snake_col_index] = "."
            break


if food >= 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food}")
for row in matrix:
    print(''.join(row))
