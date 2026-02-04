# Example 1: Basic comparisons
a = 10
b = 5
c = 10

print("Example 1:")
print(f"{a} > {b}: {a > b}")   # True
print(f"{a} < {b}: {a < b}")   # False
print(f"{a} == {c}: {a == c}") # True
print(f"{a} != {b}: {a != b}") # True

# Example 2: String comparisons
name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print("\nExample 2:")
print(f"{name1} == {name3}: {name1 == name3}")   # True
print(f"{name1} == {name2}: {name1 == name2}")   # False
print(f"{name1} != {name2}: {name1 != name2}")   # True 