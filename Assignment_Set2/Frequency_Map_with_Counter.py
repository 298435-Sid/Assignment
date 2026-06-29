from collections import Counter

def character_frequency(text):
    text = text.lower().replace(" ", "")
    return Counter(text)

text = "Python Programming"
result = character_frequency(text)

print("Character Frequency:", result)