n = int(input())
doc = {}
output_lines = []

for _ in range(n):
    parts = input().split()
    if parts[0] == "set":
        doc[parts[1]] = parts[2]
    elif parts[0] == "get":
        key = parts[1]
        if key in doc:
            output_lines.append(doc[key])
        else:
            output_lines.append(f"KE: no key {key} found in the document")

print("\n".join(output_lines))