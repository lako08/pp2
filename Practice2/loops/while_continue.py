# Example 1: Skip even numbers
print("Example 1: Odd numbers only")
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {number}")

# Example 2: Skip specific value
print("\nExample 2: Skip number 5")
count = 0
while count < 10:
    count += 1
    if count == 5:
        print("Skipping 5")
        continue
    print(f"Count: {count}")