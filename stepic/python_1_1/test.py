text = [int(i) for i in input().split()]
my_lists = []
if len(text) == 1:
    print(text[0])
elif len(text) == 2:
    my_lists.append(text[0] * 2)
    my_lists.append(text[1] * 2)
    print(*my_lists)
else:
    my_lists.append(text[1] + text[-1])
    for i in range(len(text) - 1):
        if i == 0 or i == len(text) - 1:
            continue
        else:
            my_lists.append(text[i - 1] + text[i + 1])
    my_lists.append(text[-2] + text[0])
    print(*my_lists)


# numbers = [int(i) for i in input().split()]
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     for i in range(len(numbers)):
#         print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")
