# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   2.10 LAB: More Linear Interpolation
# Date:         6 9 2024

#comment
num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))
num3 = float(input('Enter number 3: '))
maxNum = num1
if(maxNum<num2):
    maxNum=num2
if(maxNum<num3):
    maxNum=num3
print('The largest number is', maxNum)