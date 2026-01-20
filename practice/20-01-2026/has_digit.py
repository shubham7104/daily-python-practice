def has_digit(text):
    # Challenge: This loops through every character even after it finds a number.
    # Optimize this to stop as soon as it finds a digit.
    found = False
    for char in text:
        if char .isdigit():
            found = True
    return found


print(has_digit("password123"))