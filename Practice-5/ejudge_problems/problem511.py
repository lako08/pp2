import re

text = input()

uppercase = re.findall(r"[A-Z]", text)
print(len(uppercase))