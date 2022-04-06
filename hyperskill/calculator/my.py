MSG_0 = "Enter an equation"
MSG_1 = "Do you even know what numbers are? Stay focused!"
MSG_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
MSG_3 = "Yeah... division by zero. Smart move..."
MSG_4 = "Do you want to store the result? (y / n):\n"
MSG_5 = "Do you want to continue calculations? (y / n):\n"

operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0.0

while True:
    print(MSG_0)
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        result = operations[oper](x, y)
        print(result)
        if input(MSG_4) == "y":
            memory = result
        if input(MSG_5) == "n":
            break
    except ValueError:
        print(MSG_1)
    except KeyError:
        print(MSG_2)
    except ZeroDivisionError:
        print(MSG_3)

# memory = 0
# flag = True
# while flag:
#     try:
#         result = 0
#         x, operator, y = input("Enter an equation ").split()
#         if x == 'M':
#             x = memory
#         if y == 'M':
#             y = memory
#         if operator not in "+-*/":
#             print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
#             continue
#         elif operator == '+':
#             result = float(x) + float(y)
#         elif operator == '-':
#             result = float(x) - float(y)
#         elif operator == '*':
#             result = float(x) * float(y)
#         elif operator == '/':
#             result = float(x) / float(y)
#     except ValueError:
#         print("Do you even know what numbers are? Stay focused!")
#         continue
#     except ZeroDivisionError:
#         print("Yeah... division by zero. Smart move...")
#         continue
#     else:
#         print(result)
#         while True:
#             print("Do you want to store the result? (y / n): ")
#             answer = input()
#             if answer == 'y':
#                 memory = result
#             else:
#                 if answer != 'n':
#                     continue
#             print("Do you want to continue calculations? (y / n): ")
#             answer = input()
#             if answer == "y":
#                 break
#             else:
#                 if answer != 'n':
#                     continue
#                 else:
#                     flag = False
#                     break
