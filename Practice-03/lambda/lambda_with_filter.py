numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
greater_than_five = list(filter(lambda x: x > 5, numbers))

print(even_numbers)
print(odd_numbers)
print(greater_than_five)

words = ["apple", "banana", "cat", "dog", "elephant"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)