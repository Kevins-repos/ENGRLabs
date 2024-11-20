myList = []
myDict = {}#'name': 'Birth date'
months = {1:'January',
          2:'February',
          3:'March',
          4:'April',
          5:'May',
          6:'June',
          7:'July',
          8:'August',
          9:'September',
          10:'October',
          11:'November',
          12:'December'}
for i in range(5):
    myDict[f'name{i}'] = input("Birthday(MM/DD): ")
for char in myDict:
    myDict[char] = myDict[char].split()
    for j in range(len(months)):
        if myDict[char][0] == months[j+1]:
            myDict[char][0] = j+1
    myDict[char][1] = int(myDict[char][1])
myDict = sorted({date: name for name, date  in myDict.items()}.keys())#'Birth date': 'Name'
myDict = {name: date for name, date  in myDict.items()}
for i in range(len(myList)):
    myDict[i][0] = months[myDict[i][0]]
print(myDict)
for i, char in enumerate(myList):
    myList[i] = (char+f' u{i+1}').split()
    for j in range(len(months)):
        if myList[i][0] == months[j+1]:
            myList[i][0] = j+1
    myList[i][1] = int(myList[i][1])
myList.sort()
for i in range(len(myList)):
    myList[i][0] = months[myList[i][0]]
print(myList)