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
def make_numbers(puzzle:str, guess:str):
    parts = puzzle.replace('.', '').split('|')
    left = parts[0].strip().split(',')
    right= parts[1].strip().split(',')
    dividend = right[0]
    quotient = left[0]
    divisor = left[1]
    remainder = right[len(right)-1]
    return (
        make_number(dividend, guess),
        make_number(quotient, guess),
        make_number(divisor, guess),
        make_number(remainder, guess)
    )
def print_puzzle(puzzle):
    parts = puzzle.replace('.', '').split('|')
    left = parts[0].strip().split(',')
    right = parts[1].strip().split(',')
    dividend = left[0]
    quotient = right[0]
    divisor = left[1]
    print(f"             {dividend}\n         _______\n    {divisor} | {quotient}\n          {right[1].strip()}  \n          ------\n           {right[2].strip()} \n            {left[1]} \n            ----\n            {right[4].strip()}\n            {right[5].strip()}\n            ----\n             {right[6].strip()}\n")
    print(f"             {dividend}\n")
    print("         _______")
    print(f"    {divisor} | {quotient}\n")
    print(f"          {right[1].strip()}  \n")
    print("          ------\n")
    if len(right) > 3:
        print(f"           {right[2].strip()} \n")
    print(f"            {left[1]} \n")
    print("            ----")
    if len(right) > 4:
        print(f"            {right[4].strip()}")
    if len(right) > 5:
        print(f"            {right[5].strip()}")
        print("            ----\n")
    if len(right) > 6:
        print(f"             {right[6].strip()}")
    if len(right) > 7:
        print(f"             {right[7].strip()}")

def main():
    puzzle = input("Enter a word arithmetic puzzle: \n")
    print_puzzle(puzzle)
    guess = input("Enter your guess, for example ABCDEFGHIJ: ")
    valid_letters = get_valid_letters(puzzle)
    
    if not is_valid_guess(valid_letters, guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return
    
    dividend, quotient, divisor, remainder = make_numbers(puzzle, guess)
    
    if check_user_guess(dividend, quotient, divisor, remainder):
        print("Good job!")
    else:
        print("Try again!")

if __name__ == '__main__':
    main()
