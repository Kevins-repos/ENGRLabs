# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   6.16.1: LAB: Howdy Whoop
# Date:         20 9 2024
# Function to print the numbers with the specified conditions
def howdy_whoop(first_int, second_int):
    for i in range(1, 101):
        if i % first_int == 0 and i % second_int == 0:
            print("Howdy Whoop")
        elif i % first_int == 0:
            print("Howdy")
        elif i % second_int == 0:
            print("Whoop")
        else:
            print(i)

num1 = int(input('Enter an integer: '))
num2 = int(input('Enter another integer: '))
howdy_whoop(num1, num2)