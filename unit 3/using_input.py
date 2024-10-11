# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   3.19 LAB: Using input
# Date:         5 9 2024
#comment
import math
print('This program calculates the Reynolds number given velocity, length, and viscosity\n')
velocity = float(input('Please enter the velocity (m/s): \n'))
length  = float(input('Please enter the length (m): \n'))
viscosity = float(input('Please enter the viscosity (m^2/s): \n'))
print(f'Reynolds number is {round(velocity*length/viscosity)}\n')

print('This program calculates the wavelength given distance and angle\n')
distance = float(input('Please enter the distance (nm): \n'))
angle = math.radians(float(input('Please enter the angle (degrees): \n')))
print(f'Wavelength is {2*distance*math.sin(angle):.4f} nm\n')

print('\nThis program calculates the production rate given time, initial rate, and decline rate\n')
time = float(input('Please enter the time (days): \n'))
initial_rate = float(input('Please enter the initial rate (barrels/day): \n'))
decline_rate = float(input('Please enter the decline rate (1/day): \n'))
b = 0.8
print(f'Production rate is {initial_rate/pow(1+b*decline_rate*time, 1/b):.2f} barrels/day\n')

print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity\n')
initial_mass = float(input('Please enter the initial mass (kg): \n'))
final_mass = float(input('Please enter the final mass (kg): \n'))
exhaust_velocity = float(input('Please enter the exhaust velocity (m/s): \n'))
print(f'Change of velocity is {exhaust_velocity*math.log(initial_mass/final_mass):.1f} m/s')