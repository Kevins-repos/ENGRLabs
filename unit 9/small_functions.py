# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   8.18.1: LAB: Leet speak
# Date:         12 10 2024
import math
#area of a cylinder with a hole?
import math

import math

import math

def parta(sphere_radius: float, cylinder_radius: float) -> float:
    R = sphere_radius
    r = cylinder_radius
    h = math.sqrt(R**2 - r**2)
    
    # Volume of the sphere
    volume_sphere = (4 / 3) * math.pi * R**3
    
    # Volume of the cylindrical hole
    volume_cylinder = math.pi * r**2 * (2 * h)
    
    # Volume of the spherical caps
    volume_caps = (2 / 3) * math.pi * h**2 * (3 * R - h)
    
    # Volume of the bead: subtract the cylinder and add the caps
    volume_bead = volume_sphere - volume_cylinder + volume_caps
    
    return volume_bead

# Example usage
R = 1  # sphere radius
r = 0.25  # cylinder radius
print(parta(R, r))

# Example function and bounds
def f(x):
    return x  
#had to restart this because of misunderstanding
def partb(n:int):
    even = [i for i in range(2, n, 2)]
    for i, char in enumerate(even):
        for j in range(len(even)):
            if sum(even[i:j])==n:
                return even[i:j] 
    return False
#i forgot why i need the numbers but it works so its fine
def partc(symbol: str, name: str, company: str, email: str):
    largest_string = name if len(name)>len(company) and len(name)>len(email) else company if len(company)>len(email) else email
    businessCard = symbol*(len(largest_string)+6)
    name = symbol+name.center(len(businessCard)-2)+symbol
    company = symbol+company.center(len(businessCard)-2)+symbol
    email = symbol+email.center(len(businessCard)-2)+symbol
    return (f'{businessCard}\n{name}\n{company}\n{email}\n{businessCard}')
#why make the code readable if no ones gonna read it
def partd(numList: list):
    numList.sort()
    return numList[0], numList[(len(numList))//2] if len(numList)%2!=0 else (numList[len(numList)//2-1]+numList[len(numList)//2])/2,  numList[len(numList)-1]
#delta distance/delta time
def parte(times: list, distances: list):
    velocities = [0]*(len(times)-1)
    for index, time in enumerate(times):
        velocities[index-1] = (distances[index]-distances[index-1])/(times[index]-times[index-1])
    return velocities
#enumerate^2
def partf(numList: list):
    for char, i in enumerate(numList):
        for character, j in enumerate(numList):
            if char!=character and i+j==2028:
                return i*j
    return False
#part g cause this is enough code
def partg(x, tol):
    return False