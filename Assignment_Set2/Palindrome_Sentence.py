import re

def is_palindrome(sentence):
    
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()

    return cleaned == cleaned[::-1]

text = "A man, a plan, a canal: Panama"
print(is_palindrome(text))