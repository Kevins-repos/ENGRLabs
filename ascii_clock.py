nums = ['***\n* *\n* *\n* *\n***\n', ' * \n** \n * \n * \n***\n', '***\n  *\n***\n*\n***\n',
        '***\n  *\n***\n  *\n***\n', '* *\n* *\n***\n  *\n  *\n', '***\n*\n***\n  *\n***\n', 
        '***\n*\n***\n* *\n***\n', '***\n  *\n  *\n  *\n  *\n', '***\n* *\n***\n* *\n***\n',
        '***\n* *\n***\n  *\n  *\n']
symbol = input('Input:')
for i in nums:
    for j in i:
        if j!=symbol:
            j = nums
