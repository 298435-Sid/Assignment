import re

def word_count(text):
    
    words = re.findall(r'\b\w+\b', text.lower())

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts

text = "Python is great. Python is fast, and learning Python is fun!"

print(word_count(text))