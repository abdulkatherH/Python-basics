# REMOVE DUPLICATES [ preserves order ]
d = [1, 7, 2, 2, 3, 5, 4, 4]
r_d = []

for i in d:
    if i not in r_d:
        r_d.append(i)
print('Using a loop: ', r_d) # OUTPUT: [1, 7, 2, 3, 5, 4]

# Using dict.fromkeys() [ preserves order ]
my_list = [1, 7, 2, 2, 3, 5, 4, 4]
unique_list = list(dict.fromkeys(my_list))
print('Using dict.fromkeys(): ', unique_list) # OUTPUT: [1, 7, 2, 3, 5, 4]