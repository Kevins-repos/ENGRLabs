# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   6.11.1: LAB: Pyramid area (part 1)
# Date:         19 9 2024

#side of a square
cubeLength = float(input('Enter the side length in meters: '))
#height of the pyramid
pyramidHeight = float(input('Enter the number of layers: '))
#layer count of cubes 
i = 1
sideArea = 0
while i<=pyramidHeight:
    sideArea+=i*cubeLength**2
    i+=1
#4 sides of a pyramid
sideArea*=4
j = 1
topArea = cubeLength**2
while j<pyramidHeight:
    j+=1
    #side area of a square * height of the pyramid + 1 for skipping 1st layer
    topArea += (cubeLength**2)*(pyramidHeight+1)
print(f'You need {topArea+sideArea:.2f} m^2 of gold foil to cover the pyramid')