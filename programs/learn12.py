from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        print('sorted_word: ',sorted_word)
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

words = ['tea', 'eat', 'ate', 'listen', 'silent', 'rat', 'tar', 'art']
result = group_anagrams(words)
print('result: ',result)