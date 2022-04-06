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