def king_move():
    x1, y1, x2, y2 = [int(input()) for _ in range(4)]
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        print("YES")
    else:
        print("NO")


def bishop_move():
    x1, y1, x2, y2 = [int(input()) for _ in range(4)]
    if abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")


def knight_move():
    x1, y1, x2, y2 = [int(input()) for _ in range(4)]
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        print("YES")
    else:
        print("NO")


def queen_move():
    x1, y1, x2, y2 = [int(input()) for _ in range(4)]
    if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
        print("YES")
    else:
        print("NO")


def rook_move():
    first_column = int(input())
    first_row = int(input())
    second_column = int(input())
    second_row = int(input())
    first_condition = first_row == second_row
    second_condition = first_column == second_column
    print("YES" if first_condition or second_condition else "NO")


def calculate_the_triangle_inequality():
    a, b, c = [int(input()) for _ in range(3)]
    first_condition = a + b > c
    second_condition = a + c > b
    third_condition = c + b > a
    print("YES" if first_condition and second_condition and third_condition else "NO")


def calculate_leap_year():
    year = int(input())
    first_condition = year % 4 == 0 and year % 100 != 0
    second_condition = year % 400 == 0
    print("YES" if first_condition or second_condition else "NO")


def main():
    pass


if __name__ == "__main__":
    main()
