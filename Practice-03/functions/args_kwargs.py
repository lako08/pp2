def sum_all(*args):
    return sum(args)

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def complex_function(*args, **kwargs):
    print(f"Arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print(sum_all(1, 2, 3, 4, 5))
print_person_info(name="Alice", age=30, city="New York")
complex_function(1, 2, 3, name="Bob", age=25)