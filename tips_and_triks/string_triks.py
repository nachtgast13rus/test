from string import Template


def format_string():
    """
    Пример форматирования строки через f-cтроки
    :return: None
    """
    name = "Dimon"
    print(f"Hello, {name}")


def template_string():
    """
    Пример форматирования строк полученых от пользователя(в целях безопасности)
    :return:
    """
    name = input("What is your name? > ")
    greet = Template("Hello, $name!")
    print(greet.substitute(name=name))


def main():
    # format_string()
    template_string()


if __name__ == "__main__":
    main()
