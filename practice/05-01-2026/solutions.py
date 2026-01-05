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
