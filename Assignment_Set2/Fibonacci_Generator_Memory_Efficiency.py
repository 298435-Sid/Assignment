def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 8

for num in fibonacci(n):
    print(num, end=" ")