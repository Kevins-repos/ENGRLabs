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

def removePlayer(color: str) -> None:
    if len(players[color]) > 0:
        print(f'{color} still has {len(players[color])} pieces left, failed to remove')
    else:
        players.pop(color)
        print(f'{color} has been eliminated')

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

def move(color: str, piece: str, steps: int) -> None:
    home_positions = {'red': 52, 'blue': 52, 'green': 52, 'yellow': 52}  # Simplified example
    current_position = players_positions[color].get(piece, -1)
    if current_position == -1:
        if steps == 6:
            players_positions[color][piece] = 0
            print(f'{color} player moves {piece} to start position')
        else:
            print(f'{color} player needs a 6 to move {piece} out of home')
    elif current_position != 'home':
        new_position = (current_position + steps)
        if new_position >= home_positions[color]:
            print(f'{color} player moves {piece} to home')
            players_positions[color][piece] = 'home'
        else:
            new_position %= 52
            players_positions[color][piece] = new_position
            print(f'{color} player moves {piece} to position {new_position}')
            if landedOnUnprotected(new_position, color):
                opponent_color, opponent_piece = getOpponentPieceAtPosition(new_position, color)
                losePiece(opponent_color)
                print(f'{color} captures {opponent_color}\'s {opponent_piece}')

def protected(turn) -> bool:
    protected_positions = [2, 15, 28, 39]
    for piece, position in players_positions[turn].items():
        if position in protected_positions:
            return True
    return False

def landedOnUnprotected(position, color) -> bool:
    for opponent_color, pieces in players_positions.items():
        if opponent_color != color:
            for opponent_piece, opponent_position in pieces.items():
                if position == opponent_position and not protected(opponent_color):
                    return True
    return False

def getOpponentPieceAtPosition(position, color):
    for opponent_color, pieces in players_positions.items():
        if opponent_color != color:
            for opponent_piece, opponent_position in pieces.items():
                if position == opponent_position:
                    return (opponent_color, opponent_piece)
    return (None, None)

def create_visual_board():
    board = [['  ' for _ in range(15)] for _ in range(15)]
    for i in range(4):
        board[i][0] = 'R'
        board[i][1] = 'R'
        board[i][2] = 'R'
        board[i][3] = 'R'

        board[0][i+11] = 'G'
        board[1][i+11] = 'G'
        board[2][i+11] = 'G'
        board[3][i+11] = 'G'
    
        board[i+11][0] = 'Y'
        board[i+11][1] = 'Y'
        board[i+11][2] = 'Y'
        board[i+11][3] = 'Y'
    
        board[11][i+11] = 'B'
        board[12][i+11] = 'B'
        board[13][i+11] = 'B'
        board[14][i+11] = 'B'
    
    for i in range(6, 9):
        board[7][i] = 'x'
        board[i][7] = 'x'
    
    return board

def print_visual_board(board):
    for row in board:
        print(' '.join(row))

def map_piece_to_coordinates(position):
    path = [
        (14, 0), (13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (7, 0), (6, 0), (5, 0),
        (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),
        (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (9, 10), (8, 10), (7, 10), (6, 10), 
        (5, 10), (4, 10), (3, 10), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (2, 5), (1, 5), (0, 5), 
        (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 10), (2, 10), (3, 10), (4, 10), (5, 10),
        (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (14, 9),
        # Complete the full path including home columns and special positions
    ]
    if position == 'home':
        return (7, 7)  # Simplified example position for home
    return path[position % len(path)]  # Simplified example

def update_visual_board(logic_board, visual_board):
    visual_board = create_visual_board()
    for player, pieces in logic_board.items():
        for piece, position in pieces.items():
            if position != -1:
                x, y = map_piece_to_coordinates(position)
                visual_board[x][y] = player[0].upper()
    return visual_board

def check_winner():
    for player, positions in players_positions.items():
        if all(pos == 'home' for pos in positions.values()):
            print(f'Game Over! {player} wins!')
            return True
    return False

def play_turn(turn):
    dice = np.random.randint(1, 7)
    print(f'{turn} rolls a {dice}')
    piece = input(f'Select a piece to move for {turn} (e.g., piece1, leave blank to just move a piece): ')
    if piece == '':
        movable_pieces = [p for p in players_positions[turn] if players_positions[turn][p] != 'home']
        if movable_pieces:
            piece = movable_pieces[0]
        else:
            print(f'{turn} has no movable pieces.')
            return
    move(turn, piece, dice)

def main():
    global players, players_positions
    players = setPlayers()
    players_positions = {color: {piece: -1 for piece in pieces} for color, pieces in players.items()}

    visual_board = create_visual_board()
    turn = 'red'
    while len(players) > 1:
        visual_board = update_visual_board(players_positions, visual_board)
        print_visual_board(visual_board)
        if check_winner():
            return
        play_turn(turn)
        turn = nextTurn(turn)

    print(f'Game Over! {list(players.keys())[0]} wins!')

if __name__ == "__main__":
    main()
