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
