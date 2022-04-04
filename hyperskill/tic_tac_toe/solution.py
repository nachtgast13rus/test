def print_greed():
    print("---------")
    print("|", *cells[0], "|")
    print("|", *cells[1], "|")
    print("|", *cells[2], "|")
    print("---------")


def user_input():
    while True:
        x, y = input("Enter the coordinates: ").split()
        if (x or y) not in "1234567890":
            print("You should enter numbers!")
            continue
        x = int(x) - 1
        y = int(y) - 1
        if (x < 0 or x > 2) or (y < 0 or y > 2):
            print("Coordinates should be from 1 to 3!")
            continue
        if cells[x][y] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            cells[x][y] = "X"
            break


cells = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
horizontal = [[cells[0][0], cells[0][1], cells[0][2]],
              [cells[1][0], cells[1][1], cells[1][2]],
              [cells[2][0], cells[2][1], cells[2][2]]]
vertical = [[cells[0][0], cells[1][0], cells[2][0]],
            [cells[0][1], cells[1][1], cells[2][1]],
            [cells[0][2], cells[1][2], cells[2][2]]]
diagonal = [[cells[0][0], cells[1][1], cells[2][2]],
            cells[2][0], cells[1][1], cells[0][2]]
while True:
    print_greed()
    user_input()
