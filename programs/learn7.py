# remove duplicates in a list
my_list = [7, 6, 6, 1, 2, 2, 3, 4, 4, 5]
empty_list = []
for item in my_list:
    if item not in empty_list:
        empty_list.append(item)
print('ONLY UNIQUE: ', empty_list)
#--------------------------------

# get only duplicates
lst = [7, 6, 6, 1, 2, 2, 3, 4, 5, 4]
seen = set()
# dups = []
# for x in lst:
#     if x in seen and x not in dups:
#         dups.append(x)
#     seen.add(x)
# print('ONLY DUPLICATES: ', dups)
# print('seen: ', seen)
#---------------------------------

# duplicates = [x for x in lst if x in seen or seen.add(x)]
# print('ONLY DUPLICATES: ', duplicates)

#---------------------------------
duplicate = {x for x in lst if x in seen or seen.add(x)}
print('ONLY DUPLICATE: ', duplicate)
