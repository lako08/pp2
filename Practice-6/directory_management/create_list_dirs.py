import os

# Создание папки
os.mkdir("new_folder")

# Создание вложенных папок
os.makedirs("parent/child")

# Список файлов и папок
files = os.listdir(".")
print(files)