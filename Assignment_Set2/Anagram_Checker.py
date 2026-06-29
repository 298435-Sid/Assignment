def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = "listen"
word2 = "silent"

result = is_anagram(word1, word2)
print(f'Is "{word1}" an anagram of "{word2}"? {result}')