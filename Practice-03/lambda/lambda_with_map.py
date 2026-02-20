numbers = [1, 2, 3, 4, 5]
celsius = [0, 20, 30, 40]

squared = list(map(lambda x: x ** 2, numbers))
cubed = list(map(lambda x: x ** 3, numbers))
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(squared)
print(cubed)
print(fahrenheit)

names = ["Alice", "Bob", "Charlie"]
name_lengths = list(map(lambda name: len(name), names))
print(name_lengths)