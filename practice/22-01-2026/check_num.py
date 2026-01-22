def is_even(number):
    is_even = False
    if number % 2 == 0:
        is_even = True
    
    return is_even


print(f"Is 4 even? {is_even(4)}")  # Expected: True
print(f"Is 7 even? {is_even(7)}")