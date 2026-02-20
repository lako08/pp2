def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

def power(base, exponent=2):
    return base ** exponent

def display_info(*args):
    for arg in args:
        print(arg)

introduce("Bob", 25)
introduce(age=30, name="Charlie")
print(power(3))
print(power(3, 3))
display_info(1, 2, 3, 4, 5)