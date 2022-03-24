class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.draws = 0
        self.loses = 0
        self.scores = 0

    def add_win(self):
        self.wins += 1
        self.scores += 3

    def add_lose(self):
        self.loses += 1

    def add_draw(self):
        self.draws += 1
        self.scores += 1


table = {}
for i in range(int(input())):
    c1, sc1, c2, sc2 = input().split(';')
    for command in (c1, c2):
        if command not in table:
            table.update({command: Team(command)})
    if sc1 > sc2:
        table[c1].add_win()
        table[c2].add_lose()
    elif sc2 > sc1:
        table[c2].add_win()
        table[c1].add_lose()
    else:
        table[c1].add_draw()
        table[c2].add_draw()

for c in table.values():
    print(f'{c.name}:', c.wins + c.draws + c.loses, c.wins, c.draws, c.loses, c.scores)