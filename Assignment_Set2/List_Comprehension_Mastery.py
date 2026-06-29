words = ["apple", "bat", "cherry", "dog", "elderberry"]
result = [word.upper() for word in words if len(word) >= 4]
print(result)