# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   5.5 LAB: Boiling curve
# Date:         16 9 2024

import math
#put this in a function to use return for test cases
def heatFluxCalc(excessTemp):
    #check for non int values
    try:
        #out of bounds not inclusive so only valid values are calculated
        if(excessTemp<1.3 or excessTemp>1200):
            return 'Surface heat flux is not available'
    except TypeError:
        return 'Surface heat flux is not available'
    #set up free convection variables, minimum temp inclusive
    if excessTemp<5 and excessTemp>=1.3:
        x1, x0, y1, y0 = 5, 1.3, 7000, 1000
    #nucleate
    elif excessTemp<30 and excessTemp>=5:
        x1, x0, y1, y0 = 30, 5, 1.5*10**6, 7000
    #transition
    elif excessTemp<120 and excessTemp>=30:
        x1, x0, y1, y0 = 120, 30, 2.5*10**4, 1.5*10**6
    #film, maximum temp inclusive 
    elif excessTemp<=1200 and excessTemp>=120:
        x1, x0, y1, y0 = 1200, 120, 1.5*10**6, 2.5*10**4
    #final equation that will run after figuring out which stage the temp is at
    m = math.log10(y1/y0)/math.log10(x1/x0)
    y = y0*pow(excessTemp/x0, m)
    #returns the full print statement as doing this outside will run both
    #the outside print and inside error print statement for 1.5*10**6 < excessTemp < 1.3
    #also rounds to nearest int
    return (f'The surface heat flux is approximately {round(y)} W/m^2')
#ask for the excess temp
#excessTemp = float(input('Enter the excess temperature: '))
#call the function and print it
#print(heatFluxCalc(excessTemp))

#test cases
print(heatFluxCalc(excessTemp = 1.2))
print(heatFluxCalc(excessTemp = 1.201))
print(heatFluxCalc(excessTemp = '1'))
print(heatFluxCalc(excessTemp =       33        ))
print(heatFluxCalc(excessTemp = 1*5))
print(heatFluxCalc(excessTemp = 1.3))
print(heatFluxCalc(excessTemp = 5))
print(heatFluxCalc(excessTemp = 10))
print(heatFluxCalc(excessTemp = 30))
print(heatFluxCalc(excessTemp = 120))
print(heatFluxCalc(excessTemp = 1200))
