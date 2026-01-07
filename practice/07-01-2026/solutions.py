def exercise_easy_count_target():
    numbers = [1, 5, 2, 5, 3, 5, 4]
    target = 5
    print(f"List: {numbers}, Target: {target}")
    
    # TODO: Count how many times 'target' appears in the list.
    # Hint: Loop through 'numbers' and compare each item to 'target'.
    count = 0
    
    for num in numbers:
        if num == target:
            count += 1

            
    print(f"Count: {count}")  



def exercise_medium_remove_duplicates():
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original: {numbers}")
    
    # TODO: Create a new list that contains only the unique numbers (no duplicates).
    # Hint: Create an empty list 'unique'. Loop through 'numbers'.
    # Only append the number to 'unique' IF it is not already in 'unique'.
    unique = []
    
    for num in numbers:
        if num in unique:
            pass
        else:
            unique.append(num)

    print(f"Unique List: {unique}")   