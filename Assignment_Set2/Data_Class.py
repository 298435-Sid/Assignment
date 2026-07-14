from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

b1 = Book("1984", "George Orwell", 328)

print(b1)