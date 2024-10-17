# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kevin Alcantara
# Section:      578
# Assignment:   9.19 LAB: Word puzzle
# Date:         17 10 2024
#comment
def get_valid_letters(puzzle_string: str):
    first10Unique = []
    allowed = 'qwertyuiopasdfghjklzxcvbnm'
    for i in puzzle_string:
        if i.lower() in allowed and i not in first10Unique:
            first10Unique.append(i)
    return ''.join(first10Unique[:10])   
def is_valid_guess(valid_letters: str, user_guess: str):
    valid_letters = [i for i in valid_letters]
    if len(user_guess) != 10:
        return False
    user_guess = get_valid_letters(user_guess)
    for i in range(10):
        if valid_letters[i] not in user_guess:
            return False
    return True
def check_user_guess(dividend, quotient, divisor, remainder):
    return dividend == quotient * divisor + remainder
def make_number(word, user_guess):
    myInt = ''
    if len(user_guess) == 10:
        for j in word:
            for i, char in enumerate(user_guess):
                if char == j:
                    myInt+=str(i)
    return int(myInt) if myInt != '' else None
def make_numbers(puzzle_string, guess):
    
    return 
def main():
    
    valid_letters = get_valid_letters('RUE,EAR | RUMORS,UEII ,UKTR ,EAR ,KEOS,KAIK,USA.')
    valid_guess = is_valid_guess(valid_letters, 'TAKEOURSBD')
    print(make_number('RUE', 'TAKEOURSIM'))
    
if __name__ == '__main__':
    main()