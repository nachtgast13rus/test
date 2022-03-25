# lists = [input() for _ in range(3)]
# print(*lists[::-1], sep="\n")
# [print(sum([int(input()) for _ in range(3)]))]

# num = int(input())
# first_num = num // 100
# second_number = num % 100 // 10
# third_number = num % 10
# summa = first_num + second_number + third_number

# a,b,c,d = input()
# print(f"Цифра в позиции тысяч равна {a}\n"
#       f"Цифра в позиции сотен равна {b}\n"
#       f"Цифра в позиции десятков равна {c}\n"
#       f"Цифра в позиции единиц равна {d}")

a = input()
print(int(a) + int(a + a) + int(a + a + a))