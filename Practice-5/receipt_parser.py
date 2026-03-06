import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("Original text:")
print(text)

date = re.search(r"\d{4}-\d{2}-\d{2}", text)

if date:
    print("Date:", date.group())

numbers = re.findall(r"\d+", text)

print("Numbers:", numbers)

items = re.findall(r"([A-Za-z ]+)\s(\d+)", text)

print("Items and prices:")
for item, price in items:
    print(item.strip(), "-", price)