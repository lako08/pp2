square = lambda x: x ** 2
add = lambda a, b: a + b
is_even = lambda x: x % 2 == 0

print(square(5))
print(add(3, 7))
print(is_even(4))
print(is_even(7))

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)