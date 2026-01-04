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
                common.append(num)
    
    print(f"Common Elements: {common}")


def exercise_hard_rotate():
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(f"Original: {nums}, Rotate by: {k}")
    
    # TODO: Rotate the list to the right by k steps.
    # Expected Result: [4, 5, 1, 2, 3]
    # Hint: You can slice the list into two parts and swap them.
    # Part 1: The last k elements. Part 2: The rest.
    a = nums[:3]
    b = nums[3:]
    c = b + a
    rotated = c
    
    print(f"Rotated:  {rotated}")



if __name__ == "__main__":
    print("--- Easy: Vowel Count ---")
    exercise_easy_vowels()
    print("\n--- Medium: Common Elements ---")
    exercise_medium_common()
    print("\n--- Hard: Rotate List ---")
    exercise_hard_rotate()