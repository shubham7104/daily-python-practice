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