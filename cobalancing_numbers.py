# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   6.20 LAB: Co-balancing numbers
# Date:         25 9 2024

import math
#start
n = int(input('Enter a value for n: '))
r = 1
leftTotal = 0
rightTotal =0
for i in range(n+1):
    leftTotal +=i
while(leftTotal != rightTotal):
    rightTotal =0
    for j in range(n+1, n+r+1):
        rightTotal+=j
    r+=1
    if rightTotal > leftTotal:
        break
if leftTotal == rightTotal:
    print(f'{n} is a co-balancing number with r={r-1}')
else:
    print(f'{n} is not a co-balancing number')