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
    global players
    if len(players[color]) > 0:
        players[color].pop()
        print(f'{color.capitalize()} player now has {len(players[color])} pieces left')

        if len(players[color]) == 0:
            print(f'{color.capitalize()} has been eliminated')
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

# Define the track for each color
paths = {
    'red': [(12, 2), (11, 2), (10, 2), (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2), 
            (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4)],
    'blue': [(12, 12), (11, 12), (10, 12), (9, 12), (8, 12), (7, 12), (6, 12), (5, 12), (4, 12), (3, 12), (2, 12), 
            (2, 13), (2, 14), (3, 14), (4, 14), (5, 14), (6, 14), (7, 14), (8, 14), (9, 14), (10, 14), (11, 14), (12, 14)],
    'green': [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
              (12, 3), (12, 4), (11, 4), (10, 4), (9, 4), (8, 4), (7, 4), (6, 4), (5, 4), (4, 4), (3, 4), (2, 4)],
    'yellow': [(2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12),
               (12, 13), (12, 14), (11, 14), (10, 14), (9, 14), (8, 14), (7, 14), (6, 14), (5, 14), (4, 14), (3, 14), (2, 14)]
}

def move(dice, currentPlayer):
    global piece_positions
    color = currentPlayer
    piece = int(input(f"Which piece of {color} would you like to move (1-4)? ")) - 1
    
    current_pos = piece_positions[color][piece]
    path = paths[color]
    current_index = path.index(current_pos)
    new_index = current_index + dice
    
    if new_index >= len(path):
        print("Move exceeds the track length. Try a different piece or wait for next turn.")
        return
    
    new_pos = path[new_index]

    if is_valid_move(new_pos, color):
        board[current_pos[0]][current_pos[1]] = '.'  # Clear old position
        if board[new_pos[0]][new_pos[1]] == '.':
            piece_positions[color][piece] = new_pos  # Move to new position
            board[new_pos[0]][new_pos[1]] = color[0]  # Update board with new position
        else:
            # Check if it's an enemy piece and remove it
            enemy_color = get_piece_color(board[new_pos[0]][new_pos[1]])
            if enemy_color != color:
                if board[new_pos[0]][new_pos[1]].islower():
                    losePiece(enemy_color)
                    piece_positions[color][piece] = new_pos  # Move to new position
                    board[new_pos[0]][new_pos[1]] = color[0]  # Update board with new position
                else:
                    print("Cannot move to a protected enemy's piece")
            else:
                # It's a same-color piece
                if board[new_pos[0]][new_pos[1]].islower():
                    board[new_pos[0]][new_pos[1]] = board[new_pos[0]][new_pos[1]].upper()
                print("Your piece is now protected!")
    else:
        print("Invalid move.")

def calculate_new_position(current_pos, dice):
    # For Ludo, this function is now embedded in the move logic using paths
    pass

def is_valid_move(new_pos, color):
    # Add custom game rules for checking validity
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(board) or new_pos[1] >= len(board[0]):
        return False
    return True

def get_piece_color(piece):
    for color in players.keys():
        if piece.lower() == color[0]:
            return color
    return None

# Initialize game and board setup as before
def main():
    global players, board, piece_positions
    players = setPlayers()
    board = createBoard()
    currentPlayer = list(players.keys())[np.random.randint(0, len(list(players.keys())))]
    piece_positions = {
        'green': [(2, 2), (2, 4), (4, 2), (4, 4)],
        'yellow': [(2, 12), (2, 14), (4, 12), (4, 14)],
        'red': [(12, 2), (12, 4), (14, 2), (14, 4)],
        'blue': [(12, 12), (12, 14), (14, 12), (14, 14)]
    }
    placePlayers(players, board)
    showBoard(board)
    
    for i in range(12):  # Testing loop, can be changed to a while loop for the actual game
        dice = np.random.randint(1, 7)
        print(currentPlayer, 'rolled a', dice, end='! ')
        while dice == 6:
            print(currentPlayer, 'goes again and rolls a', end=' ')
            dice = np.random.randint(1, 7)
            print(dice)

        move(dice, currentPlayer)
        currentPlayer = nextTurn(currentPlayer)
        print(currentPlayer, 'its your turn now')
        showBoard(board)

if __name__ == "__main__":
    main()
