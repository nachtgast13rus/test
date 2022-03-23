def create_list():
    with open('dataset1.txt', 'r', encoding='utf-8') as file_input, open('dataset1_output.txt', 'w',
                                                                         encoding='utf-8') as file_output:
        mat = fis = rus = count = 0
        for line in file_input:
            string = line.rstrip().split(';')
            del string[0]
            for i, j in enumerate(string):
                string[i] = int(j)
            mat += string[0]
            fis += string[1]
            rus += string[2]
            count += 1
            aver = (string[0] + string[1] + string[2]) / 3
            file_output.write(str(aver) + '\n')
            print(string, aver)
        mat /= count
        fis /= count
        rus /= count
        file_output.write(str(mat) + ' ' + str(fis) + ' ' + str(rus))


def main():
    create_list()


if __name__ == '__main__':
    main()
