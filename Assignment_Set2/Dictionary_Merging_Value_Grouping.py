def merge_dicts(d1, d2):
    result = {}

    for key, value in d1.items():
        result[key] = [value]

    for key, value in d2.items():
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]

    return result

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print(merge_dicts(d1, d2))