# Question-1
# Need out put like this
# 1 
# 3 3 
# 2 2 2
# 5 5 5 5
# 4 4 4 4 4

# Question-2
# without using numbers print 1 to 100

# Question-3
# pattern = [1, [2, 3], 4, 5]
# Flatern this list without using forloop

# Question-4
# Second duplicate number in list
numberList = [12, 3, 55, 23, 6, 78, 33, 4]
max1 = numberList[0]
max2 = numberList[0]
print('max1: ',max1)
print('max2: ',max2)
for num in numberList:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print("Second maximum number:", max2)