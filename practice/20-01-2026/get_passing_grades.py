def get_passing_grades(grades):
    # Challenge: This crashes if the list contains a string (e.g., "Absent").
    # It should skip invalid grades and only return numbers >= 50.
    passing = []
    for g in grades:
        if isinstance(g,(float,int)) and g >= 50:
            passing.append(g)
    return passing

print(get_passing_grades([23,434,65,334,53]))