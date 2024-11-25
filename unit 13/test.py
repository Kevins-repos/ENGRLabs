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
    for i in range(1, 16):
        board[i][8] = '□'
        board[8][i] = '□'
    return board

def showBoard(board):
    print('+ — — — — — — — — — — — — — — — — — +')
    for row in board:
        print('|', end=' ')
        for char in row:
            print(char, end=' ')
        print('|', end=' ')
        print()
    print('+ — — — — — — — — — — — — — — — — — +')

def placePlayers(players, board: list):
    placements = {'green': [(2, 2), (2, 4), (4, 2), (4, 4), 'g'],
                  'yellow': [(2, 12), (2, 14), (4, 12), (4, 14), 'y'],
                  'red': [(12, 2), (12, 4), (14, 2), (14, 4), 'r'],
                  'blue': [(12, 12), (12, 14), (14, 12), (14, 14), 'b']}
    for color in players.keys():
        for i in range(len(players[color])):
            board[placements[color][i][0]][placements[color][i][1]] = placements[color][-1]

# Define the track for each color
track = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7), (0, 8), (0, 9), 
         (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), 
         (8, 16), (9, 16), (9, 15), (9, 14), (9, 13), (9, 12), (9, 11), (9, 10), (10, 9), (11, 9), (12, 9), (13, 9), 
         (14, 9), (15, 9), (16, 9), (16, 8), (16, 7), (15, 7), (14, 7), (13, 7), (12, 7), (11, 7), (10, 7), (9, 6), 
         (9, 5), (9, 4), (9, 3), (9, 2), (9, 1), (9, 0), (8, 0), (7, 0), (7, 1)]

starting_positions = {
    'green': (7, 1),
    'yellow': (1, 9),
    'blue': (9, 15),
    'red': (15, 7)
}

# Define home lanes for each color
home_lanes = {
    'green': [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)],
    'red': [(15, 8), (14, 8), (13, 8), (12, 8), (11, 8), (10, 8), (9, 8)],
    'blue': [(8, 15), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9)],
    'yellow': [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8)]
}

# Create the board with home lanes
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
    for i in range(1, 16):
        board[i][8] = '□'
        board[8][i] = '□'
    return board

def move(dice, currentPlayer):
    global piece_positions, pieces_home, players
    color = currentPlayer
    try:
        piece = int(input(f"Which piece of {color} would you like to move (1-4)? ")) - 1
    except ValueError:
        piece = int(input(f"Enter a number between 1 to 4 inclusive!: ")) - 1
    current_pos = piece_positions[color][piece]

    try:
        if current_pos in home_lanes[color]:
            # If the piece is already in the home lane
            home_index = home_lanes[color].index(current_pos)
            steps_to_home = len(home_lanes[color]) - 1 - home_index  # Steps to home

            if dice != steps_to_home and steps_to_home != 0:
                print(f"Cannot move. You need an exact roll of {steps_to_home} to reach home.")
                return
            else:
                new_pos = home_lanes[color][home_index + dice] if home_index + dice < len(home_lanes[color]) else home_lanes[color][-1]
                pieces_home[color] += 1
                piece_positions[color][piece] = None  # Piece has reached home

                # Clear the piece from the board since it's home
                board[current_pos[0]][current_pos[1]] = '□'
                board[new_pos[0]][new_pos[1]] = pieces_home[color]
                
                # Remove the piece from the players dictionary
                print(players[color].pop(piece), 'made it home and has been removed')
                return  # No further updates for this piece
        else:
            # Regular track logic
            home_index = None
            current_index = track.index(current_pos)
            new_index = current_index + dice

            home_entry = track.index(starting_positions[color])  # Position to enter home lane

            if current_index < home_entry and new_index >= home_entry:
                # Entering the home lane
                home_move = new_index - home_entry
                if home_move < len(home_lanes[color]):
                    new_pos = home_lanes[color][home_move]
                else:
                    required_roll = len(home_lanes[color]) - home_move
                    print(f"You need an exact roll of {required_roll} to enter the home lane.")
                    return
            elif new_index >= len(track):
                # Wrapping around the track
                new_index -= len(track)
                new_pos = track[new_index]
            else:
                # Regular track movement
                new_pos = track[new_index]

        # Ensure the piece doesn't move into another player's home lane
        if new_pos in [home for home_color in home_lanes.keys() if home_color != color for home in home_lanes[home_color]]:
            print("You cannot move into another player's home lane.")
            return

        # Validate and make the move
        if is_valid_move(new_pos):
            if home_index:
                board[current_pos[0]][current_pos[1]] = '□'
            else:
                board[current_pos[0]][current_pos[1]] = '.' 
            
            # Remove the starting piece
            remove_starting_piece(color, piece)
            
            piece_positions[color][piece] = new_pos

            if board[new_pos[0]][new_pos[1]] == '.' or board[new_pos[0]][new_pos[1]] == '□':
                if board[new_pos[0]][new_pos[1]] == '□' and home_index:
                    board[new_pos[0]][new_pos[1]] = pieces_home[color]
                else:    
                    board[new_pos[0]][new_pos[1]] = color[0]  # Update board with new position
            else:
                enemy_color = get_piece_color(board[new_pos[0]][new_pos[1]])
                if enemy_color and enemy_color != color:
                    losePiece(enemy_color)  # Capture the enemy piece
                    piece_positions[color][piece] = new_pos
                    board[new_pos[0]][new_pos[1]] = color[0]
                else:
                    print("A piece is already in this position.")
        else:
            print("Invalid move.")
    except ValueError:
        print("Invalid move. The piece is not on the track.")

