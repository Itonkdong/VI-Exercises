def get_indexes(position):
    if position == 1:
        return 0, 0
    elif position == 2:
        return 0, 1
    elif position == 3:
        return 0, 2
    elif position == 4:
        return 1, 0
    elif position == 5:
        return 1, 1
    elif position == 6:
        return 1, 2
    elif position == 7:
        return 2, 0
    elif position == 8:
        return 2, 1
    elif position == 9:
        return 2, 2


def tic_tac_toe(game):
    winnable_positions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    for combination in winnable_positions:
        position1 = get_indexes(combination[0])
        position2 = get_indexes(combination[1])
        position3 = get_indexes(combination[2])

        if game[position1[0]][position1[1]] == game[position2[0]][position2[1]] == game[position3[0]][position3[1]]:
            return game[position1[0]][position1[1]]

    return "Draw"


outcome = tic_tac_toe([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
])
print(outcome)
outcome2 = tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
])
print(outcome2)
outcome3 = tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
])
print(outcome3)
