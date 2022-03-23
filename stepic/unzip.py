with open('open1.txt', 'r', encoding='utf-8') as file:
    chars = []
    temp = ''
    for line in file:
        for i in line:
            if i.isdigit():
                temp += i
            else:
                if temp != '':
                    chars.append(int(temp))
                    temp = ''
                chars.append(i)
        chars.append(temp)
chars.remove(chars[-1])
chars.remove(chars[-1])
letters = []
numbers = []
for i in chars:
    if isinstance(i, int):
        numbers.append(i)
    elif isinstance(i, str):
        letters.append(i)
msg = ''
for i in range(len(letters)):
    msg += letters[i] * numbers[i]
print(chars)
print(numbers)
print(letters)
print(msg)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(msg)
