def is_legal_move(board, i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(board):
        return False
    if j >= len(board[0]):
        return False
    return True


def cannot_capture(board):
    l_attacks = ((1, -2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                continue
            for attack in l_attacks:
                new_i = i + attack[0]
                new_j = j + attack[1]
                if not is_legal_move(board, new_i, new_j):
                    continue
                if board[new_i][new_j] == 1:
                    return False
    return True


outcome = cannot_capture([
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0]
])
print(outcome)

outcome2 = cannot_capture([
  [1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 0, 1]
])
print(outcome2)
