# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   4.20.1: LAB: How many gadgets
# Date:         12 9 2024

#day 2 of working on this, i have no idea how this code works anymore but it passes 
targetDay = int(input('Please enter a positive value for day: '))
day = 0
if(targetDay<0):
    print("You entered an invalid number!")
    quit()
gadgetCount = 0
rate = 10
while(day<targetDay):
    rate+=1
    day +=1
    if(day<=10 or day>50):
        rate-=1
    gadgetCount += rate
    if(day>100):
       gadgetCount -=rate
print(f'The sum total number of gadgets produced on day {targetDay} is {gadgetCount}')
