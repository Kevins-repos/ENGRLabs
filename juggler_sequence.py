# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   6.19 LAB: Juggler sequence
# Date:         20 9 2024

#start
n = int(input('Enter a positive integer: '))
print(f'The Juggler sequence starting at {n} is: ')
k = 0
count = 0
while k!=1:
    count+=1
    if n%2==0:
        k-=n**(1/2)//1
    else:
        k+=n**(3/2)//1
    print(k)
print(f'It took {count} iterations to reach 1')