def input_password():
    pass1 = input()
    pass2 = input()
    check_password(pass1, pass2)


def check_password(*args, **kwargs):
    if args[0] == args[1]:
        print("Пароль принят")
    else:
        print("Пароль не принят")


def main():
    input_password()


if __name__ == "__main__":
    main()


# print('Пароль принят' if input() == input() else 'Пароль не принят')
# print(('Четное','Нечетное')[ int(input()) % 2 ])