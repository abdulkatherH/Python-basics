# Input = "a!bcd@#e"
# Output = "e!dcb@#a"
str1 = "a!bcd@#e"
print(str1[::-1])
# print(dir(str1))
# lst = []
ss = []
index = []
value = []
for i, ch in enumerate(str1):
    # print(ch.isalpha())
    if ch.isalpha() == True:
        ss.append(ch)
    elif ch.isalpha() == False:
        index.append(i)
        value.append(ch)
print(index)
print(value)
        # s = ch[::-1]
        # lst.append(s)
zz = ss[::-1]
print('reverse only alphabets: ',zz)
for i, v in zip(index, value):
    print(i, v)
    zz.insert(i, v)
print('=======> ', zz)
result = "".join(zz)
print(result)
# print(lst)