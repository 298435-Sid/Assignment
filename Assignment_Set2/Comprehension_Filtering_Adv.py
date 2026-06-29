words = ["apple", "education", "ice", "ocean", "python", "umbrella"]

result = [word for word in words if len(word) > 5 and word.lower().startswith(('a', 'e', 'i', 'o', 'u'))]

print(result)