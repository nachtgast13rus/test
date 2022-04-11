import random

count = 0
right_ansver = 0
while count < 5:
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operation = random.choice("+-*")
    answer = eval(f"{num1} {operation} {num2}")
    print(f"{num1} {operation} {num2}")
    while True:
        try:
            user_answer = int(input())
            if user_answer == answer:
                print("Right")
                right_ansver += 1
                break
            else:
                print("Wrong")
                break
        except ValueError:
            print("Incorrect format")
            continue
    count += 1

print(f"Your mark is {right_ansver}/5")
