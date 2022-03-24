import requests

with open('dataset2.txt', 'r', encoding='utf-8') as file:
    link = file.read().strip()
print(link)
text = requests.get(link).text.splitlines()
url = "https://stepic.org/media/attachments/course67/3.6.3/"
text = "".join(text)
control = 'We'
while True:
    if control in text:
        break
    else:
        url1 = url + text
        print(url1)
        text = requests.get(url1).text.splitlines()
        text = "".join(text)
print(text)