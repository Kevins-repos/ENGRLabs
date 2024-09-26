# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   7.19 LAB: The Name Game
# Date:         25 9 2024

fullName = input('What is your name? ').strip()

def firstSyllable(fullName):
    vowels = 'aeiou'
    strList = [i for i in fullName.lower()]
    for j in range(len(strList)):
        if strList[j] in vowels:
            return fullName[j:].lower()
    return fullName.lower()

print(f'{fullName}, {fullName}, Bo-B{firstSyllable(fullName)}\nBanana-Fana Fo-F{firstSyllable(fullName)}\nMe Mi Mo-M{firstSyllable(fullName)}\n{fullName}!')
