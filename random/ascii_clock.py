def asciiTime(hour: int, minute: int, symbol: str):
    
    """Enter the symbol, hour, and minute numbers and prints the ascii art of them with the symbol\n
    Doesnt handle leaving any of the 3 variables empty so dont, this return a list that when printed\n
    line by line, shows the art, i did this so that there would be a way to add AM or PM to the end\n
    meaning that you will have to write AM line by line top to bottom and append it to this fucntion"""
    nums = ['000\n0 0\n0 0\n0 0\n000', ' 1 \n11 \n 1 \n 1 \n111', '222\n  2\n222\n2  \n222',
            '333\n  3\n333\n  3\n333', '4 4\n4 4\n444\n  4\n  4', '555\n5  \n555\n  5\n555', 
            '666\n6  \n666\n6 6\n666', '777\n  7\n  7\n  7\n  7', '888\n8 8\n888\n8 8\n888',
            '999\n9 9\n999\n  9\n999']#make sure all these have the EXACT same spacing
    allowed = 'abcdeghkmnopqrsuvwxyz@$&*='
    while str(symbol) not in allowed:#handles numbers too
        symbol = input('Character not permitted! Try again: ')
    if symbol.strip()!='':
        for i, char in enumerate(nums):
            nums[i] = char.replace(str(i), symbol)#char = nums[i], im just making sure 
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

AmPm = [' A  M   M\nA A MM MM\nAAA M M M\nA A M   M\nA A M   M',
        'PPP M   M\nP P MM MM\nPPP M M M\nP   M   M\nP   M   M']
time = [int(i) for i in input('Enter the time: ').strip().split(':')]
typeIs12 = True if int(input('Choose the clock type (12 or 24): '))==12 else False
symbol = input('Enter your preferred character: ')
if time[0]>=12 and typeIs12==True:
    day, time[0]= AmPm[1].split('\n'),  time[0]-12
    asciiArt = asciiTime(time[0], time[1], symbol) 
    for i,char in enumerate(day):
        asciiArt[i]+=char
        print(asciiArt[i])
elif typeIs12==True:
    day = AmPm[0].split('\n')
    asciiArt = asciiTime(time[0], time[1], symbol) 
    for i,char in enumerate(day):
        asciiArt[i]+=char
        print(asciiArt[i])
else:
    asciiArt = asciiTime(time[0], time[1], symbol) 
    for i in asciiArt:
        print(i)

