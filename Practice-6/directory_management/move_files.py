import shutil

# Перемещение файла
shutil.move("example.txt", "new_folder/example.txt")

# Переименование файла
import os
os.rename("new_folder/example.txt", "new_folder/renamed.txt")