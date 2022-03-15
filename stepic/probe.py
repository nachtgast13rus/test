lists = [int(i) for i in input().split()]
my_set = set()
# for i, item in enumerate(lists):
#     print(i, item)
for i in lists:
    if lists.count(i) > 1:
        my_set.add(i)
print(*my_set)