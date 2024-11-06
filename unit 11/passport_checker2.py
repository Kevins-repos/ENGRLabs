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

def validFields(file):
    check, count = '', 0
    for row in allPassports:
        if row.strip():
            check += row
        else:
            if all(fields in check for fields in ['pid', 'cid', 'hgt', 'hcl', 'eyr', 'byr', 'ecl']) and ('cm' in check or 'in' in check):
                fileOut.write(check + '\n')
                count += 1
            check = ''
    if check:
        if all(fields in check for fields in ['pid', 'cid', 'hgt', 'hcl', 'eyr', 'byr', 'ecl']) and ('cm' in check or 'in' in check):
            fileOut.write(check)
            count+=1
    return count
print('There are', validFields(allPassports), 'valid passports')

def validValues(validFile):
    validFile = open(validFile, 'r+')
    check, compare = '', ''
    for row in validFile:
        if row.strip():
            check += row
        else:
            compare = check.replace('\n', ' ').rstrip().split(' ')
            for i in range(len(compare)):
                compare[i] = compare[i].split(':')
                if compare[i][0] != 'ecl' and compare[i][0] != 'hcl':
                    if compare[i][0] == 'hgt':
                        if 'in' in compare[i][1]:
                            compare[i][1] = int(compare[i][1][:2])
                        else:
                            compare[i][1] = int(compare[i][1][:3])
                    else:
                        compare[i][1] = int(compare[i][1])
                if compare[i][0] == 'pid':
                    if len(str(compare[i][1]))!=9:
                        break
                if compare[i][0] == 'cid':
                    if len(str(compare[i][1]))!=3:
                        break
                if compare[i][0] == 'hcl':
                    if compare[i][1][0]!='#':
                        break
                    elif len(compare[i][1][1:])!=6:
                        break
                    else: 
                        for j in compare[i][1][1:]:
                            if not(j.isdigit() or j.isalpha()):
                                break
                if compare[i][0] == 'ecl':
                    if compare[i][1]!='amb'or compare[i][1]!='brn'or compare[i][1]!='gry'or compare[i][1]!='grn'or compare[i][1]!='hzl'or compare[i][1]!='oth':
                        break
                if compare[i][0] == 'hgt':
                    if len(str(compare[i][1]))==2:
                        if not (59<=compare[i][1]<=76):
                            break
                    elif not (150<=compare[i][1]<=193):
                        break
                if compare[i][0] == 'eyr':
                    if not(2024<=compare[i][1]<=2034):
                        break
                if compare[i][0] == 'byr':
                    if len(str(compare[i][1]))!=4:
                        break
                    elif not(1920<=compare[i][1]<=2008):
                        break
                print(compare[i])
            check = ''
            
    
print(validValues('valid_passports.txt'))