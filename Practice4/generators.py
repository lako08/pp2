def squares(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Enter N: "))

for num in squares(n):
    print(num)