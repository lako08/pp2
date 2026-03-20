n = int(input())
keys = input().split()
values = input().split()
query = input().strip()

dictionary = dict(zip(keys, values))

if query in dictionary:
    print(dictionary[query])
else:
    print("Not found")