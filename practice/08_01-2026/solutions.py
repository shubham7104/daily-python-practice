def exercise_easy_count_upper():
    text = "Hello World Python"
    print(f"Text: '{text}'")
    
    # TODO: Count how many Uppercase letters are in the text.
    # Hint: Loop through the string. Use 'if char.isupper():' to check.
    count = 0
    
    for char in text: 
        if char.isupper():
            count += 1
    
            
    print(f"Uppercase Count: {count}")



def exercise_medium_second_largest():
    numbers = [10, 20, 4, 45, 99]
    print(f"List: {numbers}")
    
    # TODO: Find the SECOND largest number in the list.
    # Hint: You can do this in two passes:
    # 1. Find the max number.
    # 2. Loop again and find the largest number that is NOT the max number.
    # (Or try to do it in one pass if you are feeling brave!)

    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    second_max = 0
    for num in numbers:
        if num > second_max and num != max_value:
            second_max = num

    print(f"Second Largest: {second_max}")


exercise_medium_second_largest()
