myDict = {}
months = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}
for i in range(5):
    name = input('Enter a name(leave blank for auto-name): ')
    name = name if name!='' else f'name{i}'
    myDict[f'name{i}'] = input("Birthday (Month Day): ")# 'name': 'Birth date'
for char in myDict:
    month, day = myDict[char].split()
    for monthNum, name in months.items():
        if month == name:
            month = monthNum
            break
    myDict[char] = (month, int(day))
sorted_myDict = sorted(myDict.items(), key=lambda x: (x[1][0], x[1][1]))
myDict = {name: f"{months[month]} {day}" for name, (month, day) in sorted_myDict}
print(myDict)