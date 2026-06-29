def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

text = "Python is awesome"

result = reverse_words(text)

print(result)