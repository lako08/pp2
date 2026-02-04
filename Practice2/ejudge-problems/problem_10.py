n=int(input())
s=input().split()
for i in range(n):
    s[i]=int(s[i])
a=sorted(s)
for i in range(n-1, -1, -1):
    print(a[i], end=" ")
