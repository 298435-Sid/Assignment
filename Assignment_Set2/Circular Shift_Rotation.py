def rotate_list(lst, n, direction):
    if not lst:
        return lst

    n = n % len(lst) 

    if direction.lower() == "right":
        return lst[-n:] + lst[:-n]
    elif direction.lower() == "left":
        return lst[n:] + lst[:n]
    else:
        raise ValueError("Direction must be 'left' or 'right'")

numbers = [1, 2, 3, 4, 5]
result = rotate_list(numbers, 2, "right")
print(result)