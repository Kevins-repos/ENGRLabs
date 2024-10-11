# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   7.19 LAB: The Name Game
# Date:         25 9 2024

#man, if i knew all i had to return was the letters after the first vowel, this would have been so much easier 
fullName = input('What is your name? ').strip()
def firstSyllable(fullName):
    vowels = 'aeiou'
    strList = []
    for i in fullName.lower():
        strList.append(i)
    j = 0
    while j<len(strList):
        if strList[j] in vowels:
            k = j+1
            while k<len(strList):
                if strList[k] in vowels:
#                   return fullName[j:k+1]
                    return fullName[j:].lower()
                k+=1
            return fullName[j:].lower()
        j+=1
    return fullName.lower()
print(f'{fullName}, {fullName}, Bo-B{firstSyllable(fullName)}\nBanana-Fana Fo-F{firstSyllable(fullName)}\nMe Mi Mo-M{firstSyllable(fullName)}\n{fullName}!')