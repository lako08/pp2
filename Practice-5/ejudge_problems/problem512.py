import re

text = input()

sequences = re.findall(r"\d{2,}", text)
print(" ".join(sequences))