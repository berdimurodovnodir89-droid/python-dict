def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}
    
    for key, value in d.items():
        if value != 0:
            result[key] = value
    
    return result

test_dict = {"a": 0, "b": 5, "c": -2, "d": 0, "e": 3}
print(filter_non_zero(test_dict)) 