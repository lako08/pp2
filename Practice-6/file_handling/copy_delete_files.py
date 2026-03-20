import shutil
import os

# Копирование файла
shutil.copy("example.txt", "copy_example.txt")

# Удаление файла
os.remove("copy_example.txt")

# Проверка существования
if os.path.exists("example.txt"):
    print("File exists")