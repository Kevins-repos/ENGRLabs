sex = input('Male(M) or Female(F): ')
#string type
#idk why sex!="M" is always wrong(same for F) ill just use not
if(not(sex=="M" or sex=="F")):
    print("Please enter either M or F")
    quit()
age = int(input('Age :'))
#check if age is within range
if(age>79 or age<20):
    print('Please enter an age between 20 and 79, inclusive')
    quit()
#redundancy function
def AgePointScore(age, point):
    threshold = 79
    x = 0
    while(age<=threshold):
        #decrease threshold to the lower range
        threshold-=5
        #as range lowers, points change accordingly 
        x+=1
        #last range is special since its a larger range
        if(age<=34 and age>=20):
            x-=1
    #arrays start from 0 and go to 10 even if only 9 elements
    return point[x-1]
#set up points per age range backwards as we start with oldest range first
Mpoints = [13, 12, 11, 10, 8, 6, 3, 0, -4, -9]
Fpoints = [16, 14, 12, 10, 8, 6, 3, 0, -3, -7]
#decide to use either male or female point sets
if(sex=="M"):
    print(AgePointScore(age, Mpoints))
    #quit early to avoid running female points too
    quit()
print(AgePointScore(age, Fpoints))
