n = int(input())
arr = []
index_map = {}

for i in range(n):
    s = input()
    arr.append(s)
    if s not in index_map:
        index_map[s] = i + 1

unique_strings = sorted(set(arr))
for s in unique_strings:
    print(s, index_map[s])