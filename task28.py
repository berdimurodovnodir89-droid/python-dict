def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for text in words:
        max_len = len(text)
        if max_len not in result:
            result[max_len] = []
        result[max_len].append(text)
    return result



words = ["python", "code", "list", "a", "dict", "longer", "word"]


print(group_by_length(words=words))