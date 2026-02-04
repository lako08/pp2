n=int(input())
s=input().split()
for i in range(n):
    s[i]=int(s[i])
max=max(s)
min=min(s)
for i in range(n):
    if s[i]==max:
        s[i]=min
for i in range(n):
    print(s[i], end=" ")