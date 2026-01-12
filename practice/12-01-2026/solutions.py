def find_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
# --TEST--
# nums = [10, 20, 30, 40, 50]
# print(find_index(nums, 30)) # Should print 2
# print(find_index(nums, 99)) # Should print -1 



def get_even_numbers(numbers):
    even_no = []
    for num in numbers:
        if num % 2 == 0:
            even_no.append(num)
    return even_no

# --TEST--
# data = [1, 2, 3, 4, 5, 6]
# print(get_even_numbers(data))

def is_palindrome(word):
    is_palindrome = False
    if word[::] == word[::-1]:
        is_palindrome = True
    return is_palindrome

# --TEST--
# print(is_palindrome("racecar")) # Should print True
# print(is_palindrome("hello"))
