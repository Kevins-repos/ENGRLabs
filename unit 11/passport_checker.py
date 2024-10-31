fileName = input('Enter the name of the file: ')
allPassports = open(fileName, 'r').readlines()
try:
    fileOut = open(file='valid_passports.txt', mode= 'x+')
except FileExistsError:
    fileOut = open(file='valid_passports.txt', mode= 'r+')
    fileOut.truncate()
index, check, count = 0, '', 0
while index < len(allPassports):
    for row in allPassports:
        if row != '\n':
            check += row
        else:
            if 'byr' in check and 'pid' in check and 'iyr' in check and 'cid' in check and 'eyr' in check and 'hcl' in check and 'ecl' in check and 'hgt' in check:
                fileOut.write(check)
                fileOut.write('\n')
                count += 1
            index += 1
            check = ''
print('There are', count, 'valid passports')