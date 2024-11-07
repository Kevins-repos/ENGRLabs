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
try:
    file2Out = open(file='valid_passports2.txt', mode= 'x+')
except:
    file2Out = open(file='valid_passports2.txt', mode= 'r+')
    file2Out.truncate()
def validValues(validFile):
    validFile = open(validFile, 'r+')
    check, compare = '', ''
    for row in validFile:
        if row.strip():
            check += row
        else:
            compare = check.replace('\n', ' ').rstrip().split(' ')
            valid = True
            for i in range(len(compare)):
                compare[i] = compare[i].split(':')
                if compare[i][0] != 'ecl' and compare[i][0] != 'hcl':
                    if compare[i][0] == 'hgt':
                        if 'in' in compare[i][1]:
                            compare[i][1] = int(compare[i][1][:2])
                        else:
                            compare[i][1] = int(compare[i][1][:3])
                    else:
                        compare[i][1] = int(compare[i][1]) if compare[i][0] != 'pid' else compare[i][1]
                if compare[i][0] == 'pid':
                    if len(compare[i][1])!=9:
                        valid = False
                        break
                if compare[i][0] == 'cid':
                    if len(str(compare[i][1]))!=3:
                        valid = False
                        break
                if compare[i][0] == 'hcl':
                    if compare[i][1][0]!='#':
                        valid = False
                        break
                    elif len(compare[i][1][1:])!=6:
                        valid = False
                        break
                    else: 
                        for j in compare[i][1][1:]:
                            if not(j.isdigit() or j.isalpha()):
                                valid = False
                                break
                if compare[i][0] == 'ecl':
                    isMatch = False
                    for k in ['amb', 'brn', 'gry', 'grn', 'hzl', 'oth', 'blu']:
                        if k in compare[i][1]:
                            isMatch = True
                            break
                    if not isMatch:
                        valid = False
                        break
                if compare[i][0] == 'hgt':
                    if len(str(compare[i][1]))==2:
                        if not (59<=compare[i][1]<=76):
                            valid = False
                            break
                    elif not (150<=compare[i][1]<=193):
                        valid = False
                        break
                if compare[i][0] == 'eyr':
                    if not(2024<=compare[i][1]<=2034):
                        valid = False
                        break
                if compare[i][0] == 'byr':
                    if len(str(compare[i][1]))!=4:
                        valid = False
                        break
                    elif not(1920<=compare[i][1]<=2008):
                        valid = False
                        break
            if valid:
                file2Out.write(check + '\n')
            check = ''
            
    
validValues('valid_passports.txt')
fileOut.close()
file2Out.close()