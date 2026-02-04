n = int(input())
a = list(map(int, input().split()))

max_count = -1
result = a[0]

for i in range(n):
    count = 0
    for j in range(n):
        if a[i] == a[j]:
            count += 1
    if count > max_count or (count == max_count and a[i] < result):
        max_count = count
        result = a[i]

print(result)