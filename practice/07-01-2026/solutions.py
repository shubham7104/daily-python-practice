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



def exercise_hard_factorial():
    n = 5
    print(f"Calculate factorial of: {n}")
    
    # TODO: Calculate n! (Factorial).
    # Definition: 5! = 1 * 2 * 3 * 4 * 5 = 120
    # Hint: Start with 'result = 1'. Loop from 1 up to (n + 1).
    # Multiply 'result' by the loop variable each time.
    result = 1
    
    for i in range(n+1):
        if i == 0:
            pass
        else:
            result *= i

    print(f"Factorial: {result}")


if __name__ == "__main__":
    print("--- Easy: Count Target ---")
    exercise_easy_count_target()
    print("\n--- Medium: Remove Duplicates ---")
    exercise_medium_remove_duplicates()
    print("\n--- Hard: Calculate Factorial ---")
    exercise_hard_factorial()    