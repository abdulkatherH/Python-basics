def flatern_dict(nested_dict, parent_key='', separator='_'):
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