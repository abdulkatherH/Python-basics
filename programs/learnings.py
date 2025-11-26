# SUM OF ALL ELEMENTS IN A LIST
def sample1():
    numbers = [10, 20, 30, 40]
    print('SUM OF ELEMENTS: ', sum(numbers))
sample1()

# FIND MAXIMUM AND MINIMUM IN A LIST
def sample2():
    nums = [12, 3,45, 7, 19]
    print('MAXIMUM: ',max(nums))
    print('MINIMUM: ', min(nums))
sample2()

# REMOVE DUPLICATES IN A LIST
def sample3():
    nums = [1, 2, 2, 3, 4, 4, 5]
    unique = list(set(nums))
    print('REMOVE DUPLICATES: ',unique)

# FIND EVEN NUMBERS
def sample4():
    nums = [1, 2, 3, 4, 5, 6]
    even = [n for n in nums if n % 2 == 0]
    # odd = [m for m in nums if m % 2 ! == 0]
    print('EVEN NUMBERS: ',even)
    # print('ODD NUMBERS: ',odd)
sample4()

# FIND ODD NUMBERS
def sample5():
    nums = [1, 2, 3, 4, 5, 6]
    odd = [n for n in nums if n%2!=0]
    print('ODD NUMBERS: ',odd)
sample5()

# REVERSE A LIST WITHOUT USING reverse()
def sample6():
    nums = [1, 2, 3, 4, 5, 6]
    rev = nums[::-1]
    print('REVERSE LIST: ',rev)
sample6()