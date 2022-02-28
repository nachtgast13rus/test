import sys

placeholders = ["СУЩЕСТВИТЕЛЬНОЕ", "ПРИЛАГАТЕЛЬНОЕ", "ГЛАГОЛ"]


def save_laught_text(filename, text):
    file = open(filename, 'w', encoding="utf-8")
    file.write(text)
    file.close()


def make_laught_text(filename):
    try:
        file = open(filename, 'r', encoding="utf-8")
        my_text = ''
        for line in file:
            my_text += process_line(line)
        file.close()
        return my_text
    except FileExistsError:
        print("Не удалось найти файл" + filename)
    except IsADirectoryError:
        print("Файл" + filename + " является каталогом")
    except:
        print("Не удалось открыть файл")


def process_line(line):
    global placeholders
    processed_line = ''
    words = line.split()
    for word in words:
        stripped = word.strip('.,;:!?')
        if stripped in placeholders:
            answer = input("Введите " + stripped + ": ")
            processed_line += answer + ' '
            if word[-1] in '.,;:!?':
                processed_line += word[-1] + ' '
            else:
                processed_line += ' '
        else:
            processed_line += word + ' '
    return processed_line + '\n'


def main():
    if len(sys.argv) != 2:
        print("game_laught.txt <filename>")
    else:
        filename = sys.argv[1]
        text = make_laught_text(filename)
        if text is not None:
            save_laught_text("crazy" + filename, text)


if __name__ == '__main__':
    main()
