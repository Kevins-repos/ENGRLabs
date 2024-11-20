import numpy as np

def gameHelp() -> None:
    print(open('unit 13/game_rules.txt', 'r').read())

def setPlayers() -> dict:
    players_pieces = {'red': [], 'blue': [], 'green': [], 'yellow': []}
    while True:
        try:
            playerCount = int(input('How many players are playing (2-4): '))
            if 2 <= playerCount <= 4:
                colors = ['red', 'blue', 'green', 'yellow']
                for i in range(playerCount):
                    players_pieces[colors[i]] = [f'piece{j}' for j in range(1, 5)]
                return {color: pieces for color, pieces in players_pieces.items() if pieces}
            else:
                print('Only 2-4 players can play at a time. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number between 2 and 4.')

def losePiece(color: str) -> None:
    if len(players[color]) > 0:
        players[color].pop()
        print(f'{color} player now has {len(players[color])} pieces left')

        if len(players[color]) == 0:
            print(f'{color} has been eliminated')
            players.pop(color)

def nextTurn(current_turn) -> str:
    colors = list(players.keys())
    idx = (colors.index(current_turn) + 1) % len(colors)
    return colors[idx]

def createBoard():
    
    line3 = ['O', '.', 'O', '.', 'O', '.', 'O', '.', '.', '.', 'O', '.', 'O', '.', 'O', '.', 'O']
    line1 = ['O', 'O', 'O', 'O', 'O', 'O', 'O', '.', '.', '.', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
    line2 = ['O', '.', '.', '.', '.', '.', 'O', '.', '.', '.', 'O', '.', '.', '.', '.', '.', 'O']
    line4 = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    board = []
    board.append(line1.copy())
    board.append(line2.copy())
    board.append(line3.copy())
    board.append(line2.copy())
    board.append(line3.copy())
    board.append(line2.copy())
    board.append(line1.copy())
    board.append(line4.copy())
    board.append(line4.copy())
    board.append(line4.copy())
    board.append(line1.copy())
    board.append(line2.copy())
    board.append(line3.copy())
    board.append(line2.copy())
    board.append(line3.copy())
    board.append(line2.copy())
    board.append(line1.copy())
    return board

def showBoard(board):
    print('O - - - - - - - - - - - - - - - - - O')
    for row in board:
        print('|', end=' ')
        for char in row:
            print(char, end=' ')
        print('|', end=' ')
        print()
    print('O - - - - - - - - - - - - - - - - - O')

def placePlayers(players, board: list):
    placements = {'green': [(2, 2), (2, 4), (4, 2), (4, 4), 'g'],
                  'yellow': [(2, 12), (2, 14), (4, 12), (4, 14), 'y'],
                  'red': [(12, 2), (12, 4), (14, 2), (14, 4), 'r'],
                  'blue': [(12, 12), (12, 14), (14, 12), (14, 14), 'b']}
    for color in players.keys():
        for i in range(len(players[color])):
            board[placements[color][i][0]][placements[color][i][1]] = placements[color][-1]

def move(dice, currentPlayer):
    pass

def main():
    global players
    winner = None
    players = setPlayers()
    board = createBoard()
    currentPlayer = list(players.keys())[np.random.randint(0,len(list(players.keys())))]
    placePlayers(players, board)
    showBoard(board)
    for i in range(12):#testing, will turn this into a while not winner when game movement works
        dice = np.random.randint(1, 7)
        print(currentPlayer, 'rolled a', dice, end='! ')
        while dice == 6:
            print(currentPlayer, 'goes again and rolls a', end=' ')
            dice = np.random.randint(1, 7)
            print(dice)

        currentPlayer = nextTurn(currentPlayer)
        print(currentPlayer, 'its your turn now')
        showBoard(board)

if __name__ == "__main__":
    main()
