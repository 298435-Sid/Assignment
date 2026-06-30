class PowerOfTwo:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_exponent:
            raise StopIteration

        value = 2 ** self.current
        self.current += 1
        return value

powers = PowerOfTwo(3)

for power in powers:
    print(power)