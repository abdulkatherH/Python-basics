# FIND DUPLICATE ELEMENTS IN LIST
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
print(find_duplicates([1, 2, 2, 3, 4, 4, 5, 7, 7, 7, 9, 9]))
