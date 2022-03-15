numbers = [int(i) for i in input().split()]
num = int(input())
my_lists = []
for index, value in enumerate(numbers):
    if numbers.count(num) >= 1:
        if value == num:
            my_lists.append(index)
    else:
        print("Отсутствует")
        break
print(*my_lists)

# l, n = [int(i) for i in input().split()], int(input())
# print(*[x for x in range(len(l)) if l[x]==n] if n in l else ["Отсутствует"])
