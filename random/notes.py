def asciiTime(symbol: str, hour: int, minute: int):
    """Enter the symbol, hour, and minute numbers and prints the ascii art of them with the symbol\n
    Doesnt handle leaving any of the 3 variables empty so dont, this return a list that when printed\n
    line by line, shows the art, i did this so that there would be a way to add AM or PM to the end\n
    meaning that you will have to write AM line by line top to bottom and append it to this fucntion"""
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
    lines = ['' for i in range(5)]#create 5 lines to be printee verically
    for digit in time:#each element in time, as in, each ascii art for each number 
        digit_lines = digit.split('\n')#separate each line of the individual art, separated by \n, into a list to be printed vertically
        for i in range(5):
            lines[i] += digit_lines[i] + ' '  # start adding each number art one by one, line by line, then add some space between arts
    
    #Return a list containing the art but in lines 
    return [line for line in lines]

AmPm = ['  A  M   M\n A A MM MM\n AAA M M M\n A A M   M\n A A M   M',
        ' PPP M   M\n P P MM MM\n PPP M M M\n P   M   M\n P   M   M']
hour = 11
minute = 60
asciiArt = asciiTime('o', hour, minute)
day = AmPm[0].split('\n') if hour<12 else AmPm[1].split('\n')
for k,char in enumerate(day):
    asciiArt[k]+=(char)
    print(asciiArt[k])