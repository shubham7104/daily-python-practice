def exercise_easy_sum_evens():
    numbers = [12, 7, 9, 14, 22, 5, 8]
    print(f"List: {numbers}")
    
    # TODO: Calculate the sum of all even numbers in the list.
    # Hint: Loop through the list and use 'if num % 2 == 0:' checks.
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
        else:
            pass
            
    print(f"Sum of Evens: {total}")



def exercise_medium_reverse_str():
    text = "stressed"
    print(f"Original: {text}")
    
    # TODO: Reverse the string WITHOUT using slicing (text[::-1]).
    # Hint: Create an empty string var. Loop through 'text' and add each char 
    # to the *beginning* of your new variable (e.g., new = char + new).
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text

    print(f"Reversed: {reversed_text}")