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

# Average of Even and Odd Numbers Separately
print('--------------------- AVERAGE OF ODD EVEN -----------------')
numbers = [1,2,3,4,5,6]
even = [n for n in numbers if n % 2 == 0] 
odd = [n for n in numbers if n % 2 == 1]
print("Even: ",even)
print("Odd: ",odd)
avg_even = sum(even) / len(even)
avg_odd = sum(odd) / len(odd)

print("Average of even: ", avg_even)
print("Average of odd: ", avg_odd)

# Average Using stastics Module
print('--------------------- AVERAGE stastics -----------------')
import statistics
nums = [20,20]
print("Average statistics: ",statistics.mean(nums))

# Average of values in a Dictionary
print('--------------------- Average Dictionary -----------------')
marks = {"math": 10, "science": 10, "english": 10}
print("sum: ",sum(marks.values()))
print("len: ",len(marks))
avg = sum(marks.values()) / len(marks)
print("Average marks: ", avg)