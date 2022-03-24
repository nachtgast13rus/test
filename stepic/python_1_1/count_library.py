library = {}
count = 1
words =  [i for i in input().lower().split()]
for i in words:
    if i not in library:
        library[i] = count
    else:
        library[i] += 1
for i, j in library.items():
    print(i, j)

# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))