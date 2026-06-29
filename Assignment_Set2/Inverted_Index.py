def invert_author_books(author_books):
    result = {}

    for author, books in author_books.items():
        for book in books:
            result[book] = author

    return result

data = {
    "Orwell": ["1984", "Animal Farm"],
    "Huxley": ["Brave New World"]
}

print(invert_author_books(data))