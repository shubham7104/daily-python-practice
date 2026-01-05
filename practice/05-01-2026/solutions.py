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



def exercise_hard_fibonacci():
    n = 10
    print(f"Generate first {n} Fibonacci numbers")
    
    # Generate a list of the first 'n' Fibonacci numbers.
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
    fib_sequence = [0, 1]
    
    # We already have the first 2 numbers, so we loop from 2 up to n
    for i in range(2, n):
        # Calculate next number: sum of the last two in the existing list
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    print(f"Sequence: {fib_sequence}")


if __name__ == "__main__":
    print("--- Easy: Sum Even Numbers ---")
    exercise_easy_sum_evens()
    print("\n--- Medium: Manual String Reverse ---")
    exercise_medium_reverse_str()
    print("\n--- Hard: Fibonacci Sequence ---")
    exercise_hard_fibonacci()