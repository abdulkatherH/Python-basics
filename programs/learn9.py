# Implementing variable length arguments in python
def average(*t):
    print('sum: ',sum(t))
    print('length: ',len(t))
    avg = sum(t) / len(t)
    return avg
result1 = average(32,5,3)
result2 = average(5,10)

print('AVERAGE 1: ',result1)
print('AVERAGE 2: ',result2)