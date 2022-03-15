def create_matrix():
    new_list = []
    while True:
        my_list = [i for i in input().split()]
        if "end" in my_list:
            break
        else:
            new_list.append(list(map(int, my_list)))
    return new_list


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def change_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and j == 0:
                matrix[i][j] = matrix[i][j + 1] + matrix[i][j - 1] + matrix[i + 1][j] + matrix[i - 1][j]
            if i == 0 and j == len(matrix[i]) - 1:
                matrix[i][j] = matrix[i][j - 1] + matrix[i + 1][j] + matrix[i][j - j] + matrix[i - 1][j]
#TODO сделать чтобы мвссив не менялся при расчете


def main():
    my_matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]  # create_matrix()
    change_matrix(my_matrix)
    print_matrix(my_matrix)


if __name__ == "__main__":
    main()