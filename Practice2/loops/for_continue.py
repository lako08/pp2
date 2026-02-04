# Example 1: Skip vowels
print("Example 1: Consonants only")
word = "programming"
vowels = "aeiou"

for letter in word:
    if letter in vowels:
        continue
    print(letter)

# Example 2: Skip negative numbers
print("\nExample 2: Positive numbers only")
numbers = [5, -3, 2, -1, 0, 4, -2]

for num in numbers:
    if num <= 0:
        continue
    print(f"Positive number: {num}")