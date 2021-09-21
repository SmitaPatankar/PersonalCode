board = [['_'] * 3 for i in range(3)]
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board)
# [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

# behaves like
# Each iteration builds a new row and appends it to board.

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[2][0] = 'X'
print(board)
# [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]

# wrong below

weird_board = [['_'] * 3] * 3
print(weird_board)
# [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = 'O'
print(weird_board)
# [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

# behaves like
# The same row is appended three times to board.

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
