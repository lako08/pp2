# Чтение файла

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Чтение по строкам
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())