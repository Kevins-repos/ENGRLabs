game = open(file='unit 11/game.txt', mode='r')
try:
    coin = open(file='unit 11/coins.txt', mode= 'x+')
except FileExistsError:
    coin = open(file='unit 11/coins.txt', mode= 'r+')
sum = 0
for row in game:
    text = row.split(' ')
    if 'coin' in text[0]:
        coin.write(text[1])
        if '+' in text[1]:
            sum += int(text[1].replace('+', ''))
        else:
            sum -= int(text[1].replace('-', ''))
print('Total coins collected:', sum)
game.close(), coin.close()