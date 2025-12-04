# Interview Questions
# -------------------
# if words is available in chars character
words = ["cat","bt","hat","tree"]
chars = "atach"
# def can_form(word, chars):
#     chars_list = list(chars)

#     for ch in word:
#         if ch in chars_list:
#             chars_list.remove(ch)
#         else:
#             return False
#     return True
# Another way
def can_form(word, chars):
    count = {}

    for c in chars:
        count[c] = count.get(c, 0) + 1

    for ch in word:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

for word in words:
    if can_form(word, chars):
        print(f"{word} is available in chars character")
    # else:
    #     print(f"Is not available in chars character")
# --------------------------------------------------------------------------------
# Python code to get the second unique (non-repeating) character
str = "atach"
counts = {}
for ch in str:
    counts[ch] = counts.get(ch, 0) + 1
    
# print(counts)
# counts.update({"s": 3})
# print("counts after update: ",counts)
# counts.pop("s")
# print("counts after removed: ",counts)
# for key in counts.keys():
#     print('key: ', key)
# for value in counts.values():
#     print('value: ', value)
# for key, value in counts.items():
#     print('item: ',key, value)
unique_chars = []
for ch in str:
    if counts[ch] == 1:
        unique_chars.append(ch)
print("Avoided : ",unique_chars)
# print(len(unique_chars))
if len(unique_chars) >= 2:
    print("Second duplicate:", unique_chars[1])
else:
    print("No second duplicate found")

#Output: 6Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# list1 = [1,4,5,6,[8,9,10],12,13]
 