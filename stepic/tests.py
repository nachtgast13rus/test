matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(i, j, matrix[i][j], end=" ")
    print()
i = 1
j = 0
if (i != 0 and i != len(matrix) - 1):
    print(i)
print(i, j)
print(matrix[i][j + 1], matrix[i + 1][j], matrix[i][j - 1], matrix[i - 1][j])
