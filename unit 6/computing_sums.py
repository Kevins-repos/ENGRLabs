# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   6.17 LAB: Computing sums
# Date:         20 9 2024

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))
sum = 0
#add i from num1 inclusive until num2 inclusive
for i in range(num1, num2+1):
    sum+=i
print(f"The sum of all integers from {num1} to {num2} is {sum}")