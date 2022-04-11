import random


def greetings():
    while True:
        try:
            choice = int(input(f"Which level do you want? Enter a number:\n"
                               "1 - simple operations with numbers 2-9\n"
                               "2 - integral squares of 11-29\n"))
            if 0 < choice < 3:
                return choice
            else:
                raise ValueError
        except ValueError:
            print("Incorrect format.")
            continue


def easy_tasks():
    global mark
    count = 0
    right_answer = 0
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
                    right_answer += 1
                    break
                else:
                    print("Wrong")
                    break
            except ValueError:
                print("Wrong format! Try again.")
                continue
        count += 1
    mark = right_answer
    print(f"Your mark is {right_answer}/5. Would you like to save the result? Enter yes or no.")
    return input()


def hard_task():
    global mark
    count = 0
    right_answer = 0
    while count < 5:
        num = random.randint(11, 29)
        answer = num ** 2
        print(num)
        while True:
            try:
                user_answer = int(input())
                if user_answer == answer:
                    print("Right")
                    right_answer += 1
                    break
                else:
                    print("Wrong")
                    break
            except ValueError:
                print("Wrong format! Try again.")
                continue
        count += 1
    mark = right_answer
    print(f"Your mark is {right_answer}/5. Would you like to save the result? Enter yes or no.")
    return input()


def exiting(user_choice):
    name = input("What is your name?\n")
    with open("results.txt", "a+", encoding="utf-8") as file:
        if user_choice == 1:
            file.write(f"{name}: {mark}/5 in level {user_choice} (simple operations with numbers 2-9).\n")
        else:
            file.write(f"{name}: {mark}/5 in level {user_choice} (integral squares of 11-29).\n")
    print('The results are saved in "results.txt".')


def main():
    user_choice = greetings()
    if user_choice == 1:
        is_exit = easy_tasks()
    else:
        is_exit = hard_task()
    if is_exit in ["yes", "YES", "y", "Yes"]:
        exiting(user_choice=user_choice)


if __name__ == "__main__":
    mark = 0
    main()
