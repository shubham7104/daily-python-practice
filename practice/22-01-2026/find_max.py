def find_max(numbers):
    """
    Question 3: The Big One
    Return the largest number in the list.
    Note: Do not use the built-in max() function! Try writing a loop.
    """
    max = 0
    for num in numbers:
        if num > max:
            max = num
    return max

print(f"Max of [10, 5, 20, 3]: {find_max([10, 5, 20, 3])}")