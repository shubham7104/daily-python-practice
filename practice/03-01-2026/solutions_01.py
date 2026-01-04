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


def exercise_medium_common():
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    
    # TODO: Create a list containing only numbers found in BOTH lists.
    # Expected Result: [4, 5]
    common = []
    for num in list_a:
        for char in list_b:
            if num == char:
                comman.append(num)
    
    print(f"Common Elements: {common}")