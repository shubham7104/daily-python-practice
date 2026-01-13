def get_active_users(users_list):
    names = []
    for user in users_list:
        if user["is_active"] == True:
            names.append(user["name"])

    return names

users_db = [
    {"name": "Alice", "age": 25, "is_active": True},
    {"name": "Bob",   "age": 30, "is_active": False},
    {"name": "Charlie","age": 22, "is_active": True}
]
print(get_active_users(users_db))