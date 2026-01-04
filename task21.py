def count_names(names: list[str]) -> dict[str, int]:
    result = {}

    for name in names:
        result[name] = names.count(name)

    return result


names = ['Ali','Vali','Ali','gani','sami','ali']

result = count_names(names=names)

print(result)