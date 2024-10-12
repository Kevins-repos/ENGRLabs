def asciiTime(hour: int, minute: int, symbol: str):
    """Enter the hour, minute, and symbol and prints the ascii art of them with the symbol\n
    To print the art, use a for loop to print every element. i did this so that there would be a way to add AM or PM to the end\n
    meaning that you will have to write AM line by line top to bottom and add it to each line printed for the list\n
    If you need help, I have the answer"""
    nums = ['000\n0 0\n0 0\n0 0\n000', ' 1 \n11 \n 1 \n 1 \n111', '222\n  2\n222\n2  \n222',
            '333\n  3\n333\n  3\n333', '4 4\n4 4\n444\n  4\n  4', '555\n5  \n555\n  5\n555', 
            '666\n6  \n666\n6 6\n666', '777\n  7\n  7\n  7\n  7', '888\n8 8\n888\n8 8\n888',
            '999\n9 9\n999\n  9\n999']
    allowed = 'abcdeghkmnopqrsuvwxyz@$&*='
    while str(symbol) not in allowed:
        symbol = input('Character not permitted! Try again: ')
    if symbol.strip()!='':
        for i, char in enumerate(nums):
            nums[i] = char.replace(str(i), symbol)
    time = [nums[i] for i in [int(i) for i in str(hour)]] + [' \n:\n \n:\n '] + [nums[i] for i in [int(i) for i in str(minute)]]
    for i,char in enumerate(time):
        if char==' \n:\n \n:\n ':
            if len(time[i+1:])<=1:
                time.insert(i+1, nums[0])
    lines = ['' for i in range(5)]
    for digit in time:
        digit_lines = digit.split('\n')
        for i in range(5):
            lines[i] += digit_lines[i] + ' '
    return [line for line in lines]