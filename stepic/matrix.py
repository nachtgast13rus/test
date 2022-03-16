a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
for i in range(len(a)):
    for j in range(len(a[i])):
        print((a[i - 1][j] + a[(i + 1) % len(a)][j] + a[i][j - 1] + a[i][(j + 1) % len(a[i])]), end=' ')
    print()
