# Get max character in a string 
text = "It lacks visual styling like bold, italics, or font colors. "
result = {}
for ch in text:
    # print(ch)
    result[ch]= result.get(ch, 0) + 1
print('Get the each character with count: ',result)
ignored = {' ', '.', ','}
max_char, max_count = None, None

for char, count in result.items():
    if char in ignored:
        continue
    if max_count is None or count > max_count:
        max_char = char
        max_count = count
print("Max character:", max_char)
print("Count:", max_count)