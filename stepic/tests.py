matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(i, j, matrix[i][j], end=" ")
    print()
i = 0
j = len(matrix[i]) - 1
print(matrix[i][j - 1] + matrix[i + 1][j] + matrix[i][j - j] + matrix[i - 1][j])