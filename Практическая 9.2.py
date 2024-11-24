def swap_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        matrix[i][0], matrix[i][m - 1] = matrix[i][m - 1], matrix[i][0]

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("До перестановки:")
for row in matrix:
    print(row)

matrix = swap_columns(matrix)

print("\nПосле перестановки:")
for row in matrix:
    print(row)
