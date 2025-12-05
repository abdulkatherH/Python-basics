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
print('----------------------------------------------------')
# -----------------------------------------------------------
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
print('----------------------------------------------------')
# -----------------------------------------------------------
# Nested Flattern in dict

def Flattern(data, parrent_key='', sep='~'):
    items = []
    for key, value in data.items():
        new_key = f"{parrent_key} {sep} {key}" if parrent_key else key
        if isinstance(value, dict):
            items.extend(Flattern(value, new_key, sep).items())
        else:
            items.append((new_key, value))
    return dict(items)

input = {
    'a': 1,
    'b': {'b1': 2, 'b2': {'b21': 3, 'b22': 4}},
    'c': 5
}
print('Flattern Dict: ',Flattern(input))