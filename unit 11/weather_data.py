# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   11.17 LAB: Weather data
# Date:         29 10 2024
#comment
weather = open('unit 11/WeatherDataCLL-1.csv', 'r')
usable, maxTemp, minTemp = [], 0, 100
for row in weather:
    usable.append(row.split(','))
for row in usable:
    if row[5] != 'Maximum Temperature (F)' and row[5] != '':
        if float(row[5])>maxTemp:
            maxTemp = float(row[5])
for row in usable:
    if row[6] != 'Minimum Temperature (F)' and row[6] != '':
        if float(row[6])<minTemp:
            minTemp = float(row[6])
print(f'10-year maximum temperature: {round(maxTemp)} F')
print(f'10-year minimum temperature: {round(minTemp)} F\n')
month = input('Please enter a month: ')
year = input('Please enter a year: ')
print(f'For {month} {year}:')
months = ['', 'January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = months.index(month)
date = year + '-' + (str(month) if month>9 else '0'+str(month))

dewSum, count = 0, 0
for row in usable:
    if date in row[0]:
        dewSum += float(row[1])
        count += 1
print(round(dewSum/count, 1), 'F')

tempSum, count = 0, 0
for row in usable:
    if date in row[0]:
        tempSum += float(row[2])
        count +=1
print(round(tempSum/count, 1), 'F')

humiditySum, count = 0, 0
for row in usable:
    if date in row[0]:
        humiditySum += float(row[3])
        count +=1
print(round(humiditySum/count, 1), '%')

windSum, count = 0, 0
for row in usable:
    if date in row[0]:
        windSum += float(row[4])
        count +=1
print(round(windSum/count, 2), 'mph')

total, hasPre = 0, 0
for row in usable:
    if date in row[0]:
        total += 1
        if float(row[7]) != 0:
            hasPre += 1
print(round(hasPre/total*100, 1), '%')