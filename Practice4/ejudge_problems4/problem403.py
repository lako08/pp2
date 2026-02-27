def divisible_by_3_and_4(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(input())

for num in divisible_by_3_and_4(n):
    print(num, end=" ")