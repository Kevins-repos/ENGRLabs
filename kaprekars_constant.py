# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   7.21 LAB: Kaprekar's constant
# Date:         5 10 2024
num = int(input('Enter a four-digit integer: '))
tempnumcauseiforgottoaccountforit = num
def kaprekasConts(num):
    if 0<num<9999:
        count = 0
        print(f'{tempnumcauseiforgottoaccountforit} > ',end='')
        while num!=6174:
            accending, decending = sortNums(num)
            num = decending - accending
            count +=1
            if num!=6174:
                if num ==0:
                    print(f'0\n{tempnumcauseiforgottoaccountforit} reaches 0 via Kaprekar\'s routine in {count} iterations')
                    return 
                print(f'{num}', end= ' > ')
            else:
                print(f'{num}')
        print(f'{tempnumcauseiforgottoaccountforit} reaches 6174 via Kaprekar\'s routine in {count} iterations')
def sortNums(num):
    nums = [int(i) for i in str(num)]#turn num to a str and put each into a list while turning each str back to int
    while len(nums)!=4:
        if len(nums)>4:
            break
        nums.append(0)
    nums.sort()#doesnt work if num starts with 0 as a str because tYpEErRoR
    accending = int(''.join(map(str, nums)))#turn everyint in the list into a str and join them back into a int and let python handle the 0 instead
    nums.sort(reverse=True)
    decending = int(''.join(map(str, nums)))
    return accending, decending
kaprekasConts(num)