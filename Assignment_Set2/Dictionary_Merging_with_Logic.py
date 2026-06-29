def merge_dictionaries(dict_a, dict_b):
    merged = dict_a.copy()
    for key, value in dict_b.items():
     if key in merged:
            merged[key] += value
    else:
            merged[key] = value
    return merged
dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

result = merge_dictionaries(dict_a, dict_b)
print("Merged Dictionary:", result)