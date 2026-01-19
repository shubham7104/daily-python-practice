def clean_username(username):
    clean_username = username.strip()
    username_lower = clean_username.lower()
    return username_lower

"""
--TEST--
print(clean_username("  JohnDoe  "))
"""
