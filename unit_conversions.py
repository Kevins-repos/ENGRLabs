# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   3.17 LAB: Unit Conversions
# Date:         3 9 2024
#start converting
x = float(input("Please enter the quantity to beconverted:"))

newtons = x*4.4482216153
print(f'{x:.2f} pounds force is equivalent to {newtons:.2f} newtons')

feet = x*3.28084
print(f'{x:.2f} meters is equivalent to {feet:.2f} feet')

kilopascals = x*101.325
print(f'{x:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals')

BTU = x*3.412141623
print(f'{x:.2f} watts is equivalent to {BTU:.2f} BTU per hour')

gallons = (x*60)/3.78541
print(f'{x:.2f} liters per second is equivalent to {gallons:.2f} US gallons per minute')

fahren = (x*9/5)+32
print(f'{x:.2f} degrees Celsius is equivalent to {fahren:.2f} degrees Fahrenheit')