sex = input('Male(M) or Female(F): ')
if(not(sex=="M" or sex=="F")):
    print("Please enter either M or F")
    quit()
age = int(input('Age :'))
if(age>79 or age<20):
    print('Please enter an age between 20 and 79, inclusive')
    quit()
def AgePointScore(age, point):
    threshold = 79
    x = 0
    while(age<=threshold):
        threshold-=5
        x+=1
        if(age<=34 and age>=20):
            x-=1
    return point[x-1]
Mpoints = [13, 12, 11, 10, 8, 6, 3, 0, -4, -9]
Fpoints = [16, 14, 12, 10, 8, 6, 3, 0, -3, -7]
if(sex=="M"):
    print(AgePointScore(age, Mpoints))
    quit()
print(AgePointScore(age, Fpoints))
