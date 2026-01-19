def is_valid_email(email):
    is_valid = False
    for char in email:
        if "@" in email and "." in email:
            is_valid = True
    return is_valid

'''test
print(is_valid_email("user@google.com")) # True
print(is_valid_email("hello_world"))     # False

'''