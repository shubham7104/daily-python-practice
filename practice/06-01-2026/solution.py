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



def exercise_medium_palindrome():
    text = "racecar"
    print(f"Text: {text}")
    
    # TODO: Check if the string is a palindrome (reads the same forwards and backwards).
    # Expected Result: True
    # Hint: You can use string slicing [::-1] to get the reverse, then compare it to 'text'.
    is_palindrome = False
    l1 =[]
    for i in text:
        l1.append(i)

    if l1[::] == l1[::-1]:
        is_palindrome = True


    print(f"Is Palindrome?: {is_palindrome}")
