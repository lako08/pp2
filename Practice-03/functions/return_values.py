def add(a, b):
    return a + b

def get_min_max(numbers):
    return min(numbers), max(numbers)

def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

result = add(5, 3)
print(result)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")

double = create_multiplier(2)
print(double(10))