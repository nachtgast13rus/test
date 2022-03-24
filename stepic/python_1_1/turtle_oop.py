class Turtle:
    def __init__(self):
        self.east = 0
        self.nord = 0

    def to_nord(self, distance):
        self.nord += distance

    def to_south(self, distance):
        self.nord -= distance

    def to_west(self, distance):
        self.east -= distance

    def to_east(self, distance):
        self.east += distance

    def current_coord(self):
        print(self.east, self.nord)


turtle = Turtle()
coord = []
for i in range(int(input())):
    coord += [[string for string in input().split()]]
for elem in coord:
    if elem[0] == "север":
        turtle.to_nord(distance=int(elem[1]))
    elif elem[0] == "юг":
        turtle.to_south(distance=int(elem[1]))
    elif elem[0] == "запад":
        turtle.to_west(distance=int(elem[1]))
    elif elem[0] == "восток":
        turtle.to_east(distance=int(elem[1]))
turtle.current_coord()

# x, y = 0, 0
# moves = {
#     'север': lambda d: (x, y + d),
#     'юг': lambda d: (x, y - d),
#     'запад': lambda d: (x - d, y),
#     'восток': lambda d: (x + d, y)
# }
#
# n = int(input())
# for _ in range(n):
#     direction, step = input().split()
#     x, y = moves[direction](int(step))
#
# print(x, y)
