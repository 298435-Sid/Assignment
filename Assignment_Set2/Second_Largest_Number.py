import sys

def second_largest(numbers):
    unique_nums = sorted(set(numbers), reverse=True)

    if len(unique_nums) < 2:
        return "No second largest number exists."

    return unique_nums[1]

nums = list(map(int, sys.argv[1].split(',')))

print(second_largest(nums))