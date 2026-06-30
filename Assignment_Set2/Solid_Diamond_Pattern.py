def print_diamond(size):
    
    for i in range(1, size + 1):
        spaces = size - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(size - 1, 0, -1):
        spaces = size - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

print_diamond(4)