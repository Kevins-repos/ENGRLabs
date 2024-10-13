# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Kevin 
#               Max
#               Rebbeca
#               Miranda
# Section:      578
# Assignment:   2.8 LAB: Linear Interpolation
# Date:         27 8 2024

y2 = 23028
y1 = 2028
t2 = 55
t1 = 10
slope = (y2-y1)/(t2-t1)

#input time
t = 25

y = slope*(t-10)+2028
print("Part 1:")
print("For t = 25 minutes, the position p=", y, "kilometers")

#PART 2

t = 300

y = slope*(t-10)+2028

from math import*

max_y = 2*pi*6745



print("Part 2:")
print("For t = 300 minutes, the position p=", y%max_y, "kilometers")