print('Hello, World')
print('Initial commit...')

my_sklad = {"Evgen": 35, "Kobzon": 40, "Sosok": 45}
my_sklad["Slavok"] = 43
for key in my_sklad:
    print(key)
for values in my_sklad.values():
    print(values)
for items in my_sklad.items():
    print(items)
if isinstance(my_sklad['Evgen'], int):
    print("Helo")
