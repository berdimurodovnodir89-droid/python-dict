def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}
    for idx , num in enumerate(numbers,start = 1):
        if num not in group:
            group[num] = []
        group[num].append(idx)

    return group



num = [1, 2, 3 ,4, 5, 6 ,3, 2, 1 ,4 , 5, 6, 7, 7]
num = group_indices(numbers=num)

print(num)




