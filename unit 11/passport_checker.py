# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:       Maximus Maizus
#              Miranda Yang
#              Kevin Alcantara 
#              Rebecca Eason

# Section:     578
# Assignment:  11.9.1: LAB: Passport checker Part A
# Date:        11/6/24
#comment
fileName = input('Enter the name of the file: ')
allPassports = open(fileName, 'r').readlines()
try:
    fileOut = open(file='valid_passports.txt', mode= 'x+')
except FileExistsError:
    fileOut = open(file='valid_passports.txt', mode= 'r+')
    fileOut.truncate()
check, count = '', 0
for row in allPassports:
    if row.strip():
        check += row
    else:
        if all(fields in check for fields in ['pid', 'cid', 'hgt', 'hcl', 'eyr', 'byr', 'ecl']):
            fileOut.write(check + '\n')
            count += 1
        check = ''
if check:
    if all(fields in check for fields in ['pid', 'cid', 'hgt', 'hcl', 'eyr', 'byr', 'ecl']):
        fileOut.write(check)
        count+=1
print('There are', count, 'valid passports')