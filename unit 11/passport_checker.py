
def placeAndSortInList(file):
    eachPassport = ['']
    passData = ''
    index = 0
    validCount = 0
    for row in file:
        if row.replace('\n', '') != '':
            passData += row
        else:
            eachPassport[index] = passData.replace('\n', ' ').split(' ')
            eachPassport[index].sort()
            eachPassport[index][0] = 'valid' if len(eachPassport[index])==9 else 'invalid'
            if eachPassport[index][0] == 'valid':
                validCount+=1
            passData = ''
            index+=1
            eachPassport.append('')
    return eachPassport, validCount
fileName = input('Enter the name of the file: ')
allPassports = open(fileName, 'r')
try:
    fileOut = open(file='valid_passports.txt', mode= 'x+')
except FileExistsError:
    fileOut = open(file='valid_passports.txt', mode= 'r+')
    fileOut.truncate()
results = placeAndSortInList(allPassports)
for i in results[0]:
    if 'valid' in i:
        fileOut.write(' '.join(i[1:]))
        fileOut.write('\n')
print('There are', results[1], 'valid passports')
allPassports.close(), fileOut.close()