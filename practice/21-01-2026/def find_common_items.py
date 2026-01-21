def find_common_items(list_a, list_b):
    common = []
    for a in list_a:
        for b in list_b:
            if a == b:
                common.append(a)
    return common


print(f"Common: {find_common_items([1, 2, 3, 4], [3, 4, 5, 6])}") 