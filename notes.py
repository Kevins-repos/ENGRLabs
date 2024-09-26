fullName = input('What is your name? ').strip()

def firstSyllable(fullName):
    vowels = 'aeiou'
    first_vowel_index = -1
    second_vowel_index = -1
    
    for i, char in enumerate(fullName.lower()):
        if char in vowels:
            if first_vowel_index == -1:
                first_vowel_index = i
            elif second_vowel_index == -1:
                second_vowel_index = i
                break
    
    if first_vowel_index != -1 and second_vowel_index != -1:
        return fullName[first_vowel_index:second_vowel_index + 1]
    else:
        return "Not enough vowels"

print(firstSyllable(fullName))
