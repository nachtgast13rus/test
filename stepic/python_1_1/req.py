from requests import get
with open('where_downloads.txt') as f:
    url = f.readline().strip()
text = get(url).text.splitlines()
print(len(text))