# Example 1: Countdown
print("Example 1: Countdown")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Example 2: Sum of numbers
print("\nExample 2: Sum of numbers")
total = 0
number = 1
while number <= 5:
    total += number
    print(f"Adding {number}, total: {total}")
    number += 1
print(f"Final total: {total}")