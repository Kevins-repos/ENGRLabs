# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   2.10 LAB: More Linear Interpolation
# Date:         2 9 2024

#At time 12 seconds, observed position was (8, 6, 7) meters
#At time 85 seconds, observed position was (-5, 30, 9) meters
#You want to find the position at time 30 seconds
t1 = 12
t2 = 85
x1 = 8
x2 = -5
y1 = 6
y2 = 30
z1 = 7
z2 = 9
t = 30.0
x = ((x2-x1)/(t2-t1))*(t - 12) + 8
y = ((y2-y1)/(t2-t1))*(t - 12) + 6
z = ((z2-z1)/(t2-t1))*(t - 12) + 7
print("At time",t,"seconds:\nx1 =",x,"m\ny1 =",y,"m\nz1 =",z,"m\n-----------------------")
t+=7.5
x = ((x2-x1)/(t2-t1))*(t - 12) + 8
y = ((y2-y1)/(t2-t1))*(t - 12) + 6
z = ((z2-z1)/(t2-t1))*(t - 12) + 7
print("At time",t,"seconds:\nx2 =",x,"m\ny2 =",y,"m\nz2 =",z,"m\n-----------------------")
t+=7.5
x = ((x2-x1)/(t2-t1))*(t - 12) + 8
y = ((y2-y1)/(t2-t1))*(t - 12) + 6
z = ((z2-z1)/(t2-t1))*(t - 12) + 7
print("At time",t,"seconds:\nx3 =",x,"m\ny3 =",y,"m\nz3 =",z,"m\n-----------------------")
t+=7.5
x = ((x2-x1)/(t2-t1))*(t - 12) + 8
y = ((y2-y1)/(t2-t1))*(t - 12) + 6
z = ((z2-z1)/(t2-t1))*(t - 12) + 7
print("At time",t,"seconds:\nx4 =",x,"m\ny4 =",y,"m\nz4 =",z,"m\n-----------------------")
t+=7.5
x = ((x2-x1)/(t2-t1))*(t - 12) + 8
y = ((y2-y1)/(t2-t1))*(t - 12) + 6
z = ((z2-z1)/(t2-t1))*(t - 12) + 7
print("At time",t,"seconds:\nx5 =",x,"m\ny5 =",y,"m\nz5 =",z,"m")
#this could be reduced to like 28 lines but this idk pyton