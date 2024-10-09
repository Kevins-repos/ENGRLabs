board = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
         [1, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [2, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [3, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [4, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [5, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [6, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [7, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [8, '.', '.', '.', '.', '.', '.', '.', '.', '.' ],
         [9, '.', '.', '.', '.', '.', '.', '.', '.', '.' ]]
turn = 1

run = True

while run:
    if turn==1:
        for row in board:
            for spot in row:
                print(spot, end=' ')
            print()
    if turn%2==1:
        print('Black\'s turn')
    else:
        print('White\'s turn')
    print('Input the row and column you want to place the piece, separated by a comma: ')
    user = input('Enter stop to end game: ').split(',')

    if user[0]=='stop':
        print('Game ended')
        run = False
        continue
    user = [int(i) for i in user]

    if turn%2==1:
        token = chr(9675)
    else:
        token = chr(9679)
    
    row = user[0]
    col = user[1]
    if board[row][col] == '.':
        board[row][col] = token
    else:
        print('Please enter a location without a token')
        continue

    turn += 1

    for row in board:
        for spot in row:
            print(spot, end= ' ')
        print()