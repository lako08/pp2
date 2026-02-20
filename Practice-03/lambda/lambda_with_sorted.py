students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
words = ["apple", "Banana", "cherry", "Date"]

sorted_numbers = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
sorted_by_grade = sorted(students, key=lambda student: student["grade"])
sorted_by_name = sorted(students, key=lambda student: student["name"])

print(sorted_numbers)
print(sorted_desc)
print(sorted_by_grade)
print(sorted_by_name)
print(sorted(words, key=lambda word: word.lower()))