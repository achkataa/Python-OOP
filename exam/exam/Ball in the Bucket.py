matrix = []
for i in range(6):
    line = input().split()
    matrix.append(line)

def are_coordinates_valid(row, col, matrix):
    if row < len(matrix) and row > -1 and col < len(matrix) and col > -1:
        return True
    return False

points = 0
for i in range(3):
    throw = input()[1:-1].split(", ")
    row = int(throw[0])
    col = int(throw[1])

    if are_coordinates_valid(row, col, matrix):
        if matrix[row][col] == "B":
            matrix[row][col] = "."
            for row in range(len(matrix)):
                if matrix[row][col].isdigit():
                    points += int(matrix[row][col])


toys = ["Football", "Teddy Bear", "Lego Construction Set"]

def picked_toy(toys, points):
    if points >= 100 and points <= 199:
        return toys[0]
    elif points >= 200 and points <= 299:
        return toys[1]
    elif points >= 300:
        return toys[2]

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    print(f"Good job! You scored {points} points, and you've won {picked_toy(toys, points)}.")

