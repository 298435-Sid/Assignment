def remove_duplicates(lst):
    result = []
    
    for item in lst:
        if item not in result:
            result.append(item)
    
    return result

numbers = [1, 2, 2, 3, 1, 4, 2]
print(remove_duplicates(numbers))