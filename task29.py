def get_active_users(users: list[dict[str, bool | str | int]]) -> list[str]:
    active_users = []
    
    for user in users:
        if user['active'] == True:
            if 'name' in user:
                active_users.append(str(user['name']))
            elif 'id' in user:
                active_users.append(str(user['id']))
    
    return active_users

users = [
    {"id": 1, "active": True},
    {"id": 2, "active": True},
    {"id": 3, "active": False},
]

print(get_active_users(users=users))