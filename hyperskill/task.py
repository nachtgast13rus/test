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


def main():
    # threefold()
    # length()
    # word_list()
    # tennis_tournament()
    # latin_equivalents()
    # straight_a()
    # fix_the_mistakes()
    # prime_numbers()



if __name__ == "__main__":
    main()
