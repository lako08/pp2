n = int(input())
if n <= 0:
    print("NO")
else:
    x = 1
    while x < n:
        x *= 2
    if x == n:
        print("YES")
    else:
        print("NO")