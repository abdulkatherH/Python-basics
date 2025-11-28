# Implementing variable length arguments in python
print('--------------------- Tuple -----------------')
def average(*t):
    print('sum: ',sum(t))
    print('length: ',len(t))
    avg = sum(t) / len(t)
    return avg
result1 = average(32,5,3)
result2 = average(5,10)

print('AVERAGE 1: ',result1)
print('AVERAGE 2: ',result2)

# Average of numbers in a list
print('--------------------- List -----------------')
def average_list(numbers):
    return sum(numbers) / len(numbers)

nums = [10,20,30,40]
print("AVERAGE IN A LIST: ", average_list(nums))

# Average using user Input
print('--------------------- USER INPUT -----------------')
count = int(input("How many numbers? "))
numbers = []
for i in range(count):
    num = float(input("Enter the Number: "))
    numbers.append(num)

avg = sum(numbers) / count
print("Average: ",avg)