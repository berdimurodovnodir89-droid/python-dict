def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}
    for student in students:
        group_name = student['group'] # B
        if group_name not in group:
            group[group_name] = []
        group[group_name].append(student['name'])

    return group


{
    "B":["Ali","Vali"],
    "C":['Ali'],
}



students = [
    {
        'name':'Ali',
        'group':'B'
    },
    {
        'name':'Ali',
        'group':'C'
    },
    {
        'name':'VAli',
        'group':'B'
    },
]
group = group_students(students=students)
print(group)