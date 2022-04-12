def threefold():
    """
    Print a list of numbers from 1 to 1000 that can be divided by 3.
    :return:
    """
    print(*[i for i in range(1, 1001) if i % 3 == 0])


def length():
    """
    Given a list of words in the code below, create a list of lengths of those words and print it.
    :return:
    """
    words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
             "apothecary"]
    print([len(word) for word in words])


def word_list():
    """
    Create a list of words from the text below that are shorter than or equal to the input value. Print the new list.
    :return:
    """
    text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
            ["Ephemeral", "lasts", "one", "day", "only"],
            ["Accolade", "is", "an", "expression", "of", "praise"]]
    lengths = int(input())
    print([word for lists in text for word in lists if len(word) <= lengths])


def tennis_tournament():
    """
    Several warm-up matches have been played at the tennis tournament. You have data on the victories and losses of
    some players. Save the names of the winners to a list and calculate the total number of victories.
    :return:
    """
    num = int(input())
    members = [input().split() for _ in range(num)]
    my_list = [result[0] for result in members if result[1] == 'win']
    print(my_list)
    print(len(my_list))


def latin_equivalents():
    dict_replace = {"é": "e",
                    "ë": "e",
                    "á": "a",
                    "å": "a",
                    "œ": "oe",
                    "æ": "ae"}
    name = input()
    new_name = ''
    for i in name:
        if i in dict_replace:
            new_name = name.replace(i, dict_replace[i])
    return new_name


def straight_a():
    """
    Write a program that calculates the proportion of students who received grade A.
    A five-point rating system with grades A, B, C, D, F is used.
    :return:
    """
    grades = input().split()
    print(round(grades.count("A") / len(grades), 2))


def fix_the_mistakes():
    text = input().split()
    for word in text:
        if word.lower().startswith("https://") or word.lower().startswith("http://") or word.lower().startswith("www."):
            print(word)


def prime_numbers():
    """
    In math, we call a natural number prime if it's greater than 1 and can be divided without any remainder only by 1
    and itself:
    2, 3, 5, 7, 11, 13, 17, ...
    Create a list of all prime numbers up to 1000 in the code below. Just save this list into a variable prime_numbers,
    you don't have to print anything.
    :return:
    """
    prime_numbers = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]


def implementing_logic():
    """
    Advanced input() handling is used to read input directly into several variables, e. g.,
    name, surname = input().split(), but a user still can enter more or fewer words.
    In this task, you have to make sure that the user entered the necessary amount of words and...
    If there are more or fewer words in the input, print an error: "You need to enter exactly 2 words. Try again!"
    If everything's good, greet the user personally.

    :return:
    """
    try:
        name, surname = input().split()
    except ValueError:
        print("You need to enter exactly 2 words. Try again!")
    else:
        print(f"Welcome to our party, {name} {surname}")


def catching_built_in_exceptions():
    """
    You know how to catch the built-in exceptions. Right now, try to read two numbers (a, b) and find the result of
    their division. Your main task it to catch the ZeroDivisionError. If there's an error, print the following
    message: The Error!. Otherwise, print the result of the division.
    :return:
    """
    a = int(input())
    b = int(input())
    try:
        print(a / b)
    except ZeroDivisionError:
        print("The Error!")


def word_constructor():
    first_word = input()
    second_word = input()
    for f_el, s_el in zip(first_word, second_word):
        print(f_el + s_el, end='')

    # print("".join([x + y for x, y in zip(input(), input())]))


def tourists():
    # work with these variables
    eugene = set(input().split())
    rose = set(input().split())

    print(eugene ^ rose)

    # Another solution 1
    # print(eugene.symmetric_difference(rose))

    # Another solution 2
    # eugene.symmetric_difference_update(rose)
    # print(eugene)

    # Another solution 3
    # rose ^= eugene
    # print(rose)

    # Another solution 4
    # print((eugene | rose) - (eugene & rose))


def main():
    # threefold()
    # length()
    # word_list()
    # tennis_tournament()
    # latin_equivalents()
    # straight_a()
    # fix_the_mistakes()
    # prime_numbers()
    # implementing_logic()
    # catching_built_in_exceptions()
    # tourists()
    word_constructor()


if __name__ == "__main__":
    main()
