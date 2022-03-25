import itertools


def input_to_list():
    '''
    Печатает список считаных строк(в данном случае 3)
    :return: None
    '''
    print(*[input() for _ in range(3)], sep='\n')


def lists_to_list():
    """
    Объединяет список списков в один список
    :return: None
    """
    lists = [[1, 2, 3], [4, 5, 6]]
    lists = list(itertools.chain(*lists))
    print(lists)


def main():
    # input_to_list()
    lists_to_list()


if __name__ == "__main__":
    main()
