def asciiTime(symbol: str, hour: int, minute: int):
    """Enter the symbol, hour, and minute numbers and prints the ascii art of them with the symbol\n
    Doesnt handle leaving any of the 3 variables empty so dont, this return a list that when printed\n
    line by line, shows the art, i did this so that there would be a way to add AM or PM to the end\n
    meaning that you will have to write AM line by line top to bottom and append it to this fucntion\n
    If you need help i know what to do"""
    nums = ['***\n* *\n* *\n* *\n***', ' * \n** \n * \n * \n***', '***\n  *\n***\n*  \n***',
            '***\n  *\n***\n  *\n***', '* *\n* *\n***\n  *\n  *', '***\n*  \n***\n  *\n***', 
            '***\n*  \n***\n* *\n***', '***\n  *\n  *\n  *\n  *', '***\n* *\n***\n* *\n***',
            '***\n* *\n***\n  *\n  *']
    allowed = 'abcdeghkmnopqrsuvwxyz@$&*='
    while str(symbol) not in allowed:
        symbol = input('Character not permitted! Try again: ')
    for i, char in enumerate(nums):
        nums[i] = char.replace('*', symbol)
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