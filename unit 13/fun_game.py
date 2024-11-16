import numpy as np
import tkinter as tk
#import keyboard
def gameHelp():
    print(open('unit 13/game_rules.txt', 'r').read())
players_pieces = {'red':None, 'blue':None, 'green':None, 'yellow':None}
def setPlayers():
    while True:
        try:
            playerCount = int(input('How many players are playing (2-4): '))
            if 2 <= playerCount <= 4:
                colors = ['red', 'blue', 'green', 'yellow']
                for i in range(playerCount):
                    players_pieces[colors[i]] = [f'piece{j}' for j in range(1, 5)]
                return players_pieces
            else:
                print('Only 2-4 players can play at a time. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a number between 2 and 4.')
setPlayers()