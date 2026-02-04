# Example 1: Break when found
print("Example 1: Find first even number")
numbers = [1, 3, 5, 8, 9, 11, 14]

for num in numbers:
    if num % 2 == 0:
        print(f"Found first even number: {num}")
        break
    print(f"Checking {num}...")

# Example 2: Break in nested loop
print("\nExample 2: Find pair that sums to 10")
for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 10:
            print(f"Found: {i} + {j} = 10")
            break  # Breaks only inner loop
    else:
        continue
    break  # Breaks outer loop too