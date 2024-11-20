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

def createBoard():
    line1 = 
def main():
    global players
    players = setPlayers()

if __name__ == "__main__":
    main()
