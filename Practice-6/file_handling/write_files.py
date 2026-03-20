# Запись в файл (перезаписывает)
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")

# Добавление в файл
with open("example.txt", "a") as file:
    file.write("New line added\n")