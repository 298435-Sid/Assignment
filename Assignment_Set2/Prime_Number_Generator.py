import math

def get_primes(start, end):
    primes = []

    for num in range(start, end + 1):
        if num < 2:
            continue

        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
            
        if is_prime:
            primes.append(num)

    return primes

result = get_primes(10, 50)
print("Primes:", result)