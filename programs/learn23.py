def flatern_dict(nested_dict, parent_key='', separator='~'):
    items = []

    for key, value in nested_dict.items():
        new_key = f"{parent_key} {separator} {key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatern_dict(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

dictV = {
    'a': 1,
    'b': {'b1': 2, 'b2': {'b21': 3, 'b22': 4}},
    'c': 5
}
flatened_dict = flatern_dict(dictV)
print(flatened_dict)
print('--------------------------------------------------------------------')

def flatten(data, parent_key='', sep='.'):
    flat = {}

    if isinstance(data, dict):
        items = data.items()
    elif isinstance(data, list):
        items = enumerate(data)
    else:
        raise TypeError('Input must be dict ot list')
    
    for key, value in items:
        # print(key)
        new_key = f"{parent_key} {sep} {key}" if parent_key else key
        print('new_key: ', new_key)
        if isinstance(value, (dict, list)):
            flat.update(flatten(value, new_key, sep))
        else:
            flat[new_key] = value
    return flat


nested = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": [10, 20, {"g": 30}]
        }
    }
}

print(flatten(nested))

print('------------------------------------------------------------------')
def unflatten(data, sep="."):
    result = {}

    for compound_key, value in data.items():
        keys = compound_key.split(sep)
        current = result

        for i, key in enumerate(keys):
            # list index?
            if key.isdigit():
                key = int(key)

            # last key → set value
            if i == len(keys) - 1:
                if isinstance(key, int):  # ensure list
                    while not isinstance(current, list):
                        current = []
                    while len(current) <= key:
                        current.append(None)
                    current[key] = value
                else:
                    current[key] = value
            else:
                next_key = keys[i + 1]
                is_next_index = next_key.isdigit()

                if isinstance(key, int):
                    while len(current) <= key:
                        current.append([] if is_next_index else {})
                    if not isinstance(current[key], (dict, list)):
                        current[key] = [] if is_next_index else {}
                    current = current[key]
                else:
                    if key not in current:
                        current[key] = [] if is_next_index else {}
                    current = current[key]

    return result
nested = {
    "a": 1,
    "b": {
        "c": 2,
        "d": {
            "e": 3,
            "f": [10, 20, {"g": 30}]
        }
    }
}

print(unflatten(nested))