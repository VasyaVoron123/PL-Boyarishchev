def is_magic_square(matrix):
    n = len(matrix)

    target_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True

matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")
