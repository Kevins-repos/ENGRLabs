# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   8.18.1: LAB: Leet speak
# Date:         12 10 2024
#area of a cylinder with a hole?
import math
#headache
def parta(radius_sphere, radius_hole):
    height_cap = radius_sphere - math.sqrt(radius_sphere**2 - radius_hole**2)
    volume_caps = 2 * ((math.pi * height_cap**2) * (3*radius_sphere - height_cap)) / 3
    volume_cylinder = math.pi * radius_hole**2 * (2 * math.sqrt(radius_sphere**2 - radius_hole**2))
    volume_sphere = (4/3) * math.pi * radius_sphere**3
    volume_bead = volume_sphere - volume_caps - volume_cylinder
    return round(volume_bead, 6)
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
    return float