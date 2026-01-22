def count_vowels(text):
    total_vowel = 0
    text_new = text.lower()
    for i in text_new:
        if i in "aeiou":
            total_vowel += 1
    return total_vowel
print(f"Vowels in 'Apple': {count_vowels('Apple')}")