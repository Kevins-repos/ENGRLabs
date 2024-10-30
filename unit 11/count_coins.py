# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   11.15 LAB: Counting coins
# Date:         29 10 2024
#comment
i, sum = 0, 0
game = open(file='game.txt', mode='r').readlines()
try:
    coins = open(file='coins.txt', mode= 'x+')
except FileExistsError:
    coins = open(file='coins.txt', mode= 'r+')
while i<len(game):
    if 'coin' in game[i]:
        sum += int(game[i].split(' ')[1])
        coins.write(game[i].split(' ')[1].replace('+', ''))
        i+=1
    elif 'jump' in game[i]:
        i += int(game[i].split(' ')[1])
    else:
        i+=1
print('Total coins collected:', sum)
coins.close()