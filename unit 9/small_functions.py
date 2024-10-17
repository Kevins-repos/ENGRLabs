# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   8.18.1: LAB: Leet speak
# Date:         12 10 2024
import math
def parta(sphere_radius: float, cylinder_radius: float):
    sphere_volume = 4/3*math.pi*sphere_radius**3
    cylinder_volume=math.pi*cylinder_radius**2*(2*sphere_radius)
    return sphere_volume-cylinder_volume
#n = 4, 2 + 2 = 4; n= 9, 2+2+2+2+2, 3+3+3;
def partb(n:int):
    out = []
    for i in range(2, n):
        for j in range(2, n):
            print(f'{i} * {j} = {i*j}')
            if i*j>n:
                break
            if i*j==n:
                out.append(i)
                return out*j
    return False
def partc(symbol: str, name: str, company: str, email: str):
    businessCard = symbol*26
    name = symbol+name.center(len(businessCard)-2)+symbol
    company = symbol+company.center(len(businessCard)-2)+symbol
    email = symbol+email.center(len(businessCard)-2)+symbol
    return (f'{businessCard}\n{name}\n{company}\n{email}\n{businessCard}')
def partd(numList: list):
    numList.sort()
    return numList[0], numList[(len(numList))//2] if len(numList)%2!=0 else (numList[len(numList)//2-1]+numList[len(numList)//2])/2,  numList[len(numList)-1]
def parte(times: list, distances: list):
    velocities = [0]*(len(times)-1)
    for index, time in enumerate(times):
        velocities[index-1] = (distances[index]-distances[index-1])/(times[index]-times[index-1])
    return velocities
def partf(numList: list):
    for char, i in enumerate(numList):
        for character, j in enumerate(numList):
            print(i,j)
            if char!=character and i+j==2028:
                return i*j
    return False