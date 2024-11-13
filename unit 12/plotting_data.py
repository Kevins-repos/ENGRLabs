import matplotlib as mp
with open('unit 12/WeatherDataCLL-1.csv', 'r') as weather:
    usable = []
    for row in weather:
        usable.append(row.split(','))
    weather.close()
def date():
    month = input('Please enter a month: ')
    year = input('Please enter a year: ')
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = months.index(month)
    return year + '-' + (str(month) if month>9 else '0'+str(month))
def averageTemp():
    Date = date()
    tempSum, count = 0, 0
    for row in usable:
        if Date in row[0]:
            tempSum += float(row[2])
            count +=1
    return round(tempSum/count, 1)
def dateFrame():
    #year - month, both ints in a str
    print('Enter the start date: ')
    start = date().strip().split('-')
    print('Enter the end date: ')
    end = date().strip().split('-')
    print([range(int(start[0]), int(end[0]))].append([range(int(start[1]), int(end[1]))]))
dateFrame()