text = "abc"  # str.join(input())
msg = ''
count = 0
i = 0
text = text + "?"
temp = text[0]
while i < len(text):
    if text[i] == temp and text[i] != '?':
        count += 1
        i += 1
        # temp = text[i]
    else:
        msg = msg + temp + str(count)
        count = 1
        temp = text[i]
        i += 1

print(msg)
