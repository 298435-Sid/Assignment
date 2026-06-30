from itertools import combinations

def power_set(nums):
    result = []
    for r in range(len(nums) + 1):
        result.extend(combinations(nums, r))
    return result

input_set = [1, 2, 3]
print(power_set(input_set))