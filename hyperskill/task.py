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


def main():
    threefold()
    length()


if __name__ == "__main__":
    main()
