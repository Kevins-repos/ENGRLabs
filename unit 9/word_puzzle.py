# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   9.19 LAB: Word puzzle
# Date:         17 10 2024
#comment
def getVariables(puzzleStr:str) -> tuple:
    dividend = puzzleStr.split("| ")[1].split(",")[0]
    quotient = puzzleStr.split(",")[0]
    divisor = puzzleStr.split(",")[1].split(" | ")[0]
    remainder = puzzleStr.split(",")[-1]
    return (dividend,quotient,divisor,remainder)


def get_valid_letters(puzzle: str) -> str:
    removeCharactersPuzzle = "".join("".join("".join(puzzle.split("|")).split(",")).split(" "))
    retList = []
    for letter in removeCharactersPuzzle:
        if letter not in retList:
            retList.append(letter)
    ret = "".join(retList)
    return ret




def is_valid_guess(uniqueLetters,guess):
    allGuessLettersInUniqueLetters = True
    if len(guess) != 10: return False
    usedList = []
    for letter in uniqueLetters: 
        usedList.append(False)
    for letter in guess:
        if letter not in uniqueLetters:
            return False
        elif usedList[uniqueLetters.index(letter)]:
            return False
        else:
            usedList[uniqueLetters.index(letter)] = True
    return True



def check_user_guess(dividend, quotient, divisor, remainder):
    return dividend == (quotient * divisor) + remainder

def make_number(str1,guess):
    unSortedNumList = []
    for letter in str1:
        unSortedNumList.append(str(guess.index(letter)))
    return int("".join(unSortedNumList))

def make_numbers(puzzleStr, guess):
    (dividend, quotient, divisor, remainder) = getVariables(puzzleStr)
    uniqueLetters = get_valid_letters(puzzleStr)
    dividendNumber = make_number(dividend,guess)
    quotientNumber = make_number(quotient,guess)
    divisorNumber = make_number(divisor,guess)
    remainderNumber = make_number(remainder,guess)
    return (dividendNumber, quotientNumber, divisorNumber, remainderNumber)





def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    #puzzle = "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)


    #guess = "TAKEOURSIM"
    guess = input("\nEnter your guess, for example ABCDEFGHIJ: ")
    uniqueLetters = get_valid_letters(puzzle)
    if not is_valid_guess(uniqueLetters,guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    else:
        (dividendNumber, quotientNumber, divisorNumber, remainderNumber) = make_numbers(puzzle,guess)
        if check_user_guess(dividendNumber, quotientNumber, divisorNumber, remainderNumber):
            print("Good job!")
        else:
            print("Try again!")

if __name__ == '__main__':
    main()
