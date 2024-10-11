# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   4.15 LAB: Make change
# Date:         5 9 2024
#obligatory comment
pay = float(input("How much did you pay? "))
cost= float(input("How much did it cost? "))
change = round(pay-cost, 2)
print(f'You received ${pay-cost:.2f} in change. That is...')
coins = 0
dimes = 0
nickels = 0
pennies = 0
coins = change//0.25
change -= coins*0.25
dimes = change//0.10
change -= dimes*0.10
nickels = change//0.05
change -= nickels*0.05
change = round(change,2)
pennies = change/0.01  
change -= pennies*0.01
if(coins>1):
    print(int(coins), "quarters")
elif(coins!=0):
    print(int(coins), "quarter")
if(dimes>1):
    print(int(dimes), "dimes")
elif(dimes!=0):
    print(int(dimes), "dime")
if(nickels>1):
    print(int(nickels), "nickels")
elif(nickels!=0):
    print(int(nickels), "nickel")
if(pennies>1):
    print(int(pennies), "pennies")
elif(pennies!=0):
    print(int(pennies), "penny")