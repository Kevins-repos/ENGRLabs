# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   LAB: Topic 7 (team)
# Date:         26 9 2024

#colors :)
begin = '\x1b[1m'
end = '\x1b[39m\x1b[22m'
red = '\x1b[31m'
blue = '\x1b[34m'
green = '\x1b[32m'

row = ['.', '.', '.', '.', '.', '.', '.', '.', '.']#set up row that will be copied for every column
board = [row.copy() for i in row]#set up row copies and make the board
p1Turn = True#player 1 goes first, white dot
gameEnd = False#ensure the game has a future
moves = 0#ensure the games future isnt short
#all of these functions are made because without them the code will be all the way to the right side becauss of all the loops
def isSurrounded(board, x, y, player):#piece location and who it belongs to, still not 100% sure how this works but it does so good job everyone
    opponent = chr(9675) if player == chr(9679) else chr(9679)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]#set up possible directions to check, up down left right respectively
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 9 and 0 <= ny < 9 and board[nx][ny] != opponent:#check if the direction is within the board and if any piece around is friendly
            return False#there was a friendly piece around or surround check wasnt within boundary
    return True

def removeSurroundedPieces(board, player):
    for i in range(9):
        for j in range(9):
            if board[i][j] == player and isSurrounded(board, i, j, player):#go through each piece and check if its surrounded
                board[i][j] = '.'#surrounded so revert to empty 

def placeRock(board, location, p1Turn):
    if board[location[0]][location[1]] == '.':
        if p1Turn:
            board[location[0]][location[1]] = chr(9675)#Black circle
        else:
            board[location[0]][location[1]] = chr(9679)#White circle
        removeSurroundedPieces(board, chr(9675) if p1Turn else chr(9679))
        p1Turn = not p1Turn#Toggle the turn and print whos turn
        print(f'{'Black' if p1Turn else 'White'}\'s turn')  # Print whose turn it is
        return p1Turn
    print(begin + red + 'Spot taken, go again.' + end)
    return p1Turn#If the spot is taken, the turn doesn't change

def printBoard(board):
    print('  1 2 3 4 5 6 7 8 9')#Print column numbers
    for i in range(9):
        print(f'{i+1} ', end='')#Print row numbers
        for j in range(9):
            print(f'{board[i][j]} ', end='')
        print()

while not gameEnd and moves <81:
    printBoard(board)
    try:
        location = [int(i)-1 for i in input('Enter where you would put the stone as a list. Ex: "1 9" for row 1 column 9: ').strip().split()]#clear spaces,split into array,turn into correct location
    except ValueError:#Was meant to handle 'quit' but instead handles anything not numbers
        print(begin + blue + 'Ended early' + end)
        break
    try:
        p1Turn = placeRock(board, location, p1Turn)
    except IndexError:
        print(begin + red + 'Please keep the rock WITHIN the board' + end)
        continue
    moves += 1
    white_count = sum(row.count(chr(9675)) for row in board)
    black_count = sum(row.count(chr(9679)) for row in board)
    if moves == 81:#Board is full if no pieces were taken, still end here cause nobody would actually play a full session here
        gameEnd = True#end the game and check who won
        if white_count > black_count or black_count == 0:
            print(begin + green + 'White wins!' + end)
        elif black_count > white_count or white_count == 0:
            print(begin + green + 'Black wins!' + end)
        else:
            print(begin + blue + 'It\'s a tie!' + end)

print(begin + red + 'Game Over!' + end)