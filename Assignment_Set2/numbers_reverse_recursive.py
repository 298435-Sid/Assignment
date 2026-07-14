def reverse_number(n):
    if n == 0:
        return
    print(n % 10, end="")
    reverse_number(n // 10)

num = int(input("Enter a number: "))
print("Reversed number:", end=" ")
reverse_number(num)
