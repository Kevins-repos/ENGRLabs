def asciiTime(symbol: str, hour: int, minute: int):
    """Enter a symbol and returns a list with all ascii numbers in that symbol"""
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
    lines = ['' for _ in range(5)]
    for digit in time:
        digit_lines = digit.split('\n')
        for i in range(5):
            lines[i] += digit_lines[i] + '  '
    for line in lines:
        print(line)