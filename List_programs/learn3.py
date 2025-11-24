# CONVERTING AN INTEGER INTO DECIMALS
import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

# CONVERTING AND STRING OF INTEGERS INTO DECIMALS
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

# REVERSING A STRING USING AN EXTENDED SLICING TECHNIQUE
string = "Python Programming"
print(string[::-1])

# COUNTING VOWELS IN A GIVEN WORD
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)
