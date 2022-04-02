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


def main():
    threefold()
    length()
    word_list()


if __name__ == "__main__":
    main()
