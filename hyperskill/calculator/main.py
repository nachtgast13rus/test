msg = ("Enter an equation",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):\n",
       "Do you want to continue calculations? (y / n):\n",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)\n",
       "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
       "Last chance! Do you really want to embarrass yourself? (y / n)\n")

operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}

memory = 0.0


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    result = ''
    result = result + msg[6] if is_one_digit(v1) and is_one_digit(v2) else result
    result = result + msg[7] if (v1 == 1 or v2 == 1) and v3 == '*' else result
    result = result + msg[8] if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-') else result
    if result != '':
        result = msg[9] + result
        print(result)


def save_confirm(memory, result):
    if is_one_digit(result):
        msg_index = 10
        while True:
            if input(msg[msg_index]) == 'y':
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    return result
            else:
                return memory
    else:
        return result


while True:
    print(msg[0])
    x, oper, y = input().split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operations[oper](x, y)
        print(result)
        if input(msg[4]) == "y":
            memory = save_confirm(memory, result)
        if input(msg[5]) == "n":
            break
    except ValueError:
        print(msg[1])
    except KeyError:
        print(msg[2])
    except ZeroDivisionError:
        print(msg[3])
