# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   8.18.1: LAB: Leet speak
# Date:         12 10 2024
#comment
import math
def parta(sphere_radius: float, cylinder_radius: float):
    sphere_volume = 4/3*math.pi*sphere_radius**3
    cylinder_volume=math.pi*cylinder_radius**2*(2*sphere_radius)
    return sphere_volume-cylinder_volume
#n = 4, 2 + 2 = 4; n= 9, 2+2+2+2+2, 3+3+3;
def partb(n:int):
    out = []
    for i in range(2, n+2):
        print(n**(1/i))
        if n**(1/i)%1==0:
            out.append(i)
    return out*out[0] if out != [] else False
print(partb(6))