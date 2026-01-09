def bubble_sort(numbers,direction):
    n = len(numbers)
    for i in range(n):
        swapped = False

        
        for j in range(0, n-i-1):
            if direction == "asc":
                if numbers[j] > numbers [j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                    swapped = True

            elif direction == "desc":
                if numbers[j] < numbers [j+1]:
                    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
                    swapped = True
    if swapped == True:
        break

    
    return numbers



if __name__ == "__main__":
    # Test Case
    data = [3, 2, 1, 5, 4]
    
    print("Original:", data)
    print("Ascending:", bubble_sort(data, "asc"))
    
    # Note: 'data' is now sorted [1, 2, 3, 4, 5], so we re-sort that result
    print("Descending:", bubble_sort(data, "desc"))
