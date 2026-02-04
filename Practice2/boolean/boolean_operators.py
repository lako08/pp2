# Example 1: and, or, not operators
a = True
b = False
c = True

print("Example 1:")
print(f"a and b: {a and b}")    # False
print(f"a or b: {a or b}")      # True
print(f"not a: {not a}")        # False
print(f"not b: {not b}")        # True
print(f"a and b or c: {a and b or c}")  # True

# Example 2: Combined expressions
x = 10
y = 20
z = 15

print("\nExample 2:")
print(f"(x < y) and (y > z): {(x < y) and (y > z)}")    # True
print(f"(x > y) or (y > z): {(x > y) or (y > z)}")      # True
print(f"not (x < y): {not (x < y)}")                    # False