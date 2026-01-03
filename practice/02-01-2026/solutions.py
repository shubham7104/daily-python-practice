def exercise_1_squares():
    numbers = [1, 2, 3, 4, 5]
    print(f"Original: {numbers}")
    
    squares = []
    for i in numbers:
        squares.append(i**2) 
        
    print(f"Squared:  {squares}")


'''TEST'''
# exercise_1_squares()



def exercise_2_find_max():
    numbers = [10, 5, 20, 8, 15]
    print(f"List: {numbers}")
    
    # TODO: Find the largest number without using max()
    # Hint: Assume the first number is the largest, then loop to check others.
    largest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    else:
        pass

   
    print(f"Largest Number is: {largest}")



'''TEST'''
# exercise_2_find_max()



def exercise_3_reverse_words():
    sentence = "Hello World Python"
    print(f"Original: '{sentence}'")
    
    sentence = "Hello World Python"
    sentence_new = sentence.split()
    reverse_sentence = sentence_new[::-1]
    result = " ".join(reverse_sentence)
    
    print(f"Reversed: '{result}'")


'''TEST'''
# exercise_3_reverse_words()

if __name__ == "__main__":
    print("--- Exercise 1 ---")
    exercise_1_squares()
    print("\n--- Exercise 2 ---")
    exercise_2_find_max()
    print("\n--- Exercise 3 ---")
    exercise_3_reverse_words()

