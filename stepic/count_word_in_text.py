with open('text.txt', 'r', encoding='utf-8') as file:
    words = [i for i in file.read().lower().split()]

max = 0
winner = ''
for i in words:
    if words.count(i) > max:
        winner = i
        max = words.count(i)
winner_list = []
winner_list.append(winner)
for i in words:
    if words.count(i) == max:
        winner_list.append(i)
print(winner, max)


print(words)


