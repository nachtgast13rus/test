count = 0
with open("test.txt", 'r', encoding="utf-8") as file:
    # for line in file:
    #     if line.strip() == "summer":
    #         count += 1
    # for line in file:
    #     print(sum([int(i) for i in line.strip().split()]))
    text = [el.strip() for el in file]
    print(text[0])
