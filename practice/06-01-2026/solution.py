def exercise_easy_find_max():
    numbers = [14, 2, 9, 25, 6, 18]
    print(f"List: {numbers}")
    
    # TODO: Find the maximum number in the list WITHOUT using max().
    # Hint: Create a variable 'current_max' and set it to the first number.
    # Loop through the list; if you find a number bigger than 'current_max', update it.
    current_max = numbers[0]
    
    for num in numbers:
        if num > current_max:
            current_max = num
        else:
            pass
    print(f"Maximum Value: {current_max}")
