# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   4.21 LAB: Calculate roots
# Date:         13 9 2024
#too much math
import math
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

if a == 0 and b == 0:
    print("You entered an invalid combination of coefficients!")
    quit()

if a == 0:
    p1 = -c / b
    print(f"The root is x = {p1}")
    quit()

p2 = b**2 - 4*a*c
if p2 > 0:
    x1 = (-b + math.sqrt(p2)) / (2*a)
    x2 = (-b - math.sqrt(p2)) / (2*a)
    print(f"The roots are x = {x1} and x = {x2}")
elif p2 == 0:
    p1 = -b / (2*a)
    print(f"The root is x = {p1}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-p2) / (2*a)
    print(f"The roots are x = {real_part} + {imaginary_part}i and x = {real_part} - {imaginary_part}i")
