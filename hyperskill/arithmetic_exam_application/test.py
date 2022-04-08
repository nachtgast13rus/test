import random

num1 = random.randint(2, 9)
num2 = random.randint(2, 9)
operation = random.choice("+-*")
answer = eval(f"{num1} {operation} {num2}")

user_answer = input(f"{num1} {operation} {num2}\n")
print("Right!" if int(user_answer) == answer else "Wrong!")
