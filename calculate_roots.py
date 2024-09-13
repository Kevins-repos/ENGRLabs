# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   4.21 LAB: Calculate roots
# Date:         13 9 2024
import math
a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))
#fancy try-except method cause I just learned what it does and how to use it
try:
    p1 = -b/(2*a)
    p2 = math.sqrt(b**2-4*a*c)/(2*a)
    if(p1-p2 == p1+p2):
        print(f'The root is x = {p1-p2}')
    else:
        print(f'The roots are x = {p1+p2} and x = {p1-p2}')
except ZeroDivisionError:
    print('You entered an invalid combination of coefficients!')