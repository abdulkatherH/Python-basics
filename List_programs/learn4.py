# COUNTING CONSTANTS IN A GIVEN WORD
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print('COUNTING CONSTANTS IN A GIVEN WORD: ', count)

# COUNTING THE NUMBER OF OCCURANCES OF A CHARACTER IN A STRING 
word = "programming"
character = 'g'
count = 0
for i in word:
    if i == character:
        count += 1
print('COUNTING THE NUMBER OF OCCURANCES OF A CHARACTER IN A STRING: ', count)