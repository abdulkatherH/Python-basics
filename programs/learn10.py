# Sort a list without using sort()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
print('SORTING THE NUMBERS: ',bubble_sort([5,2,8,1,9]))

# Getting frequency of each number
def frequency(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq
print('FREQUENCY OF EACH NUMBERS: ', frequency([1,2,3,3,4,4,4,4,4,5,5]))