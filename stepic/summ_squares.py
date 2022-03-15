summ, total = 0, 0
while True:
    num = int(input())
    summ += num
    if summ == 0:
        break
    else:
        total += num ** 2
print(total)
# s=[int(input())]
# while sum(s)!=0: s.append(int(input()))
# print(sum([i**2 for i in s]))