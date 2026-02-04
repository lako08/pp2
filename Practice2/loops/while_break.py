# Example 1: Break when condition met
print("Example 1:")
count = 1
while True:
    print(f"Count: {count}")
    if count == 5:
        print("Breaking at 5")
        break
    count += 1

# Example 2: Break with user input
print("\nExample 2:")
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    print(f"You entered: {user_input}")