cells = list(input("Enter cells:"))
horizontal = [cells[i::3] for i in range(3)]
vertical = [cells[i:i + 3] for i in range(0, 9, 3)]
diagonale = [cells[::4], cells[2:7:2]]
win_o = ["O", "O", "O"] in horizontal or ["O", "O", "O"] in vertical or ["O", "O", "O"] in diagonale
win_x = ["X", "X", "X"] in horizontal or ["X", "X", "X"] in vertical or ["X", "X", "X"] in diagonale
print("---------")
print("|", *cells[:3], "|", sep=" ")
print("|", *cells[3:6], "|", sep=" ")
print("|", *cells[6:], "|", sep=" ")
print("---------")
if win_x and not win_o:
    print("X wins")
elif win_o and not win_x:
    print("O wins")
elif abs(cells.count("X") - cells.count("O")) > 1 or (win_x and win_o):
    print("Impossible")
elif not win_x and not win_o and cells.count("_") > 2:
    print("Game not finished")
else:
    print("Draw")
