def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    group = {}
    for person in people:
        age = person['age']
        name = person['name']
        if age not in group:
            group[age] = []
        group[age].append(name)

    return group




students = [
    {'name': 'Ali', 'age': 20},
    {'name': 'Vali', 'age': 21},
    {'name': 'Soli', 'age': 20},
    {'name': 'Guli', 'age': 22},
    {'name': 'Nodir', 'age': 21}
]
group = group_by_age(people=students)
print(group)