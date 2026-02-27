def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

last = n if n % 2 == 0 else n - 1

for num in even_numbers_generator(n):
    if num == last:
        print(num, end="")
    else:
        print(num, end=",")
