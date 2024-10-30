# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   11.16 LAB: Pixel painter
# Date:         29 10 2024
#comment
fileName, char = input('Enter the filename: '), input('Enter a character: ')
file = open(file=fileName, mode='r')
blank, line = True, ['']
for i, row in enumerate(file):
    for num in row.split(','):
        line[i] += (' '*int(num) if blank == True else char*int(num))
        blank = not blank
    line.append('')
    blank = True
try:
    fileOut = open(fileName.split('.')[0]+'.txt','x+')
except FileExistsError:
    fileOut = open(fileName.split('.')[0]+'.txt','r+')
for i in line:
    if i == '':
        continue
    fileOut.write(i+'\n')
print(fileName.split('.')[0]+'.txt', 'created!')
fileOut.close, file.close()