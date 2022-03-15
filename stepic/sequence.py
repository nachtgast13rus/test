string = ''
my_list = []
new_list = []
num = int(input())
if num == 1:
    new_list.append(1)
elif num == 2:
    new_list.append(1)
    new_list.append(1)
else:
    for i in range(1, num):
        my_list.append([i] * i)
    for i in my_list:
        new_list.extend(i)
print(*new_list[0: num])

# n = int(input())
# a = []
# i = 0
# while len(a) < n:
#     a += [i] * i
#     i += 1
# print(*a[:n])