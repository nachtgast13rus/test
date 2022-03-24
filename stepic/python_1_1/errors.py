import itertools

words = []
for i in range(int(input())):
    words.append(input().lower())
texts = []
for i in range(int(input())):
    texts.append(input().lower())
new_text = []
for string in texts:
    new_text.append([i for i in string.split()])
more_texts = list(itertools.chain(*new_text))  # список списков в один список
errors = set()
for word in more_texts:
    if word not in words:
        errors.add(word)
print(*errors, sep='\n')
