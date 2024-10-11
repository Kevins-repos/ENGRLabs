# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   3.18 LAB: Still More Linear Interpolation
# Date:         3 9 2024
t1 = float(input('Enter time 1:'))
x1 = float(input('Enter the x position of the object at time 1:'))
y1 = float(input('Enter the y position of the object at time 1:'))
z1 = float(input('Enter the z position of the object at time 1:'))
t2 = float(input('Enter time 2:'))
x2 = float(input('Enter the x position of the object at time 2:'))
y2 = float(input('Enter the y position of the object at time 2:'))
z2 = float(input('Enter the z position of the object at time 2:'))
#time we want to find
t = t1#1
x = ((x2-x1)/(t2-t1))*(t - t1) + x1
y = ((y2-y1)/(t2-t1))*(t - t1) + y1
z = ((z2-z1)/(t2-t1))*(t - t1) + z1
print(f'At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')
t +=(t2-t1)/4#1.25
x = ((x2-x1)/(t2-t1))*(t - t1) + x1
y = ((y2-y1)/(t2-t1))*(t - t1) + y1
z = ((z2-z1)/(t2-t1))*(t - t1) + z1
print(f'At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')
t +=(t2-t1)/4#1.50
x = ((x2-x1)/(t2-t1))*(t - t1) + x1
y = ((y2-y1)/(t2-t1))*(t - t1) + y1
z = ((z2-z1)/(t2-t1))*(t - t1) + z1
print(f'At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')
t +=(t2-t1)/4#1.75
x = ((x2-x1)/(t2-t1))*(t - t1) + x1
y = ((y2-y1)/(t2-t1))*(t - t1) + y1
z = ((z2-z1)/(t2-t1))*(t - t1) + z1
print(f'At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')
t +=(t2-t1)/4#t=2.00
x = ((x2-x1)/(t2-t1))*(t - t1) + x1
y = ((y2-y1)/(t2-t1))*(t - t1) + y1
z = ((z2-z1)/(t2-t1))*(t - t1) + z1
print(f'At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})')