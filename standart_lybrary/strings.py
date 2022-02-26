text = "Hello, world!"
length = len(text)  # Длинна строки
index_o = text.find('o')  # Индекс первого вхождения с начала строки (4)
index_o_right = text.rfind('l')  # Индекс первого вхождения с конца строки (10)
print(index_o, index_o_right)
replace_text = text.replace('l', 'Я')  # Замена символов
print(replace_text)
replace_text = replace_text.upper()
print(replace_text)
replace_text = replace_text.lower()
print(replace_text)

text = "asd"

if text.isalpha():  # isalpha() isdigit()
    print("Only letters")