def is_valid_move(new_pos):
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(board) or new_pos[1] >= len(board[0]):
        return False
    return True

def losePiece(color: str):
    global players
    if color not in players:
        print("Invalid enemy piece. No piece to lose.")
        return

    if len(players[color]) > 0:
        players[color].pop()
        print(f'{color.capitalize()} player now has {len(players[color])} pieces left')

        if len(players[color]) == 0:
            print(f'{color.capitalize()} has been eliminated')
            players.pop(color)

        # Find and remove the captured piece from the board
        for i in range(len(piece_positions[color])):
            if piece_positions[color][i] not in home_lanes[color] and piece_positions[color][i] in track:
                captured_pos = piece_positions[color][i]
                piece_positions[color][i] = None
                board[captured_pos[0]][captured_pos[1]] = '.'
                break

def get_piece_color(piece):
    # Check if the board position is marked as a home lane (□)
    if piece == '□':
        return None  # Return None instead of 'home_lane'
    for color in players.keys():
        if piece.lower() == color[0]:
            return color
    return None

def remove_starting_piece(color, piece):
    global board
    starting_positions_map = {
        'red': [(12, 2), (12, 4), (14, 2), (14, 4)],
        'blue': [(12, 12), (12, 14), (14, 12), (14, 14)],
        'green': [(2, 2), (2, 4), (4, 2), (4, 4)],
        'yellow': [(2, 12), (2, 14), (4, 12), (4, 14)]
    }
    start_pos = starting_positions_map[color][piece]
    if board[start_pos[0]][start_pos[1]] == color[0]:
        board[start_pos[0]][start_pos[1]] = '.'


def main():
    global players, board, piece_positions, pieces_home
    winning = None

    players = setPlayers()
    pieces_home = players
    pieces_home = {color: 0 for color in players}
    board = createBoard()
    currentPlayer = list(players.keys())[np.random.randint(0, len(list(players.keys())))]
    
    # Initialize piece positions based on starting positions
    piece_positions = {
        color: [starting_positions[color] for _ in range(4)]
        for color in starting_positions
    }

    placePlayers(players, board)
    showBoard(board)
    
    while not winning:  # Testing loop, can be changed to a while loop for the actual game
        total_dice = 0
        while True:
            dice = np.random.randint(1, 7)
            total_dice += dice
            print(currentPlayer, 'rolled a', dice, end='! ')
            if dice != 6:
                break
            print(currentPlayer, 'goes again and rolls a', end=' ')
        
        move(total_dice, currentPlayer)
        currentPlayer = nextTurn(currentPlayer)
        if all(pos is None for pos in piece_positions[currentPlayer]) or pieces_home[currentPlayer] == 4:
            print(f"{currentPlayer.capitalize()} has won the game!")
            winning = currentPlayer
            break

        print(currentPlayer, 'its your turn now')
        showBoard(board)

if __name__ == "__main__":
    main()
