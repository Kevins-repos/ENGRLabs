def acsiiNums(symbol: str):
    """Enter a symbol and returns a list with all acsii numbers in that symbol"""
    nums = ['***\n* *\n* *\n* *\n***\n', ' * \n** \n * \n * \n***\n', '***\n  *\n***\n*\n***\n',
            '***\n  *\n***\n  *\n***\n', '* *\n* *\n***\n  *\n  *\n', '***\n*\n***\n  *\n***\n', 
            '***\n*\n***\n* *\n***\n', '***\n  *\n  *\n  *\n  *\n', '***\n* *\n***\n* *\n***\n',
            '***\n* *\n***\n  *\n  *\n']
    allowed = 'abcdeghkmnopqrsuvwxyz@$&*='
    while -1==allowed.find(str(symbol)):
        symbol = input('Character not permitted! Try again: ')
    for i, char in enumerate(nums):#Minutes[i]=char
        nums[i] = char.replace('*', symbol)
    return nums