def asciiTime(symbol: str, hour: int, minute: int):
    """Enter a symbol and returns a list with all ascii numbers in that symbol"""
    nums = ['***\n* *\n* *\n* *\n***', ' * \n** \n * \n * \n***', '***\n  *\n***\n*  \n***',
            '***\n  *\n***\n  *\n***', '* *\n* *\n***\n  *\n  *', '***\n*  \n***\n  *\n***', 
            '***\n*  \n***\n* *\n***', '***\n  *\n  *\n  *\n  *', '***\n* *\n***\n* *\n***',
            '***\n* *\n***\n  *\n  *']#make sure all these have the EXACT same spacing
    allowed = 'abcdeghkmnopqrsuvwxyz@$&*='
    while str(symbol) not in allowed:#handles numbers too
        symbol = input('Character not permitted! Try again: ')
    for i, char in enumerate(nums):
        nums[i] = char.replace('*', symbol)#char = nums[i], im just making sure 
    time = [nums[i] for i in [int(i) for i in str(hour)]] + [' \n:\n \n:\n '] + [nums[i] for i in [int(i) for i in str(minute)]]#split into list, turn int into ascii art, combine both lists
    for i,char in enumerate(time):#in this loop, add a 0 art if needed
        if char==' \n:\n \n:\n ':
            if len(time[i+1:])<=1:
                time.insert(i+1, nums[0])
    # Split each digit's ASCII art into lines
    lines = ['' for _ in range(5)]#create 5 lines to be printee verically
    for digit in time:#each element in time, as in, each ascii art for each number 
        digit_lines = digit.split('\n')#separate each line of the individual art, separated by \n, into a list to be printed vertically
        for i in range(5):
            lines[i] += digit_lines[i] + '  '  # start adding each number art one by one, line by line, then add some space between arts
    
    # Print each line of lines 
    for line in lines:
        print(line)

asciiTime('o', 2, 999)
