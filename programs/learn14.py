# s = "racecar"
# t = "carracD"

# def is_anagram(s, t):
#     if len(s) != len(t):
#         return False

#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1
#     print('freq: ', freq)

#     for ch in t:
#         if ch not in freq:
#             return False
#         freq[ch] -= 1
#         if freq[ch] == 0:
#             del freq[ch]
#     return len(freq) == 0

# print(is_anagram(s, t))

s = "racecar"
# count = [0] * 26

# for ch in s:
#     count[ord(ch) - ord('a')] += 1
# print(count)
# sorted_string = ""
# for i in range(26):
#     sorted_string += chr(i + ord('a')) * count[i]

# print(sorted_string)

chars = list(s)
print('chars: ',chars)
n = len(chars)
print('n: ',n)
for i in range(n):
    for j in range(0, n - i - 1):
        if chars[j] > chars[j + 1]:
            chars[j], chars[j + 1] = chars[j + 1], chars[j]

sorted_string = "".join(chars)
print(sorted_string)