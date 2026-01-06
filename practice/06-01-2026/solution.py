def exercise_easy_find_max():
    numbers = [14, 2, 9, 25, 6, 18]
    print(f"List: {numbers}")
    
    # TODO: Find the maximum number in the list WITHOUT using max().
    # Hint: Create a variable 'current_max' and set it to the first number.
    # Loop through the list; if you find a number bigger than 'current_max', update it.
    current_max = numbers[0]
    
    for num in numbers:
        if num > current_max:
            current_max = num
            
    print(f"Maximum Value: {current_max}")



def exercise_medium_palindrome():
    text = "racecar"
    print(f"Text: {text}")
    
    # TODO: Check if the string is a palindrome (reads the same forwards and backwards).
    # Expected Result: True
    # Hint: You can use string slicing [::-1] to get the reverse, then compare it to 'text'.
    is_palindrome = False
    l1 =[]
    for i in text:
        l1.append(i)

    if l1[::] == l1[::-1]:
        is_palindrome = True


    print(f"Is Palindrome?: {is_palindrome}")



def exercise_hard_prime_check():
    num = 17
    print(f"Number to check: {num}")
    
    # TODO: Check if 'num' is a Prime Number.
    # A prime number is greater than 1 and has no divisors other than 1 and itself.
    # Hint: Loop from 2 up to (num - 1). If (num % i == 0), it is NOT prime.
    # Don't forget to handle numbers < 2!
    is_prime = True
    
    if num < 2:
        is_prime = False
    else:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break

    print(f"Is Prime?: {is_prime}")


if __name__ == "__main__":
    print("--- Easy: Find Max ---")
    exercise_easy_find_max()
    print("\n--- Medium: Palindrome Check ---")
    exercise_medium_palindrome()
    print("\n--- Hard: Prime Checker ---")
    exercise_hard_prime_check()