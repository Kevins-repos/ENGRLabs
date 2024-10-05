def kaprekars_constant(num):
    if 0 < num < 9999:
        while num != 6174:
            ascending, descending = sort_nums(num)
            num = descending - ascending
            print(f"Next number: {num}")

def sort_nums(num):
    nums = [int(i) for i in str(num)]
    while len(nums) < 4:
        nums.append(0)
    nums.sort()
    ascending = int("".join(map(str, nums)))
    nums.sort(reverse=True)
    descending = int("".join(map(str, nums)))
    print(ascending, descending)
    return ascending, descending

num = int(input('Enter a four-digit integer: '))
kaprekars_constant(num)
