def exercise_easy_vowels():
    text = "Python Programming is Fun"
    print(f"Text: '{text}'")
    
    # TODO: Count the number of vowels (a, e, i, o, u) in the text.
    # Hint: Loop through the string and check 'if char.lower() in "aeiou":'
    count = []
    for char in text:
        if char.lower() in "aeiou":
            count.append(char)
    
    print(f"Vowel Count: {len(count)}")



    