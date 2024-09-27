rows, cols = (9,9)
board = [['.']*cols]*rows
board[8][8] = 'black stone here'
for rows in board:
    print(rows)