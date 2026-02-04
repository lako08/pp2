# Example 1: Grade evaluation
score = 85

print("Example 1:")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Example 2: Time of day greeting
hour = 14  # 2 PM

print("\nExample 2:")
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
elif hour < 22:
    print("Good evening!")
else:
    print("Good night!")