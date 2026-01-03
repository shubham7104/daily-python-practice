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