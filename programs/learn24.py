# Nested List to flattern List
def flattern(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flattern(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
print('Flattern List: ', flattern(nested_list))
# -----------------------------------------------
# Nested Tuple to flattern Tuple

def flattern_tuple(nested_tuple):
    flat = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            flat.extend(flattern_tuple(item))
        else:
            flat.append(item)
    return tuple(flat)

nested_tuple = (1, (2, (3, 4), 5), 6, (7, 8))
print('Flattern Tuple: ', flattern_tuple(nested_tuple))